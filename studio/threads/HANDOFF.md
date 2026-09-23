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
| H001 | story | — | FIX | Seven chapters running are metronomic (18–24, CV 0.52–0.57; ch 12–17 ran 0.78–0.89). Measured cause: **the long tail was amputated, not both ends.** p95 fell 38–68 → 27–32 and sentences over thirty fell 10–35% → 0.3–5%, while the mean barely moved — ch 12–14 had the same mean at CV 0.81–0.89 because they still carried sentences of 54–71 words. Rule 7 says *ordinarily* under thirty; the lint printed every one over thirty as a violation, so the hedge was lost and the drafter learned "never". `chapter-lint` now reports the distribution and flags a missing tail (L071). The page fix — letting one or two sentences run per chapter — is the book thread's. | `BACKLOG` F60, `LEDGER` L071 | OPEN |
| H002 | story | — | FIX | Taste 22 (be blatant: both get fired) and `STAKES.md` / D28.2 (hints only after ch 22) contradict each other. The proxy asked for it plain on ch 24, the drafter obeyed, the keeper BLOCKED citing D28.2. Every chapter now buys a revision round on that sentence until the author rules. | ch 24 keeper note, BLOCKING item 3 | OPEN |
| H003 | story | — | NOTE | Five shapes recur across ch 21–24 that no instrument reads, because every template check reads one chapter or one opening: the `said, to the <object>` tag (3/2/1), heart-in-hand→stomach-dropped in that order, "in daylight", "was the paper", and the banned alone-at-night ending three chapters running. Found by the developmental editor by hand on ch 24. One worked replacement is documented as `proposals/P001-ch22-tag-to-an-object.md`. | `BACKLOG` F60, proposal P001 | OPEN |
| H004 | story | — | NOTE | Ch 25's card leaves three calls to the author inside the card rather than as their own DECISION PRs. The author (2026-09-21) asked that real questions reach him as PRs; PR-WORKFLOW rule 6's corollary calls a question parked in a note queue debt. | `studio/PR-WORKFLOW.md` rule 6 | OPEN |
| H006 | story | — | FIX | The 2026-09-16 sameness pass edited ten ACCEPTED chapters (1.2 ch 1, 3, 5, 6, 9, 10, 11, 15, 17, 18) and merged with #183. prose-guard flagged every edit; the continuity-keeper read that re-accepts folded prose was never run. The changes are documented in full in `book2/CHANGELOG.md` under the two 2026-09-16 entries. Fold the keeper read into the next page audit. | `BACKLOG` F61, `book2/CHANGELOG.md` 2026-09-16 | OPEN |
| H007 | story | — | FIX | **The body/romance ask is the author's most-repeated note — six times since its first fix shipped** (#219, 222, 234, 237, 242, 244), more than any other shape. Measured cause: the fix landed on one chapter and decayed in the next. Talk-to-body ratio as `chapter-lint` reports it: ch 21 **1.46** (the chapter he liked, after his comments — 29 body words) → ch 22 **16.18** (four body words in the whole chapter) → ch 23 **4.67** (he rated it romance 3) → ch 24 **5.11** (nine body words). Only ch 21 is under the 2.0 line. `TOUCH SPAN` could not see it: it reads one chapter at its highest touch cluster, and ch 22 had no cluster. `chapter-lint` now carries a whole-chapter TALK vs BODY line (L073). Aim ch 25 at ch 21's ratio, not ch 22's. | `LEDGER` L073, `notes/romance-levels.md` | OPEN |
| H005 | environment | — | FIX | Nothing forces the author-proxy to be scored against the author's real comments. The ch 23 score was written by hand; the fold gate does not require it. The one number that says whether this environment is learning can stop being computed and nothing would report it. | the 2026-09-20 study, proposal P3. PARTLY DONE 2026-09-23: `comment-census.py` measures shape recurrence and `calibration.py` measures the readers' error against the author's number (2 points so far, floor is 3). Still owed: the proxy's own SAID/MISSED/NEW score per chapter, required by the fold gate rather than written by hand. | OPEN |

## Closed

| ID | For | Finding | Outcome |
|---|---|---|---|

## Working it

A thread that acts on a row edits `Status` in the same commit as the
work, and says the ID in the commit subject. A thread that disagrees
sets `WONTFIX` with a reason in `Detail` — disagreeing in the file is
the point, because the next thread reads the file and not the
conversation where the two of you settled it.
