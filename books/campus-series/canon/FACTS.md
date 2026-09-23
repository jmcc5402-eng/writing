# Campus series — the fact manifest

Canon as **greppable assertions**. Every row is a fact the prose must
not contradict, plus the pattern that would mean it has.

`studio/tools/fact-check.py` reads this file and greps the manuscript.
It runs in under a second, it never gets tired, and it does not need an
agent to remember it exists.

## Why this file exists

On 2026-09-15 a continuity sweep found five blocking contradictions in
~86 added sentences. **Three of the five were flat fact errors** — a
character's tan line moved, a standing claim about his habits that the
book already disproved, and a clock that did not subtract. All three
had been true and checkable on the page for weeks.

The continuity-keeper is a better instrument than a grep and always
will be: it reads for meaning, and rows 3 and 4 of the sweep (a gaze
relocated mid-scene, an action order reversed) are beyond any regex.
**But the keeper runs when someone remembers to run it. The grep runs
every time.** This file is for the errors that do not need judgment.

## How to add a row

The day the author or an instrument catches a fact error, add a row.
That is the ratchet: the environment tightens, and it never loosens on
its own. A row costs sixty seconds and pays every run forever.

- **Fact** — stated positively, the way canon has it.
- **Established** — where the page says so. An author-ratified chapter
  beats everything else.
- **Scope** — `series`, `1.1`, `1.2`, or a chapter range. Facts change
  over a book; a row that is only true after ch 11 says so.
- **Contradicted by** — a Python regex, case-insensitive, that matches
  text asserting the opposite. Keep it narrow: a false positive that
  fires every run gets ignored, and an ignored check is an instruction
  again.

---

## Physical canon

| ID | Subject | Fact | Established | Scope | Contradicted by (regex) |
|---|---|---|---|---|---|
| F-CAL-01 | Cal Sutter | Tanned brown **to the elbow**; the pale begins at the elbow and a polo sleeve sits above it | 1.1 ch01:134 (author-ratified) | series | `sleeve[^.]{0,40}(rode\|ridden) up past where the brown` |
| F-RAT-01 | Ratchet | Female. She/her, always | 1.1 ch01; conformed ch04 | series | `\bRatchet\b[^,.]{0,15}\b(he\|his)\b` |
| F-RAT-02 | Ratchet | The tail is a **graded code**: delivery van one thump, crew trucks two. Cal gets two | 1.1 ch02:53 | series | `Ratchet's tail went once` |

## Character law

| ID | Subject | Fact | Established | Scope | Contradicted by (regex) |
|---|---|---|---|---|---|
| F-CAL-02 | Cal Sutter | **Talks aloud when alone** — to the dog, to the boiler, to a wrench. It is his habit, not anyone else's | 1.1 ch02:249, ch04:333, ch14:50 | series | `(did not lie\|didn't lie)[^.]{0,40}before noon\|which was her habit and not his` |
| F-CAL-03 | Cal Sutter | Gives himself cover stories before noon; the filing reflex is his signature move | 1.1 ch04:44 | series | *(see F-CAL-02 — the same row catches the contradiction)* |

## Schedule and clock

| ID | Subject | Fact | Established | Scope | Contradicted by (regex) |
|---|---|---|---|---|---|
| F-CHK-01 | The medical check | **Four fifteen**, Friday, thirty minutes — the September–November slot | 1.2 ch02:153 | 1.2 ch01–ch07 | — |
| F-CHK-02 | The medical check | **Five fifteen**, and from ch 11 it is **daily**, not weekly | 1.2 ch07:317, ch11:31 | 1.2 ch08–end | `five fifteen[^.]{0,40}(once a week\|weekly)\|thirty minutes a week` |
| F-CHK-03 | The refusal | Aisha **herself** sent the no, the same afternoon, in September | 1.2 ch02:155–158 | 1.2 | `the trainers (refused\|said no\|turned him down)` |

## Clock anchors — checked arithmetically, not by regex

Declare the scene's fixed times; the checker extracts every duration
claim in the chapter and falsifies the ones that do not subtract.

| Chapter | Anchor | Time | Line |
|---|---|---|---|
| 1.2 ch04 | Dan enters the lounge | 23:10 | 76 |
| 1.2 ch04 | Staff meeting | 07:00 | 293 |
| 1.2 ch03 | Boy seated in the tent | 18:10 | 159 |
| 1.2 ch03 | Headache reported | 18:15 | 177 |
| 1.2 ch03 | Worse | 18:22 | 178 |

## Open — needs the author, not a rule

| ID | Question | Why it is not a row yet |
|---|---|---|
| Q-MAR-01 | Does Marisol run parents' weekend? | 1.1 ch02:198 assumes Cal can guess she has started the list. Canon connects her to the parents' **group** and the welcome tent, never the weekend. Compatible with everything; supported by nothing. |
| Q-CAL-04 | The ch 4 / ch 5 interval — "two weeks" vs "two Saturdays back" | Pre-existing wobble; the available Mondays are day 9 or day 16, and day 16 puts ch 4 after ch 5. Settle before EPUB. |
| Q-CART-01 | One bad wheel or two? | 1.2 ch19 puts a bad wheel on the annex cart; ch13 has a flat-spot wheel in the Fieldhouse. |

## The regression result (2026-09-15, against main)

Built and tuned against live bugs, not synthetic ones: PR #171's fixes
were unmerged, so every contradiction the continuity sweep found was
still on `main` when this checker first ran.

```
$ python3 studio/tools/fact-check.py books/campus-series
fact-check: 6 CONTRADICTION(S)
  ✗ F-CAL-01  manuscript/ch03.md:196          ← sweep B5 (the tan line)
  ✗ F-CAL-02  manuscript/ch02.md:121          ← sweep B2 (lying before noon)
  ✗ F-CAL-02  manuscript/ch14.md:366          ← sweep Q8 ("her habit not his")
  ✗ F-RAT-02  manuscript/ch14.md:368          ← sweep Q8 (one tail thump)
  ✗ F-CHK-02  book2/manuscript/ch09.md:533    ← sweep W3 (thirty minutes a week)
  ✗ CLOCK     book2/manuscript/ch04.md        ← sweep B1 (nine hours vs 7h50m)
