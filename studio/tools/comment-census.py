#!/usr/bin/env python3
"""comment-census.py — which of the author's notes is a SHAPE, and which lesson did not hold.

    python3 studio/tools/comment-census.py             # the census, newest shapes first
    python3 studio/tools/comment-census.py --brief     # the standing-asks block for a brief
    python3 studio/tools/comment-census.py --audit     # exit 2 if a lesson regressed
    python3 studio/tools/comment-census.py --scorecard # per chapter: REPEAT vs NEW (the thread's own score)

WHY THIS EXISTS
The per-comment loop works: a note gets a LEDGER row, the row names an
enforcer, `lesson-check` blocks a [FOLD] PR without one. What nothing
computes is the TREND — the same shape said three times in a week, or a
shape that comes back after its lesson supposedly landed.

The author, 2026-09-22: *"if we've seen a trend where I'm saying that
they have a lot of romantic speech, but they aren't having a lot of
romantic touch, how can we summarize that and then feed it to the next
group of writers so they don't make the same mistake?"*

The answer this tool gives is two numbers per shape: how often he has
said it, and **whether he has said it again since the fix**. A shape
that recurs after its enforcer landed is a REGRESSION, and it is the
most valuable line in this studio, because it is the only evidence that
a guardrail is not working. Ch 21 proved the case: three notes on the
same day about the body, a lesson (L054/L055) that produced `TOUCH
SPAN`, and the talk-to-body ratio went 0.66 in ch 21 and 3.61 in ch 22
— because the check reads one chapter at its highest touch cluster, and
ch 22 had no cluster to measure. (L073)

The shapes are the author's own seven (studio/AUTHOR-QUESTIONS.md).
"""
from __future__ import annotations
import datetime, os, re, sys

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
NOTES = os.path.join(REPO, "studio", "AUTHOR-NOTES.md")
LEDGER = os.path.join(REPO, "studio", "lessons", "LEDGER.md")

# The author's seven questions, matched on how he actually phrases them.
SHAPES = {
    "MORE": r"\b(romance|romantic|ache|longing|physical reaction|body reaction|arm goes warm|electricity|heat|feel(ing)? enough|chemistry|swoon)\b",
    "WHO": r"\b(conflict with|who (he|she|they) (is|are)|remind (us|me) who|good guys?|bad guys?|motivation|what (he|she|they) wants?|unintroduced)\b",
    "CONFUSING": r"\b(confus\w+|i (have no idea|can'?t tell|don'?t know)|unclear|timeline|keeps saying)\b",
    "NOSE": r"\b(on the nose|too explicit|don'?t (say|explain)|remove that concept|nothing be said|telling (us|me))\b",
    "POINT": r"\b(stakes?|the point|what (exactly )?happens if|teeth|sideshow|flat|so what)\b",
    "SENSES": r"\b(describ\w+|the storm|senses|smell|sound|weather|a paragraph at least|set(ting)? the scene)\b",
    "FUN": r"\b(fun|downer|laugh\w*|enjoy\w*|too serious|take the edge off|lonely|alone)\b",
}
TOL_DAYS = 400   # how far back the census reads


