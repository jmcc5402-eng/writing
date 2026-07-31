# The Series Kit

_The distilled system for creating a new book series, synthesized
2026-07-30 from an artifact-archaeology study of all three books —
what was actually used, what actually drove drafts, and what died on
the shelf. Every template here earned its place in production._

## The lineage — this is your own method, hardened

The study recovered the original artifacts (2013–2025) and traced each
one into the modern system. Nothing here is imported doctrine; it is
the author's spreadsheet method with better plumbing:

| Your original artifact (2013–2025) | Where it lives now | Kit template |
|---|---|---|
| SNOWFLAKE notes: "One Sentence → One Paragraph → Four Paragraphs → breakout into spreadsheet pages" | The snowflake outline, now with Hauge timing and per-chapter ledger lines | `06-snowflake-outline.md` |
| Scene/sequel grid (Goal/Obstacle/Disaster over Reaction/Dilemma/Decision — run per POV) | The beat spine + practice-sequel scenes; chapter briefs carry scene/sequel shape | `06-snowflake-outline.md` |
| "Must have features" list (Spytwins, 10 items) + Sheet 4 "To Do / must include throughout book" | The ingredient checklist — lenses not scenes, warnings not walls | `02-story-engine.md` |
| Sheet 5 "Themes" (eagles, knots, Northern Lights + craft directives) | SUPERCONCEPTS.md — 3–4 concepts with a chapter test each | `04-superconcepts.md` |
| Sheet 6 "Loose Ends" (`scope / Loose End / Resolution`) | THREADS.md — T##/S## IDs, OWED: markers, per-chapter ledger | `07-threads.md` |
| "PreSnowflake TEMPLATE" (problem → obstacles → clues → red herrings → point of no return → resolution) | The per-book locked premise (Q1–Q4 + banked ingredients) | `05-book-premise.md` |
| Hauge 6-stage chart PDF (in the Drive archive) | `studio/craft/hauge.md` + the outline's turning-point map | referenced, not duplicated |

## The kit, in creation order

Series-level artifacts (made once, before Book 1):

| # | Template | The artifact | Exists when |
|---|---|---|---|
| 1 | `01-premise.md` | Series premise + the canon-decision log | the logline survives being said out loud |
| 2 | `02-story-engine.md` | Ingredient checklist, beat spine, menus, rule tiers | the rewrite-forcing questions are locked |
| 3 | `03-characters.md` | Character sheets + the desires/fears engine | main cast named and locked |
| 4 | `04-superconcepts.md` | The 3–4 concepts that make it win, each with a test | you can say why a reader buys book 2 |

Per-book artifacts (each installment):

| # | Template | The artifact | Exists when |
|---|---|---|---|
| 5 | `05-book-premise.md` | Locked premise: Q1–Q4 + banked ingredients | the author locks the shape |
| 6 | `06-snowflake-outline.md` | Full chapter outline with audits | plot-architect expands the premise |
| 7 | `10-production-notes.md` | Draft handoff notes, reviews, adoption pass | drafting begins |

Living ledgers (updated on acceptance, forever):

| # | Template | The artifact | Updated when |
|---|---|---|---|
| 8 | `07-threads.md` | Thread map (per book) | a chapter is ACCEPTED, not drafted |
| 9 | `08-ledger.md` | Series ledger — honest per-book rows | a draft changes what's true on the page |
| 10 | `09-dream-review.md` | The review you're writing toward | after SUPERCONCEPTS; revisit per book |

Plus, from production: a **city/setting bank** for unused researched
nuggets (`books/spytwins/series-bible/city-bank.md` is the model), and
the studio machinery this kit assumes: `studio/PIPELINE.md` (stage
gates), `studio/craft/hauge.md` (structure overlay), the writers' room
(`.claude/agents/`), personas, and the variance system.

## Order of operations (spark → accepted chapter)

1. **Premise.** Write `01`. Gate: the logline survives out loud.
2. **Engine + cast + concepts.** Write `02`, `03`, `04`. Gate: the
   questions that would force a rewrite are locked. Decisions go into
   the `01` decision log — dated, marked LOCKED.
