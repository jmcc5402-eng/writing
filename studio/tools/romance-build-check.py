#!/usr/bin/env python3
"""Check a relationship arc doc's ladder table: does the romance BUILD?

The build check (author, 2026-09-05, studio/PIPELINE.md §3b and
studio/STYLE.md "Romance first"): the romance floor counts beats
inside a chapter; nothing counted the steps across the book, so ch 8
of Book 1.2 passed the count and the author still asked "have we
earned the right for Dan to think he wants her?" This is the check
that reads the whole ladder at once.

    python3 studio/tools/romance-build-check.py ARC-DOC.md

The doc carries one table with these columns, in this order (see
studio/series-kit/11-arc-docs.md):

    | Ch | In | Out | Rung on the page | Spends | Earned by | Hole |

  In / Out   the inside stage and the outside stage this chapter
             reaches (1 hidden, 2 admitted inside, 3 shown between
             them, 4 seen, 5 public)
  Rung       the thing the two of them DO in this chapter, or —
  Spends     blank, or one of: want, kiss, claim (the three moves
             that must be earned)
  Earned by  chapter numbers of the earlier scenes that earn it

Rules, each one a FAIL:
  1. A stage never goes backward.
  2. The inside may lead the outside by ONE stage, never more.
  3. A stage never jumps by more than one between chapters.
  4. A spend lists at least TWO earlier chapters, each with a rung
     on the page (not —).
The Hole column is reported as a WARN so nobody forgets it.
Exit code 1 on any FAIL.
"""
import re
import sys

COLS = ["ch", "in", "out", "rung", "spends", "earned", "hole"]
SPENDS = {"want", "kiss", "claim"}


def parse(path):
    rows = []
    for line in open(path, encoding="utf-8"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 7 or not re.fullmatch(r"\d+", cells[0]):
            continue
        r = dict(zip(COLS, cells))
        r["ch"] = int(r["ch"])
        r["in"], r["out"] = int(r["in"]), int(r["out"])
        r["spends"] = r["spends"].strip("—- ").lower()
        r["earned"] = [int(x) for x in re.findall(r"\d+", r["earned"])]
        rows.append(r)
    return rows


def check(rows):
    fails, warns = [], []
    by_ch = {r["ch"]: r for r in rows}
    prev = None
    for r in rows:
        ch = r["ch"]
        if r["in"] - r["out"] > 1:
            fails.append(f"ch {ch}: inside is at stage {r['in']} and outside "
                         f"at {r['out']} — inside may lead by one, not "
                         f"{r['in'] - r['out']}")
        if r["out"] > r["in"]:
            warns.append(f"ch {ch}: outside ({r['out']}) is ahead of inside "
                         f"({r['in']}) — the town sees more than they feel?")
        if prev:
            for k in ("in", "out"):
                if r[k] < prev[k]:
                    fails.append(f"ch {ch}: {k}side stage goes backward "
                                 f"({prev[k]} → {r[k]})")
                elif r[k] - prev[k] > 1:
                    fails.append(f"ch {ch}: {k}side stage jumps "
                                 f"{prev[k]} → {r[k]}; one stage at a time")
        if r["spends"]:
            if r["spends"] not in SPENDS:
                fails.append(f"ch {ch}: Spends is '{r['spends']}'; use want, "
                             f"kiss, or claim")
            earned = [e for e in r["earned"] if e < ch and e in by_ch
                      and by_ch[e]["rung"].strip("—- ") != ""]
            bad = [e for e in r["earned"] if e >= ch]
            if bad:
                fails.append(f"ch {ch}: '{r['spends']}' lists ch {bad} as "
                             f"earning it, but they come later")
            if len(earned) < 2:
                fails.append(f"ch {ch}: '{r['spends']}' is earned by "
                             f"{len(earned)} earlier scene(s) on the page; "
                             f"it needs two the reader can point to")
        if r["hole"].strip("—- "):
            warns.append(f"ch {ch}: HOLE — {r['hole']}")
        prev = r
    return fails, warns


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    rows = parse(sys.argv[1])
    if not rows:
        print("no ladder table found (columns: Ch | In | Out | Rung on the "
              "page | Spends | Earned by | Hole)")
        sys.exit(2)
    fails, warns = check(rows)
    spends = ", ".join(f"ch {r['ch']} {r['spends']}" for r in rows
                       if r["spends"]) or "none"
    print(f"ladder: {len(rows)} chapters, stages {rows[0]['in']}/"
          f"{rows[0]['out']} -> {rows[-1]['in']}/{rows[-1]['out']}, "
          f"spends: {spends}")
    for w in warns:
        print("WARN ", w)
    for f in fails:
        print("FAIL ", f)
    print("BUILD CHECK:", "FAIL" if fails else "PASS")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
