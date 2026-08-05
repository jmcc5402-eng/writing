# The PR Workflow — the author as engineering director

_Author vision, 2026-07-30: agents run the publishing company —
plotting, drafting, research, GTM — asynchronously, around the clock.
When they need the author, they open a pull request. The author
triages from anywhere, approves or rules, and the team keeps moving.
The author is not the writer; the author is the engineering director
who merges._

## The core mechanic

**A PR is a recorded decision with an approval button.** This is hard
rule 7 ("decisions get recorded, not remembered") made mechanical:

1. Every PR **contains the doc edit, not just the question.** An
   agent asking for a ruling writes the ruling INTO the canon files —
   the `[Canon decision]` line, the `WAIVED:` line, the outline
   marked PROPOSED — inside the PR diff. Options go in as clearly
   marked alternatives (recommended one applied, others in the PR
   body).
2. **Merge = approved = recorded.** The moment the author merges,
   canon is updated, because the update IS the diff. No separate
   bookkeeping step, nothing to remember.
3. **Request-changes comments become rulings.** The agent applies
   them, pushes, and the thread is the audit trail.
4. **One PR = one decision — enforced hard.** Small, single-topic
   diffs the author can judge from a phone in under two minutes.
   An OUTLINE PR approves the outline as drafted, nothing else;
   every open ruling inside it ships as its OWN DECISION PR whose
   diff is just that ruling. Bundling is a process bug the author
   answers with "split this." (Evidence: PR #1, 2026-08-02 —
   an outline approval bundled five rulings and the author couldn't
   tell what they were approving.)
5. **Show the passage — the BOOK's lines, not just rule text.** If a
   decision touches prose — a line, a beat, a scene — the PR body
   QUOTES the affected manuscript lines, so the author decides from
   the body alone without opening a diff. This applies to RULE PRs
   too: a rule change quotes both the rule AND the book passage(s) it
   governs (author, 2026-08-02 — the wink-accounting PR quoted the
   rule but never showed the ch9 lines it would cut; that was
   malformed). AUTHOR-INPUT PRs include the stub plus the paragraphs
   around it. A body must be decidable in under a minute; options are
   one-liners. If the author has to go find the context, the PR is
   malformed.
6. **If it's the author's action, it's a PR** (author, 2026-08-02).
   Anything assigned to the author — a read, a listen, a passage to
   write, a decision — exists as a PR, never only as a chat message
   or a mental note. The open-PR queue IS the author's to-do list.
   Reading/writing tasks ship as the PR whose merge concludes them
   (an adoption read IS the adoption PR, with the reading copy and
   audio linked in the body), so finishing the task and recording
   the outcome stay one motion.
   **Corollary (author, 2026-08-05): a decision parked in a note,
   TODO, or "open questions" list is QUEUE DEBT, not a decision
   channel.** Instrument reports and sketches may surface questions,
   but every genuine author decision they raise must be extracted
   into its own bite-size PR — sequenced under the 5–7 budget, most
   load-bearing first — by whoever filed the report (or the
   showrunner on its next shift). Notes carry the evidence; PRs
   carry the decisions.

## The PR taxonomy — ten types

Title format, for instant triage:

    [<book>][<TYPE>] <what is being asked, in one line>

e.g. `[spytwins][OUTLINE] Book 2 Japan — 12 chapters, 2 flags`
     `[romance-a][RULE] waive cameo budget — City A finale needs 3`

| Type | The agent is asking you to… | Typical size |
|---|---|---|
| **PREMISE** | approve a book's shape: the one-paragraph overview / locked premise (Q1–Q4 + banked ingredients) | 2 min |
| **OUTLINE** | approve the chapter-by-chapter (1–2 sentences per chapter) + its audits, before drafting starts | 5–10 min |
| **CANON** | ratify new canon a draft established, or rule on a canon conflict a keeper found | 1–2 min |
| **RULE** | approve bending a warning — the diff contains the `WAIVED:` line; or rule on a wall collision (those block until you rule) | 1 min |
| **DECISION** | settle an open `[TK]` that now blocks work — names, lineage questions, arc choices; options A/B/C with a recommendation | 1–2 min |
| **AUTHOR-INPUT** | write or voice something only you can: a voice-defining passage, a personal anecdote, a lesson's wording. The PR contains a marked stub and the surrounding context | your call |
| **ADOPTION** | accept a draft as canon — the big gate. The diff updates manuscript + CHANGELOG + THREADS + ledger together | the author read |
| **SERIES** | change the machine of a series: engine rules, S-threads, SUPERCONCEPTS locks, arc structure | 5 min |
| **RELEASE** | approve anything outward-facing: covers, pricing, launch dates, blurbs, the 4-book gate | varies |
| **AGENTS** | approve changes to the studio itself: agent versions, decks, personas, this workflow | 2 min |

**Body template (all types):**

    Type: <TYPE>          Blocked work: <what waits on this>
    Ask: <one sentence>
    Passage: <the quoted lines this decision touches, when prose is
             involved — the author decides from the body alone>
    Context: <max 3 lines>
    Options: A (recommended, applied in this diff) / B / C — one line each
    Deadline pressure: <none | date + why>

## Triage rules for the author

- **RULE and DECISION first** — they block running work.
- **ADOPTION and AUTHOR-INPUT are scheduled, not triaged** — they
  need your reading/writing time; everything else fits between
  meetings.
- Anything mis-typed or bundled: request changes with one line
  ("split this"); don't untangle it yourself.
- Silence is not approval. Unmerged PRs wait; agents route around
  blocked work to other books rather than assuming.

## Per-series criteria

