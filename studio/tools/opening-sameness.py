#!/usr/bin/env python3
"""opening-sameness.py — detect convergence of SHAPE, not of strings.

    python3 studio/tools/opening-sameness.py books/campus-series/book2

Reports when chapter openings start to rhyme with each other, whatever
the rhyme is.

Exit 0 = varied. Exit 2 = a cluster has formed.

WHY THIS EXISTS — and why it is not a ban list
On 2026-09-07 the author wrote: "the first paragraph seems very similar
to previous first paragraphs. I DON'T HAVE A GOOD WAY OF CHECKING."
Chapters 10, 11 and 12 had opened on the same calendar recital, one
sentence word-for-word in all three. The cause was the brief's own rule
("say the day and the stake in the first paragraph") hardening into a
template.

`opening-check.py` was built that day to ban the calendar opening. It
worked. Five days later the superfan read six random chapters and
reported: "every scene starts with what time it is and which stool."
Chapters 4, 15, 17, 18 and 19 all opened that way.

THE LESSON: a narrow check does not eliminate a tic, it DISPLACES it.
The drafters satisfied the letter of the ban and found another recital.
So this tool never names a forbidden shape. It clusters openings by
their shape and reports whichever cluster has grown — including shapes
nobody has thought of yet.
"""
from __future__ import annotations
import argparse, collections, itertools, pathlib, re, sys

TIME_WORDS = re.compile(
    r"\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday|"
    r"january|february|march|april|may|june|july|august|september|"
    r"october|november|december|morning|noon|midnight|evening|night|"
    r"o'clock|a\.m\.|p\.m\.|dawn|dusk|"
    r"(half )?past \w+|quarter (past|to)|"
    r"(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)[- ]"
    r"(thirty|fifteen|forty|fifty|o'clock))\b|\b\d{1,2}:\d{2}\b", re.I)
COUNT_WORDS = re.compile(
    r"\b(\w+) (days?|weeks?|hours?|minutes?) (out|left|off|to go|from)\b", re.I)


def first_paragraph(text: str) -> tuple[str, int]:
    """The chapter's first prose paragraph.

    Chapter files are: H1, a production header (POV line + a multi-line
    parenthetical), a `---` rule, the epigraph as a blockquote, then the
    prose. Anchor on the rule — the header's continuation lines look like
    prose otherwise, which is how this tool first reported that every
    chapter opened on "accepted at the merge".
    """
    lines = text.splitlines()
    i = 0
    for j, l in enumerate(lines):
        if l.strip() == "---":
            i = j + 1
            break
    while i < len(lines) and (not lines[i].strip() or lines[i].startswith(">")):
        i += 1
    start, buf = i + 1, []
    while i < len(lines) and lines[i].strip():
        buf.append(lines[i].strip())
        i += 1
    return " ".join(buf), start


def shape(p: str) -> str:
    """Classify how an opening LEADS — its first move, not its content."""
    if not p:
        return "empty"
    first = re.split(r"(?<=[.!?])\s", p)[0]
    head = " ".join(first.split()[:9])
    if first.lstrip().startswith(('"', "“")):
        return "dialogue-first"
    if TIME_WORDS.search(head):
        return "clock-first"
    if COUNT_WORDS.search(first):
        return "countdown-first"
    words = first.split()
    if words and words[0].lower() in {"the", "a", "an"}:
        return "object-first"
    if words and re.match(r"^[A-Z][a-z]+$", words[0]) and \
       (len(words) > 1 and re.match(r"^[A-Z]", words[1])):
        return "name-first"
    if words and words[0].lower() in {"he", "she", "they", "nobody", "somebody"}:
        return "pronoun-first"
    return "other"


def ngrams(p: str, n: int = 4) -> set[str]:
    w = re.findall(r"[a-z']+", p.lower())
    return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("book", help="a directory containing manuscript/")
    ap.add_argument("--threshold", type=float, default=0.34,
                    help="fraction of chapters sharing one shape that trips it")
    args = ap.parse_args()

    root = pathlib.Path(args.book).resolve()
    files = sorted((root / "manuscript").glob("ch*.md"))
    if not files:
        print(f"opening-sameness: no chapters under {root}/manuscript",
              file=sys.stderr)
        return 1

    opens = {}
    for f in files:
        p, _ = first_paragraph(f.read_text(encoding="utf-8", errors="replace"))
        opens[f.stem] = p

    shapes = {c: shape(p) for c, p in opens.items()}
    counts = collections.Counter(shapes.values())
    n = len(opens)

    print(f"opening-sameness  {root.name}  ({n} chapters)\n")
    print("  shape distribution:")
    for s, c in counts.most_common():
        bar = "#" * c
        print(f"    {s:<16} {c:>3}  {bar}")

    findings = []
    for s, c in counts.items():
        if s == "other":
            continue
        if c / n >= args.threshold:
            chapters = sorted(ch for ch, sh in shapes.items() if sh == s)
            findings.append(
                f"{c} of {n} chapters ({c/n:.0%}) open {s}: "
                f"{', '.join(chapters)}")

    # verbatim overlap between any two openings
    echoes = []
    for a, b in itertools.combinations(sorted(opens), 2):
        shared = ngrams(opens[a]) & ngrams(opens[b])
        if shared:
            echoes.append((a, b, sorted(shared)[:3], len(shared)))
    echoes.sort(key=lambda e: -e[3])

    if findings:
        print("\n  CLUSTER — a shape has taken over:")
        for f in findings:
            print(f"    ✗ {f}")
    if echoes:
        print("\n  VERBATIM ECHO — four-word runs shared between openings:")
        for a, b, ex, k in echoes[:8]:
            print(f"    ✗ {a} / {b}  ({k} shared): \"{ex[0]}\"")

    if findings or echoes:
        print()
        print("  This tool names no forbidden shape on purpose. Banning one")
        print("  recital moves the tic to the next one — that already happened")
        print("  here once. Vary the openings; do not add a rule.")
        return 2
    print("\n  varied — no cluster, no echo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
