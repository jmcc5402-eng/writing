# Agent Changelog

Newest first. Every entry: version, what changed, and the evidence that
drove it.

## 2026-09-21 — author-proxy 1.1.0: scored against the author's real comments — zero of seven

The experiment ran. The author's seven comments on ch 23 (#180 and
chat): none the proxy had said; four it missed (the stakes not
blatant, why they are apart, the romance level — 3 vs the panel's 6
— and the heat level); three new (funny epigraphs, the book a
downer, the wound higher). The proxy had caught nuts-and-bolts and
passed POINT. Now: romance and heat rated on the author's own anchors
(romance-levels.md rows 20, 23; heat only in a shared room); the
stakes-blatant line (what exactly happens if — quote it or say none);
the apart-why; a seventh question, FUN (L062–L064). The score file is
notes/ch23-proxy-score-2026-09-21.md; ch 24 scores it again.

## 2026-09-20 (night) — author-proxy 1.0.1: the two big questions first; showrunner 2.4.5: one open PR at a time

The author on the proxy's first run: "all of those examples are
fixes about continuity and very nuts and bolts errors. My main
comments have been about things like 'are we making enough conflict
with X character' or 'are we feeling enough romance from this
scene.'" The proxy's read of ch 23 B had three of eight comments in
those shapes and the orchestrator led with the other five. Now: MORE
and WHO-conflict first and at least half; the counts line rates
romance felt per scene (1–10) and conflict per top character (0–3)
(L060). And the showrunner: one open PR at a time, the branch
freezes, no side branches (L061).

## 2026-09-20 (night) — romance-reader-panel 1.6.5: blind means blind

The ch 23 panel on candidate B: "the card's Targets line is inside
the card file and I saw it before I could skip." A reader cannot
un-see a line. `card-blind.py` writes the card with the Targets block
struck; a blind read is launched on that copy (L059).

## 2026-09-20 (night) — author-proxy 1.0.0 (new); instrument-auditor 1.1.0; THE AUTHOR'S READ on every brief

The author: "I'm still having to give lots of comments every chapter…
make tools or hooks or skills to implement my style of comments
before the chapter is written." The study of thirty-five comments
(`audits/2026-09-20-author-comment-study.md`) found six shapes and
that nobody in the room reads as the author. Three instruments:
`studio/AUTHOR-QUESTIONS.md` — the six questions in the author's
words — answered per scene on every brief from ch 23 (THE AUTHOR'S
READ; brief-gate refuses a drafter without it; `/author-read` drafts
it; L056). `author-proxy` 1.0.0 — a new agent whose only brief is the
author's comments verbatim; it reads the draft before the panel and
writes the comments the author would; its TESTS line carries the six
tokens and the accept gate requires its file from ch 23 (L057); every
real comment afterwards is scored SAID / MISSED / NEW against it.
`instrument-auditor` 1.1.0 — a standing pass reading RECENT's bans and
caps against the taste sheet, after the August body cap produced the
one-line cab (L058). PIPELINE's chapter line carries the new stage.

## 2026-09-20 (night) — drafting-assistant 1.7.2, romance-reader-panel 1.6.4: the touch is a scene, not a sentence

The author, rereading ch 21's cab: "we just have one line that her arm
goes warm… a key moment of love mixed with awkwardness." The panel's
TOUCH test had passed the cab on that one line — the test asked for
a body sentence and got one. It now counts the body sentences at the
chapter's highest touch and quotes the confusion said plain; three
or fewer is a finding (L054). The drafter's rule 9 says the same.
The cause was an instrument: RECENT's August scrub ban "one
involuntary-body beat per chapter max" rode in every campus brief
and told the drafter to write one line. Narrowed to outside touch
scenes (L055); chapter-lint TOUCH SPAN counts the body sentences
around each touch so the next one-line cab shows up before a reader.

## 2026-09-20 (night) — continuity-keeper 1.4.4: the clock between scenes, standing

The author, rereading ch 21: "a confusing timeline when Aisha and the
trainer decide not to drive, then it's confusing exactly when Dan
comes to pick them up." The keeper's E4 card ("watch transitions") had
caught exactly this on the ch 21 card and brief audit — and the page
audit drew E1 and did not look. A transition check that depends on a
card draw is an instruction. Now standing in the remit (AUTHOR-NOTES
233; L053).

## 2026-09-20 (night) — the pull: drafting-assistant 1.7.1, romance-reader-panel 1.6.3

The author, rereading ch 21: "She seems like a zombie… For the top
4–6 characters we need to weave in this level of conflict throughout
the book" (AUTHOR-NOTES 232; B2-D29). A stake was half the sheet; the
PULL (two wants against each other) is the other half, on the page
every time the character appears. `canon/STAKES.md` "The pull"
(Missy locked; five proposed); drafter rule 9 amended; the panel's
STANCE test asks whether the pull showed or the character was a
zombie; bans.txt L050 — the flat-face shapes, with the pages'
exhibits as fixtures.

