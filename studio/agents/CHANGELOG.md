# Agent Changelog

Newest first. Every entry: version, what changed, and the evidence that
drove it.

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
