# The Drafting Protocol (programmatic drafting)

**PROPOSED 2026-08-04 — stages 1–2 of the ladder are author-decided
(the four-paragraph expansion and the whole-book continuity gate);
the rest becomes locked when the author blesses it.**

The premise: drafting errors are cheapest at the level where they're
introduced. So the book descends a ladder of representations, and
every rung gets checked BEFORE the next expansion — continuity is
verified on 6 pages before it can infect 90.

## The ladder (each rung gated before the next)

| Rung | Artifact | Gate |
|---|---|---|
| 1 | One sentence → one paragraph → four quarters | author approval (premise) |
| 2 | 2–3 sentences per chapter + fair-play table | author approval (outline PR) |
| 3 | **Four paragraphs per chapter** + world-state chain | **whole-book continuity review** |
| 4 | Per-chapter beat brief (fact manifest + thread I/O) | mechanical checks |
| 5 | First-draft prose, one chapter per run | review stack + linters |
| 6 | Accepted chapter | THREADS/ledger updated |

## The instruments

1. **World-state chain.** Every chapter carries `STATE IN` /
   `STATE OUT` lines — day + weekday, weather, time anchors, who
   knows what, where every plot object physically is. Chapter N's
   OUT must equal chapter N+1's IN; the chain is diffable and a
   reviewer checks the seams, not the vibes. (B1's timing audit did
   this retroactively; the protocol does it prospectively.)
2. **Fact manifests.** A chapter's drafting brief enumerates the ONLY
   facts the drafter may use — names, distances, prices, dates,
   object locations — pulled from canon docs. A fact not in the
   manifest may not appear in prose except as `[TK ...]`. Drafters
   flag, never invent.
3. **Blind drafting.** Prose runs get the brief, the voice sample,
   and the relevant thread-index entries — NOT the neighboring
   chapters. This kills tic-copying (the mechanism behind the
   colon/dash epidemic): a tic can't propagate through a manuscript
   the drafter never reads. Voice consistency comes from the fixed
   sample; transitions get stitched in a dedicated seam pass.
4. **The fair-play table is an executable spec.** Every clue row
   claims its plant chapter and its payoff chapter; after drafting,
   each claim is verified against the page by grep + read. A clue
   that moved chapters is a finding, not a footnote.
5. **Mechanical linters after every run** (anything greppable gets
   grepped, never proofread): locked-name check; dangling
   colon/dash sweep; banned-moves echo scan; timeline linter (every
   day/weekday/countdown word against the state chain); wink counter
   (S01 budget); reading-band spot check.
6. **Fixed review stack, fixed order.** Continuity → developmental →
   line, each producing NUMBERED findings; author rulings answer
   findings by number; revisions cite the ruling IDs. Traceability
   is what made the B1 revision auditable.
7. **Acceptance is a state change.** THREADS.md and the series
   ledger update only when a chapter is accepted — never on draft.

## Why "uncreative" is right

The creativity budget is spent at rungs 1–2 (premise, outline,
voice) and inside sentences at rung 5. Everything between is
logistics, and logistics is where continuity errors live. A
programmatic middle doesn't flatten the book — it protects the two
ends where the book actually lives.

## The rung contract (standardized 2026-08-04)

Why the ladder works at all: **the cost of a plot hole grows with the
word count it's embedded in.** A timeline hole costs a line at rung 1,
a paragraph at rung 3, a rewrite at rung 5. Every rung therefore runs
the same contract:

    expand → gate battery → author ratifies → FREEZE

A frozen rung is canon for every rung below it; a hole found later is
fixed at the rung that introduced it and re-derived downward
(backpropagation) — never patched downstream.

**Depth is bounded by decisions, not effort.** A new rung is justified
only if it forces decisions the rung above didn't (who knows what,
where objects sit, what day it rains). Past that point, recursion adds
words that feel like rigor. Six rungs is the working ceiling.

**Width is where AI compute goes.** A human plotter writes each rung
once and can't afford an editor per rung. We can. The per-rung gate
battery, from cheapest to richest:

1. Mechanical linters (always): state-chain diff, names, timeline
   words, dangling punctuation, wink counter.
2. Continuity gate (always): full canon review, numbered findings.
   Proven: B2 rung 3 caught a cross-book season contradiction (K1)
   and a shutters-physics hole (K6) on six pages. Severity tiers:
   in-book timeline/state findings BLOCK; cross-book calendar and
   season findings are WARNING-tier only — the series floats
   (author, 2026-08-05: "not necessarily perfectly chronological") —
   flag, propose a cheap patch, never block drafting.
3. Round-trip re-derivation (rungs 3+): a fresh agent that has never
   seen rung N-1 reverse-engineers it from rung N; the diff against
   the real rung N-1 is drift the forward reader can't see.
4. Reader simulation: the panel matching the book's audience —
   kid-reader-panel (young readers) or romance-reader-panel (books
   whose contract is an emotional experience). Boredom, confusion
   and guessed-the-ending checks before prose exists.
   **Rungs 3+ generally; rung 2+ for romance**, because a romance
   outline can already be measured for wanting, and the campus 1.1
   failure was visible at rung 2. A book with no matching panel does
   not skip this gate — it is missing one, which is a finding.