3. **Dream review** (`09`). Work backwards from the rave: what must
   exist on the page for a critic to write those ★ sentences?
4. **Per-book premise** (`05`). Brainstorm freely; the author locks
   the four-quarter shape and banks ingredients. Research pass
   (culture-researcher) before drafting; unused nuggets → the bank.
5. **Outline** (`06`). Expand via snowflake + Hauge; audit against the
   ingredient checklist; mark PROPOSED. **Author approves.**
6. **Draft.** Persona + variance card + banned moves + the relevant
   THREADS index entries in the brief. Output to `drafts/DATE/`, never
   into the manuscript. Handoff notes per `10`.
7. **Review.** Critic pass; then the ordered editorial three —
   developmental, then line, then continuity LAST (earlier passes
   invalidate it). Author rules on findings; rulings become dated
   canon decisions in `01`.
8. **Adoption.** One pass updates manuscript + CHANGELOG + THREADS +
   ledger together. Until then every draft is tagged unadopted.

## The rules that made it work

- **Canon wins; decisions get recorded, not remembered.** The dated,
  append-only `[Canon decision]` log was the single most load-bearing
  artifact in production. Non-fiction dropped it and paid in scattered
  `[TK]`s — the kit makes it universal.
- **Propose, don't apply.** Outlines and structural changes are
  PROPOSED until the author flips them. Mechanical fixes apply direct.
- **Ingredients are lenses, not scenes.** No checklist item may demand
  its own scene; if an outline needs a new scene to check a box, the
  box loses.
- **Warnings, not walls.** Canon facts, age band, fair play, earned
  wins, safety rails, and voice are walls. Every numeric/cadence rule
  is a warning, waivable per book with one recorded line:
  `WAIVED: <rule> — <reason> (author, <date>)`.
- **Honest cells.** The ledger records what a book earned ON THE PAGE,
  not what the bible aspires to. ("Gadget received: NONE" is a valid,
  valuable cell.)
- **Every setup pays off; every payoff was planted.** The fair-play
  clue table (plant → payoff) is mandatory in every outline.
- **Maps update on acceptance, not drafting.**

## Lessons from production (what NOT to rebuild)

- **The flat fill-in worksheet died.** Used once, left 10/12 fields
  TBD, superseded by the locked-premise form. Brainstorm in
  conversation; lock into Q1–Q4 + banked ingredients (`05`).
- **Status boards go stale.** A wrong "✅ Complete" cost more than no
  board. Keep live state in the pipeline's current-state table only,
  and let the ledgers (not a dashboard) be the truth.
- **Wire SUPERCONCEPTS into editorial briefs explicitly.** The file
  existed but only one agent's definition read it; rule 8 only works
  if reviewer briefs cite the file.
- **Menus audit; they don't generate.** Idea menus (plot types,
  atmospherics) were consulted as yardsticks, never as generators.
  Keep them short; expect premises to come from life (a market stall,
  an island you stood on).
- **Ledger authority beats ladder aspiration.** A skills ladder will
  claim things the page never earned; the ledger is the audit trail.

## Fiction ↔ non-fiction adaptation

Same skeleton, renamed slots (proven by MYBYB):

| Fiction | Non-fiction |
|---|---|
| Plot / premise | Thesis + reframe |
| Setup → payoff | Claim → callback |
| THREADS slots: INTRODUCES/CARRIES/PAYS OFF/HANDS FWD | CLAIMS/USES/CALLS BACK/PLANTS/HANDS FWD |
| Series myth threads (S##) | Brand/lexicon threads |
| Character sheets | LEXICON.md — named frameworks, reserved terms, first-use schedule (the one genuinely new artifact) |
| Dream review: literary outlet | Dream review: trade sheet (bookseller-facing) |
| Chapter test: craft | Chapter test: retail ("quotable out of context?") |
| Inner journey: character | Inner journey: the reader (identity → essence) |
