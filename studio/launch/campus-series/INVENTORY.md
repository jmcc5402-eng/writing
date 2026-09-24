# Book 1.1 launch inventory

**Taken 2026-09-23 by the delivery thread.** Everything a KDP launch of
Book 1.1 needs: what exists, what doesn't, who does it, how long it
takes. The release rule is `studio/CYCLE.md`: 1.1 ships when 1.2 is
complete (21 of 30 accepted today), the pre-launch review says SHIP
and the export is clean. Book 1.1 launches by itself (AUTHOR-NOTES
292).

**Nothing goes live on Amazon without the author's explicit go.**

## Start these now — the long-lead items

These take calendar time, not writing time, and nothing on the
manuscript blocks them. Most of the waiting is on other people, so
these are the jobs to fill the months before 1.2 is done.

| # | Item | Who | Lead time | Why now |
|---|---|---|---|---|
| A | **Book 1.1's own title** | author (studio drafts candidates) | days to decide | Nothing names Book 1.1. The pen-name memo settled the series and the byline only ("does NOT title Book 1.1 or 1.2"). The cover, the description and the title page all wait on it. |
| B | **Pen name and series name checked by hand**: USPTO trademark search, Amazon, Goodreads, BookBub, domains and handles (memo §4) | author | 1–2 hours | Annie Farrow / Millrow are ruled (D19, #113), but the collision checks were web-search only and the memo lists four checks a person must make. Do it before money is spent on a cover with the name on it. |
| C | **KDP account, tax interview, bank details** | author | 1 hour + days of latency | Flagged "blocking and cheap" since 2026-09-03. |
| D | **Cover**: brief, then commission | studio drafts the brief; author buys | 2–8 weeks from a designer, set commissions longer | The biggest sales lever there is. It waits on A (the title) and on the fade-to-black shelf (PR #189). Commission a four-book set so the shelf reads as one series. |
| E | **Human proofread** | author hires; studio prepares the file | 2–4 weeks turnaround; $400–900 for 67k words | No agent pass substitutes for a fresh human eye on a book that is for sale (mechanics §2f). It should read the export, after the pre-launch review's fixes. |
| F | **Newsletter signup** — a list provider and a landing page | author (studio drafts the copy) | an afternoon | The back page has to link somewhere real before 1.1 ships. |

## Everything else

Status: **none** · **partial** · **done**.

### The book file

| Item | Status | Who | Notes |
|---|---|---|---|
| Clean export | **partial** | studio | `export-book.py books/campus-series`: 30 chapters, 66,693 reader words, **no workshop text**. Only the front and back matter are missing. |
| Front matter: title page, copyright, dedication placeholder | none | studio | Goes in `studio/launch/campus-series/front-matter.md` (AUTHOR-NOTES 293). The title page waits on A. |
| Back matter: continue-to-1.2 page, newsletter, review request, about the author | none | studio | Same directory. The 1.2 page needs 1.2's title, which is still [TK] (flag-13). A placeholder link works until 1.2 has an ASIN. |
| Scene breaks | none | story thread | The 2026-09-03 instrument found 12 breaks missing, 10 that don't pass the time/place test, and one form to settle. Still undone: the manuscript carries 42 `---` and 11 `***`. Page work, so it goes to the story thread via `/propose`. The export can at least normalize the form. |
| Pre-launch review (O002) | none | story thread | Glaring errors only. The gate reads `notes/prelaunch-review-*.md` with a VERDICT line. Best run around 1.2 = 27/30. |
| EPUB | none | studio | pandoc from the export, since the manuscript already lives in git. Validate with epubcheck and preview in Kindle Previewer (a free download). |
| Print interior (PDF) | none | studio | Needs a trim size (5×8 or 5.5×8.5 is standard) and the final page count, which then sets the spine width. |

### The listing

| Item | Status | Who | Notes |
|---|---|---|---|
| Description | none | studio drafts → author rules | ~4,000 characters. Must state fade to black (AUTHOR-NOTES 260). The 2026-09-15 bright lines hold unless the shelf move changes them: "college" in the blurb only, no quarterback in the first line, the ages in paragraph two. |
| Categories | none | studio drafts → author rules | Now general small-town contemporary romance, **not** Clean & Wholesome (fade to black). The 2026-09-15 category map was built for the clean shelf and has to be redone. |
| 7 keyword phrases | none | studio drafts → author rules | Trope phrases readers actually search, re-checked against fade-to-black vocabulary. |
| Comps | partial | studio | The 2026-09-15 comps are clean-shelf (Morgan, Kelley, Gussman…). Refresh them against the fade-to-black neighbourhood. |
| Price and KU | none | studio drafts → author rules | Default recommendation: KU-exclusive, 1.1 priced as the funnel. Decide what "funnel" means for a single release — no Book 2 is live on day one. |
| Pre-order: yes or no | none | author | Optional, up to 90 days. Decide per book. |
| ISBN (print) | none | author | KDP's free ISBN or a bought one (Bowker in the US). The free one names KDP as the publisher. |
| Author Central page, bio, photo | none | author | After the listing exists. |

## The shape of it

- **Blocked on nobody:** C, B, F, the EPUB pipeline, the front and back
  matter drafts (with [TK] where the title goes).
- **Blocked on PR #189 (fade to black):** description, categories,
  keywords, comps, the cover brief. #189 is open, and until it merges
  the shelf move is a ruling in chat and nothing more. Merge it before
  anything shelf-shaped is drafted.
- **Blocked on the title (A):** the cover, the title page, the
  description's headline.
- **Blocked on 1.2 = 30/30:** the release itself, the review, the
  proofread.

## Verify

```
python3 studio/tools/export-book.py books/campus-series --check
python3 studio/tools/cycle.py --gate 1.1
```