## 2026-09-20 (evening) — the author's ch 22 comments (#179): romance-reader-panel 1.6.2; the pronoun count

Three comments (AUTHOR-NOTES 228–231; B2-D28): "he" for two men in
one paragraph; Dan's stake (a second time ends him) told to the
reader; Sonny returning unintroduced; the porch conversations flat
because the reader was not told whether to like or hate Denny and
Boyd; the letter small and the trustees' agenda unexplained.
- **romance-reader-panel 1.6.1 → 1.6.2:** THE STANCE test asks two
  more things — like or hate now, and why; would a reader who skipped
  a week know who this is.
- `chapter-lint.sh`: PRONOUN CROWDING (L045). FACTS F-DAN-01,
  F-AGD-01. `canon/STAKES.md`: Dan's locked row and "How the reader
  is meant to read them now."

## 2026-09-20 — the lesson loop; romance-reader-panel 1.6.1 (the TESTS line; the stance test asks what they stand to lose)

The author: "every bug does two things: fix the bug, and fix the
environment guardrails… in this new paradigm where we use skills,
hooks, in addition to md files." Built: `studio/lessons/` (the ledger,
the bans as data with fixtures, the reader tests), `bans.py` (the
guards read the data; `--test` proves every ban fires),
`lesson-check.py` (every catch has an enforcer; runs in guardrails and
on every [FOLD] PR), the `/lesson` skill. `prose-guard.sh` and
`chapter-lint.sh` now read `bans.txt` instead of a hardcoded list —
its first run caught a place-stamp on ch 21 three readers had missed.
- **romance-reader-panel 1.6.0 → 1.6.1:** the verdict ends with a
  `TESTS:` line the accept gate reads (from ch 22); THE STANCE test
  now asks what each named character stands to LOSE and whether anyone
  reads as a type (taste 22, the author's Clavell direction:
  `canon/STAKES.md`).
- `brief-gate.py`: from ch 22 a chapter brief carries STAKES ON THE
  PAGE (L031).

## 2026-09-20 — the author's ch 21 comments (#177): drafting-assistant 1.7.0, romance-reader-panel 1.6.0

Seven comments on the merged chapter, every one a miss the readers
had not caught (AUTHOR-NOTES 216–222; B2-D26). The hand in Verna's lot
had nine sentences of approach and no sentence of what the touch did
to her body; Missy had been on twenty-one pages with no stated want;
the storm was told through its consequences; the last section was
arithmetic with no ache; and the house had a tic the author named —
"I wanted to say it in this truck" / "it's been said where you were"
— nine times on accepted pages.
- **drafting-assistant 1.6.1 → 1.7.0:** rule 9 — the touch has a
  body; the others have wants; the weather is weather; nobody says
  where a thing was said.
- **romance-reader-panel 1.5.6 → 1.6.0:** three tests — THE TOUCH
  (quote the body's reaction at every touch), THE STANCE (what each
  minor character wants, one line), THE ACHE (the romance side of any
  apart section). All three ran blind on ch 21 and none of them
  existed; the panel scored the chapter 7 three times.
- STYLE: "The touch has a body"; "Nobody says where a thing was
  said." AUTHOR-TASTE 20, 21; 17 and 19 amended. RECENT: the
  place-stamped-speech ban.

## 2026-09-17 — the targets gate: romance-reader-panel 1.5.6 (the ACTUALS line); card-lint, accept-gate, targets-check.py

The author: "choose the rank of the romance before the chapter's
written, giving us a definition of done." The card gets a Targets line
(seven values: romance, heat, laughs, ends, talk, words, pays), set
before the draft; the card lint refuses a card without it; the panel
ends its verdict with a machine-read ACTUALS line; `targets-check.py`
compares them at the accept gate and holds a chapter whose romance
level is two or more under target, and records the pair in the book's
`notes/targets.md`. From ch 21. Evidence: ch 20 counted twenty beats
and read as a 3; nothing had asked for a number beforehand.

## 2026-09-17 — romance-reader-panel 1.5.5: the romance level, 1–10 (minor)

After the count, a ROMANCE LEVEL on the reader's scale, one sentence
why, and the two-point fix. Evidence: ch 20 — the count said twenty
beats, all nine kinds, above the floor; the author said "two or three
out of 10 … read like a normal old book"; the panel, asked blind for a
level, said 3. The count and the level now travel together, and the
author's number goes beside them in `notes/romance-levels.md`.

## 2026-09-17 — two gates: the card lint and the brief gate (hooks, not rules)

`studio/tools/card-lint.py` (PreToolUse on SendUserFile) and
`studio/tools/brief-gate.py` (PreToolUse on Agent). The first blocks a
chapter card that is over 350 words, has a sentence of 30 words, a
call in two sentences, a missing section, a ledger word, or a marker.
The second blocks a drafting-assistant launched on a brief that has no
AUDIT ADDENDUM with a VERDICT on disk. Evidence: taste 13's repeats
(the card) and BACKLOG F36 (the ch 18 stray-file brief). Author,
2026-09-17: "Ok 1 and 2 now." Drafter rule 8 and the showrunner's card
rules stay as written; the hooks are what make them hold.

