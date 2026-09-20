#!/usr/bin/env python3
"""variance-draw.py — the least-recently-used card, computed, not remembered.

    python3 studio/tools/variance-draw.py <agent>            # print the LRU card for that agent's deck
    python3 studio/tools/variance-draw.py <agent> --log "<what the run is>" "<how the card is read>" "<output path>"
                                                             # …and append the LOG row

Decks: studio/agents/variance/DECKS.md (the deck's letter is the one
whose heading names the agent). History: studio/agents/variance/LOG.md
(a card's last use by THIS agent). RETIRED cards are never dealt. The
third instrument audit (F55, 2026-09-20) found the hand-kept LRU wrong
more often than right: the keeper drew E4 twice with E6 idle, the
drafter skipped D1 four times. This is the draw.
"""
from __future__ import annotations
import os, re, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
V = os.path.join(HERE, "..", "agents", "variance")


def decks():
    out = {}
    cur = None
    for line in open(os.path.join(V, "DECKS.md"), encoding="utf-8"):
        h = re.match(r"^## (.+)", line)
        if h:
            cur = h.group(1); out.setdefault(cur, [])
            continue
        m = re.match(r"^\| ([A-Z]\d+) \| (.+?) \|", line)
        if m and cur:
            out[cur].append((m.group(1), m.group(2).strip()))
    return out


def deck_for(agent):
    for heading, cards in decks().items():
        if agent in heading:
            return heading, cards
    return None, []


def last_use(agent):
    """card id → date of that agent's last draw of it (rows are chronological)."""
    seen = {}
    for line in open(os.path.join(V, "LOG.md"), encoding="utf-8"):
        m = re.match(r"^\| (\d{4}-\d{2}-\d{2}) \| ([^|]*)\| ([A-Z]\d+)\b", line)
        if not m:
            continue
        date, who, card = m.group(1), m.group(2), m.group(3)
        if agent.split("-")[0] in who:
            seen[card] = date
    return seen


def draw(agent):
    heading, cards = deck_for(agent)
    if not cards:
        return None, None, f"no deck names '{agent}' in DECKS.md"
    used = last_use(agent)
    live = [(cid, txt) for cid, txt in cards if not txt.upper().startswith("RETIRED")]
    live.sort(key=lambda c: (used.get(c[0], "0000-00-00"), c[0]))
    cid, txt = live[0]
    return cid, txt, f"deck '{heading}'; last used {used.get(cid, 'never')}"


def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    agent = sys.argv[1]
    cid, txt, why = draw(agent)
    if not cid:
        print(why, file=sys.stderr); return 2
    print(f"{cid}  {txt}   ({why})")
    if "--log" in sys.argv:
        i = sys.argv.index("--log")
        what, how, out = (sys.argv[i+1:i+4] + ["", "", ""])[:3]
        row = f"| {datetime.date.today()} | {agent} ({what}) | {cid} {txt} (LRU by variance-draw.py; read as: {how}) | {out} |\n"
        with open(os.path.join(V, "LOG.md"), "a", encoding="utf-8") as f:
            f.write(row)
        print("logged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
