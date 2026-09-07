# Instrument audit — 2026-09-07 (first run)

**Agent:** instrument-auditor 1.0.0, first run. **Batch under audit:**
campus 1.2 chapters 9–12 (`books/campus-series/book2/manuscript/ch09.md`
– `ch12.md`; ch 12 is accepted-pending on the open PR and is read as
accepted). **Ledger window:** every row in `studio/AUTHOR-NOTES.md`
dated 2026-09-05 through 2026-09-07 (rows at :69–91). **Last audit:**
none — `studio/agents/audits/` did not exist before this run.

**Variance card:** E4 — watch transitions: how scenes are entered and
left. Read as: in the CONVERGENCE pass, weigh the `***` seams — the
first line after each break, the last line before each, and the
chapter's last line — because that is where templates hide when the
opening has been fixed.

**Read, in the definition's order:** the ledger window; ch 9–12 and
their briefs, audits, panels, cards and CHANGELOG entries; STYLE,
PIPELINE, DRAFTING-PROTOCOL, PR-WORKFLOW, AUTHOR-TASTE, the campus
STANDARDS and both DECISIONS files; all fourteen agent definitions,
the five personas, ROSTER, CHANGELOG, BACKLOG, DECKS, LOG, RECENT;
the six tools' source; THREADS, the furniture registry, STATE. **Run:**
`opening-check.py` and `chapter-lint.sh` on each chapter of the batch;
`romance-build-check.py` on `plots/romance-arc.md`; a one-off grep for
any six-word-or-longer sentence verbatim on two or more pages; a
one-off listing of every section's first and last line (the E4 seams).
All paths below are under `/home/user/writing/`; `chNN` means
`books/campus-series/book2/manuscript/chNN.md`, `book2/` means
`books/campus-series/book2/`.

---

## Findings (severity-ordered)

### F1 — BLIND SPOT: the listening file silently drops lines of the chapter card

The card is law — "the first thing the author hears" (PIPELINE:113–128;
showrunner.md:113–129). `studio/tools/listening-file.py:28–29` skips
any card line that starts or ends with `*`, meant for the card's italic
instruction line. Every bold-edged card line is eaten with it.

- `book2/notes/cards/ch12-card.md:13` — "Plans, heading for the Point
  of No Return at 15. **This chapter:**" → the file the author hears,
  `book2/notes/listening/ch12-2026-09-07.md:9`, reads "Past the Change
  of Saturday."
- `ch12-card.md:86` ("**The town.** The board has never once
  speculated…") → `ch12-2026-09-07.md:27` begins mid-sentence: "adult's
  love life in plain text."
- `ch11-card.md:64` → `ch11-fixes-2026-09-07.md:27` begins "runs, and
  her own son is the board's other target."
- `ch10-card.md:56, 65, 68, 75, 77` and `ch09-card.md:75, 80` — the
  same five and two lines gone from those files.

Every card in the batch lost two to six lines in the author's copy,
including the Hauge-position sentence and both "Two more to keep an eye
on" openers. **Instrument:** `listening-file.py` (showrunner 2.3.0's
card promotion). **Fix:** `studio/tools/listening-file.py:28` — skip
only a line wrapped entirely in single `*…*` (the instruction line),
never a line that merely begins or ends with `**`; regenerate the ch 12
listening file before the author listens.

### F2 — DRIFT: one drafter ran against a default of three, for four chapters, and the record was in plain sight (test-set item 2)

