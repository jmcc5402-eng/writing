---
name: propose
description: Document a page change instead of making one — a file the writer thread can apply without judgement. Use whenever a check finds something wrong on a manuscript page and this thread is scoped off manuscripts, or whenever a change should be the book thread's call.
---

# /propose

The author, merging #183 (2026-09-22): *"Instead of making any changes
just document your changes to any chapters so I can provide to my writer
threads."*

`thread-scope.py` stops this thread editing a chapter. This is the other
half — the thing it should do instead. A lock that prevents the wrong
action does not produce the right one.

## When

Any time you would have edited a manuscript, brief, card or note and a
check, a lint or a reader gave you the reason. One proposal per change.
If the fix is a drafting instruction rather than a specific replacement
("let one or two sentences run per chapter"), it is **not** a proposal —
it is a `HANDOFF` row. Proposals are for text you could have typed.

## How

1. `python3 studio/tools/proposal-lint.py --list` — see what is already
   open, so you do not raise the same thing twice.
2. Pick the next free number. Write
   `studio/threads/proposals/PNNN-<slug>.md` with **exactly** these
   sections, in this order:

   - `Status: OPEN` and a `For:` line naming the scope that must act
   - `## What` — one line, plain
   - `## Found by` — the instrument, and the command that reproduces it
   - `## Where` — `path:line`, repo-relative
   - `## Now` — a fenced block holding the **exact current text**
   - `## Proposed` — a fenced block holding the **exact replacement**
   - `## Why` — the rule, ledger ID or reader finding it serves
   - `## Verify` — a runnable command whose answer changes after it lands

3. **Read the file and copy the text out of it.** Do not type it from
   memory. `proposal-lint.py` checks that the `Now` block appears in the
   named file byte for byte and exactly once, which is the whole point:
   the writer thread searches for `Now` and replaces it with `Proposed`,
   with no judgement about what the page currently says.
4. `python3 studio/tools/proposal-lint.py` until it passes.
5. Raise or update the `HANDOFF` row that points at it, so the proposal
   reaches the other thread at its next session start.

## What makes a bad proposal

- A `Now` block typed from memory. The lint will catch it; it is still
  the most common way this goes wrong.
- A `Now` block so short it appears twice on the page. Quote more.
- Bundling three changes in one file. One proposal, one replacement.
- Proposing prose the author has not asked for. A proposal fixes
  something an instrument found. Taste is the author's, and a page the
  reader liked is not a defect because a tool has an opinion.

## After it is applied

The writer thread sets `Status: APPLIED` (or `WONTFIX` with a reason in
the file) and closes the `HANDOFF` row in the same commit. A proposal
that is neither open nor applied is a ghost, and the instrument-auditor
reads for those.
