#!/usr/bin/env python3
"""handoff.py — findings ride into the other thread's context, not a chat message.

    python3 studio/tools/handoff.py                     # rows for THIS thread's scope
    python3 studio/tools/handoff.py --for story         # rows for a named scope
    python3 studio/tools/handoff.py --gate <book> <ch>  # exit 2 on a BLOCK for that chapter
    python3 studio/tools/handoff.py --audit             # every open row (guardrails.sh)
    python3 studio/tools/handoff.py --next              # the next free H-id
    (SessionStart)  --quiet: print only when there is something open

WHY THIS EXISTS
Two threads work this repo: one writes the book, one builds the checks.
The environment thread keeps finding things only the book thread can act
on — a rhythm that has been flat for seven chapters, two rules that
contradict each other — and until now the only way across was the author
pasting a PR link into the other conversation.

That is a handoff that depends on a human remembering, which is the
failure this studio already had: the superfan reviewer stopped running
because a thread forgot, and nothing reported it. A pull request is the
AUTHOR's channel — one decision, merge is the record. It is the wrong
pipe between two agents.

So a finding is a row in studio/threads/HANDOFF.md, and it arrives the
way roster-staleness does: printed into the thread's context the moment
it opens, whether or not anybody asks. A row the author has raised to
BLOCK also holds the chapter's accept gate. (L070)

Only the author may set BLOCK, and the row must carry the ruling. An
agent thread that could hand itself a veto over another thread's work
would eventually use it.
"""
from __future__ import annotations
import os, re, subprocess, sys

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BOARD = os.path.join(REPO, "studio", "threads", "HANDOFF.md")
FIELDS = ["id", "for", "chapter", "severity", "finding", "detail", "status"]
RULED = re.compile(r"\bauthor\b[^|]*\b(20\d\d-\d\d-\d\d|#\d+)", re.I)


def rows() -> list[dict]:
    out = []
    try:
        text = open(BOARD, encoding="utf-8").read()
    except OSError:
        return out
    for line in text.splitlines():
        if not re.match(r"\|\s*H\d{3}\s*\|", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < len(FIELDS):
            continue
        out.append(dict(zip(FIELDS, cells)))
    return out


def scope_here() -> str:
    """This thread's scope, from the same table thread-scope.py reads."""
    ts = os.path.join(REPO, "studio", "tools", "thread-scope.py")
    try:
        out = subprocess.run([sys.executable, ts, "--show"], capture_output=True, text=True, timeout=10).stdout
        m = re.search(r"→ scope '(\w+)'", out)
        return m.group(1) if m else "story"
    except Exception:
        return "story"


def chapter_of(r: dict) -> str | None:
    m = re.search(r"\d+", r["chapter"])
    return f"{int(m.group(0)):02d}" if m else None


def show(scope: str, quiet: bool) -> int:
    open_rows = [r for r in rows() if r["status"].upper().startswith("OPEN")]
    mine = [r for r in open_rows if r["for"].lower() == scope.lower()]
    if not mine:
        if not quiet:
            print(f"handoff: nothing open for the '{scope}' thread")
        return 0
    order = {"BLOCK": 0, "FIX": 1, "NOTE": 2}
    mine.sort(key=lambda r: order.get(r["severity"].upper(), 9))
    print(f"handoff  ({len(mine)} open for the '{scope}' thread — studio/threads/HANDOFF.md)\n")
    for r in mine:
        ch = f"  ch {chapter_of(r)}" if chapter_of(r) else ""
        print(f"  [{r['severity'].upper():<5}] {r['id']}{ch}  {r['finding']}")
        print(f"          → {r['detail']}")
    print("\n  Act on a row and set its Status in the same commit, naming the ID.")
    print("  Disagree by setting WONTFIX with a reason — in the file, not in chat.")
    return 0


def gate(book: str, ch_raw: str) -> int:
    ch = f"{int(re.sub(r'^ch', '', str(ch_raw))):02d}"
    held, soft = [], []
    for r in rows():
        if not r["status"].upper().startswith("OPEN"):
            continue
        rc = chapter_of(r)
        if rc and rc != ch:
            continue
        sev = r["severity"].upper()
        if sev == "BLOCK":
            if RULED.search(r["detail"]):
                held.append(r)
            else:
                soft.append((r, "BLOCK not honoured — no author ruling in Detail; treated as FIX"))
        elif sev == "FIX" and rc:
            soft.append((r, None))
    for r, why in soft:
        print(f"handoff: FIX open for ch {ch} — {r['id']}: {r['finding'][:90]}")
        if why:
            print(f"         {why}")
    if not held:
        return 0
    print(f"handoff: BLOCKED — ch {ch} has {len(held)} row(s) the author set to BLOCK:", file=sys.stderr)
    for r in held:
        print(f"    {r['id']}  {r['finding']}", file=sys.stderr)
        print(f"          → {r['detail']}", file=sys.stderr)
    print("  Do the work and set Status to DONE, or set WONTFIX with a reason.", file=sys.stderr)
    return 2


def main() -> int:
    a = sys.argv[1:]
    if "--next" in a:
        n = max((int(r["id"][1:]) for r in rows()), default=0) + 1
        print(f"handoff: next free id H{n:03d}")
        return 0
    if "--audit" in a:
        op = [r for r in rows() if r["status"].upper().startswith("OPEN")]
        if not op:
            print("handoff: no open rows")
            return 0
        print(f"handoff: {len(op)} open — " + ", ".join(f"{r['id']}({r['severity']}→{r['for']})" for r in op))
        return 0
    if "--gate" in a:
        i = a.index("--gate")
        if len(a) < i + 3:
            print("usage: handoff.py --gate <book-dir> <chapter>", file=sys.stderr)
            return 1
        return gate(a[i + 1], a[i + 2])
    scope = a[a.index("--for") + 1] if "--for" in a and len(a) > a.index("--for") + 1 else scope_here()
    return show(scope, "--quiet" in a)


if __name__ == "__main__":
    sys.exit(main())
