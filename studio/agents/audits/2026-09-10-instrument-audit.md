# Instrument audit — 2026-09-10 (second run)

**Agent:** instrument-auditor 1.0.0, second run. **Batch under audit:**
campus 1.2 chapters 13–16 (`books/campus-series/book2/manuscript/ch13.md`
– `ch16.md`, accepted #147, #153/#154, #155, #156; ch 16 read as
accepted with its #156 recut applied). **Ledger window:**
`studio/AUTHOR-NOTES.md:87–112` (2026-09-08 through 2026-09-10) and
`studio/AUTHOR-TASTE.md` entries 13, 15, 16 and the 09-08/09-09
additions to entry 1. **Last audit:** `studio/agents/audits/
2026-09-07-instrument-audit.md` (F1–F16; F17 added to BACKLOG 09-09).

**Variance card:** E5 — dialogue mechanics pass first. Read as: start
from the instruments that judge talk — the panel, the ending check,
the brief's dialogue lines, the addendum's example sentences — and
ask why "I heard them go by the window. They were talking." / "They
were." went through a blind drafter, a panel read and the lint to the
author. Then widen.

**Read, in the definition's order:** the ledger window; ch 13–16 with
their briefs and addenda, four brief audits, nine panel reports and
one recut re-read, three scoreboards, four cards (and the first
versions of the ch 15 and 16 cards the author approved, from git),
the book CHANGELOG, THREADS, the registry, STATE; STYLE, PIPELINE,
DRAFTING-PROTOCOL, PR-WORKFLOW, AUTHOR-TASTE; the six agents named
in the task plus the drafter persona; ROSTER, CHANGELOG, BACKLOG,
DECKS, RECENT, LOG; every tool's source. **Run:** `chapter-lint.sh`
on ch 13–16 (all exit 0); `dialogue-lint.py` on ch 1–16;
`romance-build-check.py` on the arc doc (PASS, one WARN);
`ending-check.py` on the accepted pages AND on ch 16 as the author
read it (`git show 8cb518e`); a per-section dialogue-mechanics scan
(words, dialogue lines, mean words per line, longest run of ≤4-word
lines); an echo-reply scan (a ≤4-word reply whose content words all
appear in the previous line); a verbatim-sentence and shared-7-word-
run scan across ch 1–16; a count of ration words in each brief. All
paths below are under `/home/user/writing/`; `chNN` means
`books/campus-series/book2/manuscript/chNN.md`; `book2/` means
`books/campus-series/book2/`.

---

## Findings (severity-ordered)

### F18 — OVER-TOOLED + TEMPLATE (the mechanism): the brief is a ration register, and forty ceilings with no floor is what "terse" is made of

The author's three catches in three days — ch 13 "too staccato," ch 14
"too cold… a robot… too staccato," ch 16 "the kiss is too fast… much
of this seems so terse" — are one failure, and the instrument that
produced it is the brief's grammar. Count the ration words:

| brief | "once" | "one clause" | "one line" | "at most" | "never" | words |
|---|---|---|---|---|---|---|
| `book2/plots/brief-ch13.md` | 14 | 1 | 7 | 2 | 8 | 3,654 |
| `brief-ch14.md` | 24 | 8 | 5 | 1 | 16 | 4,311 |
| `brief-ch15.md` | 15 | 4 | 8 | 3 | 22 | 4,172 |
| `brief-ch16.md` | 38 | 4 | 6 | 6 | 33 | 4,291 |

Every one is a ceiling; there is not one floor for a scene the leads
share. The set-piece notes allocate words *away* from the leads:
`brief-ch16.md:371–376` "Spend two thirds on the game as the TOWN'S
night… the tailgate is a flash; the walk is three paragraphs; the
cage is one"; `brief-ch13.md:268–271` "The test is short… the motel
is short"; `brief-ch14.md:129–142` scenes 3 and 4 "(short)". The
drafters obeyed. Ch 16 as the author read it: tailgate + game + walk
= 2,088 words; the annex 721 and the cage 267. The recut she asked
for added 576 words to the annex (+80%) and 252 to the cage (+94%)
and cut nothing. Ch 13's check scene, the one she called staccato:
203 words, six dialogue lines averaging 3.8 words, a run of FIVE
lines of four words or fewer (`ch13:378–388`). And the kiss itself
was rationed by the brief, not the drafter: `brief-ch16.md:64–65`
"a kiss, if it comes, is texture at the ceiling, one line, not the
scene's point"; addendum 29 (`:170`) "one line at most" — the panel
then read the page against the brief and found the kiss "one line
and right" (`book2/notes/ch16-panel-A-2026-09-10.md:179`).

What the room did with the three catches is the second half of the
finding. Nine rules in three days, each written into four or five
files: the establishing line (09-08: STYLE:493–497; taste 1;
RECENT:26–30; DECKS:35; the ch 14 brief), WHO is named (09-09:
STYLE:498–501), the other lead's face (STYLE:502–508; DRAFTING-
PROTOCOL:345–350; taste 15), no staccato endings (STYLE:509–515;
protocol:361–365; `ending-check.py`), a disclosure has a prompt
(taste 1:92–96), and the four of "slow the good parts" (STYLE:
516–540; protocol:351–360; RECENT:86–92; panel 1.5.0; taste 16).
None retired. The brief template is now sixteen slots (DRAFTING-
PROTOCOL:300–383). The over-tooling guard — "one in, one out"
(DRAFTING-PROTOCOL:249–252) — was not applied once, and the first
audit's four retire proposals (F15) were not taken. Each new rule
adds another "once"; the drafters minimize to comply; the panel
checks compliance; the author reads the sum.

