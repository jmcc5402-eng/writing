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
        problems += check(p)
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
