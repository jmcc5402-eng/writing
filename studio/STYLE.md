# Style

Shared conventions. A book may override any of these in its own bible — if it
does, the book wins, and the override should be written down there.

## Files

- Manuscripts, bibles, outlines, and notes are Markdown.
- Wrap at 80 columns.
- One chapter per file. Name them so they sort: `ch01-the-return.md`.
- A book's bible is `STORY_BIBLE.md` at the root of the book's directory.

## Drafting

- Break lines at clause and sentence boundaries rather than filling to the
  margin. A reworded sentence should produce a one-line diff.
- Mark unresolved choices inline with `[TK ...]` — placeholder, needs deciding.
  `[TK surname]`, `[TK does she already know?]`. They are meant to be greppable:
  `grep -rn '\[TK' books/` should return the full list of open questions.
- Don't delete a scene to revise it. Move it aside, then cut when the
  replacement is working.

## Prose defaults

- American spelling, serial comma.
- Em dashes unspaced — like this.
- Scene breaks are a centered `***` on its own line.
- Numbers under one hundred spelled out in narration; numerals in dialogue only
  where a character would say them that way.

## AI drafting tics (mandatory sweep)

- **No paragraph ends in a colon or a dash.** The dangling-reveal
  cadence ("...lit by a battery lantern:" + paragraph break) is an AI
  drafting tic, not house voice. A reveal earns its paragraph break
  only as a complete sentence; interruptions and trail-offs resolve
  inside the paragraph, not at its edge.
- Every drafting or editing pass that touches a manuscript runs the
  sweep before delivering, and reports zero hits or names each survivor
  as a deliberate, author-approved beat:

  ```
  awk 'prev ~ /[:—]$/ && $0=="" {print NR-1": "prev} {prev=$0}' <file>
  ```

- Why this rule exists: on the B1 adoption read (2026-08-04) the author
  caught six dangling colons and six dangling dashes across twelve
  chapters. Tics self-copy — voice-matching reads a previous chapter's
  tic as style, so every drafting run reinforced it. Mechanical sweeps
  don't get tired and don't learn bad habits; anything greppable gets
  grepped, not proofread.

- **The 2026-08-22 scrub rules** (author-directed AI-tell scrub of
  campus ch 1–12; evidence in
  `books/campus-series/notes/ai-tell-scrub-2026-08-22.md`):
  - **Endings budget.** At most half the chapters in a book may end
    on a wry button or antithesis couplet ("Nobody X. Everybody Y.";
    "wanted A / settled for B"). At least two chapters per book end
    unresolved, mid-gesture, or on plain information — a sentence
    that sits there being true. Twelve composed landings in a row is
    itself the tell. Briefs deal each chapter an ending register.
  - **No feelings in the filing cabinet outside Cal's POV** (campus;
    generalize per book: the ledger family — filed, logged,
    unbudgeted, itemized, under advisement — applied to emotion is
    ONE character's tic, max twice per chapter, never in a chapter's
    final ten lines).
  - **Body-autonomy scaffold, once per chapter.** The exact idioms
    "before s/he could vote on it" and "before s/he could dress it
    up/down" are spent — banned.
  - **Banned fingerprint words** (campus): "unhurried" (spent);
    "declined to" + mental verb (Cal only, once per book); "That was
    the whole [X] of it" (spent); "and meant it" (spent);
    sentence-initial vague "Somewhere…" (2 per chapter).
  - **Precision-timed feelings: one gauge per chapter** ("for
    exactly N seconds" family). "One beat" in timing constructions:
    closed at five uses (campus).
  - **Personification ration: three per chapter,** memorable ones;
    everything else gets a plain verb.
  - **Someone's joke must die.** Per chapter with 3+ named speakers,
    at least one line of dialogue lands flat, boring, or wrong — and
    stays uncommented.
  - **Homeward-coda cap.** The alone-in-transit-home closing is
    spent for campus Book 1.1; new chapters may not end in a vehicle
    or on a solitary walk home.

## Revision passes

Run them separately. Combining them is how notes get lost:

1. **Structure** — does the scene earn its place, and does it turn?
2. **Character** — is the want, the obstacle, and the cost visible?
3. **Line** — rhythm, repetition, filter words, weak verbs.
4. **Continuity** — names, ages, timeline, geography, established facts.

## The standing table (author observation, 2026-08-18)

Every series anchors on a recurring gathering the reader returns to
— the room where ensemble, comedy, and plot get digested together.
Spytwins has the family dinner; the campus series has wine night
(with the Liars' Table as its public twin). The pattern is now
deliberate: a new series names its standing table at bible time,
and the table earns a scene whenever the plot has been loud for
too long.

## Introduce them at their best (author law, 2026-08-18)

> "A book should introduce the main character at their best. Then
> difficult things happen, which might make the reader second
> guess, but then by the end of the book the reader has passed all
> expectations."

The arc law for every lead in every book here:

1. **The entrance is a highlight reel.** The lead's first chapter
   shows them at their best: competent, generous, admired — good
   works completed on the page, thanks received, compliments
   deflected. The reader roots first and worries later. The campus
   series ch 1 warmth pass (Marisol's rootability directive) is
   the reference implementation.
2. **The middle earns the doubt.** The difficult things are real
   mistakes with real costs, sourced from the same qualities the
   entrance showcased — the strength overextended is what breaks.
   Cosmetic stumbles don't count; the reader must genuinely
   second-guess.
3. **The ending clears the opening bar.** By the last chapter the
   lead surpasses the chapter-one version of themselves — the
   entrance turns out to have been the floor, not the ceiling.

Gate checks, using instruments that already exist (no new ones):
a chapter-1 drafting brief names the lead's at-their-best beats;
the developmental editor judges openings against rule 1 and
climaxes against rule 3; a lead introduced mid-struggle, or an
ending that merely restores the opening's competence, is a
finding.
