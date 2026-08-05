# Project Status

_Living state — update this rather than appending new summaries. Last updated:
2026-08-04._

## Where things stand

| Workstream | Status |
|---|---|
| **Concept & 40-book arc** | ✅ Locked — `concept/premise.md` |
| **Series bible / story engine** | ✅ Locked — `series-bible/story-engine.md` |
| **Character canon** | ✅ Locked — `characters/characters.md` |
| **Book 1 — *The Petroglyph Mystery* (Maui)** | ✅ **ADOPTED** (v2 canon, PR #6 merged 2026-08-04) — author calls it 95% edited; final polish batched until Books 1–3 exist |
| **Book 2 — Japan (Tokyo)** | ✅ Rung 3 FROZEN (four-para expansion ratified, PR #11 + continuity gate PASS) — season PR + rung-4 briefs next; prose awaits the author's explicit "draft" |
| **Go-to-market roadmap** | ✅ Drafted — `roadmap/go-to-market.md` |
| **Writers'-room agents** | ✅ Live at the workspace root, `../../.claude/agents/` (9 agents + outlining skill) |
| **Reusable agents across books** | ✅ Done — see below |

## Book 1 detail

The v2 rewrite is CANON as of 2026-08-04 (adoption PR #6): twelve
chapters read and ruled on by the author line by line, with the
two-door climax, the day-21 clock, the culture-pass fixes, and the
post-adoption orthography sweep all in. **Program plan (author,
2026-08-04): Book 1 is done for now at ~95% edited; the remaining
polish happens in one batch once Books 1–3 are written; publishing
begins when four books exist (per `roadmap/go-to-market.md`).**
Open micro-decisions ride as PRs #8–#10 (Kalani job, Kekoa season,
tennis ball). Pre-publication: Native Hawaiian sensitivity reader.

Original import notes: a complete 12-chapter manuscript at `manuscripts/book-01-hawaii/manuscript.md`.
Work done: cleaned from the Google Docs export, chapter headings normalized,
continuity bug fixed (villain was called "Dr. Chen" in two places — now "Dr. Lee"
throughout; note "Coach Chen" is a *different*, intentional character), a full
copy-edit pass, and four author-approved plot fixes (single ticking clock, tightened
deadline logic, explained the villain's key card, and made the petroglyph map a
shared clue rather than a coincidence).

Remaining, optional: decide whether to state the twins' ages on the page.

## Next actions

1. **Outline Book 2 (Japan)** — pick the core mystery + the new skill, then run the
   Snowflake. Use the `plot-architect` agent or `/new-book-outline`.
2. **Build the pitch package** — one-page synopsis, query blurb, comps
   (`market-pitch-agent`).
3. **Decide the Stage 1 path** — traditional agent vs. self-publish vs. hybrid.
4. **Get beta readers** on Book 1 — the cheapest, highest-value market signal.

## Open questions

- Do the twins ever learn the parents' secret before Arc 4, or does the reader
  stay ahead of them?
- How large a role do Moonbeam (the cat) and the online-class kids play?
- Does the agency — and the parents' boss, "the woman they always mention" — get a
  name and a face, and when?
- State the twins' exact ages on-page, or keep it implied?

## Blockers / notes

- **Reusable agents — resolved.** The plan was a standalone `book-studio` repo so
  the writers' room could serve the author's other books. That turned out to be
  unnecessary: Spytwins now lives in the `writing` workspace alongside MYBYB and
  Young Nicholas, and the agents were promoted to the workspace root, where all
  three books already use them. No fifth repo. The plugin manifests are parked at
  `../../studio/plugin/` for the one remaining case — publishing the team for use
  outside this workspace.
- **Repo:** work is merged and this book now lives at `books/spytwins/` in the
  `writing` workspace. The standalone `Spytwins` repo is archived.
- **Original source material** lives in the author's Google Drive folder
  `aSpyTwins`; `archive/README.md` catalogs it and the project's name history.
