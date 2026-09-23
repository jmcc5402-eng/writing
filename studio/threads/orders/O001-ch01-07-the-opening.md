# O001 — the cold opening: a floor forward, and one bounded question back

Status: OPEN · For: story · Raised: 2026-09-24 by the environment thread
Board: HANDOFF H008 · Ledger: L073, L078, L079

> **Re-scoped 2026-09-24 on the author's standing ruling (note 251):**
> *"an anti-pattern is for us to continually look backwards at stuff
> that's already written… I'd rather focus our efforts on building the
> guard rail, so future work is improved."*
>
> The first version of this order asked for a revision pass over seven
> finished chapters. That was the anti-pattern. **Most of this order is
> now forward.** The backward ask is three chapters, it is optional, and
> it is the author's call.

---

## GO LIGHT ON THE PAST

The measurement below is real and it is about chapters that are already
written. **It is not an instruction to rewrite them.** Its first job is
to set the floor for chapters that do not exist yet. Read the forward
section, do that work, and treat the backward section as a question you
bring back rather than a task you start.

## The forward fix — this is the work

**Every chapter from 25 on meets these floors before it is accepted.**
They are not new standards; they are the numbers the book already hits
when it is working (ch 21, the chapter the author liked after his own
notes landed).

| Floor | Number | Where it is checked |
|---|---|---|
| talk-to-body ratio | **under 2.0** (ch 21 = 1.46) | `chapter-lint`, TALK vs BODY |
| body words | never zero; **3+ per 1,000** | same line |
| the stake, said plain | once per chapter, same stake | `canon/STAKES.md`, ruled #185 |
| what was taken | named, with a line | `THE BILL`, the score's TESTS: line |
| sentences | 4+ commas is the finding, **not** length; one or two a chapter should run past thirty | `chapter-lint`, SENTENCES |

Nothing here needs the author. It is how ch 25 gets written.

## The forward fix that matters more — the next book

The reason ch 1–7 went cold is that **nothing looked at an opening until
the book was finished.** That is now fixed, and it is the real deliverable
of this order:

```
bash studio/tools/guardrails.sh --opening books/<book>
```

Run it the day chapter 3 of any book exists. Three chapters is the floor
— one or two hold too few markers to score. On Book 1.2 it would have
reported the cold sample at roughly 8,000 words instead of 64,000.

**For Books 1.3 and 1.4 this belongs at the outline, not the draft.** The
opening's temperature is set by who is in the room and what presses, and
both are fixed before a word is written. Ch 1–7 of 1.2 have the two leads
apart and the antagonist absent; no drafting pass fixes a structure like
that, which is precisely why this order does not ask for one.

## The backward question — bounded, optional, the author's call

Not seven chapters. **Three**, and only if he says the sample is
mission-critical.

```
  ch  words  POV  Menace | body/1k  talk%  talk:body
   1   2456  A      0    |    2.9   14.4      5.06
   2   2779  D      1    |    0.0   16.4      none
   3   2686  A      0    |    5.2   11.3      2.17
```

**Ch 2 contains no body words at all.** Ch 1–3 are the stretch a reader
downloads free, and three instruments built at different times — the
density survey, the superfan's retail read, the pressure curve — all
name this opening independently.

**The mission-critical test:** does a reader decide whether to buy Book
1.2 on these pages? If yes, this is worth a light pass. If Book 1.2 is
not shipping soon, it is not, and it waits.

**If the author says go, the ask is deliberately small:** body beats at
moments that are already charged in ch 1 and ch 2. No new scenes, no new
plot, no restructuring. Two or three sentences a chapter. Ch 3 is
already at 2.17 and can be left alone.

**Chapters 4–7 are explicitly out of scope.** They are worse on the
numbers and they are not the sample.

## What is NOT being asked for

- No pass over ch 4–7.
- No raising Menace in the written chapters — that is a plot change to a
  finished structure, and the fix belongs in the 1.3/1.4 outlines.
- No re-scoring of ch 1–20. Those rows in `TARGETS.md` are the readers'
  actuals, the panel runs about +1.8 against the author's scale, and
  correcting a historical record changes no page.

## Verify

```
bash studio/tools/guardrails.sh --opening books/campus-series/book2
bash studio/tools/chapter-lint.sh books/campus-series/book2/manuscript/ch25.md
```

DONE when ch 25 meets the floors and `--opening` is part of how a new
book starts. The backward question closes either way — a light pass, or
a ruling that the sample waits.
