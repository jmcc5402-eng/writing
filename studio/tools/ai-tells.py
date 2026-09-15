#!/usr/bin/env python3
"""ai-tells.py — the machine's fingerprints, measured rather than banned.

    python3 studio/tools/ai-tells.py books/campus-series
    python3 studio/tools/ai-tells.py books/campus-series --calibrate
    python3 studio/tools/ai-tells.py --file path/to/ch07.md

Exit 0 = no chapter is an outlier. Exit 2 = at least one is.

TWO KINDS OF TELL, CHECKED TWO DIFFERENT WAYS

Absolute tells are phrases that should never appear in this house's
prose at all. They get a flat ban and a zero tolerance.

Density tells are legitimate devices that become fingerprints by
repetition. "Not hers." is a good beat. Four of them in one chapter is
a template. So these are NOT banned — each chapter's rate is compared
against the corpus, and only outliers are reported.

WHY DENSITY AND NOT A BAN LIST
Measured across 49 accepted chapters and 131,000 words on 2026-09-15:
stock AI vocabulary scored ZERO, "not just X, it was Y" ZERO,
body-autonomy ZERO, "a mix of" ZERO. The 2026-08-22 scrub had already
eliminated every vocabulary tell in the book. Sentence-length variance
came in at CV 0.79, squarely inside the human literary range.

("the kind of X that" was in the first draft of this list and came out:
it fired on "a room built for the kind of waiting that doesn't improve
with company," which is good prose. A tell that flags good prose is a
bad regex.)

What survived were the STRUCTURAL ones — the antithesis opener at 78
narration instances, the tricolon at 72 — because STYLE caps those only
at chapter ENDINGS (the endings budget), and nothing looked at the
middle of a chapter.

This is the same lesson `opening-sameness.py` was built on: banning a
shape moves the tic to the next shape. Measuring the rate catches the
tic wherever it lands.

CALIBRATION
Thresholds below come from the corpus's own measured distribution, not
from a guess. Re-derive them with --calibrate after any large batch of
new prose, and update the table in the source with a note saying why.
"""
from __future__ import annotations
import argparse, pathlib, re, statistics, sys

# ---- absolute: never in this house's prose, old or new --------------
# Each of these measured ZERO across the accepted corpus on 2026-09-15.
# That is the bar for belonging here: if a pattern fires on prose the
# author has already approved, it is not an absolute — it is either a
# density tell or a bad regex.
ABSOLUTE = {
    "stock AI vocabulary":
        r"\b(testament to|tapestry|delve[sd]?|myriad|"
        r"navigate the \w+ (of|landscape)|underscore[sd]?|palpable|"
        r"cacophony|symphony of|a beacon of|in the realm of|"
        r"it'?s worth noting|that being said)\b",
    "'not just X, it was Y'":
        r"\b(wasn'?t|isn'?t|was not|is not) just\b[^.!?]{0,40}\bit (was|is)\b",
    "body-autonomy ('her hand found')":
        r"\b(his|her|their) (hand|eyes|gaze|fingers|feet) "
        r"(found|drifted|landed on|betrayed)\b",
}

# ---- spent: the budget is used up, so NO NEW ONES -------------------
# These differ from ABSOLUTE in a way that matters. RECENT.md marks a
# word "spent" when the prose has used its allowance — the existing
# instances are the ones that spent it, and they are legitimate. Only
# NEW uses are violations, so these are checked against the diff, never
# against the corpus.
#
# The first build of this tool got that backwards and reported fifteen
# violations, all of them the original approved uses. A check that
# fires on clean prose trains everyone to skim it, and a skimmed check
# is an instruction again.
SPENT = {
    "committee-of-the-self":
        r"\bbefore (s?he|they) could (vote|dress it)\b",
    "spent fingerprint word":
        r"\b(unhurried|and meant it|that was the whole)\b",
}

# ---- density: fine once, a fingerprint at volume --------------------
# rate = instances per 1,000 words of a chapter, unless noted.
# corpus medians measured 2026-09-15 over 49 chapters / 131k words.
DENSITY = {
    # name:            (regex or None, corpus median, flag above, note)
    "em dash":         (r"—", 0.9, 3.0,
                        "narration dashes are SPACED here by override; "
                        "density is the tell, not presence"),
    "antithesis opener": (None, 0.6, 2.2,
                        "'Not X.' / 'Nobody Y.' opening a narration line — "
                        "STYLE caps these at chapter endings only"),
    "tricolon (a, b, and c)": (r"\b\w+, \w+, and \w+\b", 0.55, 1.6,
                        "the rule of three, on repeat"),
    "'in that moment'": (r"\b(in that moment|for a moment|for a second|"
                        r"for the space of)\b", 0.06, 0.45,
                        "time-dilation filler"),
}
FRAG_PCT_FLAG = 11.0   # corpus 4.3% of paragraphs
CV_FLOOR = 0.55        # corpus 0.79; human literary prose ~0.6-0.9


def body(path: pathlib.Path) -> str:
    t = path.read_text(encoding="utf-8", errors="replace")
    parts = t.split("\n---\n", 1)
    return parts[-1] if len(parts) > 1 else t


def antithesis_count(text: str) -> int:
    """Narration only — dialogue may open however a person talks."""
    n = 0
    for line in text.split("\n"):
        s = line.strip()
        if not s or '"' in s or s.startswith("“") or s.startswith(">"):
            continue
        if re.match(r"^(Not|Never|Nobody|Nothing|No one)\b[^.!?]{0,60}\.\s*$", s):
            n += 1
    return n


