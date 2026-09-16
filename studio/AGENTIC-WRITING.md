# Agentic writing: one author, one repo

The writing-repo translation of *Getting started: one developer, one
repo*. Same thesis, different domain — and the domain turns out to
matter less than you would expect.

> The teams getting the most out of agents are the ones that trust the
> model least. They stopped asking it to be careful and built an
> environment where it cannot be careless.

Filed 2026-09-15, using this repo's own failures as the test data.

---

## The diagnosis, in one command

```
$ ls .claude/
agents  skills

$ wc -l books/campus-series/STANDARDS.md studio/STYLE.md \
        studio/AUTHOR-TASTE.md studio/agents/variance/RECENT.md
  327  STANDARDS.md
  742  STYLE.md
  542  AUTHOR-TASTE.md
  157  RECENT.md
 1768  total

$ cat .claude/settings.json
cat: .claude/settings.json: No such file or directory
```

**1,768 lines of rules. Fifteen agents. Seven working checkers in
`studio/tools/`. Zero hooks.**

Every rule in this repo was an instruction. The checkers existed and
ran only when an agent remembered. That is the whole problem, and it is
visible in an `ls`.

---

## What actually went wrong, 2026-09-14 to 15

Not hypotheticals. One working day, one repo, one author.

| What happened | Rule kind it relied on | What would have stopped it |
|---|---|---|
| A parallel thread **skipped the superfan** before acceptance — it forgot | Instruction | A gate on the ACCEPTED transition |
| A drafter reported *"longest added sentence 27 words"*; it had written a **43-word** one | Self-reported evidence | The lint, invoked by something other than the agent |
| An **epigraph shipped at 37 words** against a 35-word cap | Instruction | A word count in a hook (found it in 2 seconds once written) |
| Two heat passes ran on accepted, folded chapters **with no continuity read**. Both drafters flagged it. Everyone agreed. It merged anyway → **5 contradictions on main** | Instruction | A gate: folded prose cannot be re-accepted without a keeper verdict |
| `git add -A` swept Book 1.1's files onto Book 1.2's branch | — | A commit-scope check |
| A container restart lost a completed market study | — | Commit-and-push before long work, not after |
| Earlier: commits landed **after** their PR merged; Rules v1 never reached main | — | Verify merges from `git log`, not API flags |

Five blocking contradictions in ~86 added sentences — **about one per
seventeen**. Every one was a *seam* error: a line true of the book and
false of the page it landed on. Which is exactly the class the skipped
instrument catches.

**The pattern: no one was careless. Every failure was a rule that
existed, was correct, was written down, and was an instruction.**

---

## The three kinds, translated

| Kind | In code | In prose |
|---|---|---|
| **Instruction** | CLAUDE.md line, skill, review comment | A standard, a taste entry, an agent's remit |
| **Guardrail** | PreToolUse hook, lint rule, test, CI | (1) a **greppable ban** · (2) a **mechanical check** · (3) a **gate on a state transition** |
| **Evidence** | Test output, curl result, diff stat | A **verdict file** — the panel note, the scoreboard, the keeper sweep, the lint transcript |

### The one genuinely new idea

Most of what a novel cares about is not a boolean. *Is it fun. Are the
leads seen. Slow down the good parts.* You cannot lint those, which is
the usual reason people conclude prose can't be governed like code.

That conclusion is wrong, and the fix is the useful export:

> **An unlintable rule is not an unenforceable one. The guardrail is
> not a check on the text — it is a requirement that a named reader
> ran and left a verdict on disk.**

The evidence artifact is a *file*, and the gate is on the state
transition, not the content. `accept-gate.sh` does not read the prose.
It asks whether `notes/ch14-panel-*.md` exists. That single move turns
fifteen optional specialists into a pipeline that cannot silently skip
a stage — and it is exactly what "the thread forgot the superfan"
needed.

This generalises past prose. Any domain with expert judgment that
resists assertion — design review, legal read, security sign-off — can
be gated the same way: not "was it good," but "did the named reviewer
run, and where is their verdict."

### Surprise: more is mechanizable than anyone assumes

Already checkable here, and mostly already written:

- 80 columns · sentence length · "and" chains · dialogue-percentage
  floor · AI drafting tics (dangling colon/dash) · banned idioms from
  the recency ledger · romance-beat floor per chapter · ending-register
  budget · opening-line repetition · epigraph word cap · **protect-list
  lines that must never change** · **load-bearing plants that must
  never be cut**

Those last two are the prose analogue of an architecture rule, and they
are the highest-value checks in the repo. The continuity sweep found
that ch 14's fence-line thumb is load-bearing for ch 18's payoff — a
future reviser deleting it would break a plant three chapters later and
nothing would notice. That belongs in a manifest and a hook, not in a
sentence someone hopes gets read.

