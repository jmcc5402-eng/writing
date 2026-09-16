#!/usr/bin/env python3
"""story-matrix.py — the instrument panel for a book's shape.

    python3 studio/tools/story-matrix.py books/campus-series/book2
    python3 studio/tools/story-matrix.py books/campus-series --csv out.csv

Every guardrail before this one measured mechanics — columns, tics,
dashes, whether an instrument ran. None of them knew whether the story
worked. This one measures SHAPE: the romance curve, the presence curve,
the POV alternation, and where the Hauge turning points actually fall
against where they should.

WHAT IT IS AND IS NOT

It is not a judge. It cannot tell you a chapter is good, and it never
tries. The panel, the superfan and the author do that.

What it does is the thing a machine is actually better at than a person:
hold 30 chapters in mind at once and say where the line goes flat. The
2026-09-14 density survey found Book 1.2 running 26% romance-forward for
ten chapters and 54% after — and nothing caught it until chapter 19,
because every instrument in this studio reads ONE CHAPTER AT A TIME.

That is the division of labour this studio was built on: the machine
counts and remembers, the human decides.

THE COLUMNS, AND HOW HONEST EACH ONE IS

  words, cum%, dialogue%, POV     computed exactly
  both-leads                      computed exactly (both named on the page)
  presence                        PROXY — share of paragraphs in which the
                                  POV's counterpart is named or referred to.
                                  It correlates with the panel's
                                  romance-forward share; it is not the same
                                  measurement and must never be quoted as if
                                  it were. The panel's count is the truth.
  Hauge stage                     computed from cumulative position against
                                  studio/craft/hauge.md

Everything here is a diagnostic. A flat stretch is a question for the
author, not a defect.
"""
from __future__ import annotations
import argparse, pathlib, re, statistics, sys

# studio/craft/hauge.md — the timing spec, diagnostic not dogma.
HAUGE = [
    (0.00, "Setup"),
    (0.10, "New Situation"),       # TP1 Opportunity
    (0.25, "Progress"),            # TP2 Change of Plans
    (0.50, "Complications"),       # TP3 Point of No Return
    (0.75, "Final Push"),          # TP4 Major Setback
    (0.90, "Aftermath"),           # TP5 Climax
]
TURNING = {0.10: "Opportunity", 0.25: "Change of Plans",
           0.50: "Point of No Return", 0.75: "Major Setback",
           0.90: "Climax"}


def body(p: pathlib.Path) -> str:
    t = p.read_text(encoding="utf-8", errors="replace")
    parts = t.split("\n---\n", 1)
    return parts[-1] if len(parts) > 1 else t


def pov_of(p: pathlib.Path) -> str:
    head = p.read_text(encoding="utf-8", errors="replace")[:400]
    m = re.search(r"POV:\s*([A-Z][a-z]+)", head)
    return m.group(1) if m else "?"


def leads(files: list[pathlib.Path]) -> list[str]:
    """The two most common POV names are the leads."""
    povs = [pov_of(f) for f in files]
    seen: dict[str, int] = {}
    for p in povs:
        if p != "?":
            seen[p] = seen.get(p, 0) + 1
    return [n for n, _ in sorted(seen.items(), key=lambda kv: -kv[1])[:2]]


def declared_aliases(root: pathlib.Path) -> dict[str, list[str]]:
    """Read canon/NAMES.md if the book has one. A declaration beats a
    heuristic — see the note at the top of that file."""
    for cand in (root / "canon" / "NAMES.md",
                 root.parent / "canon" / "NAMES.md"):
        if not cand.exists():
            continue
        out: dict[str, list[str]] = {}
        for line in cand.read_text(encoding="utf-8").splitlines():
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 2 or cells[0] in ("Character",) or \
               set("".join(cells)) <= set("-: "):
                continue
            names = [a.strip() for a in cells[1].split(",") if a.strip()]
            if names:
                out[cells[0]] = sorted(names, key=len, reverse=True)
        if out:
            return out
    return {}


def aliases(both: list[str], corpus: str) -> dict[str, list[str]]:
    """Every way the page refers to each lead.

    The naming rule in STYLE makes this necessary: "names are
    relationships", so one character is Dan, Merritt and Coach depending
    on who is looking. Counting first names only reported the leads
    sharing 0-10% of paragraphs, which is nonsense — in ch09 Dan is
    "Merritt" six times, "Dan" twice and "Coach" once.

    A role epithet is assigned to ONE lead, by whichever it sits nearer
    to more often. The first build handed "Coach" to the doctor and
    "Doc" to the coach, because both appear in the same scenes.
    """
    from collections import Counter
    out = {n: {n} for n in both}
    for n in both:
        sur = Counter(re.findall(rf"\b{re.escape(n)}\s+([A-Z][a-z]+)", corpus))
        if sur:
            surname = sur.most_common(1)[0][0]
            out[n] |= {surname, f"Dr. {surname}"}
    for role in ("Coach", "Doc", "Doctor", "Captain", "Chief", "Professor"):
        score = {}
        for n in both:
            score[n] = len(re.findall(
                rf"\b{re.escape(n)}\b[^.]{{0,60}}\b{role}\b|"
                rf"\b{role}\b[^.]{{0,60}}\b{re.escape(n)}\b", corpus))
        best = max(score, key=score.get) if score else None
        if best and score[best] >= 3 and score[best] > 1.5 * min(score.values()):
            out[best].add(role)
            out[best].add(f"the {role.lower()}")
    return {n: sorted(v, key=len, reverse=True) for n, v in out.items()}


