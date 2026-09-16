# Signal registers — the small things that carry the feeling

A **signal register** is a recurring, ordinary detail whose *variation*
tells the reader how a character feels, so the page never has to say
it. The default is furniture. The change is the beat.

The author's own example, which named the device:

> "I like that beer is his primary drink, but we can use different
> types of alcohol to convey different feelings throughout these
> books." — 2026-09-13, on 1.2 ch 18
>
> "…and I'm planning for it at the darkest part of the book he drinks
> bourbon." — 2026-09-16

Dan drinks beer. On New Year's Eve, in a house rather than a motel
room, he drinks red wine out of a jelly jar and nobody says why. That
is the whole device: **one substitution, unremarked, doing the work of
a paragraph of interiority.**

This file specs the pattern so every book gets one. Each book declares
its registers in `canon/REGISTERS.md`; `register-check.py` verifies the
default actually holds and each spend lands where it was declared.

---

## Two kinds of register

**A spend** is momentary. The substitution happens once and the default
resumes — Dan's wine on New Year's Eve, and he is back on beer after.

**A shift** is permanent. The substitution becomes the new default from
that chapter on — Aisha puts on the staff parka at ch 7 and wears it
for the rest of the book. A shift says something has *changed*, not
that something *happened*.

Declare which in `canon/REGISTERS.md` — mark a shift `[shift]`. The
checker holds them to opposite standards: a spend used twice is a
habit, and a shift that keeps vanishing was never a change.

## The rules

1. **A register has a default, and the default must be boring.** If the
   ordinary state is interesting, the variation has nothing to push
   against. Beer is right because beer is nothing.

2. **Establish the default before you spend it.** At least three
   ordinary uses before the first substitution, or the reader reads the
   change as a random detail rather than a signal.

3. **A spend is once.** The same substitution twice stops being a
   signal and becomes a habit. If a book needs two wine nights, the
   second one is a different register or a deliberate rhyme that the
   page acknowledges.

4. **Never explain it.** The moment a character or the narration says
   *he only drinks wine when he's happy*, the device dies. This is the
   one rule with no exceptions.

5. **The reader should feel it on a second read, not the first.** A
   register that announces itself is a symbol. A register that works is
   a texture the reader trusts before they notice it.

6. **Spend against the curve.** A register's changes should land on the
   beats in `curves.md` — the midpoint, the retreat, the dark night —
   because that is where a feeling needs saying without words.

---

## The registers worth running in every book

Not all of them, every time. Three or four, chosen for the cast.

| Register | Default | What a change says | Already live here |
|---|---|---|---|
| **Drink** | one thing, ordinary | mood, occasion, who they are with | Dan: beer → wine (NYE) → bourbon (planned) |
| **Name** | what the town calls them | intimacy, and who is listening | "Doc"/"Coach" in public, first names alone |
| **Seat** | the same stool, the same chair | belonging, and its loss | the two Checkerboard stools with the register between them |
| **Clothing** | their own coat | being looked after | the staff parka with her name over the patch |
| **Vehicle** | their own truck | exposure; who sees whom | the two-door F-150, the RAV4 two streets over |
| **The animal** | a graded, consistent reaction | a second opinion the reader trusts | Ratchet's tail: van one thump, crew trucks two |
| **Food** | what they always order | comfort, ritual, an offering | the Coach's Slice; the pie the Table sends |
| **Sound** | the radio, the yard, the ear | attention, and where it goes | Cal runs the campus by ear |

**The animal is the strongest of these** and the most under-used. A dog
with a *graded* reaction — not just happy or not, but a scale the
reader learns — becomes an instrument the reader reads faster than they
read dialogue. Ratchet's one-thump-for-a-delivery-van is the best
register in the series and it has been spent exactly once on purpose.

---

## The name register, in detail

The author's own idea, 2026-09-07: *"having different people call
different characters by unique names is kind of a good signature. We
could have across many books."*

Names carry three variables at once, which is why they are the richest
register available:

- **Who is speaking.** Only Ty calls her Mack. Only Verna says "my
  winter doctor."
- **Where they are in the relationship.** Aisha says "Merritt" in her
  head for fourteen chapters, then "Dan," and the page marks the
  change: *"she had said it once in a bar and not since, and it came
  easier in an empty room than his last name did."*
- **Who else is in the room.** The terms make them "Doc" and "Coach" in
  public and first names alone. The public name is the cost of the
  secret, paid in every scene, and the reader hears it.

**The rule:** a one-person name is a spend. It never drifts into a
second mouth by accident. `canon/NAMES.md` records the sole-use column
so a drafter cannot quietly give it away.

---

## What the checker verifies

`register-check.py` reads `canon/REGISTERS.md` and reports:

- **Default not established** — fewer than three ordinary uses before
  the first spend.
- **Spent early** — the substitution appears in a chapter before its
  declared spend. This is the failure that devalues the planned beat,
  and it is easy to commit months apart.
- **Spent twice** — a `spend` appears in more than one chapter. A
  `[shift]` is exempt; it is *supposed* to persist.
- **A shift that vanishes** — declared permanent and then absent from
  the character's later POV chapters.
- **Declared but missing** — the spend chapter is written and the
  substitution is not in it.
- **Explained** — narration within two lines of the substitution
  contains a "because"-shaped clause. Rule 4, the only absolute one.

It cannot tell you whether the substitution *lands*. That is the
panel's job, and the author's.

**And it cannot check a register carried by a situation.** Dan's seat
register spends at ch 19 by putting *somebody else* on the stool next
to his — an absence and a substitution of person, with no noun to grep.
Declared in `canon/REGISTERS.md` so no drafter spends it twice, and
verified by eye. A register carried by a noun is checkable; one carried
by a situation is not, and pretending otherwise would be the false
confidence this whole environment exists to avoid.
