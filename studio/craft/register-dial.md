# The register dial — how to actually change a book's vibe

The author, 2026-09-16:

> "I'm constantly trying to get the other thread to make it less small
> town and country, but it seems like they can't."

They couldn't, and this file is why. Measured with
`studio/tools/voice-dial.py`.

---

## What the measurement says

| | Modernity | Warmth | Country markers | Urban markers |
|---|---|---|---|---|
| **Book 1.1** | **1.5** / 10 | 5.2 | 6.95 / 1k | 0.33 / 1k |
| **Book 1.2** | **2.2** / 10 | 4.1 | 4.26 / 1k | 0.43 / 1k |
| *declared in DIALS.md* | *3 and 5* | *—* | | |

Two things are true at once.

**The note partly landed.** Book 1.2 halved the country density and
dropped a click of warmth — which is precisely how the author describes
the two books: *"book one was warm and country; book two less warm,
slightly more serious, still country."* The measurement and his ear
agree exactly, which is the first evidence that this axis is real and
not a made-up number.

**And it landed nowhere near the target.** `DIALS.md` declares Book 1.2
at Modernity 5. It measures **2.2**. The sheet has said 5 since
2026-08-30 and nothing ever checked it, so the gap was invisible to
everyone including the drafters.

---

## Why "less country" never works as an instruction

The country signal is not spread across a vocabulary. It is two words:

```
porch   223
county  212     = 54% of every country marker in both books
```

**Those are not style words. They are the setting.** The Checkerboard,
Delmar's screen porch, the square, the Liars' Table, the annex, the
fairgrounds — the *rooms the story happens in* are country rooms. A
drafter told "less country" deletes a `y'all`, keeps writing porch
scenes, and honestly believes it complied.

> **You cannot move this dial with a word list. You move it by changing
> the rooms, the institutions, and the jobs.**

That is also why five weeks of asking produced a half-click. The ask
was aimed at the prose; the cause is in the outline.

---

## How to actually spin it

In rough order of force. The first two do more than the rest combined.

**1. Change the rooms.** Every scene happens somewhere, and the
location roster is set at the outline, not the draft. A book whose
rooms are an apartment, a hospital cafeteria, a rideshare, a rooftop
and a co-working space reads contemporary no matter how the sentences
sound.

**2. Change the institutions.** The church, the county, the courthouse,
the feed store, the VFW, the radio station and the parents' board are
what make a place feel small. Swap in a hospital system, a university
department, a city council, a group chat, a management company — the
same social pressure with different furniture.

**3. Change the jobs.** Facilities director and team doctor are
place-bound. A book about people whose work could happen in any city
reads as any city.

**4. Change what people travel in and how far.** Trucks and a
twenty-minute drive are a register. Transit, flights, a commute, a
building lobby are another.

**5. Then, last, the vocabulary.** The word list is the finishing pass
and worth perhaps a click on its own. Doing it first is the mistake
this series made.

---

## The dials, and their tolerance

`DIALS.md` sets each book's targets; `voice-dial.py` measures three of
them. Tolerance is **±1.5 clicks** — tighter is false precision at this
sample size.

| Dial | Low pole | High pole | Measurable |
|---|---|---|---|
| **Modernity** | small-town country | contemporary / cosmopolitan | yes |
| **Warmth** | cool, formal, apart | warm, funny, together | yes |
| **Edge** | mild oaths | profanity | **not in this series** — under 25 markers per book is noise, and the tool says so rather than inventing a score |
| Audience centre, Humour register, Heat | | | declared only; panel's ear |

**The adjacency rule still applies:** no dial moves more than one click
between neighbouring books. It is what makes a quartet feel like a
quartet.

---

## The ruling this produced (author, 2026-09-16)

- **Books 1.3 and 1.4 hold roughly where 1.2 is.** Don't break a
  quartet mid-stride. Modernity target **3**, one click up from 1.2's
  measured 2.2, and reachable by swapping two or three rooms rather
  than rewriting a voice.
- **Set 2 is a deliberate, large move.** New town, new register, and
  the dial set **before the couples are cast** — per the 2026-09-11
  ruling that a book's register is assigned with its season, not
  discovered afterwards.
- **Set 2's Modernity target is a decision to make at its premise
  gate, not here.** What this file fixes is that the target will be a
  number somebody can check, and the first draft of chapter one can be
  measured against it the day it exists.

## The standing rule

**A dial nobody measures is a wish.** `DIALS.md` carried honest,
ratified numbers for six weeks while the prose sat three clicks away,
and no instrument in the studio could see it. From now the dial sheet
is checked like canon: `voice-dial.py` runs in `guardrails.sh`, and a
gap is either drift in the book or aspiration in the sheet. Both are
worth knowing. Neither is visible without a number.
