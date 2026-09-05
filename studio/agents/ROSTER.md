# Agent Roster

The writers' room, tracked like software. **Definitions are the source code**
and live in `.claude/agents/` — this directory is the project around them:
versions, changes, backlog, and the prompt library.

Rules of the project:

- **The definition file is canonical.** This roster records versions and
  status; if it disagrees with the file, the file wins and the roster is stale.
- **Every agent change gets a CHANGELOG entry and a version bump.** Patch =
  wording/clarity, minor = new capability or rule, major = changed remit.
- **Changes are driven by evidence.** An agent gets edited because a run showed
  a failure or a gap — cite the run in the changelog entry. The BACKLOG holds
  known issues not yet fixed.
- **Commit prefix `agents:`** for anything touching `.claude/agents/`,
  `.claude/skills/`, or this directory.
- **Every run draws one variance card.** See `variance/DECKS.md` for the
  decks and rules, `variance/LOG.md` for the draw log, and
  `variance/RECENT.md` for each agent's current banned moves. Cards shift
  emphasis, never standards.

## Active agents (`.claude/agents/`)

| Agent | Ver | Model / effort | Remit (one line) |
|---|---|---|---|
| `plot-architect` | 1.4.0 | inherit / high | Premise → chapter-by-chapter outline (Snowflake + Hauge timing + location roster) |
| `drafting-assistant` | 1.5.0 | inherit | Approved outline → first-draft prose in the author's voice |
| `developmental-editor` | 1.4.0 | inherit / high | Story-level critique; non-fiction mode = the argument is the plot |
| `line-copy-editor` | 1.3.0 | inherit | Sentence-level; mechanical fixes applied, style proposed |
| `continuity-keeper` | 1.3.0 | inherit | Facts vs canon + scene staging; classifies contradiction / unestablished / deliberate |
| `kid-reader-panel` | 1.1.0 | inherit | Simulated 8–12 reader reactions |
| `red-team-critic` | 1.2.0 | inherit / high | Adversarial read before anything goes out |
| `romance-reader-panel` | 1.2.0 | inherit / high | Simulated 35–45 romance reader: engagement, skim, swoon, DNF |
| `superfan-reviewer` | 1.0.0 | inherit / high | The retail review section, predicted: star math, pet peeves, promise-keeping; the anti-professional-critic |
| `culture-researcher` | 1.1.0 | inherit | Setting/culture research + fact-check, web access |
| `market-pitch-agent` | 1.1.0 | inherit | Comps, queries, synopses, publishing strategy |
| `junior-literary-critic` | 1.1.0 | inherit / high | Two-part outside read: one-page critique + one-page prioritized recommendations |
| `gtm-strategist` | 1.0.0 | inherit / high | Go-to-market strategy and portfolio economics; materials stay with market-pitch-agent |
| `showrunner` | 2.2.1 | inherit / high | The ambitious publisher-author: nightly all-books shift, publisher's-eye + author's-eye per book, dispatches the instrument battery, momentum mandate; still never writes prose, decides canon, or merges |

Plus the skills `/new-book-outline` (`.claude/skills/new-book-outline/`)
and `/triage` 1.0.0 (`.claude/skills/triage/` — the author's PR queue
console; see `studio/PR-WORKFLOW.md`).

## Prompt library (`personas/`)

Parameterizations used to specialize generic agents for one book or one run.
Not standalone agents — they ride on top of one.

| Persona | Rides on | Proven on |
|---|---|---|
| `drafter-spytwins` | drafting-assistant | Book 1 ch1–4 rewrite, 2026-07-26 |
| `drafter-mybyb` | drafting-assistant | Part I ch1–4 draft, 2026-07-26 |
| `drafter-youngnick` | drafting-assistant | ch1–4 draft, 2026-07-26 |
| `drafter-campus` | drafting-assistant | new 2026-09-04 (the romance drafter; first use = 1.2 ch 8 re-cut) |
| `analyst-briefs` | (workflow analysts) | 9 analyst reports, 2026-07-26 |

## Deprecated / retired

| Agent | Fate |
|---|---|
| `continuity-checker` | Merged into `continuity-keeper` 1.1.0 (2026-07-26) |
| `line-editor` | Merged into `line-copy-editor` 1.1.0 (2026-07-26) |

## Provenance

The original nine were born in the standalone Spytwins repo
(commit `0487396`, 2026-07-25) and promoted to the workspace root on
2026-07-26 so all three books share them. The plugin packaging for
publishing the room outside this workspace is parked at `../plugin/`.