### Spytwins (`[spytwins]`)

- **PREMISE:** Q1–Q4 + banked ingredients, audited against the
  19-ingredient checklist; crossover cadence position; one S10 nudge.
- **OUTLINE:** Hauge map present; fair-play clue table complete; full
  ingredient audit (ABSENT items carry a WAIVED proposal or a fix);
  wink budget stated.
- **CANON:** locked names/props (who owns the tablet); ledger honest
  cells; anything a draft established beyond the bible.
- **RULE:** the usual warnings — wink floor, nudge count, gag
  touches, crossover cadence. Walls (age band, fair play, twins earn
  the win, safety rails) are never waivable — a wall collision PR is
  a redesign proposal, not a waiver.
- **DECISION:** open [TK]s — Andrew's fears, Amanda's desires, the
  B1 lineage-style questions.
- **ADOPTION:** the B1 twelve-chapter adoption pass is the standing
  example — one PR, four files, your read is the review.
- **RELEASE:** KU-velocity gates — the 4-book gate, launch dates,
  covers, pricing, read-through tripwire responses.

### Romance city quartets (`[romance-<city>]`)

- **PREMISE:** city + season map (which couple gets which season);
  the bench of 3 with wounds stated; trope rotation vs. the ledger
  (no back-to-back repeats); the relocation hand-forward named.
- **OUTLINE:** beat placement (meet / proximity / midpoint / dark
  moment / gesture) vs. the spine; heat scenes placed per the locked
  ladder; the lie seeded by established wounds (fair-play check);
  matchmaker touch = exactly one, deniable; the featured
  show-of-the-book named (invented titles only).
- **CANON:** the past-couples registry (marriages, babies — romance
  readers are the fiercest continuity-keepers alive); container
  geography; matchmaker thread facts.
- **RULE:** waivable — cameo counts, gag touches, seed timing.
  NEVER waivable — the HEA, consent, the heat band.
- **DECISION:** which bench character relocates; matchmaker identity
  and reveal pacing; whether the show thread gets an S-ID.
- **AUTHOR-INPUT:** the grand gesture of each book (the emotional
  core — agents propose, you own the final beat), and any
  lesson/theme wording.
- **RELEASE:** quartet box sets; season-matched release calendar;
  City A's 4-book launch gate.

## Implementation phases

- **Phase 1 (now, no new infrastructure):** work continues in
  sessions; every author gate becomes a PR on a short-lived branch
  instead of an in-chat question. The ten types and title format
  apply immediately. The author's two consoles: the GitHub mobile
  app for 1-minute types (read the body, tap Merge), and the
  `/triage` skill in any session for the queue and for walking
  through big PRs (OUTLINE, ADOPTION) conversationally. Reading
  assignments ship with a rendered reading page and audio; the
  studio's audio voice is Kokoro "heart" (author-picked,
  2026-08-02).
- **Phase 2 (the while-you-sleep vision):** scheduled Routines run
  per-book sessions overnight (this environment already supports
  scheduled triggers and PR-activity subscriptions). Each nightly
  session: reads merged PRs for new rulings → advances its book to
  the next gate → opens the next PRs → ends. Mornings, the author
  wakes to a triage queue sorted by type. Blockers get solved over
  coffee; the team never stopped.
- **Guardrails:** agents never merge their own PRs; walls block
  regardless of PR state; one book per PR (workspace commit rule);
  PR volume is a tuned number — if the author faces more than ~5–7
  PRs a day, gates are too fine; batch DECISIONs per book.

## Why this fits

The pipeline already has gates ("leaves when…"); this gives every
gate a button. The canon-decision log already records rulings; the
PR diff writes them. The variance/roster system already tracks the
team like software; PRs are how software teams actually ask their
director for a call. Nothing about the philosophy changes — only the
latency of author involvement, which stops being "whenever the author
is in a session" and becomes "whenever the author has two minutes."

## Rule 7 — the MINOR lane (author, 2026-08-05)

The author's ruling: "create an agent that chooses to merge the minor
PRs... for those small ones I only get a daily summary so I can
revert if needed but trusting most of them." This deliberately amends
the agents-never-merge wall for ONE narrow lane:

- **Typing:** eligible PRs are opened as `[book][MINOR] ...` — the
  opener's explicit declaration. A PR not typed MINOR at creation is
  never auto-merged, full stop.
- **Eligibility (ALL must hold, verified twice — by the opener at
  creation and by the merging shift before merging):** one decision;
  recommended option applied in the diff; body quotes the book's
  lines. It touches NO manuscript prose beyond mechanical fixes of a
  few lines, NO reversal of any LOCKED canon, NO SUPERCONCEPTS, NO
  series rules, NO outline/premise/adoption/agent-charter material,
  and nothing the author has flagged in chat or VISION.md.
  Qualifying examples: tertiary-character micro-facts, era-idiom
  swaps, geography micro-details, institution-name picks,
  bookkeeping folds. When in doubt, it is not minor — leaving it for
  the author costs one click; a wrong merge costs trust.
- **Who merges:** the nightly showrunner shift, as its own checklist
  step — so every MINOR PR naturally sits in the queue most of a day
  first, and the author can always beat the bot to it.
- **The daily summary:** the morning nudge carries a "MERGED FOR
  YOU" section — one line per auto-merge, PR number and the decision
  taken. Revert protocol: the author says "revert #N" anywhere; the
  merge commit is reverted the same day, the decision reopens as a
  fresh PR marked NOT-minor.
- **The kill switch:** the author saying "hold minors" (chat or
  VISION.md) suspends the lane until lifted; the lane also
  self-suspends for a night if any revert was requested that day.
