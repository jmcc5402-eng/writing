#!/usr/bin/env python3
"""voice-dial.py — measure the book's register, not just declare it.

    python3 studio/tools/voice-dial.py books/campus-series/book2
    python3 studio/tools/voice-dial.py books/campus-series --compare
    python3 studio/tools/voice-dial.py books/campus-series/book2 --drivers

Exit 0 = every dial inside tolerance of its declared setting.
Exit 2 = a dial has drifted from what DIALS.md says it is.

WHY THIS EXISTS
`DIALS.md` has declared a setting for every dial since 2026-08-29 —
"Modernity 3", "Edge 2" — and **nothing has ever measured one.** They
are numbers in a markdown file.

Which is why the author's most-repeated note never landed. From the
transcripts: *"I'm constantly trying to get the other thread to make it
less small town and country, but it seems like they can't."* A drafter
told "less country" with no number cannot tell whether it succeeded,
and neither can anyone reviewing it.

WHAT THE FIRST MEASUREMENT FOUND (2026-09-16)

    Book 1.1   country 6.95/1k   urban 0.33/1k   ratio 21.0:1
    Book 1.2   country 4.26/1k   urban 0.43/1k   ratio  9.8:1

So the note DID land — 1.2 halved the country density. It is still
overwhelmingly country, and the reason is the important part:

    porch  223
    county 212        = 54% of every country marker in both books

Those are not style words. They are the SETTING. A drafter told to be
less country drops a "y'all" and writes another porch scene, because
the rooms it has to write in are porches and the county.

**You do not move this dial with a word list. You move it by changing
the rooms and the institutions.** That is the finding this tool exists
to make visible, and it is why five weeks of asking did not work.
"""
from __future__ import annotations
import argparse, pathlib, re, sys
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import booklib as bl

# Each dial: (low-pole markers, high-pole markers). The score is 1–10,
# where 10 is the HIGH pole. Markers are deliberately plain nouns —
# register lives in furniture, not in adjectives.
DIALS = {
    "Modernity": (
        # low = small-town country
        r"\b(porch|pickup|truck bed|tailgate|holler|y'all|ma'am|church|"
        r"congregation|casserole|feed store|gravel|screen door|county|"
        r"barbecue|brisket|tractor|pasture|fairground\w*|courthouse|"
        r"the square|Main Street|diner|barber|VFW|grange|creek|pew|"
        r"revival|hymn|supper|fixin|reckon|yonder|granny|mama|daddy)\b",
        # high = contemporary / cosmopolitan
        r"\b(apartment|condo|rideshare|Uber|Lyft|app\b|podcast|sublet|"
        r"gallery|subway|transit|airport|terminal|barista|espresso|"
        r"cocktail|rooftop|co-?working|startup|consultant|boutique|"
        r"museum|gym|elevator|takeout|streaming|playlist|group chat|"
        r"inbox|text thread|screenshot|stream)\b"),
    "Warmth": (
        r"\b(cold|silence|silent|flat|formal|stiff|professional|distance|"
        r"alone|empty|quiet in the bad way|nobody said)\b",
        r"\b(laugh\w*|smil\w*|grin\w*|warm|kindness|hugg?\w*|teas\w*|"
        r"delight\w*|beam\w*|chuckl\w*|fond)\b"),
    "Edge": (
        r"\b(gosh|darn|shoot|heck|goodness|bless)\b",
        r"\b(damn|hell|bastard|ass|bitch|shit|screw(ed)? (up|over)|"
        r"pissed|crap)\b"),
}
TOLERANCE = 1.5   # clicks on the 1–10 scale


MIN_SIGNAL = 25   # below this the ratio is noise, not a reading


def score(text: str, low: str, high: str):
    """(score 1-10, low hits, high hits, confident?).

    A ratio built on a handful of hits is not a measurement. Book 1.2
    scored Edge 10.0 on six profanities and zero mild oaths in 64,000
    words — a confident-looking number from almost no signal, which is
    the failure mode this whole environment exists to avoid.
    """
    lo = len(re.findall(low, text, re.I))
    hi = len(re.findall(high, text, re.I))
    if lo + hi == 0:
        return 5.5, 0, 0, False
    val = 1 + 9 * (hi / (lo + hi))
    return val, lo, hi, (lo + hi) >= MIN_SIGNAL