`studio/agents/variance/LOG.md:370, 374, 377, 381` log "single drafter"
for ch 9, 10, 11, 12. `book2/plots/brief-ch09.md:3–7` cites "PIPELINE
§3c" as authority for "ONE drafter"; PIPELINE §3c as it then stood
(:157–160) said "Blind competition stays where the chapter is new (2–3
candidates)"; DRAFTING-PROTOCOL:129–130 said "default N=3". The
showrunner reported the drift only when the author asked (AUTHOR-
NOTES:86). No instrument reads the LOG against the protocol, and the
showrunner did not run once in the batch (no showrunner row in LOG
after :277). The ruling changed the rule to fit the practice (item 5,
DRAFTING-PROTOCOL:189–219) — right for connecting chapters. **The rule
is about to drift again the other way:** `book2/STATE.md:14–17` still
states the cadence as "one drafter", and `STATE.md:49–57` plans ch 13
"alone … drafter D1 or D5" — one card — while DRAFTING-PROTOCOL:193–200
names ch 13 a SET PIECE requiring three blind drafters with distinct
cards. **Instrument:** STATE.md's PICK UP HERE block (the hand-forward
every thread reads first). **Fix:** `book2/STATE.md:14–17, 49–57` —
"ch 13 is a SET PIECE: three drafters (D1, D5, and the next LRU), panel
blind A/B/C, the showrunner's scoreboard, one line in the PR on which
won"; the ch 13 brief's status line names it.

### F3 — TEMPLATE: the explicit-opening rule produced the same opening three times (test-set item 1), and the same mechanism is live at every scene entry

