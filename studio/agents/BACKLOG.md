# Agent Backlog

Known issues and wanted improvements, with the production evidence that
surfaced them. Fixing one = edit the definition, bump the version, move the
item to CHANGELOG.

## drafting-assistant

*(All three items below are mitigated at run time by the banned-moves seed
in `variance/RECENT.md` as of 2026-07-27; the permanent definition fixes
are still pending.)*

- **Add an anti-sheen rule.** Evidence: the 2026-07-26 Young Nicholas run
  produced a "the way X does Y" simile template 24 times in 8,099 words, and
  smoothed two of the author's signature lines the critique had explicitly
  said to protect ("but it made no sense" → "and"; "daring him to fall" →
  "inviting him down"). Proposed rule: no recurring simile scaffold more than
  ~once per chapter; lines quoted in a critique as voice-defining are
  immutable and must be reused verbatim.
- **Ban trailer-voice chapter endings.** Evidence: all four MYBYB chapters
  ended by advertising the next chapter (critic: "cap every handoff at two
  lines"). Proposed rule: a chapter ends on its own strongest beat; handoffs
  get at most two lines.
- **[TK] placement discipline.** Evidence: Young Nicholas ch3 had a [TK]
  block at the peak of the predator pause, and "Nick [TK surname]" inside a
  spoken line, both killing the beat. Proposed rule: [TK] markers go between
  beats or in an end-of-file block, never mid-scene at an emotional peak.

## junior-literary-critic

- **Word budgets keep overrunning.** Evidence: every run exceeded the
  one-page target and self-reported it (920, 963/868 words). Either raise
  the stated budget to ~900 honestly, or add a hard cap with a "cut findings,
  say what was cut" rule. Decide, don't leave the tension in the prompt.

## line-copy-editor

- **Add a sheen-detection pass.** Same evidence as the drafting-assistant
  item: repeated simile scaffolds and replaced signature lines are exactly
  what a line pass should catch. Add "flag any recurring sentence template
  and any edit to a line the author's docs mark as voice-defining."

## continuity-keeper

- **Chapter-break integrity check.** Evidence: the Young Nicholas import had
  ~5 chapter breaks swallowed by the Google Docs export and chapters 5–24
  unnumbered; nothing in the current remit would catch a mis-ordered or
  merged chapter. Add a structural pass: chapter count, numbering, and
  scene-boundary sanity against the outline/bible.

## Roster-level

- **Decide the fate of `red-team-critic` vs `junior-literary-critic`.**
  Overlapping remits (adversarial pre-flight read vs two-part outside read).
  Either sharpen the boundary in both descriptions or merge them. Evidence:
  nothing has invoked red-team-critic yet; the junior critic has five runs.
- **Publish the plugin** (`../plugin/`) once versions stabilize, so other
  workspaces can install the room.
