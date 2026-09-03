# Getting a book onto Kindle — the actual mechanics

**Filed 2026-09-03 at the author's request.** Companion to
`gtm-overview-2026-07-28.md` (portfolio strategy, pre-dates the campus
series) and `kindle-romance-market-study-2026-08-01.md` (the romance
economics). This doc is narrower than either: **what physically has to
happen** between a finished manuscript and a live Amazon listing.

Nothing here is a strategy proposal. Where the author has already
ruled, it says so and builds on it.

---

## 0. WHERE THE CAMPUS SERIES ACTUALLY STANDS

- **Book 1.1: 67,533 words, 30 chapters, complete and edited.** That is
  a full-length contemporary romance, comfortably in band.
- **Book 1.2: 8 of 30 chapters written**, outline ratified.
- **Already ruled (STANDARDS.md, author 2026-08-08):** *"ship four at a
  time — the quartet is the unit of work and of launch."*

That ruling is the correct one and this doc assumes it. The romance
study independently reached the same place: **bank 3-4 finished books
before Book 1 ships**, because Amazon's 30-day new-release window
rewards cadence and a series monetizes one discovery event across every
title. The author got there first.

**Nothing in this portfolio has ever been published.** Every step below
is a first time, which is the main reason to write them down.

---

## 1. THE HONEST POSITIONING FLAG (read before the cover brief)

The market study of 2026-08-01 recommended **demon/monster paranormal
romance, high steam, 50-70k words**. What got written is **small-town
college-town contemporary, closed-door, 67.5k words**.

That is not a mistake — it is a different shelf, and it needs to be
named out loud before anyone commissions packaging:

| | The study's recommendation | What exists |
|---|---|---|
| Shelf | Dark/monster paranormal | Small-town contemporary, **sweet branch** |
| Steam | Explicit, mandatory to the niche | Closed-door (standard 9 — cut at the first garment) |
| Cover language | Photographic, moody | **Illustrated** (the sweet/rom-com convention) |
| Competition | Very high | Much lower |
| Ceiling per title | Higher | Lower |
| Reader | Binge-reads, high churn | Voracious, loyal, under-served |

**Consequences, stated plainly:**

1. **The study's $50k-in-24-months math does not transfer.** It was
   built on high-steam KU velocity. Sweet small-town is a real,
   commercially viable ecosystem with full-time indie careers in it —
   but the arithmetic has to be redone against clean/sweet comps
   before any revenue expectation is set. [TK: that redo]
2. **Packaging must match the sweet branch.** The study's own rule:
   mismatching heat and packaging earns "false advertising" one-stars.
   A closed-door book in steamy packaging is the single most
   predictable way to tank a launch.
3. **Book 1.2 raises the heat one notch** (one licensed door-ajar side
   scene, ch 11). That is still inside the sweet branch, but it is a
   labeling question by Book 3. [TK: author call]

---

## 2. WHAT HAS TO EXIST BEFORE YOU CAN UPLOAD ANYTHING

Six things. Four of them do not exist yet.

### 2a. The file — and a real problem inside it

The manuscript is 30 markdown files in git, each opening with a
production header. Getting to EPUB is mechanical:

```
strip production headers  →  concatenate in order  →  add front/back
matter  →  convert  →  validate  →  upload
```

The stripper already exists (it builds the listening files). The
conversion tool is a choice, not a problem — **Kindle Create** (free,
Amazon's own, takes .docx), **Vellum** (Mac only, ~$250, the industry
default for a reason), **Atticus** (~$147, cross-platform), or
**pandoc** (free, scriptable, and the natural fit for a manuscript that
already lives in git).

**THE SCENE-BREAK JOB — corrected 2026-09-03 (same day):**

The first version of this doc claimed the manuscript had *zero*
scene-break markers. **That was wrong** — the orchestrator sampled
one chapter and extrapolated. The line-copy-editor's instrument
(`books/campus-series/notes/scene-break-instrument-2026-09-03.md`)
read all 30: **22 chapters carry markers (53 in all, a mix of `---`
and `***`); 5 are single continuous scenes; 3 need breaks they lack.**

What is actually owed before EPUB, per that report:
- **12 breaks missing** (1 HIGH, 4 MEDIUM, 7 LOW — e.g. ch 23, kitchen
  morning to diner noon, no marker).
- **10 existing markers that fail the time/place test** — section
  dividers inside one continuous scene (five in ch 3's market
  morning, two fencing a three-line vignette in ch 19). A human
  should look at these with a view to removing, not adding.
- **One form.** `studio/STYLE.md` names `***`; 43 of the 53 markers
  are `---`. Conform in the same pass, because the EPUB converter
  will render the two differently.

Still a real pre-publication pass with editorial judgment inside it;
much smaller than first stated.

### 2b. Front and back matter — none of it exists