**Instrument:** the brief template (DRAFTING-PROTOCOL, "The reversal
slot and the say-it test") and the showrunner's set-piece note.
**Fix:** one slot replaces four — THE LEADS' SCENES: for every scene
the leads share, the brief gives a word FLOOR (not a ceiling) and
says the scene runs long — faces, the approach, what the POV thinks —
and the set-piece note spends the words on the leads, not the town.
Fold THE OTHER LEAD'S FACE, THE SLOW BEAT, THE ENDING THINKS and THE
LAST EXCHANGE into it (their content survives as the line's three
clauses); delete "one line" from any sentence about a touch. Why a
narrowing and not a new rule: the four slots already say what the
scene must contain; what none of them says is how long it is allowed
to be, and length is the thing the author asked for three times.

### F19 — BLIND SPOT: the panel's method rewards density and cannot see duration (the task's question 1)

The count is the headline (`romance-reader-panel.md:87–97`: "your
count stands"; a beat "may be one sentence"; the persona
`studio/agents/personas/drafter-campus.md:32` "A sentence is enough
for any of them"). So drafters write one-sentence beats, the count
climbs, and the headline is a density score: 28–30 beats in ~3,000
words (`ch16-panel-A:17, :58`), 23 in ch 15, 25 in ch 13. Nothing in
the eight parts measures how long anything lasts. The swoon
inventory is the second half of the same bias: it is a list of short
quotable units, and the panel PROTECTS them — which is how the terse
lines got past it three times:

- ch 13: the check scene's five-line volley (`ch13:378–388`) — panel
  C: "the check exchange replays ch 11… Deliberate: the ritual with
  one word changed. Keep." (`ch13-panel-C-2026-09-08.md:150`). The
  author: "too staccato."
- ch 14: the turf ending's four lines averaging 4.5 words (the
  pre-recut page, `git show f1e155b`) — panel: swoon #13 "Seven. I'll
  have it before you do." / "You'll have it before anybody."
  (`ch14-panel-2026-09-09.md:130`), and Q5 "'Dan watched his feet' is
  the right last clause" (`:191`). The author: "way too robotic… too
  staccato."
- ch 16: "They were." was in the blind candidate (`git show ce711e5`,
  candidate A :300–302); panel A's engagement map runs "287–382 LEAN
  IN. Peak at 320–348" (`ch16-panel-A:95`) straight over it; the
  swoon list picks up at 304 (`:131`). The author: "boring."

And the panel judged the kiss against the brief's ration, not the
reader ("one line and right," `ch16-panel-A:179`) — the remit says it
measures pleasure and never rules on structure (`romance-reader-
panel.md:59–61`), but a brief's "one line at most" is a structure
call the panel ratified. What would have caught "terse": numbers the
batch already contains. Narration words per dialogue line in the
scene the leads share — ch 16's annex as the author read it: 721/21
= 34; after her recut 1,297/28 = 46; ch 15's annex (her "good
chapter"): 1,457/37 = 39; ch 14's annex after its recut: 1,810/38 =
48. The reaction beats per scene the Closeness law already requires
(STYLE:164–169, "roughly forty words a scene"; campus `METERS.md` §6)
— no panel or brief in ch 13–16 mentions CLOSENESS or a reaction beat
(grep: zero hits in `book2/notes/ch1[3-6]*` and the four briefs), so
the cage as the author read it (267 words, one thought) passed an
instrument that exists and was not run. 1.5.0's slow-beat count is
right and narrow (it fires only at a touch); the awkward test is a
yes/no. Neither reads the scene's length.

**Instrument:** romance-reader-panel (the count as the headline; the
swoon inventory as protection). **Fix:** `romance-reader-panel.md`,
"Romance first — your count stands" — the verdict line carries, for
every scene the leads share alone, three numbers beside the count:
words, narration words per dialogue line, reaction beats (STYLE
Closeness rule 2); under the brief's floor (F18) is a finding
"whatever the count says." The swoon inventory names at most one
line per scene under twelve words, so ten one-liners cannot outscore
one long paragraph. No new instrument: the Closeness meter is
already law and already dealt to this book.

### F20 — BLIND SPOT: the check built for the author's volley cannot fire on it, and fires on three chapters she accepted

`studio/tools/ending-check.py:36–43` defines a volley as three
consecutive dialogue lines of four words or fewer. The author's
exhibit is a nine-word line answered by a two-word line
(`git show 8cb518e:…/ch16.md:291–293`). Run on that file today: no
volley warning (the check prints only the name line). Run on the
accepted pages: ch 13, 14 and 15 each get "WARN: 1 run(s) of three
short volleys" — on three chapters the author accepted without a
volley note (the ch 15 hit is "Doc." / "Watch." / "Again.", the
exchange the panel listed under FUN). A check that misses its own
exhibit and fires on the accepted pages trains the operator to skip
it (the same lesson as F6's banned-words regex, which still fires on
`ch13:361` "On the way out she passed the drawing" — the F6
narrowing did not land). An echo-reply test — a short reply whose
content words all appear in the line before it — fires on exactly
two lines in the batch: the author's ("They were.") and one
deliberate one (`ch15:312` "I nodded."). Two smaller holes in the
same file: the name detector is "any capitalized word seen three
times" (`:17–20`), so ch 16's last section "names: Fieldhouse" and
the accepted ch 13 ending (fixed at #148 to say the annex) still
warns "NOBODY"; and the staccato test reads the last section only,
while the author's ch 13 note was about "the last two sections."

**Instrument:** `ending-check.py`. **Fix:** replace the run-of-three
with the echo-reply test, scoped to scenes the leads share; read the
names from the registry's name map, not capitalization; run the
staccato numbers on every section and print them (the panel's F19
numbers come from the same pass). Then the lint's WARN is worth
reading.

### F21 — CONTRADICTION + DRIFT: the panel is the book's second drafter, and the audit's example phrasing reaches the page through it (the task's question 5)

DRAFTING-PROTOCOL:210–214: "the voice stays one person's… never as a
merge of drafts." The panel's remit asks for "a concrete fix for
each" (`romance-reader-panel.md:52–54`). In practice the panel writes
the line and the drafter pastes it. On the accepted pages, verbatim
from the panel reports:

- ch 13 (panel C fixes 2, 3, 7): `ch13:216`, `:293`, `:350`.
- ch 14 (panel Q2, Q6, Q7): `ch14:239`, `:270`, `:281`, `:350–351`.
- ch 15 (panel A Q6, Q7, Q8, Q9, Q10): `ch15:25` (the establishing
  sentence), `:114–116` (a scene's establishing line), `:147–151`
  (another), `:155–164` (the trainer's three lines, whole), `:197`,
  `:207–209`, `:243`, `:361`, `:375`, `:394–395`.
- ch 16 (panel A Q1, Q2, Q4, Q5, Q6, Q9): `ch16:25`, `:61–63`,
  `:145`, `:264`, `:357–358`, `:502`, `:515–516`.

Ten sentences of ch 15 and eight of ch 16 are the panel's, including
three establishing lines and the one exchange the author praised as
"good chapter." The CHANGELOG records them as "the panel's fixes
applied." Whether that is good prose is not this audit's question;
that it is a second voice the protocol forbids, unlogged, is. The
same channel carries the audit's phrasing: `ch15-brief-audit-2026-
09-10.md:65` offered "that room always says something" as the
trainer's content, candidates B and C wrote it verbatim (`notes/
candidates/ch15-B.md:125, :266`; `ch15-C.md:104`), and candidate A —
which had not — got it on the page through the panel's rewrite
("That bunch always has something to say in a hall," `ch15:158`).
"Name in my mouth" is the same mechanism one register up: the ch 15
audit and brief say "mouth" fourteen times — "in his mouth," "in
her mouth," "his mouth was at" — as their idiom for who says a thing
(`ch15-brief-audit:78, :88, :93, :99, :104, :126, :139`;
`brief-ch15.md:72, :224, :228, :352, :400, :402`), and two of three blind
drafters wrote "your name in my mouth" (`ch15-C.md:333`; A's line,
struck at #155). The first audit's F4 named this channel (the
manifest as a voice sample); it did not land, and the batch shows
its second and third routes.

**The ruling asked for:** "shape only, not words" does not work — B
and C prove that a shape offered in an addendum IS the convergence.
Any sentence an addendum or a panel quotes as an example is banned
text on arrival. **Instrument:** the audit addendum; the panel's fix
line. **Fix:** `continuity-keeper.md` rule 4 / the addendum template
— rulings are facts and prohibitions; a phrasing offered as an
example goes on the brief's BANNED line in the same addendum;
`romance-reader-panel.md:52–54` — "a concrete fix names what the
line must do and where; the drafter writes it." The fold logs any
panel line kept verbatim as a graft (the protocol's own NAMED FIX
rule, `DRAFTING-PROTOCOL:210–214`).

### F22 — MISS: every author catch in the window, and the instrument each ran past

| Ledger row | The catch | Instrument on duty and what it was running | What it could not see | Landed? |
|---|---|---|---|---|
| :88 (#147, ch 13) | "too many pronouns… too cold" — say Dan's name | The naming list ("Merritt" in narration; "Dan" once, optional — `brief-ch13.md:224–227`; addendum 6) | A rule about which name never asks whether the page is warm; the lint counts names, not warmth | The name map; ch 13 fixed |
| :89 | the tablet scene needs his side — a look held, a hand that stays | The rung ruling (6: "a second, unremarked" — addendum 4) | The ladder measures the touch, not whether the reader saw HIM choose it | Fixed on the page; STYLE unchanged |
| :90 | the last two sections "too staccato… where are they" | Panel C: swoon #10 and #11 are the two sections (`ch13-panel-C:105–106`); the check "Deliberate… Keep." (`:150`); D7 ("open mid-motion") drawn for the winner (LOG:387) | The panel protected the terse lines; the card asked for the thing the author disliked | The establishing line; D7 annotated instead of retired (F26) |
| :100 (#153, ch 14) | the disclosure abrupt — needs a prompt | The brief: "THEN, unprompted" (`brief-ch14.md:115`); the outline: "unprompted" (`:12`) | The brief ordered the abruptness | The prompt rule; B2-D17 |
| :100 | the boxes "too dry… too boring" | The panel: scene 2 "Felt throughout" (`ch14-panel:52`); the beats counted (13 in the scene) | A count of beats cannot see a work montage | Taste 15's pleasure beats |
| :101 | the stakes first, leading to the disclosure; the old story a copy of the new | The panel Q1 asked "said or recited" and found the stakes "stapled" (`:160–166`) — half the catch; the audit built the colleague from `ch02:165–169` (the one who decided who played) — the copy was canon | The audit checks facts against pages; nothing asks whether a backstory rhymes too closely with the plot | B2-D17; no instrument |
| :102 | "too cold… a robot" — second time | The panel CAUGHT it: Q2 "Cold for thirty lines" (`ch14-panel:171–177`); its one-line fix was applied before the author read (`git show f1e155b:…/ch14.md:221–223`) | The fix scale — one line locating her eyes — is below the author's threshold ("a half smile, she looked him in the eyes"); the remit asks for "a line or a beat" | The face rule; F18's floor is the whole |
| :104 | Delores's bank note "random" | The brief: "ten years is long enough to pay a thing" as a rhyme with Dan's decade (`brief-ch14.md:129–133`); the audit approved the register (W4) | Nothing asks whether an anchor decodes without the reader knowing the rhyme | B2-D17(5) |
| :105 | the last section "doesn't even say Ayesha is there… too staccato" — second time | The panel: "L332–336 (the turf, five fifteen, the sheet in his hand)" honored (`:220`); swoon #13 protected the exchange (`:130`) | The rule then said where/when/hand, not WHO; the panel protected the staccato as a swoon (F19) | WHO; `ending-check.py` (which cannot fire on the exhibit, F20) |
| :107 (#155, ch 15) | "name in my mouth" | The panel: swoon #8, "the line of the chapter" (`ch15-panel-A:107`); the scoreboard quoted it (`ch15-scoreboard:15`) | A phrase-level dislike has no instrument but the ban list; the convergence has one (F21 — the audit's idiom) | RECENT ban |
| :108 (chat) | the cards "read like a list of things" | Kit 12: "what has happened, in chapter numbers" — every card since ch 9 obeyed it (`ch15-card.md:11–17`) | The template asked for the ledger | Kit 12 amended — and still contradicts itself (F27) |
| :109 (#156, ch 16) | "They were." — boring | The blind candidate wrote it (A:300–302); panel A read past it (F19); the lint had no volley check | No instrument read exchanges for work done | STYLE (d); `ending-check.py` — which cannot fire on it (F20) |
| :110 | more description of looks and feelings; awkward | The brief: "Her face at every turn" (`brief-ch16.md:205`) — and the panel found it "at every turn" (`ch16-panel-A:179`) | Presence of a face at each turn is not the same as time spent on it; nothing asked for awkwardness | STYLE (b); panel 1.5.0 awkward test |
| :111 | the kiss too fast | The brief: "one line, not the scene's point" (`brief-ch16.md:64–65`; addendum 29); the panel: "one line and right" (`:179`) | The brief ordered it; the panel ratified the brief | STYLE (a); panel 1.5.0 slow-beat count |
| :112 | the cage's first sentence too long; more introspection at the ball; "much of this seems so terse" | The brief: "the cage is one [paragraph]" (`brief-ch16.md:376`); the Closeness law's reaction beat per scene was not run by anyone (F19) | The brief rationed the scene; the existing meter was idle | STYLE (c) — a new rule where an old one was unrun |
| :99 (chat) | "don't be so clever" (a PR titled "the handful") | showrunner 2.2.1's say-it rule already covered it (`showrunner.md:146–159`) | A rule about sentences did not reach titles | 2.4.1 |

Two of sixteen were half-caught by the instrument on duty (the ch 14
stakes "stapled"; the ch 14 cold, at the wrong scale); the rest went
through a brief that ordered the thing, a panel that protected it,
or a check that could not see it. **Fix:** F18–F21 are the fixes;
the one gap with no instrument at all — a backstory that copies the
plot (:101) — is a developmental-editor question (its Hauge audit's
"echoes" item, `developmental-editor.md:92–93`) and the developmental
editor did not read a chapter this batch (LOG:384–406).

### F23 — TEMPLATE: the seams are still the same sentences, and the brief still hands every drafter the banned sentence

The first audit's F3 asked for the opening check to read the first
paragraph after every `***`; `opening-check.py:32–43` still reads
paragraph one. This batch's seams, from the section scan:

- The 5:15 check opens the same way in three consecutive chapters —
  `ch13:366` "Five fifteen, the practice turf, the lights on over the
  field"; `ch14:380` "At five fifteen on the practice turf the lights
  were up white"; `ch15:147` "At five fifteen Aisha stood at the near
  hash" — after the ch 15 panel flagged ch 14's as "verbatim in shape"
  and wrote the replacement (`ch15-panel-A:180`, F21).
- Her office opens the same way in two consecutive chapters —
  `ch15:215` "Aisha was at her desk at the warm end of the annex at
  ten to seven"; `ch16:279` "Aisha was at her desk at the warm end of
  the annex at eleven" (eleven shared seven-word runs between ch 15
  and 16; eleven between 14 and 16).
- "in the parka with the cuffs pinned" is the establishing clause on
  three pages (`ch12`, `ch14:80`, `ch16:42`).

None of these is a chapter opening, so the tool passes all four and
the lint exits 0. And the STAKES RESTATED slot (DRAFTING-PROTOCOL:
333–335, "every brief restates that sentence") still prints the
sentence RECENT closed at ch 10–11 (`RECENT.md:31–37`) into every
brief — `brief-ch13.md:207`, `brief-ch15.md:283`, `brief-ch16.md:272`
— so the ch 16 audit had to add "the brief's STAKES RESTATED sentence
is for the drafter's eyes, not the page" (`ch16-brief-audit:167`). A
slot whose output must be banned on arrival is a template feeding
itself. **Instrument:** `opening-check.py`'s scope; the STAKES
RESTATED slot. **Fix:** the F3 change (every section's first
paragraph; print the seams); the slot reads "what THIS chapter puts
at risk, in the POV's terms" and drops the standing sentence.

### F24 — DRIFT: nobody ran the showrunner, so nothing bound the brief-writer; the cards the author approved carried the errors (the task's question 3)

Every brief in the batch cites "the showrunner's ruling" (`brief-
ch15.md:198`, addendum `:385–389`; the three scoreboards "the
showrunner read all three"). `LOG.md:384–406` has no showrunner row
— the last is `:295` (2026-08-29). The orchestrating session wrote
the cards, briefs and scoreboards, so the showrunner's rule 1
("compute state from the files — store nothing," `showrunner.md:34`)
and its talk-plainly rule did not apply to whoever wrote them; the
2.4.1 and 2.4.2 bumps amended an agent that has not run in twelve
days. The briefs' errors are the kind memory makes: ch 16's fixed
text put Aisha "at the near hash" in a stadium (the hash is the
practice field's on five pages), Tick on the stadium PA (he was on
WDSS at `ch03:265–267`), In 3/Out 4 against the arc doc's row
(`ch16-brief-audit:11, :128–129`), plus "the ambulance gate," "the
AED," "the rail behind the bench" (`:49–50`); ch 15's defaults had
six contradictions (`ch15-brief-audit:5`). The audit caught all of
them — it is a blocking gate and it worked. What it could not undo:
the card had already gone to the author and been approved. The ch 15
card she said "Go" to reads "nothing public until the eleventh of
February" and "Nothing public until February 11" (`git show 4ff1edd:
…/ch15-card.md:80, :104` — the annex deadline, not the terms'; audit
B3); the ch 16 card she approved has "she stands at the hash" and
Tick "signing off the broadcast" (`git show 79268f4:…/ch16-card.md:
39, :96`). PIPELINE §3c orders card → author → brief → audit
(`PIPELINE.md:131–136`; kit 12:8–10), so the author's ruling is
spent on facts nobody has checked, and the correction arrives as a
second card (`90cbe40`, `2c135ad`). **Instrument:** PIPELINE §3c's
order; the brief's FURNITURE line; the registry's Source column.
**Fix (three narrowings, no new rule):** (1) `PIPELINE.md:131–136` —
the audit runs on the card and brief together, BEFORE the card goes
to the author; (2) the FURNITURE and NAMING lines cite a `chNN:line`
or a registry row for every item that is not marked NEW — the audit
then verifies cites instead of re-deriving the stadium; (3) the
registry's Source column gets its line cites (F11 — today it has
zero `chNN:NN` cites in 138 rows). And either log the orchestrator's
showrunner work as showrunner runs, or say in `showrunner.md` that
the orchestrator holds the role under the same rules.

### F25 — MISCOUNT + GHOST: the ledgers disagree with themselves again, and the fold has no owner (the task's question 6)

- **Edges (test-set item 4, recurring):** `book2/THREADS.md:36–39`
  reads "3 spent —" then lists four and ends "**4 spent; 6 remain**";
  the ch 16 entry (`:581` onward, "Edges: one ('Damn') — 5 remain")
  is right against the page (`ch16:183`) and the header was not
  updated. The header is what the next brief reads (`brief-ch16.md:
  321` "6 remain" was written from it).
- **The quiet band:** header `:56–57` "Q2 open"; the ch 16 entry
  "~12% (the quiet band, once this quarter)"; the lint says 11.9%,
  which is inside the tool's band and outside the protocol's (F26).
- **The arc ladder:** the ch 14 fold wrote "rung 7" into the Spends
  column (`plots/romance-arc.md:91`), so `romance-build-check.py`
  FAILED the doc from 2026-09-09 until the ch 15 audit simulated the
  tool by hand and found it (`ch15-brief-audit:15–18`). Nobody with a
  shell ran the check at the fold; the keeper, who is told to run it,
  has no shell (F8, again: `ch15-brief-audit:7`, `ch16-brief-audit:9`
  "no shell in this run").
- **Fixed after an audit caught them:** "Mark today: 5" (lagged since
  ch 6; `THREADS.md:98–99` now 8); `plots/provider-partner.md:27`
  (said 19; now 15); the letter count (`THREADS.md:670`, ruled at
  #156).
- **Still wrong:** `plots/b12-outline.md:576` "the whole county wants
  Friday" — ruled Saturday at the ch 15 addendum, the outline not
  conformed; the next brief that pastes the "verbatim manifest" gets
  Friday back.
- **GHOST by design:** `notes/furniture-registry.md:116` and `:126`
  store twenty lines from the losing candidates of ch 15 and 16
  ("Banked, unused… never reinvent by accident") in a registry whose
  header says "canon from ACCEPTED chapters" (`:3`). The first
  audit's F11 found one losing-candidate line in the registry
  (FirstDownMom) and called it a ghost; the fold now files them on
  purpose, and the brief's furniture source is a voice sample from
  drafts the drafters must not read (F4).

**Owner at the fold:** none named. PIPELINE §3c lists "merge → fold"
and stops; PR-WORKFLOW mentions folds once (`:203`). **Fix — one
line in the fold's checklist (PIPELINE §3c):** "Before the fold
commit: copy the chapter entry's counts (edges, anchor, dialogue %,
rung, name spends) into the header ledger by hand in the same
commit; run `romance-build-check.py` on the arc doc and quote its
verdict line in the commit message; conform any doc an addendum
ruled against (the outline, the partner doc); the registry takes
rows only with a `chNN:line` — losing-candidate lines go to the
estate file, not the registry."

### F26 — DRIFT: four rules the practice no longer follows (the task's question 7)

- **Length.** `PIPELINE.md:170–171`: "~2,000–2,500 words, ten minutes
  of audio." The briefs: 2,400–2,800 (ch 13, 14), 2,600–3,000 (ch 15),
  2,800–3,200 (ch 16). The pages: 2,858 / 3,015 / 2,944 / 3,937 body
  words (`dialogue-lint.py`). Ch 16 after the author's recut is 700
  over its brief and 1,400 over the pipeline. The practice is right
  (the author asked for more, three times); the two numbers are
  wrong, and the brief's ceiling is F18's mechanism. Fix: PIPELINE
  says "~2,800–3,500; a set piece may run past it"; the brief's
  length line becomes the leads' floor (F18).
- **The quiet band.** DRAFTING-PROTOCOL:170–171 and `chapter-lint.sh:
  10`: "~8–10% once per quarter." `dialogue-lint.py:41–46` labels
  anything from 8% to the 15% floor "quiet-chapter band." Q1 was
  logged spent on ch 3 at 13.1% (`THREADS.md:56`) and ch 16 at 11.9%
  is logged the same way — twice under the tool's band, never under
  the protocol's. The practice has decided; conform the protocol and
  the lint's echo line to "8–15%," and log Q2 = ch 16 (F25).
- **D7.** The first audit proposed retiring it (F15: it duplicates
  DRAFTING-PROTOCOL:372–374). Instead it was annotated (`DECKS.md:35`
  "mid-motion still locates the reader…") and drawn twice more:
  for the ch 13 winner (LOG:387 — the draft whose last two sections
  the author called unlocated, `AUTHOR-NOTES:90`) and for ch 16
  candidate B (LOG:403, "read as: mid-motion AND located and named…
  the author's catch stands"). A card that has to be read against
  itself is not variance. Retire it.
- **"Wave."** PIPELINE:151 retired the wave on 2026-09-03.
  `RECENT.md:13` ("ride in every wave-4+ brief"), `:104–153` ("Wave-
  2+ drafters," "wave 6 HONORED it," "Wave-7+ drafters") address
  drafters who no longer exist. And RECENT now carries STYLE law
  verbatim (`:26–30` the establishing line, `:31–39` the calendar
  opening, `:86–92` "WATCH → LAW" slow the good parts) — the two-
  ledgers finding (F10) has a third ledger. RECENT is a recency
  ledger of tics; law lives in STYLE; a brief points at both.

### F27 — CONTRADICTION: templates and agents that disagree with the law or with themselves

- **Kit 12 against its own amendment.** The 09-10 header says
  "chapter numbers only for what comes NEXT… no bolded sub-labels
  inside a paragraph except the one Rooting for sentence"
  (`studio/series-kit/12-chapter-card.md:21–33`). The template body
  below it still says "the kiss, by chapter" (`:62`), "their moves
  so far, by chapter" (`:67–68`), "its arc by chapter" (`:72`), and
  its last section is two bolded sub-labels inside one paragraph
  (`:72–73`). The next book starts from the body, not the header.
  Fix: conform `:62, :67–68, :72–73`; the ch 16 card v2 is already
  the model.
- **The brief against STYLE on the kiss.** `brief-ch16.md:64–65` and
  addendum 29 (`:170`) "one line at most" vs STYLE:523–527 "at least
  four sentences between the decision and the contact." The slot
  that produced the ration (THE ROMANCE MOVE's "texture" clause) was
  not amended when (a) was written; the next set-piece brief can
  say both.
- **Two review-stack orders (F13, unlanded).** DRAFTING-PROTOCOL:
  51–54 "Continuity → developmental → line"; PIPELINE:244–257 and
  `showrunner.md:64–66` the reverse. In this batch neither ran: no
  developmental, line, or post-draft continuity pass on ch 13–16
  (LOG:384–406); the developmental editor ran the rooting-for survey
  only.
- **The keeper and its tool (F8, unlanded).** `continuity-keeper.md:
  22–28` "run `python3 studio/tools/romance-build-check.py`"; tools:
  Read, Grep, Glob (`:4`). Both audits this batch open with "no
  shell" and simulate it by hand (`ch15-brief-audit:7`; `ch16-brief-
  audit:9`). The fold line in F25 puts the run where the shell is.
- **The panel's remit against the protocol** (F21).

### F28 — STALE: references that no longer match the room

- `CLAUDE.md:18` "twelve specialists"; `:127` "Thirteen specialists";
  `studio/agents/ROSTER.md:25–41` lists fifteen. The table at
  `CLAUDE.md:129–142` still omits romance-reader-panel, superfan-
  reviewer and gtm-strategist (F16, unlanded).
- `studio/AUTHOR-TASTE.md:375–378` "Last review: 2026-09-05 (entries
  13 and 14 added)" — entries 15 and 16 (`:380–448`) sit below the
  footer; entry 8 still carries its duplicated "Caught:" block
  (`:231–244`).
- `studio/DRAFTING-PROTOCOL.md:3–5` "PROPOSED 2026-08-04… locked when
  the author blesses it" — cited as LAW in every brief of the batch.
- `studio/PIPELINE.md:268–278` "Current state" — three books, not the
  one in production.
- `studio/agents/variance/DECKS.md:8–23` rules numbered 1, 2, 3, 4,
  5, 7, 6; the editor deck (`:52`) is dealt to three agents and the
  auditor's definition says to draw from it (`instrument-auditor.md:
  138–140`) — the auditor is not in the deck's list.
- `instrument-auditor.md:142–156` "Your own test set — The first run
  must account for these four" — the second run's test set came in
  the orchestrator's brief; the definition has no rule for the
  second run onward. Fix: "from the second run, the test set is the
  last audit's open findings — report each as landed, recurring, or
  dropped."
- `studio/agents/CHANGELOG.md:86` — an entry with no date header
  (": plot-architect 1.5.0, developmental-editor 1.5.0…").
- `book2/STATE.md:14–19` "panel 1.3.0" (now 1.5.0); `showrunner.md:
  92–96` "variance-EXEMPT" — moot while the agent does not run (F24).
- `LOG.md:406` names `notes/rooting-for-survey-2026-09-10.md`; the
  file is not on disk at the time of this audit (a concurrent run —
  verify at the fold rather than a finding).

### F29 — OVER-TOOLED: retire, merge, or narrow

- **The four brief slots** THE OTHER LEAD'S FACE, THE SLOW BEAT, THE
  ENDING THINKS, THE LAST EXCHANGE → one floor line (F18).
- **STAKES RESTATED** → "what this chapter risks, in the POV's terms"
  (F23).
- **D7** → retire (F26).
- **The ending check's run-of-three** → the echo-reply test (F20).
- **The "which"-appendix WATCH** (`RECENT.md:149–154`): one hit each
  in ch 15 and 16, zero in 13 and 14 — the ration is honored two
  batches running; keep the grep, drop the WATCH text (F15, again).
- **The "since June" per-chapter cap:** exactly one in each of ch
  13–16 — honored; keep the grep, drop the reconciliation nobody
  does.
- **The personification quota** fired once this batch (`ch16-panel-
  A:198` counted six) and was applied; it earns its place for now —
  withdrawn from the F15 retire list.
- **The banned-words regex** still fires on innocents (`ch13:361`)
  and on nothing real in four chapters — narrow it as F6 asked.
- **RECENT's duplicated law** (`:26–39`, `:86–92`) → one line each
  pointing at STYLE (F26).

Net: nine rules in, zero out, in three days. This list is nine out.

---

## What to fix TODAY (before ch 17's card) versus BACKLOG

**Today — the fold and the ch 17 brief, no agent edits needed:**
1. `book2/THREADS.md:36–39` and `:56–57` — conform the edge header
   (5 spent, 5 remain) and log Q2 = ch 16; run `romance-build-check.py`
   and quote its line in the fold commit (F25).
2. `book2/plots/b12-outline.md:576` — Friday → Saturday (F25).
3. `studio/series-kit/12-chapter-card.md:62, :67–68, :72–73` — strike
   "by chapter"; the last section as sentences (F27).
4. `studio/tools/ending-check.py` — the echo-reply test in place of
   the run-of-three; names from the name map; every section's numbers
   printed (F20). One tool, one afternoon.
5. The ch 17 brief: one THE LEADS' SCENES floor line in place of the
   four slots; no "one line" for any touch; the STAKES sentence
   replaced by the chapter's own risk (F18, F23, F27) — a trial on one
   connecting chapter before the template changes.
6. The ch 17 card and brief go to the audit BEFORE the card goes to
   the author (F24, item 1) — an order change, not a rule.

**BACKLOG (an `agents:` PR after ch 17 shows the floor works):**
- F18 the template consolidation (DRAFTING-PROTOCOL; STYLE's four
  rules become one section with the floor); F19 the panel's three
  numbers and the swoon cap; F21 the addendum's "examples are banned
  text" and the panel's "name what the line must do"; F23 the seams
  in `opening-check.py`; F24 the furniture cites and the registry's
  Source column; F26 the pipeline's numbers, the quiet band, D7,
  RECENT's wave text; F27 the review-stack order and the keeper's
  tool line; F28 the housekeeping PR (the counts, the taste footer,
  the protocol header, DECKS, the auditor's test-set rule); F29 the
  retire list. Plus the first audit's unlanded ten (below).

## What landed from the last audit

**Landed:** F1 (the listening file keeps bold card lines), F2 (STATE's
ch 13 hand-forward; ch 13, 15 and 16 ran three drafters), F6 (the lint
exits 1 on an opening-check FAIL — verified: `chapter-lint.sh:48`).
**Partly:** F10 (the BANNED line now points at RECENT as of a date —
and its "plus" list is thirty items in ch 16, `brief-ch16.md:325–345`);
F11 (FirstDownMom struck from THREADS; the Source cites were not
added, and the registry now files losing-candidate lines on purpose,
F25); F12 (anchors 7–12, "Mark today," and the ch 11 edge line were
conformed — and the edge header is wrong again at ch 16, F25).
**Not landed, and each recurred in this batch:** F3/F14 (the seams:
the check scene three chapters running, F23), F4 (the manifest and
now the addendum and the panel as voice samples, F21), F5 (no
per-chapter repetition scan; no canon sweep for ch 9–12 or 13–16 in
the LOG), F7 (the build check's blank-Spends hole — and the fold then
broke the doc a different way, F25), F8 (both audits "no shell"),
F9 (the keeper has no taste-sheet section; the panel's TASTE finding
still lists a subset — `ch16-panel-A:204–212` names six of the sixteen
numbered entries),
F13, F15 (D7 drawn twice more), F16 (every reference still stale).
Ten of sixteen untouched, while nine rules were added.

## Verdict — what the room learned

The room is very good at facts. Four brief audits caught a hash mark
in a stadium, a radio host on the wrong microphone, a date that meant
her building instead of his season, a phrase the doctor refused on
air, and a broken ladder table, and none of it reached the author.
The three-drafter competition worked as designed three times: the
panel read blind, the scoreboard picked, the author read one winner
and called two of the three "good" or close to it. What the room
cannot yet do is give the two people the reader bought the book for
enough room. Every rule it writes is a ceiling — once, one line, one
clause, at most, never — and the leads' scenes are the only scenes
with no floor, so the author has now said "staccato," "robot," and
"terse" on three chapters in a row, and each time the room answered
with more ceilings. The panel makes it worse in a way that is easy to
miss: it counts beats and lists quotable lines, so it rewards the
short clipped exchange and then protects it as a swoon — three of the
lines the author disliked were on the panel's keep list. And the
panel has quietly become the book's second drafter: ten sentences of
chapter 15 and eight of chapter 16 are its words verbatim, which the
protocol forbids and nobody logs. The one thing most likely to
embarrass the room next is the fold: the ledger header says six
swears remain and the chapter entry says five, the arc table was
broken for a day by the fold's own hand and no one with a shell ran
the tool, and the registry now keeps twenty lines from drafts the
author never read as if they were canon — the same class of ghost the
first audit found, now filed on purpose. The fix is not a rule. It is
one floor line in the brief, three numbers in the panel's verdict, a
tool that can actually see "They were.", and a fold that runs the
check it already owns.