The calendar recital: `ch10:20–36` ("Monday of signing week … Trey
Gault played on the nineteenth only if she signed a form saying his
brain had healed"); `ch11:21–29` ("Friday, December eleventh … Trey
played on the nineteenth only if Aisha Cole signed a form saying his
brain had healed"); ch 12 before its rewrite (`git show
ff34a83^:…/ch12.md`, first paragraph: "Saturday, December twelfth, and
the nineteenth was seven days off … Trey Gault played on the nineteenth
only if Aisha Cole signed a form saying his brain had healed"). The
rule they ran under: THE OPENING, SAID — "the chapter's first
paragraph … what today is and what is at stake" (DRAFTING-PROTOCOL:
339–342 pre-amendment; STYLE:480–487). The check on it, the panel's
opening test, PASSED all three because it reads one chapter at a time:
`ch10-panel-2026-09-06.md:126–128` ("A stranger can repeat it back.
Passes."), `ch11-panel-2026-09-07.md:169–171` ("Pass — this is the
explicit opening the author praised on ch 6"), `ch09-panel-2026-09-05.
md:129–131`. What the rule could not see: it demanded X of each chapter
and nothing compared X across chapters. **Landed the same day:**
`opening-check.py`, the "said, not recited" amendment, RECENT's calendar
ban. **What the E4 read shows is still open — the seams:**

- The Mule enters the same way three times in two chapters: "The Blind
  Mule on a weeknight this deep in the season / was the rail…"
  (`ch10:379–380`), "The Blind Mule had one booth" (`ch11:109`), "The
  Blind Mule at midnight, last call" (`ch11:403`).
- The house enters the same way in both Dan chapters: "At the house,
  the truck keys went toward the hook by the door, / and the hook
  already had a coat on it" (`ch10:478–479`); "At the house, at
  midnight, the keys went on the hook, / and the coat was still under
  them" (`ch12:380–381`) — after the ch 12 audit listed ch 10's
  sentences as "not to repeat" (`ch12-brief-audit-2026-09-07.md:
  233–240`); the drafter rebuilt the shape with the words moved.
- The check scene is one template across two POVs: "came onto the turf
  from the annex side" (`ch10:247`, `ch11:39`); "the trainer cutting
  tape a few yards off" (`ch10:277`, `ch11:44`); "went to thirty-four
  at the near hash" (`ch10:353`, `ch11:100`); "the pins … went with
  her" (`ch10:356`, `ch11:102`); "across the lot by five forty"
  (`ch10:360`, `ch11:103`).
- "the annex across the lot, low, dark at the cold end": `ch10:319`,
  `ch11:81–82`, `ch12:189` (the ch 12 panel counted five across the
  batch and varied one, `ch12-panel-2026-09-07.md:65–66`).

`opening-check.py` reads paragraph one only (`opening()`, :32–43).
**Instrument:** the opening check's scope. **Fix:** `studio/tools/
opening-check.py` — run the shared-five-word-run test on the first
paragraph after every `***` against every earlier chapter's section
openings, and print each section's first and last line so the panel
sees the batch's seams side by side; no new rule.

### F4 — TEMPLATE (the mechanism): the fact manifest hands the drafter the neighboring chapter's narration, which is the channel blind drafting exists to close

DRAFTING-PROTOCOL:36–41 — drafters get "NOT the neighboring chapters
… a tic can't propagate through a manuscript the drafter never reads."
The manifest reads it to them. `book2/notes/ch11-brief-audit-2026-09-07.
md:243`, FACT MANIFEST, Places: "The practice turf under lights, 5:15,
printed sheet, the trainer cutting tape within earshot of the coach
only (ch10:227–267). The annex across the lot, low, dark at the cold
end." → `ch11:44` "with the trainer cutting tape a few yards off";
`ch11:81–82` "the annex across the lot, / low, dark at the cold end."
`ch10-brief-audit-2026-09-06.md:117` and `brief-ch10.md:326–328` hand
the drafter "the film-room window looks across the lot to the Annex" →
`ch10:28`, `:148`, `:319`, three renders in one chapter. `ch12-brief-
audit-2026-09-07.md:233–240` quotes ch 10's home-scene sentences in
full under "sentences not to repeat" → `ch12:380–381` (F3). The
manifest is meant to be facts (DRAFTING-PROTOCOL:31–35); written as
narration it is a voice sample from the chapter the drafter must not
read. **Instrument:** the continuity-keeper's FACT MANIFEST and the
brief's "do not repeat" lists. **Fix:** `.claude/agents/continuity-
keeper.md`, rule 4 / the manifest form — furniture as nouns with a
`chNN:line` cite, never a narration sentence; verbatim quotes are
dialogue only (the PROTECTED LINES block); a "do not repeat" entry
cites the line and never prints it.

### F5 — DRIFT: the repetition scan now runs after the author reads

DRAFTING-PROTOCOL:161–165: the cross-batch repetition scan "runs BEFORE
the author reads." PIPELINE:165–166 (the cadence): "The cross-batch
canon sweep still runs per batch … after every fourth accepted
chapter." Under the cadence the only repetition scan is the batch
sweep, which runs after the author has accepted four chapters — which
is why the author, not the studio, found the opening template
(AUTHOR-TASTE:151–160). No sweep has run since LOG:324 (2026-08-30).
The batch shows what it would have caught: `ch10:467` "He read to the
bottom. He read to the bottom every night." is `ch02:421` verbatim;
`ch10:474` "He put the phone in his coat." is `ch08:458` verbatim —
both accepted at #137, both later banned in the ch 12 brief as "ch 10's"
(`brief-ch12.md:270`) though the first was ch 2's. **Which is wrong:**
the practice. A grep is cheap and belongs with the lint, per chapter,
before the PR; the canon sweep can stay per batch. **Instrument:**
PIPELINE §3c. **Fix:** `studio/PIPELINE.md:165–166` — "the repetition
scan runs per chapter, inside the lint, before the PR opens; the canon
sweep stays per batch" (the F3 tool change is the scan).

### F6 — BLIND SPOT: the chapter lint cannot fail

`studio/tools/chapter-lint.sh` ends on `echo "== done"` (:46) and never
propagates an exit code; the opening check inside it (:40–41) fails and
the lint still returns 0. Run today: ch 11 `opening-check` exit 1 (six
shared runs against ch 10), `chapter-lint` exit 0. Ch 11 was accepted
(#139) with the FAIL standing — `book2/CHANGELOG.md:774–775` ("it FAILS
ch 11 against ch 10 … a MINOR fix owed") — and it still fails on the
accepted page. DRAFTING-PROTOCOL:350–353 calls it "a FAIL"; nothing
makes a FAIL block. Two smaller holes in the same file: (a) the banned-
words regex (:19) fires on innocents — `ch09:307` "all the way to the
RAV4", `ch09:361` "all the way down and back", `ch10:438` "the whole
length of it" — three false positives and zero true hits in the batch,
which trains the operator to skip the section; (b) the epigraph's "hard
cap 35 words" (SHARED-CANON:63) is checked by hand only (the ch 9 audit
had to add it to the brief, `ch09-brief-audit-2026-09-05.md:93–95`) and
ch 10's epigraph, rewritten after the "supper" note, is 36 words
(`ch10:11–17`). **Instrument:** `chapter-lint.sh`. **Fix:** `studio/
tools/chapter-lint.sh` — capture the opening check's status and exit 1
at the end if it failed; narrow the two patterns to `That was the whole
[a-z]* of it` and `the way (a|an|the|his|her) [a-z]+ [a-z]+s\b`; add an
epigraph word count to the existing epigraph line.

### F7 — BLIND SPOT + CONTRADICTION: the build check cannot fail a stage that opens unearned, and the arc doc disagrees with itself about which stage the batch is in

`studio/tools/romance-build-check.py:80–93` applies rule 4 (two earlier
rungs) only when the Spends cell is non-blank. Rows 11 (In 2→3) and 13
(Out 2→3) carry "—" (`book2/plots/romance-arc.md:88, :90`), so the want
said out loud and the first question — the two stage openings of this
batch and the next — need nothing behind them for the tool to pass.
PIPELINE:100–106 says the tool "reads the whole ladder"; it reads the
spends. Fed the batch's own miss (the author's "have we earned it"), it
fires only on the three named spends. And the doc's stage table puts
ch 9–12 in stage 3 ("Apart, carrying each other (9–12)", `romance-
arc.md:50`) while the ladder has In 2 / Out 2 for 9–10 (:86–87); the
doc keeps a footnote instead of a fix (:54–57); the ch 9 panel flagged
it (`ch09-brief-audit-2026-09-05.md:272`, the `[CHECK]`) and the ch 10
audit re-derived it (item 9). **Instrument:** the build check; the
romance arc doc. **Fix:** `romance-build-check.py` — treat any In or
Out increment as a spend needing two earlier rungs (three lines);
`romance-arc.md:50` — the stage-3 chapter range reads "11–15 (inside
from 11, outside from 13)".

### F8 — CONTRADICTION: the continuity-keeper is told to run a tool it has no shell for

`.claude/agents/continuity-keeper.md:4` tools: Read, Grep, Glob;
`:22–28` "run `python3 studio/tools/romance-build-check.py` … A FAIL
blocks the brief." All four audits say so: "No shell. I could not run
the build check. I read the tool's source and ran its rules … by hand"
(`ch09-brief-audit-2026-09-05.md:5`; `ch10-brief-audit-2026-09-06.md:5`;
`ch11-brief-audit-2026-09-07.md:172`; `ch12-brief-audit-2026-09-07.md:
178`). A check simulated by hand is a reading, not a check — it cannot
fail differently from the reader. Same class as BACKLOG:129–148 (agents
briefed to write with no Write tool). PIPELINE:100–106 and the agents
CHANGELOG (:44–54) both describe the keeper as running it. **Fix:** the
orchestrator runs the tool before dispatch and pastes its output into
the brief's AUDIT section; `continuity-keeper.md:22–28` reads "confirm
the pasted output and that the EARNED BY scenes are on accepted pages"
(no tool expansion).

### F9 — MISS: the author's catches in the window, and the instrument each ran past

| Ledger row | The catch | Instrument on duty and the rule it ran under | What the rule could not see | Landed? |
|---|---|---|---|---|
| :74 (#134, ch 9) | "is there really evidence about the boy in the boxes?" | The brief audit, facts vs canon: it quoted the records room as "thirty years of files … her predecessors' handwriting" (`ch09-brief-audit:114`) and passed the brief's opening that called that paper the boy's evidence (`brief-ch09.md:58–63`); the panel's opening test passed it too (`ch09-panel-2026-09-05.md:131`) | The audit checks the brief's facts one by one, never the brief's ARGUMENT against the facts it just cited | The page was fixed; the audit's remit was not |
| :74 | "Is this line suggesting Aisha is driving a stick shift? … a rav4 or Camry" | The brief audit ruled "the truck" from accepted pages (F8, `ch09-brief-audit:66`; addendum item 7, `brief-ch09.md:330`) | The page-wins rule beat taste entry 5 (modern); `continuity-keeper.md` is the one prose-judging agent with no taste-sheet section (CLAUDE.md:139–142 says every one reads it) | RAV4 ruled (B2-D10.4); the keeper's definition unchanged |
| :74 | "door of nine? Where is she?" · :88 the whirlpool · :89 the Magnolia Court | The panel's "too implicit for a listener" list (`ch09-panel-2026-09-05.md:113–118`) named Millrow only; the lint's LEAD NAMES count (chapter-lint:36–37) passed ch 9 with six Dan/Merritt hits while "let him into the room" after Verna still lost the author (:90) | A per-chapter count cannot see a pronoun's antecedent per paragraph; decode is judgment and the list was short | Panel 1.3.0 added "where the POV stands, first sentence per scene"; taste 1 amended |
| :74 | "nothing woven in to the various scenes" | The romance floor: six beats, four kinds, both thirds (`ch09-panel-2026-09-05.md:22`) | The floor counts thirds; the reader feels scenes | The apart test; "Woven, not counted" (STYLE:313–327); BACKLOG opened |
| :79 | "supper … way too 80s country and way too small town" (ch 10 epigraph) | Nothing. The realism rulebook had no out-of-state rule; the modernity check is a word list (STYLE:377–380); the culture-researcher's rulebook ran once (LOG:301, 08-29) | A gap — no instrument judges register realism; the ch 10 audit checked the rulebook's conditions and the rulebook was short | Rule 12; "supper" in the lint |
| :80 | nostalgia for the annex, not her job | The REVERSAL slot priced the building ("the annex's ground", `brief-ch10.md:147–154`); the audit passed it | Nothing asks whose loss a stake is, in her terms; taste 3 already existed | B2-D13; RECENT's abstract-stake ban |
| :83 (#139, ch 11) | the stake "doesn't sound like a big deal" | The brief wrote it abstract (`brief-ch11.md:94–96`); the panel called it "the real stake, plainly" (`ch11-panel-2026-09-07.md:71`) and its TASTE list omits entry 3 (`:173–184` lists 1, 2, 4–12) | The panel's last finding skipped the one entry the author then invoked | Taste 7 amended; RECENT ban |
| :83 | wine night "not playful enough" | The drafter's card D6, "run a beat past comfortable," produced the stillness on purpose (`brief-ch11.md:381–382`); the panel's fun inventory counts laughs per chapter | DECKS rule 3 (a card correlating with a verdict is too strong) has no place to record an author reaction; LOG:377 carries none | Fixed on the page; the LOG row not annotated |
| :83 | the truck — "way too old for that" | None; STANDARDS:87–95 and premise §7 govern how far, not where | A gap | RECENT:35–38 |
| :84 | "the stakes aren't high enough for the pending playoff game" | The card's clock paragraph carried dates and no price (`ch11-card.md:67–68`; `ch12-card.md:91–93`) | The card asked for the clock, not its cost | Kit 12 prices the clock (:27–30); B2-D15 |
| :87 | "just say the QB's name" | The naming full list gave narration "the boy" including her POV (RECENT, pre-amendment) | The rule was wrong, not the check | RECENT:49–53 amended |

**Fix (one line each):** `continuity-keeper.md` gains the taste-sheet
section every other prose-judging agent carries, plus one audit item —
"read the brief's OPENING, ARGUMENT and REVERSAL against the manifest:
does each claim survive the facts, and is each stake a named loss in
the POV's terms"; `romance-reader-panel.md:79–85` — the TASTE finding
lists every entry 1–14 with a hit or "clear" so an omission is visible;
`DECKS.md` rule 3 — the LOG row notes an author comment that lands on
a card's effect.

### F10 — DRIFT + CONTRADICTION: two ledgers for one ban list, and an audit cap that never bound

The per-brief BANNED line restates one list by hand, growing each time:
`brief-ch09.md:209–217` → `brief-ch10.md:206–211` → `brief-ch11.md:
186–192` → `brief-ch12.md:266–272`. `RECENT.md:7–9` says the ledger
appends "what the review flagged"; in the window it gained only the
author-driven bans (RECENT:26–41), while the batch's panel- and
audit-caught tics — "That was the rule" / "That was all of it."
(`ch11-brief-audit:22`), "his voice came down to say it" (`ch10-panel:
75`), the annex shape, the lamp as last image (`ch12-brief-audit:
143–145`), the "Doc." / "Coach." close — live only in reports and
addenda. Two files, one rule; they have already diverged. And the same
agent ruled twice in opposite directions: the ch 11 audit capped the
"Doc." / "Coach." close ("may not land on it a third time", `ch11-
brief-audit:22`); the cap never reached the binding addendum (`brief-
ch11.md:314–325`); the ch 12 audit permitted it ("may recur", `ch12-
brief-audit:74`); the page did it a third time (`ch12:311–313`); the
panel deferred it to ch 13 (`ch12-panel:70–71`). **Instrument:** the
brief template's BANNED line; the audit addendum. **Fix:** the BANNED
line becomes one sentence — "RECENT.md, drafting-assistant, as of
<date>, plus:" — and the fold appends flagged tics to RECENT; the
audit addendum template gets a CAPS line so a finding binds or is
visibly dropped.

### F11 — GHOST: a board handle on no page survived one strike (test-set item 3), and the registry records intent the page does not carry

FirstDownMom was struck from the registry at commit 8297d08 (`book2/
notes/furniture-registry.md:24` now reads "on NO page"), but `book2/
THREADS.md:363` still lists it under "board usernames on record," and
it reached the ch 12 brief's naming roster from the registry (`brief-
ch12.md:253`) before the audit caught it (`ch12-brief-audit:128–133`).
Origin: the wave-1 fold wrote the row from a losing candidate
(`book2/drafts/2026-08-30-wave1/ch04-candidate-C.md`), not the accepted
page — the only file in either manuscript that contains the handle is a
draft. Two more rows of the same kind: `furniture-registry.md:14` "Dan's
Friday check | 4:15–4:45" stands beside `:37` (practice at five, the
check at 5:15) and `ch10:241` — an unretired row; `:66` records "he
hears everything and puts it nowhere" as Peanut's canon, on no page
(`ch11:349–352` says only that the seltzer came before she asked; the
panel left it `[CHECK: author's call]`, `ch11-panel:142, :197`; the
CHANGELOG records it as "kept on purpose", `book2/CHANGELOG.md:710`) —
an orchestrator's choice became a registry row, which the showrunner
charter forbids (showrunner.md:14–15). **Instrument:** the fold's
registry write. **Fix:** `THREADS.md:363` strike the handle; `furniture-
registry.md:14` mark SUPERSEDED by :37; `:66` trim to what the page
says; the registry's Source column requires a `chNN:line` cite (a
narrowing of an existing column).

