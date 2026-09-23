# The release cycle — one finished book in hand at every launch

**Read by `studio/tools/cycle.py`** (a line at every SessionStart; a gate
on every `[RELEASE]` PR).

The author, 2026-09-24:

> *"My plan was to ship 1.1 once 1.2 was done. I wanna get into this
> long-term pattern where I always have one book finished when we
> launched the previous book. For me, the biggest failure mode is
> getting out of this cycle, so I'm buffering upfront."*

## The rule

**Book N is released only when Book N+1 is complete.** At every launch
there is one finished, unreleased book behind it. Complete means every
planned chapter accepted, not "nearly done".

**And Book N itself must be shippable, which is not the same thing.**
The author, 2026-09-24: *"Honestly, I'm not convinced that 1.1 is done
either."* He was right. Complete is the story; shippable is the product.
A release also needs:

- **a clean export** — `export-book.py` assembles the text the reader
  gets and fails on anything from the workshop. Pasted into KDP as it
  stands, Book 1.1's raw manuscript would ship **95 lines** of
  production headers: POV lines, "ACCEPTED by…", drafter cards, paths.
- **front and back matter** — title page, copyright, and the series
  call to action that the launch study calls "where KU series money is
  actually made". None exists yet.
- **a pre-launch review** of the book being released, glaring errors
  only (`studio/threads/orders/O002`). Book 1.1 was edited after it was
  marked complete — a thirty-sentence heat pass on 2026-09-15 that the
  continuity sweep then found **five blocking errors** in — and nothing
  has read the whole book since.

`cycle.py --gate` checks all three.

## Why the cycle breaks, and what the tool watches

The failure is not a late launch. It is a launch that leaves the buffer
empty. After Book N ships, Book N+1 sits finished and waiting — and if
Book N+2 has not started, the next launch either breaks the rule or
waits indefinitely. The lead measure is therefore **the book after
next**: when N+1 is complete, N+2 should already be moving.

The second quiet break is **launch admin**. Pen name, series title, the
KDP account and the tax interview take calendar time, not writing time,
and they are the author's. They belong in the months the buffer book is
being written, so that the day it completes the release is days away,
not weeks. Listed below so they cannot be forgotten into the gap.

## The books in the cycle

| Book | Directory | Status | Planned chapters | Complete | Released |
|---|---|---|---|---|---|
| 1.1 | `books/campus-series` | HELD | 30 | 2026-08-29 (story); edited 2026-09-15; not yet shippable | — |
| 1.2 | `books/campus-series/book2` | DRAFTING | 30 | — | — |
| 1.3 | — | NOT STARTED | — | — | — |

Status is one of `NOT STARTED` · `OUTLINE` · `DRAFTING` · `HELD` (complete,
waiting for the next one) · `RELEASED`.

## Launch readiness — done during the buffer

**The author's** (calendar time, not writing time):

- [ ] Pen name decided
- [ ] Series title decided
- [ ] KDP account opened, tax interview done
- [ ] Cover direction for Book 1.1
- [ ] Book 1.1 blurb

**The studio's** (before the held book can release — the gate checks):

- [ ] Pre-launch review of 1.1, glaring errors only (O002)
- [ ] `studio/launch/campus-series/front-matter.md` for 1.1 — title page, copyright, disclaimer
- [ ] `studio/launch/campus-series/back-matter.md` for 1.1 — continue-the-series link to 1.2, newsletter, review request
- [ ] Clean export (`python3 studio/tools/export-book.py books/campus-series`)

See `studio/gtm/kdp-launch-mechanics-2026-09-03.md` for each step. The
cycle tool reports how many are open once the held book's successor is
past two-thirds.
