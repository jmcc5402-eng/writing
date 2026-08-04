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
