# Whole-book sampling run — spec + manifest (2026-08-29)

**Author-directed ("kick off some of these sampling ideas").**
Four instruments run against accepted ch 1–28 plus the STAGED
ch 29–30 (PR #99 open — finale findings are provisional until
merge). Sampling is seeded (seed 20260829) and scripted; the
manifest below makes every result reproducible. Blind
instruments receive ONLY excerpt text with opaque IDs — no repo
access, no chapter numbers; the orchestrator holds the keys.

**Action thresholds, set in advance** (so findings become a
short list, not a re-litigation of the book):

1. **Bookstore browse** (10 random ~300-word pages, cold):
   finding = a page the reader would put back on the shelf.
   Polish item only if ≥3 pages fail, or 2 fail in the same
   four-chapter region. Agent: romance-reader-panel (no card;
   panel deck TK).
2. **Warmth map** (one ~300-word window per chapter, shuffled,
   scored 1–10 on want/warmth alone): report the distribution;
   polish item only where ≥2 ADJACENT chapters land in the
   bottom quartile. Agent: romance-reader-panel (no card).
3. **Voice-drift dating** (16 narration paragraphs, 2 per
   4-chapter era, shuffled): the critic guesses early/middle/
   late book and names the tells used. Drift finding only if
   era-accuracy beats chance materially (>60% within one era)
   AND the tells named are un-ruled (the Closeness law and the
   scrub-era bans are DESIGNED drift — guessing from those is
   not a finding). Named un-ruled tells feed RECENT watches.
   Agent: red-team-critic, card C1 (LRU, first draw).
4. **Continuity fuzz** (8 random distant chapter pairs,
   |i−j| ≥ 8): full cross-read per pair hunting seams no
   wave-local sweep could see. Mandatory findings → the
   POLISH-PASS list; ruling-needed → PR flags. Agent:
   continuity-keeper, card E2 (LRU, first draw — weakest-first
   ordering applied to the pair queue).

**Manifest (seed 20260829):**

- Browse pages drawn from chapters: 14, 6, 24, 15, 12, 20, 26,
  25, 23, 17 (IDs B01–B10 in that order; text withheld from
  this note to keep future instrument runs blind).
- Warmth windows: one per chapter 1–30, presented shuffled as
  K01–K30; key held in the run's scratchpad
  (key-warmth.json) and reproducible from the seed.
- Dating paragraphs: 2 per era (1–4, 5–8, 9–12, 13–16, 17–20,
  21–24, 25–28, 29–30), 40–140 words, narration-led, shuffled
  as D01–D16; era key reproducible from the seed.
- Fuzz pairs: (3,11) (4,25) (6,17) (7,24) (9,25) (14,23)
  (19,27) (19,28).

Results file as notes/sampling-<instrument>-2026-08-29.md.
Findings above threshold land on the POLISH-PASS list (STATE)
or as PR flags — nothing here reopens accepted prose on its
own; the author rules per the standing model.