---

## The artifacts

### Shipped with this document

| Artifact | Kind | What it does |
|---|---|---|
| `studio/tools/prose-guard.sh` | Guardrail | PostToolUse hook on every manuscript edit: columns, AI tics, banned idioms, added-sentence discipline, epigraph cap, and a loud warning when the chapter is ACCEPTED |
| `studio/tools/accept-gate.sh` | Guardrail | A chapter cannot be marked accepted without its verdict files on disk. Continuity read **required** for folded prose. `SUPERFAN_REQUIRED=1` for wave boundaries |
| `.claude/settings.json` | Wiring | Makes the guard run without anyone remembering |
| `/canon-audit` | Skill | Sorts all 1,768 lines by instruction/guardrail/evidence and names the two fixes to make today |
| `/chapter-proof` | Skill | Proof-of-done for a chapter, written before drafting, filled with real output after |

`prose-guard.sh` found the 37-word epigraph on its first run against
main, unprompted.

### Worth building next, in order

1. **`protect-manifest.md` + a hook.** Every swoon line and load-bearing
   plant, by chapter and quoted. The hook refuses an edit that changes
   one without an explicit override. This is the highest-value guardrail
   in the repo and it does not exist.
2. **`fact-manifest.md` per book.** Greppable canon — *Ratchet is
   female. Cal is brown to the elbow. The check is five fifteen and
   daily from ch 11.* Three of today's five blockers were fact errors a
   manifest would have caught at draft time. The keeper is a better
   instrument than a grep, but the grep runs every time.
3. **`/blast-radius` for prose.** Before handing a chapter to an agent:
   is it accepted? folded? does it contain a protected line? a plant
   another chapter pays? The autonomy level is a property of the
   chapter, not of the thread.
4. **`variance-draw.sh`.** The LRU card draw is computed by hand from a
   400-row log on every single run. It is a procedure, so it should be
   a script.
5. **`/what-would-catch-this`** on a manuscript diff.

### Already here and worth naming

- **`instrument-auditor`** is `/session-postmortem`, already running
  every four chapters, already producing numbered findings (F1–F35).
  The ratchet exists.
- **`RECENT.md`** is the ratchet's output: every author-caught tic
  became a greppable ban within the day. That is *"fix the bug, then
  fix the thing that let the bug in,"* already house practice.
- The **reading page** (`reading-page.py`) is evidence for a human: the
  author reads prose on a phone instead of a diff.

---

## Applying this to the next book

The promotion rule, in writing terms: **anything useful in two books
moves from the book's folder to `studio/` by PR.** A check written for
the campus series that the middle-grade series also needs belongs in
`studio/tools/`, not copied.

For a new book, in order:

1. `SUPERCONCEPTS.md` — the three or four things it wins on (exists).
2. **The proof-of-done block before chapter one is drafted.** Cheapest
   possible start; needs no infrastructure.
3. `accept-gate.sh` pointed at the new book's notes directory, with the
   instrument list that book actually needs.
4. A fact manifest from the bible, before drafting rather than after
   the first contradiction.
5. Then the ratchet: every author catch becomes a ban, a check, or a
   gate **the same day**, and the environment never loosens.

---

## The five questions, answered honestly for this repo

1. **Context.** Does the agent know what a senior editor knows?
   *Partly.* 1,768 lines is not short and not all true — the sweep found
   rules stated twice with different wording. **Run `/canon-audit`.**
2. **Delegation.** Can I say what a task must not touch? *Now, yes* —
   the protect list exists in the survey. It is not yet enforced.
3. **Verification.** Is acceptance evidence written before the work?
   *It is now* — `/chapter-proof`. It was not, and that is why a
   drafter's self-count stood in for a lint.
4. **Review.** Is every hard rule enforced by something other than good
   behaviour? *No — this is the gap.* Today: two hooks and a gate,
   against 1,768 lines of instruction. Better than zero.
5. **Recovery.** Did the last bad session produce a one-line change?
   *This document, two hooks and two skills.* The bad session was
   yesterday.

---

## The uncomfortable part

This repo is unusually well-run. Fifteen specialist agents, a variance
system, a recency ledger, typed PRs, a taste sheet in the author's own
words, an auditor that audits the instruments themselves. It is more
disciplined than most production codebases.

**And every one of today's failures happened anyway**, because
discipline that lives in prose is an instruction, and instructions are
the weakest of the three kinds. The sophistication of the instructions
had no bearing on it. A 742-line style guide and a one-line hook are
not the same tool, and only one of them was awake at 11 p.m. when a
drafter counted its own sentences by eye.

That is the whole lesson, and it is worth more to a customer than any
amount of agreement about the principle: *you can do all of this right
and still be one `ls .claude/` away from the trap.*
