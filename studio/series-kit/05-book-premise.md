# Template — Per-Book Locked Premise (Q1–Q4 + banked ingredients)

_Proven by: `books/spytwins/plots/book-02-japan.md` (LOCKED PREMISE)
and `book-03-toronto.md`. This form REPLACED the flat fill-in
worksheet, which died in production. Brainstorm in conversation; the
author locks the shape here; the outline expands it._

---

## LOCKED PREMISE (author, YYYY-MM-DD) — <Working Title>

_Supersedes any earlier scaffold where they conflict. Brainstorm
record: <where>. Outline next via plot-architect._

**Q1.** <First quarter in 1–2 sentences: arrival/setup, the problem
lands, why it belongs to the heroes.>
**Q2.** <Second quarter: investigation deepens, the fair-but-wrong
turn — someone close gets implicated / the cost gets personal.>
**Q3.** <Third quarter: the clock and stakes fuse; the evidence
tightens the wrong way; all-is-lost approaches.>
**Q4.** <Fourth quarter: the earned climax and the turn that
transforms the problem — the resolution's SHAPE, stated plainly.>

**Banked ingredients:** skill = <what pays at the climax, and where>;
<ingredient> = <its placement>; running gag = <thing> (N touches:
<t1>, <t2>, <t3>); food = <beat>; nudge/curriculum = <one line>;
weather = <how it changes the plot>; wow = <set piece>; crossover
lesson = <whose / NONE this book per cadence>.

**Safety rails (locked, this book only):** <hard limits the premise
itself imposes — e.g. "kids never cross the airport fence line".>

**Open:** [TK <names/details the author will pick>]
[CHECK: <cultural/factual items for the researcher pass — run it
BEFORE drafting>]

**Waivers:** <none, or `WAIVED: <rule> — <reason> (author, <date>)`>

---

**Kit notes.**
- The Q-shape is the author's PreSnowflake template compressed: the
  quarters carry problem → obstacles/herrings → point of no return →
  disaster-and-resolution.
- Banked ingredients are COMMITMENTS — the outline honors them
  verbatim; the ingredient audit checks the rest of the checklist.
- Keep [TK]s open through outlining. Names and cultural specifics are
  filled by the author and the researcher, never by the outline.
- After the research pass, deposit unused nuggets in the setting bank
  (see `books/spytwins/series-bible/city-bank.md` for the model).


---

## The dials — REQUIRED before a drafter launches  *(L077)*

The author, 2026-09-23: *"I'm OK if this book feels country, because
that's how this set has shaken out. I wanna make sure that in future
sets or books if I want to dial the vibe left or right I can."*

He could not, and this section is why. Book 1.2's sheet declared
**Modernity 5** on 2026-08-30 and the prose measured **2.1**. The gap
survived twenty-four chapters because nothing asked for the number at
the gate and nothing measured it until `voice-dial.py` existed.

**Every book's premise names its dials, as numbers, before the outline
is approved.** Copy this block into the book's `DIALS.md` row.

| Dial | Scale | Set it by |
|---|---|---|
| **Modernity** | 1 small-town country → 10 contemporary/cosmopolitan | the ROOMS and the INSTITUTIONS |
| **Warmth** | 1 cool, formal, apart → 10 warm, funny, together | the chorus and the ensemble |
| **Edge** | 1 mild oaths → 10 profane | vocabulary (the only dial words move) |
| Audience centre, Humour register, Heat | declared only | the panel's ear |

### The rule this exists to teach

**You do not move Modernity with a word list.** In Book 1.2, `porch`
(223) and `county` (212) are **54% of every country marker in the
book**, and those are rooms, not adjectives. A drafter told "less
country" drops a *y'all* and writes another porch scene.

So a premise that wants a different vibe names **different rooms,
different institutions and different jobs** — an apartment, a hospital
system, a rideshare, a city council — and the dial follows. A premise
that names the same rooms and a higher number is a wish.

### The checks

- `voice-dial.py <book> --first 3` the day chapter 3 exists. **Three is
  the floor**; one or two chapters hold too few markers to score. Book
  1.2 read 1.8 at three chapters against a finished 2.1 — the drift was
  findable at 8,000 words.
- `voice-dial.py <book> --drivers` names which words are actually
  carrying the dial, so a wrong number points at the outline rather
  than the prose.
- `guardrails.sh` runs the full comparison against `DIALS.md` every
  stint. **The adjacency rule holds**: no dial moves more than one click
  between neighbouring books in a set.
