# Agent Changelog

Newest first. Every entry: version, what changed, and the evidence that
drove it.

## 2026-08-05 — showrunner 2.0.0 → 2.1.0 (the MINOR merge lane)

Author ruling amends the agents-never-merge wall for one narrow
lane: PRs typed `[book][MINOR]` at creation may be merged by the
nightly shift after double verification (opener declares, merger
re-verifies), reported next morning under MERGED FOR YOU with a
"revert #N" handle; any doubt disqualifies; "hold minors" or a
same-day revert suspends the lane. Full rails in PR-WORKFLOW rule 7.
Evidence: the author — "for those small ones I only get a daily
summary so I can revert if needed but trusting most of them."

## 2026-08-05 — showrunner 1.0.0 → 2.0.0 (major: remit change)

Author-directed promotion: "act as if it's a young ambitious,
well-intentioned book publisher and author... scan over all the
books... I want to feel as if these agents are the ones driving the
momentum and my job is to give the vision and steer direction."
Changes: (1) scope widens from Spytwins to ALL books; (2) persona =
ambitious publisher-author with a momentum mandate — every book moves
one increment per shift or the report names the exact gate; (3) two
lenses per book (publisher's eye = path to market; author's eye =
weakest craft point + which instrument exposes it); (4) empowered to
dispatch the DRAFTING-PROTOCOL instrument battery, incl. tournaments
on OPEN decisions only; (5) reads studio/VISION.md (new — the
author's steering doc) first, every run; (6) morning nudge gains "at
most ONE steering question." Walls unchanged: never writes prose,
never decides canon, never merges; nightly budgets 3 jobs + 2 PRs,
saturation cap 5. The nightly Routine's prompt was updated to match.

## 2026-08-04 — drafting-assistant 1.2.0 → 1.3.0, line-copy-editor 1.2.0 → 1.3.0

New shared rule: **no paragraph ends in a colon or a dash**, plus a
mandatory mechanical sweep (`studio/STYLE.md`, "AI drafting tics") —
drafting-assistant runs it before delivering (rule 6); line-copy-editor
treats it as a COPY EDIT-mode mechanical check and reports
zero-or-explained. Evidence: on the B1 adoption read the author caught
six dangling colons and six dangling dashes across twelve chapters
("weird colons," "weird long dashes") that no editorial pass had
flagged — the dangling-reveal cadence is an AI tic that self-copies
through voice-matching, so prevention has to be mechanical, not
stylistic judgment.

## 2026-08-04 — plot-architect 1.2.0 → 1.3.0

Outlines now include a LOCATION ROSTER — every recurring setting
named, one-line identity, relative positions; <5 recurring (2–3
best), single-visit sites named but uncounted, no confusable names.
Evidence: the author, mid-adoption-read, confused the B1 cultural
center with the one-mention community center and with a "museum"
narration alias; the fix cost three edits post-draft that a roster
would have prevented at outline time.

## 2026-08-03 — continuity-keeper 1.2.0 → 1.3.0

New standing check: scene staging — where each scene is and whether
every movement inside it obeys the page (teleports, scene-interior
drift, who's-present drift, in-scene object staging). Evidence: the
author, listening to B1 ch3–4 audio, sensed an unmarked beach→
petroglyph-rocks jump and asked "do we have checks on setting,
specifically within a scene?" — the remit covered cross-chapter
geography but not scene-interior staging. First production run: the
2026-08-03 B1 staging sweep (card E3).

## 2026-07-30 — showrunner 1.0.0 (new)

Author-requested: a proactive lead-writer/program-manager agent that
surveys every book and recommends/kicks off the next job. Fills the
vacancy the 2026-07-30 artifact study documented: the acceptance/
kickoff step was the only pipeline stage with no owning agent, and
the stale STATUS.md proved stored status boards rot — so the
showrunner's first rule is compute-state-from-files, store nothing.
Remit boundaries: ranks and preps (briefs for dispatchable jobs,
typed PR specs for author gates per PR-WORKFLOW.md); never writes
prose, never decides canon, never merges. Variance-EXEMPT by design:
scheduling judgment must be stable run-to-run; a lens card would
churn priorities between mornings. Ties rotate deterministically
(release-train date, then alphabetical). Phase 2 slot: the nightly
Routine driver.

## 2026-07-30 — /triage skill 1.0.0 (new)

Author-requested, implementing `studio/PR-WORKFLOW.md` (the author-as-
engineering-director model): a session-side console for the PR queue.
Lists open PRs sorted by type priority (RULE/DECISION first; ADOPTION/
AUTHOR-INPUT labeled schedule-don't-squeeze), walks through any PR
conversationally, merges or posts rulings only on explicit per-PR
instruction. Guardrails: never merge own work, walls never waived in
triage, one book per PR. Companion to the GitHub mobile app, which
remains the recommended path for the 1-minute PR types.

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