### F12 — MISCOUNT: the edge ration corrected in one place and not the other (test-set item 4), and four more counts the pages do not support

- `THREADS.md:33–38` now says 4 spent, 6 remain (corrected at the ch 12
  audit); `THREADS.md:351–352`, the ch 11 entry, still says "Edges:
  none spent." The file disagrees with itself; the pages have four
  (`ch04:343`, `ch08:411`, `ch10:167`, `ch11:453`).
- "Somebody's" (once per book): `THREADS.md:91–97` logs ch 1 ×1 and ch 3
  ×2; the pages also have `ch01:294` ("somebody's dropped cocoa") and
  `ch08:159` ("somebody's choice a man could argue with", narration,
  accepted after the ban) — neither logged.
- Anchor lines ("exactly one per chapter"): `THREADS.md:39–46` lists
  ch 1–6 only; the ch 12 audit counted Earlene's third by hand
  (`ch12-brief-audit:162–163`).
- The thread index: B2-T06 and B2-T07 "not yet planted" (`THREADS.md:
  18–19`) while the entries say planted (`:279–280`, `:303–304`).
- "Since June" (lint cap 1 per chapter, chapter-lint:22–23): `ch01` ×2,
  `ch03` ×2, `ch08` ×3 (`:265`, `:328`, `:415`); the ledger's arrival-
  clock row covers ch 2 only (`THREADS.md:71–72`). Q2 quiet band says
  ch 9 = 15.5% (`:48`); the lint says 15.2%.

