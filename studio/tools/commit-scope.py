#!/usr/bin/env python3
"""commit-scope.py — one commit, one scope (CLAUDE.md, "Working on a book").

PreToolUse hook on Bash. For every `git commit` in the command line, the
files that commit would carry — the index as it stands, plus whatever the
same line `git add`s before that commit — must belong to exactly one
scope, and the subject's prefix must name it:

    books/<book>/…                     → "<book>:"   (campus-series → campus)
    .claude/agents, .claude/skills,
    studio/agents                      → "agents:"
    everything else                    → "studio:"

A line with three scoped commits in a row passes. A `git commit` quoted
inside a heredoc is text, not a commit. Exit 2 blocks and says which
files sit in which scope; exit 0 passes; any other command passes.
The token --allow-mixed-scope anywhere in the command is the override,
and it is visible in the transcript.

Why a hook: the rule sat in CLAUDE.md as an instruction and the
showrunner broke it on 2026-09-19 (a campus+studio commit, split by
hand). On its first live day it blocked the showrunner twice more —
once rightly, once on its own bugs (a compound line read as one commit;
a heredoc read as a command). (L033)
"""
from __future__ import annotations
import json, os, re, shlex, subprocess, sys

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BOOK_PREFIX = {"campus-series": "campus"}


def scope_of(path: str) -> str:
    p = re.sub(r"^\./", "", path.replace("\\", "/"))
    m = re.match(r"books/([^/]+)/", p)
    if m:
        return BOOK_PREFIX.get(m.group(1), m.group(1))
    if p.startswith((".claude/agents/", ".claude/skills/", "studio/agents/")):
        return "agents"
    return "studio"


def git(*a):
    return subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True).stdout.splitlines()


def add_paths(seg: str) -> set[str]:
    try:
        toks = shlex.split(seg)
    except ValueError:
        toks = seg.split()
    args = [t for t in toks[2:] if not t.startswith("-")]
    if any(t in ("-A", "--all") for t in toks) or "." in args:
        return {l[3:] for l in git("status", "--porcelain") if l.strip()}
    out: set[str] = set()
    for a in args:
        if os.path.isdir(os.path.join(REPO, a)):
            out |= {x[3:] for x in git("status", "--porcelain", "--", a) if x.strip()}
        else:
            out.add(a)
    return out


def strip_heredocs(command: str) -> str:
    return re.sub(r"<<-?\s*['\"]?(\w+)['\"]?[^\n]*\n.*?\n\1[ \t]*(?=\n|$)", " ", command, flags=re.S)


def commits_in(command: str) -> list[tuple[str, list[str]]]:
    pending: set[str] = set(git("diff", "--cached", "--name-only"))
    out = []
    for seg in re.split(r"&&|;|\|\||\n", strip_heredocs(command)):
        seg = seg.strip()
        if re.match(r"git\s+add\b", seg):
            pending |= add_paths(seg)
        elif re.match(r"git\s+commit\b", seg):
            files = set(pending)
            if re.search(r"\s-a\b|\s-am\b|\s--all\b", seg):
                files |= set(git("diff", "--name-only"))
            out.append((seg, sorted(f for f in files if f)))
            pending = set()
    return out


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    cmd = (payload.get("tool_input") or {}).get("command") or ""
    if not re.search(r"\bgit\s+commit\b", cmd) or "--allow-mixed-scope" in cmd:
        return 0
    problems = []
    for seg, files in commits_in(cmd):
        if not files:
            continue
        scopes: dict[str, list[str]] = {}
        for f in files:
            scopes.setdefault(scope_of(f), []).append(f)
        m = re.search(r"-m\s+(?:\"([^\"]*)|'([^']*)|(\S+))", seg)
        msg = (m.group(1) or m.group(2) or m.group(3) or "") if m else ""
        prefix = msg.split(":", 1)[0].strip().lower() if ":" in msg else ""
        only = next(iter(scopes))
        if len(scopes) > 1:
            problems.append("a commit spans " + ", ".join(f"{k} ({len(v)} file{'s' if len(v) > 1 else ''})" for k, v in scopes.items()))
            for k, v in scopes.items():
                problems.append(f"  {k}: " + ", ".join(v[:6]) + (" …" if len(v) > 6 else ""))
            problems.append("one commit = one book or studio or agents (CLAUDE.md). Split it: git add <one scope> && git commit; then the next.")
        elif prefix and prefix != only:
            problems.append(f"the message prefix is '{prefix}:' but every file is in scope '{only}' — prefix the subject with '{only}:'")
        elif not prefix:
            problems.append(f"no scope prefix on the subject — start it with '{only}:'")
    if problems:
        print("commit-scope: BLOCKED — " + problems[0], file=sys.stderr)
        for p in problems[1:]:
            print("  " + p, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
