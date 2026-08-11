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
4. Reader simulation (rungs 3+): kid-reader-panel on the expansion —
   boredom, confusion, and guessed-the-ending checks before prose
   exists.
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
