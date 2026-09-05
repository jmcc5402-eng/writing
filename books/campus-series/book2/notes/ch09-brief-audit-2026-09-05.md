# CH 9 BRIEF AUDIT — continuity-keeper (blocking), variance card E4 (transitions)

**Read:** the brief; `b12-outline.md` :184–278 and :440–520 (plus :211–237, :728–741); `romance-arc.md`; `arc-docs.md`; 1.2 ch 1, 3, 4, 5, 6, 7, 8 (7 and 8 whole); `town-ashford.md`; series `DECISIONS.md`; series `THREADS.md` (index + S01 row); book2 `THREADS.md`, `DECISIONS.md`, `STATE.md`; `furniture-registry.md`; the Grapevine realism rulebook; `studio/SHARED-CANON.md`; `DIALS.md`; `STYLE.md` (closeness ladder, Romance first, the say-it test at :396–428); `RECENT.md`; `AUTHOR-TASTE.md`; Book One ch 30 whole, plus ch 3, 6, 7, 8, 9, 12, 13, 19, 24, 28 at the cited lines; Book One premise v2 :190–203, :314–361; `studio/tools/romance-build-check.py` (source).

**No shell.** I could not run the build check. I read the tool's source and ran its rules on the arc-doc table by hand. The result is under item 8.

**Card E4 note.** Where the card touched a finding, I say so. It changed nothing about what counts as a finding.

All paths below are under `/home/user/writing/books/campus-series/` unless they start with `studio/`.

---

## FINDINGS

### F1 — Cordelia "a hundred years dead" cannot be true. CONTRADICTION — blocking (cleared by addendum)

The brief tells the drafter to put the letter's age on the page: "a hundred years dead" (`book2/plots/brief-ch09.md:12–13`, :154–155), "age (a hundred years, by the hand and the paper)" (:238–239). The phrase comes from the outline (`book2/plots/b12-outline.md:450–452`) and the canon arc-doc row (`book2/plots/arc-docs.md:44`).

Canon says Cordelia was alive within the last sixty years:
- `town-ashford.md:156–161` — the Magnolia Court Motel dates from 1962, and Aisha's room nine is "Cordelia's room." Verna's canon line: "Cordelia Hartwell stayed in room nine" (:261–262). A woman who slept in a 1962 motel room was not dead a hundred years before Year 1.
- Book One ch 3 (`manuscript/ch03.md:391`) — Verna: "Sixty years of honeymoons at the Magnolia Court."
- Book One premise (`plots/book-1-1-premise-v2.md:318–321`, :336–338, :349–350) — the porch light "has not been off in living memory"; "fifty years of never turning the light off"; Verna is "the last living witness to what the light was for." Cordelia made the trust promise. So she died roughly fifty years back, inside Verna's adult life.

Both cannot stand. The census is ratified canon (D04) and Book One's engine rests on it. The arc-doc row is canon too (B2-D05) but its phrase is a gloss inherited from the outline, and no accepted page has ever printed "Cordelia" (grep across both manuscripts: zero hits). The fix costs the chapter nothing: the LETTER may be old; the WOMAN may not be dated. The letter went to "the infirmary's night nurse," and the annex is "the old WPA infirmary" (`b12-outline.md:211`; `book2/plots/premise.md:190`), so the paper is at most about ninety years old anyway.

