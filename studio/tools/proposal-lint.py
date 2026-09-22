#!/usr/bin/env python3
"""proposal-lint.py — a documented page change the writer thread can apply blind.

    python3 studio/tools/proposal-lint.py                    # every open proposal
    python3 studio/tools/proposal-lint.py <file.md>          # one
    python3 studio/tools/proposal-lint.py --list             # the board, one line each

Exit 0 = every open proposal is applicable as written. Exit 2 = one is not.

WHY THIS EXISTS
The author, merging #183 (2026-09-22): *"Instead of making any changes
just document your changes to any chapters so I can provide to my writer
threads."*

`thread-scope.py` already stops this thread editing a chapter. A lock
that stops the wrong thing does not produce the right thing, though, and
"document it" degrades on its own: the note says "tighten the tag in ch
22" and the writer thread has to go find what that means, guess which
three lines, and decide what to put instead. That is not a handoff, it is
homework.

So a proposal is a file with a fixed shape, and the shape is checked:

  NOW must appear in the named file, byte for byte.

That one rule is what makes the thing applicable without judgement — the
writer thread can search for NOW and replace it with PROPOSED. It also
makes a stale proposal impossible to miss: if the page moved under it,
the lint fails and says so, instead of a writer thread silently applying
a patch to prose that has changed. (L072)
"""
from __future__ import annotations
import glob, os, re, sys

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DIR = os.path.join(REPO, "studio", "threads", "proposals")
NEEDED = ["What", "Found by", "Where", "Now", "Proposed", "Why", "Verify"]


def parse(path: str) -> dict:
    text = open(path, encoding="utf-8").read()
    out = {"_status": "OPEN", "_blocks": {}}
    m = re.search(r"^Status:\s*(\w+)", text, re.M)
    if m:
        out["_status"] = m.group(1).upper()
    for sec in NEEDED:
        m = re.search(rf"^##\s+{re.escape(sec)}\s*$\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        out[sec] = m.group(1).strip() if m else None
        if out[sec]:
            fences = re.findall(r"^```[^\n]*\n(.*?)^```", out[sec], re.M | re.S)
            if fences:
                out["_blocks"][sec] = fences[0].rstrip("\n")
    return out


def check(path: str) -> list[str]:
    p, rel = parse(path), os.path.relpath(path, REPO)
    if p["_status"] != "OPEN":
        return []
    bad = [f"{rel}: no '## {s}' section" for s in NEEDED if not p.get(s)]
    if bad:
        return bad

    where = p["Where"].strip().strip("`")
    fm = re.match(r"([^\s:]+)", where)
    target = os.path.join(REPO, fm.group(1)) if fm else None
    if not target or not os.path.isfile(target):
        return [f"{rel}: Where names no file that exists: '{where}'"]

    for sec in ("Now", "Proposed"):
        if sec not in p["_blocks"]:
            bad.append(f"{rel}: '## {sec}' must be a fenced block holding the exact text")
    if bad:
        return bad

    now, prop = p["_blocks"]["Now"], p["_blocks"]["Proposed"]
    if now == prop:
        bad.append(f"{rel}: Now and Proposed are identical")
    body = open(target, encoding="utf-8").read()
    if now not in body:
        bad.append(f"{rel}: the Now block is NOT in {fm.group(1)} byte for byte — "
                   f"the page moved under this proposal, or it was transcribed by hand. "
                   f"A writer thread cannot apply it. Re-read the file and rewrite Now.")
    elif body.count(now) > 1:
        bad.append(f"{rel}: the Now block appears {body.count(now)} times in {fm.group(1)} — "
                   f"quote more context so the replacement is unambiguous")
    if not re.search(r"`[^`]+`|^\s{4}\S|^```", p["Verify"], re.M):
        bad.append(f"{rel}: Verify must name a runnable command")
    return bad


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    files = args or sorted(glob.glob(os.path.join(DIR, "P*.md")))
    if not files:
        print("proposal-lint: no proposals")
        return 0
    if "--list" in sys.argv:
        for f in files:
            p = parse(f)
            print(f"  {os.path.basename(f):<34} {p['_status']:<8} {(p.get('What') or '').splitlines()[0][:70]}")
        return 0
    problems = []
    for f in files:
        problems += check(f)
    n_open = sum(1 for f in files if parse(f)["_status"] == "OPEN")
    if problems:
        print(f"proposal-lint: {len(problems)} problem(s) across {n_open} open proposal(s)", file=sys.stderr)
        for x in problems:
            print(f"  ✗ {x}", file=sys.stderr)
        print("  A proposal the writer thread cannot apply blind is not documentation.", file=sys.stderr)
        return 2
    print(f"proposal-lint: {n_open} open proposal(s), every one applicable as written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
