#!/usr/bin/env python3
"""bans.py — the greppable bans as data, and the test that proves them.

    python3 studio/tools/bans.py FILE [FILE...]   # findings, one per line; exit 2 if any
    python3 studio/tools/bans.py --test           # every ban has a fixture and fires on it
    python3 studio/tools/bans.py --list           # the bans, for a brief

The bans live in studio/lessons/bans.txt (ID, regex, note); the fixtures
in studio/lessons/fixtures.tsv (ID, a sentence that must trip it).
prose-guard.sh and chapter-lint.sh call this instead of carrying their
own lists — before 2026-09-20 prose-guard had six phrases hardcoded
from August and RECENT.md had twenty bans, so a new ban was an
instruction until somebody edited a shell script. (L028)
"""
from __future__ import annotations
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LESSONS = os.path.join(HERE, "..", "lessons")


def load_bans():
    out = []
    for line in open(os.path.join(LESSONS, "bans.txt"), encoding="utf-8"):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 2:
            continue
        bid, rx = parts[0].strip(), parts[1].strip()
        note = parts[2].strip() if len(parts) > 2 else ""
        try:
            out.append((bid, re.compile(rx, re.I), rx, note))
        except re.error as e:
            print(f"bans.txt {bid}: bad regex ({e})", file=sys.stderr)
    return out


def load_fixtures():
    fx = {}
    for line in open(os.path.join(LESSONS, "fixtures.tsv"), encoding="utf-8"):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.rstrip("\n").split("\t", 1)
        if len(parts) == 2:
            fx.setdefault(parts[0].strip(), []).append(parts[1])
    return fx


def check_file(path, bans):
    findings = []
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except OSError:
        return findings
    for i, ln in enumerate(lines, 1):
        if ln.lstrip().startswith("(") and i < 15:      # the production header
            continue
        for bid, rx, _, note in bans:
            m = rx.search(ln)
            if m:
                findings.append(f"{os.path.basename(path)}:{i}: banned ({bid}) \"{m.group(0)}\" — {note}")
    return findings


def self_test(bans):
    fx = load_fixtures()
    bad = []
    for bid, rx, raw, _ in bans:
        if bid not in fx:
            bad.append(f"{bid}: no fixture in fixtures.tsv — a ban nobody has proven fires")
            continue
        for s in fx[bid]:
            if not rx.search(s):
                bad.append(f"{bid}: fixture does not fire: \"{s}\"  (regex: {raw})")
    for bid in fx:
        if bid not in {b[0] for b in bans}:
            bad.append(f"{bid}: fixture with no ban")
    return bad


def main():
    bans = load_bans()
    args = sys.argv[1:]
    if "--test" in args:
        bad = self_test(bans)
        for b in bad:
            print("FAIL " + b)
        print(f"bans.py --test: {len(bans)} bans, {'ALL FIRE' if not bad else str(len(bad)) + ' problem(s)'}")
        return 2 if bad else 0
    if "--list" in args:
        for bid, _, raw, note in bans:
            print(f"{bid}  {raw}   # {note}")
        return 0
    if not args:
        print(__doc__); return 0
    total = []
    for p in args:
        total += check_file(p, bans)
    for f in total:
        print(f)
    return 2 if total else 0


if __name__ == "__main__":
    sys.exit(main())
