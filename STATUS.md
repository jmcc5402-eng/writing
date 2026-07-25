# Project Status

_Living state — update this rather than appending new summaries. Last updated:
2026-07-25._

## Where things stand

| Workstream | Status |
|---|---|
| **Concept & 40-book arc** | ✅ Locked — `concept/premise.md` |
| **Series bible / story engine** | ✅ Locked — `series-bible/story-engine.md` |
| **Character canon** | ✅ Locked — `characters/characters.md` |
| **Book 1 — *The Petroglyph Mystery* (Maui)** | ✅ Complete: imported, copy-edited, 4 structural plot fixes applied |
| **Book 2 — Japan (Tokyo)** | 🧩 Starter outline only — `plots/book-02-japan.md` |
| **Go-to-market roadmap** | ✅ Drafted — `roadmap/go-to-market.md` |
| **Writers'-room agents** | ✅ Live in `.claude/agents/` (9 agents + outlining skill) |
| **Reusable `book-studio` repo** | ⛔ Blocked — see below |

## Book 1 detail

A complete 12-chapter manuscript at `manuscripts/book-01-hawaii/manuscript.md`.
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

- **`book-studio` repo:** the plan is to move the writers'-room agents into a
  standalone repo so they're reusable across the author's other books. This session
  could not reach that repo — GitHub access here is scoped to
  `jmcc5402-eng/fasting-timer` and `jmcc5402-eng/spytwins` only. **To finish it:
  start a session with `book-studio` attached as a source**, then copy
  `.claude/agents/`, `.claude/skills/`, and the manifests in `.claude/studio/` into
  the plugin layout described in `.claude/studio/USAGE.md`.
- **Branch:** work is on `claude/spytwins-repo-v2z2j1`, not yet merged to `main`.
- **Original source material** lives in the author's Google Drive folder
  `aSpyTwins`; `archive/README.md` catalogs it and the project's name history.
