# Work orders — a revision brief for a stretch of chapters

Three artifacts carry work between threads, and they are not
interchangeable:

| Artifact | Carries | Verified by |
|---|---|---|
| `HANDOFF.md` row | a finding, one line, addressed to a scope | printed at SessionStart; a BLOCK holds a gate |
| `proposals/PNNN` | **exact replacement text** for one place | `proposal-lint.py` — the NOW block must be in the file byte for byte |
| `orders/ONNN` | **a revision brief for a stretch** — numbers, a target, constraints, a verification | the commands it names |

A work order exists because the other two cannot say *"raise the body
count across seven chapters."* A proposal needs text you could have
typed; a board row is one line.

## The first rule — forward, unless it is mission-critical

The author, 2026-09-24: *"I generally wanna focus on future books more
than the existing or previous books. I think an anti-pattern is for us
to continually look backwards at stuff that's already written… I'd
rather focus our efforts on building the guard rail, so future work is
improved. So for any messages to the writers, please make sure they know
to go light on any changes in the past unless we really think they are
mission critical."*

**Every order leads with the forward fix**, and `order-lint.py` refuses
one that does not. A finding about written chapters becomes a floor for
the chapters that do not exist yet; it becomes a revision only when the
backward work passes a named test, and then it is small.

- a `## The forward fix` section is **required**
- a backward ask needs a `## Why backward` or mission-critical section
- a backward ask over **three chapters** is a warning: narrow it

The pull toward the past is structural, not careless — the pages exist
and the numbers are already computed, so it is the easiest thing to act
on. O001's first draft turned a real measurement into a revision pass
over seven finished chapters, written by the thread whose job is to
stop anti-patterns, on the day the author named it. That is why this is
a lint and not a paragraph of advice. (L079)

## The rule that makes an order useful

**An order carries numbers and a verification, never a scene.** The
environment thread measures and names what done looks like; the drafter
and the author decide what goes on the page. An order that says "add a
moment where she notices his hands" has crossed into the story thread's
work and should be a note to the author instead.

Every number in an order names the command that regenerates it. An
order whose figures cannot be re-derived is a memo, and memos drift.

## Sections

`Status`/`For`/`Board` · **Why this stretch** (the independent findings
that agree) · **The measurement** (per chapter, from the tools) ·
**What done looks like** (numbers, not adjectives) · **Constraints**
(what must not move, with the check that enforces each) · **What the
author must rule first** · **Verify**.
