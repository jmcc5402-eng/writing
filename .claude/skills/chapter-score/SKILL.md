---
name: chapter-score
description: Score a chapter (or a range) on the two things the book sells — the romance level and each lead's development — with a reader's number per chapter and one line of evidence, written to notes/scores/chNN-score.md and rolled up into notes/SCORECARD.md. Use after a chapter is drafted (before the panel's verdict is final), on any block of accepted chapters, or when the author asks "how much did this chapter move them?"
---

# /chapter-score

Two numbers a chapter, from readers, kept where a script can read them.

The author (2026-09-19): "Did we do any scoring on the level of romance
or character development? I'd like a skill that does that for each
chapter." Before this, the romance level existed from ch 17 on
(`notes/romance-levels.md`) and nothing scored development at all —
the dossiers said what each chapter *owed* a lead, and no one said
whether it paid.

## The scores

**ROMANCE LEVEL, 1–10** (the reader's scale, `notes/romance-levels.md`):
1 a normal old book with a couple in it somewhere · 5 she never
forgets what book she is reading, but nothing happened between them
she'd tell her group about · 10 she stayed up. The romance-reader-panel
gives it (panel 1.5.6's ACTUALS line already carries it for a fresh
draft; this skill asks for it on accepted chapters too).

**DEVELOPMENT, 0–3 per lead** (the developmental-editor gives it, one
number per lead per chapter, scored against the lead's dossier row for
that chapter and the beat map in `canon/BEATS.md`):
- **0 — not moved.** Absent, or present and the same person at the end
  as at the start.
- **1 — seen.** The reader learns one true new thing about who they are
  (a habit, a fear, a history said), and nothing they believe is tested.
- **2 — tested.** They do something at a cost, or a belief they hold is
  put under weight on the page and holds or cracks — the dossier's
  "kindness" row lands, or the wound is touched.
- **3 — turned.** An arc beat lands: the person at the end would
  decide something differently than the person at the start (the
  dossier's planned turn, or one the page earned that the dossier did
  not plan — say which).
A book should not score 3 every chapter; a run of 0s for a lead across
three chapters is a finding.

Each score comes with ONE line of evidence — the sentence on the page
that earns it, with its line number — or the number is not a score.

## How to run it

1. Name the chapter(s). Read the book's `canon/BEATS.md`, both
   dossiers' rows for those chapters, and `notes/romance-levels.md`.
2. Launch the two readers, blind to each other, in parallel:
   - `romance-reader-panel`: the ROMANCE LEVEL per chapter, one
     sentence why, the two-point fix. (Skip chapters already in
     `notes/romance-levels.md` unless re-scoring after an edit.)
   - `developmental-editor`: DEVELOPMENT per lead per chapter, the
     evidence line, and whether it matched the dossier's plan.
   Each draws its deck card (LRU from `studio/agents/variance/LOG.md`)
   and is logged.
3. File one `notes/scores/chNN-score.md` per chapter in this shape
   (the roll-up script parses it — keep the field names):

   ```
   # Score — ch NN "<title>" (<date>)
   ROMANCE: 6 — <one sentence> (panel)
   AISHA: 2 — <the line, l.NNN> (developmental-editor)
   DAN: 1 — <the line, l.NNN> (developmental-editor)
   PLAN: Aisha <matched|under|over> the dossier's row; Dan <…>
   ```
4. Run `python3 studio/tools/scorecard.py books/<book>` — it rolls every
   score file into `notes/SCORECARD.md` (one row per chapter, the
   author's own number from `romance-levels.md` beside the panel's) and
   flags: a lead at 0 three chapters running; a romance level two or
   more under the card's target; a chapter with no score file.
5. Commit under the book's prefix. The accept gate requires the score
   file from ch 21 on (`studio/tools/accept-gate.sh`).

## What this is not

Not a craft review. The numbers are a reader's and an editor's, not a
grade; the point is the shape across chapters — where a lead stalls,
where the romance drops — visible the week it happens instead of at
the box set. The scores never change a page by themselves; a low
number is a finding for the drafter, the brief, or the author.
