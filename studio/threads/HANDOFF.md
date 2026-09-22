# The handoff board — findings one thread owes another

**Read by `studio/tools/handoff.py`.** Open rows addressed to a thread
are printed into that thread's context at SessionStart, and a row at
`BLOCK` holds the accept gate for the chapter it names.

## Why this is not a PR

A pull request is the **author's** decision channel: one PR, one thing
to rule on, merge is the record. It is the wrong pipe between two
agent threads, because it needs a human to carry the link across —
and a handoff that depends on somebody remembering is the failure this
studio keeps having. The superfan stopped running because a thread
forgot. Nothing decided it.

So findings ride the pipe that already reaches every thread on open,
and the ones that must not be skipped hold a gate. The PR stays for
what only the author can settle.

## The row

| Field | What it holds |
|---|---|
| `ID` | `H###`, minted once (`handoff.py --next`) |
| `For` | the scope that must act: `story` or `environment` |
| `Chapter` | the chapter it bites, `—` if none. A row with a chapter is checked at that chapter's gate |
| `Severity` | `NOTE` · `FIX` · `BLOCK` (see below) |
| `Finding` | one line, in plain words |
| `Detail` | where the evidence lives — a `BACKLOG` F-number, a `LEDGER` L-id, a notes file |
| `Status` | `OPEN` · `DONE` · `WONTFIX` (+ why) |

### Severity, and who may set it

- **`NOTE`** — worth knowing. Printed at SessionStart. Blocks nothing.
- **`FIX`** — the raising thread believes this should be done. Printed,
  and named at the chapter's gate as a soft line. Blocks nothing.
- **`BLOCK`** — the chapter does not pass its accept gate until the row
  is `DONE` or `WONTFIX`.

**Only the author sets `BLOCK`.** A row at BLOCK carries the author's
ruling in `Detail` (`author 2026-09-22 #183`), and `handoff.py` refuses
to honour a BLOCK without one. An agent thread may raise a finding at
FIX and argue for it; it may not hand itself a veto over another
thread's work. That asymmetry is deliberate: the environment thread
exists to serve the book, not to stop it.

## Open

| ID | For | Chapter | Severity | Finding | Detail | Status |
|---|---|---|---|---|---|---|
| H001 | story | — | FIX | Seven chapters running are metronomic (18–24, CV 0.52–0.57; ch 12–17 ran 0.78–0.89). Measured cause: **the long tail was amputated, not both ends.** p95 fell 38–68 → 27–32 and sentences over thirty fell 10–35% → 0.3–5%, while the mean barely moved — ch 12–14 had the same mean at CV 0.81–0.89 because they still carried sentences of 54–71 words. Rule 7 says *ordinarily* under thirty; the lint printed every one over thirty as a violation, so the hedge was lost and the drafter learned "never". `chapter-lint` now reports the distribution and flags a missing tail (L071). The page fix — letting one or two sentences run per chapter — is the book thread's. | `BACKLOG` F60, `LEDGER` L071; the story thread 2026-09-22: `plots/brief-ch25.md` BANS AND BUDGETS carries THE TAIL (one or two sentences run past forty; SENTENCE SHAPE read before delivering) and its proof line requires CV ≥ 0.60, p95 ≥ 33, one over thirty; `RECENT.md` carries it for every drafter run. The page closes it at ch 25's fold | OPEN |
| H002 | story | — | FIX | Taste 22 (be blatant: both get fired) and `STAKES.md` / D28.2 (hints only after ch 22) contradict each other. The proxy asked for it plain on ch 24, the drafter obeyed, the keeper BLOCKED citing D28.2. Every chapter now buys a revision round on that sentence until the author rules. | ch 24 keeper note, BLOCKING item 3; the story thread 2026-09-22: already before the author as PR #182's "Two things the keeper wants you to rule", item 1 (keep one plain saying per apart chapter and amend D30.1). Closes on the author's merge comment | OPEN |
| H004 | story | — | NOTE | Ch 25's card leaves three calls to the author inside the card rather than as their own DECISION PRs. The author (2026-09-21) asked that real questions reach him as PRs; PR-WORKFLOW rule 6's corollary calls a question parked in a note queue debt. | `studio/PR-WORKFLOW.md` rule 6; the story thread 2026-09-22: Kat's call was ruled the same day (L067) and struck; the two remaining (does she call Dan; the letter's text) go to the author as one [DECISION] PR the moment #182 merges — one branch can carry one open PR (BACKLOG F59), so it could not open beside #182 | OPEN |
| H005 | environment | — | FIX | Nothing forces the author-proxy to be scored against the author's real comments. The ch 23 score was written by hand; the fold gate does not require it. The one number that says whether this environment is learning can stop being computed and nothing would report it. | the 2026-09-20 study, proposal P3 (`comment-census.py`, never built) | OPEN |

## Closed

| ID | For | Finding | Outcome |
|---|---|---|---|
| H003 | story | Five shapes recur across ch 21–24 that no instrument reads (`said, to the <object>`; heart-in-hand→stomach-dropped; "in daylight"; "was the paper"; the alone-at-night ending) | DONE 2026-09-22 by the story thread: banned in `studio/agents/variance/RECENT.md` (drafting-assistant) and in `plots/brief-ch25.md`; the brief ends at Verna's storm door. A cross-chapter shape reader stays with the environment (`BACKLOG` F60) |

## Working it

A thread that acts on a row edits `Status` in the same commit as the
work, and says the ID in the commit subject. A thread that disagrees
sets `WONTFIX` with a reason in `Detail` — disagreeing in the file is
the point, because the next thread reads the file and not the
conversation where the two of you settled it.
