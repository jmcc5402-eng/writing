#!/usr/bin/env python3
"""Report the dialogue percentage of a chapter or candidate.

The dialogue floor (author, 2026-08-18, recorded in
studio/DRAFTING-PROTOCOL.md): the shelf runs 30-40% dialogue; this
voice is narration-forward on purpose, so the working targets are a
book average near 25%, a per-chapter floor of 15%, at most one
deliberate quiet chapter (~8-10%) per quarter, and never two
sub-floor chapters in a row.

That ruling says: "the linter counts quoted words and reports the
percentage with every candidate." This is that linter.

    python3 studio/tools/dialogue-lint.py FILE [FILE ...]

Counts words inside double quotes against total body words. Front
matter above the first '---' rule is excluded, so a candidate's
header block does not dilute the count.
"""
import re
import sys

FLOOR = 15.0
QUIET_MIN = 8.0
TARGET_AVG = 25.0


def measure(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    try:
        body = "\n".join(lines[lines.index("---") + 1:])
    except ValueError:
        body = "\n".join(lines)
    total = len(body.split())
    quoted = sum(len(m.split()) for m in re.findall(r'"([^"]+)"', body))
    return total, quoted


def verdict(pct):
    if pct >= FLOOR:
        return "OK"
    if pct >= QUIET_MIN:
        return "quiet-chapter band (one per quarter)"
    return "BELOW FLOOR"


def main(paths):
    rows = []
    print(f"{'file':<34}{'words':>7}{'quoted':>8}{'pct':>8}   verdict")
    for p in paths:
        total, quoted = measure(p)
        pct = 100 * quoted / total if total else 0.0
        rows.append((p, total, quoted, pct))
        name = p.rsplit("/", 1)[-1]
        print(f"{name:<34}{total:>7}{quoted:>8}{pct:>7.1f}%   {verdict(pct)}")
    if len(rows) > 1:
        words = sum(r[1] for r in rows)
        avg = 100 * sum(r[2] for r in rows) / words if words else 0.0
        print(f"\naverage across {len(rows)} files: {avg:.1f}%  "
              f"(target ~{TARGET_AVG:.0f}%)")
        sub = [i for i, r in enumerate(rows) if r[3] < FLOOR]
        if sub:
            names = ", ".join(rows[i][0].rsplit("/", 1)[-1] for i in sub)
            print(f"sub-floor: {names}")
        if any(b - a == 1 for a, b in zip(sub, sub[1:])):
            print("VIOLATION: two or more sub-floor chapters in a row.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
