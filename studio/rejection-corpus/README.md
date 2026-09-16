# The rejection corpus

Every line the author ever rejected, with the reason, in a form a
checker can use.

`studio/AUTHOR-NOTES.md` already holds 212 mined rows from PRs and chat.
This directory is the **wider haul**: session transcripts mined for
corrections that never reached the ledger, and turned into something
that runs rather than something an agent is asked to remember.

## Why

The studio has fifteen agents that produce prose and one author whose
taste decides whether it lives. That taste is the scarcest input in the
building and it has been spent, over and over, on the same classes of
mistake — too oblique, too terse, too composed, a wry button on the
twelfth chapter running.

A rejection is expensive. It costs the author a read, a comment and a
revision cycle. **Spending it once and writing it down is the whole
game**; spending it twice on the same class is the studio failing.

## The row format

| Field | Meaning |
|---|---|
| `id` | R-### , stable, never renumbered |
| `date` | when the author said it |
| `source` | session id, PR number, or file:line |
| `verbatim` | **the author's own words**, unparaphrased |
| `target` | the text he was reacting to, quoted if recoverable |
| `class` | the failure class (see below) |
| `already_a_rule` | the RECENT.md ban / STYLE law / STANDARD it became — or `NONE`, which is the interesting case |
| `mechanizable` | `grep` · `check` · `gate` · `reader-only` |

## The classes

Seeded from the eleven patterns the 2026-09-04 miner's read found in
AUTHOR-NOTES. Add classes as the data demands; do not force a row.

- `too-oblique` — say the actual thing *(the strongest through-line)*
- `too-terse` — slow down the good parts
- `too-composed` — every landing is a wry button; it reads written
- `not-fun` — warmth, swoon and fun outrank structure
- `not-romance-first` — the plot ate the chapter
- `leads-not-seen` — physically absent, or admired instead of felt
- `campy` — the energy is right, the furniture is dated
- `gold-plated` — too perfect to be true
- `mystery-habit` — a plot object carried as a puzzle
- `repetition` — a construction that has become a template
- `canon` — a fact error

## What gets built from it

1. **A regression check.** New prose scored against the corpus: *this
   sentence resembles R-141, rejected as "too oblique."* Not a grep —
   a cheap classifier pass over the drafter's diff, before the author
   ever sees it.
2. **Coverage.** Which rejection classes have a guardrail and which are
   still only instructions. The `already_a_rule = NONE` rows are the
   backlog, ranked by how often the author has had to repeat himself.
3. **Drafter telemetry.** Which agents and which variance cards produce
   rows. `DECKS.md` already requires this — *"if a critic's verdict
   starts correlating with its card, the card is too strong"* — and
   nothing has ever measured it.

## Mining discipline

- **Verbatim or nothing.** A paraphrased rejection is a second-hand
  opinion; the author's exact words are the asset. If the wording is
  lost, mark the row `[paraphrase]` and trust it less.
- **One rejection, one row.** A comment that makes three complaints is
  three rows.
- **Praise counts too**, in a separate file — knowing what he *kept* is
  half the signal, and the swoon inventory proves he is specific about it.
- **Commit after every source file.** A container restart already cost
  this session one completed study; unmined transcripts sitting in a
  context window are the same exposure.

## Raw material

`raw/` holds the source transcripts as uploaded, unedited, so any row
can be traced back and re-read. They are inputs, not canon.