def measure(text: str) -> dict:
    words = len(re.findall(r"\S+", text)) or 1
    flat = re.sub(r"\s+", " ", text)
    out = {"words": words}
    for name, (rx, _med, _flag, _n) in DENSITY.items():
        hits = antithesis_count(text) if rx is None else len(re.findall(rx, flat, re.I))
        out[name] = (hits, hits / words * 1000)
    paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    frag = 0
    for p in paras:
        lines = [l for l in p.strip().split("\n") if l.strip()]
        if len(lines) > 1 and len(lines[-1].split()) < 5 \
           and lines[-1].rstrip().endswith((".", "!", "?")):
            frag += 1
    out["frag_pct"] = frag / max(len(paras), 1) * 100
    lens = [len(s.split()) for s in re.split(r"(?<=[.!?])\s+", flat)
            if 1 < len(s.split()) < 80]
    out["cv"] = (statistics.pstdev(lens) / statistics.mean(lens)) if len(lens) > 5 else 1.0
    out["abs"] = {n: len(re.findall(rx, flat, re.I))
                  for n, rx in ABSOLUTE.items()}
    return out


def chapters(target: str) -> list[pathlib.Path]:
    p = pathlib.Path(target).resolve()
    if p.is_file():
        return [p]
    out = []
    for d in (p / "manuscript", p / "book2" / "manuscript"):
        if d.is_dir():
            out += sorted(d.glob("ch*.md"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("book", nargs="?", default="books/campus-series")
    ap.add_argument("--file", help="check one chapter")
    ap.add_argument("--calibrate", action="store_true",
                    help="print the corpus distribution and exit")
    ap.add_argument("--diff", metavar="REF", nargs="?", const="origin/main",
                    help="also check ADDED lines vs REF for spent words")
    args = ap.parse_args()

    files = chapters(args.file or args.book)
    if not files:
        print("ai-tells: no chapters found", file=sys.stderr)
        return 1

    data = {f: measure(body(f)) for f in files}

    if args.calibrate:
        print(f"calibration over {len(files)} chapters\n")
        for name in DENSITY:
            rates = sorted(d[name][1] for d in data.values())
            print(f"  {name:<26} median {statistics.median(rates):5.2f}  "
                  f"p90 {rates[int(len(rates)*.9)]:5.2f}  max {rates[-1]:5.2f}")
        fr = sorted(d["frag_pct"] for d in data.values())
        cv = sorted(d["cv"] for d in data.values())
        print(f"  {'para-final fragment %':<26} median {statistics.median(fr):5.1f}  max {fr[-1]:5.1f}")
        print(f"  {'sentence-length CV':<26} median {statistics.median(cv):5.2f}  min {cv[0]:5.2f}")
        return 0

    findings = []
    for f, d in data.items():
        label = f"{f.parent.parent.name}/{f.stem}"
        for name, n in d["abs"].items():
            if n:
                findings.append(("ABSOLUTE", label, f"{name} ×{n}"))
        for name, (_rx, med, flag, note) in DENSITY.items():
            hits, rate = d[name]
            if rate > flag and hits >= 3:
                findings.append(("density", label,
                                 f"{name}: {hits} in {d['words']}w = "
                                 f"{rate:.1f}/1k (corpus median {med}, flag {flag})"))
        if d["frag_pct"] > FRAG_PCT_FLAG:
            findings.append(("density", label,
                             f"para-final fragments: {d['frag_pct']:.0f}% of "
                             f"paragraphs (corpus 4.3%, flag {FRAG_PCT_FLAG:.0f}%)"))
        if d["cv"] < CV_FLOOR:
            findings.append(("shape", label,
                             f"sentence lengths too uniform: CV {d['cv']:.2f} "
                             f"(corpus 0.79, floor {CV_FLOOR}) — human prose varies"))

    if args.diff:
        import subprocess
        # Manuscripts only. Notes and panel reports QUOTE the prose, so
        # scanning them reported a "new" spent word that was a citation
        # of an approved line — tuning round three on this tool.
        d = subprocess.run(
            ["git", "diff", args.diff, "--",
             "*/manuscript/*.md"], capture_output=True, text=True).stdout
        added = " ".join(l[1:] for l in d.splitlines()
                         if l.startswith("+") and not l.startswith("+++"))
        for name, rx in SPENT.items():
            for m in re.finditer(rx, added, re.I):
                findings.append(("ABSOLUTE", f"(added vs {args.diff})",
                                 f"{name}: \"{m.group(0)}\" — RECENT.md says "
                                 f"the budget is spent; no new ones"))

    print(f"ai-tells  ({len(files)} chapters, "
          f"{sum(d['words'] for d in data.values()):,} words)\n")
    if not findings:
        print("  clean — no absolute tells, no chapter an outlier on density.")
        return 0

    for kind in ("ABSOLUTE", "density", "shape"):
        rows = [r for r in findings if r[0] == kind]
        if not rows:
            continue
        hdr = {"ABSOLUTE": "ABSOLUTE — never in this house's prose",
               "density": "DENSITY — a device that has become a fingerprint",
               "shape": "SHAPE"}[kind]
        print(f"  {hdr}:")
        for _, label, msg in rows:
            print(f"    ✗ {label:<22} {msg}")
        print()
    print("  Density findings are not bans. The device is fine; this chapter")
    print("  is leaning on it. Vary the chapter, do not add a rule — banning a")
    print("  shape moves the tic to the next shape, which has happened here.")
    return 2


if __name__ == "__main__":
    sys.exit(main())