**Instrument:** the fold. **Fix:** one ledger pass at the ch 12 fold —
conform `THREADS.md:351`, `:18–19`, `:39–46`, `:91–97`; log `ch01:294`
and `ch08:159` as polish debt; either log ch 1/3/8's "since June" or
drop the per-chapter cap from the lint (F15).

### F13 — CONTRADICTION: two laws give the review stack in opposite orders, and the cadence runs neither

DRAFTING-PROTOCOL:51–54: "Continuity → developmental → line." PIPELINE:
224–236 and CLAUDE.md:150–153: structure, then line, "continuity last";
showrunner.md:64–67 the same. In the batch neither ran: brief audit
(continuity, pre-prose) → draft → panel → lint, and no developmental,
line, or post-draft continuity pass on ch 9–12 (LOG:369–382). The
panel's continuity deferrals land on no run — "[CHECK] for continuity,
not mine to rule" (`ch09-panel-rewrite-2026-09-06.md:108`), the jar and
the seltzer (`ch11-panel:196–197`) — and the orchestrator resolved them
(F11). **Instrument:** DRAFTING-PROTOCOL instrument 6; PIPELINE §3c.
**Fix:** `DRAFTING-PROTOCOL.md:51` conformed to PIPELINE's order; §3c
names who answers the panel's `[CHECK]`s — the fold's registry grep,
which the registry header already claims (`furniture-registry.md:3–5`).

