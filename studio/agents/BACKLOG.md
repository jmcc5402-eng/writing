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

## culture-researcher

- **No write access — deliverables come back as chat text.** Evidence:
  the 2026-07-30 Toronto Islands run was briefed to write its brief to
  `notes/` but its toolset (Read/Grep/Glob/WebSearch/WebFetch) has no
  Write; the orchestrator had to save the file for it. Either add Write
  to the definition (matching plot-architect and market-pitch-agent) or
  change the standing brief pattern to "return the document as your
  final message."

## Roster-level

- **Decide the fate of `red-team-critic` vs `junior-literary-critic`.**
  Overlapping remits (adversarial pre-flight read vs two-part outside read).
  Either sharpen the boundary in both descriptions or merge them. Evidence:
  nothing has invoked red-team-critic yet; the junior critic has five runs.
- **Publish the plugin** (`../plugin/`) once versions stabilize, so other
  workspaces can install the room.

## 2026-08-30 — Instrument-consolidation review (author asked; showrunner ruling: DEFER the big one, do three cheap items)

The Book-1 retro's escape analysis already audited gate VALUE
with data (it retired the staging lint, reassigned its checks
with named owners, and set instrument trust levels) — a fresh
judgment-based consolidation review now would violate our own
rule 7 (decisions from data, thresholds before instruments).
The FULL roster-consolidation review is scheduled for the
BOOK-2 RETRO, when we have a second book's data under the new
rules (label shuffle, brief audit, jewel forge). Until then,
three cheap items:
1. **DEBT — the "deck TK" backlog.** romance-reader-panel,
   superfan, dev-editor, market-pitch, and culture-researcher
   have logged "no card; deck TK" ~30 times. Either deal them
   decks (a P-deck for reception instruments) or rule formally
   that reception instruments run card-free — the LOG should
   stop apologizing either way. [author-gate PR candidate,
   small]
2. **CONSOLIDATION CANDIDATE — the sampling trio.** Browse,
   warmth map, and voice-dating ran as three separate specs;
   at Book-2's milestones they can run as ONE "book health
   panel" spec (one seeded sampler, three scores per window,
   one note) — same signal, one launch instead of three.
3. **NON-CANDIDATE, recorded so it isn't re-litigated:**
   romance-reader-panel vs superfan look adjacent but measured
   differently all book — panels SELECT (blind candidates, craft
   verdicts), superfan predicts RECEPTION (reviews, stars,
   promise-keeping). Their one collision (both read outlines)
   is a feature: the twin read just caught what neither alone
   would. Keep separate.

## 2026-08-30 — author listens on TTS audio (calibration note)

The author reports consuming chapters as AUDIO via the ElevenReader
app ("ch 1–3 on audio were really good" — first wave of 1.2, day of
staging). Implications, standing:
- Audio is a REAL author channel, not a persona hypothesis — the 1.2
  P-deck deal (developmental-editor = P3 audio ear) is validated;
  keep an audio-posture instrument in every book's deal.
- Line passes watch for audio-tells: clock strings ("6:10"),
  jersey-number renderings ("#7" vs "the seven" — the house's
  "the seven" reads aloud correctly), homographs, and dialogue
  attribution that only works by eye.
- Reading-page/manuscript markdown already TTS-friendly (semantic
  line breaks read as phrasing); keep it that way.

## 2026-09-04 — brief an agent that can write the file you asked for

Both instrument jobs on tonight's shift (youngnick decision sheet,
mybyb gap map) were briefed to `developmental-editor` with a named
output path. `developmental-editor` has Read, Grep and Glob and no
write tool (`.claude/agents/`, roster), so both agents did the full
job, produced the document in chat, and could not file it. Each
opened its reply by saying so. The orchestrator transcribed both by
hand — roughly 1,500 lines through the conversation for no reason.

Standing fix, for whoever dispatches:
- **Check the agent's tools before naming an output path.** The
  writing-capable analysts are `junior-literary-critic`,
  `plot-architect`, `market-pitch-agent` and `gtm-strategist`. The
  editorial three — developmental, line, continuity — are read-only
  by design and report to the orchestrator, who files.
- If a read-only agent is the right specialist (it usually is for
  judgment work), brief it to **return** the report, and say so, so
  the agent does not waste its opening paragraph apologizing for a
  tool it was never given.
- The mybyb run also flagged that it was dispatched with no variance
  card and declined to pick one for itself. Correct behavior. The
  dispatcher draws the card; MYBYB has never been dealt a P-deck
  card and that gap is real.
