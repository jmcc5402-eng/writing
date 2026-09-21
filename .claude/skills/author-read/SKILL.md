---
name: author-read
description: Draft THE AUTHOR'S READ table for a chapter brief — the author's seven standing questions (MORE, WHO, CONFUSING, NOSE, POINT, SENSES, FUN) answered one line per scene, before any drafter launches. Use on every chapter brief from ch 23; brief-gate refuses a drafter without it.
---

# /author-read plots/brief-chNN.md

The author's comments, asked before the page exists. The six
questions are in `studio/AUTHOR-QUESTIONS.md`, in the author's words.

1. Read the card (`notes/cards/chNN-card.md`), the matrix row
   (`python3 studio/tools/matrix-strip.py <book> NN --row`), the
   brief's THE SCENES, the book's `canon/STAKES.md` (the pull table),
   `THREADS.md` hands-forward into this chapter, and the last three
   chapters' keeper and panel files (what was handed forward).
2. For every numbered scene in THE SCENES write one table row:

   ```
   ## THE AUTHOR'S READ (studio/AUTHOR-QUESTIONS.md; L056)

   | Scene | MORE | WHO | CONFUSING | NOSE | POINT | SENSES | FUN |
   |---|---|---|---|---|---|---|---|
   | 1. The morning | — (no touch; the ache at l.x: one paragraph, where she feels it; romance felt 3) | Verna: wants the rent; pull — the tenant vs the town; LIKE, warily; conflict 1 | clock: 6:10, boots on, the phone face down since last night; "the copies" = the letter's copies to the trustees, said | the drink is seen, never named | the point: she reads it once and goes to work; the stake BLATANT: what exactly happens if — quote the sentence | the lot after the thaw: gravel, water in the ruts, the RAV4 back | a downer by design; what takes the edge off: Verna's one line at the window |
   ```

   A cell is one line. "—" is allowed with a reason. MORE carries a
   COUNT at any touch or proximity (four or more body beats at a key
   moment) and names the ache paragraph in any apart section.
3. Put the section in the brief ABOVE the audit addendum, so the
   keeper audits it with the rest.
4. Run `python3 studio/tools/brief-gate.py <brief>`; it counts the
   rows against THE SCENES.

The table is a plan for the drafter, not a checklist for the panel:
the drafter gets it verbatim in the launch prompt. `author-proxy`
reads the draft against the same six questions afterwards.
