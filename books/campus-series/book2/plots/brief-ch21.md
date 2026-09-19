# Brief — Chapter 21: "Rides Home" (Aisha · Wednesday, January 13 → Thursday morning) — THE ICE STORM (B2-D19)

**Status: SET PIECE** — three blind drafters (D2, D5, D3 — LRU), the
scoreboard, the author reads only the winner, no grafting. The card
(`notes/cards/ch21-card.md`) and this brief are audited TOGETHER (E6)
before the card goes to the author. The card is canon for this chapter
once the author says go. A brief without its audit addendum is not a
brief (drafter rule 8; the brief gate on the launch).

**TARGETS (the definition of done, set before the draft — B2-D25.5):**
Romance 7 · Heat 5 · Aisha 2 · Dan 1 · Wound 2 · Fun 1 · Town 2 ·
Menace 0 · Ends up · Talk quiet · Words 3500 · Pays Aisha (the
`canon/TARGETS.md` row 21, copied). The panel scores actuals against these; a romance level
two or more under 7 holds the chapter (`targets-check.py`). Heat 5 is
a ceiling: a deliberate touch with no errand, in the cab, and nothing
past it.

## PROOF OF DONE — campus 1.2 ch 21, 2026-09-18 (chapter-proof; filled at the end)

MECHANICAL (commands, output attached at the end)
  [ ] chapter-lint.sh (each candidate)      → opening PASS; SENTENCES 0 over thirty; no volley
  [ ] dialogue-lint.py                       → quiet band (8–15%)
  [ ] opening-check.py                       → PASS; the seams read (not ch 13's bike line, not ch 19's counter)
  [ ] fact-check.py                          → clean
  [ ] prose-guard.sh (fires on the write)    → silent
  [ ] ai-tells.py                            → no outlier
  [ ] romance-build-check.py                 → PASS (row 21 held, 4/4, no spend)
  [ ] targets-check.py (in the accept gate)  → romance actual within one of 7; heat ≤ 5
  [ ] accept-gate.sh                         → PASS with the panel, the keeper and the scoreboard on disk

READERS (verdict files)
  [ ] romance-reader-panel 1.5.6 ×3 (blind) → notes/ch21-panel-{A,B,C}-<date>.md, each with an ACTUALS line
  [ ] the scoreboard                          → notes/ch21-scoreboard-<date>.md (a competition requires it)
  [ ] continuity-keeper                       → the card+brief audit in this file; the page audit at the fold before ACCEPTED
  [ ] superfan-reviewer                       → not this chapter (the 17–20 block read is running; the next block is 21–24)

