#!/usr/bin/env python3
"""ack.py — a finding that is already tracked or already ruled stops shouting.

    bash studio/tools/guardrails.sh | python3 studio/tools/ack.py --filter
    python3 studio/tools/ack.py --propose     # what is repeating and could be acked
    python3 studio/tools/ack.py --list        # the acknowledgements in force

WHY THIS EXISTS
On 2026-09-23 the suite printed **39 findings and 11 passes** in one run,
and most of the 39 were the same findings it had printed every day for a
week — six chapters flat (already HANDOFF H001), the opening echoes
(already H003), Book 1.1's em dashes on a book the author has shipped.

A suite that reports thirty-nine things every run is a suite people stop
reading, and a check nobody reads is an instruction again. That is the
failure this whole environment exists to prevent, and the environment had
grown it. Counting tools was the wrong measure of over-tooling; counting
UNCLOSED FINDINGS is the right one.

Two ways a finding goes quiet, and neither is deletion:

  TRACKED  it is already an open row on the handoff board. It prints as
           one line naming the row, not as a block. Nothing is lost: the
           board is what carries it to the thread that must act.
  RULED    the author has decided it. The row in ACKED.md carries who
           ruled, when, why, and what would bring it back.

An acknowledgement is never silent and never permanent: `--filter` always
says how many it suppressed and under which row. (L074)
"""
from __future__ import annotations
import fnmatch, os, re, sys

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ACKED = os.path.join(REPO, "studio", "threads", "ACKED.md")
BOARD = os.path.join(REPO, "studio", "threads", "HANDOFF.md")


def rows() -> list[dict]:
    """The acknowledgements: | Pattern | Kind | Ruled by | Why | Until |"""
    out = []
    try:
        text = open(ACKED, encoding="utf-8").read()
    except OSError:
        return out
    for line in text.splitlines():
        if not line.startswith("| `"):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) < 5:
            continue
        out.append({"pat": c[0].strip("`"), "kind": c[1].upper(), "by": c[2],
                    "why": c[3], "until": c[4]})
    return out


def open_handoff_ids() -> set[str]:
    ids = set()
    try:
        for line in open(BOARD, encoding="utf-8"):
            m = re.match(r"\|\s*(H\d{3})\s*\|", line)
            if m and line.strip().rstrip("|").strip().upper().endswith("OPEN"):
                ids.add(m.group(1))
    except OSError:
        pass
    return ids


def match(line: str, rs: list[dict]) -> dict | None:
    flat = " ".join(line.split())
    for r in rs:
        if fnmatch.fnmatch(flat.lower(), r["pat"].lower()):
            return r
    return None


def filter_stream() -> int:
    rs, live = rows(), open_handoff_ids()
    kept, hidden = [], {}
    stale = []
    for raw in sys.stdin.read().splitlines():
        if "✗" not in raw:
            kept.append(raw)
            continue
        r = match(raw, rs)
        if not r:
            kept.append(raw)
            continue
        # A TRACKED ack dies with its row: if the handoff row is closed, the
        # finding must come back, or closing a row would hide it forever.
        cited = re.findall(r"\bH\d{3}\b", r["why"])
        if r["kind"] == "TRACKED" and cited and not (set(cited) & live):
            kept.append(raw)
            if (r["pat"], cited[0]) not in stale:
                stale.append((r["pat"], cited[0]))
            continue
        key = f"{r['kind']}: {r['why'][:64]}"
        hidden[key] = hidden.get(key, 0) + 1
    print("\n".join(kept))
    if hidden:
        print(f"\n  acknowledged, not shown ({sum(hidden.values())} finding(s)) — studio/threads/ACKED.md:")
        for k, n in sorted(hidden.items(), key=lambda x: -x[1]):
            print(f"    {n:3d} ×  {k}")
    if stale:
        print("\n  an acknowledgement points at a CLOSED handoff row, so its findings are back:")
        for pat, hid in stale:
            print(f"    {hid} is closed → `{pat}` reports again. Delete the ACKED row or reopen {hid}.")
    return 0


def propose() -> int:
    """What is repeating enough to be worth a ruling."""
    text = sys.stdin.read() if not sys.stdin.isatty() else ""
    findings = [" ".join(l.split()) for l in text.splitlines() if "✗" in l]
    if not findings:
        print("ack: pipe guardrails.sh output in to see candidates")
        return 0
    groups: dict[str, int] = {}
    for f in findings:
        key = re.sub(r"\b\d+(\.\d+)?%?\b", "N", re.sub(r"\bch\d+\b", "chNN", f))
        key = re.sub(r"^.*?✗\s*", "", key)[:70]
        groups[key] = groups.get(key, 0) + 1
    rs = rows()
    print("ack: candidates — a shape the suite repeats, and whether it is already acked\n")
    for k, n in sorted(groups.items(), key=lambda x: -x[1]):
        if n < 2:
            continue
        acked = "acked" if match(k, rs) else "OPEN — worth a ruling"
        print(f"  {n:3d} ×  {k}   [{acked}]")
    return 0


def main() -> int:
    if "--filter" in sys.argv:
        return filter_stream()
    if "--propose" in sys.argv:
        return propose()
    rs, live = rows(), open_handoff_ids()
    if not rs:
        print("ack: no acknowledgements in force — every finding reports")
        return 0
    print(f"ack: {len(rs)} acknowledgement(s) in force\n")
    for r in rs:
        cited = re.findall(r"\bH\d{3}\b", r["why"])
        dead = " (ROW CLOSED — this ack no longer applies)" if r["kind"] == "TRACKED" and cited and not (set(cited) & live) else ""
        print(f"  [{r['kind']:<7}] `{r['pat']}`{dead}\n      {r['why']}  ({r['by']}; until {r['until']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
