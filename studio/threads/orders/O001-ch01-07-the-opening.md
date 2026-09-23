# O001 — the opening stretch, 1.2 ch 1–7

Status: OPEN · For: story · Raised: 2026-09-24 by the environment thread
Board: HANDOFF H008 · Ledger: L073, L078

**This is a work order, not a proposal.** A proposal carries exact
replacement text (`/propose`). This carries numbers, a target and a
verification, and leaves every craft decision to the drafter and the
author. Nothing in it names a scene to write.

---

## Why this stretch, and not another

Three instruments built at different times, for different reasons, all
point at the same seven chapters. That has not happened before.

| Instrument | Finding | Date |
|---|---|---|
| `romance-reader-panel` density survey | ch 1–10 run **26% romance-forward** against **54%** for ch 11–19 | 2026-09-14 |
| `superfan-reviewer` retail read | Book 1.2 demoted to *borrow-worthy*; the sample is the coldest opening of either book | 2026-09-14 |
| `stakes-check` pressure curve | **ch 1–7 run at Menace 1 or less** — the longest stretch in the book where nothing presses | 2026-09-23 |

This is also the stretch a reader downloads free.

## The measurement, per chapter

```
  ch  words  POV   Rom Heat Wound Menace Fun  | body/1k  talk%  talk:body
   1   2456  A      3    1     1      0   1  |    2.9   14.4      5.06
   2   2779  D      4    2     1      1   1  |    0.0   16.4       n/a
   3   2686  A      5    2     1      0   1  |    5.2   11.3      2.17
   4   2658  D      6    3     2      0   3  |    0.4   28.2     74.90
   5   2660  A      6    3     2      0   1  |    0.0   24.8       n/a
   6   3131  D      5    2     1      0   3  |    0.6   15.8     24.70
   7   2928  A      6    4     2      1   3  |    3.1   21.6      7.02
```

**Chapters 2 and 5 contain no body words at all.** Not few — none. Ch 4
has one, in 2,658 words, on a page the sheet scores Heat 3.

For scale: ch 21, the chapter the author liked after his own notes were
applied, runs **talk:body 1.46**. Every chapter here is over the 2.0
line and five are over 5.

## Do not trust the Rom and Heat columns in that table

Rows 1–20 of `canon/TARGETS.md` are the **readers' actuals**, not a
plan. So the panel scored ch 5 at romance 6 and heat 3 on a chapter
with zero body words in it.

The author's ruling of 2026-09-21 says romance needs **conflict between
the two of them on the page** — longing alone is a 3 — and heat counts
**only with both in a room**. Measured against his own scale, these
numbers are high; `calibration.py` has the panel running **+1.8** on two
paired readings and the floor for judging is three.

**Re-score this stretch against the author's anchors before planning
anything.** The old numbers are the instrument's, not his.

## What done looks like

Numbers, because "warmer" is what failed for five weeks.

1. **talk:body under 2.0 in every chapter.** Ch 21 is the reference at
   1.46. This is not a word-count exercise: the ratio moves when the POV
   character's body is on the page at the moments that are already
   charged, not when adjectives are added.
2. **No chapter at zero.** Ch 2 and ch 5 are the hard floor case.
3. **Menace above 1 in at least two of the seven.** The antagonist moves
   in 6 of 30 chapters across the whole book; seven consecutive at 0–1
   is the part that reads as nothing at stake.
4. **The romance-forward share of ch 1–7 at or above 40%**, against 26%
   for ch 1–10 today. Book 1.1 and the back half of 1.2 both sit near
   40%; this is parity, not escalation.

## Constraints

- **Heat stays closed-door.** `DIALS.md`, and the author's standing
  ruling. Raising the ratio means the body reacting, not the door
  opening.
- **The plot does not move.** Beats, reveals and the calendar are fixed
  by `BEATS.md` and the keeper's clock; this stretch gets denser, not
  different.
- **The registers are live.** Aisha's seltzer is seeded in ch 3, 5 and 6
  and spent at ch 11; her coat shifts at ch 7. Do not spend either
  early — `register-check.py` will catch it.
- **The stake is said plain once per chapter**, the same stake each time
  (`canon/STAKES.md`, ruled on #185).
- One or two narration sentences per chapter **should** run past thirty
  words, and four or more commas in one is the finding, not the length
  (rule 7, ruled on #186).

## What the author must rule before drafting

1. **Is this a pass or a recut?** Denser inside the existing scenes, or
   new material in the stretch? A pass is cheap and bounded; a recut
   touches the outline. The measurement does not answer this.
2. **Menace in ch 1–7.** Raising it means Boyd acts earlier than the
   outline has him act — that is a plot change and it is his.
3. **Ch 2 and ch 5 are Dan and Aisha alone.** Reaching parity may need
   them in a room together earlier, which is a structural question.

## Verify

Every number above regenerates from the repo. Re-run after the pass:

```
bash studio/tools/chapter-lint.sh books/campus-series/book2/manuscript/ch0N.md
python3 studio/tools/stakes-check.py books/campus-series/book2
python3 studio/tools/calibration.py books/campus-series/book2
```

The order is DONE when the four numbers under "what done looks like"
hold and the author has given his own romance number for at least one
chapter in the stretch — that last one is what makes the rest
trustworthy.