5. Adversarial pass (before author ratify): red-team the fair play
   and the stakes at the current rung.
6. Variant tournament (highest-value chapters only): N expansions
   from different angles, judge panel scores against SUPERCONCEPTS,
   winner takes the rung with the runners-up's best beats grafted in.

**Simulate, don't prosify.** Anything that is really data — timelines,
weather, object locations, who-knows-what — lives as a table checked
like a program (B2's rain calendar), and prose refers to it rather
than restating it.

## The conveyor — blind-competition drafting (author, 2026-08-11)

The scarce resource is the author's reading-and-ruling bandwidth;
agent drafting is not. A human studio serializes drafting because
drafters are expensive; this studio serializes THE AUTHOR'S READING
and parallelizes everything else.

1. **Rung-5 prose is a blind competition by default.** Every chapter
   is drafted N times (default N=3) by independent runs: distinct
   variance cards, same brief, same voice sample — and each drafter
   blind to the other candidates, to neighboring chapters, and to
   the mined source (instrument 3, now applied N-wide). Parallel
   independence is not just faster, it is cleaner: tics cannot copy
   between drafts that never read each other.
2. **The author reads winners, not drafts.** Candidates go through
   instrument judging (scored against SUPERCONCEPTS, the brief's
   obligations, and the register test — the climax-variant
   scoreboard is the model) plus the editorial battery. The author
   receives ONE winner (with the runners-up's best beats flagged
   for grafting) and rules: accept, amend, or reject. Author time
   per chapter: one read, one ruling.
3. **The register pilot.** The first chapter in any new POV or
   register runs the competition FIRST and alone — the author's
   ruling on its winner (what stayed, what got struck) becomes the
   register calibration document every later brief in that register
   cites. No batch-drafting in an unvalidated voice.
4. **Plans run ahead; prose never outruns the last ruling.** Briefs
   batch ahead freely (they are cheap and age well) and are
   alignment-checked against canon and each other before any prose.
   Prose holds a WIP limit of ONE: no chapter is drafted while more
   than one earlier chapter awaits the author's ruling. A ruling
   that shifts the voice therefore invalidates briefs at worst,
   never finished prose.
   **Batch mode (author, 2026-08-16):** once a register pilot's
   winner has been RULED, prose may batch three chapters per wave.
   Anti-tic containment, stacked: each competition's drafters stay
   blind within AND across chapters (a tic cannot copy through
   pages nobody reads); voice comes only from the fixed calibration
   chapter (accepted prose cannot drift); per-chapter linters and
   banned-moves apply per run; and one added check — a
   **cross-batch repetition scan** (the wave's winners plus all
   accepted chapters, grepped together for repeated sentence
   templates, opening shapes, and crutch words) runs BEFORE the
   author reads. Transitions are stitched in the seam pass after
   ruling. The author reads a wave's winners in one sitting; a
   register-shifting ruling invalidates at most one wave.
   **Dialogue floor (author flag, 2026-08-18):** the shelf runs
   30–40% dialogue; this voice is narration-forward on purpose, so
   the working targets are a book average near 25%, a per-chapter
   floor of 15%, at most one deliberate quiet chapter (~8–10%) per
   quarter, and never two sub-floor chapters in a row. Briefs state
   the target; the linter counts quoted words and reports the
   percentage with every candidate.
   **Notice budget (amended per the author's 2026-08-20 note —
   "we're not humanizing these characters enough — there's not the
   little characteristics of them that people really remember"):**
   at least 2 physical-notice beats per chapter, **of which at most
   one may be hands/competence — the other must be face, mouth,
   hair, or body-in-clothes; cap 4 per chapter.** A budget satisfied
   entirely with hands passes the count and fails the gate: the
   campus ch 5–8 audit found four chapters of forearms and thumbs
   with no face on the page, because every gate was satisfiable
   with hands. Composition, not count, is what the gate checks.
5. **Losers are kept, not deleted.** Runner-up candidates stay in
   `drafts/DATE/` unadopted — they are the graft bank for the
   winner's revision and the evidence base for register rulings.

## Snowflake prose is written for a stranger (author, 2026-08-08)

Rung 1–3 artifacts are the first place a book must sell itself —
including to the Director. The one-sentence and one-paragraph must
work as JACKET COPY: a reader who has never heard of the book should
be hooked by them. Each quarter (and each chapter entry at rung 3)
reads as a compelling miniature story with momentum and stakes —
never a beat inventory, never insider shorthand that assumes the
reader already knows the plot. Technical apparatus (PLANTS/PAYS,
ledger lines, clocks, density declarations, state chains) stays in
its labeled blocks BELOW the prose. Evidence: the author on the Nick
Books 2–4 sketch — "you're writing as if I already know the plot...
it should almost read like the back cover."

## Instrument governance — the over-tooling guard (author, 2026-08-14)

Prompted by the author's test: "if we have a million different
factors, we don't really have any." Three rules govern every
instrument in this studio — meters, gates, panels, scoreboards,
chapter-line requirements — across all books:

1. **Tool freeze until prose proves the tools.** The campus Book 1
   instrument set is declared COMPLETE as of this ruling: the walls,
   the four promises, the five meters (#62), the romance-reader
   panel, and fair play. No new instrument may be added until
   Book 1 has three drafted chapters — instruments must prove
   themselves on prose before anyone builds another.
2. **One in, one out.** After the freeze, adding an instrument
   requires either retiring one or citing a real failure the
   existing set demonstrably missed. Consolidation applied now:
   the per-chapter MEM:/SPINE: lines RETIRE in favor of the meters
   when METERS.md is ratified — one measurement system, not two.
   (SPINE's tether test survives inside standard 24's language;
   the meters measure what MEM asserted.)
3. **Instruments decay like banned moves.** An instrument that goes
   three books without a unique finding — a finding no other
   instrument produced — is retired from the battery. Tools keep
   earning their place exactly like chapters do.

**WAIVER — the CLOSENESS meter (author, 2026-08-23, in chat: "I
want to add this. We'll make a waiver to the tool count").** The
freeze and the one-in-one-out rule are waived ONCE, for a sixth
campus meter measuring reaction density (campus `METERS.md` §6;
the craft law is `studio/STYLE.md`, "Closeness"). Why it cleared a
bar the freeze exists to defend: it was not proposed in the
abstract but produced by a measurement of drafted prose (ch 1–20
at ~1.3 tagged interior moments per thousand words, three chapters
at zero), and it names a failure the existing five demonstrably
missed — ROMANCE, FUN, HEART, TENSION and TOWN can all score high
on a chapter the reader watches from across the street, which is
exactly what rule 2 of this section asks for before an instrument
is added. **Nothing is retired against it; the one-in-one-out rule
resumes immediately after.** The waiver covers this instrument
only and is not precedent — the next addition pays the old price.

The underlying law: a studio's output is books, and every factor is
worth only what it changes in a book. Nobody in the system holds
the full tool list — dreamers see briefs that open from wanting;
each instrument checks one thing, backstage; the author sees a
chart, a winner, and options. If any single mind ever needs the
whole inventory to do its job, that is the failure this section
exists to prevent.

## Book-2+ operating amendments (ratified 2026-08-29)

The Book-1 retrospective's ratified practice list —
`studio/RETRO-BOOK1.md` §II as amended by §III — governs all
1.2+ production: the pre-flight brief audit, the label-shuffle
judging protocol, the jewel-forge slot, the staging clause, the
furniture registry, the series dial, the storefront test, and
the retirement of the standalone staging lint (checks
reassigned, named owners). Where that list and older text here
conflict, the ratified list wins.

## The reversal slot and the say-it test (author law, 2026-09-03)

Every chapter brief opens with THE ROMANCE MOVE and carries the
lines below, each one the drafter must be able to read back as a
sentence:
- **THE ROMANCE MOVE (first line of every brief — Romance first,
  studio/STYLE.md):** what this chapter does to the feeling between
  the leads — closer, farther, or a new thing known — in one
  sentence. Plot comes after it.
- **ROMANCE BEATS:** at least three, of at least two kinds from the
  rule's list, planned as a numbered list with kinds and placement
  (first third / middle / last third). The COUPLE LINE lives here as
  kind 1 (the ladder rung). The panel's independent count is the one
  that stands; under three, the chapter is returned before staging.
- **REVERSAL:** who loses what in this chapter, on the page, and
  what it costs them. A chapter without a loser is not a chapter.
- **THE ARGUMENT, SAID:** the one complete sentence a stranger could
  repeat that states what the scene's people want from each other.
  See studio/STYLE.md, "The say-it test." Beats in briefs are
  written as sentences, never as noun-phrase clusters.
- **ARC BEAT:** what this character does in this chapter that the
  person they were in chapter one would not have done, and why.
  From the author-approved arc doc (studio/PIPELINE.md §3b). A
  chapter may have no arc beat only if the arc doc says so.
- **COUPLE LINE (now inside ROMANCE BEATS as kind 1):** which rung
  the chapter's proximity beat plays and whether the leads share a
  scene and speak. Two apart-chapters may not run in a row; an
  apart-chapter says why, and still owes three beats.
- **END REGISTER carries a direction:** UP or DOWN, relative to where
  the chapter opened. No two consecutive chapters end at the same
  level. (Author, 2026-09-03: "more ups and downs.")
- **THE STAKES, RESTATED:** from the chapter where the book's goal is
  first said whole (campus 1.2: ch 8), every brief restates that
  sentence and adds what THIS chapter puts at risk.
- **NAMING, FULL LIST:** any naming rule in the brief lists every
  speaker class and a default for the rest; the chapter lint reports
  each use with its speaker.
- **THE OPENING, SAID:** the chapter's first paragraph, as a plain
  sentence a stranger could repeat — what today is and what is at
  stake in it (STYLE.md, the explicit opening). The panel reads the
  first paragraph alone and says what the chapter is about.
- **TASTE:** the two or three entries of `studio/AUTHOR-TASTE.md`
  this chapter most risks, by number, and the check that catches
  each. Panels and editors answer it as their last finding.