A published ebook is not just chapters. It needs, in order:

- Title page · copyright page (year, rights reserved, "this is a work
  of fiction" disclaimer, ISBN if used) · optional dedication
- The chapters
- **The back-of-book call to action — this is where KU series money is
  actually made.** "Continue the series" with a direct link to Book 2,
  a newsletter signup, and a review request. Every book in the quartet
  needs one, and Book 4's points back to Book 1.
- "Also by" page · author note · about the author

### 2c. The cover — the single biggest lever

Genre-correct signalling beats artistic quality every time. For sweet
small-town contemporary that means **illustrated**, warm palette, town
or porch iconography, clearly legible series branding at thumbnail
size. Budget **$150-800** for a professional genre cover; a
four-book set should be commissioned as a set so the shelf reads as one
series.

The paperback needs a *different* file — a full wrap with spine, and
the spine width depends on final page count, so it comes last.

### 2d. The blurb and the metadata

- **Title + subtitle + series name.** Note: **Book 1.2's title is still
  [TK]** (flag-13, open since the outline). The *series* name matters
  more than either — the study's finding is that a series brand should
  be stronger than the pen name.
- **Description**, ~4,000 characters, light HTML allowed. Trope-forward,
  not plot-summary. This is a written deliverable, not a form field.
- **7 keyword slots** — these are trope phrases readers actually search,
  not single words.
- **Categories** — chosen at upload and adjustable afterward. The sweet
  branch has its own bestseller categories (Clean & Wholesome), which
  is a genuine discovery advantage of this shelf. [CHECK: Amazon has
  changed the number of selectable categories more than once; verify
  the current limit at upload.]

### 2e. The pen name — decide before anything is public

Romance readers expect genre-dedicated pen names, and the study already
flagged firewalling this work from the middle-grade titles. This is
hard to undo once a listing, an Author Central page and reviews exist.
**[TK: author call]**

### 2f. Copyedit and proofread

The studio's line pass is a *craft* pass — it is not a proofread by a
fresh human eye, and no amount of agent review substitutes for one on a
book that is about to be sold. **$400-900** for 67k words.

---

## 3. THE KDP MECHANICS, ONCE THE ABOVE EXISTS

1. **Open the KDP account and do the tax interview early.** W-9,
   bank details, tax identity. It is bureaucratic and it can take days.
   Doing this months ahead costs nothing and removes a launch-week
   surprise.
2. **Upload**: the EPUB plus a cover JPEG (2560 x 1600, 1.6:1).
3. **Fill the metadata screen**: title, subtitle, series, author,
   description, keywords, categories.
4. **KDP Select / Kindle Unlimited** — the one genuinely consequential
   toggle. Enrolling makes the ebook **exclusive to Amazon for 90 days**
   (renewing) in exchange for KU page-read income and promo tools.
   For a four-book small-town romance launch by an unknown author this
   is close to a default yes: the romance Top 100 runs ~75% KU-enrolled
   and KU is where series read-through pays. Going wide is a slower,
   list-first game. **Print is never exclusive** — the paperback can go
   everywhere regardless.
5. **Price.** 70% royalty applies from **$2.99 to $9.99**; outside that
   band it drops to 35%. The standard series ladder is Book 1 cheap or
   free as the funnel and Books 2-4 at full price.
6. **Pre-order** (up to 90 days) is optional and genuinely double-edged:
   pre-orders bank into a single release-day rank spike, but they also
   spread the sales that would have made a launch-day burst. Decide per
   book, not as a policy.
7. **Paperback** is a separate upload with its own cover file and its
   own royalty formula (60% of list minus print cost).
8. **Review takes roughly 24-72 hours** before the book is live.

---

## 4. THE SEQUENCE

1. Finish Book 1.2 (in progress; wave 3 of 8 is next after the hold).
2. **Decide the pen name and the series title.** Nothing downstream —
   cover brief, blurb, Author Central — can start without them.
3. **The scene-break pass on Book 1.1**, then build and script the
   EPUB pipeline once, so books 2-4 are one command.
4. Commission the four-book cover set once the series title is locked.
5. Open the KDP account, do the tax interview.
6. Write Books 1.3 and 1.4.
7. Human proofread on all four.
8. Launch the quartet on a 4-6 week ladder so something is always
   inside a 30-day window.

**The two items that are blocking and cheap** are 2 and 5. Both are
decisions or paperwork, neither needs a finished book, and everything
else queues behind them.

---

## 5. WHAT TO VERIFY AT LAUNCH TIME, NOT NOW

These drift, and this doc will be stale before it is used:

- The current KENP per-page rate (Amazon publishes it monthly).
- The number of selectable categories.
- KDP Select's current terms and promo tools.
- Whether KU's share of the romance Top 100 has kept drifting down
  (it fell through 2025) — this is the one fact that could change the
  exclusivity call.
