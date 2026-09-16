# Failure taxonomy — mined from parts 05–08

**Source:** session `01QTG1FrnesYj8GqPKzMQrXC`, Sep 7–15 2026, four
transcripts in `raw/`. Mined 2026-09-15.

Part 01's audit asked *"is the check a mechanism or another document?"*
These four ask the harder question: **when an instrument exists and is
good, what makes it stop working?** Five distinct mechanisms, all
present here, none of them anyone being careless.

---

## 1. THE SUPERFAN, ANSWERED

The question I could not answer from the repo is answered verbatim.

> **Author** (Sep 14, 22:36): *"Are we still using the Super fan?"*
>
> **Showrunner:** *"No. The superfan hasn't run on a Book 1.2 chapter
> since the outline gate on August 30… For 1.2, the romance panel took
> over the pre-acceptance read chapter by chapter, and she quietly
> dropped out of the loop. **Nothing decided that; it just happened.**"*

**Not (a) never knew. Not (c) decided to skip.** It is a fourth thing I
did not offer: **displacement.** An adjacent instrument — the romance
panel — grew to cover the same slot, and the older one fell out of the
loop without any decision being made. Fifteen chapters.

**The detector was the human.** No instrument noticed a fifteen-chapter
gap in its own roster. The author did, in a one-line question.

The showrunner's own proposed fix names the right thing: *"I'll write it
into the pipeline and the roster **so it stops depending on memory**."*
That is `accept-gate.sh`, and this transcript is its justification.

**Design note for the gate:** it must detect *absence over time*, not
just absence at one moment. A per-chapter check would have passed
happily for fifteen chapters, because no chapter's brief ever claimed
the superfan was due. The right shape is a **roster staleness report**:
for every instrument, when did it last run, and is that longer than its
stated cadence.

---

## 2. DRIFT — the same failure, three times

| # | What drifted | How long | Who caught it |
|---|---|---|---|
| 1 | **Three-drafter competition.** The protocol's default for new chapters; ch 9–12 each ran one drafter. *"It's still on the books, and honestly, we drifted from it… it's a deviation, and I should have said so."* | 4 chapters | the author, asking |
| 2 | **The superfan.** Above. | 15 chapters | the author, asking |
| 3 | **The card summary format.** The template asked for "what has happened so far, by chapter," so *"every card since chapter 9 came out as a run of beats."* | 7 chapters | the author: *"Sometimes it reads like a list of things"* |

**All three were caught by the author asking a question.** None by an
instrument. Drift is invisible from inside a session because each
individual chapter looks correct — the deviation only exists across
chapters, and nothing in the studio reads across chapters.

---

## 3. THE JUDGE CONTAMINATED THE WRITER

The single most important structural finding in these four files. From
the instrument auditor's second run (Sep 10, 23:47):

> **"The panel has become the book's second drafter. Ten sentences of
> chapter 15 and eight of chapter 16 are the panel's exact words,
> pasted in by the drafter as 'fixes.' The protocol forbids a second
> voice, and nobody was logging it."**
>
> *"And when the audit offers an example sentence, the blind drafters
> converge on it, which is how two of three reached for 'name in my
> mouth.'"*

Two separate contaminations:

1. **The judge's prose entered the manuscript.** A panel that writes
   example lines gets those lines pasted in as fixes. Eighteen
   sentences of a "competition winner" were written by the judge.
2. **A shared upstream document de-blinds a blind competition.** Three
   drafters who never saw each other's work converged on the same
   phrase because the *audit* had suggested it. The competition was
   structurally blind and informationally not.

**Fix applied then:** *"The panel now says what a line must do and never
writes it. The audit's example sentences are banned text on arrival."*

