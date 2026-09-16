---
name: canon-audit
description: Sort every rule that shapes agent behaviour in this writing repo by whether it is an instruction, a guardrail, or evidence — and say where each one belongs. Use when the same mistake keeps recurring, when onboarding a new book, or when a thread has "forgotten" a standing rule.
---

# /canon-audit

The prose twin of a context audit. In a writing repo the rules are not
in a lint config; they are in a standards file, a style file, a taste
sheet and a bans ledger, and **almost all of them are instructions** —
things an agent might follow.

That is the trap. A thread that has been drafting for forty minutes has
a standards file somewhere behind it and a chapter in front of it.

## What to read

- the book's `STANDARDS.md` and `SUPERCONCEPTS.md`
- `studio/STYLE.md`, `studio/AUTHOR-TASTE.md`, `studio/PIPELINE.md`
- `studio/agents/variance/RECENT.md` (the bans ledger)
- `CLAUDE.md` and the book's own `CLAUDE.md` if it has one
- `.claude/agents/` — every agent is a bundle of instructions
- `.claude/settings.json` — the hooks, if any
- `studio/tools/` — what CAN be checked mechanically
- the last twenty author comments in `studio/AUTHOR-NOTES.md`

## What to produce

**One table**, every rule you find:

| Rule | Lives in | Kind today | Belongs | Cost if ignored late in a long session |
|---|---|---|---|---|

Kinds, for prose:

- **Instruction** — a line in a standards or taste file. The agent
  usually follows it. Nothing happens if it doesn't.
- **Guardrail** — something that stops the wrong thing landing. In this
  repo that is one of three shapes:
  1. a **greppable ban** (a spent idiom, a blacklisted word)
  2. a **mechanical check** (`studio/tools/*` — columns, sentence
     length, dialogue floor, AI tics, beat counts, word caps)
  3. a **gate on a state transition** — a chapter may not become
     ACCEPTED until named verdict files exist (`accept-gate.sh`)
- **Evidence** — an artifact the work must produce: a panel note, a
  scoreboard, a keeper sweep, a lint transcript, a CHANGELOG entry.

**Then flag drift:**

- rules stated in two places with different wording
- rules an instrument contradicts
- rules that were author catches (AUTHOR-NOTES) and never became bans
- **instruments with no trigger** — an agent that is supposed to run
  "before acceptance" with nothing checking that it did

**Then name the two fixes to make today.** The usual two:
a long procedure that should be a skill, and a "never X" that should
be a check.

## The test for any rule

> If a drafting agent ignored this forty minutes into a long session,
> how bad would it be?

If the answer is "a chapter ships with a contradiction in it," it is a
guardrail written as an instruction.

## The prose-specific finding to watch for

Many of this repo's real rules are not booleans — "the chapter must be
fun," "the leads must be seen," "slow down the good parts." Those
cannot be linted. **They can still be gated**: the guardrail is not a
check on the text, it is a requirement that *a named reader ran and
left a verdict on disk.* An unlintable rule is not an unenforceable
one. It just needs a file instead of a boolean.

Do not change anything. Output the table, the drift and the two fixes.
