# KEEPER — sameness-pass page audit, ch 1/3/5/6/9/10/11/15/17/18 (2026-09-22, E4)

continuity-keeper, card E4 (watch transitions: how scenes are entered
and left). The page audit PR #183 merged without (BACKLOG F61). Scope:
the 21 hunks of the 2026-09-16 sameness pass and register seed, read
in place on disk with surrounding page, against canon/FACTS.md,
book2/canon/REGISTERS.md, THREADS.md, DECISIONS.md (B2-D03, D10.4,
D18.1, D21.9, D23.5, D25.1), STYLE ("The establishing line"; "Rules
are full lists"), RECENT (the calendar-opening ban; RECENT has no
continuity-keeper section, so no banned moves this run),
AUTHOR-TASTE. No file edited; no shell. E4 conflicted with nothing.

Two notes on the inputs. (1) The patch as given carries manuscript
hunks only — ten files, 21 hunks; the REGISTERS.md edit the brief
names is not in it. REGISTERS.md on disk (l.43–50) shows the 09-16
seeding; what the default row read before 09-16 is `[TK — not in the
patch; the 2026-09-14 ch 19 fold logged "the drinks row corrected to
sparkling water," and the row now reads sparkling water|seltzer]`.
(2) The CHANGELOG entry "Mechanical only. No story, no beat, no line of
dialogue changed" covers the sameness pass; the register seed under
it added one line of dialogue to an accepted chapter (ch 3:336).

## The hunks

| # | Ch | Lines | Ruling | Evidence |
|---|---|---|---|---|
| 1 | 1 | 78–79 | CLEAN | dash to period; nothing moved |
| 2 | 1 | 90–93 | CLEAN | dash to comma; the verb series still reads; her hands first (SR-B2-16) intact |
| 3 | 1 | 235 | CLEAN | E4: a scene entry after `***`; the band, Millrow, the square still establish |
| 4 | 1 | 246 | CLEAN | dash to comma; flatbed at the courthouse steps, her table across the square — unchanged |
| 5 | 1 | 261–262 | CLEAN | dash to period; "stood still" pre-existing (stillness as tell, SR-B2-15) |
| 6 | 3 | 56–58 | CLEAN | dash to period; the repeat-and-extend shape pre-existing (RECENT watch) |
| 7 | 3 | 93–95 | CLEAN | dash to comma; the hit's second half unchanged; clock anchors 18:10/15/22 untouched |
| 8 | 3 | 270–273 | CLEAN* | the pair's OPENING dash became a comma; the CLOSING dash (l.272 "all week —") now has no opener. Mechanical — X1 |
| 9 | 3 | 335–336 | FACT | staging: she is not indoors. Verna "had the storm door open before Aisha was out of the car" (l.328–329), "holding the door with her hip" (l.332), "frowned out at the lot" (l.341); "carried IN from the car" puts Aisha inside a room she has not entered. Also the word (B2-D23.5) and a new dialogue line — X2 |
| 10 | 5 | 133–134 | FACT | the word (B2-D23.5) — X3. New canon: the Checkerboard stocks none. Not contradicted after ch 6: ch 17:163 Aisha takes coffee there; ch 22:426 and 24:327 the water glass is Dan's; ch 12 coffee self-serve |
| 11 | 6 | 108–109 | FACT | the word (B2-D23.5) — X3. Staging clean: the can never reappears, the plate does (l.199, 298), no hands on the rail for her; Dan's POV learns it, so ch 18:525 "I've seen what you drink" holds |
| 12 | 9 | 21–26 | CLEAN | E4: still mid-motion on the tape gun; "she had the records room at the cold end" still locates; Saturday said l.24; RAV4 l.33 (B2-D10.4). The ch 5 architecture (halfway…/finished the…) still rhymes by ear; the tool's four-word test is met — not mine to rule |
| 13 | 10 | 34 | CLEAN | "safe" survives as the county's word; the chain ch 8:24–25 (plant) → ch 15:45 "the word the county had wanted out of her all fall, safe" (payoff) is intact; no THREADS row makes the ch 8/10 echo a motif. Ch 10:20's calendar first line is pre-existing and spent-closed (RECENT) |
| 14 | 11 | 21–29 | VOICE | the chapter now opens on "She"; Aisha is first named at l.114. STYLE, the establishing line as amended #153 ("It just starts with saying 'she'"). E4: still mid-motion on the sheet; Friday's date, eight days, 5:15 nightly (F-CHK-02) intact — X4 |
| 15 | 15 | 19–21 | CLEAN | E4: mid-motion on the pen; warm end, ten past seven; THREADS ch 15 ("pen out of the parka's inside pocket… whole name on a printed form") intact |
| 16 | 15 | 40, 44 | CLEAN | tense only |
| 17 | 17 | 25–26 | CLEAN | E4: the RAV4 (B2-D10.4) in the first clause; the square; "the twenty-first" l.35 |
| 18 | 18 | 29–30 | CLEAN | "Same as the night before" = Saturday the 26th on foot from the Fieldhouse (ch 17; B2-D18.1); keys into the jacket at nine — the walk-down mechanic (THREADS ch 18) intact |
| 19 | 18 | 77–78 | CLEAN | ch 17's "the chair and the bed" echo intact; the Verna-light formula pre-existing (banned later, RECENT) |
| 20 | 18 | 446–447 | CLEAN | the counter he eats at = ch 2:395; the two chairs pay at l.549–551 |
| 21 | 18 | 543–545 | CLEAN | the jelly jar (B2-D21.9; registry 149); Dan's wine spend (REGISTERS ch 18) intact |

## The seltzer seeding

