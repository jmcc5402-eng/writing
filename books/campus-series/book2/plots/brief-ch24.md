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
  [ ] python3 studio/tools/opening-check.py / ending-check.py → not a repeat (the counter is NOT the opening — ch 12, 20; NOT the Fieldhouse window as the ending — 15, 16, 21, 23; NOT a phone at night; NOT a running car)
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
  [ ] no new fact, name, date or object not on a page or in canon — `[TK]` it (the lawyer and the press woman are NEW and unnamed; the vote's count `[TK]`; who conducts the review `[TK]`; the clinic's cover `[TK]`; Tunk not an alderman on this page `[TK]`)
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
in his read, once, plain). The window goes up. She leaves at noon, in
daylight, the RAV4 down Millrow with the county watching (keeper B2 —
no five-hour hole). He walks back across the lot with the county
watching a coach who went to a car and said nothing worth hearing. THE CONFLICT IS ON THE PAGE: the sentence he
could have said is in his head, whole, before he taps the glass — and
he does not say it. The reader hates him a little. He knows they
should. APART, WHY — said once, plain, in his head: the lawyer's
sentence ("any statement makes it worse for her") is true and it is
also the job; fourteen-hour days eleven months a year are what he is,
and he is choosing what he is (D30.3 — the apart-why clause, his
side). ENDS DOWN, held-quiet: call 3's DEFAULT (revised after the
keeper) — her empty office door at the annex at dark, the clinic open
around him, the sentence he did not say whole one more time, and he
does not go in; NOT the Fieldhouse window (spent 15, 16, 21, 23), NOT
the counter, NOT the stool, NOT a phone (20, 22, 23), NOT a running
car (21, 22).

**WOVEN:** she is in every scene of his (the email; the lawyer's
"her"; the town room; the window; the taillights).

## THE OPENING, SAID

Wednesday morning. MID-MOTION on a thing that is none of the accepted
openings (13 the trowel, 14 the printer, 15 the pen, 16 the ice
chest, 17 the RAV4, 18 the keys, 19 the stool, 20 Sonny's twenty, 21
Missy's chair, 22 the lot on foot, 23 the thumb through four hundred
pictures) — and NOT the Checkerboard counter (ch 12's and ch 20's
opening shape; keeper B5). The opening: the first rain since the ice
on the truck's windshield going up Millrow before seven, the wipers,
the water off the hill; the email lands on his phone at the
Fieldhouse door, and he reads it standing in the rain with the key in
the lock — alone; nobody in the county knows yet but the two names on
it. The first paragraph SAYS Wednesday the twentieth of January in
words a listener keeps (ch 23 was Monday the eighteenth; the aldermen
sat Tuesday night); a face before a clock; NOT a calendar first line.
The paragraph locates: the truck, the hill, the rain, the door. Where
he was Monday night and Tuesday: one clause each (Monday — the board
opened or not, say which; Tuesday — the building, fourteen hours, the
vote heard about how). The stranger's-sentence device is NOT used
this chapter (keeper B6: no example sentences).

## THE ARGUMENT, SAID

*The school wants the county to do its firing for it, under a word
that sounds like fairness. The county wants a name said out loud and
gets a building across the street instead. Dan wants to say her name
and keeps his job. Aisha wants nothing from anybody, and gets it.*
Between the leads: *he could spend one sentence; she will not ask for
it; both of them know the other knows.*

## THE SCENES

1. **Before seven, the hill, the door** (the opening). The first rain
   since the ice; the truck; the email on his phone at the Fieldhouse
   door — the athletic director's shape (registry 26/27: her name
   under his in the address line; italic lines in his reading; no
   header, no signature, no time; "the athletic director," unnamed,
   he; his phrase "medical determination"): administrative leave —
   or suspended; the card says suspended — pending an independent
   review of the December medical determination, findings published
   within fourteen days. `[TK who conducts the review — on no page]`.
   The arithmetic, his: fourteen days is the third of February, the
   day the class signs. He reads it twice in the rain. Nobody at the
   counter, nobody in any room, knows yet — the page says so. Monday
   night and Tuesday in a clause each. The stake HINTED once, here
   or in scene 2 (D30.1): a coach caught with the team physician in
   season is gone that day, and so is she — one clause, his read,
   never plain again.