```

**Six real findings, zero false positives, under one second.** The
continuity sweep that found the same six took sixteen minutes of agent
time and had to be remembered.

Three rounds of tuning were needed to get there, and that is the honest
part of the story. `F-RAT-01` first matched *"Ratchet saw **him** to the
gate"* (that is Cal), then matched every *"his head"* in the book. A
row that fires on innocent prose is worse than no row: it trains
everyone to skim the output, and a skimmed check is an instruction
again. **Narrow the pattern until it is silent on clean text, or retire
the row.**

## What this file deliberately does NOT try to catch

Staging inside a scene — where a character's eyes are, what order two
actions happened in. Two of the sweep's five blockers were of that kind
and **no regex will ever find them.** They belong to the
continuity-keeper, gated by `accept-gate.sh`.

Knowing which errors are mechanical and which need a reader is the
whole skill. Claiming a checker covers the second kind is how a repo
gets a false sense of safety.
| F-TRN-01 | The trainer's debt | **Ten thousand dollars**, a gambling habit; the amount never drifts (B2-D27.1, LOCKED 2026-09-20; canon/STAKES.md) | B2-D27 | 1.2 | `\b(five|six|seven|eight|nine|twelve|fifteen|twenty|thirty|forty|fifty) (thousand|grand)\b[^.]{0,40}\b(bookie|owed|owes|debt|gambl|bet)` |
| F-MIS-02 | Missy Gault is Ashford-born | Grew up in the town; went to school with half the rail; "they know my car" (the author, B2-D29.2: "the town where she grew up"; ch 21). School unnamed — keep it so | B2-D29 | 1.2 | `Missy[^.]{0,60}\b(moved here|moved to Ashford|from (Birmingham|Atlanta|Mobile|out of state))\b` |
| F-MIS-01 | Missy Gault's drinking | A drinking problem, **never shown being done** — smelled, counted, missed, paid for (B2-D27.2, LOCKED 2026-09-20; canon/STAKES.md) | B2-D27 | 1.2 | `Missy[^.]{0,40}\b(drank|drinking|poured|sipped|swallowed|knocked back)\b[^.]{0,30}\b(wine|vodka|bourbon|beer|whiskey|a glass|a bottle|a drink)\b` |
| F-DAN-02 | Caught in season, both fired | A coach and the team physician in a relationship during the season are BOTH out the day it is proven — his second time ends him in college coaching; hers ends her here (B2-D30.1, LOCKED 2026-09-21; said blatantly on the page, ch 23 fold; from #185, 2026-09-23, said plain once per chapter, the same stake each time) (L064) | B2-D30 | 1.2 | `\b(sat (him|her) down|a warning|a reprimand|suspended for)\b[^.]{0,40}\b(if they were caught|if the county found out|caught together)\b` |
| F-DAN-01 | Dan's first time | Ten years ago, an assistant elsewhere, the woman on the academic side, the screenshot; **"the school sat me down a year"** — suspended, never fired; a SECOND time ends him in college coaching (B2-D28.2, LOCKED 2026-09-20; L046) | 1.2 ch14:222–243 | 1.2 | `\b(fired|let go|dismissed)\b[^.]{0,40}\b(ten years|the first time|back then|at the other program)\b` |
| F-AGD-01 | The February agenda | Holds THREE things: Boyd's pledge (the performance center on the annex's ground), Dan's extension ("a review" after the loss), and the provider partner's contract that takes over team physician services — her job (B2-D13, D15, D28.4; L049); no vote date on any page | 1.2 ch20:143; DECISIONS | 1.2 | `\b(spring|March|April) agenda\b` |
