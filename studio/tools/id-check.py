#!/usr/bin/env python3
"""id-check.py — a ledger ID or an author-note number is minted once, across threads.

    python3 studio/tools/id-check.py            # HEAD against every origin/* ref; exit 2 on a collision
    python3 studio/tools/id-check.py --next     # the next free L-id and note number across ALL refs
    (as a hook)  PreToolUse on Bash: runs only when the command is a `git push`

WHY THIS EXISTS
On 2026-09-21 two threads each added "the next row" to studio/lessons/
LEDGER.md and studio/AUTHOR-NOTES.md. Both picked L067 and 245 — one for
Kat's wine night, one for the thread-scope lock — because "last row plus
one" is computed against the branch you are on, and the other branch is
not on it. Nothing checked. The first sign would have been a merge
conflict in two files, resolved by whoever merged second, by hand, with
the losing thread's citations (L067 in six files) silently pointing at
the other thread's lesson. This reads every fetched origin/* ref and
refuses a push while an ID on HEAD is a different row on another ref.
(L069)

It does not fetch. guardrails.sh fetches before it runs; the hook judges
whatever refs the last fetch left, which is the same view the thread
worked from.
"""
from __future__ import annotations
import json, os, re, subprocess, sys

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LEDGER = "studio/lessons/LEDGER.md"
NOTES = "studio/AUTHOR-NOTES.md"


def git(*a) -> str:
    return subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True).stdout


def refs() -> list[str]:
    out = [l.strip() for l in git("for-each-ref", "--format=%(refname:short)", "refs/remotes/origin/").splitlines()]
    return [r for r in out if r and not r.endswith("/HEAD")]


def rows_at(ref: str, path: str, kind: str) -> dict[str, str]:
    """{id: the row's catch text} for LEDGER (L###) or NOTES (###)."""
    text = git("show", f"{ref}:{path}") if ref != "WORKTREE" else open(os.path.join(REPO, path), encoding="utf-8").read()
    out = {}
    for line in text.splitlines():
        if not line.startswith("| "):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        head = cells[0]
        if kind == "ledger" and re.fullmatch(r"L\d{3}(–L\d{3})?", head):
            out[head.split("–")[0]] = cells[3]           # the catch, short
        elif kind == "notes" and re.fullmatch(r"\d{3}", head):
            out[head] = cells[4] if len(cells) > 4 else cells[3]   # the author's words
    return out


def key(s: str) -> str:
    return re.sub(r"\W+", " ", s.lower()).strip()[:40]


def collisions():
    here = {"ledger": rows_at("WORKTREE", LEDGER, "ledger"), "notes": rows_at("WORKTREE", NOTES, "notes")}
    found = []
    for ref in refs():
        for kind, path in (("ledger", LEDGER), ("notes", NOTES)):
            theirs = rows_at(ref, path, kind)
            for i, mine in here[kind].items():
                if i in theirs and key(theirs[i]) != key(mine):
                    found.append((kind, i, ref, mine[:60], theirs[i][:60]))
    return found


def next_free():
    l, n = set(), set()
    for ref in ["WORKTREE"] + refs():
        l |= set(rows_at(ref, LEDGER, "ledger")); n |= set(rows_at(ref, NOTES, "notes"))
    li = max((int(x[1:]) for x in l), default=0) + 1
    ni = max((int(x) for x in n), default=0) + 1
    return f"L{li:03d}", f"{ni:03d}"


def main() -> int:
    if "--next" in sys.argv:
        L, N = next_free()
        print(f"id-check: next free across every ref — ledger {L}, author note {N}")
        return 0
    if not sys.stdin.isatty() and "--audit" not in sys.argv:
        try:
            payload = json.load(sys.stdin)
            cmd = (payload.get("tool_input") or {}).get("command") or ""
            if not re.search(r"\bgit\s+push\b", cmd):
                return 0
        except Exception:
            pass
    bad = collisions()
    if not bad:
        print("id-check: no ledger or note ID is a different row on another thread")
        return 0
    L, N = next_free()
    print("id-check: BLOCKED — an ID on this branch is a DIFFERENT row on another thread:", file=sys.stderr)
    for kind, i, ref, mine, theirs in bad:
        print(f"  {i} ({kind})  here: {mine!r}\n        {ref}: {theirs!r}", file=sys.stderr)
    print(f"  Renumber yours (next free across every ref: ledger {L}, note {N}) and fix every file that cites it.", file=sys.stderr)
    print("  Two threads minting the same number is how a lesson ends up pointing at somebody else's catch. (L069)", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