2. **Before eight, his office** (the sit-down). The university's
   lawyer and the department's press woman — NEW, unnamed ("the
   lawyer," "the press woman"; who summoned them, one clause: the
   athletic director's office sent them up) — and the LAWYER shuts
   the door, and the page says so (every Fieldhouse door stands open
   by his rule, ch 20:127). Say nothing; the department's statement
   goes out at ten and it is the athletic director's words; "any
   statement makes it worse for her" — and it is TRUE, which is the
   trap. The apart-why (D30.3), his terms: he is in this building
   fourteen hours today and every day, eleven months. What he does
   with his hands. He agrees. The sentence he could say is in his
   head, whole, and the reader should mind. The film room's fan is
   NOT heard through the wall (no adjacency on any page).
3. **Ten, the statement; mid-morning, the town room** (rule 7 spent).
   The department's statement goes out at ten (the channel, said —
   this is how the county learns). By eleven Rhonda's plain post has
   crossed rooms: call 1's DEFAULT — DeeAnn Prewitt (local; the car
   with the heat on at practice, ch 12:104; a real-name poster) puts
   it in the town room (lost dogs, road work — town-ashford 410–420)
   with a line of her own, and the town room TURNS on her, not on the
   doctor: this isn't the room for it; some of us are here for the
   recycling schedule — the waffle register turned cold. It costs
   DeeAnn (rule 7). No moderator acts (the town room's mod is OPEN —
   nobody deletes). Dan reads it at his desk — the habit with its
   why in a clause (a board knew first; the football hidden in the
   ordinary talk — B2-T08): he is looking for what the town knows
   about the review and finds the town cares who brought it in. ON
   THE PAGE: two posts and one reply quoted in blocks, the rest told.
   Beside it, the vote: the Millrow rezoning in three replies about
   parking — the town's whole reaction. THE VOTE'S MEANING, one plain
   sentence in his read (keeper B3): Tuesday night the aldermen
   rezoned the town's side of Millrow so Boyd's building can cross
   the street; the ground under her clinic is the university's, and
   it goes to the trustees in February with her job. No vote count
   on the page (`[TK the count]`); no new stake in the ground (ch 23's
   flags stand; ch 26 owns the stakes).
4. **Noon, the annex lot** (the window — THE LEADS' SCENES above). He
   knows she is in the lot from the Fieldhouse window on it (ch
   21:299; registry) — a clause; he goes down the stairs and across,
   NOT ch 22's walk (vary it: the rain; the lot's water). Her ONE box
   (the day's: the tablet, the parka, the mug — NOT a review letter,
   the email has no paper; NOT the office — ch 25 is the boxes); the
   RAV4 with the engine running and the heat on; the trainer in the
   warm-end door, seen, NOT named, NO drop — his pull in where he
   stands; a staff car at the fence (NEW; unnamed). Who covers the
   clinic for the fortnight (ankles due back through the 28th): one
   clause or `[TK the cover]`. The knuckle on the glass; four inches;
   his body first, four beats or more; "Film's at four" — the WHOLE
   line, nothing else; she does not ask; the window up. SHE LEAVES
   AT NOON, in daylight — the RAV4 takes Millrow down with the county
   watching, and he watches it from the lot (keeper B2: the
   taillights are noon's; there is no five-hour hole). The walk back.
5. **Four, the film room; six, the Checkerboard** (the count; the
   anchor; FUN). Film at four with the staff — Ty ("Coach," and
   nothing about the statement; Ty knows how to be on a staff);
   nothing sent, and the page does not stage a phone for it (ch 20's
   shape). Six, the Checkerboard counter — allowed HERE, not as the
   opening: Earlene at the window with the pot, Tunk (NOT an alderman
   on this page — `[TK Tunk on the board]`), the cook; the vote has
   reached the counter by mouth (never "the minutes" — the Courier is
   weekly; the paper unnamed); the statement reached it at ten. THE
   TABLE COUNTS — a woman put on leave and a street rezoned in the
   same four days, and nobody at the counter says the name in both
   (F3 discipline). EARLENE'S ANCHOR, SPOKEN (she does not type —
   ch 9, ch 12:463): the card's meaning in her own words — they
   didn't fire her; they invited the county to do it for them; the
   week's other news anybody can count — NOT the outline's wording
   (keeper B6). One laugh Dan loses (the cook's or Tunk's). The Slice
   set down unasked (registry 73). No phone on the counter, face up
   or down (keeper B5 — banned).
