# Variance Decks

Small, planned variety so repeated runs don't converge on the same moves.
**Vary the lens, never the law.**

## Rules

1. **One card per run.** Draw the least-recently-used card for that agent
   (check `LOG.md`); never stack two — you couldn't tell which caused what.
2. **Log every draw** in `LOG.md`: date, agent, card, where the output went.
3. **Cards shift emphasis, never standards.** Canon, remits, output formats,
   and verdict thresholds are exempt. If a critic's verdict starts
   correlating with its card, the card is too strong — retire it.
4. **Pair the card with the agent's banned moves** from `RECENT.md`.
5. **Deck maintenance is an `agents:` change** like any other: add or retire
   cards through the changelog. Refresh a deck when its cards stop surprising.
7. **Cards may carry a scope tag** (`[romance]`, `[mg]`, `[nf]`). An
   untagged card is in scope for every run. The least-recently-used draw
   considers only cards in scope for the run's book, so a
   program-specific card never starves another book's rotation.
6. **Mechanical runs don't draw.** Verbatim imports, file moves, and other
   transcription work take no card — variance exists for judgment, and
   injecting it into transcription would be damage. Log the run with "—".

## Drafter deck — `drafting-assistant` (any persona)

| ID | Card |
|---|---|
| D1 | Sound-forward: let hearing carry the scene where sight usually would |
| D2 | Hands and objects: physical business carries the emotion |
| D3 | Short-declarative session: favor plain sentences; earn every long one |
| D4 | Give one minor character a moment of unexpected competence |
| D5 | Weather as texture, never as topic |
| D6 | Let one scene run a beat past comfortable before cutting |
| D7 | Open every scene mid-motion; no arrivals, no waking up |

## Critic deck — `junior-literary-critic`, `red-team-critic`, `kid-reader-panel`, `superfan-reviewer`

| ID | Card |
|---|---|
| C1 | Weight pacing above all this read |
| C2 | Read as a bookseller deciding shelf placement |
| C3 | Dialogue-only first pass, then the rest |
| C4 | Read as a first-timer who knows nothing of the canon docs |
| C5 | Judge every chapter by its last five lines |
| C6 | Comp-shelf read: hold each element against the named comps |
| C7 | `[romance]` Read only the chapter endings, in order |
| C8 | `[romance]` Read as a reader who skips to the good parts |
| C9 | `[romance]` Track one lead's wanting and nothing else |
| C10 | `[romance]` Suspend attention to plot; report only what it felt like |

## Editor deck — `developmental-editor`, `line-copy-editor`, `continuity-keeper`

| ID | Card |
|---|---|
| E1 | Hunt sentence-template repetition first |
| E2 | Start from the weakest chapter, not the first |
| E3 | Work in reverse order (continuity: sweep the timeline backwards) |
| E4 | Watch transitions: how scenes are entered and left |
| E5 | Dialogue mechanics pass first |
| E6 | Weight what's missing over what's wrong |

For `continuity-keeper` the card may only change sweep *order* and reporting
emphasis — a fact is a fact under every card.

## Architect & researcher deck — `plot-architect`, `culture-researcher`, `market-pitch-agent`

| ID | Card |
|---|---|
| A1 | Antagonist-first: structure from the villain's plan outward |
| A2 | Subplot audit: make the B-story earn its pages |
| A3 | Sensory inventory: what the place smells, sounds, and feels like |
| A4 | Contrarian comp: find the comp arguing this book shouldn't work |
| A5 | Midpoint-first: fix the middle before touching the ends |
| A6 | `[romance]` Room-first: build each act from the town rooms and events it happens in, and let the plot find them |
| A7 | `[romance]` Two in the room: spine the book using only scenes where both leads are present, then add what's missing |
| A8 | `[romance]` Set-piece-first: name the three big fun events before any plot beat |
| A9 | `[romance]` Appetite pass: what people eat, drink, wear, and want — one beat built around each |
| A10 | `[romance]` Blurb-backwards: write the cover copy first and outline the book that earns it |
