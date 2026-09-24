# P003 — STANDARDS: the quartet is no longer the launch unit

Status: OPEN
For: story
Raised: 2026-09-23 by the delivery thread (environment)

## What

STANDARDS still says the quartet is the unit of launch. The author
ruled on 2026-09-23 (AUTHOR-NOTES 292) that `studio/CYCLE.md` governs
instead: each book ships once the next one is complete. The author's
2026-08-08 words stay as they are; a dated line under them records
that the launch half is superseded.

## Found by

The delivery thread, reading STANDARDS against CYCLE.md while taking
the launch inventory for Book 1.1.

## Where

books/campus-series/STANDARDS.md

## Now

```
**Author note (2026-08-08):** ship four at a time — the quartet is
```

## Proposed

```
**Superseded in part (author, 2026-09-23, AUTHOR-NOTES 292):** the
quartet stays the unit of work but is no longer the unit of launch —
each book ships when the next is complete (`studio/CYCLE.md`).

**Author note (2026-08-08):** ship four at a time — the quartet is
```

## Why

Two rules disagreeing about launch would bring the same question back
at every release, and the author has now ruled on it. Hard rule 7:
decisions get recorded, not remembered.

## Verify

```
grep -n 'Superseded in part' books/campus-series/STANDARDS.md
python3 studio/tools/proposal-lint.py studio/threads/proposals/P003-standards-launch-unit.md
```
