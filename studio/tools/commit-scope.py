#!/usr/bin/env python3
"""commit-scope.py — one commit, one scope (CLAUDE.md, "Working on a book").

PreToolUse hook on Bash. If the command runs `git commit`, the files it
commits (already staged, plus whatever the same command `git add`s) must
belong to exactly one scope, and the message prefix must name it:

    books/<book>/…                     → "<book>:"   (campus-series → campus)
    .claude/agents, .claude/skills,
    studio/agents                      → "agents:"
    everything else                    → "studio:"

Exit 2 blocks the commit and says which files are in which scope. Exit
0 lets it through. Any other command passes untouched.

Why a hook: the rule sat in CLAUDE.md as an instruction and was broken
by the showrunner on 2026-09-19 (a campus+studio commit, split by hand
after the fact). The doc's test — "if the agent ignored this forty
minutes into a long session, how bad would it be?" — answered: a fold
PR mixing book canon and studio tooling that the author cannot merge
one without the other. (L033)
"""
from __future__ import annotations
import json, os, re, shlex, subprocess, sys

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BOOK_PREFIX = {"campus-series": "campus"}


def scope_of(path: str) -> str:
    p = path.replace("\\", "/").lstrip("./")
    m = re.match(r"books/([^/]+)/", p)
    if m:
        b = m.group(1)
        return BOOK_PREFIX.get(b, b)
    if p.startswith((".claude/agents/", ".claude/skills/", "studio/agents/")):
        return "agents"
    return "studio"


def git(*a):
    return subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True).stdout.splitlines()


def files_for(command: str) -> list[str]:
    files = set(git("diff", "--cached", "--name-only"))
    # paths named by `git add …` earlier in the same command line
    for seg in re.split(r"&&|;|\|\|", command):
        seg = seg.strip()
        if not re.match(r"git\s+add\b", seg):
            continue
        try:
            toks = shlex.split(seg)
        except ValueError:
            toks = seg.split()
        args = [t for t in toks[2:] if not t.startswith("-")]
        if any(t in ("-A", "--all") for t in toks) or "." in args:
            files |= {l[3:] for l in git("status", "--porcelain") if l.strip()}
            continue
        for a in args:
            ap = os.path.join(REPO, a)
            if os.path.isdir(ap):
                files |= {x[3:] for x in git("status", "--porcelain", "--", a) if x.strip()}
            else:
                files.add(a)
    if re.search(r"git\s+commit\b[^&;|]*\s-a\b", command) or re.search(r"git\s+commit\b[^&;|]*\s-am\b", command):
        files |= set(git("diff", "--name-only"))
    return sorted(f for f in files if f)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    cmd = (payload.get("tool_input") or {}).get("command") or ""
    if not re.search(r"\bgit\s+commit\b", cmd):
        return 0
    if "--allow-mixed-scope" in cmd or os.environ.get("COMMIT_SCOPE_OFF") == "1":
        return 0
    files = files_for(cmd)
    if not files:
        return 0
    scopes = {}
    for f in files:
        scopes.setdefault(scope_of(f), []).append(f)
    m = re.search(r"-m\s+(?:\"([^\"]*)|'([^']*)|(\S+))", cmd)
    msg = (m.group(1) or m.group(2) or m.group(3) or "") if m else ""
    prefix = msg.split(":", 1)[0].strip().lower() if ":" in msg else ""
    problems = []
    if len(scopes) > 1:
        problems.append("this commit spans " + ", ".join(f"{k} ({len(v)} file{'s' if len(v)>1 else ''})" for k, v in scopes.items()))
        for k, v in scopes.items():
            problems.append(f"  {k}: " + ", ".join(v[:6]) + (" …" if len(v) > 6 else ""))
        problems.append("one commit = one book or studio or agents (CLAUDE.md). Split it: git add <one scope> && git commit; then the next.")
    elif prefix and prefix != next(iter(scopes)):
        problems.append(f"the message prefix is '{prefix}:' but every file is in scope '{next(iter(scopes))}' — prefix the subject with '{next(iter(scopes))}:'")
    elif not prefix:
        problems.append(f"no scope prefix on the subject — start it with '{next(iter(scopes))}:'")
    if problems:
        print("commit-scope: BLOCKED — " + problems[0], file=sys.stderr)
        for p in problems[1:]:
            print("  " + p, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
