#!/usr/bin/env python3
"""stakes-check.py — is the threat ever CHARGED, or only ever stated?

    python3 studio/tools/stakes-check.py books/campus-series/book2
    python3 studio/tools/stakes-check.py <book> --gate <ch>

Exit 0 = the pressure curve has shape. Exit 2 = the antagonist is weather.

WHY THIS EXISTS
The author, merging #185 (2026-09-23): *"But not only do we need to say
the stakes, the stakes need to be high."*

Every instrument in this studio asks whether the stake is SAID. The
author's seventh question (POINT) asks "what exactly happens if" — said
on the page, blatantly. Nothing asks whether it is ever COLLECTED, and a
threat that is named for twenty chapters and never acts reads as low
however plainly it is stated.

Two things are measurable, and neither of them judges the story:

  THE PRESSURE CURVE  `canon/TARGETS.md` scores Menace 0-3 per chapter,
      where 3 is "he moves". Book 1.2 plans Menace at 0 or 1 in TWENTY
      of thirty chapters; the antagonist moves in six. A threat that
      acts a fifth of the time is weather.

  THE UNPAID BILL     the matrix has a `Pays` column — who loses
      something this chapter — and `targets-check.py` says, in its own
      docstring, "Pays is recorded, not judged." It is the one column
      that measures whether a stake was actually charged and the one
      column no gate verifies. The ch 24 developmental score found
      exactly the failure that allows: *"the cost is felt, never paid
      — nothing is taken from Dan today."*

This tool reports the curve and the bill. It does not decide whether a
stake is "high" — that is a reader's judgement and it stays one. What it
refuses to let happen is a book where nobody notices the villain has not
moved since chapter nine. (L078)
"""
from __future__ import annotations
import os, pathlib, re, sys

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
COLS = ["ch", "pov", "romance", "heat", "aisha", "dan", "wound", "fun",
        "town", "menace", "ends", "talk", "words", "pays"]
MOVES_FLOOR = 0.25     # share of chapters where the antagonist must MOVE (menace 3)
QUIET_RUN = 5          # consecutive chapters at menace <= 1 before it is a finding


def rows(book: pathlib.Path) -> list[dict]:
    f = book / "canon" / "TARGETS.md"
    if not f.exists():
        return []
    out = []
    for line in f.read_text(encoding="utf-8").splitlines():
        if not re.match(r"\|\s*\d+\s*\|", line):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) < len(COLS):
            continue
        r = dict(zip(COLS, c[:len(COLS)]))
        try:
            r["ch"] = int(re.search(r"\d+", r["ch"]).group(0))
            r["menace"] = int(re.search(r"\d", r["menace"]).group(0))
        except (AttributeError, ValueError):
            continue
        out.append(r)
    return sorted(out, key=lambda r: r["ch"])


def longest_quiet(rs: list[dict]) -> tuple[int, int, int]:
    best = cur = 0
    start = best_start = rs[0]["ch"] if rs else 0
    for r in rs:
        if r["menace"] <= 1:
            if cur == 0:
                start = r["ch"]
            cur += 1
            if cur > best:
                best, best_start = cur, start
        else:
            cur = 0
    return best, best_start, best_start + best - 1


def report(book: pathlib.Path) -> int:
    rs = rows(book)
    if not rs:
        print(f"stakes-check: no readable canon/TARGETS.md under {book}")
        return 0
    n = len(rs)
    moves = [r for r in rs if r["menace"] == 3]
    quiet, q0, q1 = longest_quiet(rs)
    dist = {k: sum(1 for r in rs if r["menace"] == k) for k in range(4)}

    print(f"stakes-check  ({n} chapters)\n")
    print("  the pressure curve — Menace by chapter (0 absent · 1 a name · 2 in the room · 3 he MOVES)")
    line = "".join(str(r["menace"]) for r in rs)
    print(f"    ch{rs[0]['ch']:<3}{line}  ch{rs[-1]['ch']}")
    print(f"    distribution: " + " · ".join(f"{k}:{v}" for k, v in dist.items()))
    print(f"    he MOVES in {len(moves)} of {n} chapters ({100*len(moves)/n:.0f}%)"
          + (f" — {', '.join('ch'+str(r['ch']) for r in moves)}" if moves else ""))

    payers = [r["pays"] for r in rs if r["pays"] not in ("", "—")]
    print(f"\n  the bill — who loses something, per chapter")
    from collections import Counter
    for who, c in Counter(payers).most_common():
        print(f"    {who:<12} {c:2d} chapter(s)")
    print(f"    {n - len(payers)} chapter(s) name nobody")

    bad = []
    if len(moves) / n < MOVES_FLOOR:
        bad.append(f"the antagonist MOVES in only {100*len(moves)/n:.0f}% of chapters "
                   f"(floor {100*MOVES_FLOOR:.0f}%) — he is weather, not a threat")
    if quiet >= QUIET_RUN:
        bad.append(f"ch {q0}-{q1} is {quiet} chapters running at Menace 1 or less — "
                   f"the longest stretch where nothing presses")
    print()
    if not bad:
        print("  The curve has shape. Whether the stake is HIGH is still a reader's call;")
        print("  this only proves it is not purely notional.")
        return 0
    for b in bad:
        print(f"  FINDING: {b}")
    print()
    print("  The author, 2026-09-23: \"not only do we need to say the stakes, the stakes")
    print("  need to be high.\" A stake that is stated every chapter and collected in a")
    print("  handful reads low however blatantly it is said. This is the measurable half;")
    print("  the reader judges the rest.")
    return 2


def gate(book: pathlib.Path, ch_raw: str) -> int:
    """At the accept gate: name the bill this chapter owes."""
    ch = int(re.sub(r"^ch", "", str(ch_raw)))
    rs = rows(book)
    row = next((r for r in rs if r["ch"] == ch), None)
    if not row:
        return 0
    if row["pays"] in ("", "—"):
        return 0
    print(f"  stakes: ch {ch} plans Pays {row['pays']}, Menace {row['menace']}. The score file")
    print(f"          must name what {row['pays']} actually LOST on the page, with a line —")
    print(f"          'recorded' is not 'charged' (L078).")
    return 0


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    book = pathlib.Path(args[0]).resolve() if args else pathlib.Path(REPO, "books/campus-series/book2")
    if "--first" in sys.argv:
        i = sys.argv.index("--first")
        n = int(sys.argv[i + 1])
        rs = rows(book)[:n]
        if not rs:
            print("stakes-check: nothing to read"); return 0
        quiet = sum(1 for r in rs if r["menace"] <= 1)
        print(f"  stakes (first {len(rs)} chapters): Menace " +
              "".join(str(r["menace"]) for r in rs) +
              f" — {quiet} of {len(rs)} at 1 or less")
        if quiet == len(rs):
            print("  FINDING: nothing presses anywhere in the opening. This is the")
            print("  stretch a reader downloads free. Book 1.2 ran seven consecutive")
            print("  chapters at Menace 1 or less and nobody saw it until ch 24. (L079)")
            return 2
        return 0
    if "--gate" in sys.argv:
        i = sys.argv.index("--gate")
        return gate(book, sys.argv[i + 1] if len(sys.argv) > i + 1 else args[-1])
    return report(book)


if __name__ == "__main__":
    sys.exit(main())