**Fix:** ch 9 says Cordelia is dead (Verna's past tense does it), ages the paper and the hand without a number, and never says how long she has been dead. Read the arc-doc row as "long dead," by annotation, the way the ch 7 row is read (`arc-docs.md:110–135`). Cordelia's era goes to the author as `[TK]`. The addendum text is in the verdict.

Related, same object: **no year on the page** for the letter. D05 (`DECISIONS.md:95–105`) bans any date that lets a reader anchor Year 1. A year on an envelope plus "a hundred years" on the page does exactly that. Also: the carton "KNEES, 1994" is on the page (`book2/manuscript/ch07.md:254`); ch 9 may cite it but may not subtract it from today.

### F2 — "The two plates on the rail as she left them" is not in her knowledge. CONTRADICTION — warning (an addendum removes the option)

Brief, romance beat 1 (`brief-ch09.md:129–131`): "the two plates on the rail as she left them." On the ch 8 page she set ONE plate down and left (`book2/manuscript/ch08.md:351–354`); her car started (:355); Dan then "built himself a plate he did not want so that hers would not be sitting up there by itself" (:356–357). The two-plates image is Dan's, after she was gone (:464–467). She can carry her own plate, one rib, one bite gone. She cannot carry the pair.

**Fix:** beat 1 is "a line of his from the rail, kept" or her own plate. Strike "the two plates."

### F3 — Friday's medical check happened between ch 8 and ch 9; Saturday's practice is unruled. DECIDES-OPEN-QUESTION — warning (card E4: this is the seam into the chapter)

The brief's romance move (:40–41): "Two nights ago at the rail… Today she has heard nothing." True for Saturday. But the day between was Friday, and the Friday check is the book's spine: "Every Friday since June… printed, every Friday of the season" (`ch02.md:288–293`), moved to 5:15 on the turf with Dan running practice at five "till the nineteenth" (`ch07.md:308–317`; "Five fifteen tomorrow. It'll be printed," :415; registry :36). So she stood on the turf with him Friday, off the page. A drafter who writes that she has not seen him since the porch makes a contradiction.

Saturday itself: the moved practice "stays there till the nineteenth" (:308–309). Whether it runs Saturdays is on no page. The brief says "a Saturday with no game" (:59) and never says "no practice."

**Fix (default, strikeable):** one line that Friday's check ran at 5:15, printed, and neither of them said the word porch — this is the "He did not answer her" carried forward and it is a clean kind-4 beat. One line, or silence, that Saturday is the roster's off day; if said, it is canon after. Ch 9 must not stage a Saturday check.

### F4 — The Curb Market in December is unruled, and the census leans closed. UNESTABLISHED — warning

Brief scene 4 (:104–106) offers "the Curb Market shed." No 1.2 page names the market; Earlene "sells the eggs" and "We met in June. At the eggs" (`ch01.md:60–62`) is all there is. The census lists it as a Saturday shed market (`town-ashford.md:164–167`) and, under Spring, says "The Curb Market reopens with onion sets" (:293) — which implies it closes for winter. Book One shows it breaking camp at noon on Saturdays in September (`manuscript/ch13.md:16–24`) and its vans catering the November hearing (`ch28.md:30`). Nothing gives a close date. Using the shed on a December Saturday decides that question on the page, against the census's implication.

**Fix:** default to the annex door (or a Saturday stop at the Checkerboard counter, where Earlene sits — `ch05.md:119–122`). If the drafter wants the shed, it is an author ruling, not a drafter choice.

### F5 — "Verna, delivering towels (canon: Verna's arrangement, never charity)" cites the wrong canon. UNESTABLISHED — warning

The towels are the outline's own line (`b12-outline.md:460–461`). No page or doc has Verna supplying the annex. The census's "Verna's arrangement, never discussed as charity" (`town-ashford.md:161–163`) is the BACK-ROOM displacement on home Saturdays (on the page at `ch03.md:330–343`). The towels are new canon. That is fine — it fits her (the blanket `ch01.md:332–337`, the plates `ch03.md:304–307`, the saltines `ch07.md:452–453`), but the drafter must say the arrangement plainly once, and the brief must not call it canon. Small rider: Verna walks everywhere on the accepted pages (`manuscript/ch12.md:187–188`, `ch24.md:195–196`, :236); how she gets towels up to campus is unestablished — a vehicle would be new canon.

### F6 — The House is not on the way home. UNESTABLISHED (geography) — warning (card E4: scene 5's entry)

Brief scene 5 (:111–115): "Millrow, from the truck… Up Millrow." Canon geography: the annex sits between the stadium's north side and Millrow's LOW end (`b12-outline.md:211–215`); Millrow climbs from Delmar's low end to the House at the HIGH end (`town-ashford.md:396–399`; `manuscript/ch09.md:112`; `ch06.md:84–85`); the Magnolia Court is "off past the square" from Delmar's porch (`manuscript/ch09.md:271–273`), on the far side of the square from Millrow. From the annex, the motel is down and across the square; the House is up the hill the other way. She does not pass the House going home.

**Fix:** give her the drive on purpose — one clause that she went up Millrow instead of home. That is the right choice anyway; she goes to look at the town's other rescue and does not say so. Two riders: the sighting must be by DAY (coffee is Book One's, by day — `book2/DECISIONS.md:74–82`; brief :224–226), and the crew works "till dark" (`manuscript/ch30.md:188–189`), so this scene sits before December dusk even though it is in the last third. "The scaffold path" is new and fine.

### F7 — Verna and the boxes: the vacate order leaks by supper. STAGING — warning (card E4: scene 3's entry and exit)

The brief fences the vacate order as not public (:232) and puts Verna, "the town's guest room and its gossip clearinghouse" (`town-ashford.md:159`), inside the annex while thirty years of paper is going into boxes. If she sees the records room, the town knows tonight. The drafter must stage the handoff at the cold-end door or in a rehab room (the whirlpool is where towels belong — `ch07.md:244–248`), not in the records room, or must play Verna seeing and choosing silence, which is its own beat and new canon about her.

### F8 — Her vehicle is "the truck" and "her car" on accepted pages. UNESTABLISHED — warning

