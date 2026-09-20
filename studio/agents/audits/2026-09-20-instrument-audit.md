# INSTRUMENT AUDIT 3 — campus 1.2, 2026-09-20 (E6)

instrument-auditor, card E6 (weight what's missing over what's wrong).
Filed by the orchestrator from the auditor's final message; the text
is the auditor's; the STATUS lines are the orchestrator's, the same
stint. Paths under the repo root; `book2/` = `books/campus-series/book2/`.
Run: every tool on ch 17–21, hook-check, bans --test, lesson-check,
accept-gate 20–21, the ch 22 card and brief through their gates, a
per-agent LRU reconstruction from the variance LOG.

## A. Catches no instrument caught

**F45 — MISS: the test set.** Every row 213–227 of AUTHOR-NOTES went
past an instrument on duty; the builds since would catch the next of
its kind for six of thirteen. (213 drinks aloud — NO: L013 bans "Beer
again" only; 214 the board's why — NO; 215 level vs count — PARTLY,
the gate anchors (F48); 216 Missy's want — YES if the STANCE test
runs; 217/218 the storm — NO, D5 still dealt (F49); 219 the touch —
YES; 220 place-stamp — 2 of 9 (F46); 221 wrong room — NO (L026); 222
the ache — YES; 223/224/227 stakes, POV — PARTLY.)
STATUS: F46, F48, F49 fixed below; L013 broadened to "any drink
explained aloud" is not greppable — stays a reader test (the panel's
JOKE/register read); L026 waits on the author's ch 12 ruling.

**F46 — BLIND SPOT: the place-stamp ban fired on two of the author's
nine exhibits**; the fixtures were invented sentences. FIX: fixtures
take the exhibits verbatim from the pages; the regex split into two
branches. STATUS: DONE — eight verbatim exhibits are fixtures; all
fire.

**F47 — BLIND SPOT: three enforcers verify attendance, not the
thing.** lesson-check exempted CANON rows; brief-gate checks the
STAKES heading exists; accept-gate greps the token so "stance
FINDING" passes. STATUS: lesson-check now requires a canon file
carrying the ID (L026, L030 re-classed INSTRUCTION with reasons);
accept-gate prints a FINDING as a note; the brief's STAKES rows per
NAMING name — BACKLOG.

**F48 — BLIND SPOT: the definition-of-done gate anchors.** All three
blind reads returned the card's Targets line to the digit. FIX: the
panel launched blind to the Targets line; targets-check warns when
actuals equal targets in every field. STATUS: DONE (the ECHO warning;
the ch 22 panel prompt carries no targets).

## B. Contradictions

**F49 — D5 orders the miss** (weather as texture, never as topic, vs
taste 17 amended). STATUS: D5 RETIRED.

**F50 — the talk floor is dead law**: dialogue-lint always exited 0.
STATUS: exits 2 below 8%; "one quiet per quarter" retired — the
matrix decides the band per chapter. Consequence: ch 21 stands
accepted at 7.5% (the author's additions were narration); the gate
would block it today; recorded, not retrofitted.

**F51 — ch 22's card and brief disagreed on the drafter count.**
STATUS: fixed on the card; card-lint now compares the card's phrase
with the brief's Status line.

**F52 — CADENCE vs PIPELINE on the red-team cadence; the tool
measures the agent name, not the deliverable.** STATUS: BACKLOG (a
deliverable token per CADENCE row; roster-staleness to match LOG
text). The red-team taste read is queued (the board's item 7).

**F53 — STALE: the second answer's numbers** (1,912 lines, not
1,700); the [FOLD] tag undefined in PR-WORKFLOW. STATUS: BACKLOG
(one line each).

## C. Rules that became templates

**F54 — OVER-TOOLED: seven catches, thirty-odd restatements, zero
retired.** FIX: the ledger row is the rule; STYLE and TASTE point at
LEDGER by ID; the brief's two stakes slots merged. STATUS: BACKLOG —
a refactor, the author's call on the shape.

## D. Drift

**F55 — the LRU draws are not LRU** (the keeper drew E4 twice with E6
idle; the drafter skipped D1 four times; the dev editor never drew
E1/E5). STATUS: `variance-draw.py` built — computes the LRU card from
DECKS and LOG and appends the row; ch 22's drafter drew D1 by it.

**F56 — the accept gate's continuity requirement could not fail** (any
*continuity*.md satisfied every chapter). STATUS: DONE — from ch 21
the gate requires `chNN-keeper-*.md`.

**F57 — the card lint guarded a door the pipeline does not use** (the
card rides in the listening file). STATUS: DONE — listening-file.py
refuses a card that fails the lint.

## E. Ghosts

**F58** — (a) ch 21 has no section seams (one 4,360-word section to
the ending check) — BACKLOG for the fold; (b) the THREADS edges header
— FIXED; (c) the ch 21 candidates sat in manuscript/ — MOVED to
notes/candidates/; (d) two housekeeping lines — the TASTE review line
FIXED; the agents CHANGELOG order left.

## THE TWO FIXES TO MAKE TODAY — both made
1. accept-gate requires the chapter's own keeper file (F56).
2. The panel blind to the Targets line (F48); dialogue-lint exits 2
   below 8% (F50).

## VERDICT (the auditor's)
Safer, yes: a drafter cannot launch unaudited, a commit cannot
straddle scopes, every ban has a fixture, and lesson-check proved
every catch of the window has a row — the lesson loop is real and it
caught a place-stamp three readers missed. The one place the room is
not safer is the verdicts it now trusts mechanically: the reader who
writes the ACTUALS line has read the target, the gate that "requires"
the keeper is satisfied by a file from the 15th, the talk floor
cannot fire, and the LRU draw is done by hand and wrong more often
than right. The environment moved the rules from prose to code, and
the code inherited the prose's habit of checking that a thing was
said rather than that it was so.

AUDIT DONE