## 2026-09-13 — drafting-assistant 1.6.1: no addendum, no draft (patch)

Rule 8: a brief without its AUDIT ADDENDUM is not a brief; the drafter
stops and says so. Evidence: the ch 18 v2 competition — the audited
brief was written to a stray file by the orchestrator; two drafters
worked from the unaudited copy; the third checked. BACKLOG F36.

## 2026-09-13 — drafting-assistant 1.6.0, romance-reader-panel 1.5.4: say it plain (the author's #161 read of 1.2 ch 18)

Evidence: eight comments on #161 — "paras that almost read like a
weird poem"; "trying too hard to make this into some glorious
mystery… It's just a romance novel"; "I honestly don't understand
what they're talking about… too implicit"; "we need to explain why
they're not together more"; "Dan is still kind of a mystery." The
panel (1.5.3) passed the chapter with fixes and caught none of it.
- **drafting-assistant 1.6.0** — rule 7: sentences end (under thirty
  words, at most three "and"s, no one-sentence paragraphs); a plot
  object weighs what the plot has made it weigh; jokes understood on
  the page; apart has a reason; the SENTENCES count run before
  delivery.
- **romance-reader-panel 1.5.4** — the POEM test, the MYSTERY test,
  THE JOKE, and APART, WHY, reported under the verdict every run.
- **Law:** STYLE "It's just a romance novel — say it plain" (a–d);
  taste 18; the chapter lint's SENTENCES section (over thirty words;
  more than three "and"s). BACKLOG F34 (the panel's miss) and F35 (the
  chapter built on an object the plot had not made heavy — the card
  and brief did it, and the audit passed them).

## 2026-09-12 — THE BACKLOG PR: second audit F18–F30 and the first audit's unlanded items

Evidence: `studio/agents/audits/2026-09-10-instrument-audit.md` and
`2026-09-07-instrument-audit.md`; the author's catches at #156, #158
and in chat (the weather; the seeds). Landed:
- **DRAFTING-PROTOCOL:** THE LEADS' SCENES replaces the four brief
  slots with a word FLOOR (F18); "one line" and "texture, one line"
  banned for anything between the leads (F27); THE STAKES cited, not
  restated (F23); FURNITURE, CITED (F24); the manifest is nouns with
  cites, never a voice sample (F4); the review stack conformed to
  PIPELINE — developmental → line → continuity last (F13); the
  PROPOSED header retired (F28).
- **romance-reader-panel 1.5.3:** duration numbers per leads' scene
  (words, narration per dialogue line, reaction beats) in the verdict;
  the swoon inventory protects at most one short line per scene (F19);
  TASTE goes down the whole numbered sheet (F9).
- **continuity-keeper 1.4.3:** the build check is run by the
  orchestrator and pasted (F8); the brief's OPENING / ARGUMENT /
  REVERSAL read against the manifest, the taste sheet read first
  (F9); the registry's COUPLES rows read before any couple line
  (F32).
- **showrunner 2.4.4:** survey runs exempt; an audit or fold done in
  the showrunner's hands draws that agent's deck card (F16).
- **instrument-auditor 1.0.1:** listed under the editor deck; every
  later run builds its test set from the author's catches since the
  last audit (F28).
- **DECKS:** D7 retired (F15/F26); rules renumbered; the auditor on
  the editor deck (F28). **RECENT:** wave text gone; briefs point here
  as of a date (F10); the duplicated establishing-line law is a
  pointer; the "which"-appendix watch discharged; the since-June watch
  kept as a lint count (F29).
- **PIPELINE:** the fold checklist with an owner, nine lines including
  the page against the card (F25, F31); length ~2,800–3,500 and the
  quiet band 8–15% (F26); the outline gate runs the engine checklist
  (F30); the arc gate checks the dossiers' pre-page history (F33);
  Current state carries campus (F28).
- **Tools:** `opening-check.py` prints the seams and checks every
  section's opening (F3/F14/F23); `romance-build-check.py` warns
  UNEARNED STAGE on any In/Out increment with no Earned-by (F7; rows
  11/13/16 of the 1.2 ladder filled); the chapter lint's simile
  scaffold regex narrowed (F6/F29) and a per-chapter REPETITION scan
  added (F5).
- **Kit:** 06's ingredient audit named as the outline gate and the
  `/new-book-outline` skill runs it (F30); 11's parts renumbered
  (F16). **CLAUDE.md:** fifteen specialists; the three missing rows
  (F16/F28). **AUTHOR-TASTE:** the footer moved to the end (F28).
  **1.2 registry:** a COUPLES section (F32). **STATE:** "panel 1.3.0"
  retired (F28).