Truck: `ch01.md:320`, `ch07.md:278` (her POV). Car: `ch03.md:274` (her POV), `ch08.md:355` (Dan's). Ch 9 should say "truck," per the brief and the registry's nine-minute-pack row (registry :12). The registry owes a row, and it matters before ch 12: RH1's honest signal is a crew-cab truck that is not Dan's (`b12-outline.md:262`). Two leads in trucks muddies that decode.

### F9 — "No coffee for Aisha" is a chapter ration, not a character fact. CLARIFICATION — warning

She drinks coffee by day on three accepted pages (`ch05.md:174` "second cup"; `ch07.md:52`, :205 "Eggs and coffee"). B2-D03 bans coffee at night and makes it Book One's object. The brief's rule (:224–226) is fine as this chapter's ration. The draft may not write that she does not drink coffee.

### F10 — The whiteboard does not hold three calendars. UNESTABLISHED — warning

Audit item 1 says "three calendars on the whiteboard." The page: "The whiteboard held its two calendars. The mail had brought a third." (`ch07.md:271–272`). The third is the memo, under the stapler (:292). FEB 11 is on the board only if ch 9 writes it there. Also the board is in her office at the warm end (`ch05.md:48–49`, `ch07.md:93–96`, :106), not in the records room — scene 1 cannot see it without a walk.

### F11 — "One person she has treated" must be a townsperson. STANDARD — warning

Series standard 1: no students as active characters; no named student carries dialogue or POV (`STANDARDS.md:21`, :42–47). Her patients who are on the page are townspeople: the bonfire's burn table and the Scout's thumb (`ch01.md:120`, :342–346). An athlete looking past her at the annex door fails the chapter test.

### F12 — "The people who thanked her in the tent." UNESTABLISHED — low warning

Nobody thanks her on the ch 3 page (grep "thank" in `ch03.md`: zero). The memory may stand unnamed. The draft may not name who thanked her.

### F13 — The brief's ch 8 citations. WARNING (housekeeping, two items)

- The brief says ch 8 "ended DOWN ('film at five')" (:123, :177), and THREADS says the same (`book2/THREADS.md:232`). The ch 8 page ends on the two plates (`ch08.md:464–467`). "Film at five" is Dan's on-air line (:121). The DOWN register stands; the quote does not.
- The ch 8 header still reads "PROPOSED, not accepted until the re-cut PR merges" (`ch08.md:7–8`). THREADS records it ACCEPTED at #127 and #129 (`book2/THREADS.md:213`). The header is stale.

### F14 — "Fieldhouse" capitalization drift. WARNING (polish debt, not ch 9's)

`ch07.md:34` "from the fieldhouse"; `ch06.md:34` and `ch08.md:139` "the Fieldhouse"; outline roster capitalizes (`b12-outline.md:223`). Ch 9 and ch 10 use "Fieldhouse."

### F15 — The epigraph's hard limits are not in the brief. NOTE

`studio/SHARED-CANON.md:63–69`: hard cap 35 words for the whole epigraph, one to three posts, no timestamps, real names for citizens, bold frame with colon. The brief's "~3 posts" (:227) fits only if short — ch 6's three posts run about fifteen words. Frame line for 1.2 is fixed: `On Grapevine, the Ashford parents' board —` (:48). If the chapter renders board text in-scene as well, SR-EPI-2 applies: no colon after the name in-scene (`ch08.md:440–454` is the model).

### F16 — The arc-docs header. HOUSEKEEPING

`arc-docs.md:3–5` still says "PROPOSED… Nothing below is canon until this PR merges." B2-D05 made it canon (#114). Stale header; no effect on ch 9.

---

## AUDIT ITEMS, ANSWERED

**1. State in from ch 7 and ch 8 — all confirmed on the page.**
- Memo under the stapler: `ch07.md:292`, :336. Text :227–234. Addressed to OCCUPANT PROGRAMS, ATHLETICS ANNEX (:224).
- Calendars on the whiteboard: TWO, plus the memo — see F10. DEC 19 circled (`ch05.md:24–25` "twice in red"; `ch07.md:106`); the six-rung ladder REST→GAME with no dates (`ch05.md:33–37`).
- Facilities' mailbox full: `ch07.md:261–263`. "Facilities will provide boxes": :233–234, :257.
- Practice moved to five, film first, till the nineteenth: `ch07.md:308–310`. The check at 5:15, same half hour, on the turf, typed by Dan: :314–319, :415. Meeting room held at seven, projector unplugged; "His mother drives him": :320–328.
- The parka: team issue, navy, staff patch, A. COLE in block letters over the patch, tag XXL (`ch07.md:98–100`); hem below the knees, sleeves past her hands (:157–159); "Roll the cuff under, not over. Twice around. The liner grips itself" (:154–155); cuffs rolled and holding at chapter's end (:492–495). HIS spare, re-badged — outline :244 (B2-T02); nobody on the page knows; the only man who knows is the equipment manager, absent here. The banked ch 29 line may not appear. Verna's pins are Sunday after church (:462–465), so on Saturday the cuffs are still rolled, not hemmed.
- Kat's three listings, by text, each with a February in it: `ch07.md:479–487`.
- Ch 8's porch: the rail exchange verbatim `ch08.md:301–349`; "He did not answer her." :349; her plate :351–353; her car :355; the board's three posts :440–454 (Tim Brasher, Rhonda Sipes "talking down to families on the radio," Kendra Voyles). She reads the board silently — Verna added her in June, "so you'll know things before they know you" (`ch01.md:179–182`). Verna was on the step beside her at the Table (`ch08.md:52–53`), so Verna witnessed Thursday. Boyd's line to Dan (:359–365) came after she left; she may not carry it.

**2. The records room as ch 7 staged it:** "thirty years of files in four cabinets, and two walls of boxes that were already boxes, her predecessors' handwriting going back past ballpoint. A shelf of X-ray film in brown sleeves that no machine left on this campus could read. A taped carton marked KNEES, 1994." (`ch07.md:249–254`; also `ch05.md:44–45`). The annex: one corridor at the cold end of campus, four rehab rooms, the water fountain, the records room, her office at the warm end (`ch05.md:42–52`); the rehab rooms' contents (`ch07.md:244–248`); the outside door at the cold end with its two-stage bang (:299, :419). **The key hook is on no page.** It exists in the outline (:449) and F5 (:260) only. Ch 9 introduces it. Nearest rhyme on an accepted page: "in June nobody could tell her whose key they were handing her" (`ch05.md:46–47`).

**3. The Book One couple — confirmed.**
- Names: Marisol Pruett (`manuscript/ch15.md:8`, `ch25.md:223`, `ch28.md:141`; in 1.2 as "Marisol Pruett's boy," `book2/manuscript/ch06.md:150`). Cal Sutter (`manuscript/ch01.md:294`, `ch28.md:184`; in 1.2 `ch01.md:191`).
- The House at Millrow's high end: `town-ashford.md:396–399`; `manuscript/ch09.md:112`; `ch06.md:84–85` ("on its hill"). Its name is Hartwell House (`town-ashford.md:181–182`; `manuscript/ch19.md:27`, `ch23.md:21`). **No 1.2 page has named it yet** (grep "Hartwell" in book2 manuscript: zero). Say "Hartwell House" once for the new reader.
- Tarps and scaffold in winter: `manuscript/ch29.md:25–26`, `ch30.md:69–70` ("tarps still, scaffolding pearled with frost"), :307–308. The crew is contracted through March (`ch30.md:40–41`; `ch29.md:80`); it worked the House on a Saturday in ch 30, so Saturday work is canon. Crew names available: DeShawn, Ronnie, Travis, Cal's unnamed second, a woman (`ch30.md:129–147`).
- Coffee: Marisol brings the crew coffee — "coffee for twelve," two cardboard trays from the Checkerboard (`manuscript/ch19.md:44–49`); the steel thermos on the tailgate and the white mug (`ch30.md:214–219`); "I bring the coffee. That's the arrangement" (`ch09.md:118–119`). Cal taking his cup rhymes with the cup crossing (series THREADS T12). Saturday is Marisol's own day (D12, `DECISIONS.md:288`).
- May they stay wordless? Yes. Nothing in canon obliges them to speak; Cal's tell is doing things without speaking (T02, `THREADS.md:37`); the outline's mandatory fix 2 orders "two lines, no stakes" (:454–459). Confirmed.
- One thing the brief does not say: **Aisha knows them.** She is a wine-night regular in Book One (`manuscript/ch07.md:193–303`, `ch17.md:187–225`, `ch22.md:329`, `ch25.md:185–349`). In her POV they are friends, not figures. The camera moving on has to be her not stopping.

**4. Verna's canon — confirmed; the towels are new (F5).** Voice: "flirtatious past tense" (`town-ashford.md:259–262`); on the page her "Mm" (`ch07.md:437`, :469), the fur collar "older than the interstate" (`ch01.md:158–159`), "my winter doctor. I rent her the quiet end" (:162–163), "They hem these with a mower" (`ch07.md:440`), "Noon was noon" (:452). Never soft: `ch03.md:298–309`. Book One: "I have watched fights on this porch for sixty years" (`manuscript/ch08.md:222–225`), the Mule doorway (`ch24.md:203–231`), "Sixty years of honeymoons" (`ch03.md:391`). **The room-nine line is unspent on any page**; ch 9 is its first spend, verbatim: "Cordelia Hartwell stayed in room nine. I don't say that to everybody." (`town-ashford.md:261–262`). Verna at the annex contradicts nothing; see F5 and F7 for what it needs.

**5. Earlene — confirmed.** She is the front-row grandmother by ruling (SR-B2-19, `book2/DECISIONS.md:220–222`; on the page `ch06.md:94–95` "Earlene Tatum was already patting the wood. 'I don't bite.'"). She IS on a page since ch 6: ch 7, the Checkerboard at noon Wednesday (`ch07.md:187–200`, "Leave the doctor's coat alone"). Not in ch 8. Earlier: ch 1 (:58–62, :162–167, the anchor :227–231), ch 5 (the Table, :119–198). Census: egg-and-dahlia vendor at the Curb Market, the Liars' Table's only woman, 71, "declarative, unhurried, correct" (`town-ashford.md:246–247`); the age stays off the page; "unhurried" is a banned word in prose. The Curb Market is on no 1.2 page (F4). RECENT: ration Earlene opening a beat with "I didn't say anything" (`studio/agents/variance/RECENT.md:59–60`).

**6. The board vs. the epigraph.** Names on the page: Tim Brasher (ch 2, 4, 6, 8), Rhonda Sipes (ch 4, 5, 6, 7, 8), Kendra Voyles (ch 1, 2, 3, 6, 8); all three are the 1.2 poster registry (`studio/SHARED-CANON.md:121–127`). One new real name is allowed (the registry cap is four or five regulars, :105–107). The rulebook conditions the brief lists are right: grievance through a child (rule 1, `grapevine-realism-2026-08-29.md:169–174`); no plain-text pairing under real names — vagueposting only (rule 2, :175–181); the physician dogpile's shape is impatience framed as devotion, never incompetence alleged by name (rule 4, :187–194); Saturday-morning daylight register. Ch 8's posts already made it personal ("who does she think she is," `ch08.md:446`), so the epigraph continues that thread without escalating it. Add F15's limits (35 words, no timestamps). "Coach stayed in his lane" (`ch08.md:449–450`) is the accidental pairing the romance arc counts at stage 2 (`romance-arc.md:49`); the epigraph may not sharpen it — RH1 is ch 12.

**7. The calendar (A1) — one paragraph.** Canon says December 19 is a Saturday and February 11 a Thursday (B2-D08.2, `book2/DECISIONS.md:251–253`). The outline's week table puts the playoff in week five, so week three's Saturday — this chapter — is December 5, two weeks before the game. Chapter 7's accepted page counts differently: Aisha says "Nine weeks to the eleventh" on a Wednesday (`ch07.md:274`). Nine weeks before February 11 is December 10, which makes chapter 7's Wednesday December 9 and this chapter Saturday, December 12, one week before the game. The two cannot both be true. Option one keeps the outline's table. It costs three words on accepted pages: chapter 7's "Nine weeks" becomes "Ten weeks" and "Seven working weeks" becomes "Eight" (:274–275), and chapter 4's "The playoff. Two weeks out" — said on the night of the hit, which is four weeks before the game — becomes "Four weeks out" (`ch04.md:112`). Option two keeps chapter 7's count. Then this chapter sits one week before the playoff and the outline loses a week: chapter 10's Monday, chapter 11's Friday, and chapter 12's Saturday would all land inside playoff week, on top of chapter 13's Monday exertion test and chapter 16's game, and chapter 12's leak would arrive on game day. Chapter 4 would still need a fix ("Three weeks out"). Option two is closer to the real college calendar, where the bracket is set about thirteen days before the first round; option one is what the ratified outline (B2-D02) is built on. Recommended default: **option one.** It costs three words and no structure, and chapter 7's own arithmetic agrees with it — four cabinets at "half a cabinet a week" is eight working weeks, not seven (:275–276), and "I've held a room three weeks" (:328) rounds from December 2 to the nineteenth but not from December 9. Under either option ch 9 carries no day-of-month and no count to the nineteenth. "Two nights ago" for the porch and "tomorrow, after church" for Verna's pins are safe under both. Other Wk3 day-words already on accepted pages: freeze Monday night, Tuesday practice, Wednesday morning at seven, Wednesday noon, a little after six Wednesday (`ch07.md:19–20`, :93, :175, :299); Thursday night (`ch08.md:19`); "since Sunday" (:67); "two weeks back" for the card (:105). None contradicts "a Saturday with no game."

**8. The build check — run by hand from the tool's source against `romance-arc.md:71–102`.** Rules: no stage goes backward; inside leads outside by at most one; no jump of more than one; each spend lists two earlier chapters with a rung on the page. Spends: ch 5 want, earned by 2, 3, 4 (all earlier, all with rung text) — pass. Ch 8 want, earned by 2, 4 — pass. Ch 15 kiss, earned by 13, 14 — pass. Ch 27 claim, earned by 22, 26 — pass. Ch 11 inside 3 / outside 2 — lead of one, allowed. No backward moves; no jumps over one. Ch 26's Hole cell is non-empty, which the tool reports as a warning. The output the tool would print:

```
ladder: 30 chapters, stages 1/1 -> 5/5, spends: ch 5 want, ch 8 want, ch 15 kiss, ch 27 claim
WARN  ch 26: HOLE — [CHECK: is the standoff the private repair the ch 27 claim needs, or does ch 26 owe one?]
BUILD CHECK: PASS
```

Ch 9 spends nothing (`romance-arc.md:81`; brief :50). Note for the record: the check reads the table, and the table already lists the ch 2 fight and the ch 4 exchange, which are approved but still OWED on the page (B2-D09.3; `book2/THREADS.md:25`). Ch 9 does not depend on them. The stage stated in the brief (Stage 2, no new rung) matches the ladder row.

**9. The fact manifest** — below.

---

## THE SEAMS (card E4)

- **In from ch 8.** Ch 8 is Thursday night, Dan's POV, ending on the two plates and the board turned. Ch 9 opens Saturday in her POV. The reader's last sight of her was her plate on the rail and her car starting in the dark. Between them lies Friday's 5:15 check (F3). The opening paragraph is required to say the day and the stakes (brief :56–63); the Grapevine epigraph sits above it and may not carry the beat.
- **Scene 1 → 2.** Both in the records room; no move. The key hook is IN that room. The whiteboard is not (F10).
- **Scene 2 → 3.** Verna arrives from outside. The outside door is at the cold end and bangs twice (`ch07.md:299`, :419); she comes down the corridor to wherever Aisha meets her. Keep her out of the records room (F7). The letter is already in the coat's inside pocket when Verna speaks.
- **Scene 3 → 4.** If the annex door: no transit needed. If the market: an unruled place (F4).
- **Scene 4 → 5.** She leaves the annex in the truck and goes UP Millrow, away from home, by daylight (F6). The cameo is seen from a moving or stopped truck; the drafter must slow it honestly.
- **Scene 5 → 6.** Down Millrow, across the square, to the Magnolia Court: the lot, the office window lit, room nine at the quiet end (`ch01.md:308–315`; `ch07.md:423–428`). No game, so she is in room nine, not the back room (`ch03.md:330–333`). Objects waiting there: the wool coat on the closet rod with its woodsmoke, Verna's blanket, the near suitcase open, the far suitcase latched.
- **Out to ch 10.** Ch 10 is Dan's POV, Monday, the Fieldhouse, the consultant measuring the annex through the window (`b12-outline.md:468–478`). Ch 9 must leave the annex still hers and the vacate order still private; the letter kept; the boxes begun. Nothing in ch 9 may pre-empt ch 10's discovery that the annex is Boyd's money (arc-doc annotation 3, `arc-docs.md:129–133`).

---

## NEW CANON THIS DRAFT ESTABLISHES (write into the registry and bible on acceptance)

1. The key hook and the wall cavity behind it (records room).
2. The envelope: from Cordelia Hartwell to the infirmary's night nurse; the letter exists; read once; kept. Contents withheld (B2-T06).
3. The annex's town history, one sentence: the fevers, the WPA ward. Nothing beyond it.
4. Earlene's anchor, in her words.
5. Verna's towel arrangement with the annex (and how she gets there).
6. The parka's inside pocket.
7. Where the letter lives after ch 9 (the drafter chooses; ch 25 rereads it there).
8. The scaffold path at the House; what Marisol carries the coffee in (thermos or trays — both are Book One objects).
9. Saturday as the roster's off day, if said.
10. Aisha fetched her own boxes because Facilities' mailbox was full.
11. "Hartwell House" named on a 1.2 page.
12. Aisha's vehicle as "the truck" (F8 — the registry owes the row).
13. A seltzer as her drink, if used.
14. Any fourth board name in the epigraph.
15. If the Curb Market is used: that it runs in December (needs the author, F4).

## OPEN MARKERS ENCOUNTERED

- `book2/plots/b12-outline.md:248` — `[TK: letter text is S01-sensitive — author blesses wording]`. Not needed by ch 9 (the text stays off the page).
- `book2/plots/b12-outline.md:264` — `[CHECK mechanics at drafting time]` (F9, the portal QB) — not ch 9's.
- `book2/plots/romance-arc.md:98` — `[CHECK: is the standoff the private repair the ch 27 claim needs…]` — ch 26.
- `town-ashford.md:43–45` — `[CHECK: a real Ashford, Alabama exists…] [TK: author call.]`; :196–198 `[TK: the state…]`; :231–232 wards `[TK]`; :327–328 `[TK: state]`; :350–356 `[TK — author call, with sensitivity reader]` (Ray's family); :360–361 `[TK]` (toponyms).
- `book2/DECISIONS.md:82` — Dan's own drink `[TK]`; :98–100 — Verna's bourbon (ch 3) and the sub-couple's early introduction, both waiting on the author; :42–43 sub-couple names `[TK]`; :50–52 town-room moderator uncast; :63 title `[TK]`.
- New from this audit: Cordelia's era `[TK]` (F1); the Curb Market's winter status `[TK]` (F4); Aisha's vehicle (F8).

---

## FACT MANIFEST (anything not here is `[TK]` to the drafter)

**People**
- Dr. Aisha Cole, 41 — small, runner's frame, dark curls tied back on duty, brown eyes; loud by velocity not volume (SR-B2-16, `book2/DECISIONS.md:140–150`). Never-married; month-to-month in room nine since June. She never says "Dan"; her narration says "Merritt" (`ch03.md:348`, `ch07.md:26`, :306) and she says "Coach" aloud (`ch07.md:304`). "Dan Merritt" once in narration is new but consistent with his public name (`ch01.md:198` "Coach Merritt"). Silent board member since June (`ch01.md:179–182`).
- Coach Dan Merritt, 38 — six-three, an honest XXL, dark hair cut short, no gray; loud; the cap turned in his hands (SR-B2-15, :127–139). Off the page in ch 9. Never spend a line on his age (B2-D03.2).
- Verna Poteat — see item 4. Age off the page. Aloud: "Coach" / "that coach" / "Coach Merritt."
- Earlene Tatum — see item 5. Aloud: "Coach Merritt." One anchor, one flat line.
- Marisol Pruett and Cal Sutter — item 3. Full names once each. Wordless.
- Cordelia Hartwell — full name once, then "Cordelia" / "the letter." Dead; era undated (F1).
- Trey Gault — not in this chapter; "the boy" if the board says it (RECENT :33–39).
- Kat — by text only, if at all (`ch07.md:479–487`).
- Board names: Tim Brasher, Rhonda Sipes, Kendra Voyles (registry); one new real name allowed.
- Roberta, "out on the Millrow road" — the ch 8 caller (`ch08.md:144–152`); Aisha said her name on air (:216).
- Tick Moran (`ch08.md:29–39`), Rex Boyd (:130–132) — may be remembered from the porch; Boyd's line to Dan may not.
- No student on the page (STANDARDS 1).

**Places**
- The annex: one corridor at the cold end of campus; four rehab rooms (two tables, the whirlpool, the parallel bars, the cot with an army blanket); the records room; her office at the warm end, two rooms ahead of its radiator; the cold water fountain; the outside door at the cold end, two-stage bang (`ch05.md:42–52`; `ch07.md:93–96`, :239–257, :299, :419). Sits between the stadium's north side and Millrow's low end; leans against the Fieldhouse (`b12-outline.md:211–215`, :223–226). "The old WPA infirmary" (:211).
- The Fieldhouse — capital F (F14). Two cups came from it in ch 7 (:34).
- Millrow — climbs from Delmar's low end (two blocks off the square) to Hartwell House at the high end (`town-ashford.md:396–399`; `b12-outline.md:219–222`). "I'm not on Millrow, Coach." (`ch06.md:340`).
- Hartwell House — trust-owned; tarps and scaffold; crew of twelve through March; the east wall's dated glass under the scaffold (`manuscript/ch30.md:69–87`) — texture only, not for ch 9 to explain.
- The Magnolia Court — 1962 (doc furniture; no year on the page); neon, VACANCY; the office window at the end of the lot, the television on; room nine at the quiet end; the back room off the office (game days only) (`ch01.md:308–337`; `ch03.md:289–343`; `ch07.md:423–428`). Off past the square from Millrow (`manuscript/ch09.md:271–273`).
- The Checkerboard — on the square; down to one cook (`ch05.md:115–118`; `town-ashford.md:280`); the Liars' Table: Tick, Tunk Ferrell, Peanut Kyzer, Earlene Tatum, Sonny Dillard (`ch05.md:121–124`).
- The Doss County Curb Market — Saturday shed, WPA-built; December status unruled (F4).
- The county hospital — "twenty minutes up the highway," never a mileage (SR-B2-7; registry :21).
- Delmar's porch — Thursday's place; the rail, the smoker, the yard steps (`ch08.md:18–47`).

**Objects**
- Four cabinets; two walls of boxes; the film in brown sleeves; KNEES, 1994 (no arithmetic from it); her predecessors' handwriting "going back past ballpoint" (`ch07.md:249–254`).
- The memo under the stapler; its five sentences (:227–234, :292).
- The whiteboard in her office: DEC 19 circled twice in red, boxed at the top; the six-rung ladder, no dates, ever (`ch05.md:18–40`); the second card folded under the caster (registry :27) — cite only.
- PROTECTED, do not move, open, or pack: the diploma frames in their mailing box against the office baseboard (`ch05.md:48–50`; `ch07.md:339–340`; arc doc :29–30) — ch 29 unpacks; the far suitcase, latched since June, by the window (`ch01.md:318–319`, :355–356) — ch 25 packs. The near suitcase lives open on the rack (:316–317).
- The tablet (`ch07.md:59`, :293–296); the treatment log.
- The parka — item 1. Inside pocket new. Nobody knows whose it was.
- The wool coat on the closet rod, month-old woodsmoke (`ch07.md:477–478`; `ch01.md:349–353`).
- Verna's blanket, cedar, on the bed "where it lived now" (`ch07.md:475`; `ch01.md:332–340`).
- Her phone; the board read "like a river gauge" (`ch01.md:182`).
- Her plate on Delmar's rail: one rib, one bite (`ch08.md:351–353`). Not two plates (F2).
- Her truck (F8). The nine-minute pack, timed June and October (`ch01.md:320–322`; `ch07.md:278–279`).
- Coffee: only in Marisol's and Cal's hands, by day (B2-D03; brief). Aisha: nothing named, or a seltzer; at night beer, whiskey, or seltzer.
- The envelope, the key hook, the cavity, the towels, the boxes she fetched — new (see New Canon).
- Banned furniture: casserole, foil, tinfoil, pans, doilies (RECENT :40–44).

**Times**
- Saturday, week three, no game. No day-of-month, no "two weeks," no "next Saturday," no count to the nineteenth (A1). "The nineteenth" alone is allowed. "Two nights ago" for the porch is safe. Verna's pins are "tomorrow, after church."
- Thursday night was Coach's Table, live on WDSS 1340 (`ch08.md:18–21`).
- Friday: practice at five, film first; the check at 5:15 on the turf, printed (`ch07.md:308–317`, :415). It happened (F3).
- The playoff is on the nineteenth, a Saturday, at home, on campus (`ch08.md:24–25`, :62, :428; B2-D08.2). Trey plays only when she signs (`ch08.md:426–430`). The county wants "safe" (:24–25, :77–81).
- February eleventh is the boxing deadline, a Thursday (`ch07.md:255`, :356; B2-D08.2).
- The university closes two weeks over the holidays (`ch07.md:274`).
- The town's morning clock binds any 5–7 a.m. scene (`town-ashford.md:64–70`) — not expected here.
- December dusk is early; the House cameo is by day.

**Protected lines (verbatim, quotable in her memory)**
- The whole rail exchange, `ch08.md:301–349`, including his: "I did." / "Came with the job." / "So would I." / "It won't be the last." And hers: "Take it back. It doesn't fit you." / "You read that board like it's a chart. It isn't. It's the weather." / "He did not answer her."
- Her forty seconds on air, `ch08.md:216–235` ("I'm the hold… When it comes out of my mouth, it's medicine.").
- The three posts, `ch08.md:440–454`.
- Ch 7: "Who's doing the boxing?" / "I am." / "By yourself." / "By myself." (:380–386); "Let me ask around before you start carrying anything… Give me a few days" (:398–402); "Five fifteen tomorrow. It'll be printed." (:415); "in June nobody could tell her whose key they were handing her" (`ch05.md:46–47`).
- Verna's room-nine line, verbatim (`town-ashford.md:261–262`). First spend.
- Earlene's anchor gist (`b12-outline.md:464–466`), in her words, exactly once.
- BANKED, may NOT appear: the letter's severable line (`b12-outline.md:248`); the coat's severable line (:244); any paraphrase of the letter's contents.
- Spent or capped constructions (brief :209–217; RECENT): "never once" (cap blown), "somebody's ___" (spent ch 1), "one beat," "unhurried," "declined to," "and meant it," "which was its own," "the way X does Y," "neither of them stepped back" (spent twice), "six months," a second "since June" (prefer zero), "Somewhere" as an opener more than twice, the laugh scaffold.

**Rules in force**
- Stage 2, no new rung; the coat is rung-4 texture she does not know (`romance-arc.md:49`, :81; STYLE :218–228).
- Three romance beats, two kinds, first and last third; kinds 4, 8, 6, and 4-or-3 only (STYLE :269–292).
- One anchor; no swear; dialogue floor 15% unless the drafter argues under it.
- No students; the offstage-student mechanic (STANDARDS :21, :34–47).
- The vacate order is not public (brief :232; F7).
- The say-it test: the first paragraph says what today is and what is at stake (STYLE :396–428; TASTE entry 1).
- The letter's contents off the page; its effect on her said plainly (brief :237–239, :247–250).

---

**AUDIT VERDICT: CLEAR WITH ADDENDA** — the brief goes to the drafter with these nine lines added to it:

1. Strike "a hundred years dead" and "a hundred years" from the drafter's page instructions. Cordelia is dead and undated. The paper and the hand are old; no number, no year on the page. Cordelia's era is `[TK]` to the author. (F1)
2. Romance beat 1 is a line of his from the rail, or her own plate. Not "the two plates." (F2)
3. Friday's 5:15 check happened, off the page; one line may say so, with the porch unmentioned. Saturday is the roster's off day by default; say it once or not at all. No Saturday check on the page. (F3)
4. Scene 4's place is the annex door (or the Checkerboard counter). The Curb Market shed needs the author's word on winter hours. (F4)
5. Verna's towels are new canon; say the arrangement plainly once. Stage the handoff away from the records room. (F5, F7)
6. She drives up Millrow on purpose, by daylight, before the crew's dark; the House is not on her way home. (F6)
7. Her vehicle is "the truck." Say "Hartwell House" once. (F8, item 3)
8. The whiteboard holds two calendars; FEB 11 is on it only if ch 9 writes it there. (F10)
9. The calendar question (A1) goes to the author on the PR with option one as the strikeable default; the chapter carries no day-of-month either way.
