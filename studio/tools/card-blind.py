#!/usr/bin/env python3
"""card-blind.py — the card with its Targets line struck, for a blind reader.

    python3 studio/tools/card-blind.py notes/cards/chNN-card.md [OUT.md]

The panel reads BLIND to the targets (the third audit, F48) — but the
card file carries the Targets line, and on ch 23 candidate B the panel
"saw the card's Targets line before it could skip." A reader cannot
un-see a line; the launch hands it this copy instead. Writes OUT.md
(default: the scratchpad-style path next to the card,
notes/cards/chNN-card-blind.md is NOT used — keep the repo clean; pass
a path under the session scratchpad) and prints it.
"""
import re, sys, os

def blind(text: str) -> str:
    # strike the "**Targets.**" block (the label line, the row line, and
    # the blank line after) wherever the card carries it
    return re.sub(r"\*\*Targets\.\*\*\s*\n+[^\n]*\n+", "", text, count=1)

def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    src = sys.argv[1]
    text = open(src, encoding="utf-8").read()
    out = blind(text)
    if re.search(r"Romance \d+ · Heat \d+", out):
        print("card-blind: a targets row survived — check the card's shape", file=sys.stderr); return 1
    dst = sys.argv[2] if len(sys.argv) > 2 else None
    if dst:
        os.makedirs(os.path.dirname(dst) or ".", exist_ok=True)
        open(dst, "w", encoding="utf-8").write(out)
        print(f"wrote {dst}")
    else:
        sys.stdout.write(out)
    return 0

if __name__ == "__main__":
    sys.exit(main())
