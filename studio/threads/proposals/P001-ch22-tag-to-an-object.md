# P001 — the tag-to-an-object scaffold, ch 22

Status: OPEN
For: story
Raised: 2026-09-22 by the environment thread (HANDOFF H003)

## What

Three speech tags in ch 22 use the same scaffold — a line of dialogue,
then `said, to the <object>` — and ch 23 uses it twice more. Vary two of
the three here so the shape reads as a choice rather than a habit.

## Found by

The developmental editor, by hand, in the ch 24 score's "Templates from
21–23" section: *"the tag-to-an-object scaffold, six in two chapters."*
No instrument reads it, because every template check in the studio reads
one chapter or one opening.

```
grep -n 'said, to the' books/campus-series/book2/manuscript/ch2*.md
```

ch22:27, ch22:430, ch22:439, ch23:130, ch23:169, ch24:344.

## Where

books/campus-series/book2/manuscript/ch22.md:439

## Now

```
"Refroze at dark," Sonny said, to the eggs. "Square'll be worse by six.
```

## Proposed

```
"Refroze at dark," Sonny told his eggs. "Square'll be worse by six.
```

## Why

`studio/STYLE.md` and the drafter's banned-moves ledger both treat a
repeated sentence scaffold as a template, and hard rule 3 says the
author's voice is the point — the scaffold IS the voice here, which is
exactly why it should stay rare. One instance in ch 22 is the cheapest
break: ch22:430 (the cook, to the griddle) is load-bearing for the
Slice-as-exception beat the keeper cited, and ch22:27 is the chapter's
first line of dialogue.

This is a proposal, not an edit. The environment thread is scoped off
manuscripts (`studio/threads/SCOPES.md`, L068).

## Verify

After applying, the count in ch 22 drops from three to two:

```
grep -c 'said, to the' books/campus-series/book2/manuscript/ch22.md
```
