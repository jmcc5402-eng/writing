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
| H006 | story | — | FIX | The 2026-09-16 sameness pass edited ten ACCEPTED chapters (1.2 ch 1, 3, 5, 6, 9, 10, 11, 15, 17, 18) and merged with #183. prose-guard flagged every edit; the continuity-keeper read that re-accepts folded prose was never run. The changes are documented in full in `book2/CHANGELOG.md` under the two 2026-09-16 entries. Fold the keeper read into the next page audit. | `BACKLOG` F61, `book2/CHANGELOG.md` 2026-09-16 | OPEN |
| H007 | story | — | FIX | **The body/romance ask is the author's most-repeated note — six times since its first fix shipped** (#219, 222, 234, 237, 242, 244), more than any other shape. Measured cause: the fix landed on one chapter and decayed in the next. Talk-to-body ratio as `chapter-lint` reports it: ch 21 **1.46** (the chapter he liked, after his comments — 29 body words) → ch 22 **16.18** (four body words in the whole chapter) → ch 23 **4.67** (he rated it romance 3) → ch 24 **5.11** (nine body words). Only ch 21 is under the 2.0 line. `TOUCH SPAN` could not see it: it reads one chapter at its highest touch cluster, and ch 22 had no cluster. `chapter-lint` now carries a whole-chapter TALK vs BODY line (L073). Aim ch 25 at ch 21's ratio, not ch 22's. | `LEDGER` L073, `notes/romance-levels.md` | OPEN |
| H008 | story | — | FIX | **The antagonist moves in 6 of 30 chapters (20%), and ch 1–7 run at Menace 1 or less** — seven chapters at the opening where nothing presses, which is also the stretch a reader downloads free. The author (2026-09-23): *"not only do we need to say the stakes, the stakes need to be high."* A threat stated every chapter and collected in a handful reads low however blatantly it is said. `stakes-check.py` reports the curve; the judgement of whether a stake is high stays a reader's. | `LEDGER` L078; the work order is `studio/threads/orders/O001-ch01-07-the-opening.md` — per-chapter numbers, the target, the constraints, and the three rulings the author owes first | OPEN |
| H005 | environment | — | FIX | Nothing forces the author-proxy to be scored against the author's real comments. The ch 23 score was written by hand; the fold gate does not require it. The one number that says whether this environment is learning can stop being computed and nothing would report it. | the 2026-09-20 study, proposal P3. PARTLY DONE 2026-09-23: `comment-census.py` measures shape recurrence and `calibration.py` measures the readers' error against the author's number (2 points so far, floor is 3). Still owed: the proxy's own SAID/MISSED/NEW score per chapter, required by the fold gate rather than written by hand. | OPEN |
| H009 | story | — | FIX | **The author retired "closed door" and 1.2 steps toward the new line from the next chapter — gradually.** The line is now BODY WORDS, not the first garment: on the page, kissing, any touching, clothes coming off, the certainty they will spend the night, touching under clothing away from sensitive spots; off the page, explicit anatomical words and the act (fade). Consent: both clear-headed when a scene turns intimate — buzzed yes, drunk or high no; too much and an outside obstacle breaks it up. Banter: crude intent yes, crude or demeaning language never. Swearing unchanged. Ch 22–30 climb a notch at a time; accepted ch 1–21 stay; **ch 29 is outlined "cut at the garment" — re-brief it under the new line.** | `AUTHOR-NOTES` 255–258 | OPEN |
| H010 | story | — | FIX | Record the 2026-09-23 rulings in canon, by PR: amend STANDARDS 9 (the body-word line, replacing closed door, and its packaging clause), add the consent wall, answer STANDARDS 16's swearing [TK] (unchanged — earns its place, never for shock); update DIALS (edge 1.1 = 2, 1.2 = 5, 1.3 = 7, 1.4 = 5–6; 1.3 modernity 7, superseding the 2026-09-16 hold at 3; the one-click rule superseded for Set 1). VISION's adjacency sentence needs the same note. | `AUTHOR-NOTES` 254, 255, 257–259 | OPEN |
| H011 | story | — | NOTE | **Book 1.3's direction is planned and ruled** — spring, baseball as the calendar, Priya meeting this world late, Marcus's betting debt and custody weekends, Ty and Mackenzie back, three steamy side couples, two or three side quests, weed allowed and nothing stronger, 65–70k words. It is planning only: 1.2 finishes first, and no 1.3 prose until the author approves the arcs (PIPELINE §3b). The next 1.3 deliverables are the premise PR and the arc docs. | `books/campus-series/notes/book3-direction-2026-09-23.md`; `AUTHOR-NOTES` 254, 261–264 | OPEN |
| H012 | environment | — | NOTE | The superfan's packaging check reads for "the closed door I was promised" (`.claude/agents/superfan-reviewer.md:33`). The series now promises FADE TO BLACK; the check should read against that. The planning thread (`claude/new-writing-repo-xkfdj2`) is plans-only by the author's ruling (AUTHOR-NOTES 265) and has no lock — the environment lock would also refuse its planning notes, so a planning scope may be worth building. | `AUTHOR-NOTES` 260, 265 | OPEN |

## Closed

| ID | For | Finding | Outcome |
|---|---|---|---|
| H004 | story | Ch 25's card leaves three calls to the author inside the card rather than as their own DECISION PRs. The author (2026-09-21) asked that real questions reach him as PRs; PR-WORKFLOW rule 6's corollary calls a question parked in a note queue debt. | DONE 2026-09-23 by the story thread: ch 25's two remaining calls went to the author in #190 as B2-D31.7 (she does not call Dan) and D31.8 (the Cordelia letter's last line, blessed); merged |
| H002 | story | Taste 22 (be blatant: both get fired) and `STAKES.md` / D28.2 (hints only after ch 22) contradict each other. The proxy asked for it plain on ch 24, the drafter obeyed, the keeper BLOCKED citing D28.2. Every chapter now buys a revision round on that sentence until the author rules. | DONE 2026-09-23 by the story thread: the author merged #185 (the stake said plain once per chapter, the same stake each time); B2-D28.2, D30.1 and F-DAN-02 amended at the ch 24 fold, and STAKES.md marks the rule RULED |
| H003 | story | Five shapes recur across ch 21–24 that no instrument reads (`said, to the <object>`; heart-in-hand→stomach-dropped; "in daylight"; "was the paper"; the alone-at-night ending) | DONE 2026-09-22 by the story thread: banned in `studio/agents/variance/RECENT.md` (drafting-assistant) and in `plots/brief-ch25.md`; the brief ends at Verna's storm door. A cross-chapter shape reader stays with the environment (`BACKLOG` F60) |

## Working it

A thread that acts on a row edits `Status` in the same commit as the
work, and says the ID in the commit subject. A thread that disagrees
sets `WONTFIX` with a reason in `Detail` — disagreeing in the file is
the point, because the next thread reads the file and not the
conversation where the two of you settled it.
