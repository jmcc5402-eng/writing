#!/usr/bin/env python3
"""thread-scope.py — a branch scoped to the environment cannot touch the story.

    (as a hook)  PreToolUse on Edit|Write|MultiEdit, Bash and Agent.
                 Reads the hook JSON on stdin. Looks up the current
                 branch in studio/threads/SCOPES.md. On an
                 `environment` branch it refuses (exit 2):
                   - an Edit/Write whose file_path is story (any
                     books/ path outside canon/ and CHANGELOG.md)
                   - a Bash command that mutates a story path (a
                     redirection, sed -i, mv, cp, rm, tee, git add/rm/
                     mv/restore/checkout -- on it), or that sweeps the
                     tree (git add -A / . / --all; git commit -a with
                     story files modified)
                   - an Agent launch of a drafter, a line editor or a
                     plot architect
    python3 studio/tools/thread-scope.py --show     prints the branch and its scope
    STUDIO_THREAD_SCOPE=environment  overrides the table for one shell
    --unlock-thread-scope            anywhere in a Bash command lets that one
                                     command through; it is visible in the transcript

WHY THIS EXISTS
The author (2026-09-21): "I need an engine to hyper focus on the
environment. The other thread always reverts to the story." A thread
told to build guardrails drifts to fixing the page, because the page
is right there and the fix is satisfying. That is an instruction
failing in the usual way. This is the same rule as a lock: the thread
can build the check and cannot apply the fix, so the fix goes to the
book thread by the board and the check gets built. (L067)

Known hole: a script that writes a story file from inside python or a
heredoc is not parsed. The commit-scope hook and the PR diff are the
second line.
"""
from __future__ import annotations
import fnmatch, json, os, re, shlex, subprocess, sys

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SCOPES = os.path.join(REPO, "studio", "threads", "SCOPES.md")

# What an environment branch may write under books/. Everything else under
# books/ is story. Outside books/ everything is environment.
BOOK_OPEN = (r"books/[^/]+/(?:[^/]+/)*canon/", r"books/[^/]+/(?:[^/]+/)*CHANGELOG\.md$")
DENIED_AGENTS = ("drafting-assistant", "line-copy-editor", "plot-architect")
MUTATORS = re.compile(r"(?:^|[\s;&|(])(?:sed\s+-i|mv|cp|rm|tee|truncate|git\s+(?:add|rm|mv|restore|checkout\s+--))\b")


def branch() -> str:
    try:
        return subprocess.run(["git", "-C", REPO, "rev-parse", "--abbrev-ref", "HEAD"],
                              capture_output=True, text=True, timeout=5).stdout.strip()
    except Exception:
        return ""


def scope_rows() -> list[tuple[str, str]]:
    out = []
    try:
        lines = open(SCOPES, encoding="utf-8").read().splitlines()
    except OSError:
        return out
    in_branches = False
    for line in lines:
        if line.startswith("## "):
            in_branches = line.strip("# ").lower().startswith("branches")
            continue
        if not in_branches or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not cells[0].startswith("`"):
            continue
        out.append((cells[0].strip("`"), cells[1].strip("`").lower()))
    return out


def scope_of(br: str) -> str:
    env = os.environ.get("STUDIO_THREAD_SCOPE")
    if env:
        return env.strip().lower()
    for pat, sc in scope_rows():
        if fnmatch.fnmatchcase(br, pat):
            return sc
    return "story"


def rel(path: str) -> str:
    p = path.replace("\\", "/")
    if os.path.isabs(p):
        try:
            p = os.path.relpath(p, REPO)
        except ValueError:
            return p
    return re.sub(r"^(\./)+", "", p)


def is_story(path: str) -> bool:
    p = rel(path)
    if p.startswith("../"):
        return False
    if not re.match(r"books/[^/]+/.+", p):
        return False
    return not any(re.match(rx, p) for rx in BOOK_OPEN)


def block(msg: str, br: str) -> int:
    print(f"thread-scope: BLOCKED — branch '{br}' is scoped 'environment' (studio/threads/SCOPES.md).", file=sys.stderr)
    print(f"  {msg}", file=sys.stderr)
    print("  This thread builds the check; the page fix belongs to the book thread. Put the fix on the board", file=sys.stderr)
    print("  (the book's BACKLOG or the open PR) and build the enforcer here. To change the scope, edit the row and say why.", file=sys.stderr)
    return 2


def check_edit(ti: dict, br: str) -> int:
    fp = ti.get("file_path") or ti.get("path") or ""
    if fp and is_story(fp):
        return block(f"{rel(fp)} is story (a manuscript, brief, card, note or bible).", br)
    return 0


def git(*a) -> list[str]:
    return subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True).stdout.splitlines()


def check_bash(ti: dict, br: str) -> int:
    cmd = ti.get("command") or ""
    if "--unlock-thread-scope" in cmd:
        return 0
    # Strip heredoc BODIES only. The first line stays, so `cat <<EOF > ch05.md`
    # still shows its redirection onto a story path.
    body = re.sub(r"(<<-?\s*['\"]?(\w+)['\"]?[^\n]*)\n.*?\n\2[ \t]*(?=\n|$)", r"\1", cmd, flags=re.S)
    for seg in re.split(r"&&|;|\|\||\n", body):
        seg = seg.strip()
        if not seg:
            continue
        if re.match(r"git\s+add\b", seg) and (re.search(r"\s(-A|--all)\b", seg) or re.search(r"\s\.(\s|$)", seg)):
            return block("git add -A / . sweeps the working tree; on an environment branch name the files (studio/…, .claude/…).", br)
        if re.match(r"git\s+commit\b", seg) and re.search(r"\s-a\b|\s-am\b|\s--all\b", seg):
            story = [f for f in git("diff", "--name-only") if is_story(f)]
            if story:
                return block("git commit -a would carry story files: " + ", ".join(story[:4]) + (" …" if len(story) > 4 else ""), br)
        try:
            toks = shlex.split(seg)
        except ValueError:
            toks = seg.split()
        story_toks = [t for t in toks if "books/" in t and is_story(t.split("=", 1)[-1])]
        if story_toks and (MUTATORS.search(" " + seg) or ">" in seg):
            return block(f"the command writes to {rel(story_toks[0])}.", br)
    return 0


def check_agent(ti: dict, br: str) -> int:
    kind = (ti.get("subagent_type") or "").lower()
    if any(d in kind for d in DENIED_AGENTS):
        return block(f"'{kind}' writes prose or outlines. An environment thread launches readers and the environment-engineer, never a drafter.", br)
    return 0


def main() -> int:
    br = branch()
    sc = scope_of(br)
    if "--show" not in sys.argv:
        try:
            payload = json.load(sys.stdin)
        except Exception:
            return 0
        if sc != "environment":
            return 0
        tool = payload.get("tool_name") or ""
        ti = payload.get("tool_input") or {}
        if "command" in ti and (tool in ("", "Bash")):
            return check_bash(ti, br)
        if "subagent_type" in ti:
            return check_agent(ti, br)
        if "file_path" in ti or "path" in ti:
            return check_edit(ti, br)
        return 0
    print(f"thread-scope: branch '{br}' → scope '{sc}'" + ("" if sc != "environment" else "  (locked: manuscripts, plots, cards, notes; no drafters)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