def declared(series: pathlib.Path, book_label: str) -> dict[str, float]:
    """Settings from DIALS.md for a book, if the sheet names them."""
    f = series / "DIALS.md"
    out = {}
    if not f.exists():
        return out
    text = f.read_text(encoding="utf-8")
    m = re.search(rf"##\s*Book {re.escape(book_label)}[^\n]*\n(.*?)(?=\n## |\Z)",
                  text, re.S)
    if not m:
        return out
    for line in m.group(1).splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 2:
            num = re.match(r"^(\d+(?:\.\d+)?)", cells[1])
            if num and cells[0] in DIALS:
                out[cells[0]] = float(num.group(1))
    return out


def analyse(book: pathlib.Path, first: int | None = None) -> dict:
    chs = bl.chapters(book)
    if first:
        chs = {n: f for n, f in sorted(chs.items())[:first]}
    text = "\n".join(bl.body(f) for f in chs.values())
    return {name: score(text, lo, hi) for name, (lo, hi) in DIALS.items()}, text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    ap.add_argument("--compare", action="store_true",
                    help="every book under this path, side by side")
    ap.add_argument("--drivers", action="store_true",
                    help="which words actually move each dial")
    ap.add_argument("--first", type=int, metavar="N",
                    help="read only the first N chapters — the early warning. "
                         "THREE is the floor: ch 1-2 hold too few markers to score, "
                         "ch 1-3 of Book 1.2 read Modernity 1.8 against a finished 2.1 "
                         "and a sheet declaring 5. That gap was findable at 8,000 words "
                         "and nobody found it until chapter 24. (L077)")
    args = ap.parse_args()

    root = pathlib.Path(args.book).resolve()
    books = bl.find_books(root) if args.compare else [root]
    series = root if (root / "DIALS.md").exists() else root.parent

    if args.first:
        print(f"voice-dial   EARLY READ — first {args.first} chapter(s) only")
        print("  A dial is set by the rooms and the institutions, and those are fixed at")
        print("  the outline. Reading ch 1 tells you at 3,000 words what the finished book")
        print("  will measure, instead of at 60,000. The gap is cheap to close here and an")
        print("  outline rewrite later.\n")
    else:
        print(f"voice-dial   scale 1–10, high pole named\n")
    rows = {}
    for b in books:
        scores, text = analyse(b, args.first)
        rows[b] = (scores, text)
        label = "1.1" if b.name != "book2" else "1.2"
        want = declared(series, label)
        print(f"  {b.name}")
        for name, (val, lo, hi, conf) in scores.items():
            hip = {"Modernity": "contemporary", "Warmth": "warm",
                   "Edge": "profane"}[name]
            bar = "─" * int(val) + "●" + "─" * (10 - int(val))
            tgt = want.get(name)
            flag = ""
            if not conf:
                print(f"    {name:<10}  n/a  {'·'*11}  "
                      f"only {lo+hi} markers in the book — too little "
                      f"signal to score (floor {MIN_SIGNAL})")
                continue
            if tgt is not None:
                gap = val - tgt
                flag = (f"   declared {tgt:.0f}"
                        + ("" if abs(gap) <= TOLERANCE
                           else f"  ✗ off by {abs(gap):.1f}"))
            print(f"    {name:<10} {val:4.1f}  {bar}  ({lo} low / {hi} {hip})"
                  f"{flag}")
        print()

    if args.drivers:
        for b, (_, text) in rows.items():
            print(f"  what makes {b.name} read the way it does:")
            for name, (lo, hi) in DIALS.items():
                c = Counter(m if isinstance(m, str) else m[0]
                            for m in re.findall(lo, text, re.I))
                top = ", ".join(f"{w.lower()}×{n}" for w, n in c.most_common(5))
                if top:
                    print(f"    {name:<10} low pole: {top}")
            print()
        print("  The top two markers are usually SETTING, not style. In this")
        print("  series porch (223) and county (212) are 54% of the country")
        print("  signal — so a drafter told 'less country' drops a y'all and")
        print("  writes another porch scene. Move the ROOMS, not the words.")

    # drift against the declared sheet
    bad = []
    for b, (scores, _) in rows.items():
        label = "1.1" if b.name != "book2" else "1.2"
        want = declared(series, label)
        for name, (val, lo, hi, conf) in scores.items():
            if conf and name in want and abs(val - want[name]) > TOLERANCE:
                bad.append(f"{b.name}: {name} measures {val:.1f}, "
                           f"DIALS.md says {want[name]:.0f}")
    if bad:
        print("  DRIFT — the sheet and the prose disagree:")
        for x in bad:
            print(f"    ✗ {x}")
        print()
        print("  Either the book drifted or the sheet was aspirational.")
        print("  Both are worth knowing; neither is visible without a number.")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
