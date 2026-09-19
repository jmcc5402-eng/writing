# Targets — what good looks like, chapter by chapter, before it is written

The matrix the author asked for (2026-09-19): one row per chapter, all
thirty, a number per thing the book sells, set BEFORE the chapter is
drafted. The card's Targets line is this row, copied — the card lint
refuses a card whose line differs from it; `targets-check.py` compares
the row with the readers' actuals at the accept gate; `scorecard.py`
writes the actuals beside it in `notes/SCORECARD.md`. Change a number
here, with a word on why in the commit; nowhere else.

**Rows 1–20 are the baseline, not a plan:** those chapters were
written before the matrix existed, so their cells are the readers'
ACTUALS (the panel's romance level; the developmental editor's
development, wound, town, menace), filled by `/chapter-score` on
2026-09-19. **Rows 21–30 are the plan**, drafted by the showrunner
from the outline, the curves (`studio/craft/curves.md`) and the beat
map (`BEATS.md`), for the author to edit.

## The columns

| Column | Scale | Who scores the actual |
|---|---|---|
| Romance | 1–10, the reader's (1 a normal book with a couple in it · 5 never forgets the book, nothing to tell her group · 10 stayed up) | romance-reader-panel |
| Heat | 0–8, the CHARGE scale; never above standard 9's 8; a ceiling, not a floor | romance-reader-panel |
| Aisha, Dan | 0–3 development (0 not moved · 1 seen · 2 tested · 3 turned) | developmental-editor |
| Wound | 0–3 — how hard a lead's wound is pressed on the page (0 untouched · 1 named · 2 pressed · 3 the wound decides something) | developmental-editor |
| Fun | laughs: 0, 1 or 3 | romance-reader-panel |
| Town | 0–3 — how much the town works on the page (0 a room anywhere · 1 a named room · 2 a town institution doing its job · 3 the town acts on the story) | developmental-editor |
| Menace | 0–3 — Boyd's pressure on the page (0 absent · 1 a name or a sign · 2 in the room · 3 he moves) | developmental-editor |
| Ends | up · down · flat · button | romance-reader-panel |
| Talk | quiet (8–15%) · normal (15–25%) | dialogue-lint |
| Words | the prose budget; ±15% on target | wc |
| Pays | who loses something this chapter (one name; "nobody" is allowed once a book) | the brief's reversal |

## The matrix

