# Agent Backlog

Known issues and wanted improvements, with the production evidence that
surfaced them. Fixing one = edit the definition, bump the version, move the
item to CHANGELOG.

## The romance floor (studio/STYLE.md "Romance first")

- **A passing count is not a passing chapter.** Evidence: 1.2 ch 8
  (thirteen beats; the author: "have we earned the right… it almost
  seems to come out of nowhere") and 1.2 ch 9 (six beats, four kinds,
  both edge thirds; the author: "she doesn't think about Dan the
  entire chapter… nothing woven in to the various scenes"). The
  floor counts thirds and kinds; the author feels scenes and warmth.
  Mitigated 2026-09-06 by "Woven, not counted" (per scene) and panel
  1.3.0's apart test. Still wanted: a way to measure WARMTH (Book
  One's vibe) rather than presence — the panel's judgment is the
  only instrument for it today.

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

## From the first instrument audit (2026-09-07 — `audits/2026-09-07-instrument-audit.md`)

Fixed on the ch 12 PR (2026-09-07): F1, F2, F6. **Landed on the backlog
PR (2026-09-12; agents CHANGELOG, "THE BACKLOG PR"):** F3/F14, F4,
F5, F7, F8, F9, F10, F13, F15, F16. Still open:

- **F11 / F12 — ghosts and miscounts**: the registry's Source column
  needs `chNN:line` on its older rows (the new rows carry them); one
  ledger pass at the ch 20 fold.
- **F17 — second-time catches (2026-09-09, 1.2 ch 14, #153).** The
  panel's scene-by-scene now carries a FACE column and an ending row
  in practice (1.5.x); the auditor's next run checks that the 1.5.3
  duration numbers catch what 1.4.0 missed.

## From the second instrument audit (2026-09-10) — `studio/agents/audits/2026-09-10-instrument-audit.md`

**Landed on the backlog PR (2026-09-12):** F18, F19, F23, F24, F25,
F26, F27, F28 (all but the two not found), F29, F30, F31, F32, F33.
Still open:

- **F21 — the panel as second drafter.** The remit lines landed
  (panel 1.5.2: a fix names what a line must do; the keeper bans its
  own examples). Still wanted: the fold logs any panel or audit line
  kept verbatim on the page as a GRAFT.
- **F22 — a backstory that copies the plot** has no instrument; the
  developmental editor's Hauge "echoes" item is the home.
- **F28, two items not found on re-read:** AUTHOR-TASTE "entry 8's
  duplicate block"; "the undated agents CHANGELOG entry." Closed
  unless the auditor's third run points at a line.
- **F32, the series half:** the COUPLES section is in the 1.2
  registry; the kit's registry template (08-ledger or the retro's
  registry rule) should carry it for every series.
- **F31, the fold half:** landed as line (8) of PIPELINE's fold
  checklist.
- **F34 — the panel passed a poem (author catch, #161).** 1.5.3 read
  ch 18 with the new duration numbers and missed chained one-sentence
  paragraphs, banter nobody could decode, and a week apart with no
  reason. Landed: panel 1.5.4 (poem, mystery, joke, apart-why); the
  lint's SENTENCES count; drafter 1.6.0. Open for the third audit: why
  the duration numbers rewarded chained sentences (narration per
  dialogue line rises when sentences chain).
- **F35 — a chapter built on an object the plot had not made heavy
  (author catch, #161).** The card, the brief and the audit all made
  the letter the chapter's spine; nothing asked what the letter
  weighs to the reader at ch 18. Landed: STYLE (b); the panel's
  MYSTERY test. Open: the card template (kit 12) asks "what does the
  reader already know to fear about this" for any object the chapter
  leans on; the showrunner's card writing reads the outline's PAYOFF
  chapter before making a plant a spine.
- **F36 — the audited brief went to a stray file (2026-09-13).** The
  orchestrator's Python edit shadowed its path variable and wrote the
  corrected ch 18 v2 brief to `book2/x`; the plots copy lacked the
  addendum; candidates A and B drafted from it, C found the stray
  file and said so. Landed: drafter 1.6.1 rule 8 (no addendum, no
  draft). LANDED 2026-09-17: `studio/tools/brief-gate.py`, a
  PreToolUse hook on the Agent tool — a drafting-assistant named on a
  brief without an AUDIT ADDENDUM and a VERDICT on disk does not
  launch. Still open: the edit scripts assert the target path.
- **The third audit (after ch 20):** its test set is the author's
  catches since 2026-09-10 (AUTHOR-NOTES rows from #156 on): the
  seeds, the couple, the card drift, the ending's return, the
  weather row.

## From the superfan's six-random-chapter read (2026-09-15 — `books/campus-series/book2/notes/superfan-random-2026-09-15.md`)

- **F37 — the clock-and-stool opening (the superfan's three-star:
  "this author loves a clock… every scene starts by telling me what
  time it is and which stool, and I wanted her face instead").** Ch
  4, 15, 17, 18, 19 all open on a time of day or a counter position;
  the opening check caught the shared runs, not the habit. LANDED
  the same day: `opening-check.py` WARNs when the first paragraph
  carries a clock or a stool. Not a law until the author rules;
  briefs may still ask for the hour, second. Related: ch 15's first
  paragraph (the step count) and ch 6's "I'm not on Millrow, Coach"
  are MINOR-edit candidates for the author's call.
- **F38 — the superfan dropped out of the 1.2 loop.** No chapter
  read between the outline gate (2026-08-30) and this run; nothing
  decided it. PROPOSED: she reads every accepted block of four as a
  stretch, and every set piece before the author does — PIPELINE and
  ROSTER to carry it once the author picks the cadence (asked
  2026-09-14).
- **F39 — `roster-staleness.py` reads the showrunner as stale by
  design (2026-09-16).** It measures every instrument by the variance
  draw log, and showrunner survey runs are exempt from draws
  (showrunner 2.4.4). So the showrunner shows "last run 2026-08-29"
  after seventeen days of daily stints. Fix: either the showrunner
  logs a no-draw row per stint, or the tool reads STATE.md's pick-up
  date for it. One or the other; not both.
- **F40 — the card lint (2026-09-17, author: "1 and 2 now").**
  `studio/tools/card-lint.py`, a PreToolUse hook on SendUserFile:
  body under 350, sentences under 30, calls one sentence each, the
  sections present, no ledger words, no markers. Cards before ch 18
  fail it (older format, no calls) — it governs going forward, not
  backward.
- **F41 — targets before the chapter (author, 2026-09-17: "choose the
  rank of the romance before the chapter's written, giving us a
  definition of done").** LANDED the same day as environment, not a
  rule: the card's Targets line (card-lint refuses a card without it),
  the panel's ACTUALS line (1.5.6), `targets-check.py` in the accept
  gate from ch 21, the pair recorded in `notes/targets.md`. Open: the
  author's own number after reading goes in `notes/romance-levels.md`
  by hand from the PR comment — a script that reads the PR comments
  could do it.
- **F42 — the accept gate's "CHANGELOG entry for today" (2026-09-19).**
  The gate requires a CHANGELOG line dated TODAY, so a re-run on an
  accepted chapter on a quiet day BLOCKS on nothing (ch 20 on the
  19th). It should look for the chapter's own entry (`ch NN` in a
  heading), not today's date. One-line fix; not done here because a
  backfill was mid-run.
- **F43 — /chapter-score landed (author, 2026-09-19: "I'd like a skill
  that does that for each chapter").** The skill, `scorecard.py`, the
  score file required at the accept gate from ch 21, and the backfill
  of ch 1–20 (panel: romance levels; developmental editor: 0–3 per
  lead with evidence). The two readers are agents; the environment
  makes the file required, the roll-up mechanical, and the flags
  (a lead at 0 three chapters running; a level two or more under
  target) printed.
- **F44 — the matrix viewed before and after (author, 2026-09-19).**
  LANDED as environment: `matrix-strip.py` at session start (the
  chapter in progress); the brief gate refuses a drafter whose prompt
  lacks the row; the card lint refuses a card whose line differs; the
  PR lint refuses a [CHAPTER] PR without the row and a [FOLD] PR
  without plan → actual; the accept gate runs targets-check.
