# The mechanism

How a guardrail gets built in this studio, so the next one takes an hour
and works on every book instead of this one.

Eight guardrails were built on 2026-09-15/16 and the same four-part
shape appeared every time without anyone planning it. Writing it down
is what turns a habit into a mechanism.

---

## The four parts

```
  studio/craft/<pattern>.md        the SPEC        book-agnostic, reusable
  books/<book>/canon/<X>.md        the DECLARATION this book's instance
  studio/tools/<check>.py          the CHECKER     generic; reads both
  .claude/settings.json            the TRIGGER     so nobody has to remember
        or studio/tools/guardrails.sh
```

**Spec.** What the pattern is, why it exists, and its targets. Written
once, for the studio, never naming a character. `hauge.md`,
`curves.md`, `registers.md`.

**Declaration.** What this book does with the pattern. Which chapter
carries which beat; who is called what; which drink is the default.
Tables a human maintains and a tool parses. `BEATS.md`, `NAMES.md`,
`REGISTERS.md`, `FACTS.md`.

**Checker.** Reads the spec's rules and the book's declaration,
measures the manuscript, reports the gap. **Takes a book directory as
an argument and knows nothing else about the book.**

**Trigger.** A hook fires it, or `guardrails.sh` does. A checker with
no trigger is a script somebody has to remember, which is the condition
this whole environment exists to escape.

---

## The rules, learned the hard way

**1. Declare rather than derive.** Auto-deriving name aliases gave the
doctor "Coach" and the coach "Doc", because they share scenes and "Doc"
is what *he calls her*. A heuristic that is subtly wrong is worse than
a declaration a human wrote in sixty seconds. Derive only as a fallback,
and say in the output which one you used.

**2. Measure before you set a threshold.** Every number in `ai-tells`
came from running the corpus first. The author expected em dashes to be
the problem; they run at a median of 0.9 per thousand words and the
real tells were structural. A guessed threshold flags the wrong thing
with total confidence.

**3. Narrow until it is silent on clean text.** Three tools needed
three tuning rounds each. *Ratchet is female* first matched "Ratchet saw
**him** to the gate" — that is Cal. **A row that fires on approved prose
trains everyone to skim the output, and a skimmed check is an
instruction again.**

**4. Never ban a shape; measure its rate.** Banning the calendar
opening moved the tic to "what time it is and which stool" within five
days. Cluster and report whichever cluster grew, including shapes
nobody has thought of.

**5. Separate absolute from spent.** An absolute never appears. A
*spent* thing has already been used legitimately and must not be used
*again* — so it is checked against the diff, not the corpus. Getting
this backwards reported fifteen violations that were all the original
approved uses.

**6. Say what the checker cannot do, in the checker.** Dan's seat
register has no noun to grep. Two of the continuity sweep's five
blockers are beyond any regex. Writing the limit into the docstring is
what keeps the rest credible — a tool that claims full coverage earns
false confidence, which is worse than no tool.

**7. Report coverage, never assume it.** `find_books` returned an empty
list for three of this repo's four books — they use `manuscripts/`
plural, or a single master file — and said nothing. **A guardrail suite
that reports "all clear" on books it never opened is worse than no
suite: it is false confidence with a green tick.** `coverage.py` now
prints what is covered and what is not, and why, before anything runs.

**8. A gate checks content, not attendance.** `accept-gate.sh` asks
whether the verdict file exists *and is non-trivial*. A stub passed as
a verdict once. The next version should parse the verdict's PASS/FAIL,
because a panel note saying FAIL would pass the gate today.

---

## Which declarations go where

| File | Lives at | Scope |
|---|---|---|
| `FACTS.md` | series | physical canon, character law, anything true across books |
| `NAMES.md` | series | the name map; sole-use names are series furniture |
| `BEATS.md` | **book** | which chapter carries which beat — changes every book |
| `REGISTERS.md` | **book** | defaults and spends — a register may recur, its spends do not |
| `CADENCE.md` | studio | which instrument owes what, how often |

The test: **does it change when the next book starts?** If yes, it is a
book declaration. If no, it is series canon.

---

## Starting a new book

1. Copy the four templates from `studio/series-kit/14-canon-templates/`
   into `books/<book>/canon/`.
2. Fill `BEATS.md` from the outline **at the outline gate**, before a
   word is drafted. This is the highest-value moment in the whole
   mechanism: a beat declared late shows up as a number before it costs
   a chapter. Book 1.2's "first crack at 43% against a target of 25%"
   was findable at the gate and instead took the author thirteen
   chapters of reading.
3. Seed `FACTS.md` from the bible rather than after the first
   contradiction.
4. Add the book's rows to `CADENCE.md`.
5. Run `python3 studio/tools/coverage.py books` and confirm the book
   is **covered**, not silently skipped.
6. Run `guardrails.sh`. Everything else is inherited.

The convention the checkers require, from CLAUDE.md: **one chapter per
file, named to sort, under `manuscript/`.** Only campus-series follows
it today; spytwins, youngnick and mybyb are listed as NOT COVERED until
they conform or a checker is taught their layout deliberately.

A checker never needs editing for a new book. If one does, that is a
leak — fix the checker, do not fork it.

---

## Adding a new guardrail

Write the spec first, even if it is four lines. A checker without a
spec encodes a rule nobody agreed to, which is how a lint becomes
policy by accident.

Then: declaration format, checker, trigger, and **a test against live
data**. Every tool here was built against real bugs on `main` rather
than synthetic examples, which is why each one found something on its
first run and why each one needed tuning. A guardrail that has never
been wrong has never been tested.

Finally, add it to `guardrails.sh` and to the table in
`studio/ENVIRONMENT.md`. A guardrail nobody runs is a file.

---

## The division of labour this serves

The machine counts, remembers, and holds thirty chapters in mind at
once. It does not judge.

Every checker in this studio reports **where to look**. Not one of them
has an opinion about whether the prose is good, and none of them should
acquire one. That is the panel, the superfan, and the author — and the
whole point of automating the counting is to spend more of the author's
attention on the part only he can do.

## The lesson loop (2026-09-20)

The four parts above are for a pattern. For a single author catch the
shape is smaller and runs the same day: the words (AUTHOR-NOTES), the
page (a fold pass), the Kind, the enforcer, the ledger row, and
`lesson-check.py` to prove it. See `/lesson` and
`studio/lessons/LEDGER.md`. The test of a guardrail is a fixture that
fires; a guardrail nobody has watched fire is an instruction.
