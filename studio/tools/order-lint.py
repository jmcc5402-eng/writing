#!/usr/bin/env python3
"""order-lint.py — a work order leads with the forward fix.

    python3 studio/tools/order-lint.py                 # every open order
    python3 studio/tools/order-lint.py <file.md>

Exit 0 = every open order is forward-first, or justifies its backward ask.
Exit 2 = one asks for work on finished chapters without saying why.

WHY THIS EXISTS
The author, 2026-09-24: *"I generally wanna focus on future books more
than the existing or previous books. I think an anti-pattern is for us
to continually look backwards at stuff that's already written… I'd
rather focus our efforts on building the guard rail, so future work is
improved."*

He is describing something this thread had just done. O001's first
version took a real measurement — ch 1-7 are cold, three instruments
agree — and turned it into a revision pass over seven finished chapters.
That is the anti-pattern, written by the thread whose job is to stop
anti-patterns, on the same day.

The pull is structural, not careless: a measurement of the past is the
easiest thing to act on, because the pages exist and the numbers are
already computed. The forward fix is harder to write and pays more. So
the default has to be enforced rather than remembered.

An order may ask for backward work. It has to say why, against a named
test, and it has to be small. Over three chapters is a warning; no
justification at all is a refusal. (L079)
"""
from __future__ import annotations
import glob, os, re, sys

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DIR = os.path.join(REPO, "studio", "threads", "orders")
BACKWARD_WARN = 3          # chapters; above this a backward ask is a warning
# Phrases that mean "go change pages that already exist".
BACKWARD = re.compile(
    r"\b(revision pass|revise|rewrite|recut|re-?cut|pass over|fix ch\s?\d|"
    r"raise .{0,20}\bin ch\s?\d|go back)\b", re.I)
FORWARD_HEAD = re.compile(r"^##+\s.*\bforward\b", re.I | re.M)
WHY_BACK = re.compile(r"^##+\s.*\b(why backward|backward question|mission.?critical)\b", re.I | re.M)
CH_RANGE = re.compile(r"\bch\s?(\d{1,2})\s*[–-]\s*(\d{1,2})\b", re.I)


def sections(text: str) -> list[str]:
    return re.findall(r"^##+\s+(.+)$", text, re.M)


def check(path: str) -> list[str]:
    text = open(path, encoding="utf-8").read()
    rel = os.path.relpath(path, REPO)
    if re.search(r"^Status:\s*(DONE|WONTFIX)", text, re.M):
        return []
    bad = []

    asks_back = bool(BACKWARD.search(text))
    if not FORWARD_HEAD.search(text):
        bad.append(f"{rel}: no section whose heading names the FORWARD fix. "
                   f"An order leads with what changes for the chapters that do "
                   f"not exist yet (L079)")
    if asks_back and not WHY_BACK.search(text):
        bad.append(f"{rel}: asks for work on written chapters with no "
                   f"'## Why backward' or mission-critical section. Say what test "
                   f"the backward ask passes, or drop it")

    # How wide is the backward ask? Count ranges ONLY inside a section that
    # actually asks for backward work, and never inside a section whose
    # heading is a negation. The first run of this check flagged O001 for
    # "ch 1-20" quoted under "What is NOT being asked for" — the opposite
    # of a backward ask. A check that cries wolf gets switched off.
    if asks_back:
        widest = 0
        blocks = re.split(r"^(##+\s+.+)$", text, flags=re.M)
        for i in range(1, len(blocks), 2):
            head, body = blocks[i], blocks[i + 1] if i + 1 < len(blocks) else ""
            if re.search(r"\bnot\b|\bNOT\b|out of scope", head):
                continue
            if not BACKWARD.search(body):
                continue
            for m in CH_RANGE.finditer(body):
                a, b = int(m.group(1)), int(m.group(2))
                widest = max(widest, abs(b - a) + 1)
        if widest > BACKWARD_WARN:
            bad.append(f"{rel}: the backward ask spans {widest} chapters "
                       f"(warn above {BACKWARD_WARN}). The author, 2026-09-24: "
                       f"\"go light on any changes in the past unless we really "
                       f"think they are mission critical\". Narrow it or split "
                       f"the forward half out")
    return bad


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    files = args or sorted(glob.glob(os.path.join(DIR, "O*.md")))
    if not files:
        print("order-lint: no orders")
        return 0
    problems = []
    for f in files:
        problems += check(f)
    if problems:
        print(f"order-lint: {len(problems)} problem(s) across {len(files)} order(s)", file=sys.stderr)
        for p in problems:
            print(f"  ✗ {p}", file=sys.stderr)
        print("  The forward fix is the work. The past is a question, not a task.", file=sys.stderr)
        return 2
    print(f"order-lint: {len(files)} order(s), every one forward-first")
    return 0


if __name__ == "__main__":
    sys.exit(main())
