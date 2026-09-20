#!/usr/bin/env python3
"""catch-map.py — what would catch this, if it were wrong?

    python3 studio/tools/catch-map.py                # the working tree + index vs HEAD
    python3 studio/tools/catch-map.py origin/main    # everything on this branch vs main

For every changed file, names the hook, lint, gate or reader that would
fail if the change were wrong — and says GAP where nothing would. The
doc's /what-would-catch-this; gaps feed /lesson. (L035)
"""
from __future__ import annotations
import os, re, subprocess, sys

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# (regex on the path, what catches it, the gap if any)
MAP = [
    (r"books/.+/manuscript/ch\d+\.md$",
     "prose-guard (on the edit: columns, tics, bans.txt, added sentences); chapter-lint + dialogue-lint + opening-check + ending-check; fact-check; ai-tells; accept-gate (panel, keeper on folded prose, score, targets-check, TESTS line from ch 22)",
     "the prose's meaning — only the readers (panel, keeper) judge it, and only when the gate runs"),
    (r"books/.+/manuscript/ch\d+-candidate-[A-Z]\.md$",
     "prose-guard on the edit; chapter-lint by hand; the blind panel; the scoreboard",
     "nothing runs on a candidate until the showrunner lints it"),
    (r"books/.+/notes/cards/ch\d+-card\.md$",
     "card-lint (on send: 350 words, 30-word sentences, calls, sections, ledger words, the Targets line = the matrix row)",
     ""),
    (r"books/.+/plots/brief-ch\d+\.md$",
     "brief-gate (on the drafter's launch: AUDIT ADDENDUM + VERDICT ≥150 words; the matrix row in the prompt; STAKES ON THE PAGE from ch 22)",
     "the brief's facts — only the keeper's audit; a wrong line number is caught by nobody"),
    (r"books/.+/canon/FACTS\.md$", "fact-check (every regex greps every chapter; a bad regex is a silent no-op)", "a row whose regex never matches anything is not tested — add a fixture"),
    (r"books/.+/canon/TARGETS\.md$", "card-lint (the card must equal the row); targets-check at the gate; matrix-strip at session start", ""),
    (r"books/.+/canon/STAKES\.md$", "brief-gate demands the section; the panel's STANCE test", "the sheet's own consistency with DECISIONS — nobody greps it"),
    (r"books/.+/(DECISIONS|THREADS|STATE|CHANGELOG)\.md$", "accept-gate wants a CHANGELOG entry dated today; nothing else", "GAP: a decision that contradicts the page is caught only by the keeper at the next fold"),
    (r"books/.+/notes/(scores/)?ch\d+-.*\.md$", "accept-gate (the file must exist and be non-trivial); targets-check reads ACTUALS; scorecard reads scores", "a verdict's content — the gate checks presence, not judgment"),
    (r"books/.+/notes/furniture-registry\.md$", "nothing", "GAP: registry rows are read by the keeper by hand; fact-check does not read them"),
    (r"\.claude/agents/.+\.md$", "lesson-check (a reader test's name must be in the agent file); roster-staleness (cadence)", "GAP: an agent's instructions are never executed by a test — only its verdict file is"),
    (r"\.claude/skills/", "nothing", "GAP: a skill is a procedure; only its outputs are gated"),
    (r"\.claude/settings\.json$", "hook-check (every hook fed a bad input)", ""),
    (r"studio/tools/.+\.(py|sh)$", "hook-check for the hooks; bans.py --test for the bans; guardrails.sh runs the rest", "a tool that is not a hook has no test unless hook-check names it"),
    (r"studio/lessons/", "lesson-check; bans.py --test", ""),
    (r"studio/(STYLE|AUTHOR-TASTE|AUTHOR-NOTES)\.md$", "lesson-check (a recent author note needs a ledger row); canon-audit sorts the rules", "GAP: a rule in STYLE is an instruction until a ledger row names its enforcer"),
    (r"studio/agents/variance/", "accept-gate wants a draw logged today", "GAP: nothing checks a card was actually the LRU one"),
    (r"studio/.*\.md$", "pr-lint on the PR body only", "GAP: studio prose is governed by review"),
    (r"CLAUDE\.md$", "commit-scope enforces its one-scope rule; canon-audit", "the rest of CLAUDE.md is instruction"),
]


def changed(base: str | None):
    if base:
        out = subprocess.run(["git", "-C", REPO, "diff", "--name-only", f"{base}...HEAD"], capture_output=True, text=True).stdout
    else:
        out = subprocess.run(["git", "-C", REPO, "status", "--porcelain"], capture_output=True, text=True).stdout
        out = "\n".join(l[3:] for l in out.splitlines() if l.strip())
    return [l.strip() for l in out.splitlines() if l.strip()]


def main():
    base = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else None
    files = changed(base)
    if not files:
        print("catch-map: no changes"); return 0
    rows, gaps = [], 0
    for f in files:
        for rx, catch, gap in MAP:
            if re.search(rx, f):
                rows.append((f, catch, gap)); gaps += bool(gap); break
        else:
            rows.append((f, "nothing", "GAP: no check knows this path")); gaps += 1
    w = max(len(r[0]) for r in rows)
    print(f"catch-map  ({len(files)} file{'s' if len(files)!=1 else ''}{', vs ' + base if base else ''})")
    for f, catch, gap in rows:
        print(f"  {f:<{w}}  → {catch}")
        if gap:
            print(f"  {'':<{w}}    gap: {gap}")
    print(f"\n{gaps} of {len(rows)} changes have a gap — each one is a /lesson candidate (BAN, CHECK, GATE, READER, CANON or PROCESS).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