def note_rows() -> list[dict]:
    out = []
    for line in open(NOTES, encoding="utf-8"):
        m = re.match(r"\|\s*(\d{3})\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|", line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6:
            continue
        out.append({"n": m.group(1), "date": datetime.date.fromisoformat(m.group(2)),
                    "source": cells[2], "words": cells[4], "rule": cells[5]})
    return out


def classify(text: str) -> list[str]:
    return [s for s, rx in SHAPES.items() if re.search(rx, text, re.I)]


def lesson_dates() -> dict[str, datetime.date]:
    """For each note number cited by a ledger row, the row's date."""
    out = {}
    for line in open(LEDGER, encoding="utf-8"):
        if not line.startswith("| L"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        try:
            d = datetime.date.fromisoformat(cells[1])
        except ValueError:
            continue
        for n in re.findall(r"\b(\d{3})\b", cells[2]):
            out[n] = max(out.get(n, d), d)
    return out


def census():
    today = datetime.date.today()
    rows = [r for r in note_rows() if (today - r["date"]).days <= TOL_DAYS]
    led = lesson_dates()
    by = {}
    for r in rows:
        for s in classify(r["words"] + " " + r["rule"]):
            by.setdefault(s, []).append(r)
    out = []
    for s, rs in by.items():
        rs.sort(key=lambda r: r["date"])
        enforced = [r for r in rs if r["n"] in led]
        # The baseline is the FIRST time this shape got an enforcer, not the
        # latest. This studio fixes same-day, so measuring against the latest
        # fix made `after` zero for every shape — a regression detector that
        # cannot fire, which is the failure this whole environment is about.
        first_fix = min((led[r["n"]] for r in enforced), default=None)
        last_fix = max((led[r["n"]] for r in enforced), default=None)
        after = [r for r in rs if first_fix and r["date"] > first_fix]
        out.append({"shape": s, "n": len(rs), "first": rs[0]["date"], "last": rs[-1]["date"],
                    "enforced": len(enforced), "first_fix": first_fix, "last_fix": last_fix, "after": after,
                    "recent": [r for r in rs if (today - r["date"]).days <= 14]})
    out.sort(key=lambda x: (-len(x["after"]), -len(x["recent"]), -x["n"]))
    return out


def scorecard() -> int:
    """Per chapter: how many of the author's notes REPEAT a shape already fixed.

    The author, 2026-09-24: "We can't just count comments because I want
    to give fresh taste... but the goal is for the comments to inform the
    guard rail, and the writers going forward so they don't keep making
    the same mistakes." So the number is not comments per chapter. It is
    the share of a chapter's comments that repeat a shape whose enforcer
    had already shipped — a miss by the environment. NEW notes are the
    author writing the book, and they are welcome. (L081)
    """
    led = lesson_dates()
    notes = note_rows()
    # A note says its chapter directly ("PR #180 (1.2 ch 23)") or only its
    # PR ("chat (after #180)", "rereading ch 21"). Learn PR -> chapter from
    # the direct ones, then resolve the rest. The first version read only
    # the direct form and scored ch 23 at 0% repeat, missing the three chat
    # notes where the author said MORE and POINT again about that chapter —
    # the exact failure this scorecard exists to count.
    pr_ch: dict[str, str] = {}
    for r in notes:
        m = re.search(r"PR #(\d+) \((\d\.\d) ch (\d+)\)", r["source"])
        if m:
            pr_ch[m.group(1)] = f"{m.group(2)} ch{int(m.group(3)):02d}"
    by_ch: dict[str, list] = {}
    for r in notes:
        m = re.search(r"\((\d\.\d) ch (\d+)\)", r["source"])
        if m:
            key = f"{m.group(1)} ch{int(m.group(2)):02d}"
        else:
            m2 = re.search(r"after #(\d+)", r["source"])
            m3 = re.search(r"rereading ch (\d+)", r["source"])
            if m2 and m2.group(1) in pr_ch:
                key = pr_ch[m2.group(1)]
            elif m3:
                key = f"1.2 ch{int(m3.group(1)):02d}"
            else:
                continue
        by_ch.setdefault(key, []).append(r)
    # the date each shape FIRST got an enforcer
    first = {}
    for r in notes:
        if r["n"] in led:
            for s in classify(r["words"] + " " + r["rule"]):
                first[s] = min(first.get(s, led[r["n"]]), led[r["n"]])
    print("scorecard — the author's comments per chapter, REPEAT vs NEW\n")
    print("  REPEAT = the shape had an enforcer BEFORE he said it again (the environment missed)")
    print("  NEW    = fresh taste, or a shape nothing enforced yet (the author writing the book)\n")
    print("  chapter      notes  repeat  new   repeat%   repeated shapes")
    rows = []
    for ch in sorted(by_ch):
        rs = by_ch[ch]
        rep, shapes = 0, set()
        for r in rs:
            hit = [s for s in classify(r["words"]) if s in first and first[s] < r["date"]]
            if hit:
                rep += 1
                shapes |= set(hit)
        pct = 100 * rep / len(rs)
        rows.append((ch, len(rs), rep, pct))
        print(f"  {ch:<11} {len(rs):5d}  {rep:6d}  {len(rs)-rep:3d}   {pct:6.0f}%   {', '.join(sorted(shapes)) or '—'}")
    if len(rows) >= 2:
        a, b = rows[-2][3], rows[-1][3]
        trend = "falling" if b < a else "rising" if b > a else "flat"
        print(f"\n  last two chapters: {a:.0f}% → {b:.0f}% repeat ({trend}).")
    print("  The goal is the repeat column trending to zero while the new column stays alive.")
    print("  Fewer comments is not the goal; fewer comments he has already made is.")
    return 0


def main() -> int:
    if "--scorecard" in sys.argv:
        return scorecard()
    c = census()
    if "--quiet" in sys.argv:
        bad = [x for x in c if x["after"]]
        if not bad:
            return 0
        print("standing asks — shapes the author has repeated SINCE their fix shipped:")
        for x in bad[:4]:
            print(f"  [{x['shape']}] said {len(x['after'])} more time(s) since {x['first_fix']}"
                  f" — last: \"{x['after'][-1]['words'][:96]}…\"")
        print("  (python3 studio/tools/comment-census.py --brief for the full block)")
        return 0
    if "--brief" in sys.argv:
        print("STANDING ASKS — the author's recurring shapes, newest pressure first.")
        print("Generated by comment-census.py; do not hand-edit. Each line is a thing")
        print("he has asked for more than once. A shape marked REGRESSED came back")
        print("AFTER its fix shipped, so the fix is not holding — treat it as the")
        print("chapter's first job, not a box to tick.\n")
        for x in c[:6]:
            tag = f"REGRESSED ×{len(x['after'])}" if x["after"] else f"×{x['n']}"
            note = f" (last said {x['last']})"
            print(f"  [{x['shape']:<9}] {tag:<14}{note}")
            if x["after"]:
                for r in x["after"][:2]:
                    print(f"      since the fix: \"{r['words'][:110]}…\"")
        return 0
    if "--audit" in sys.argv:
        bad = [x for x in c if x["after"]]
        if not bad:
            print(f"comment-census: {len(c)} shapes, none has recurred since its fix")
            return 0
        print("comment-census: a lesson did not hold — the author said it again AFTER the fix:", file=sys.stderr)
        for x in bad:
            print(f"  ✗ {x['shape']}: first enforced {x['first_fix']}, then {len(x['after'])} more "
                  f"note(s) (#{', #'.join(r['n'] for r in x['after'])})", file=sys.stderr)
        print("  A recurrence after the fix is the only hard evidence a guardrail is not working.", file=sys.stderr)
        return 2
    print(f"comment-census  ({sum(x['n'] for x in c)} classified notes)\n")
    print("  shape      said  enforced  1st fix      SINCE       first       last")
    for x in c:
        lf = x["first_fix"].isoformat() if x["first_fix"] else "—"
        print(f"  {x['shape']:<9} {x['n']:5d}  {x['enforced']:8d}  {lf:<11}  "
              f"{len(x['after']):9d}   {x['first']}  {x['last']}")
    print("\n  'since fix' is the number that matters: the author saying a shape again")
    print("  after its enforcer shipped is the only hard evidence the enforcer is weak.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
