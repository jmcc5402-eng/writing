#!/usr/bin/env python3
"""roster-staleness.py — which instruments have gone quiet.

    python3 studio/tools/roster-staleness.py
    python3 studio/tools/roster-staleness.py --asof 2026-09-14

Joins studio/agents/CADENCE.md against studio/agents/variance/LOG.md and
reports every instrument whose last run is older than its cadence.

Exit 0 = nothing stale. Exit 2 = something has fallen out of the loop.

WHY THIS EXISTS
On 2026-09-14 the superfan had not run in fifteen chapters and nothing
had noticed. Not a skipped gate — no gate was ever due. An adjacent
instrument grew into the same slot and the old one fell out, and every
individual chapter looked correct.

Drift is invisible per-chapter and obvious across chapters. Nothing in
the studio read across chapters. This does.
"""
from __future__ import annotations
import argparse, datetime as dt, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
CADENCE = ROOT / "studio" / "agents" / "CADENCE.md"
LOG = ROOT / "studio" / "agents" / "variance" / "LOG.md"
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def read_cadences() -> list[tuple[str, str, int | None]]:
    """(instrument, cadence phrase, threshold days or None for on-demand)."""
    out = []
    for line in CADENCE.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3 or not cells[0].startswith("`"):
            continue
        name = cells[0].strip("`")
        phrase = cells[1].replace("**","")
        raw = cells[2].strip()
        days = int(raw) if raw.isdigit() else None
        out.append((name, phrase, days))
    return out


def last_runs() -> dict[str, dt.date]:
    """Latest logged date per instrument, from the variance draw log."""
    seen: dict[str, dt.date] = {}
    for line in LOG.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        m = DATE_RE.match(cells[0])
        if not m:
            continue
        day = dt.date.fromisoformat(m.group(1))
        # The agent name is the leading token of the second cell:
        #   "romance-reader-panel 1.5.4 (B1.2 CH 19 — ...)"
        who = re.match(r"[a-z][a-z-]+", cells[1])
        if not who:
            continue
        name = who.group(0)
        if name not in seen or day > seen[name]:
            seen[name] = day
    return seen


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--asof", help="YYYY-MM-DD; default: the log's newest entry")
    ap.add_argument("--quiet", action="store_true",
                    help="print only the stale ones")
    args = ap.parse_args()

    runs = last_runs()
    if not runs:
        print("roster-staleness: no dated rows in the draw log", file=sys.stderr)
        return 1

    # Default "today" is the log's own newest date, so the report is
    # reproducible and works in a repo that has been idle for a week.
    asof = dt.date.fromisoformat(args.asof) if args.asof else max(runs.values())

    stale, ok, never, ondemand = [], [], [], []
    for name, phrase, days in read_cadences():
        last = runs.get(name)
        if days is None:
            ondemand.append((name, last))
            continue
        if last is None:
            never.append((name, phrase, days))
            continue
        age = (asof - last).days
        (stale if age > days else ok).append((name, phrase, days, last, age))

    print(f"roster-staleness  (as of {asof})\n")

    if stale:
        print("  STALE — an instrument has fallen out of the loop:")
        for name, phrase, days, last, age in sorted(stale, key=lambda r: -r[4]):
            print(f"    ✗ {name:<24} last run {last}  "
                  f"({age} days ago; cadence: {phrase}, threshold {days}d)")
        print()
    if never:
        print("  NEVER RUN:")
        for name, phrase, days in never:
            print(f"    ? {name:<24} cadence: {phrase}")
        print()
    if not args.quiet:
        if ok:
            print("  current:")
            for name, phrase, days, last, age in sorted(ok, key=lambda r: r[4]):
                print(f"    ✓ {name:<24} last run {last}  ({age}d, ok to {days}d)")
        if ondemand:
            print("\n  on-demand (never stale):")
            print("    " + ", ".join(n for n, _ in ondemand))

    if stale or never:
        print()
        print("  An instrument going quiet is fine. An instrument going quiet")
        print("  with nobody deciding is the failure. Either run it, or change")
        print("  its row in studio/agents/CADENCE.md and say why in the commit.")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
