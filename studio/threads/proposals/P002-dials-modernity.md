# P002 — the Modernity dial: lower the sheet, or change the rooms

Status: OPEN
For: author (then story)
Raised: 2026-09-23 by the environment thread (HANDOFF, guardrails)

## What

`DIALS.md` has declared Modernity 3 for Book 1.1 and 5 for Book 1.2
since 2026-08-29. Measured, they are **1.5** and **2.1**. The sheet has
been wrong for three and a half weeks and the gap reports every run.

## Found by

`voice-dial.py`, in `guardrails.sh`:

```
campus-series  Modernity 1.5  (444 low / 26 contemporary)   declared 3  ✗ off by 1.5
book2          Modernity 2.1  (365 low / 49 contemporary)   declared 5  ✗ off by 2.9
```

## Where

books/campus-series/DIALS.md

## Now

```
| Modernity | 5 (Grapevine ON STAGE; meal trains; group chats; telehealth-era sports med; the modernity register binds props) | +1 |
```

## Proposed

```
| Modernity | 3 — MEASURED 2026-09-23 at 2.1, sheet lowered to the reachable number (was 5, aspirational since 2026-08-30) | +1 |
```

## Why

A dial nobody measures is a wish, and this one has been a wish since the
sheet was written. Two honest ways out, and the author picks:

**A (applied above) — lower the sheet to 3.** 1.2 measures 2.1; 3 is one
click, reachable by swapping two or three rooms in ch 25–30 rather than
rewriting a voice. The 2026-09-16 ruling already set 1.3 and 1.4 at
Modernity 3, so this makes 1.2 consistent with its own quartet.

**B — keep 5 and change the rooms.** The country signal is not
vocabulary: `porch` 223 and `county` 212 are 54% of every country marker
in both books, and those are the rooms the story happens in. Moving from
2.1 to 5 means the Checkerboard, the Liars' Table, the fairgrounds and
the square give way to an apartment, a hospital cafeteria, a rideshare.
That is an outline change six chapters from the end of the book.

The recommendation is A. B is a real option for Set 2, where the dial is
set before the couples are cast; it is not a thing to start at ch 25.

## Verify

After applying, the dial stops reporting:

```
python3 studio/tools/voice-dial.py books/campus-series --compare
```
