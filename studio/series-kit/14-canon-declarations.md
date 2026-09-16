# 14 — Canon declarations (the four files every book needs)

Copy these into `books/<book>/canon/` when a book starts. They are what
the checkers read; without them a book gets the mechanical checks and
none of the story ones.

Mechanism: `studio/MECHANISM.md`. Specs: `studio/craft/`.

**Where each one lives.** The test is *does it change when the next
book starts?* `FACTS.md` and `NAMES.md` are series canon and live one
level up, shared. `BEATS.md` and `REGISTERS.md` are per book.

---

## `canon/FACTS.md` — canon as greppable assertions

```markdown
# <Series> — the fact manifest

| ID | Subject | Fact | Established | Scope | Contradicted by (regex) |
|---|---|---|---|---|---|
| F-XXX-01 | <who> | <stated positively, as canon has it> | <ch and line> | series \| 1.1 \| 1.2 ch08–end | `<narrow regex>` |
```

**Add a row the day an error is caught.** Sixty seconds, pays every run
forever. Scope matters: a fact can be true only after ch 11.

**The regex must be silent on approved prose.** If it fires on a page
the author has accepted, it is wrong — narrow it or drop the row.

---

## `canon/NAMES.md` — who the page calls whom

```markdown
| Character | Aliases | Sole use |
|---|---|---|
| <first name> | <every form: first, surname, title, role, "the <role>"> | <name only one person may use> |
```

Required by `story-matrix.py` and `register-check.py` to attribute
anything to a character. Auto-derivation gets this wrong — it gave the
doctor "Coach" and the coach "Doc", because they share scenes.

A **sole use** is a spend. It never drifts into a second mouth.

---

## `canon/BEATS.md` — which chapter carries which beat

```markdown
# Beat map — <Book>

**Planned chapters: NN.** Written and accepted: 1–N.

## Plot — studio/craft/hauge.md
| Beat | Target % | Chapter |
|---|---|---|
| Opportunity | 10 |  |
| Change of Plans | 25 |  |
| Point of No Return | 50 |  |
| Major Setback | 75 |  |
| Climax | 90 |  |

## Romance — curves.md §1
| Beat | Target % | Chapter |
|---|---|---|
| Meet / re-meet | 10 |  |
| No way | 18 |  |
| Adhesion | 25 |  |
| Midpoint of love | 50 |  |
| Inkling of doubt | 56 |  |
| Deepening doubt | 68 |  |
| Retreat | 75 |  |
| Dark night | 82 |  |
| Grand gesture | 90 |  |
| Whole-hearted yes | 98 |  |

## <Lead A>'s arc / <Lead B>'s arc — curves.md §2
| Identity established | 5 |  |
| The wound glimpsed | 15 |  |
| First crack | 25 |  |
| Essence glimpsed | 50 |  |
| Retreat to identity | 75 |  |
| Essence chosen at cost | 90 |  |

## <Antagonist> — curves.md §3
| Sighted | 10 |  | · | First cost | 25 |  |
| The shape is understood | 50 |  | · | Maximum pressure | 75 |  |
| Beaten | 90 |  | · | The residue | 98 |  |
```

**Fill this at the outline gate, before a word is drafted.** It is the
highest-value moment in the mechanism. Book 1.2's "first crack at 43%
against a target of 25%" was visible here and instead cost the author
thirteen chapters of reading to notice.

---

## `canon/REGISTERS.md` — the small things that carry the feeling

```markdown
## <Character> — the <register>

- **default:** `<searchable term>` or `<term a>\|<term b>` or `<term> !<exclude>`
- **established by:** ch N

| Ch | Substitution | What it says |
|---|---|---|
| N | `<term>` | <what the change means> |
| N | `<term>` | **[shift]** <permanent from here> |
```

Terms must be **literal and searchable**, not descriptions. `stool`,
not "the stool nearest the register". A register carried by a
*situation* rather than a noun is not checkable — declare it anyway,
marked, so no drafter spends it twice.

`[shift]` = permanent. A spend used twice is a habit; a shift that
vanishes was never a change.

---

## Then

1. Add the book's rows to `studio/agents/CADENCE.md`.
2. Run `python3 studio/tools/coverage.py books` and confirm the new
   book is **covered**. If it is listed as NOT COVERED, its manuscript
   layout does not match the convention — one chapter per file, named
   to sort, under `manuscript/`.
3. Run `bash studio/tools/guardrails.sh --book books/<book>`.

Everything else is inherited. **No checker should need editing for a
new book; if one does, that is a leak in the checker, not a job for
the book.**
