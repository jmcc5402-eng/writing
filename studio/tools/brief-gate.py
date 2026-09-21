#!/usr/bin/env python3
"""brief-gate.py — no drafter launches on a brief that was never audited.

    (as a hook)  PreToolUse on the Agent tool. Reads the hook JSON on
                 stdin. If the agent is a drafting-assistant and its
                 prompt names a chapter brief, the brief must exist and
                 carry a real AUDIT ADDENDUM with a VERDICT. Exit 2
                 blocks the launch.
    python3 studio/tools/brief-gate.py books/<book>/plots/brief-chNN.md
                 checks one brief on the command line (exit 1 on fail).

WHY THIS EXISTS
2026-09-13, the ch 18 rewrite: the orchestrator's edit script wrote the
audited brief to a stray file; the copy in plots/ had no addendum; two
of three blind drafters worked from it. The fix that day was drafter
rule 8 — "a brief without its audit addendum is not a brief" — an
instruction the drafter has to remember (BACKLOG F36). This is the
same rule as a gate on the launch, so it cannot be forgotten by anyone.

What counts as audited: the brief contains a heading with
"AUDIT ADDENDUM" and, after it, a line beginning "VERDICT:" (bare,
as a heading, or in bold). A brief
whose addendum is a heading and nothing else is not audited.

A drafting-assistant prompt that names no brief at all is allowed
through with a note (line fixes, epigraph rewrites and heat passes
run without one); the note is the reminder, not a block.
"""
from __future__ import annotations
import json, os, re, sys

BRIEF_RE = re.compile(r"[\w./-]*plots/(?:brief|recut-briefs?)[\w-]*\.md")


def check(path: str) -> list[str]:
    if not os.path.isfile(path):
        return [f"brief not on disk: {path}"]
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^#+ .*AUDIT ADDENDUM", text, re.M)
    if not m:
        return [f"no AUDIT ADDENDUM in {os.path.relpath(path)} — the card and brief are audited together before a drafter launches (drafter rule 8; BACKLOG F36)"]
    tail = text[m.end():]
    # L031 (author, 2026-09-20): every named character on the page has a
    # stake the reader knows. From ch 22 a chapter brief carries a
    # "STAKES ON THE PAGE" section naming each one's stake and whose line
    # drops it (canon/STAKES.md is the sheet).
    STAKES_FROM = 22
    mch = re.search(r"brief-ch(\d+)\.md$", path)
    if mch and int(mch.group(1)) >= STAKES_FROM and not re.search(r"^#+ .*STAKES ON THE PAGE", text, re.M):
        return [f"no 'STAKES ON THE PAGE' section in {os.path.relpath(path)} — from ch 22 every named character on the page has a stake the reader knows (taste 22; canon/STAKES.md; L031)"]
    # L056 (the author, 2026-09-20: "implement my style of comments before
    # the chapter is written"): from ch 23 a chapter brief carries THE
    # AUTHOR'S READ — the six questions of studio/AUTHOR-QUESTIONS.md
    # answered one line per scene of THE SCENES.
    READ_FROM = 23
    if mch and int(mch.group(1)) >= READ_FROM:
        mr = re.search(r"^#+ .*THE AUTHOR'S READ", text, re.M)
        if not mr:
            return [f"no 'THE AUTHOR'S READ' section in {os.path.relpath(path)} — from ch 23 the author's six questions are answered per scene before a drafter launches (studio/AUTHOR-QUESTIONS.md; /author-read; L056)"]
        sect = text[mr.end():]
        nxt = re.search(r"^#+ ", sect, re.M)
        sect = sect[:nxt.start()] if nxt else sect
        rows = [ln for ln in sect.splitlines() if ln.startswith("|") and not re.match(r"^\|\s*-", ln) and not re.match(r"^\|\s*Scene\b", ln, re.I)]
        ms = re.search(r"^#+ .*THE SCENES", text, re.M)
        scenes = 0
        if ms:
            body = text[ms.end():]
            nx = re.search(r"^## ", body, re.M)
            body = body[:nx.start()] if nx else body
            scenes = len(re.findall(r"^\d+\. \*\*", body, re.M))
        need = scenes if scenes else 3
        if len(rows) < need:
            return [f"THE AUTHOR'S READ in {os.path.relpath(path)} has {len(rows)} row(s) for {need} scene(s) — one row per scene of THE SCENES (L056)"]
    if not re.search(r"^(#+ |\*\*)?VERDICT:", tail, re.M):
        return [f"the addendum in {os.path.relpath(path)} has no '## VERDICT:' line — a heading is not an audit"]
    if len(tail.split()) < 150:
        return [f"the addendum in {os.path.relpath(path)} is {len(tail.split())} words — too short to be the audit; paste the audit, not a pointer to it"]
    return []


