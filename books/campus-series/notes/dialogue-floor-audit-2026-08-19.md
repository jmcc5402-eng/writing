# Dialogue floor — first measurement (2026-08-19)

**PROPOSED — instrument output.** First run of
`studio/tools/dialogue-lint.py`, built tonight because the ruling that
created the floor specifies a linter that did not exist.

> **Dialogue floor (author flag, 2026-08-18**, recorded in
> `studio/DRAFTING-PROTOCOL.md`): *"the shelf runs 30–40% dialogue;
> this voice is narration-forward on purpose, so the working targets
> are a book average near 25%, a per-chapter floor of 15%, at most one
> deliberate quiet chapter (~8–10%) per quarter, and never two
> sub-floor chapters in a row. Briefs state the target; **the linter
> counts quoted words and reports the percentage with every
> candidate**."*

Method: words inside double quotes ÷ total body words, with each
file's header block excluded so it cannot dilute the count.

---

## The batch as staged in `campus/ch234-batch`

| Chapter | Words | Quoted | Dialogue | Verdict |
|---|---:|---:|---:|---|
| ch01 *(accepted)* | 2,109 | 211 | **10.0%** | quiet-chapter band |
| ch02 | 1,982 | 119 | **6.0%** | **below floor** |
| ch03 *(as staged)* | 2,101 | 79 | **3.8%** | **below floor** |
| ch04 | 2,104 | 570 | **27.1%** | OK |

**Book so far: 11.8% against a ~25% target. Three sub-floor chapters
in a row, against a rule that permits none.**

## The finding under the numbers

**`manuscript/ch03.md` is the chapter the author rejected.**

Its own header says it was staged from *"blind-competition candidate
C, card D2"* — the **2026-08-16** field. The branch then records
`ch3 REJECTED by author — rerun brief v2`, and three rerun candidates
were drafted on 2026-08-18 to the new dialogue target:

| Rerun candidate | Words | Dialogue |
|---|---:|---:|
| ch3-candidate-A (2026-08-18) | 2,289 | **21.4%** |
| ch3-candidate-B (2026-08-18) | 1,896 | **23.6%** |
| ch3-candidate-C (2026-08-18) | 2,177 | **22.5%** |

All three clear the floor comfortably and hit the ordered target.
**None of them is in the manuscript.** The rerun was drafted and never
staged, so the batch PR presents the rejected version for the author's
read.

Staging any rerun winner moves the book average from **11.8% to
roughly 16%** on its own.

## What the numbers do and do not accuse

**Ch 1 and ch 2 predate the ruling.** The floor was flagged
2026-08-18; ch 1 was accepted 2026-08-16 and ch 2 drafted 2026-08-16.
Neither was written against a target that existed. So this is not a
drafting failure — it is the new rule meeting the existing book, and
the question it raises is the author's:

**Does the floor apply retroactively?** Three readings, all defensible:

1. **Yes, book-wide.** Ch 1 and ch 2 get a dialogue pass. Costs a
   revision of accepted prose; buys a consistent read from page one.
2. **Forward only.** Ch 1 and ch 2 stand; the floor governs ch 5
   onward, and the book average climbs as the book grows.
3. **Ch 2 only.** Ch 1 is the register pilot the author has already
   ruled on twice and edited by hand; ch 2 is unaccepted and cheap to
   re-run.

**Ch 3's design was deliberately quiet, and then wasn't.** The ch3
competition panel calibrated to *"the watching IS the beat; the leads
never speak this chapter."* At 3.8% the staged version executes that
brief faithfully. The rerun brief changed the design. Both facts are
true, and the rerun is what the author asked for.

**Ch 4 is the proof the target is reachable in this voice** — 27.1%
without reading as chatter, in a chapter that is mostly one man and
an antagonist in a motor pool.

## The quiet-chapter allowance

The rule permits one deliberate quiet chapter (~8–10%) per quarter.
Chapters 1–8 are the first quarter, so **exactly one of ch 1–8 may sit
in the 8–10% band and none may sit below it.** Ch 1 is at 10.0% — it
fits the allowance precisely, which makes it the natural candidate to
*keep* quiet if the author rules forward-only. That would mean ch 2
has to come up regardless of how the retroactivity question lands.
