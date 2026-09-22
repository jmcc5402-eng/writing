# The environment

**How this studio stops agents making mistakes, as opposed to asking
them not to.**

Fifteen specialist agents wrote most of two novels here and produced
excellent work nearly every time. The failures were never carelessness.
They were rules that existed, were correct, were written down — and
were *instructions*.

This file is the map of what is now enforced, what is merely written,
and what is deliberately left to a human.

---

## The three kinds, and where this repo sits

| Kind | What it is | If ignored |
|---|---|---|
| **Instruction** | a standard, a taste entry, an agent's remit | nothing happens |
| **Guardrail** | a greppable ban, a mechanical check, or a gate on a state change | the wrong thing does not land |
| **Evidence** | a verdict file, a lint transcript, a listening file | review reads it before the prose |

On 2026-09-14 the count was **1,768 lines of instruction, 15 agents,
7 checkers nothing invoked, and zero hooks.** Every rule was an
instruction, and the checkers were instructions wearing a lab coat:
running them depended on an agent remembering.

---

## What runs now, and when

### Automatically, via `.claude/settings.json`

| Event | Runs | Can it block? |
|---|---|---|
| **SessionStart** | `roster-staleness.py` | no — it prints into context so every session opens knowing what has gone quiet |
| **PostToolUse** on `Edit\|Write\|MultiEdit` | `prose-guard.sh` | no — `PostToolUse` is advisory by design; the edit already happened, and the finding goes back to the agent |
| **PreToolUse** on the PR tools | `pr-lint.py` | **yes** — a PR body that fails the say-it test never reaches GitHub |
| **PreToolUse** on `SendUserFile` | `card-lint.py` | **yes** — a chapter card under `notes/cards/` that is over 350 words, has a 30-word sentence, a two-sentence call, or a ledger word never reaches the author (2026-09-17) |
| **SessionStart** | `matrix-strip.py --current` | no — prints the chapter-in-progress row of `canon/TARGETS.md` (and plan → actual once the readers have run) so every session opens on the plan (2026-09-19) |
| **PreToolUse** on `Bash` | `commit-scope.py` | **yes** — a `git commit` whose files span two scopes (a book, studio, agents) or whose subject prefix names the wrong one is refused (2026-09-20; the showrunner's own mixed commit the day before) |
| **PreToolUse** on `Agent` | `brief-gate.py` (+ the matrix row must be in the drafter's prompt) | **yes** — a drafting-assistant launched on a brief with no AUDIT ADDENDUM and VERDICT on disk does not launch (2026-09-17; the ch 18 stray-file mistake, BACKLOG F36) |
| **PreToolUse** on `Bash` (a `git push`) | `id-check.py` | **yes** — a ledger ID or author-note number that is a different row on another fetched thread refuses the push (2026-09-21; two threads minted L067 and 245 the same day; L069) |
| **PreToolUse** on `Edit\|Write\|MultiEdit\|NotebookEdit`, `Bash`, `Agent` | `thread-scope.py` | **yes** — on a branch scoped `environment` in `studio/threads/SCOPES.md`, an edit to a manuscript, brief, card or note, a `git add -A`, a `sed -i` or redirect onto a story path, or a drafter launch is refused (2026-09-21; the author: "the other thread always reverts to the story"; L068) |

`PreToolUse` is the only event that can stop an action. Everything else
reports.

### The lesson loop (author, 2026-09-20: "every bug does two things")

| Piece | What it does |
|---|---|
| `studio/lessons/LEDGER.md` | every author catch, its Kind, and what now enforces it — or why nothing can |
| `studio/lessons/bans.txt` + `fixtures.tsv` | the greppable bans as data; `bans.py --test` proves each one fires. `prose-guard.sh` and `chapter-lint.sh` read the file, so a ban is enforced the day it is written |
| `studio/lessons/reader-tests.txt` | the unlintable lessons: a reader, a test, a token. `accept-gate.sh` demands the token on the verdict's `TESTS:` line (from ch 22) |
| `studio/tools/lesson-check.py` | refuses a ledger row with no enforcer, a ban with no fixture, a reader test the agent does not carry, and a recent author note with no ledger row. Runs in `guardrails.sh`, and `pr-lint.py` runs it on every [FOLD] PR |
| `/lesson` | the procedure, per catch: the words, the page, the Kind, the enforcer, the row, the check |

Its first run caught, on the chapter it was built from, a place-stamped
line ("She had not said it yet in this building") that the drafter, the
panel and the showrunner had all read past.

### Tests for the guardrails, and the catch map (the doc's /hook-check and /what-would-catch-this, 2026-09-20)

`bash studio/tools/hook-check.sh` feeds every hook a known-bad input
and a known-good one and reports DEAD for any that lets the bad one
through. `python3 studio/tools/catch-map.py [origin/main]` names, for
every changed file, what would fail if it were wrong, and says GAP
where nothing would. Both run in `guardrails.sh`.

### On demand

```
bash studio/tools/guardrails.sh            # every check, one command
bash studio/tools/accept-gate.sh <book> <ch>   # may this chapter be accepted?
```

---

## The guardrails, and the failure each one killed

| Guardrail | Kills | The evidence |
|---|---|---|
| `roster-staleness.py` + `CADENCE.md` | **Drift** | The superfan ran on no chapter for 15 chapters. *"Nothing decided that; it just happened."* Two more drifts the same shape: the three-drafter competition lapsed for 4 chapters, the card format for 7. All three caught by the author asking a question. |
| `accept-gate.sh` | **A skipped stage** | A chapter cannot be marked accepted without its verdict files on disk. Continuity read required for folded prose. Also asserts verdict files are **non-trivial** — a stub file passed as a verdict once, and the listening tool silently dropped bold lines so the author read four chapters of summaries missing 2–6 lines each. |
| `fact-check.py` + `canon/FACTS.md` | **Canon contradictions** | Found 6 live contradictions on main in under a second, reproducing 3 of the continuity sweep's 5 blockers plus 3 secondary findings. The sweep took 16 minutes and had to be remembered. |
| `prose-guard.sh` | **Mechanical defects** | Columns, AI tics, banned idioms, added-sentence discipline, epigraph cap, and a warning when the chapter is ACCEPTED. Caught a 37-word epigraph on its first run — and, later the same day, a banned idiom in prose *it had just helped produce*. |
| `opening-sameness.py` | **Template drift** | Names no forbidden shape on purpose. Found that **53% of Book 1.2 opens `object-first`** — the tic that appeared *after* the calendar opening was banned. |
| `pr-lint.py` | **Talking to the author like an engineer** | Taste entry 13 was the only entry with no check and the most repeats per week: *"don't be so clever," "too much to read," "reads like a list of things."* |
| `card-lint.py` | **The card that reads like a ledger** | The card is the one document the author reads for every chapter and the one with the most repeated notes ("reads like a list," "too much to read," a 40-word sentence read aloud at the ch 20 audit). The rules lived in the showrunner's remit. Now the send is blocked. |
| `matrix-strip.py` (SessionStart; in `brief-gate.py`, `pr-lint.py`) | **A plan nobody looked at** | The author: "what tool can we build to ensure that this matrix is viewed before and after each chapter?" Before: the drafter cannot launch without the row in its prompt; the card cannot be sent without it. After: a [FOLD] PR cannot open without plan → actual; the accept gate runs the comparison. |
| `thread-scope.py` + `studio/threads/SCOPES.md` | **The environment thread drifting to the page** | The author (2026-09-21): "I need an engine to hyper focus on the environment. The other thread always reverts to the story." A thread told to build checks fixes the page instead, because the page is right there and the fix is satisfying — an instruction failing the usual way. Now the branch cannot: the fix goes on the board for the book thread and the check gets built. On its first day the lock found its own branch already carrying ten manuscript edits from before the ruling. |
| `targets-check.py` (in `accept-gate.sh`, from ch 21) | **A chapter with no definition of done** | Ch 20 counted twenty romance beats and the author read it as "a normal old book," a 2 or 3. Nothing had asked for a number before the draft. Now the card carries seven targets, the panel writes actuals, and a romance level two or more under target holds the chapter. |
| `brief-gate.py` | **A drafter on an unaudited brief** | 2026-09-13: the audited ch 18 brief went to a stray file; two of three blind drafters worked from the unaudited copy. Drafter rule 8 was the fix, as an instruction. Now the launch is blocked. |

---

## The idea that makes prose governable

Most of what a novel cares about is not a boolean. *Is it fun. Are the
leads seen. Slow down the good parts.* That is the usual reason people
conclude prose cannot be governed like code.

> **An unlintable rule is not an unenforceable one. The guardrail is not
> a check on the text — it is a requirement that a named reader ran and
> left a verdict on disk.**

`accept-gate.sh` never reads the prose. It asks whether
`notes/ch14-panel-*.md` exists and has content in it. That single move
turns fifteen optional specialists into a pipeline that cannot silently
skip a stage.

It generalises past prose: any domain with expert judgment that resists
assertion — design review, legal sign-off, security review — can be
gated the same way. Not *was it good*, but *did the named reviewer run,
and where is their verdict*.

---

## Two rules learned the hard way

**A narrow check displaces a tic; it does not remove it.** The opening
check banned the calendar opening and the drafters found another
recital that satisfied the letter — "what time it is and which stool,"
across five chapters. That is why `opening-sameness.py` clusters shapes
instead of banning them. **Prefer a detector that finds convergence to a
list that forbids yesterday's convergence.**

**A row that fires on clean prose is worse than no row.** The
`FACTS.md` rule for *Ratchet is female* first matched "Ratchet saw
**him** to the gate" — that is Cal — then matched every "his head" in
the book. Twenty-five findings, almost all garbage. **Narrow the pattern
until it is silent on clean text, or retire it**, because a check
everyone skims has quietly become an instruction again.

---

## What is deliberately NOT enforced

Being honest about this is what keeps the rest credible.

- **Staging inside a scene.** Two of the continuity sweep's five
  blockers — a gaze relocated mid-scene, an action order reversed — are
  beyond any regex. They belong to the continuity-keeper, gated by
  `accept-gate.sh`.
- **Whether the prose is any good.** No tool here has an opinion about
  that. The panels, the superfan and the author do.
- **Provenance per sentence.** The instrument auditor found that *"the
  panel has become the book's second drafter — ten sentences of ch 15
  and eight of ch 16 are the panel's exact words, pasted in as fixes."*
  Nothing yet logs which agent wrote which line. This is the largest
  known gap.

---

## The mechanism

Every guardrail here is the same four parts, written up in
`studio/MECHANISM.md`:

```
studio/craft/<pattern>.md     SPEC         book-agnostic
books/<book>/canon/<X>.md     DECLARATION  this book's instance
studio/tools/<check>.py       CHECKER      generic; reads both
.claude/settings.json         TRIGGER      so nobody has to remember
```

`studio/tools/booklib.py` holds the conventions in code, so a new
checker inherits them instead of re-deriving where books live.
`coverage.py` says which books are actually covered — three of this
repo's four are not, and used to be skipped in silence.

Templates for a new book: `studio/series-kit/14-canon-declarations.md`.

## The ratchet

**Fix the bug, then fix the thing that let the bug in.** Every author
catch becomes, the same day, one of three things: a greppable ban, a
check, or a gate. Taste entry 14 has said this from the beginning — and
it was itself an instruction, which is exactly why the enforced count
sat at four out of nineteen.

So the ratchet now has a handle: **add the row, add the check, and say
why in the commit.** An instrument may absolutely be retired or slowed.
What must not happen is it going quiet with nobody deciding.

---

## Adding a book

1. `SUPERCONCEPTS.md` — the three or four things it wins on.
2. `/chapter-proof` before chapter one is drafted. Costs nothing,
   needs no infrastructure.
3. `canon/FACTS.md` seeded from the bible, **before** drafting rather
   than after the first contradiction.
4. Point `accept-gate.sh` at the new book's notes directory with the
   instrument list that book actually needs.
5. Add its rows to `CADENCE.md`.

Anything useful in two books moves to `studio/` by PR. That is how one
book's guardrail becomes the studio's.
