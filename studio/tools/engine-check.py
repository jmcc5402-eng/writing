#!/usr/bin/env python3
"""engine-check.py — are the book's 23 ingredients actually in it?

    python3 studio/tools/engine-check.py books/campus-series/book2

Exit 0 = every ingredient claimed, and every checkable one verified.
Exit 2 = something is unclaimed or claimed-but-absent.

WHY THIS EXISTS
`ENGINE-CHECKLIST.md` lists 23 ingredients every book in the series
owes. Ingredient 22 is "a dog", author-stated 2026-08-08. Book 1.2 is
nineteen chapters in and has no dog — only two mentions of a lost one
somebody is still looking for out past the fairgrounds.

Nobody decided to drop it. The rule existed, was correct, was written
down five weeks earlier, and the book drifted off it — the same shape
as the superfan going quiet for fifteen chapters and the three-drafter
competition lapsing for four.

The list was an instruction. This makes it a check.

HOW IT HANDLES WHAT IT CANNOT MEASURE
Most ingredients are not greppable. There is no regex for "competence
porn" or "the lie with a felt cost". So the checker holds two standards:

  greppable ingredients   verified against the prose
  everything else         verified as DECLARED — the book has to say
                          which chapter carries it

That is the same move `accept-gate.sh` makes. When you cannot check the
content, check that somebody committed to it. An unclaimed ingredient
is the failure; a claimed one that turns out weak is the panel's job.
"""
from __future__ import annotations
import argparse, pathlib, re, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import booklib as bl


def engine_list(series: pathlib.Path) -> dict[int, str]:
    """The 23, from ENGINE-CHECKLIST.md."""
    f = series / "ENGINE-CHECKLIST.md"
    out = {}
    if not f.exists():
        return out
    for cells in bl.tables(f, "Ingredient"):
        if len(cells) >= 2 and re.match(r"^\d+$", cells[0]):
            name = re.sub(r"\s*\(author[^)]*\)", "", cells[1]).strip()
            out[int(cells[0])] = name
    return out


def claims(book: pathlib.Path) -> dict[int, dict]:
    """canon/INGREDIENTS.md — where this book puts each one."""
    f = bl.declaration(book, "INGREDIENTS.md")
    out = {}
    if not f:
        return out
    for cells in bl.tables(f, "Verify"):
        if len(cells) < 3 or not re.match(r"^\d+$", cells[0]):
            continue
        n = int(cells[0])
        chs = [int(x) for x in re.findall(r"\d+", cells[1])]
        grep = None
        m = re.search(r"`([^`]+)`", cells[2])
        if m:
            grep = m.group(1)
        out[n] = {"chapters": chs, "grep": grep, "note": cells[2],
                  "missing": "MISSING" in cells[1].upper()}
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    args = ap.parse_args()

    book = pathlib.Path(args.book).resolve()
    series = book if (book / "ENGINE-CHECKLIST.md").exists() else book.parent
    ing = engine_list(series)
    if not ing:
        print("engine-check: no ENGINE-CHECKLIST.md found", file=sys.stderr)
        return 1
    cl = claims(book)
    chs = bl.chapters(book)
    text = {n: bl.body(p) for n, p in chs.items()}
    written = max(chs) if chs else 0

    print(f"engine-check  {book.name}   {len(ing)} ingredients, "
          f"{written} chapters written\n")

    unclaimed, absent, flagged, ok = [], [], [], []
    for n, name in sorted(ing.items()):
        c = cl.get(n)
        if not c:
            unclaimed.append((n, name))
            continue
        if c["missing"]:
            flagged.append((n, name, c["note"]))
            continue
        if c["grep"]:
            rx = re.compile(c["grep"], re.I)
            hits = sorted(k for k, t in text.items() if rx.search(t))
            wanted = [x for x in c["chapters"] if x <= written]
            if wanted and not any(x in hits for x in wanted):
                absent.append((n, name, c["chapters"], hits))
                continue
            ok.append((n, name, f"ch {','.join(map(str, hits[:6]))}"))
        else:
            ok.append((n, name, "declared ch " +
                       ",".join(map(str, c["chapters"])) + " (not greppable)"))

    for n, name, where in ok:
        print(f"    ok   {n:>2}  {name:<42} {where}")
    print()
    if flagged:
        print("  DECLARED MISSING — the author knows; recorded so it stays known:")
        for n, name, note in flagged:
            print(f"    !  {n:>2}  {name:<42} {note}")
        print()
    if unclaimed:
        print("  UNCLAIMED — no chapter has been named for these:")
        for n, name in unclaimed:
            print(f"    ?  {n:>2}  {name}")
        print()
    if absent:
        print("  CLAIMED BUT ABSENT — declared, and the prose does not have it:")
        for n, name, want, got in absent:
            print(f"    ✗  {n:>2}  {name:<42} claimed ch "
                  f"{','.join(map(str, want))}; found in "
                  f"{('ch ' + ','.join(map(str, got))) if got else 'no chapter'}")
        print()

    if unclaimed or absent:
        print("  An ingredient list nobody checks is a list of good intentions.")
        print("  Ingredient 22 (a dog) was author-stated on 2026-08-08 and")
        print("  Book 1.2 reached chapter 19 without one, because nothing asked.")
        return 2
    print("  every ingredient claimed; every checkable one found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