- **Is it a register item?** Yes — REGISTERS "Aisha — the drink,"
  default `sparkling water|seltzer`, established by ch 3/5/6 (seeded
  2026-09-16), spend ch 11 (wine). The row matches the manuscript:
  ch 3:335, 5:133, 6:109 carry the word; ch 11:350–355 carries the
  jar then Peanut's can.
- **The word.** B2-D23.5 (author, 2026-09-14): "Her drink in public
  is sparkling water, not a drink. 'Seltzer' was ambiguous (alcoholic
  seltzers exist); the page says sparkling water." The three seeds
  were written two days after that ruling and use the word the author
  called ambiguous. Contradiction with a ruled decision — X3, X2(b).
  The register-check regex accepts either word; the fix costs the tool
  nothing.
- **Ch 5 is a mention, not a use.** "Had never stocked seltzer… so she
  drank the coffee" names the default by its absence. `register-check`
  counts the word; the spec's rule 2 asks for ordinary USES. On the
  page the default is carried by ch 3 and ch 6 (and ch 11:352 after
  the jar). For the tool's owner; not a block.
- **After ch 6, nothing contradicts the ch 5 claim.** No page puts a
  can in front of anybody at the Checkerboard (ch 12, 17, 19, 22, 24
  checked); ch 17:163 has Aisha's cup filled there, which agrees with
  ch 5.
- **Pre-existing debt, not this pass:** "seltzer" stands on accepted
  pages that predate D23.5 — ch 11:352, 16:284, 17:332, 18:50/453/
  519/523 (18:523 is dialogue). STYLE "Rules are full lists": debt
  logged at the fold, never silently rewritten. The author's call —
  sweep or forward-only, the same shape as D26.4's open question.

## CONFIRMED (no action)

- E4: no scene EXIT was touched. Two scene entries were (ch 1:235,
  ch 3:269–270); both still say where and what within three lines.
  All four recast openings still land mid-motion on a thing (tape
  gun, sheet, pen, RAV4); the calendar-opening ban is not tripped.
- Clocks: ch 11:26 "Eight days" = Fri Dec 11 → Sat Dec 19; ch 15:25
  Thursday the seventeenth; ch 18 Sunday the 27th at nine. Ch 11:32
  "the fourth since Monday" reads either way (Mon–Fri is five checks
  if Monday's counts) — pre-existing, not this pass.
- No name, age, place or COUPLES-row line was changed in any hunk.
- The ch 8/10 "county wanted to hear" echo is not a THREADS thread;
  breaking it drops no plant.

## New canon this pass establishes

- The Checkerboard does not stock seltzer / sparkling water, and is
  not going to (ch 5:133, Aisha's POV) → furniture registry row.
- Aisha keeps a can in the RAV4 and brings it in at night
  (ch 3:335) → registry, under her drink.
- The drink default now on the page before its spend (REGISTERS row
  already carries it).

## Open markers

None in the 21 hunks. `[TK — REGISTERS.md pre-09-16 default row]` is
mine, above, not the page's.

## AUTHOR-TASTE risks (last finding)

Entry 1 (the establishing line — ch 11 opens on "She"); entry 5
(modern, not campy — a diner that "was not going to" stock seltzer,
and "Set on the rest." in the modern lead's mouth, both read as the
country register the author retired); entry 9 (don't make it perfect
— a mechanical pass over ten accepted chapters is the polish the
author warned against; nothing in it was a measured failure of a fact).
Entry 6 (no phrase becomes a tic) is what the pass served.

## VERDICT: RE-ACCEPT EXCEPT

Re-accept hunks 1–7, 10*, 11*, 12–21 as they stand (*10 and 11 with
the one-word fix in X3). Exceptions, fixes proposed, not applied:

- **X1 — ch 3:272 (hunk 8), mechanical.** The comma at l.270 opened
  an appositive that the dash at l.272 closes. Make the closer a
  comma too ("all week," — the appositive then reads
  comma-to-comma), or restore the original dash pair (the
  double-dash budget in RECENT argues for the comma).
- **X2 — ch 3:335–336 (hunk 9), FACT.** (a) The line must put the can
  in her hand without putting her indoors: she is at the car or on
  the walk to Verna's door, not "in." Drop the "in" or name the car
  as where the can came from. (b) "seltzer" → "sparkling water"
  (B2-D23.5). (c) "Set on the rest." is new dialogue in an accepted
  chapter and a stranger cannot repeat what it means; either she
  declines both offers in plain words, or the line is cut and the
  lift of the can does the declining. (d) l.338 presses the clamshell
  "into Aisha's hands" with a can in one of them — a free hand, or
  the can goes down first.
- **X3 — ch 5:133 and ch 6:109 (hunks 10, 11), FACT.** "seltzer" →
  "sparkling water" in both (B2-D23.5). The REGISTERS regex already
  accepts the phrase; `register-check.py` result unchanged.
- **X4 — ch 11:21 (hunk 14), VOICE.** The first sentence names her.
  On the tool's distribution name-first goes 4 → 5; the establishing
  line is law and the distribution is not. Restoring the original
  object-first line is the other acceptable fix.

KEEPER: FACT 3 (hunks 9, 10, 11) · VOICE 1 (hunk 14) · mechanical 1
(hunk 8) · CLEAN 16 · THREAD 0 · TRANSITION 0 · TK 0 on the page

## Showrunner's note (2026-09-22)

The four fixes are page edits on accepted chapters and wait for the
branch to be free of prose (one open PR at a time; #182 is open).
They go in the ch 24 fold with their own CHANGELOG rows, and the
"seltzer" sweep-or-forward-only call goes to the author with the
ch 25 DECISION PR.
