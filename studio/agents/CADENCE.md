# Instrument cadence

**What each instrument owes, and how often.** Read by
`studio/tools/roster-staleness.py`, which compares this against the
actual draw log and reports what has gone quiet.

## Why this file exists

On 2026-09-14 the author asked, *"Are we still using the Super fan?"*
The answer was no — and had been no for **fifteen chapters**:

> *"For 1.2, the romance panel took over the pre-acceptance read chapter
> by chapter, and she quietly dropped out of the loop. **Nothing decided
> that; it just happened.**"*

Nothing decided it. No chapter's brief was wrong, no run failed, no gate
was skipped — an adjacent instrument grew into the same slot and the
older one fell out. **Every individual chapter looked correct.** The
deviation existed only across chapters, and nothing in the studio read
across chapters.

Two other drifts have the same shape and were caught the same way, by
the author noticing: three-drafter competition lapsed for four chapters
(*"it's a deviation, and I should have said so"*), and the card summary
format drifted for seven.

**A cadence that lives only in a pipeline doc is a cadence nothing can
miss.** This file makes "when did we last hear from X" a query.

## The cadences

`days` is the staleness threshold. It is deliberately generous — this
report is for catching an instrument that has *fallen out of the loop*,
not for nagging about a quiet week. An instrument marked `on-demand`
is never stale.

| Instrument | Cadence | days | What it owes |
|---|---|---|---|
| `drafting-assistant` | every chapter | 4 | the prose |
| `romance-reader-panel` | every chapter | 4 | the pre-acceptance read |
| `continuity-keeper` | every chapter | 4 | the blocking brief/card audit |
| `showrunner` | every working stint | 5 | the board and the next job |
| `superfan-reviewer` | **every 4 accepted chapters** | 12 | the retail read — promise-keeping, pet peeves, stars |
| `instrument-auditor` | every 4 accepted chapters | 12 | the audit of the instruments themselves |
| `developmental-editor` | every 4 accepted chapters | 12 | the rooting-for survey |
| `red-team-critic` | every wave or gate | 25 | the harshest fair read |
| `line-copy-editor` | every wave | 25 | the mechanical pass |
| `plot-architect` | on-demand | — | outlines and directives |
| `market-pitch-agent` | on-demand | — | comps, blurbs, names |
| `gtm-strategist` | on-demand | — | channel and revenue |
| `culture-researcher` | on-demand | — | setting and fact-checking |
| `junior-literary-critic` | on-demand | — | the outside read |
| `kid-reader-panel` | on-demand | — | not this series |

## Changing a cadence

Edit the row and say why in the commit. **That is the point:** an
instrument may absolutely be retired or slowed — what must not happen
is it going quiet with nobody deciding. A deliberate change is one line
of diff. Drift is invisible.