def measure(text: str, pov: str, both: list[str],
            alias_map: dict[str, list[str]]) -> dict:
    words = len(re.findall(r"\S+", text)) or 1
    other = next((n for n in both if n != pov), None)
    paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    present = 0
    if other:
        names = alias_map.get(other, [other])
        rx = re.compile("|".join(rf"\b{re.escape(n)}\b" for n in names), re.I)
        for p in paras:
            if rx.search(p):
                present += 1
    dlg = sum(1 for l in text.split("\n")
              if l.strip().startswith(('"', "“")))
    lines = [l for l in text.split("\n") if l.strip()]
    return {
        "words": words,
        "paras": len(paras),
        "presence": present / max(len(paras), 1) * 100,
        "dialogue": dlg / max(len(lines), 1) * 100,
        "both": bool(other and present > 0),
    }


def beat_map(root: pathlib.Path) -> tuple[dict, int]:
    """canon/BEATS.md — which chapter carries which beat, per curve.

    Returns {curve: [(beat, target_pct, chapter_no)]} and the planned
    chapter count. Positions are measured by CHAPTER NUMBER against the
    planned total, not by word count, so a half-written book still
    reports a beat that has slid.
    """
    f = root / "canon" / "BEATS.md"
    if not f.exists():
        return {}, 0
    text = f.read_text(encoding="utf-8")
    planned = 0
    m = re.search(r"[Pp]lanned chapters:\s*\*{0,2}(\d+)", text)
    if m:
        planned = int(m.group(1))
    curves, cur = {}, None
    for line in text.splitlines():
        if line.startswith("## "):
            cur = line[3:].split("—")[0].strip()
            continue
        if not line.startswith("|") or cur is None:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3 or set("".join(cells)) <= set("-: "):
            continue
        beat, tgt, ch = cells[0], cells[1], cells[2]
        if not re.match(r"^\d+$", tgt) or not re.match(r"^\d+$", ch):
            continue
        curves.setdefault(cur, []).append((beat, int(tgt), int(ch)))
    return curves, planned