Not landed, left on the backlog: F21 (the fold logs panel grafts —
remit lines only), F22 (backstory that copies the plot — the
developmental editor's Hauge item), F28's "AUTHOR-TASTE entry 8's
duplicate block" (not found on re-read), the undated agents CHANGELOG
entry (not found), and the roster-level items from July.

## 2026-09-12 — continuity-keeper 1.4.2: the card is canon for its chapter (patch)

Rule 6: a brief or a draft is read against the chapter's card; a
contradiction of a card promise is a BLOCK, quoted side by side.
Evidence: 1.2 ch 17 — the card promised the chart sent unasked; the
brief had the release arrive first and her send after; the audit
passed the brief; the author caught it on the page (#158: "I thought
earlier we said Aisha sent them on her own? Something seems weird
with the timing"). BACKLOG F31.

## 2026-09-09 — showrunner 2.4.1: no coined names (patch)

Author, 2026-09-09, after a PR titled "The handful" needed
explaining: "Ha ok. Remember don't be so clever!" One line added to
"How you talk to the author": name the work by what it does to the
book, never by a phrase the author would have to ask about. Taste
entry 13 amended.

## 2026-09-08 — romance-reader-panel 1.4.0: the beer test

Author, 2026-09-08 (#147 comment on campus 1.2 ch 13): "I think we
need to go back and make both of our lead characters more likable,
we need our readers to be rooting for them." The panel now answers,
per lead per chapter, whether the reader would have a beer with
them, with the line where the lead did something for someone else at
a cost, or NONE. A chapter can pass the romance floor and fail the
beer test. Paired with the ROOTING FOR line in every brief and card
(DRAFTING-PROTOCOL; kit 12) and taste entry 15.

## 2026-09-07 — instrument-auditor 1.0.0: the audit of the instruments

Author, 2026-09-07, after catching that campus 1.2 ch 10–12 opened on
the same calendar recital (one stake sentence in all three, word for
word — a rule that said "state the day and the stake" had become a
template, and no instrument noticed): "Thinking for the long-term,
let's add some type of agent that scanned all of our agents for
potential mistakes like this one. Maybe it only runs every few
chapters." New agent: runs after every fourth accepted chapter with
the cross-batch canon sweep, or on demand after an author catch.
Seven passes — MISS, CONVERGENCE, DRIFT, CONTRADICTION, LEDGER,
BLIND SPOT, OVER-TOOLING — and a classified report in
`studio/agents/audits/`. Judges instruments, never prose; proposes,
never edits. Ships with a four-item test set from the day it was
born (the calendar opening; the one-drafter drift; the FirstDownMom
ghost; the ch 11 edge miscount).

## 2026-09-07 — showrunner 2.4.0: set pieces get a competition; connecting chapters get one drafter

Author, 2026-09-07, on "the idea that we had 3 drafters write each
chapter and then compete": the showrunner reported the drift
(chapters 9–12 of campus 1.2 ran one drafter each under the
single-chapter cadence, against the conveyor's default of three) and
recommended a selective rule — competition for the set pieces (the
first heat scene, the kiss, the game, the antagonist's price, the
hearing, any register pilot), one drafter for connecting chapters,
the panel judging blind, the author reading only the winner, no
grafting by default. Author: "yes i like that." Written into
DRAFTING-PROTOCOL ("The conveyor," item 5), PIPELINE §3c, and the
showrunner's duties (the brief names SET PIECE or CONNECTING; the
scoreboard; the one-line "which won and why" in the PR). First run:
campus 1.2 ch 13.

## 2026-09-06 — showrunner 2.3.0: the chapter card before every chapter read

Author, 2026-09-06: "For each new chapter I would like a very
concise overview of where we are in the plot (plot arc), same for
character arcs for both leads, and a same for romance arc." Then:
"Yes this was great. Make this a standing review before each chapter
read." The showrunner writes the card from the arc docs, the outline
and THREADS before any chapter PR opens; it is the top of the PR
body and, via the new `studio/tools/listening-file.py` (the scratch
generator promoted to a tool), the top of the listening file. Kit
template 12; PIPELINE §3c; PR-WORKFLOW rule 10.

## 2026-09-06 — romance-reader-panel 1.3.0: every scene, and the apart test

Author, 2026-09-06, returning ch 9 of Book 1.2 after the panel
passed it with six beats, four kinds, and both edge thirds covered:
"She doesn't think about Dan the entire chapter and then just says
to herself that she wants him. Too abrupt. This book seems to have
none of the romance vibe of book one. There's nothing woven in to
the various scenes." The count measured thirds; the author reads
scenes. The panel now goes scene by scene after the count and says
where the other lead is in each and whether the reader feels him or
is told about him; an apart chapter gets the apart test first.
STYLE's "Romance first" gained "Woven, not counted"; the protocol's
ROMANCE BEATS line asks one beat per scene. BACKLOG item opened
against the floor's check (a passing count is not a passing
chapter).

: plot-architect 1.5.0, developmental-editor 1.5.0, continuity-keeper 1.4.0

Author, 2026-09-05, after ch 8 of Book 1.2 passed the romance count
with thirteen beats and still felt abrupt: "we need one [arc] for
the romance overall to show how early on the romance is hidden and
just shows some signs of life, but over the book it grows and turns
external." Then: "I want this to be another instrument we use so
eventually we can build these books really fast." The finding: the
arc gate (§3b, 2026-09-03) existed in PIPELINE and nowhere else — no
kit template, no tool, no agent whose job it was. Now:
`series-kit/11-arc-docs.md` is the template (the leads' arcs and the
relationship's arc with a ladder table); `tools/romance-build-check.py`
reads the ladder and fails an unearned want, kiss, or claim, an
inside more than one stage ahead, or a stage that jumps or reverses
(it fails Book 1.2 as the page stands, at ch 8, for the author's
reason; it passes with the ch 2 add). plot-architect writes the
three docs after every outline and runs the check; the developmental
editor names the scenes that earn a spend; the continuity-keeper's
brief audit runs the tool and blocks on FAIL.

## 2026-09-05 — showrunner 2.2.1: talk to the author like an author

Author, 2026-09-05, on a PR summary: "this blurb by you is too
complicated for me (or any human) to understand… keep things simple
and step by step like an author might talk, not like these are the
plans to a complex satellite." The offending paragraph stacked three
studio terms and a dependency into one sentence. Patch bump: the
showrunner's messages, PR bodies and comments pass the say-it test —
plain words, one idea per sentence, steps in order, the book's
meaning instead of the studio's names. Taste-sheet entry 13 carries
it for every agent that writes to the author.

## 2026-09-04 — Romance first: drafting-assistant 1.5.0, romance-reader-panel 1.2.0, and the campus drafter persona

Author, 2026-09-04: "I think the writers don't understand
fundamentally that this is a romance novel. They are writing great
plots… the reader here doesn't care about the plot, they care about
the feeling of romance… every chapter has to have multiple romance
aspects to it. They can be tiny, but they need to be. That should be
a fundamental wall." Then, shown the wall: "Rule not wall. It's like
I have to work to convince the writers to include romance where it
should be a core fundamental piece." The finding that answers that:
the campus drafter had no persona — Spytwins, MYBYB and Young
Nicholas each had one; the romance did not — so nothing ever told
the drafter what book it was writing. `personas/drafter-campus.md`
is new and is the first thing every campus brief hands the drafter.
Evidence for the count: 1.2 ch 5–8 as first shipped carried
one romance beat a chapter against a full plot; every instrument
added this week (reversal, arc beat, stakes, the ladder) counts plot
mechanics or one proximity beat. The rule (studio/STYLE.md; campus
STANDARDS 26) requires three beats of two kinds per chapter, first
and last third. The drafter's brief now opens with THE ROMANCE MOVE
and the drafter reports each beat by line; the panel inventories the
beats blind and its count stands — a chapter under the floor goes
back to the drafter before any other finding is weighed.

## 2026-09-04 — the author's taste sheet wired into five agents

drafting-assistant 1.4.0 · developmental-editor 1.4.0 ·
red-team-critic 1.2.0 · romance-reader-panel 1.1.0 · showrunner 2.2.0.

Author directive (chat, 2026-09-04): "I want to set up a system where
my comments are regularly reviewed by the agents as another mechanism
to avoid pitfalls that I don't like." Evidence that the gap was real:
the author's 2026-09-03 PR #107 comment ("there needs to be some
interaction between Dan and Aisha… too completely separate
characters") was not converted to a rule until the author repeated it
on 2026-09-04; "too 70s country" (2026-08-18) came back as "campy 80s
country" (2026-09-03). Comments lived on GitHub and in listen notes
nobody re-read. Now: `studio/AUTHOR-NOTES.md` (the verbatim ledger,
backfilled from every PR comment and 208 recorded rulings) and
`studio/AUTHOR-TASTE.md` (twelve standing entries in the author's
words, each with its check). Drafters read the sheet before writing;
panels and editors end every run with a TASTE finding; the red team
runs the taste audit every fourth accepted chapter; the showrunner
feeds the ledger at every fold and re-mines after every listen. New
capability = minor bump for each.

## 2026-08-19 — superfan-reviewer 1.0.0 (new): the review section, predicted

Author request (chat, 2026-08-19, campus thread): "the annoying fan
who is obsessed with the comments in Amazon... the
anti-professional-critic who represents the common folk reader."
Gap confirmed against the roster: romance-reader-panel measures the
experience DURING the read; nothing predicted the public conversation
AFTER it — star math, pet-peeve triggers, promise-vs-page mismatches,
the "I wanted to love this" three-star. New agent owns that remit,
runs after panels / before author acceptance, and doubles as the
enforcement instrument for the metadata bright line (R9). Added to
the critic variance deck.

## 2026-08-13 — romance-reader-panel 1.0.0 (new): the audience gate the adult books never had

Author ruling (`books/campus-series/notes/author-register-note-2026-08-13.md`,
directive 6): "the instruments must reward fun and swoon, not only
structure."

**Evidence.** The author read the winning campus 1.1 outline — a
tournament winner scored against SUPERCONCEPTS and cleared by every
gate in DRAFTING-PROTOCOL — and returned "this reads more like a real
estate attorney novel… my read of the outline is that this is a
serious book about a construction issue."

**Root cause** (`studio/agents/notes/romance-register-tuning-2026-08-13.md`),
and it is worse than an omission on two counts:

1. The only reader-simulation instrument in the battery
   (PIPELINE stage 5 step 2, DRAFTING-PROTOCOL gate 4) is hard-coded
   to `kid-reader-panel`. For the adult books the audience gate did
   not run weakly — it did not run at all. The studio understood the
   problem completely and built the instrument for two of its books.
2. The tournament rubric is four SUPERCONCEPT integrity tests, and
   SC4 rewards institutional obstacles. The outline did not sneak
   past the judges; it WON a contest scored against a rubric with no
   line for pleasure. The battery selected for machinery rather than
   merely failing to notice it.

- **`romance-reader-panel` 1.0.0 (new).** Simulates the target adult
  romance reader: engagement map, DNF point, skim ledger, wanting
  curve, swoon and fun inventories, genre contract, buy-the-next-one.
  Runs from rung 2, so the author is never the first reader to be
  bored. **No veto power** — the walls outrank its findings by
  charter, and decorative charm is itself a finding, so the
  instrument cannot be gamed with garnish.

Rejected alternative, recorded: generalize `kid-reader-panel` into an
age-parameterized `reader-panel`. Cheaper on roster size, and
genuinely tempting. Rejected because the kid panel's value is a voice
and a reading-level lens while this panel's value is genre-contract
literacy — a reader who has read four hundred of these and knows what
she is owed — and the workspace already holds that blurring
instruments together is the failure mode worth paying to avoid.

Held for the follow-on `agents:` PR, pending the author's ruling on
this roster addition: the four campus personas
(`architect-campus`, `drafter-campus`, `dev-editor-campus`,
`red-team-campus`), the version bumps they imply
(plot-architect 1.5.0, developmental-editor 1.4.0,
red-team-critic 1.2.0), DECKS rule 7 with cards A6–A10 / D8–D11 /
C7–C10 / E7–E8, and the `studio:` PR wiring the panel into
PIPELINE and DRAFTING-PROTOCOL. The wiring must land after the
charter or the pipeline names an agent that does not exist.

## 2026-08-08 — plot-architect 1.3.0 → 1.4.0 (write for a stranger)

New rule: snowflake prose is jacket copy — one-sentences and
one-paragraphs must hook a reader who has never heard of the book;
quarters read as miniature stories; technical apparatus lives in
labeled blocks below the prose. Evidence: the author on the Nick
Books 2-4 sketch (PR #26 read): "You're writing it as if I already
know the plot... the one paragraph should almost read like the back
cover... each paragraph should read almost like a short story. Right
now it almost reads like shorthand." Also recorded in
DRAFTING-PROTOCOL as a rung 1-3 standard for all generators.

## 2026-08-05 — showrunner 2.0.0 → 2.1.0 (the MINOR merge lane)

Author ruling amends the agents-never-merge wall for one narrow
lane: PRs typed `[book][MINOR]` at creation may be merged by the
nightly shift after double verification (opener declares, merger
re-verifies), reported next morning under MERGED FOR YOU with a
"revert #N" handle; any doubt disqualifies; "hold minors" or a
same-day revert suspends the lane. Full rails in PR-WORKFLOW rule 7.
Evidence: the author — "for those small ones I only get a daily
summary so I can revert if needed but trusting most of them."

## 2026-08-05 — showrunner 1.0.0 → 2.0.0 (major: remit change)

Author-directed promotion: "act as if it's a young ambitious,
well-intentioned book publisher and author... scan over all the
books... I want to feel as if these agents are the ones driving the
momentum and my job is to give the vision and steer direction."
Changes: (1) scope widens from Spytwins to ALL books; (2) persona =
ambitious publisher-author with a momentum mandate — every book moves
one increment per shift or the report names the exact gate; (3) two
lenses per book (publisher's eye = path to market; author's eye =
weakest craft point + which instrument exposes it); (4) empowered to
dispatch the DRAFTING-PROTOCOL instrument battery, incl. tournaments
on OPEN decisions only; (5) reads studio/VISION.md (new — the
author's steering doc) first, every run; (6) morning nudge gains "at
most ONE steering question." Walls unchanged: never writes prose,
never decides canon, never merges; nightly budgets 3 jobs + 2 PRs,
saturation cap 5. The nightly Routine's prompt was updated to match.

## 2026-08-04 — drafting-assistant 1.2.0 → 1.3.0, line-copy-editor 1.2.0 → 1.3.0

New shared rule: **no paragraph ends in a colon or a dash**, plus a
mandatory mechanical sweep (`studio/STYLE.md`, "AI drafting tics") —
drafting-assistant runs it before delivering (rule 6); line-copy-editor
treats it as a COPY EDIT-mode mechanical check and reports
zero-or-explained. Evidence: on the B1 adoption read the author caught
six dangling colons and six dangling dashes across twelve chapters
("weird colons," "weird long dashes") that no editorial pass had
flagged — the dangling-reveal cadence is an AI tic that self-copies
through voice-matching, so prevention has to be mechanical, not
stylistic judgment.

## 2026-08-04 — plot-architect 1.2.0 → 1.3.0

Outlines now include a LOCATION ROSTER — every recurring setting
named, one-line identity, relative positions; <5 recurring (2–3
best), single-visit sites named but uncounted, no confusable names.
Evidence: the author, mid-adoption-read, confused the B1 cultural
center with the one-mention community center and with a "museum"
narration alias; the fix cost three edits post-draft that a roster
would have prevented at outline time.

## 2026-08-03 — continuity-keeper 1.2.0 → 1.3.0

New standing check: scene staging — where each scene is and whether
every movement inside it obeys the page (teleports, scene-interior
drift, who's-present drift, in-scene object staging). Evidence: the
author, listening to B1 ch3–4 audio, sensed an unmarked beach→
petroglyph-rocks jump and asked "do we have checks on setting,
specifically within a scene?" — the remit covered cross-chapter
geography but not scene-interior staging. First production run: the
2026-08-03 B1 staging sweep (card E3).

## 2026-07-30 — showrunner 1.0.0 (new)

Author-requested: a proactive lead-writer/program-manager agent that
surveys every book and recommends/kicks off the next job. Fills the
vacancy the 2026-07-30 artifact study documented: the acceptance/
kickoff step was the only pipeline stage with no owning agent, and
the stale STATUS.md proved stored status boards rot — so the
showrunner's first rule is compute-state-from-files, store nothing.
Remit boundaries: ranks and preps (briefs for dispatchable jobs,
typed PR specs for author gates per PR-WORKFLOW.md); never writes
prose, never decides canon, never merges. Variance-EXEMPT by design:
scheduling judgment must be stable run-to-run; a lens card would
churn priorities between mornings. Ties rotate deterministically
(release-train date, then alphabetical). Phase 2 slot: the nightly
Routine driver.

## 2026-07-30 — /triage skill 1.0.0 (new)

Author-requested, implementing `studio/PR-WORKFLOW.md` (the author-as-
engineering-director model): a session-side console for the PR queue.
Lists open PRs sorted by type priority (RULE/DECISION first; ADOPTION/
AUTHOR-INPUT labeled schedule-don't-squeeze), walks through any PR
conversationally, merges or posts rulings only on explicit per-PR
instruction. Guardrails: never merge own work, walls never waived in
triage, one book per PR. Companion to the GitHub mobile app, which
remains the recommended path for the 1-minute PR types.

## 2026-07-28 — gtm-strategist 1.0.0 (new)

Author-requested: a business-focused agent for go-to-market analysis —
channel economics (KDP/Kindle, print, audio), trad-vs-self decisions,
author-platform strategy, sequencing. Boundary set at creation to avoid
remit overlap: market-pitch-agent makes the selling materials;
gtm-strategist decides the machine they're used in. Realism rules baked
in: labeled claim types (verified/estimate/author-data-needed), median
outcomes not survivor stories, kids-market gatekeeper reality (COPPA),
per-book strategies never averaged, every recommendation costed in
hours-per-week.

## 2026-07-28 — the Hauge frame (three agents, minor bumps)

Author-stated preference: Michael Hauge's framework (six stages, five
timed turning points, the identity→essence inner journey braided with
the outer goal, and the four devices — foreshadowing, echoing, superior
position, ticking clock). Distilled to `studio/craft/hauge.md`; agents
cite the file rather than carrying the framework.

- **plot-architect 1.1.0 → 1.2.0.** Outlines now name both journeys
  before beats exist and pin the turning points to their positions.
- **developmental-editor 1.2.0 → 1.3.0.** New audit: journey braid,
  turning-point depth, superior-position inventory, orphaned echoes.
- **drafting-assistant 1.1.0 → 1.2.0.** Scene-level rule: internal state
  rides in external action; superior-position beats and echoes are
  placed effects.

Evidence the frame fits: the studio was already running half of it
unnamed — S01 (the spy wink) is superior position as a series engine,
the knowledge-thread type in THREADS.md tracks it, the blessing-ceremony
day ledger is a ticking clock, and OWED markers are foreshadowing
discipline. Echoing and the timed inner/outer braid are the new imports.

## 2026-07-27 — the variance system (all agents, minor bump)

All ten agents gain a standing Variance section: a run may hand them one
card from `variance/DECKS.md` (emphasis only — never overrides canon, remit,
or output format) and a banned-moves list from `variance/RECENT.md`.
Versions: the seven 1.0.0 agents → 1.1.0; the three 1.1.0 agents → 1.2.0.

Evidence: repeated fixed-prompt runs converge — the 2026-07-26 reviews
caught a drafter simile scaffold used 24 times, four trailer-voice chapter
endings, and critique structures repeating across books. Design principle:
vary the lens, never the law. `RECENT.md` seeded with the caught tics;
selection is least-recently-used and logged, not random, so rotation is
enforced and card → quality effects stay observable.

## 2026-07-26 — junior-literary-critic 1.0.0 (new)

Promoted from an ad-hoc session prompt to a tracked agent after five
production runs (three initial book critiques, the Young Nicholas
manuscript re-read, and the post-rewrite reviews of all three books).
Distinctives worth preserving: verdict up front, every claim cites the
page, classifies findings, two-part output (critique + prioritized
recommendations), and it verifies its own quotations before returning.

## 2026-07-26 — the merge (workspace consolidation)

- **developmental-editor 1.0.0 → 1.1.0.** Merged the Spytwins version with
  the workspace variant: opens by naming the shape it found, scene-function
  and POV checks added, and an explicit non-fiction mode (thesis for plot,
  chapter spine for structure) because MYBYB is adult non-fiction and the
  original assumed middle grade.
- **continuity-keeper 1.0.0 → 1.1.0.** Absorbed `continuity-checker`
  (retired). Added the three-way finding classification (contradiction /
  unestablished / deliberate) and separate lists for new canon established
  and open `[TK]`/`[CHECK]` markers.
- **line-copy-editor 1.0.0 → 1.1.0.** Absorbed `line-editor` (retired).
  Added the line-pass checklist (filter words, rhythm, repetition,
  dialogue tags, throat-clearing) on top of the two-mode
  copy-edit/line-edit split.
- All other agents promoted unchanged at 1.0.0.

## 2026-07-25 — birth (Spytwins repo, commit 0487396)

Nine agents created as the Spytwins writers' room: plot-architect,
drafting-assistant, developmental-editor, line-copy-editor,
continuity-keeper, kid-reader-panel, red-team-critic, culture-researcher,
market-pitch-agent. Plus the /new-book-outline skill and the book-studio
plugin packaging.

## 2026-09-10 — showrunner 2.4.2: the card reads like a letter

The author, on the ch 16 card: "Remember the summaries before the
chapter need to read easily. Sometimes it reads like a list of
things." The card template (kit 12) had asked for "what has
happened, in chapter numbers," and every card since ch 9 carried a
run of beats with parenthetical chapter numbers and labeled
"Wound:" / "False belief:" lines. Kit 12 amended: the "so far" is
two or three sentences of story; chapter numbers only for what
comes next; no labels inside paragraphs; the ear test. Showrunner
2.4.2 carries the rule. The ch 16 card rewritten as the model.

## 2026-09-10 — romance-reader-panel 1.5.0: the slow beat and the awkward test

The author, on 1.2 ch 16 (#156): the kiss too fast; the annex talk
terse and not awkward enough; the cage button with no thought. The
panel 1.4.0 had passed the chapter with 28 beats and called the
one-line kiss "one line and right" — the count measured presence,
not pace. New: for every chapter with a touch, count the sentences
of approach before the highest touch (fewer than four is a finding)
and run the awkward test on every scene the leads share alone. STYLE
"Slow the good parts"; taste entry 16; two brief lines; the
ending-check now reports short-volley runs chapter-wide.

## 2026-09-10 — romance-reader-panel 1.5.1: who saw it, who thanked it

Survey 2 (developmental-editor, E4): the beer test passed ch 16
while its seen rung was thanked to her face against the card's own
wall; three chapters running ended on one lead itemizing the other's
kindness. Two columns added to the beer test; kit 12's ROOTING FOR
line now says "seen" means felt, never said to the doer's face.

## 2026-09-10 — the second instrument audit's TODAY list (F18–F29 filed; six items done)

Audit at `studio/agents/audits/2026-09-10-instrument-audit.md`. Done
today: the edge header and the quiet band conformed (F25); the
outline's "Friday" → Saturday (F25); kit 12's body freed of "by
chapter" (F27); `ending-check.py` rewritten — an echo-reply test in
place of the run-of-three (it now fires on "They were." and not on
the accepted pages' exchanges), names from the registry's name map,
per-section numbers (F20); PIPELINE §3c — the audit reads the card
and brief BEFORE the card goes to the author (F24); the panel 1.5.2
names what a line must do and never writes it, and the keeper's
addendum bans its own examples (F21); the losing candidates' banked
lines moved out of the registry to `notes/banked-lines.md` (F25).
The ch 17 brief trials the leads'-scenes FLOOR in place of the four
ceiling slots (F18). Everything else to BACKLOG.

## 2026-09-11 — showrunner 2.4.3: the card is short

The author, on the ch 17 card: "Too much to read make more concise."
Kit 12: under 350 words, questions one line each; the chat message
shorter than the card.

