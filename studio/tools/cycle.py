#!/usr/bin/env python3
"""cycle.py — one finished book in hand at every launch.

    python3 studio/tools/cycle.py                 # the full report
    python3 studio/tools/cycle.py --status        # one line (SessionStart)
    python3 studio/tools/cycle.py --gate <book>   # exit 2: releasing <book> would break the cycle
    (from pr-lint.py on any [RELEASE] PR title)

WHY THIS EXISTS
The author, 2026-09-24: *"I wanna get into this long-term pattern where
I always have one book finished when we launched the previous book. For
me, the biggest failure mode is getting out of this cycle, so I'm
buffering upfront."*

He named it as his biggest failure mode, and cycles break silently. No
one decides to break one — a launch goes out with the next book at
two-thirds, or the book after next never starts because the buffer book
looks finished. So the rule is declared in `studio/CYCLE.md`, the
in-progress book's real count is read off its chapter headers, and a
release PR cannot open while the next book is incomplete. (L080)

This environment had already misread the plan once: it reported Book 1.1
as "blocked on admin" when it was being held on purpose. A declared cycle
is what stops the next thread making the same mistake.
"""
from __future__ import annotations
import os, pathlib, re, sys

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CYCLE = pathlib.Path(REPO, "studio", "CYCLE.md")
ACCEPTED = re.compile(r"\bACCEPTED\b")


def books() -> list[dict]:
    out = []
    if not CYCLE.exists():
        return out
    for line in CYCLE.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d+\.\d+)\s*\|", line)
        if not m:
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) < 6:
            continue
        planned = int(c[3]) if c[3].isdigit() else None
        out.append({"book": c[0], "dir": c[1].strip("`"), "status": c[2].upper(),
                    "planned": planned, "complete": c[4], "released": c[5]})
    return out


def accepted(b: dict) -> int | None:
    """Chapters whose header says ACCEPTED. A book marked HELD or RELEASED is complete."""
    if b["status"] in ("HELD", "RELEASED"):
        return b["planned"]
    if not b["dir"] or b["dir"] == "—":
        return 0
    d = pathlib.Path(REPO, b["dir"], "manuscript")
    if not d.is_dir():
        return 0
    n = 0
    for f in sorted(d.glob("ch[0-9][0-9].md")):
        head = f.read_text(encoding="utf-8")[:900]
        head = head.split("\n---\n", 1)[0]
        if ACCEPTED.search(head):
            n += 1
    return n


def readiness_open() -> list[str]:
    if not CYCLE.exists():
        return []
    return re.findall(r"^- \[ \] (.+)$", CYCLE.read_text(encoding="utf-8"), re.M)


def status_line() -> str:
    bs = books()
    if not bs:
        return ""
    parts = []
    for b in bs:
        if b["status"] == "NOT STARTED":
            parts.append(f"{b['book']} not started")
            continue
        if b["status"] in ("HELD", "RELEASED"):
            parts.append(f"{b['book']} {b['status']}")
            continue
        a, p = accepted(b), b["planned"]
        parts.append(f"{b['book']} {a}/{p} accepted" if p else f"{b['book']} {b['status']}")
    held = [b for b in bs if b["status"] == "HELD"]
    tail = ""
    if held:
        i = bs.index(held[0])
        nxt = bs[i + 1] if i + 1 < len(bs) else None
        if nxt and nxt["planned"]:
            tail = f" — {held[0]['book']} ships when {nxt['book']} reaches {nxt['planned']}/{nxt['planned']}"
    return "cycle: " + " · ".join(parts) + tail


def gate(book: str) -> int:
    bs = books()
    ids = [b["book"] for b in bs]
    if book not in ids:
        print(f"cycle: {book} is not in studio/CYCLE.md — declare it before releasing it", file=sys.stderr)
        return 2
    i = ids.index(book)
    if i + 1 >= len(bs):
        print(f"cycle: BLOCKED — nothing is declared after {book}. Releasing it would leave "
              f"no finished book in hand, which is the failure the author named.", file=sys.stderr)
        return 2
    nxt = bs[i + 1]
    a, p = accepted(nxt), nxt["planned"]
    if not p or a < p:
        print(f"cycle: BLOCKED — releasing {book} needs {nxt['book']} complete; it is at "
              f"{a}/{p or '?'} accepted.", file=sys.stderr)
        print("  The author, 2026-09-24: \"I always have one book finished when we launched "
              "the previous book… the biggest failure mode is getting out of this cycle.\"", file=sys.stderr)
        return 2
    print(f"cycle: {book} may release — {nxt['book']} is complete ({a}/{p}).")
    return 0


def report() -> int:
    bs = books()
    if not bs:
        print("cycle: no studio/CYCLE.md")
        return 0
    print("cycle  (studio/CYCLE.md)\n")
    for b in bs:
        a = accepted(b)
        prog = f"{a}/{b['planned']}" if b["planned"] else "—"
        print(f"  {b['book']:<5} {b['status']:<12} {prog:>7}   {b['dir']}")
    print()
    warn = []
    for i, b in enumerate(bs):
        if b["status"] != "HELD":
            continue
        nxt = bs[i + 1] if i + 1 < len(bs) else None
        after = bs[i + 2] if i + 2 < len(bs) else None
        if nxt and nxt["planned"]:
            a = accepted(nxt)
            print(f"  {b['book']} is held; it ships when {nxt['book']} is complete "
                  f"({a}/{nxt['planned']}, {100*a//nxt['planned']}%).")
            if a >= (2 * nxt["planned"]) // 3:
                open_items = readiness_open()
                if open_items:
                    warn.append(f"{nxt['book']} is past two-thirds and {len(open_items)} launch-readiness "
                                f"item(s) are open — these take calendar time, not writing time: "
                                + "; ".join(open_items))
                if after and after["status"] == "NOT STARTED":
                    warn.append(f"{after['book']} has not started. When {nxt['book']} completes and "
                                f"{b['book']} ships, {after['book']} is the buffer — the cycle "
                                f"breaks if it is not moving by then")
    for w in warn:
        print(f"  LEAD: {w}")
    return 0


def main() -> int:
    if "--status" in sys.argv:
        s = status_line()
        if s:
            print(s)
        return 0
    if "--gate" in sys.argv:
        i = sys.argv.index("--gate")
        return gate(sys.argv[i + 1] if len(sys.argv) > i + 1 else "")
    return report()


if __name__ == "__main__":
    sys.exit(main())
