# Agent Changelog

Newest first. Every entry: version, what changed, and the evidence that
drove it.

## 2026-07-28 — gtm-strategist 1.0.0 (new)

Author-requested: a business-focused agent for go-to-market analysis —
channel economics (KDP/Kindle, print, audio), trad-vs-self decisions,
author-platform strategy, sequencing. Boundary set at creation to avoid
remit overlap: market-pitch-agent makes the selling materials;
gtm-strategist decides the machine they're used in. Realism rules baked
in: labeled claim types (verified/estimate/author-data-needed), median
outcomes not survivor stories, kids-market gatekeeper reality (COPPA),
per-book strategies never averaged, every recommendation costed in
hours-per-week.

## 2026-07-28 — the Hauge frame (three agents, minor bumps)

Author-stated preference: Michael Hauge's framework (six stages, five
timed turning points, the identity→essence inner journey braided with
the outer goal, and the four devices — foreshadowing, echoing, superior
position, ticking clock). Distilled to `studio/craft/hauge.md`; agents
cite the file rather than carrying the framework.

- **plot-architect 1.1.0 → 1.2.0.** Outlines now name both journeys
  before beats exist and pin the turning points to their positions.
- **developmental-editor 1.2.0 → 1.3.0.** New audit: journey braid,
  turning-point depth, superior-position inventory, orphaned echoes.
- **drafting-assistant 1.1.0 → 1.2.0.** Scene-level rule: internal state
  rides in external action; superior-position beats and echoes are
  placed effects.

Evidence the frame fits: the studio was already running half of it
unnamed — S01 (the spy wink) is superior position as a series engine,
the knowledge-thread type in THREADS.md tracks it, the blessing-ceremony
day ledger is a ticking clock, and OWED markers are foreshadowing
discipline. Echoing and the timed inner/outer braid are the new imports.

## 2026-07-27 — the variance system (all agents, minor bump)

All ten agents gain a standing Variance section: a run may hand them one
card from `variance/DECKS.md` (emphasis only — never overrides canon, remit,
or output format) and a banned-moves list from `variance/RECENT.md`.
Versions: the seven 1.0.0 agents → 1.1.0; the three 1.1.0 agents → 1.2.0.

Evidence: repeated fixed-prompt runs converge — the 2026-07-26 reviews
caught a drafter simile scaffold used 24 times, four trailer-voice chapter
endings, and critique structures repeating across books. Design principle:
vary the lens, never the law. `RECENT.md` seeded with the caught tics;
selection is least-recently-used and logged, not random, so rotation is
enforced and card → quality effects stay observable.

## 2026-07-26 — junior-literary-critic 1.0.0 (new)

Promoted from an ad-hoc session prompt to a tracked agent after five
production runs (three initial book critiques, the Young Nicholas
manuscript re-read, and the post-rewrite reviews of all three books).
Distinctives worth preserving: verdict up front, every claim cites the
page, classifies findings, two-part output (critique + prioritized
recommendations), and it verifies its own quotations before returning.

## 2026-07-26 — the merge (workspace consolidation)

- **developmental-editor 1.0.0 → 1.1.0.** Merged the Spytwins version with
  the workspace variant: opens by naming the shape it found, scene-function
  and POV checks added, and an explicit non-fiction mode (thesis for plot,
  chapter spine for structure) because MYBYB is adult non-fiction and the
  original assumed middle grade.
- **continuity-keeper 1.0.0 → 1.1.0.** Absorbed `continuity-checker`
  (retired). Added the three-way finding classification (contradiction /
  unestablished / deliberate) and separate lists for new canon established
  and open `[TK]`/`[CHECK]` markers.
- **line-copy-editor 1.0.0 → 1.1.0.** Absorbed `line-editor` (retired).
  Added the line-pass checklist (filter words, rhythm, repetition,
  dialogue tags, throat-clearing) on top of the two-mode
  copy-edit/line-edit split.
- All other agents promoted unchanged at 1.0.0.

## 2026-07-25 — birth (Spytwins repo, commit 0487396)

Nine agents created as the Spytwins writers' room: plot-architect,
drafting-assistant, developmental-editor, line-copy-editor,
continuity-keeper, kid-reader-panel, red-team-critic, culture-researcher,
market-pitch-agent. Plus the /new-book-outline skill and the book-studio
plugin packaging.
