# O002 — pre-launch review of Book 1.1: glaring errors only

Status: OPEN · For: story · Raised: 2026-09-24 by the environment thread
Due: before 1.1 can release — `cycle.py --gate 1.1` holds the release
until `notes/prelaunch-review-<date>.md` exists with `VERDICT: SHIP`.
Ledger: L082

> The author, 2026-09-24: *"Honestly, I'm not convinced that 1.1 is done
> either. We made so many changes to the environment for book 2 at some
> point I might want to do a review of book one with some of our guard
> rails. I don't wanna change too much but we might look for glaring
> errors."*

## GO LIGHT ON THE PAST

This is the one legitimate backward job under the forward-first rule —
a book that is about to ship — and it is still **small**. The review
finds errors a reader would notice. It does not make a finished book
better. Book 1.1 keeps its grain (VISION, "Imperfection": *"if we make
every line of the book perfect it will seem fake"*).

## The forward fix

**Every glaring error this review finds becomes a check**, so Book 1.2
and 1.3 cannot ship the same one. That is the part that pays: the
review of one book is the test suite for the next three. File each as a
ledger row the day it is found.

Also forward: `front-matter.md` and `back-matter.md` for 1.1 become the
templates in `studio/series-kit/` for every later book, so no book is
"complete" again without them.

## Why backward — the mission-critical test

**Does a reader pay for these pages?** Yes: 1.1 is the next book to
ship. And there is a specific reason to look: it was edited after it
was marked complete. The 2026-09-15 heat pass changed about thirty
sentences across ch 1–15 and ch 26, the continuity sweep then found
**five blocking errors** in that pass, and nothing has read the whole
book since. Seams are where retrofit errors live.

## What "glaring" means — the whole test

**Would a reader notice it as a MISTAKE?** Not "would a critic prefer it
different." Only the first is in scope.

| In scope — BLOCKING, fix before release | Out of scope — DEFERRED, never touched in 1.1 |
|---|---|
| A continuity contradiction: a name, an age, a date, who knows what, where a room is | Style: em dashes, rhythm, openings, fragments (the five `ai-tells` findings are acknowledged) |
| Workshop text in the export | Romance density, warmth, "could be better" |
| A typo, a doubled or missing word, a sentence that breaks | Replacing a good sentence with a different good sentence |
| A thread the reader was promised and never paid (hard rule 5), when a reader would notice it dangling | A stronger version of anything that works |
| Formatting that breaks on a Kindle: an unclosed italic, a scene break that renders as text | Anything the panel liked |

A DEFERRED finding is not wasted. It goes on the ledger as a floor for
Book 1.3, which is where it can do some good.

## How

1. **The export first.** `python3 studio/tools/export-book.py
   books/campus-series` — the review reads what the reader will get.
2. **The heat-pass seams first**: ch 1–15 and ch 26, entering and
   leaving every changed sentence (the 2026-09-15 CHANGELOG entry lists
   them). That is where five blocking errors were found last time.
3. **Then the whole book, once, straight through**, for continuity.
4. **A line pass for typos only** — the line editor runs BEFORE the
   continuity keeper, never after (the editorial order in CLAUDE.md).
5. **Fixes as proposals.** Each BLOCKING finding becomes a `/propose`
   file with the exact before and after, applied by the book thread.

**Budget: if BLOCKING findings pass ten, stop and bring it to the
author.** At that point "not done" is the finding, and how much to fix
is his decision rather than the reviewer's.

## The file the gate reads

`books/campus-series/notes/prelaunch-review-<date>.md`: a table of
findings, each marked BLOCKING or DEFERRED with a line number, and a
final line —

    VERDICT: SHIP                  (no blocking findings)
    VERDICT: SHIP WITH FIXES DONE  (blocking findings, every one applied)
    VERDICT: HOLD                  (more than ten, or one the author must rule)

## When

The author's call. The gate only guarantees it happens **before**
release. The natural moment is when 1.2 nears completion, around 27 of
30: close enough to launch that 1.1 will not be touched again, and early
enough that fixes do not delay it.

## Verify

```
python3 studio/tools/export-book.py books/campus-series
python3 studio/tools/cycle.py --gate 1.1
```
