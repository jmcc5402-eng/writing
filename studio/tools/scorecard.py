#!/usr/bin/env python3
"""scorecard.py — roll every chapter's score file into one table.

    python3 studio/tools/scorecard.py books/<book>/book2

Reads notes/scores/chNN-score.md (written by /chapter-score), the
author's own numbers from notes/romance-levels.md, and the card's
Targets line from notes/cards/chNN-card.md, and writes
notes/SCORECARD.md — one row per chapter:

    | Ch | Romance (author / panel / target) | Aisha | Dan | Plan | Evidence |

Flags (printed, and listed at the top of the file):
  - a lead at 0 three chapters running
  - a romance level two or more under the card's target
  - an accepted chapter with no score file

Exit 0 always; this is a report, not a gate. The accept gate checks
that the score file exists; this reads what it says.
"""
from __future__ import annotations
import glob, os, re, sys

SCORE_RE = {
    "romance": re.compile(r"^ROMANCE:\s*(\d+)\s*[—-]\s*(.*)$", re.M),
    "plan": re.compile(r"^PLAN:\s*(.*)$", re.M),
}
LEAD_RE = re.compile(r"^([A-Z][A-Za-z]+):\s*([0-3])\s*[—-]\s*(.*)$", re.M)
T_RE = re.compile(r"Romance\s+(\d+)\s*·", re.I)


def read(p):
    return open(p, encoding="utf-8").read() if os.path.isfile(p) else ""


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__); return 2
    book = sys.argv[1].rstrip("/")
    notes = os.path.join(book, "notes")
    scores = {}
    for p in sorted(glob.glob(os.path.join(notes, "scores", "ch*-score.md"))):
        n = int(re.search(r"ch(\d+)", os.path.basename(p)).group(1))
        t = read(p)
        row = {"file": p}
        m = SCORE_RE["romance"].search(t)
        row["romance"] = int(m.group(1)) if m else None
        row["romance_why"] = m.group(2).strip() if m else ""
        row["leads"] = {}
        for lm in LEAD_RE.finditer(t):
            name = lm.group(1)
            if name in ("ROMANCE", "PLAN"):
                continue
            row["leads"][name] = (int(lm.group(2)), lm.group(3).strip())
        pm = SCORE_RE["plan"].search(t)
        row["plan"] = pm.group(1).strip() if pm else ""
        scores[n] = row

    # the author's number from romance-levels.md (first cell after the Ch)
    author = {}
    for line in read(os.path.join(notes, "romance-levels.md")).splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|\s*([^|]*)\|", line)
        if m:
            cell = m.group(2).strip()
            mm = re.search(r"\d+(?:–\d+)?", cell)
            author[int(m.group(1))] = mm.group(0) if mm else "—"

    # the card's target
    target = {}
    for p in glob.glob(os.path.join(notes, "cards", "ch*-card.md")):
        n = int(re.search(r"ch(\d+)", os.path.basename(p)).group(1))
        m = T_RE.search(read(p))
        if m:
            target[n] = int(m.group(1))

    accepted = []
    for p in sorted(glob.glob(os.path.join(book, "manuscript", "ch*.md"))):
        n = int(re.search(r"ch(\d+)", os.path.basename(p)).group(1))
        head = "\n".join(read(p).splitlines()[:12])
        if "ACCEPTED" in head:
            accepted.append(n)

    leads = sorted({k for r in scores.values() for k in r["leads"]})
    flags = []
    for n in accepted:
        if n not in scores:
            flags.append(f"ch {n}: accepted, no score file (run /chapter-score)")
    for n, r in sorted(scores.items()):
        if r["romance"] is not None and n in target and r["romance"] <= target[n] - 2:
            flags.append(f"ch {n}: romance {r['romance']} against a target of {target[n]}")
    for lead in leads:
        run = 0
        for n in sorted(scores):
            v = scores[n]["leads"].get(lead, (None, ""))[0]
            run = run + 1 if v == 0 else 0
            if run == 3:
                flags.append(f"{lead}: at 0 for three chapters running, ending ch {n}")

    out = ["# Scorecard — the romance level and each lead's development, chapter by chapter\n",
           "Written by `studio/tools/scorecard.py` from `notes/scores/chNN-score.md` (the readers' numbers), `notes/romance-levels.md` (the author's), and the cards' Targets lines. Scales: romance 1–10 (the reader's); development 0–3 per lead (0 not moved · 1 seen · 2 tested · 3 turned). A number without its evidence line is not a score.\n"]
    if flags:
        out.append("## Flags\n")
        out += [f"- {f}" for f in flags]
        out.append("")
    hdr = "| Ch | Romance author / panel / target | " + " | ".join(leads) + " | Plan | Evidence |"
    out.append("## The table\n")
    out.append(hdr)
    out.append("|" + "---|" * (hdr.count("|") - 1))
    for n in sorted(set(scores) | set(accepted)):
        r = scores.get(n)
        if not r:
            out.append(f"| {n} | {author.get(n, '—')} / — / {target.get(n, '—')} | " + " | ".join("—" for _ in leads) + " | — | no score file |")
            continue
        cells = []
        ev = []
        for lead in leads:
            v = r["leads"].get(lead)
            cells.append(str(v[0]) if v else "—")
            if v and v[1]:
                ev.append(f"{lead}: {v[1]}")
        rom = f"{author.get(n, '—')} / {r['romance'] if r['romance'] is not None else '—'} / {target.get(n, '—')}"
        evidence = (r["romance_why"] + (" · " if r["romance_why"] and ev else "") + " · ".join(ev)).replace("|", "/")
        out.append(f"| {n} | {rom} | " + " | ".join(cells) + f" | {r['plan'].replace('|', '/')} | {evidence} |")
    dst = os.path.join(notes, "SCORECARD.md")
    open(dst, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"scorecard: {len(scores)} chapters scored, {len(accepted)} accepted, {len(flags)} flag(s) → {os.path.relpath(dst)}")
    for f in flags:
        print(f"  ! {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