MUST NOT HAVE CHANGED
  [ ] Trey never speaks and is never the point of view (STANDARDS R1, the offstage mechanic; ch 13's staging is the precedent — on the bike, hood up, his back to her)
  [ ] the rung ladder: In 4 / Out 4; no kiss, no garment; the touch in the cab is hands, once, and the page says nobody could see it
  [ ] no stranded night, no power out, no rescue (B2-D19.3); the terms hold; "after signing day" said as the date
  [ ] no new fact, name, date or object not on the page — the trainer unnamed; the consultant absent; no street named for his house or the trainer's; no salt truck named (town TK)

VARIANCE
  [ ] cards drawn: D2, D5, D3 (LRU) — logged; three blind briefs identical
  [ ] banned moves read: RECENT.md as of 2026-09-17 + this brief's BANS + the addendum's BANNED line

**Outline entry, verbatim manifest** (`plots/b12-outline.md:669–695`):
"Trey's re-eval: real progress, documented, unhurried — and she does
the thing nobody asked: builds his return-to-play portfolio for the
scouts, protecting the boy's draft stock THROUGH the caution instead
of despite it (F12 — Missy watches her do it; the thaw starts here,
on the page). The ice storm the board has been forecasting since ch
20 comes in behind the re-eval: the hill glazes by dark, the town
shuts, and the RAV4 cannot get down Millrow. His F-150 can, and he is
the last one up the hill. He drives whoever is still in the buildings
down to the square — the trainer first, her last, to the motel, the
truck in Verna's lot for the minutes it takes. Nobody broke the rule.
Vaguepost 2 lands the next morning with only her in the cab:
'interesting to see who gets rides home from the facility these days'
(rulebook's permitted form, aimed) — and the two-door truck that
cleared them at ch 13 is the truck the county now puts her in (RH1
read the other way; fair play). The storm costs and never rescues: no
stranded night, no power-out intimacy. They hold; the 'after signing
day' date is three weeks out; hope is the chapter's engine and the
reader's dread (superior position: the photo already exists). —
Plants: F12. Pays: the protocol's honest arc (her call aging into
visibly right); the forecast planted at ch 20; engine row 11 (weather
forces the thing). ANCHOR (Verna): healing is the one thing in this
county that won't hurry for football. End: ache-hope."

**B2-D19, binding** (`DECISIONS.md`): one weather event in 1.2, the
Deep South kind — the town shuts for two days, the hill glazes,
nobody drives; what it forces is the ride; the storm costs and never
rescues; planted at ch 20 (the epigraph, "midweek next week") and the
county's one salt truck or its absence is a town fact `[TK:
town-ashford — who salts Millrow]` — the page does NOT name a truck;
the day defaults to Wednesday the 13th into Thursday the 14th and the
CARD LOCKS IT (call 1); the trainer dropped first (call 2); Verna at
her window, never a word (call 3).

**Format:** Aisha, third limited, past tense. **Length:** ~3,500 (a
set piece; ±15% is on target). **Day:** Wednesday, January 13, from
the re-eval in the afternoon to the ride after dark, and a short last
section Thursday morning, January 14, at room nine. Ch 20 was Friday
the 8th (his). The window shuts Thursday the 14th (ch 22, Dan's, is
Thursday — Coach's Table round two; the roads still bad). The terms
end Wednesday, February 3 — three weeks; "after signing day" is
Dan's phrase for that date (ch15:363 "So it's February"; the card
says three weeks). Never "the eleventh" (the annex memo, Feb 11 —
four weeks; hers, not this chapter's business unless one clause).

## THE ROMANCE MOVE (first line)

Stage 4 held, In 4 / Out 4 (`plots/romance-arc.md` row 21: "A photo
exists; the ice storm puts her in his truck"). No new rung. What this
chapter does to the feeling: the weather forces the one thing the
terms never allowed — her in his truck where the town can see — and
they hold anyway, and it is the holding that aches. Hope is the
engine: three weeks. Earned by: ch 15 (the terms; the firewall), ch
20 (the rule kept at his table, the hand held and taken back).
Nothing spent. Build check: PASS (pasted in the audit).

## THE LEADS' SCENES (the floor)

One scene together: the cab of the F-150, from the Fieldhouse lot
down Millrow to the square (the trainer in the cab), then to the
Magnolia Court's lot (the two of them, call 2). Floor: 900 words from
her getting into the truck to her door shutting behind her. Her face
and his at every turn — his in the dash light, hers in the hood. The
talk is small and true: the road, the trainer's house, the date. One
awkward beat: three across a bench seat. HEAT 5, THE CEILING: in
Verna's lot, with the engine running and the minutes it takes, his
hand over hers on the seat, or hers on his, deliberate, no errand;
the page says once that nobody could see it. Nothing past it. Her
body answers before she decides (kind 9, STANDARDS 27) — the cab is
where. The last exchange in full sentences: the date, said as a
date. Then her door. APART, WHY: the terms; three weeks; said once.
The chapter's last section is hers alone (Thursday morning, room
nine, the tablet) and THINKS: about the ride, and what she fears (the
post; a county that reads a truck), and comes back to him — on a
thing (his glove on the seat, the tire tracks in the gravel, the
date), not a verdict. ENDS UP: hope.

**WOVEN:** he is in every scene of hers. The re-eval (his quarterback,
his rule at the door — "not you," ch 13); the file (his player's
future; what he cannot ask about, ch 20); the ice (the truck she
knows has two doors); the ride; the post.

## THE OPENING, SAID

Wednesday afternoon. The thing in the room, MID-MOTION: NOT the
number on the tablet (ch 13's opening line shape, "The number had sat
at one thirty-one" — BANNED as a shape); NOT the counter (ch 19); NOT
the RAV4 taking a space (ch 17); NOT a pen or a step count (ch 15);
NOT Sonny's trowel (ch 13); NOT the truck keys (ch 18). Candidates:
Missy's chair carried out of the office into the hall; the chest strap
in her hand before it goes under a hoodie; the sky over the practice
field going the color the board promised. The first paragraph SAYS
Wednesday the thirteenth of January in words a listener keeps (STYLE,
"after a jump" — ch 20 was Friday the 8th); NOT a calendar first
line; the clock-and-stool WARN says a face before a clock. The
stranger's sentence: *On the Wednesday the board had promised ice,
Aisha put Trey on the bike for the check she owed his chart, and the
ice came in while she was typing it.* (Twenty-seven words.) The
paragraph locates:
where, when, what is in her hand, who is in the room.

## THE ARGUMENT, SAID

*She wants the boy's way back built through the hold so nobody can
say the hold cost him. The county wants a reason to put her in his
truck. The weather gives it one.* Between the leads: *he wants to
drive her home because nobody else can. She wants not to be seen in
his truck. She gets in.*

## THE SCENES

1. **The re-eval, the annex, afternoon** (the opening). The quiet
   room's bike (registry 86: the annex's own bike, one chair, the
   chest strap paired to her tablet, the cap one-forty — "seventy
   percent of what August measured," twenty minutes, she asks at
   four, eight, twelve). TREY IS ON THE BIKE AND NEVER SPEAKS, hood
   up, his back to her (ch13:111–118 — the precedent; STANDARDS R1;
   dossier-dan walls: "Trey is offstage absolutely"). The trainer at
   the door (registry 78; ch20:232 "I'll be in the room"). MISSY IN
   THE HALL on a chair from the office with the notebook on her knee
   (ch13:121–123 — the precedent). WHAT THE BIKE IS IN JANUARY (audit item 9, binding): NOT "the
   next step." The ladder is six rungs (ch05:231–246: two is the bike;
   five is full practice); the last sheet was "Step four. Holds
   overnight." (ch16:447, Dec 18); and there is no practice till
   spring workouts (ch20:240–243), so there is nothing to climb into.
   The bike today is a RE-EVALUATION UNDER LOAD — the check she owes
   his chart before there is a practice to put him in. The page says
   that once, plainly. "Real progress" is measurable and NEW: the
   full twenty minutes at the cap against December's fourteen
   (ch13:139–151). "Not cleared" means nothing exists to clear him
   into, and no page before ch 30 clears him. The trainer's place:
   "I'll be in the room" (ch20:232) or at the door (ch13:120) — pick
   one in the establishing line. The numbers are NEW and hers; the tape on her wrist
   (ch 13); typed standing before said (ch13:147–153). Missy's
   notebook order stands (registry 105: "What step does it say he's
   on." / "The step, then the rest."). NO "Wednesday" written by
   Missy this time — a different word. Missy's face: ch13:172–173
   ("did not do one thing Aisha could have charted") — do not repeat
   the sentence. Trey down the corridor ahead of the trainer. MISSY
   DROVE HIM (Trey has no car on any page; "His mother drives him,"
   registry 37, 106; her car ch15:50, ch17:269): they go down the hill
   before it glazes, one clause. Her every line on the page: ch04:178–
   179; ch13:159, 164; ch15:69–70; ch16:230; ch17:269–270 (a nod, no
   thank you). "Thaw" is Dan's word (ch04:193) — never in her POV.
2. **The file a scout could read (F12)** — her office, boxed since
   the 5th (ch20:350–351; registry) — one desk left, the tablet on it. The thing nobody asked: she starts Trey's
   return-to-play file for the scouts — both scans (ch05:70–78, her
   own order), the tape times, every step of the ladder in her
   typing, dated, the hold shown as the reason his brain is worth
   drafting and not the reason it isn't (ch17:240–247 is the spine:
   the chart she sent to Birmingham). ROOTING FOR, before the first
   romance beat: costs her the evening and the board's reading
   ("benching him while she builds his stock" — dossier row 21); seen
   by Missy, thanked by nobody. MISSY WATCHES HER DO IT — the thaw
   starts here, on the page, SMALL: Missy in the door or the hall,
   sees the file on the screen, asks one plain thing or asks nothing
   and does one thing (brings the chair back in herself; stays a
   minute longer than she has to). Missy's register: ch 4, 13, 15, 16,
   17 — short, level, a pen; she does not thank; she does not
   soften in a sentence. "Scout" / "the scouts" / "draft" are NEW talent
   words (on no page yet; ch 19's "agents" is the nearest); one
   clause says what a scout is (taste 1). THE WALL (audit item 17):
   Birmingham needed a release in Missy's hand (ch17:258–267); no
   scout has one — she builds the file and puts it in Missy's hands or
   keeps it; she may NOT send it anywhere. Verna's towels are
   Saturday's (registry 54) — not today.
3. **The ice** (late afternoon into dark). The sky the board promised
   (ch 20's epigraph, "midweek next week" — the promise pays; taste
   17). The hill glazes by dark; the town shuts (the Checkerboard's
   one cook — open or shut is unestablished; say nothing or say
   once); the annex's corridor and the Fieldhouse lot; the RAV4 at
   the annex's warm end (ch12:192–193) cannot get down Millrow. THE
   HILL, RIGHT WAY UP (audit item 10): going up from the square —
   Delmar's at Millrow's low end, the stadium's north side, then the
   annex and the Fieldhouse lot at the TOP of her drive (ch17:59–64
   "At the top the lot between the annex and the Fieldhouse";
   ch16:215–217), and the House above (registry 58); the square and
   the Magnolia Court at the bottom (ch18:27–32; ch12:92). WHY THE
   RAV4 STAYS AND THE TRUCK GOES (audit item 5): a person's reason,
   not a machine's — he has gone down that hill every winter night in
   the dark (ch18:29–30; ch19:305); she has driven it in daylight
   (ch17:59–64); said once. PROHIBITION: tires, drive train,
   four-wheel, weight (registry 13: no gears, no transmission talk);
   never that she has or has not driven ice (her history is TK). NO SALT TRUCK NAMED: the page may
   say nothing has been down the hill, not who owns the truck that
   didn't come (`[TK town-ashford — who salts Millrow]`). Who is
   still in the buildings: the trainer; her; Dan up at the Fieldhouse
   (the last one up the hill — his truck in the Fieldhouse lot, ch
   18/19). THE STAFF SENT DOWN BEFORE DARK, said once (audit item 2 —
   the Fieldhouse has staff by day in January, registry 153, ch19:46,
   ch20:199–226). WHY THE TRAINER RIDES (item 1): his car, house and
   street are on no page — the page says once why a man who drove up
   does not drive down (his car stays up the hill like hers, or he
   came up without one); no street, no make. Nobody else is in either
   building, said once. Trey and Missy are GONE before dark (Missy
   drove; one clause). The kid thirty-four: not here (nothing scheduled in
   January). Dan comes across the lot on foot to the annex door, or
   the truck comes to the annex's warm end — either; ch 14's truck at
   the cold-end door is spent furniture, say it differently.
4. **The ride** (the floor). The F-150, two doors, a bench seat (ch
   12/registry 79 — "two doors since he got here"; the cab's inside
   is on no page: NEW, plain, a bench, the heater, the dash light).
   Three across: the trainer in the middle or by the door — one
   awkward beat. Down Millrow on ice, slow, the truck can do the
   road (the RAV4 could not — said once, plainly, why: the hill, the
   tires, whatever the page knows; do not invent four-wheel drive
   unless it is the plain reason and said once). The trainer first
   (call 2, default): dropped at the bottom of the hill at the square,
   one clause on where without a street. Then the two of them for the
   last minute to the Magnolia Court. HEAT 5 in Verna's lot: the
   engine running, the minutes it takes, the hand — deliberate, no
   errand, and nobody could see THE HAND (the page says so once; the
   clause attaches to the hand, never to the truck). THE TERMS AND THE
   RIDE (audit item 18, binding): "a coach's two-door pickup in Verna
   Poteat's lot at night was a thing anybody could see" (ch18:40–41,
   his own reading). "Nobody broke the rule" is the couple's reading
   and the page earns it once in her head: the trainer in the cab for
   the hill, the weather, the minutes — and the truck in the lot is
   still the thing anybody could see. That is the cost, not a break. The date:
   he says it — "after signing day," February, three weeks — as the
   thing they are holding for. He does not get out (dossier row 21,
   seen: they hold). Her door. VERNA AT HER WINDOW (call 3, default):
   the office light (ch18:425–426 — "Verna's office light was on
   across the gravel until eleven, and she never said a word about
   it"); she never says. NO stranded night, NO power out, NO "come
   in" (B2-D19.3, binding). The truck's tracks in the gravel (a
   thing for the ending). Verna's anchor — where: at the window as
   Aisha comes in, or Thursday morning — ONE anchor, hers, her third
   (ch 3, 15): healing is the one thing in this county that won't
   hurry for football — in Verna's words, said once, no reply.
5. **Thursday morning, room nine** (short; the last section). The
   hill still glazed; the annex shut; nobody drives (B2-D19.1 — two
   days). SIX O'CLOCK, her boots on (ch13:63–64; ch17:295 — her habit;
   never seven). THE RAV4 is up the hill at the annex's warm end, and
   the space in front of nine is empty when Verna's light comes on
   (audit item 3) — one clause. MISSY'S SEVEN O'CLOCK PAGE (item 4):
   the photograph of the notebook page arrives every morning after a
   check (ch05:55–62; ch13:91–97; ch17:239) — it comes, one line above
   the county's, and says the twenty held overnight; or the page says
   once why it does not. The tablet, the board: VAGUEPOST 2 — "interesting to see
   who gets rides home from the facility these days" (the outline's
   words; the rulebook's permitted form; aimed) — under a handle not
   seen before, or a known one; no photo (B2-T05 is ch 23's, and the
   reader's superior position is the reader's — her POV cannot know
   the photo exists); the board's pairing has been ambient since ch
   3 and 5 (the sweep's constraint 1) — one clause may lean on it.
   RH1 READ THE OTHER WAY, FAIR PLAY (F7): the crew cab cleared them
   in December because Coach's has two doors (registry 79, Earlene
   relayed); the two-door truck in Verna's lot last night is the
   truck the county now puts her in — she may think it in one plain
   sentence. She holds. The date, three weeks. ENDS UP — hope, on a
   thing: the tracks in the gravel, or the glove, or the date. The
   last section thinks and comes back to him (STYLE (c)).

## ROMANCE BEATS (one per scene, at least three, two kinds)

Scene 1 — kind 4 (his quarterback; his rule at the door). Scene 2 —
kind 6 or 7 (his player's future built by her; the thing he cannot
ask about). Scene 3 — kind 4 (the last one up the hill). Scene 4 —
kinds 1, 2, 5, 9 (the cab; his face in the dash light; the hand;
her body answering before she decides). Scene 5 — kind 8 (the
private admission; the post read and held). Awkward beat: three on a
bench. The panel's count stands; the ACTUALS line goes in each
panel file.

## REVERSAL — who loses what

Aisha loses the one thing the terms bought her: nothing anybody can
see. The county has seen her in his truck, and she chose the truck
(PAYS Aisha). Dan loses nothing yet; he gains the county's eye. Missy
loses a little of her certainty (the thaw). The storm costs; it never
rescues.

## ARC BEATS

**Aisha (dossier row 21):** the file for the scouts on her own
evening, through the hold — the thing nobody asked; Missy watches;
costs her the board's reading. She reads a scout's sheet (row 21).
**Dan (dossier row 21, seen):** they hold; the "after signing day"
date in his mouth. **Missy (F12):** the thaw, small, on the page.
**Boyd:** absent; the survey's chalk on the Millrow curbs may be
under the ice (ch17:59–60; town file), one clause at most.

## THE STAKES, THIS CHAPTER'S

The book's goal is said whole at ch 8 (cited). This chapter's risk, in
her terms: a county that reads a truck; the hold aging into visibly
right (the numbers) while the one thing the terms protected — nothing
anybody can see — is spent by weather. Three weeks.

## COUPLE LINE

Together once, in the cab, in public and unseen. Rung held. The rule
kept, and the county sees it anyway.

## END REGISTER: UP (ache-hope). Ch 20 ended down, on the chair.

Hope is the engine and the reader's dread. Not wry; not a "she wanted
him" paragraph; on a thing.

## ROOTING FOR

**Aisha:** the file, before the first romance beat; seen by Missy;
thanked by nobody. **Dan (seen):** the trainer driven home first,
unasked; the last one up the hill; seen by the trainer and her;
thanked by nobody, and she does not thank him for the ride.

## NAMING, FULL LIST

Narration (her POV): "Dan" (spent since ch 13); "Dan Merritt" once.
Aloud with the trainer in the cab: "Coach" / "Doc" (Dan's sole
use of "Doc" — NAMES.md). Alone in the lot: "Dan," allowed, once,
NOT the one-word "Dan." line (ch 19, spent). Trey: "Trey" / "Trey
Gault" in HER POV narration and to Missy (RECENT's full list — she is
the doctor, she uses his name); the trainer says "7" or "the boy"
(NAMES.md — "Trey" in the trainer's mouth is the author's open call,
B2-D25.6; do not spend it). Missy: "Missy" / "Missy Gault"; Denny by
name if mentioned (at work). The trainer: "the trainer" (`[TK name —
none on any page]`). Verna: "Verna" / "Verna Poteat" once. The
athletic director: never "the AD"; on no page today. The scouts: "a
scout" / "the scouts"; no team, no name. The board: "the board";
Grapevine once at most.

## FURNITURE, CITED

The quiet room and the bike (registry 86; ch13:111–118); the cap
one-forty, the twenty minutes, the asks at four, eight, twelve; the
tape on her wrist (ch 13); the trainer at the door (registry 78);
Missy's chair in the hall and the notebook (ch13:123–125; registry
105); the rehab rooms (registry 55); her office boxed since the 5th
(ch20:350–351); the chart to Birmingham as the file's spine
(ch17:234–253); both scans (ch05:70–78); the RAV4 at the annex's
warm end (ch12:192–193); the F-150, two doors (registry 79; ch18:24–
27 the Fieldhouse lot); Millrow (climbs from Delmar's end at the square to
the House; the annex and the Fieldhouse lot at the TOP of her drive —
ch17:59–64, ch16:215–217); the Magnolia Court at the bottom of the hill
(ch18:30–31), the gravel lot, the office light (ch18:425–426), room
nine (registry 10, 135); Verna's blanket, the furnace that runs
behind under a north wind (registry 135 — the storm's wind may be
north; the furnace may run behind, one clause); the board's
"midweek next week" (ch20:16–18); the vaguepost form (ch 12; the
rulebook); the two-door signal (registry 79; F7); the survey chalk
(ch17:59–60). Verna's anchors: ch 3, 15 (this is her third).

## BANS AND BUDGETS

- Sentences END (STYLE (a)): under thirty; at most three "and"s; no
  one-sentence paragraph. Hand count and report the five longest.
- No mystery-making (b): the post is a post; the file is a file.
  Jokes understood (c). Apart-why said (d).
- ONE anchor (Verna, her third). Edges: Aisha may swear ONCE (3
  remain); not at the wheel.
- Calendar: "Wednesday the thirteenth of January" in the first
  paragraph; "Thursday" for the window and the morning; "three
  weeks" / "after signing day" / "February" for the terms; never
  "the eleventh"; never "signing day" as a page's noun outside Dan's
  phrase.
- Trey never speaks; never his POV; never "the boy" in HER
  narration.
- No stranded night; no power out; no "come in"; no rescue.
- No salt truck named; no street for the trainer or his house; no
  four-wheel-drive unless said plainly once as the reason.
- BANNED: RECENT.md as of 2026-09-18; "The number had sat" (ch 13's
  shape); "the next step" for the bike; "the annex at its low end";
  Verna's "I had a man once who'd have…" shape (ch 13, 15 — no
  third); "the next sixty years" (her ch 15 anchor); "her face did not do one thing Aisha could have charted";
  "It meant something now"; the coat-and-wind exit; the one-word
  "Dan."; "Beer again" and any drink explained; "somebody's"; "never
  once"; "one beat"; "plainly" more than once; the half smile (his
  view; not hers); any sentence quoted as an example in the audit
  addendum.
- BANNED (the superfan's block read, 2026-09-18): "the first Wednesday
  in February" (say "three weeks"); "in plain words, because that was
  how she thought"; "timed and short and finished"; Verna's light "on
  till eleven and never a word" (Verna at the window is seen, once, in
  fresh words); no alone-under-a-lamp ending (this one is a MORNING,
  on a thing); no Boyd doorway (he is absent).
- ECHO REPLIES and volleys: findings anywhere.
- `[TK ...]` only between beats.

## THE EPIGRAPH

Per STYLE "The epigraph" and taste 19: a parent's eye, no plot, no
count, no rule, no named object. The ice from a mother's side —
classes on or off, the dorm, socks, "he says the roads are fine" —
under a handle from registry 24 not used by ch 17–20 (PomPoms 17,
DeeAnn 18, Rhonda 19, Kendra 20; not Denny G. — local), or a new
one; under 35 words. NO weekday in the epigraph; the page's first
paragraph carries the date.

## TASTE (the entries this chapter risks)

17 (this IS the weather chapter — the storm forces the ride; it must
cost and never rescue); 16 (the cab has room; the hand gets its
sentences; the silence at the lot allowed to sit); 4 (the proximity
beat is a NEW sense — the heater, the dash light, the ice on the
glass; not hands only); 11 (her face at every turn — his POV is not
here, so HIS face at every turn, in the dash light); 15 (the file,
unthanked; the trainer driven first, unthanked); 2 (Aisha pays);
18 (the file and the post are plain things; no poem on the ice); 1
(the date said as a date; why the RAV4 can't and the truck can, said
once); 7 (a storm is not lonely — three on a bench, Verna's light);
5 (modern: the scouts, the tablet, the board; no casserole in the
storm); 19 (the epigraph); 6 (ch 13's bike scene is furniture — the
day is new, not the shape; Verna's light is ch 18's — one clause);
8 (a storm chapter is loud; the count lives in the cab and the file,
not the weather); 3 (her wound: the one thing the terms bought her,
spent by weather — the ARC BEAT says it); 10 (three on a bench, two
drops, one hand — who is where in the cab, said once, audible).

---

## AUDIT ADDENDUM (continuity-keeper 1.4.3, E6, 2026-09-18) — BLOCK, then corrected in the body above

The two blocks are corrected in the brief body (the bike in January is a re-evaluation under load, not "the next step" — rung five is full practice and there is no practice till spring workouts; Millrow climbs from the square past Delmar's to the annex and Fieldhouse lot at the TOP, the motel at the bottom). The E6 list (what the storm chapter owes and the brief did not stage) is now staged in the body: why the trainer rides; the staff sent down before dark; the RAV4 up the hill Thursday morning; Missy's seven o'clock page Thursday; the reason the RAV4 stays is a person's, not a machine's; the trainer's place in the room. The card's three corrections applied. The addendum's facts stand as rulings; its BANNED line binds the drafters.

**CH 21 CARD + BRIEF — BLOCKING AUDIT (E6: what's missing first)**

BUILD CHECK: PASS — row 21 In 4 / Out 4, no spend; the brief spends nothing. Heat 5 = "deliberate touch, no errand" (survey l.50–54) — the same charge as ch 20's hand across the table (ch20:340–345) and the wrist (ch20:456). Within stage 4. COUPLES: no row touched; a vaguepost is not the record (registry 190). TARGETS line legal (card-lint 126–132; targets-check 17–23). CONFIRMED.

### A. What the storm chapter owes and the brief did not stage (E6)
1. **Why the trainer rides.** His car, house or street on no page (ch19:335, 370, 400; ch20:229–232). UNESTABLISHED — the page says once, plainly, why a man who drove up does not drive down (his car stays up the hill like hers, or he came up without one); no street, no make.
2. **Emptying the Fieldhouse.** Staff by day in January (registry 153; ch19:46; ch20:199–226; ch18:252–259). "The last one up the hill" is true only if the page sends the staff down before the glaze. RULING — default: the staff gone down before dark, said once.
3. **The RAV4 Thursday morning.** It lives in Verna's lot in front of nine (ch20:265–266); Wednesday night it stays at the annex's warm end (ch12:192–193). The empty space in front of nine at 6:15 (town clock, town-ashford 64–70) is a thing the county reads. UNESTABLISHED — one clause in scene 5.
4. **Missy's seven o'clock page Thursday.** After every check her photograph of the notebook page arrives at seven and Aisha answers "Good record." (ch05:55–62; ch13:91–97; "every morning since" ch17:239). UNESTABLISHED — decide it: the page comes (it says the twenty held overnight) or say once why not.
5. **Why the RAV4 stays and the truck goes.** No four-wheel drive, tires or drivetrain on any page (registry 13: "no gears, no transmission talk"). Her history is [TK] (dossier-aisha 31, 39) — the page may not say she has or has not driven ice. What the page knows: he has gone down that hill every winter night in the dark (ch18:29–30; ch19:305; ch17:488); she has driven it in daylight (ch17:59–64). RULING — the reason is a person's, said once from those facts; PROHIBITION: tires, drive train, four-wheel, weight.
6. **The salt.** No salt fact in the town file. B2-D19.4's TK stands. "Nothing has been down the hill," no truck named — CONFIRMED as the most the page may say.
7. **The trainer's place.** "I'll be in the room" (ch20:232); ch 13 had him at the door (ch13:120). Either; pick one in the establishing line. RULING.
8. **Which step** — see B.9.

### B. The facts
9. **"The next step on her ladder" — CONTRADICTION (BLOCK 1).** The ladder is six rungs, gated overnight (ch05:34–36; ch05:231–246: one student · two light aerobic, a bike in a quiet room · three football-shaped · four noncontact · five full practice · six a Saturday). Last sheet: "Step four. Holds overnight." Dec 18 (ch16:447). The next rung is FIVE, full practice — and "In January there was no sheet. There was no practice … until spring workouts" (ch20:240–243). A bike is step two's instrument (ch05:238; ch12:300–301; ch13:111–116). So the bike in January is a re-evaluation under load in a month with nothing to climb into — the outline's word (b12-outline 670). FIX: the page says once what the bike is; "not cleared" is that nothing exists to clear him into; "real progress" is measurable and NEW — the full twenty at the cap against December's fourteen (ch13:139–151). Consistent with ch 22 (the hold defended on air), ch 28, ch 30 ("Trey's spring clearance on her letterhead").
10. **Millrow's grade — CONTRADICTION (BLOCK 2).** The annex and the Fieldhouse lot are at the TOP of her drive up Millrow (ch17:59–64 "At the top the lot between the annex and the Fieldhouse"; ch16:215–217 "Millrow's low end … up past the annex and the Fieldhouse"; ch18:27–32 the truck on that side of the hill, "At the bottom of the hill the Magnolia Court"; ch12:92 the carillon up the hill from the square). Order going up: the square → Delmar's (the low end) → the stadium's north side → the annex and Fieldhouse lot → the House (Millrow's high end, registry 58). No annex line in the town file.
11. **The stranger's sentence** — 32 words (STYLE (a)); "the doctor put the quarterback" — in HER POV the name is Trey (RECENT 52–56; registry 196); "the next step" (item 9). BANNED below.
12. **The day — CONFIRMED.** Jan 13 a Wednesday (B2-D19.5); ch 20 Friday the 8th, "six days left," "shut on Thursday" (ch20:25–26); "midweek next week" (ch20:16–17). Afternoon re-eval: the hour on no page; legal; it sidesteps the semester question (ch19:55–56).
13. **Arithmetic — CONFIRMED.** Jan 13 → Feb 3 = 21 days, three weeks exactly. Feb 11 from Jan 13 = 29 days, "four weeks." Forward note for ch 22: "two weeks out" from Jan 14 is 20 days — ch 22 must not say "two weeks."
14. **"After signing day"** — Dan's phrase (ch15:363 "So it's February, and not a day sooner"); "the first Wednesday in February" BANNED as a page phrase (RECENT 95–98). CONFIRMED.
15. **Trey on the page — CONFIRMED with a rule.** STANDARDS 42 (no named student carries dialogue or POV); R1 bars gaze, not medical presence; ch 13 put him on the bike, hood up, back to her, answers reported never quoted (ch13:114–116, 133, 142–143). Both dossiers' "offstage absolutely" walls (dossier-dan 282–283; dossier-aisha 260–261) are read by ch 13. RULING: present, silent, never quoted, never POV.
16. **Missy — CONFIRMED with the register.** Chair in the hall, notebook, "Denny was at work, and that was Missy's doing" (ch13:123–125); her car (ch15:50; ch17:269); "His mother drives him" (registry 37, 106); Trey has no car on any page — Missy driving is the only staging; she goes down before the glaze, one clause. Her every line: ch04:178–179; ch13:159, 164; ch15:69–70; ch16:230; ch17:269–270 (a nod, no thank you). "Thaw" was Dan's word (ch04:193) — not in her POV. The smallest true thing: one act with her hands, no sentence. F12 satisfied by her seeing the screen; the office is boxed to one desk (ch20:350–351).
17. **The file for the scouts — RULING.** Inside her authority (ch05:74–79, 285; ch17:240, 253); not a call told to Dan (ch15:366–373; ch20:383–395); R4 clean. THE WALL: Birmingham needed a release in Missy's hand (ch17:258–267); no scout has one — she builds it and puts it in Missy's hands or keeps it; she may not send it anywhere. "Scout"/"the scouts"/"draft" are NEW talent words (only scout-team and Cub Scouts on the pages; "agents" ch19:157, ch20:95), licensed by the outline (671–672; ch 30 "Missy filming it for the scouts"); one clause says what a scout is.
18. **The terms and the ride — RULING.** "Nothing anybody can see" (ch15:354); "A coach's two-door pickup in Verna Poteat's lot at night was a thing anybody could see" (ch18:40–41, his own reading); the truck never in the lot (registry 136; B2-D21.6); daylight logic is daylight (ch19:285, 352). So "Nobody broke the rule" is the couple's reading and the page earns it once: the trainer in the cab for the hill, the weather, the minutes, the hand below the dash — and the truck in the lot is still the thing anybody could see: the cost, not a break. Said once in her head. "Nobody could see it" attaches to the HAND, never the truck. RECENT's parked-vehicle ban was the sub-couple's door-ajar scene; a hand at charge 5 with the engine running is not that. Tell the panel.
19. **Verna — CONFIRMED.** Anchors ch03:355–359 and ch15:136–138 (THREADS 61). A third within practice. "Won't hurry for football" vs Sonny's concrete (ch13:76–80): a different voice and noun; but it is the argument of her own ch 15 line ("the next sixty years") — the third must not reuse nights, rooms or sixty years. WATCH: "I had a man once who'd have…" is Verna's shape on two pages (ch13:82–83; ch15:130–132); no third. Her light: the formula BANNED (RECENT 99–101); the sight in fresh words allowed; the office light on at 6:15 (town clock) usable Thursday. "My winter doctor" hers (ch13:54).
20. **Vaguepost 2 — CONFIRMED.** The permitted form word for word: "Interesting to see who gets rides home from the facility these days" (grapevine-realism 178–179, rule 2; the outline); ch 12's was DeeAnn's, spent. A handle from registry 24 or new; not DeeAnn, not Denny G. She reads the board at SIX in room nine with her boots on (ch13:63–64; ch17:295) and at the counter (ch19:74) — the card's "seven" corrected. She knows the two-door signal in her own POV (ch13:59–61 Verna: "Earlene counted the doors on that truck. Four."; ch15:119–122). F7 read the other way is hers to think in one sentence. The photo (B2-T05) — her POV cannot know it (THREADS 17). The pairing in print since ch 3/5 — one clause allowed.
21. **Who is in the buildings — RULING.** No practice (ch20:240–243); thirty-four's rehab on no January page; the kid of B2-D19.2 dropped under D19.5's default — legal; say once nobody else is in either building.
22. **The cab — CONFIRMED NEW.** Two doors (ch12:461–462, 474; registry 79); the inside on no page — a bench, the heater, the dash light, his glove, the tracks in the gravel are NEW (registry at the fold). Three across needs the bench said (taste 10). The square and the motel are both at the bottom (ch18:31; ch12:92); the distance between them on no page — "the last minute" legal.
23. **The opening candidates — CONFIRMED.** Accepted openings: 13 the trowel, 14 the printer, 15 the pen, 16 the ice chest, 17 the RAV4, 18 the keys, 19 the stool, 20 Sonny's twenty. None is a chair, a chest strap or a sky. The chest strap (ch20:247; ch13:115) and the chair in a boxed office (ch20:350) are consistent.
24. **Naming — CONFIRMED, one registry wobble.** "7" in the trainer's mouth (ch20:232; B2-D25.6 open). "Doc": NAMES.md gives it to Dan alone, but Sonny says it on three accepted pages (ch03:50; ch07:181; ch13:75) and Tick on air (ch08:208) — pre-existing drift for the registry, not this chapter's; the trainer says "the doctor" (ch20:232). "Trey" in her narration and to Missy; Missy "Trey"; never "the boy" in her POV.
25. **Ending — CONFIRMED.** Ch 20 down on the chair; 21 up; a morning on a thing at room nine satisfies today's ban and STYLE (c).
26. **Furniture — cites corrected in the body:** ch20:229→232; ch20:308–310→350–351; ch20:12–14→16–18; ch12:52–53→192–193; ch13:121–123→123–125; ch13:147–153→147–153; ch13:177–178→172–173; the annex's place → ch16:215–217, ch17:59–64. Edges: 7 spent, 3 remain.
27. **Long sentences.** Card: none at thirty. Brief: the stranger's sentence, 32 (item 11).
28. **TASTE — add 8** (a storm chapter is loud; the count must be in the cab and the file), **3** (her wound: the one thing the terms bought her, spent by weather — the ARC BEAT says it), **10** (three on a bench, two drops, one hand — audible in one hearing; who is where in the cab, once).

**BANNED (this addendum):** "On the Wednesday the board had promised ice, the doctor put the quarterback back on the bike for the next step, and the ice came in while she was writing it down." · "the next step on her ladder" (as a phrase for the bike) · "the annex at its low end" · "drives the trainer home first".

**CARD CORRECTIONS (applied):** "drives the trainer down first, unasked"; "interesting to see who gets rides home from the facility these days"; "She reads the post at six and holds."

## THE CARD'S CALLS — DEFAULTS FOR DRAFTING
1. Wednesday the thirteenth into Thursday the fourteenth.
2. The trainer rides down first; she is alone in the cab for the last minute.
3. Verna at her window when the truck stops, and she never says; the post comes from nobody the page names.

## VERDICT: BLOCK
1. The brief, scene 1 and the stranger's sentence — "the next step on her ladder" (item 9; item 11).
2. The brief, scene 3 — Millrow's geography (item 10).
The card passes with the three corrections. The E6 list (items 1–5, 7) is not blocking but each is a sentence the page must carry or a drafter will invent it.

## New canon this brief will establish (registry at the fold)
The cab's inside (bench, heater, dash light); his glove; tire tracks in Verna's gravel; "a scout" / "the scouts" / "draft" as talent words; the return-to-play file in her hands; the trainer's reason for riding; the January re-eval on the bike as a check, not a rung; Verna's third anchor; the handle for vaguepost 2; the epigraph's handle.

Files: `notes/cards/ch21-card.md`, `plots/brief-ch21.md`, `DECISIONS.md` (B2-D19, D24, D25), `plots/b12-outline.md`, `plots/romance-arc.md`, `manuscript/ch03, 04, 05, 07, 08, 12, 13, 15, 16, 17, 18, 19, 20`, `notes/furniture-registry.md`, `THREADS.md`, `plots/dossier-aisha.md`, `plots/dossier-dan.md`, `notes/grapevine-realism-2026-08-29.md`, `../STANDARDS.md`, `../town-ashford.md`, `../canon/NAMES.md`, `../canon/FACTS.md`, `../notes/heat-continuity-sweep-2026-09-15.md`, `../notes/romance-density-survey-2026-09-14.md`, `studio/STYLE.md`, `studio/agents/variance/RECENT.md`, `studio/AUTHOR-TASTE.md`, `studio/tools/card-lint.py`, `studio/tools/targets-check.py`.