def stage_at(frac: float) -> str:
    out = HAUGE[0][1]
    for pos, name in HAUGE:
        if frac >= pos:
            out = name
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    ap.add_argument("--csv", help="also write the matrix as CSV")
    args = ap.parse_args()

    root = pathlib.Path(args.book).resolve()
    files = sorted((root / "manuscript").glob("ch*.md"))
    if not files:
        print(f"story-matrix: no chapters under {root}/manuscript",
              file=sys.stderr)
        return 1

    both = leads(files)
    corpus = " ".join(body(f) for f in files)
    declared = declared_aliases(root)
    if all(n in declared for n in both):
        alias_map = {n: declared[n] for n in both}
        source = "canon/NAMES.md"
    else:
        alias_map = aliases(both, corpus)
        source = "auto-derived (no canon/NAMES.md row) — declare them"
    rows = []
    total = sum(len(re.findall(r"\S+", body(f))) for f in files)
    run = 0
    for f in files:
        b = body(f)
        pov = pov_of(f)
        m = measure(b, pov, both, alias_map)
        run += m["words"]
        rows.append({"ch": f.stem, "pov": pov, "frac": run / total, **m})

    print(f"story-matrix  {root.name}   {len(rows)} chapters, "
          f"{total:,} words   leads: {' / '.join(both) or '?'}")
    for n in both:
        print(f"    {n} on the page as: {', '.join(alias_map[n])}")
    print(f"    names from: {source}")
    print()
    print("  ch    words  cum%  POV        both  presence  dlg%  Hauge stage")
    print("  " + "-" * 68)
    for r in rows:
        bar = "#" * int(r["presence"] / 5)
        print(f"  {r['ch']:<5} {r['words']:>5}  {r['frac']*100:>4.0f}  "
              f"{r['pov']:<10} {'yes' if r['both'] else ' — ':<4}  "
              f"{r['presence']:>5.0f}%  {r['dialogue']:>4.0f}  "
              f"{stage_at(r['frac']):<14} {bar}")

    findings = []

    # --- the flat stretch: the failure that cost Book 1.2 ten chapters
    pres = [r["presence"] for r in rows]
    med = statistics.median(pres)
    runlen, start = 0, None
    for i, r in enumerate(rows):
        if r["presence"] < med * 0.6:
            start = r["ch"] if runlen == 0 else start
            runlen += 1
        else:
            if runlen >= 3:
                findings.append(
                    f"FLAT: {runlen} chapters from {start} run under 60% of "
                    f"the book's median presence ({med:.0f}%) — the shape that "
                    f"made 1.2 read as a plot book for ten chapters")
            runlen, start = 0, None
    if runlen >= 3:
        findings.append(
            f"FLAT: {runlen} chapters from {start} run under 60% of median "
            f"presence ({med:.0f}%)")

    # --- the opening stretch is the Kindle sample
    sample = [r for r in rows if r["frac"] <= 0.12]
    if sample:
        s = statistics.mean(r["presence"] for r in sample)
        if s < med * 0.75:
            findings.append(
                f"SAMPLE: the first {len(sample)} chapters average "
                f"{s:.0f}% presence against a book median of {med:.0f}% — "
                f"this is the stretch a reader downloads free")

    # --- POV alternation (campus STANDARDS 11: dual, alternating)
    streak, worst, who = 1, 1, ""
    for a, b_ in zip(rows, rows[1:]):
        if a["pov"] == b_["pov"] and a["pov"] != "?":
            streak += 1
            if streak > worst:
                worst, who = streak, a["pov"]
        else:
            streak = 1
    if worst >= 3:
        findings.append(
            f"POV: {worst} consecutive chapters in {who}'s head — "
            f"standard 11 is dual, alternating")

    # --- both leads absent, back to back
    runlen, start = 0, None
    for r in rows:
        if not r["both"]:
            start = r["ch"] if runlen == 0 else start
            runlen += 1
        else:
            if runlen >= 2:
                findings.append(
                    f"APART: {runlen} consecutive chapters from {start} with "
                    f"the other lead never named — the closeness ladder says "
                    f"two apart chapters never run in a row")
            runlen, start = 0, None

    # --- Hauge: where the turning points land by word count
    print("\n  Hauge turning points, by position in the manuscript:")
    for pos, name in TURNING.items():
        hit = next((r for r in rows if r["frac"] >= pos), rows[-1])
        print(f"    {pos*100:>3.0f}%  {name:<20} falls in {hit['ch']}")
    print("    (studio/craft/hauge.md: diagnostic, not dogma — but a Point")
    print("     of No Return at 70% means the middle is stalling)")

    curves, planned = beat_map(root)
    if curves:
        planned = planned or len(rows)
        written = len(rows)
        print(f"\n  BEAT MAP vs the curves  (planned {planned} chapters, "
              f"{written} written; tolerance ±7%)")
        for curve, beats in curves.items():
            print(f"\n    {curve}")
            for beat, tgt, ch in beats:
                actual = ch / planned * 100
                gap = actual - tgt
                # EARLY on a setup beat is usually a gift — the obstacle
                # on the page sooner. LATE is the one that signals a
                # stall. Both are reported; only LATE is ranked first.
                state = "ok " if abs(gap) <= 7 else ("LATE" if gap > 0 else "EARLY")
                mark = " " if state == "ok " else "?"
                w = "" if ch <= written else "  (not written yet)"
                print(f"      {mark} {beat:<26} target {tgt:>3}%  "
                      f"ch {ch:>2} = {actual:>3.0f}%  {state}{w}")
                if state != "ok ":
                    findings.append(
                        f"{curve}: \"{beat}\" declared at ch {ch} "
                        f"({actual:.0f}%) against a target of {tgt}% "
                        f"— {abs(gap):.0f} points {state.lower()}")

    if args.csv:
        with open(args.csv, "w") as fh:
            fh.write("chapter,words,cum_pct,pov,both_leads,presence_pct,"
                     "dialogue_pct,hauge_stage\n")
            for r in rows:
                fh.write(f"{r['ch']},{r['words']},{r['frac']*100:.1f},"
                         f"{r['pov']},{int(r['both'])},{r['presence']:.1f},"
                         f"{r['dialogue']:.1f},{stage_at(r['frac'])}\n")
        print(f"\n  csv → {args.csv}")

    if findings:
        print("\n  SHAPE FINDINGS — questions for the author, not defects:")
        late = [f for f in findings if "late" in f]
        rest = [f for f in findings if "late" not in f]
        for f in late + rest:
            print(f"    ? {f}")
        if late:
            print("\n    LATE is the one that matters. EARLY on a setup beat is")
            print("    usually a gift — the obstacle on the page sooner.")
        print("\n  'presence' is a proxy, not the panel's count. It is good at")
        print("  saying WHERE to look across thirty chapters and bad at saying")
        print("  whether any one of them works. Send the flagged stretch to a")
        print("  reader; that is the part a machine does not do.")
        return 2
    print("\n  no flat stretches, no POV runs, no apart-pairs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
