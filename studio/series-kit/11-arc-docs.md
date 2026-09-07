# Template — The Arc Docs (the leads' arcs and the relationship's arc)

_Proven by: `books/campus-series/book2/plots/arc-docs.md` (the two
leads, 2026-09-03) and `books/campus-series/book2/plots/romance-arc.md`
(the romance itself, 2026-09-05). Both came from the same finding:
Book 1.2 had a great plot and flat people, then a great plot and an
abrupt romance, because the outline carried the arcs as craft
shorthand and no brief ever saw them. The author's laws:
"I have to approve each character's arc throughout the story before
we write" (2026-09-03) and "we need one for the romance overall to
show how early on the romance is hidden and just shows some signs of
life, but over the book it grows and turns external" (2026-09-05).
This template is the instrument that came out of it: "I want this to
be another instrument we use so eventually we can build these books
really fast."_

**When:** between the outline (`06`) and the first chapter brief.
**Gate:** the author approves all three docs as ONE PR before a
single brief is written (`studio/PIPELINE.md` §3b).
**Check:** `python3 studio/tools/romance-build-check.py <this file>`
reads the ladder table in Part 3 and fails the doc when the
relationship does not build.

The say-it test applies to every line: a sentence a stranger could
repeat. No "wound → identity → essence" shorthand; say what happened.

---

# <Book> — Arc docs (THE ARC GATE)

**PROPOSED — awaiting author approval (<agent+version>, YYYY-MM-DD,
variance card <ID>). Nothing below is canon until this PR merges.**

Sources: <the premise section, the outline's two-journeys paragraph,
the author's rulings by date>.

## Part 1 — <LEAD 1>, <age> — <the one-phrase identity>

**1. The wound.** <What happened before the book, in one sentence a
stranger could repeat.>

**2. The false belief, and what it makes them do.** <The wrong lesson
they took from the wound, then the behavior the reader WATCHES every
chapter: the objects, the habits, the thing they never do.>

**3. Want vs. need.** <What they want. What they need. Why getting
the want without the need would not fix them, and which chapter
proves it.>

**4. The turns.**
| Ch | What they do | What it shows |
|---|---|---|
| <n> | <an ACTION the reader can see, not a realization> | <what it says about the false belief: at full strength / tested / failing / first act against it / changed> |

At least one turn per quarter.

**5. The moment of change, and its cost.** <The scene where they do
the thing the false belief exists to prevent, and what it costs them,
on their face, before the reader sees it pay.>

**6. What <Lead 2> gives them.** <The other lead is the instrument
of the change, or the romance is decoration.>

## Part 1, again — <LEAD 2>

<Same six headings.>

## Part 2 — The two arcs, together

<Where the two moments of change sit, and why they must fall in the
same chapter or in the order they do. What each lead's change asks
of the other.>

## Part 4 — The antagonist's arc (where the book has one)

_Proven by `books/campus-series/book2/plots/boyd-arc.md`._ Who they
are in one sentence. What they want. What they believe and what it
makes them do. What they are NOT (the walls: never a cartoon; how
much is proven). The escalation table — chapter, what they do on
the page, what it shows. What they give the leads (the price). The
reader's superior position. The register, binding on every brief
that stages them. Open questions.

## Part 3 — The relationship's own arc

_For a romance this is the romance. For any other book it is the
central pair (the twins; the boy and the girl who is not yet his).
The relationship has two journeys, like a character does._

- **The inside journey** — what each of them feels about the other,
  stage by stage. <From ___ to ___ to ___.>
- **The outside journey** — what the two of them DO together and
  what the town can SEE, stage by stage. <From ___ to ___ to ___.>

**The stages and their chapters**
| Stage | Chapters | Inside (each of them) | Outside (the two of them; the town) | The reader can point to |
|---|---|---|---|---|
| 1. Hidden | | Neither admits anything. | They argue about work and the argument is the flirt — shown, not told. | |
| 2. Admitted inside | | Each names it to themselves and files it as impossible. | They stand too close and do not step back. | |
| 3. Shown between them | | Said out loud to a third party. | Help accepted; the first kiss. The town sees nothing yet. | |
| 4. Seen | | Hope, and the tax on it. | Couple beats, rationed. The town half-sees. | |
| 5. Public | | Each would rather be the one who pays. | The public claim; the town names them. | |

**The build check (the rule).** The inside may run ahead of the
outside by ONE stage, never more. A want may not be named inside
until the reader has watched the two of them enjoy each other on the
page at least twice. A kiss waits for help accepted. A public claim
waits for a private repair. The reader must always be able to point
to the scene where the next step started.

**The ladder, chapter by chapter.** This is the table the check
reads. Keep the seven columns in this order. **In** and **Out** are
stage numbers 1–5. **Rung on the page** is what the two of them DO
this chapter, or —. **Spends** is blank or one of `want`, `kiss`,
`claim`. **Earned by** lists the earlier chapters whose rung earns
it. **Hole** is anything the page does not yet have; write it as a
`[CHECK: …]` or `[TK …]` so it stays greppable.

| Ch | In | Out | Rung on the page | Spends | Earned by | Hole |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | <what they do> | — | — | — |
| 2 | 1 | 1 | | — | — | — |
| … | | | | | | |

**What this changes in the chapters that exist.** <For a book already
in drafting: which accepted chapters get an add, and exactly what.
Nothing else moves.>

---

## Downstream (how the docs reach the page)

- **Every brief** carries an ARC BEAT per lead from Part 1 ("In this
  chapter X does Y, which the old X would not have done, because Z")
  and opens with THE ROMANCE MOVE from Part 3, naming the stage and
  the rung it climbs (`studio/DRAFTING-PROTOCOL.md`).
- **The brief audit** runs the build check before a brief that
  spends a want, kiss, or claim; a FAIL blocks the brief.
- **The developmental editor** judges the arc beat and, on a spend
  chapter, names the earlier scenes that earn it; fewer than two is a
  finding, however good the chapter.
- **The ladder table is updated on acceptance,** like THREADS: the
  rung that reached the page, in the words the page used.
