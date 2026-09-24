# The delivery thread — kickoff

**Written 2026-09-23 by the 1.3 planning thread, at the author's
request (AUTHOR-NOTES 266). Read this first when the delivery thread
opens.**

The author: *"you brought up great points earlier abuot packaging up
the books for being 'reader level' and ready to upload to amazon,
etc. I think i'm going to start a new thread just with that as a
goal."*

## What this thread is for

Turning finished books into the product a reader buys: the export,
the front and back matter, the cover, the description, categories and
keywords, EPUB and print files, pricing and Kindle Unlimited, and the
launch admin. **It never writes or edits a chapter.** A problem found
on a page becomes a proposal for the story thread (`/propose`).

## Do these first

1. `git fetch origin main`.
2. **Lock your branch out of the manuscripts.** Session branches get
   random `claude/...` names, and a branch `studio/threads/SCOPES.md`
   does not list is treated as a story thread that may edit prose. Add
   your branch to that table before anything else. (The `environment`
   scope may write `studio/**`, which is where launch material lives.)
3. Read: `studio/CYCLE.md` (the release rule) ·
   `studio/tools/export-book.py` (the reader-facing text) ·
   `studio/threads/orders/O002-prelaunch-review-1-1.md` (the story
   thread's pre-launch review) · `studio/gtm/kdp-launch-mechanics-
   2026-09-03.md` · `studio/gtm/sweet-smalltown-quartet-gtm-
   2026-09-15.md` · `books/campus-series/notes/series-name-pen-name-
   memo-2026-09-03.md`.

## Author rulings that change your work (2026-09-23)

- **The series moves from Clean & Wholesome to FADE TO BLACK**
  (AUTHOR-NOTES 260). The couple sleeps together; the scene fades
  before it happens. Fade to black is a promise stated in the book
  description, not an Amazon category — the categories become general
  small-town contemporary romance. Book 1.2 already carries a rationed
  swearing budget, which the clean shelf generally does not allow, so
  the move fixes that too.
- **Annie Farrow and Millrow stand** (#113), but their positioning
  copy was written for the clean shelf ("never 'steamy'"). Re-check
  comps, description vocabulary and categories against fade to black.
- **The release cycle:** 1.1 ships only when 1.2 is complete (21 of 30
  accepted as of 2026-09-23), with a clean export and a pre-launch
  review that says SHIP.

## The job, in order

1. **An inventory.** Everything a KDP launch of 1.1 needs, what exists,
   what doesn't, who must do it (you or the author), and how long it
   takes. Flag the long-lead items to start now — the waiting months
   are when launch admin gets done.
2. **Front and back matter for 1.1:** title page, copyright, a
   dedication placeholder, and a back page that sells 1.2. None exists.
3. **A clean export:** `export-book.py` producing 1.1 with no workshop
   lines, then EPUB and print formatting.
4. **Description, categories, keywords, pricing and the KU plan**, each
   as a small PR for the author to rule on.
5. **The author's own checklist** — the steps only he can do: the KDP
   account, tax and bank details, buying a cover, and checking the pen
   name by hand (trademark search, Amazon, Goodreads, BookBub, domains).

Every decision reaches the author as a small PR. **Nothing goes live on
Amazon without his explicit go.**