### F14 — TEMPLATE (E4, the exits): the batch closes its scenes with one gesture

Of the batch's 21 sections, 13 close on an "and [small physical
action]" tail clause and about 15 on an object put down or picked up:
`ch09:114` ("and she kept it"), `:190`, `:342`, `:477`, `:542`;
`ch10:375`, `:474` ("He put the phone in his coat."), `:509` ("and
turned off the lamp."); `ch11:105`, `:358`, `:399` ("and she put it in
drive."), `:464`, `:487`; `ch12:322`, `:376` ("and put the next play
up."), `:419` ("He set it down face up, and left it that way."). The
endings budget governs chapter endings only (STYLE:61–66); the ch 11
audit counted eight of ten chapter endings flat (`ch11-brief-audit:21`)
and the ch 12 audit banned the lamp (`:143–145`); no instrument reads
scene endings, and the drafter cards govern openings. **Instrument:**
the endings budget's scope. **Fix:** none new — the F3 tool change
prints each section's last line; widen STYLE:61's sentence to "scene
and chapter endings" only if the panel then finds it.

### F15 — OVER-TOOLED: four rules or checks to narrow or retire

- **D7 duplicates law.** DECKS:35 "Open every scene mid-motion; no
  arrivals" is now DRAFTING-PROTOCOL:344–346 ("begins on a THING in the
  room, mid-motion"). A card that repeats a rule adds no variance —
  retire D7 (`studio/agents/variance/DECKS.md`, via the CHANGELOG).
- **A quota nobody counts.** "Three personifications per chapter" rides
  every brief (`brief-ch09.md:218`, `brief-ch10.md:212`, `brief-ch11.md:
  193`, `brief-ch12.md:273`; STYLE:82–83); no panel in the batch counted
  it (the five panel reports contain no "personif") and the lint cannot.
  Drop it from the brief template.
- **WATCHes past their discharge.** The "which"-appendix (RECENT:132–
  137) and sentence-initial "Somewhere" (RECENT:78, STYLE:78) — zero and
  one hits across ch 5–12; RECENT:7–9 says drop after two clean runs.
  Keep the greps (free), retire the WATCH text.
- **A per-chapter cap the ledger does not keep.** "Since June" cap 1
  per chapter (chapter-lint:22–23) — three accepted chapters exceed it
  unlogged (F12). Keep or drop; a cap nobody reconciles is noise.

### F16 — STALE: references that no longer match the room

- CLAUDE.md:18 and :127 say "twelve specialists"; ROSTER lists fourteen,
  and CLAUDE.md's table (:129–142) omits romance-reader-panel, superfan-
  reviewer and gtm-strategist. LOG:383 names "instrument-auditor 1.0.0"
  and no such file exists in `.claude/agents/` nor a ROSTER row.
- AUTHOR-TASTE:281 ("the wave-3 directive (ch 10, ch 12)") and
  `book2/plots/romance-arc.md:153` ("The wave-3 directive (ch 9–12) is
  written to stage 3") cite a file that was never written (`plots/`
  holds wave1 and wave2 only; AUTHOR-NOTES:73).
- AUTHOR-TASTE:333 "Last review: 2026-09-05" while entries 1, 5, 6, 7
  and 8 were amended 09-06/09-07; entry 8 carries a duplicated "Caught:"
  block (:203–216).
- DRAFTING-PROTOCOL:3–5 still reads "PROPOSED 2026-08-04 … locked when
  the author blesses it" while every brief cites it as law.
- PIPELINE:248–258 "Current state" lists three books and not the one in
  production.
- DECKS rules are numbered 1, 2, 3, 4, 5, 7, 6 (:8–23); kit 11's parts
  run 1, 1, 2, 4, 3 (`studio/series-kit/11-arc-docs.md:37–84`).
- showrunner.md:92–96 says the showrunner is "variance-EXEMPT"; LOG:277
  records it drawing A10.

**Fix:** one housekeeping PR (`studio:` and `agents:`) — the counts and
the table; the two wave-3 cites; the taste footer and duplicate; the
protocol header; the pipeline table; the deck and kit numbering; the
auditor's file and roster row.

---

## What landed from the last audit

Nothing to report: this is the first run and `studio/agents/audits/`
did not exist before it. For the next audit, the proposals above that
would show as landed are F1 (the listening file), F2 (STATE's ch 13
line), F6 (the lint's exit), F7 (the build check on stage openings),
F11–F12 (the ledger pass), and the F16 housekeeping PR.

## Verdict

The room is good at catching facts before prose exists — the four brief
audits in this batch found a hundred-year error, a closed market, a
Saturday practice that could not happen, and a truck that was the wrong
truck, and none of those reached the author. It is good at counting
what it has been told to count. What it cannot yet do is see two
chapters at once: every instrument reads one chapter, so the author was
the first to notice three openings were the same paragraph, and the
seams of these four chapters — the Mule, the house, the check, the
annex across the lot — are already the same sentences waiting to be
noticed next. Two things would embarrass it soonest. The listening file
the author hears has been quietly dropping lines of the card in every
chapter of this batch, so the "standing review before every chapter
read" is not what was written. And the hand-forward for chapter 13
still says one drafter, the day after the author agreed set pieces get
three.
