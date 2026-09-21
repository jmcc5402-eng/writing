# Brief — Chapter 24: "Pending Review" (Dan · Wednesday, January 20 — the suspension; the greenlight the same week; his silence)

**Status: SET PIECE — three blind drafters (distinct variance cards,
same brief and addendum).** The seventh set piece: the Major Setback
lands in full (BEATS: Retreat to identity 75%, Maximum pressure 75% —
both at 24); arc-docs rung 24 — "the identity's last, most plausible
cowardice; the reader should hate him a little here"; romance-arc row
24, In 5 / Out 5: his silence. The card (`notes/cards/ch24-card.md`)
and this brief are audited TOGETHER by the keeper before a drafter
launches; the brief carries THE AUTHOR'S READ (seven questions now —
FUN joined 2026-09-21, `studio/AUTHOR-QUESTIONS.md`). ONE OPEN PR AT A
TIME: the drafters launch after #181 (the ch 23 fold) merges. The
card's three calls are taken at the defaults below and shown on the
PR. THE SECOND TRIAL OF THE AUTHOR-PROXY (1.1.0 — rating on the
author's scale; the stakes-blatant line; the apart-why; FUN).

**TARGETS (the definition of done — `canon/TARGETS.md` row 24, copied):**
Romance 5 · Heat 2 · Aisha 2 · Dan 3 · Wound 3 · Fun 0 · Town 2 ·
Menace 3 · Ends down · Talk quiet · Words 3200 · Pays Dan.
On the AUTHOR'S scale (TARGETS definitions, 2026-09-21): Romance 5
means CONFLICT between the two of them on the page, not longing — and
this chapter has it: he chooses the job in front of her, and she lets
him; the window is where it happens. Heat 2 counts only because they
share the lot and the window — no touch; her face a foot away through
glass, the cold, what he does with his hands. Aisha 2: seen from his
side, tested — she does not ask him for the one thing. Dan 3: TURNED
— the cowardice chosen with his eyes open; the person at the end would
decide differently than the person at the start, and does not. Wound
3: his — the silence he must buy back (ch 27); and hers, seen. Fun 0
by design — a hit chapter — so the FUN question asks what takes the
edge off (the Table's count; Earlene; a laugh Dan loses). Town 2: the
town acts once (the room jump, rule 7 spent) and counts once (the
Table). Menace 3: the greenlight — the building on her clinic's ground
approved the same week she is suspended, said BLATANTLY once (D30.4),
and Boyd in none of it by name. Talk QUIET (8–15%): a coach who says
nothing all day. Ends DOWN, held-quiet, the worst one. Pays Dan (in
the reader's regard). Words 3200; 3400 the ceiling — ch 21–23 all ran
over; this one is short by design: a man who says nothing.

## PROOF OF DONE — campus 1.2 ch 24, 2026-09-21 (chapter-proof; filled at the end)

MECHANICAL (commands, output attached at the end)
  [ ] bash studio/tools/chapter-lint.sh manuscript/ch24.md → BANS clean; TOUCH SPAN: the window cluster ≥4 body sentences (his); no crowding; ≤2 questions ending in a period
  [ ] python3 studio/tools/dialogue-lint.py manuscript/ch24.md → quiet band (8–15%)
  [ ] python3 studio/tools/bans.py manuscript/ch24.md → clean
  [ ] python3 studio/tools/opening-check.py / ending-check.py → not a repeat (NOT the counter, NOT the stool, NOT the stove light, NOT the tracks)
  [ ] python3 studio/tools/fact-check.py books/campus-series → clean
  [ ] every sentence under 30 words, ≤3 "and"s; wrap at 80; ≤3400 words
READERS (verdict files, path attached at the end)
  [ ] author-proxy 1.1.0    → notes/ch24-author-proxy-<A|B|C>-<date>.md (BEFORE the panel; TESTS line, seven tokens; romance and heat on the author's scale; the stakes-blatant line)
  [ ] romance-reader-panel  → notes/ch24-panel-<A|B|C>-<date>.md (BLIND — launched on the card-blind copy; TESTS + ACTUALS on the author's anchors)
  [ ] continuity-keeper     → notes/ch24-keeper-<date>.md (the page audit, the clock standing)
  [ ] /chapter-score        → notes/scores/ch24-score.md
MUST NOT HAVE CHANGED
  [ ] the rung ladder: no touch, no kiss — the window stays glass; nothing passed through it
  [ ] the trainer: NO drop (none left); Missy: NO drop; the athletic director unnamed, never "the AD"; Boyd unnamed on this page
  [ ] Dan's stake: ONE hint (both gone that day if caught — D30.1), never said plain again
  [ ] the gossip room's name not repeated; the trainer unnamed
  [ ] no new fact, name, date or object not on a page or in canon — `[TK]` it (the lawyer and the press woman are NEW and unnamed: "the university's lawyer," "the department's press woman" — say so in the registry)
VARIANCE
  [ ] three cards drawn (LRU, drafter deck; distinct) and logged; the keeper's, the proxy's and the panel's draws logged

## THE ROMANCE MOVE (first line)

Stage 5 held, In 5 / Out 5 (romance-arc row 24: "His silence"). No
new rung — the window is glass and stays glass. What this chapter
does to the feeling: the county has said it for them, the school has
put it on letterhead, and the one thing he could spend — a sentence
with her name in it — he keeps, on advice, in front of her, and she
does not ask. The romance CONFLICT is between the two of them for the
first time since the terms: his job against her, chosen, and her
never asking, chosen. Earned by: ch 22 (the process on the air,
everything but her name; his stake said plain), ch 23 (the picture;
both fired if caught — D30.1; "she would rather be the one who
pays"), ch 15 (the terms), ch 18 (the week at his house — what he is
keeping). Spends nothing (row 24 "—"). The inside runs one stage
ahead of the outside and no more: each would rather be the one who
pays, and each pays alone.

## THE LEADS' SCENES (the floor — ONE scene, the window)

They share ONE scene: the annex lot at noon. Everything else is him
with her in it — her name under his on the email; the statement he
does not make; her taillights. THE WINDOW (dossier-dan row 24: "Dan
crosses the practice lot to her car with the heat on, taps the window
— and nothing else; costs him being seen with the woman who started
the truck; unrewarded"): she has carried one box to the RAV4 (ch 25
is the boxes; this is ONE box, the day's — the review letter, the
tablet, the parka; NOT the office packing) and sits in it with the
engine running and the heat on, in the annex lot, in daylight, at
noon, where the county can see. He crosses the lot in daylight —
after a morning of being told not to — taps the glass with one
knuckle. She rolls it down four inches. KIND 9 — his body first: what
the four inches of her face do to him before he has decided anything
(the breath, the hand that wants the door handle and goes in the
pocket), four sentences or more (TOUCH SPAN counts them; the touch is
a scene, taste 20 amended — and there is NO touch, which is the
point). Then call 2's DEFAULT: he says the one flat thing a coach can
say — "Film's at four" — and nothing else; she says "I know," or
nothing; and SHE DOES NOT ASK HIM TO SPEAK. He sees that she does not.
He knows what it is: nobody has ever spent anything on her and she
was not going to start requesting it (arc-docs 23–24 — her sentence,
in his read, once, plain). The window goes up. He walks back across
the lot with the county watching a coach who went to a car and said
nothing worth hearing. THE CONFLICT IS ON THE PAGE: the sentence he
could have said is in his head, whole, before he taps the glass — and
he does not say it. The reader hates him a little. He knows they
should. APART, WHY — said once, plain, in his head: the lawyer's
sentence ("any statement makes it worse for her") is true and it is
also the job; fourteen-hour days eleven months a year are what he is,
and he is choosing what he is (D30.3 — the apart-why clause, his
side). ENDS DOWN, held-quiet: call 3's DEFAULT — the Fieldhouse
window at dark, her taillights taking Millrow, the statement he did
not make in his head, whole, one more time; NOT the counter, NOT the
stool, NOT a phone face down (ch 22's shape), NOT the stove light.

**WOVEN:** she is in every scene of his (the email; the lawyer's
"her"; the town room; the window; the taillights).

## THE OPENING, SAID

Wednesday morning. MID-MOTION on a thing that is none of the accepted
openings (13 the trowel, 14 the printer, 15 the pen, 16 the ice
chest, 17 the RAV4, 18 the keys, 19 the stool, 20 Sonny's twenty, 21
Missy's chair, 22 the lot on foot, 23 the thumb through four hundred
pictures). Candidates: the Checkerboard at six with Earlene's paper
folded to the aldermen's minutes and Tunk reading over her shoulder;
the athletic director's email arriving on his phone while the griddle
ticks; his truck's wipers on the first rain since the ice. The first
paragraph SAYS Wednesday the twentieth of January in words a listener
keeps (ch 23 was Monday the eighteenth; the aldermen sat Tuesday the
nineteenth); a face before a clock; NOT a calendar first line. The
stranger's sentence: *On the Wednesday the aldermen's vote made the
paper, Dan Merritt read the athletic director's email at the
Checkerboard counter with her name under his.* (Twenty-eight words.)
The paragraph locates: the counter, the paper, who is in the room
(Earlene, Tunk, the cook).

## THE ARGUMENT, SAID

*The school wants the county to do its firing for it, under a word
that sounds like fairness. The county wants a name said out loud and
gets a building instead. Dan wants to say her name and keeps his job.
Aisha wants nothing from anybody, and gets it.* Between the leads:
*he could spend one sentence; she will not ask for it; both of them
know the other knows.*

## THE SCENES

1. **Six, the Checkerboard** (the opening). Earlene's paper folded to
   the aldermen's minutes: the Millrow parcels rezoned — Boyd's ground
   approved Tuesday night, five to two (`[TK the vote — town-ashford
   187–230: mayor plus seven; Delores counted; the number is new
   canon]`); Tunk over her shoulder; the cook; the Coach's Slice set
   down unasked (registry 73). THE TABLE COUNTS: a woman's hold
   questioned and a building approved in the same four days, and
   nobody at the counter says the name that connects them (F3
   discipline — the tell on the page, uncommented except by the
   Table). Earlene's anchor is NOT here (scene 5 or the end of 3) —
   here she counts. FUN: the room the reader wants to stay in; one
   laugh Dan loses (Tunk's, or the cook's). The email arrives on his
   phone at the counter (the athletic director — unnamed, "he"; the
   registry's italic lines; her name under his in the address line,
   as in ch 5): *Dr. Cole is placed on administrative leave pending an
   independent review of the December medical determination; the
   review's findings will be published within fourteen days.* Two
   weeks. The third of February. He reads it twice and puts the phone
   face UP.
2. **Before eight, the Fieldhouse** (the sit-down). The university's
   lawyer and the department's press woman (NEW, unnamed — "the
   lawyer," "the press woman"; no names invented; the registry) in
   his office with the door shut: say nothing; the program's
   statement is the athletic director's statement; "any statement
   makes it worse for her" — and it is TRUE, which is the trap. The
   stake HINTED once, his read (D30.1): a coach caught with the team
   physician in season is gone that day, and so is she — one clause,
   never said plain again. The apart-why (D30.3): fourteen-hour days
   eleven months, in his own terms — he is in this building fourteen
   hours today and every day. What he does with his hands while they
   talk. He agrees. The reader should mind.
3. **Mid-morning, the town room** (rule 7 spent). Rhonda's plain post
   crosses rooms: call 1's DEFAULT — DeeAnn Prewitt carries it into
   the town room (the lost-dog, road-work room — town-ashford 410–
   420) with a line of her own, and the town room TURNS on her for it
   — not on the doctor, on the poster: "this isn't the room for it";
   "some of us come here for the recycling schedule"; the retainer-
   in-the-waffle register turned cold. It costs DeeAnn (rule 7: a
   story that jumps rooms costs someone). Dan reads it — the habit,
   with its why in a clause (a board knew first; the football hidden
   in ordinary talk — B2-T08, ch 20's second why): he is looking for
   what the town knows about the review, and finds the town does not
   care about the review; it cares who brought it in. ON THE PAGE we
   see two posts and a reply, quoted once in blocks, the rest told.
   The greenlight thread beside it: three replies about parking. The
   Table's count made by the room without knowing it.
4. **Noon, the annex lot** (the window — THE LEADS' SCENES above).
   Her box; the RAV4 with the heat on; the trainer at the warm-end
   door, seen, NOT named, NO drop (none left) — his pull in where he
   stands (in the door, on nobody's side of the lot); Dan crosses in
   daylight; the knuckle on the glass; four inches; "Film's at four";
   she does not ask; the window up; the walk back. The county: a
   staff car at the fence; the survey crew's flags still in the
   ground across the lot (ch 23), and a new stake — orange, taller —
   at the annex's corner since Tuesday's vote (NEW canon; ch 26's
   stakes cross here).
5. **Four, the film room; dark, the window** (the ending). Film at
   four with the staff — Ty ("Coach," and nothing about the email —
   Ty knows how to be on a staff); the statement he did not make,
   whole, in his head; the phone face up on the table with nothing
   sent. Earlene's ANCHOR placed honestly — she is NOT in the
   Fieldhouse: DEFAULT — the anchor closes scene 3 in the town room
   in her own handle's voice (Earlene posts, once, under her real
   name — registry 24 has her as a board presence via B. Hollis; a
   post of her own is NEW — or she says it at the counter at six in
   scene 1 as the day's forecast, before the email lands: *They won't
   fire her. They'll invite the county to do it for them. Y'all can
   count the week's other news yourselves.* — the drafter chooses and
   says which; ONE anchor this chapter). At dark, the Fieldhouse
   window: her taillights take Millrow down (she is leaving the
   building for the fortnight); the sentence one more time; ENDS
   DOWN, held-quiet, the worst one — call 3's DEFAULT (the window),
   the alternative his house with the statement unsent (a phone at
   night is ch 22's and ch 23's shape — avoid).

## THE AUTHOR'S READ (studio/AUTHOR-QUESTIONS.md; L056)

| Scene | MORE | WHO | CONFUSING | NOSE | POINT | SENSES | FUN |
|---|---|---|---|---|---|---|---|
| 1. Six, the Checkerboard | Romance felt 3: her name under his on the email — one body beat (what the address line does to him); no longing paragraph here | Earlene: wants the county counted straight; conflict 1 (she says the forecast and reads on); Tunk: wants the gossip; the cook: wants the griddle; Dan: conflict 2 — the job against her, in the way he reads the email twice | Wednesday the twentieth said; the aldermen sat Tuesday (the third Tuesday, ch 23); "the minutes" = the paper's report of the vote; who the athletic director is (unnamed, "he," the email's shape from ch 5); "pending review" glossed once — a fortnight, findings published | Nobody explains the Coach's Slice or the paper; the count is Earlene's, not the narrator's | The point: the county is being handed the firing. The stake BLATANT once: the review is the paper that lets the trustees vote her job in February (D30.4's sentence, his side) | The griddle after the first rain; the paper's fold; the cup Earlene fills | The room the reader wants to stay in; one laugh Dan loses (Tunk on the aldermen) — what takes the edge off a hit chapter |
| 2. Before eight, the Fieldhouse | Romance felt 4: what "her" does in the lawyer's mouth; the hand in the pocket — two body beats | The lawyer: wants no statement, ever; the press woman: wants the athletic director's words to be the only words; LIKE neither, HATE neither — they are right; Dan: conflict 3 — the sentence he could say is in his head whole and he agrees to keep it; the reader should hate him a little | Who these two are (one clause each, unnamed); why they are here (the program's exposure); "any statement makes it worse for her" — true, and the trap, said | Nobody says "cowardice"; the page shows him agreeing | The point: he chooses the job. The stake hinted once: caught in season, both gone that day (D30.1); fourteen-hour days, his side (D30.3) | His office with the door shut; the film room's projector fan through the wall; the lot's water | — (none; a hit by design; the FUN in this chapter is scene 1 and the Table) |
| 3. Mid-morning, the town room | Romance felt 3: her name in a room that does not care; one beat | DeeAnn: wants to be first; pays — the room turns on her (conflict 2); Rhonda: her post carried without her; the town-room regulars: want the recycling schedule; Dan: the habit with its why | Which room this is (the town room — lost dogs, road work); who carried it (DeeAnn, under her real name); what it cost her, shown in the replies | Nobody explains rule 7; the room's own sentences do it | The point: the town does not care about the review; it cares who brought it in — the county's verdict is a shrug, which is worse. The greenlight thread beside it (three replies about parking) | The screen at his desk; the parking replies | The room's register is the funny one turned cold — the reader laughs at the town room's reply and then does not |
| 4. Noon, the annex lot | Romance felt 6 (the peak): his body at the four inches — four beats or more; the sentence in his head whole; the confusion plain: he wants to say it and he is not going to | Aisha, seen: wants nothing from anybody; conflict 3 — she does not ask, and it costs her (his read: nobody has ever spent anything on her); the trainer in the door: wants no side; conflict 1; Dan: conflict 3 | Noon said; her one box (not the office); the heat on; who can see (a staff car at the fence; the trainer in the door); the window four inches | "Film's at four" is the whole line — nobody says "I can't say anything" | The point: the couple's worst hour. The stake: the county watching a coach cross a lot to a suspended doctor — one clause of what that is worth to a bettor's county | The lot's water; the new orange stake at the annex corner since Tuesday; the RAV4's exhaust in the cold; the glass | — |
| 5. Four, the film room; dark, the window | Romance felt 4: the statement whole one more time; her taillights — two body beats, and the ache in his terms (what he keeps and what it is worth) | Ty: wants to be on a staff and says "Coach"; conflict 1; Dan: turned — the person at the end would decide the same, and knows it | Film at four (no practice till spring — ch 21); the fortnight's date (February 3, signing day — said); where she is going (down Millrow; the fortnight; not said where) | Nobody says "he had chosen the job" — the page shows the phone face up and nothing sent | The point: the silence he must buy back (ch 27). Ends down, held-quiet | The projector fan; the window at dark; the taillights on wet Millrow | — |

## ROMANCE BEATS (one per scene, at least three, two kinds)

Scene 1 — kind 6 (her name under his; the county's letterhead).
Scene 2 — kind 7 (the sentence he could spend, for her, kept).
Scene 3 — kind 6 (the room's shrug). Scene 4 — kinds 1, 2, 9 (the
four inches; his body first; her face; the not-asking). Scene 5 —
kinds 7, 8 (the statement whole; what he keeps and knows he keeps).
No touch. The panel counts; TESTS and ACTUALS on the author's
anchors; the proxy's TESTS line with seven tokens.

## REVERSAL — who loses what

Dan keeps the job and loses the reader's regard, on purpose (PAYS
Dan). Aisha loses the building for a fortnight and asks for nothing.
DeeAnn loses the town room. Boyd gains a vote and is nowhere. The
lawyer and the press woman lose nothing; they were right.

## ARC BEATS

**Dan (arc-docs rung 24; dossier row 24):** the silence on counsel's
advice; the window; TURNED (3) — the cowardice chosen; the silence he
must buy back at 27. **Aisha (dossier row 24):** seen — she does not
ask him to speak; the wound itself. **Boyd (§5; boyd-arc 23–24):** the
greenlight the same week; in none of it by name. **The trainer:**
present in a door, no drop. **Earlene:** the anchor. **Ty:** one word.
**DeeAnn:** pays rule 7. **Missy, Denny:** absent.

## STAKES ON THE PAGE (taste 22 amended — BLATANT; `canon/STAKES.md`; the brief gate)

| Who | Locked stake carried | The drop (whose eye, what) — the blatant sentence |
|---|---|---|
| Dan | caught in season, both gone that day; his second time ends him in college coaching (D30.1, F-DAN-02); the extension on the February agenda | ONE hint in his read (scene 2): *a coach caught with the team physician in season was gone that day, and so was she* — never plain again this chapter |
| Aisha (seen) | suspended; her job on the February agenda under a politer name; the review is the paper | scene 1, his read, once: *the review was the paper that let the trustees vote her job to the group in February without anybody saying her name* (D30.4) |
| Boyd (absent, unnamed) | the pledge; the building on her clinic's ground — APPROVED Tuesday | scene 1: *the aldermen had voted the ground under her clinic to a building on Tuesday night, and the school had voted her out of the clinic on Wednesday morning, and nobody at the counter said the name that was in both* — the Table's count, blatant |
| The trainer | ten thousand (LOCKED) — NO drop (none left) | pull only: where he stands |
| DeeAnn | none locked — rule 7's cost is hers | the town room's replies |
| Earlene, Tunk, the cook, Ty | none | — |
| The lawyer, the press woman (NEW, unnamed) | none — they carry the school's stake: exposure | "any statement makes it worse for her" |

## THE STAKES, THIS CHAPTER'S

In his terms: her name is on letterhead now; the review's findings
publish the day the class signs; the ground under her clinic was
voted to a building last night; a sentence from him with her name in
it ends both of them today, and not saying it ends something else,
slower; fourteen days.

## COUPLE LINE

"Film's at four." / "I know." — the whole exchange. The couple line
is the one he does not say, in his head, whole, twice.

## END REGISTER: DOWN, held-quiet. Ch 23 ended down, on two phones; 22 flat, at a counter; 21 up, on the tracks.

Not a phone at night (22, 23). Not a room with people (22). The
Fieldhouse window at dark, her taillights, the sentence. The worst
one. Down is not wry and not a button.

## ROOTING FOR

**Dan:** crosses the lot in daylight after being told not to — seen
by the county, thanked by nobody; and then says nothing worth hearing
— the beer test fails on purpose this chapter, and the page knows it.
**Aisha (seen):** does not ask — seen by him alone.

## NAMING, FULL LIST

Narration (his POV): "Aisha" in his head; "Dr. Cole" in the email and
the lawyer's mouth; "her" everywhere else. "Dan" / "Dan Merritt" once;
"Coach" in Ty's and the cook's mouths. "Earlene" / "Earlene Tatum"
once; "Tunk" / "Tunk Ferrell" once; "the cook"; "Ty" / "Ty Beaumont"
once — never "he" where Ty and Dan share a paragraph (L045). "DeeAnn
Prewitt" on the post; "Rhonda Sipes" as the post's author, once. "the
trainer" ONLY. "the athletic director" — never "the AD." "the
lawyer," "the press woman" — unnamed, NEW. Boyd: UNNAMED on this page
(the Table's count carries him without his name). The town room, the
parents' board, the gossip room (unnamed).

## FURNITURE, CITED

The Checkerboard (town-ashford 131; registry 65, 73 — the Coach's
Slice; Earlene walks the pot); Earlene and Tunk at the window (ch
20:30); the athletic director's email (registry 26 — the shape; ch 5);
the aldermen (town-ashford 187–230; Delores's count, ch 23); the
Millrow parcels rezoned (town-ashford 207); the town room's register
(town-ashford 410–420; the rulebook §2 rules 6, 7); rule 7 (the
rulebook 216–223); Rhonda's plain post (ch 23); the board habit's two
whys (B2-T08; ch 20; ch 23:421–425); the annex lot, the warm-end door,
the survey flags (ch 23); the RAV4 (ch 21, 23); Ty on a staff (registry
70); the film room (ch 22:61, 99; ch 23:161); the Fieldhouse window on
the lot (ch 21:299); the drinks register (nothing explained); F-DAN-01
(the first screenshot — the hint's shape).

## BANS AND BUDGETS

- Sentences END (STYLE (a)): under thirty; at most three "and"s; no
  one-sentence paragraph. Hand count and report the five longest.
- No mystery-making (b): the email is an email; the vote is a vote;
  the lawyer's sentence is true and the page says so. Jokes
  understood (c) — one, lost. Apart-why said (d) — his side.
- ONE anchor (Earlene's). Edges: ONE remains for the book — NOT spent
  here (ch 27). Nobody swears.
- Calendar: "Wednesday the twentieth of January" in the first
  paragraph; "Tuesday night" for the vote; "the third of February" /
  "fourteen days" / "a fortnight" once; NEVER "two weeks out";
  "signing day" allowed once, glossed.
- The trainer: NO drop; Missy: NO drop; Dan's stake: ONE hint.
- The blatant sentences (D30.4): the review as the paper; the building
  on her clinic's ground — once each, plain, his read; never explained
  twice.
- Nobody explains a drink. No POV dip (B2-D27.3).
- The touch has a body and the touch is a scene (taste 20 amended):
  at the window, his body over four beats or more — and NO touch.
- Names, not "he," where two men share a paragraph (L045): Dan and
  Ty; Dan and the lawyer; Dan and Tunk.
- The clock between scenes on the page (L053): six → before eight →
  mid-morning → noon → four → dark; where he was, how each thing
  reached him (the email on the phone; the room on the desk screen;
  the lot on foot).
- BANNED: RECENT.md as of 2026-09-21; studio/lessons/bans.txt (the
  hooks read it); "in this room/office/lot" in any form; "somebody's";
  "never once"; "one beat"; "plainly" more than once; a phone face
  down (ch 22's); a phone at night as the ending (22, 23); the stool
  with nobody on it (22); the tracks (21); the stove light (20);
  "It's written down, and it's hers" (22 — spent); "everything but her
  name" (22); "did not say thank you" and every thank-you shape
  (L042); a face that "did nothing" (L050); "electricity"; "the whole
  county could see"; "Interesting to see who"; Ty for the trainer;
  "the AD"; any sentence quoted as an example in the audit addendum.
- The epigraph's handles unused by 20–23: Tim Brasher, PieBeforeKickoff
  (GrammyInSectionC was 23's; PomPoms&Prayers 22's; FridayNightFaye
  21's; Kendra Voyles 20's).
- ECHO REPLIES and volleys: findings anywhere.
- `[TK ...]` only between beats.

## THE EPIGRAPH

Per STYLE "The epigraph" and taste 19 as amended: a parent's eye, no
plot, no count, no rule, no weekday, light — and ch 23's was the funny
one, so this one may be light without a laugh, or funny again (every
third owes one; two in a row is allowed). The first rain after the
ice from a parent's side — the dorm's leak, the umbrella nobody
packed, "he says he's fine" — under Tim Brasher or PieBeforeKickoff,
under 35 words. NOT the email, NOT the vote: the epigraph does not
know what the chapter knows.

## TASTE (the entries this chapter risks)

22 amended (BLATANT — the review as the paper, the building on her
ground, both fired: said once each in plain sentences; and no
cartoon: the lawyer and the press woman are right, not villains); 2
(Dan pays — in the reader's regard, on purpose); 3 (the wound named
once — his silence he must buy back); 7 (a hit chapter — the Table
and one laugh keep it from lonely; the FUN cell); 8 and 16 (the
window gets its sentences; the taillights get theirs); 1 (every clock
a date); 15 (the lot crossed unthanked; the not-asking unthanked); 12
(the sit-down SHOWN — the lawyer's words, his); 18 (the vote is a
vote; the tell is on the page uncommented); 6 (not ch 22's counter,
stool or phone; not a third window-at-dark if one exists — the
opening check); 19 (the epigraph); 20 amended (his body at the
window, four beats, no touch); 21 (who the lawyer and the press woman
are, in a clause; who DeeAnn is); 13 (the card); 10 (who is at the
counter, once, audible).

## THE CARD'S CALLS — DEFAULTS FOR DRAFTING

1. DeeAnn carries Rhonda's post into the town room and pays for it.
2. At the window he says "Film's at four" and nothing else.
3. It ends at the Fieldhouse window at dark, her taillights taking
   Millrow; the alternative (his house, the statement unsent) is a
   phone-at-night shape and is not taken.
