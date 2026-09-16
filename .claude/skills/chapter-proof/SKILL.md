---
name: chapter-proof
description: Write the acceptance evidence for a chapter BEFORE drafting it, then fill each line with real output at the end. Use at the start of any drafting, recut, or heat-pass run so "done" is defined before the prose exists.
---

# /chapter-proof

Proof-of-done, for prose. Run it **before** a word is drafted.

A chapter is not done because a thread believes it is good. It is done
when the checks it named up front have real output attached.

## Step 1 — before drafting, write the block

Five to eight lines. Each is a check with a command or a named reader
whose output gets attached at the end. Always include **one thing that
must not have changed.**

```
PROOF OF DONE — <book> ch<NN>, <date>

MECHANICAL (commands, output attached at the end)
  [ ] bash studio/tools/chapter-lint.sh <chapter>        → clean
  [ ] python3 studio/tools/dialogue-lint.py <chapter>    → ≥15%
  [ ] awk 'prev ~ /[:—]$/ && $0=="" {...}' <chapter>     → zero hits
  [ ] every ADDED sentence under 30 words, ≤3 "and"s
  [ ] wrap at 80 columns

READERS (verdict files, path attached at the end)
  [ ] romance-reader-panel   → notes/ch<NN>-panel-<date>.md
  [ ] continuity-keeper      → REQUIRED if this chapter is ACCEPTED
  [ ] superfan-reviewer      → if this closes a wave

MUST NOT HAVE CHANGED
  [ ] <the protected line(s) this chapter contains — quote them>
  [ ] the rung ladder: no kiss, touch or garment moved
  [ ] no new fact, name, date or object not already on the page

VARIANCE
  [ ] card drawn (LRU from studio/agents/variance/LOG.md) and logged
  [ ] banned moves read from studio/agents/variance/RECENT.md
```

## Step 2 — do the work

## Step 3 — fill every line with actual output

Not "lint passes." The lint's output. Not "continuity checked." The
path to the file the keeper wrote.

**If a line cannot be filled, say so instead of declaring done.** A
chapter that reports "panel not run — no agent available" is honest and
useful. A chapter that reports "looks good" is neither.

## The rule this exists to enforce

> A self-check is not a check.

On 2026-09-15 a drafting run reported *"longest added sentence: 27
words"* and had written a 43-word one. It was not lying; it had no
shell and counted by eye. The lint existed the whole time. The
difference between a check and a self-check is who runs it.

Attach the transcript, not the claim.

## Where the block goes

Top of the chapter brief while drafting; then into the PR body, above
the prose, so the author reads the evidence before the chapter.