6. **Dark, the annex** (the ending). Not the Fieldhouse window (spent:
   15, 16, 21, 23), not a phone at night (20, 22, 23), not a person in
   a running car (21, 22). He drives across to the annex at dark: the
   clinic is still lit — whoever covers it — and the warm-end door is
   unlocked because the clinic is open (ch 19:195). Her office door
   stands open; the chair; the desk with the tablet gone; the file
   drawer shut. He stands in her door with the sentence he did not
   say whole in his head one more time, and does not go in. ENDS
   DOWN, held-quiet, the worst one — a coach in a doctor's empty
   office door, and the building open around him. Call 3's DEFAULT
   (revised after the keeper): her office door; the alternative the
   Fieldhouse window.

## THE AUTHOR'S READ (studio/AUTHOR-QUESTIONS.md; L056)

| Scene | MORE | WHO | CONFUSING | NOSE | POINT | SENSES | FUN |
|---|---|---|---|---|---|---|---|
| 1. Before seven, the door | Romance felt 3: her name under his in the address line — one body beat in the rain; the arithmetic is his and it is about her | Dan: conflict 2 — the job against her in the way he reads it twice; the athletic director: wants the county to do it (unnamed, he) | Wednesday the twentieth said; Monday night and Tuesday in a clause each; "pending review" glossed once — fourteen days, the third of February, signing day; nobody else knows yet, said | Nobody explains the email's shape; the italic lines do it | The point: the county is being handed the firing. The stake hinted once: caught in season, both gone that day (D30.1) | The first rain since the ice; the wipers; the water off the hill; the key in the lock | — (a hit by design) |
| 2. Before eight, his office | Romance felt 4: what "her" does in the lawyer's mouth; the hand in the pocket — two beats | The lawyer: wants no statement, ever; the press woman: wants the athletic director's words to be the only words; LIKE neither, HATE neither — they are right; Dan: conflict 3 — the sentence whole in his head and he agrees to keep it; the reader should hate him a little | Who these two are (one clause each, unnamed; sent up by the athletic director's office); the door shut BY THE LAWYER, said; the statement at ten, said | Nobody says "cowardice"; the page shows him agreeing | The point: he chooses the job. Fourteen-hour days, his side (D30.3) | His office; the rain on the lot; the shut door | — |
| 3. Ten; the town room | Romance felt 3: her name in a room that does not care — one beat | DeeAnn: wants to be first; conflict 2 — the room turns on her; the town-room regulars: want the recycling schedule; Dan: the habit with its why | Ten: the statement, the channel the county learns by; which room (the town room, lost dogs); who carried it (DeeAnn, real name); the vote's MEANING in one plain sentence (the town's side of Millrow rezoned; the university's ground goes to the trustees in February with her job) | Nobody explains rule 7; the room's own replies do it | The point: the town's verdict is a shrug, which is worse. The vote's price said blatantly, once | The desk screen; three replies about parking | The town room's reply is the funny register turned cold — the reader laughs once and then does not |
| 4. Noon, the annex lot | Romance felt 6 (the peak): his body at the four inches — four beats or more, no touch; the sentence whole; the confusion plain: he wants to say it and is not going to | Aisha, seen: wants nothing from anybody; conflict 3 — she does not ask, and it costs her (his read: nobody has ever spent anything on her); the trainer in the door: no side, conflict 1; Dan: conflict 3 | Noon said; how he knew (the window on the lot); her one box (the tablet, the parka — not the office); who covers the clinic — a clause or TK; the window four inches; SHE LEAVES AT NOON, the RAV4 down Millrow in daylight | "Film's at four" is the whole line — nobody says "I can't say anything" | The point: the couple's worst hour. The county watching a coach cross a lot to a suspended doctor — one clause of what that is worth | The lot's water in the rain; the RAV4's exhaust; the glass; ch 23's flags still in the ground, no new stake | — |
| 5. Four; six, the Checkerboard | Romance felt 3: the sentence whole in the film room — one beat; none at the counter | Ty: "Coach," conflict 1; Earlene: wants the county counted straight — conflict 1, and the anchor SPOKEN; Tunk: wants the gossip (not an alderman here); the cook: the griddle | Film at four (no practice till spring); six at the counter said; how the vote and the statement reached the counter (by mouth; at ten) | Nobody explains the Slice; the count is Earlene's, not the narrator's; the anchor in her words, not the outline's | The point: the Table sees the tell and says it as a shrug. Nobody says the name in both | The griddle; the pot; the rain on the square's glass | The room the reader wants to stay in; one laugh Dan loses — what takes the edge off two Fun 0 chapters (the FUN cell earns its keep here) |
| 6. Dark, the annex | Romance felt 5: her empty office — the ache in his terms, three beats (the chair, the desk, the door he does not go through) | Whoever covers the clinic: one clause; Dan: turned — the person at the end would decide the same, and knows it | Dark said; the clinic lit and why; the warm-end door unlocked because the clinic is open (ch 19); where she went (down Millrow at noon; not said where) | Nobody says "he had chosen the job"; the page shows him not going in | The point: the silence he must buy back (ch 27). Ends down, held-quiet | The corridor's heat; the tank off; her office with the tablet gone; the rain on the annex roof | — |

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
| Dan | caught in season, both gone that day; his second time ends him in college coaching (D30.1, F-DAN-02); the extension on the February agenda | ONE hint in his read (scene 1 or 2), in the drafter's words — never plain again this chapter |
| Aisha (seen) | suspended; her job on the February agenda under a politer name; the review is the paper | scene 1, his read, once, in the drafter's words: the review is the paper that lets the trustees vote her job to the group in February without anybody saying her name (D30.4) |
| Boyd (absent, unnamed) | the pledge; the building — the town's side of Millrow REZONED Tuesday so it can cross the street; the ground under her clinic is the university's and goes to the trustees in February with her job (keeper B3) | scene 3, his read, one plain sentence of the vote's meaning; scene 5, the Table's count in its own words — a street rezoned and a woman put on leave in the same four days, and nobody at the counter says the name in both. In the DRAFTER'S words (no example sentence — keeper B6) |
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

Not a phone at night (20, 22, 23). Not a room with people (22). Not
the Fieldhouse window (15, 16, 21, 23). Not a running car (21, 22).
Her empty office door at the annex, the building open, the sentence.
The worst one. Down is not wry and not a button.

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
- BANNED (keeper B5, B6): a phone on the Checkerboard counter; a phone
  face up or face down as a beat; the email's text as the brief had it
  ("placed on administrative leave pending an independent review of the
  December medical determination; the review's findings will be
  published within fourteen days" — the drafter writes the athletic
  director's own sentences); "On the Wednesday the aldermen's vote made
  the paper"; "a coach caught with the team physician in season was
  gone that day, and so was she"; "the review was the paper that let
  the trustees vote her job"; "the aldermen had voted the ground under
  her clinic"; "They didn't fire her. They invited the county to do it
  for them. Y'all can count the week's other news yourselves" (the
  anchor keeps the MEANING in Earlene's own words); "the minutes";
  "five to two"; a new stake in the annex ground; "through the wall";
  "the review letter"; "till the poles go off"; lights going down
  toward the square.
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
3. It ends in her empty office door at the annex at dark (revised
   after the keeper — the Fieldhouse window is spent four times; his
   house with the statement unsent is a phone-at-night shape).

## AUDIT ADDENDUM — ch 24 card + brief (continuity-keeper 1.4.4, card E1, 2026-09-21) — BLOCK, then corrected in the body above

KEEPER — ch 24 card + brief audit (continuity-keeper 1.4.4, card E1; L053 standing). Read: card, brief whole, ch 5/12/14/19/20/21/22/23, outline 24–27, dossiers, arc-docs, romance-arc, boyd-arc, STAKES, BEATS, TARGETS, FACTS, NAMES, town-ashford 120–240 and 395–470, grapevine §2/§4, registry, THREADS, DECISIONS D28–D30, ch 23 keeper note, AUTHOR-TASTE. No file edited. Card vs brief: no promise contradicted; the brief overreaches the card in three places (below).

A. TRANSITIONS AND WHAT THE BRIEF DID NOT STAGE
- Six: the email reaches Dan's phone at the counter. Nobody else at the counter can know it. The brief's Table "counts a woman suspended and a building approved" at six, and Earlene's anchor is past-tense ("they didn't fire her") — the card places it after the fact. The brief never says HOW or WHEN the town learns of the suspension (the press woman's "the athletic director's statement" implies one; no hour, no channel).
- Six → before eight: who summoned the lawyer and the press woman — a clause.
- Mid-morning → noon: how he knows she is in the car — the Fieldhouse window on the lot (registry 110–111; 21:299) — a clause; he crosses on foot (ch 22's opening shape — vary the walk).
- Noon → dark: she sits in a running car with one box at noon; her taillights take Millrow at dark. Five hours unstaged, and a suspended physician's right to be in the building is on no page.
- Monday night and Tuesday: ch 23:474 does not know which building he was in; no page places Dan Tuesday (the vote night). Owe a clause: where he was, and whether he opened the board Monday night (ch 22 he skipped it once).

B. THE FACTS
- Calendar CONFIRMED: Jan 1 is a Friday (ch 18) → Tuesdays 5/12/19; Jan 19 is the third Tuesday (ch 14:362); Mon 18 (ch 23:28); Wed 20; 20 + 14 = Wed Feb 3 = signing day (ch 23:386). "Fourteen days / a fortnight / the third of February" all true.
- Email shape CONFIRMED against registry 26/27 and ch 5:359–370: her name under his, italic lines, no header, "the athletic director," he; "medical determination" is his phrase. "Administrative leave" is new wording (the card says "suspended") — either.
- "Film's at four" CONFIRMED: no practice till spring (ch 20:240–243, 21:48); staff film in January is on the page (ch 20:199; ch 23:161). Dossier-dan row 24 "practice is at four this week" CONTRADICTS canon — conform the dossier at the fold; the page never says practice.
- Ladder CONFIRMED: romance-arc row 24 In 5/Out 5 spends nothing; glass, no touch, no rung.
- DeeAnn CONFIRMED able to carry: local (ch 12:104 "sits in that car at practice every day with the heat on" — the dossier's rhyme is deliberate), real-name poster (ch 12:125). Rhonda is out-of-state (ch 23:286) — the alternative (a regular reposts, Rhonda pays twice) cannot cost her in a room she is not in; the default is the canon-safe call. Town-room moderator OPEN (town-ashford 421) — no deletion, no mod on the page.
- The lawyer and the press woman: no canon anywhere (grep of manuscript, town-ashford, canon, provider-partner: nothing). Unestablished, acceptable as two unnamed figures; the athletic director alone could carry it (ch 5's shape; STAKES proposed row). Author's pick; registry rows owed.
- Who conducts the "independent review": no page. `[TK]`. Earlene's "the county" is her framing — Deliberate, never a fact.

BLOCKING
1. The six o'clock count — the counter cannot count what only Dan's phone knows. Fix: the count at six is Dan's alone in his head; the Table's count and Earlene's anchor come after a stated channel (the department's statement at a named hour, or Delores/Tick by mouth) — one scene, one channel, said.
2. Noon → dark gap (L053). Fix: the page says where she was for five hours and why she is still in the annex suspended, or the taillights are noon's, seen in daylight — pick one and say it.
3. "The aldermen voted the ground under her clinic to a building" — CONTRADICTION. The annex is on campus (ch 5:43); the university is immune from town zoning on its own ground (town-ashford 200–203); the aldermen's vote is the Millrow parcels rezoned to Planned Institutional (207). Fix, one sentence for drafters: Tuesday night the aldermen rezoned the town's side of Millrow so Boyd's building can cross the street; the ground under her clinic is the university's and goes to the trustees in February with her job.
4. Earlene posting under her own name — CONTRADICTION: "I don't type" (ch 9), "She doesn't type, so I'm typing it" (ch 12:463; registry 80). Fix: spoken at the counter, or relayed by B. Hollis in her words.
5. E1 — the opening recites ch 12's (phone lit on the Checkerboard counter, Earlene with the pot, the Table at the window) and ch 20's (Earlene and Tunk at the window, the Slice set down), and breaks the brief's own PROOF line 46 "NOT the counter." Fix: open elsewhere (the wipers, the first rain — candidate 3); if the counter stays, the phone-on-the-counter beat and the face-up/face-down motif (registry 15, 82; ch 12:16, 12:477, 22:428) are banned.
6. Rule 4 — the brief quotes six sentences as examples (the email text, the stranger's sentence, the three STAKES sentences, the anchor's outline wording). Three drafters converge. Fix: put all six on BANNED; each line must do its job in the drafter's words; the anchor keeps the card's meaning, not the outline's words.

NON-BLOCKING
1. Tunk Ferrell is a PROPOSED alderman (town-ashford 226, 1.4 casting), as is Delores (227) — 1.2 pages keep Delores outside the body (ch 23:340, 368). "Tunk on the aldermen" must not seat him or vote him — `[TK]`.
2. "The paper folded to the aldermen's minutes": minutes are hand-kept (191), not printed overnight; the Courier is weekly (139); the Table's paper is unnamed (12:40, 20:30). The vote reaches the counter by mouth, or as a line in the unnamed paper — never "minutes."
3. "Five to two" — NEW canon, `[TK]`, seven aldermen (mayor ties only). Never call it the vote that approves the whole footprint; 1.4's street vacation is 4–3 against Boyd (214). No hearing, sign or procedure beyond ch 23:340.
4. The new orange stake at the annex's corner — campus ground; a town vote plants nothing there; ch 23's flags already stand between annex and fence; ch 26 owns the stakes walking the lawn. Keep ch 23's flags; no new stake.
5. The office door shut (scene 2): every Fieldhouse door stands open by his rule (ch 20:127; registry 113). If shut, the lawyer shuts it and the page says so.
6. "The review letter" in her box — the email has no paper form (registry 26). Drop. The tablet and the parka are what she carries daily (ch 23:128). Who covers the clinic for the fortnight (ankles due back through the 28th, ch 23:167, 207) — a clause or `[TK]`.
7. "The projector fan through the wall" — office/film-room adjacency is on no page (ch 12:386). Drop "through the wall."
8. E1, beyond the opening: the Fieldhouse window at dark is spent at 15, 16, 21:299, 23:349 — the ending may stand at it but not in the "till the poles go off" shape (registry 111, 120); "lights going down toward the square" is Tick's van (22:409–411); a person in a car with the engine running is 21:445–486 and 22:416 — vary; "the phone with nothing sent" is ch 20:496–522.
9. Fun 0 after ch 23's author-scored 0 is a finding by TARGETS 112–113 unless Kat's surprise (D30.6) lands in ch 23. Orchestrator's call.
10. Hands-forward: Kat's surprise is Aisha's — rightly absent; the fourth call (she tells him of Boyd's offer) stays unspent — say so; Ty's stake is proposed only — "none" is right.
11. Taste risked: 6 (the counter opening), 1 (the noon–dark hole), 18 (the vote must say what it means), 21 (who the lawyer is), 7 (two Fun 0s), 22 (blatant, and true).

New canon this brief makes: the lawyer, the press woman; the town room's turn; the first rain since the ice; a staff car at the fence; the parking replies; the vote count. Open markers: `[TK the vote]` (brief); add `[TK who conducts the review]`, `[TK Tunk on the board]`, `[TK the clinic's cover]`.

## VERDICT: BLOCK — B1–B6 corrected in the body above (the count moved behind the ten o'clock statement; she leaves at noon in daylight; the vote's meaning in one sentence; Earlene speaks; the opening moved to the rain and the door; the six example sentences banned); N1–N8, N10 applied; N9 (Fun 0 twice) is the Kat call on #181; the brief now passes

KEEPER: blocking 6 · non-blocking 11 · TK 4
