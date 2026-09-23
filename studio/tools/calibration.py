#!/usr/bin/env python3
"""calibration.py — how far the readers' numbers sit from the author's.

    python3 studio/tools/calibration.py books/campus-series/book2
    python3 studio/tools/calibration.py <book> --gate     # for the accept gate

Exit 0 = every instrument is inside tolerance, or there is not enough
ground truth to judge one. Exit 2 = an instrument is running outside it.

WHY THIS EXISTS
The qualitative layer is the larger half of this studio: romance 1–10,
each lead's development 0–3, the wound, the menace, who pays — planned
on `canon/TARGETS.md` before the draft, scored by a named reader after
it, and gated (`targets-check` holds a chapter whose romance is two or
more under target).

All of that rests on the readers' numbers being right, and twice they
have not been:

    ch 20   author 2–3    panel 6
    ch 23   author 3      panel 6

Three points high, twice. A gate that holds a chapter at "two under
target" is firing on a number that has been three over — so a chapter
the author would call a 3 passes as a 6, and the green check launders
it. That is worse than no gate.

Nothing measured the drift. `notes/romance-levels.md` records the
author's number beside the panel's by hand, only when he gives one.
This reads that record and computes the error, per instrument, with the
sample size stated — because two points is not a trend and the tool
should say so rather than sound certain. (L075)

It never blocks. An instrument running hot is a reason to distrust its
number, not a reason to stop the book; the gate prints the error beside
the score so a reader can weigh it.
"""
from __future__ import annotations
import os, pathlib, re, statistics as st, sys

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TOL = 1.5          # clicks on the 1–10 romance scale
MIN_POINTS = 3     # below this, report but never judge


def first_number(cell: str) -> float | None:
    """The first number in a prose cell, tolerating '2–3', '**6 · 6 · 6**', '3 → 6'."""
    c = re.sub(r"\([^)]*\)", " ", cell)          # drop parentheticals
    c = re.sub(r"[*_`]", "", c)
    # The FIRST number in the cell is the one that counts, and it is a range
    # only if the dash follows it immediately. Matching ranges first read
    # ch 23's "3 ... heat 1-2" as 1.5 when the author had said 3 — a silent
    # two-point error in the one record the gates calibrate against.
    m = re.search(r"(\d+(?:\.\d+)?)(?:\s*[–-]\s*(\d+(?:\.\d+)?))?", c)
    if not m:
        return None
    return (float(m.group(1)) + float(m.group(2))) / 2 if m.group(2) else float(m.group(1))


def read_rows(book: pathlib.Path):
    """(chapter, author, panel, superfan) from notes/romance-levels.md."""
    f = book / "notes" / "romance-levels.md"
    if not f.exists():
        return None, []
    rows = []
    for line in f.read_text(encoding="utf-8").splitlines():
        if not re.match(r"\|\s*\d+\s*\|", line):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) < 3:
            continue
        ch = int(re.search(r"\d+", c[0]).group(0))
        rows.append({"ch": ch, "author": first_number(c[1]), "panel": first_number(c[2]),
                     "superfan": first_number(c[3]) if len(c) > 3 else None})
    return f, rows


def report(book: pathlib.Path, gate: bool) -> int:
    f, rows = read_rows(book)
    if f is None:
        print(f"calibration: no notes/romance-levels.md under {book} — nothing to calibrate against")
        return 0
    paired = {k: [(r["ch"], r["author"], r[k]) for r in rows
                  if r["author"] is not None and r.get(k) is not None]
              for k in ("panel", "superfan")}
    if gate:
        for k, ps in paired.items():
            if len(ps) < MIN_POINTS:
                continue
            err = st.mean(v - a for _, a, v in ps)
            if abs(err) > TOL:
                print(f"  calibration: the {k}'s romance level has run {err:+.1f} against the "
                      f"author's across {len(ps)} chapters — weigh its number accordingly")
        return 0

    try:
        shown = f.relative_to(REPO)
    except ValueError:            # a fixture outside the repo — hook-check uses one
        shown = f
    print(f"calibration  ({shown})\n")
    any_judged = False
    for k, ps in paired.items():
        if not ps:
            print(f"  {k:<9} no chapter has both an author number and a {k} number")
            continue
        errs = [v - a for _, a, v in ps]
        err = st.mean(errs)
        print(f"  {k:<9} {len(ps)} calibration point(s): " +
              ", ".join(f"ch{c} {a:g} vs {v:g}" for c, a, v in ps))
        if len(ps) < MIN_POINTS:
            print(f"            mean error {err:+.1f} — but {len(ps)} point(s) is not a trend. "
                  f"NOT JUDGED (floor {MIN_POINTS}).")
            continue
        any_judged = True
        verdict = "inside tolerance" if abs(err) <= TOL else f"OUTSIDE tolerance (±{TOL})"
        print(f"            mean error {err:+.1f}  →  {verdict}")
    print()
    print("  The author's number is the ground truth and there are very few of them.")
    print("  One line on a chapter PR — the romance level, and whether each lead moved —")
    print("  is what makes every gate in the qualitative layer trustworthy.")
    if not any_judged:
        print("\n  Nothing judged yet: no instrument has reached the floor of "
              f"{MIN_POINTS} paired readings.")
        return 0
    bad = [k for k, ps in paired.items()
           if len(ps) >= MIN_POINTS and abs(st.mean(v - a for _, a, v in ps)) > TOL]
    if bad:
        print(f"\n  OUT OF CALIBRATION: {', '.join(bad)}. Its number should not be "
              f"trusted to hold or pass a chapter until it re-calibrates.")
        return 2
    return 0


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    book = pathlib.Path(args[0]).resolve() if args else pathlib.Path(REPO, "books/campus-series/book2")
    return report(book, "--gate" in sys.argv)


if __name__ == "__main__":
    try:
        rc = main()
    except BrokenPipeError:
        os._exit(0)
    sys.exit(rc)