def main() -> int:
    if len(sys.argv) > 1:
        rc = 0
        for p in sys.argv[1:]:
            probs = check(p)
            for x in probs:
                print(f"FAIL  {x}", file=sys.stderr)
            print(f"BRIEF GATE {os.path.relpath(p)}: {'FAIL' if probs else 'PASS'}", file=sys.stderr)
            rc = rc or (1 if probs else 0)
        return rc
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    ti = payload.get("tool_input") or {}
    kind = (ti.get("subagent_type") or "").lower()
    if "draft" not in kind:
        return 0
    prompt = ti.get("prompt") or ""
    root = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    briefs = sorted(set(BRIEF_RE.findall(prompt)))
    if not briefs:
        print("brief-gate: drafting-assistant launched with no brief named — fine for a line fix; a chapter draft names its brief.",
              file=sys.stderr)
        return 0
    problems: list[str] = []
    resolved: list[str] = []
    for b in briefs:
        p = b if os.path.isabs(b) else os.path.join(root, b)
        if not os.path.isfile(p):
            # the prompt may cite a bare plots/ path relative to a book dir
            hits = []
            for dp, _, fs in os.walk(os.path.join(root, "books")):
                for f in fs:
                    if os.path.join(dp, f).endswith(b):
                        hits.append(os.path.join(dp, f))
            p = hits[0] if len(hits) == 1 else p
        resolved.append(p)
        problems += check(p)
    # the matrix row must be in front of the drafter (matrix-strip.py; the
    # author, 2026-09-19: the matrix viewed before and after each chapter)
    for bp in resolved:
        mm = re.search(r"brief-ch(\d+)\.md", bp)
        if not mm:
            continue
        n = int(mm.group(1))
        bookdir = os.path.dirname(os.path.dirname(bp))
        tp = os.path.join(bookdir, "canon", "TARGETS.md")
        if not os.path.isfile(tp):
            continue
        rowline = ""
        for line in open(tp, encoding="utf-8"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 14 and cells[0] == str(n):
                rowline = (f"Romance {cells[2]} · Heat {cells[3]} · Aisha {cells[4]} · Dan {cells[5]} · Wound {cells[6]} · "
                           f"Fun {cells[7]} · Town {cells[8]} · Menace {cells[9]} · Ends {cells[10]} · Talk {cells[11]} · "
                           f"Words {cells[12]} · Pays {cells[13]}")
        if not rowline:
            problems.append(f"canon/TARGETS.md has no row for ch {n} — plan it before the draft")
        elif re.sub(r"\s+", " ", rowline).lower() not in re.sub(r"\s+", " ", prompt.replace("Laughs", "Fun")).lower():
            problems.append(f"the drafter's prompt does not carry the matrix row for ch {n} — paste it: '{rowline}'")
    for x in problems:
        print(f"FAIL  {x}", file=sys.stderr)
    if problems:
        print("BLOCKED: the drafter does not launch until the brief on disk carries its audit addendum (studio/tools/brief-gate.py).",
              file=sys.stderr)
        return 2
    print(f"brief-gate: {', '.join(os.path.relpath(b) if os.path.isabs(b) else b for b in briefs)} audited — go.",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
