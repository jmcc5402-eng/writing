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
| 1.1 | `books/campus-series` | HELD | 30 | 2026-08-29 | — |
| 1.2 | `books/campus-series/book2` | DRAFTING | 30 | — | — |
| 1.3 | — | NOT STARTED | — | — | — |

Status is one of `NOT STARTED` · `OUTLINE` · `DRAFTING` · `HELD` (complete,
waiting for the next one) · `RELEASED`.

## Launch readiness — the author's, done during the buffer

- [ ] Pen name decided
- [ ] Series title decided
- [ ] KDP account opened, tax interview done
- [ ] Cover direction for Book 1.1
- [ ] Book 1.1 blurb

See `studio/gtm/kdp-launch-mechanics-2026-09-03.md` for each step. The
cycle tool reports how many are open once the held book's successor is
past two-thirds.