| Ch | POV | Romance | Heat | Aisha | Dan | Wound | Fun | Town | Menace | Ends | Talk | Words | Pays |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | A | 3 | 1 | 1 | 1 | · | 1 | 3 | 1 | up | normal | 2461 | Aisha |
| 2 | D | 4 | 2 | 1 | 1 | · | 1 | 2 | 1 | flat | quiet | 2779 | Dan |
| 3 | A | 5 | 2 | 2 | 1 | · | 1 | 3 | 0 | flat | quiet | 2674 | Aisha |
| 4 | D | 6 | 3 | 1 | 2 | · | 3 | 3 | 1 | up | normal | 2658 | Dan |
| 5 | A | 6 | 3 | 2 | 1 | · | 1 | 2 | 1 | down | normal | 2639 | Aisha |
| 6 | D | 5 | 2 | 1 | 2 | · | 3 | 3 | 1 | flat | normal | 3122 | Dan |
| 7 | A | 6 | 4 | 2 | 1 | · | 3 | 3 | 1 | up | normal | 2928 | Aisha |
| 8 | D | 7 | 4 | 2 | 2 | · | 1 | 3 | 2 | flat | quiet | 3129 | Dan |
| 9 | A | 5 | 2 | 2 | 0 | · | 1 | 2 | 1 | flat | normal | 3698 | Aisha |
| 10 | D | 5 | 3 | 2 | 2 | · | 1 | 2 | 3 | flat | normal | 3356 | Dan |
| 11 | A | 7 | 4 | 2 | 1 | · | 3 | 3 | 0 | down | normal | 3241 | Aisha |
| 12 | D | 6 | 3 | 1 | 2 | · | 1 | 3 | 1 | flat | quiet | 3268 | Dan |
| 13 | A | 7 | 4 | 2 | 2 | · | 1 | 2 | 1 | flat | quiet | 2969 | Aisha |
| 14 | D | 8 | 5 | 2 | 2 | · | 1 | 2 | 1 | up | normal | 3165 | Dan |
| 15 | A | 9 | 6 | 3 | 2 | · | 1 | 2 | 0 | up | normal | 3008 | Aisha |
| 16 | D | 8 | 5 | 1 | 2 | · | 1 | 3 | 2 | down | quiet | 3907 | Dan |
| 17 | A | 9 | 8 | 2 | 1 | · | 1 | 3 | 0 | up | quiet | 4596 | Aisha |
| 18 | D | 8 | 8 | 1 | 2 | · | 3 | 2 | 1 | up | normal | 6104 | Dan |
| 19 | A | 6 | 4 | 2 | 2 | · | 1 | 2 | 2 | flat | quiet | 4809 | Aisha |
| 20 | D | 6 | 5 | 2 | 2 | · | 3 | 2 | 2 | down | quiet | 4121 | Dan |
| 21 | A | 7 | 5 | 2 | 1 | 2 | 1 | 2 | 0 | up | quiet | 3500 | Aisha |
| 22 | D | 5 | 2 | 1 | 2 | 1 | 1 | 3 | 2 | flat | normal | 3200 | Dan |
| 23 | A | 6 | 3 | 2 | 1 | 3 | 0 | 3 | 3 | down | normal | 3400 | Aisha |
| 24 | D | 5 | 2 | 2 | 3 | 3 | 0 | 2 | 3 | down | quiet | 3200 | Dan |
| 25 | A | 6 | 3 | 3 | 1 | 3 | 1 | 3 | 1 | down | quiet | 3400 | Aisha |
| 26 | D | 7 | 4 | 2 | 3 | 3 | 0 | 1 | 2 | button | normal | 3000 | Dan |
| 27 | A | 8 | 4 | 3 | 3 | 2 | 1 | 3 | 3 | flat | normal | 3800 | Dan |
| 28 | D | 7 | 3 | 2 | 2 | 1 | 3 | 3 | 1 | up | normal | 3400 | Boyd |
| 29 | A | 9 | 6 | 3 | 3 | 1 | 1 | 2 | 0 | up | quiet | 3400 | Boyd |
| 30 | D | 10 | 7 | 2 | 2 | 0 | 3 | 3 | 1 | up | normal | 3000 | nobody |

Cells marked `·` in rows 1–20 are filled by the developmental
editor's backfill (2026-09-19) when it lands; the heat, fun, town and
menace cells in rows 1–20 are the showrunner's reading of the
accepted pages pending the readers' numbers, and the readers'
numbers replace them.

## The shape the plan draws (rows 21–30)

Romance: 7 (the storm) · 5 (the whip count) · 6 (the album) · 5 (the
suspension, the worst hour) · 6 (the bottom, the coat folded) · 7
(the standoff) · 8 (his name in the boardroom) · 7 (signing day) ·
9 (the answer) · 10 (warm Friday). One dip at 22–24 while the county
turns, then a climb of five to the end — the Romancing-the-Beat curve
(`studio/craft/curves.md` §1: retreat at 75%, dark night, grand
gesture, whole-hearted yes).

Development: Aisha turns at 25 (chooses the offer), 27 (her case is
the chart), 29 (the answer as a want); Dan turns at 24 (says
nothing — the plausible cowardice), 26 (the turn signal away from
home), 27 (his name, the last inch). Wound: pressed hardest at
23–26 (her "nobody has ever spent anything on her"; his "a managed
verdict cannot blindside him"), released at 29–30.

Menace: Boyd moves at 23 (the trawl), 24 (the greenlight), 27 (the
consequence); absent from 21 and 29; glimpsed once at 30.