**Fix still owed:** nothing logs it. A graft log — every line whose
provenance is not the drafter — was named in the backlog and never
built. **Provenance per sentence** (build #4 on the 2026-09-15 list) is
this finding's real answer.

---

## 4. SILENT CORRUPTION — the class nobody can read their way out of

| Where | What happened |
|---|---|
| Sep 7, 22:45 | **The listening-file tool dropped any card line starting or ending in bold.** *"Every 'where we are' you've read since chapter 9 was missing two to six lines."* The author read corrupted summaries for four chapters. |
| Sep 4, 01:41 | *"the audit notes file on disk is a stub (my extraction missed the report)"* — a verdict file existed with nothing in it. |
| Sep 13, 16:48 | *"my edit had written the corrected brief to a stray file, so the plots copy lacked the audit"* — a drafter nearly ran on an uncorrected brief. |

Three instances of **an artifact that exists, looks right, and is
wrong.** No amount of careful reading catches these; the reader cannot
see what was dropped.

**This is the strongest argument in the whole corpus for evidence over
instruction.** The fix is cheap and mechanical every time: a tool that
produces an artifact must assert something about it — line count in
versus out, non-empty, checksum. `accept-gate.sh` checks that verdict
files *exist*; **it must check they are non-trivial.**

---

## 5. TEMPLATE-INDUCED SAMENESS — and the displacement that follows a narrow fix

The repo's rules keep becoming templates. Four instances:

- **The opening recital.** *"the first paragraph seems very similar to
  previous first paragraphs. **I don't have a good way of checking.**"*
  Ch 10, 11, 12 all opened on the same calendar recital — one sentence
  **word for word in all three.** Cause: the brief's own rule, *"say
  the day and the stake in the first paragraph."*
- **The card summary** (drift #3 above), same cause: the template.
- **Variance card D7**, "open every scene mid-motion," produced scenes
  that never said where they were. *"it was the variance card's fault."*
- **The ceiling rules.** The auditor's best line: *"Every rule it has
  written is a **ceiling** — once, one line, one clause, at most — and
  the scenes where the two leads are alone were the only scenes with
  **no floor**. So you said 'staccato,' then 'robot,' then 'terse' on
  three chapters in a row, and each time the room answered with more
  ceilings."*

**And then the subtlest finding in all four files.** `opening-check.py`
was built to catch the calendar opening. Five days later the superfan
reported:

> *"every scene starts with what time it is and which stool"* — and
> ch 4, 15, 17, 18 and 19 all open that way.

**A narrow check does not eliminate a tic; it displaces it.** The rule
was "no calendar opening," so the drafters found a different recital
that satisfied the letter. The countermeasure is not a longer ban list
— it is a **sameness detector**: compare each new opening against all
previous ones and flag convergence of *shape*, whatever the shape is.

---

## 6. AGENT-TO-HUMAN COMMUNICATION — the ungoverned surface

Three rejections in four days, all about the agent's own output, none
about the prose:

- Sep 9: *"Ha ok. Remember **don't be so clever**!"* (a PR named "the
  handful," which the author then had to ask about)
- Sep 10: *"Remember the summaries before the chapter needs to read
  easily. Sometimes it reads like a list of things."*
- Sep 11: *"**Too much to read** make more concise"* → cards capped at
  350 words

Plus the founding ruling, Sep 3: the say-it test *"applies to your
writing to me as much as to the manuscript."*

**Taste entry 13 governs this and nothing checks it.** Every other
entry has a panel, a lint or a gate; the one about talking to the author
has a sentence. It is also the entry with the most repeats per unit
time in the whole ledger.

---

## 7. WHAT THE AUTHOR HIMSELF BUILT

Worth recording, because it argues against over-automating the room:

- **The instrument auditor was his idea** (Sep 7): *"let's add some type
  of agent that scanned all of our agents for potential mistakes like
  this one. Maybe it only runs every few chapters."*
- **The comment-tracking system was his idea** (Sep 4).
- **The glorious week** — the best structural fix in these four files —
  was his, and the showrunner said so: *"Yes. It fits, and **it's better
  than what I proposed**."*
- **The provider-partner stake**, which fixed the annex's motivation
  problem, was his (Sep 7).

Every one of these came from him reading the output and noticing
something was off. **That is the scarce resource the guardrails exist to
protect** — not to replace.

---

## The build list this changes

1. **Roster staleness report** — NEW, and now ranked first. For every
   instrument: last run, stated cadence, chapters since. Catches all
   three drifts. The superfan gap would have shown up in week one.
2. **Non-trivial artifact assertion** in `accept-gate.sh` — a verdict
   file must have content, not just exist. Three silent-corruption
   instances demand it.
3. **Sameness detector** over openings and card summaries — shape
   convergence, not a ban list, because a ban list displaces the tic.
4. **Provenance per sentence / a graft log** — promoted. The panel wrote
   eighteen sentences of two "competition winners" and nothing logged
   it.
5. **Lint the agent's output to the author**, not just the prose —
   taste entry 13 is the only ungoverned surface in the studio.
6. **Changelog conflicts**: three in one day (Sep 8). Every PR appends
   to the same file at the same spot. Mechanical; an append-only
   fragment directory fixes it permanently.
