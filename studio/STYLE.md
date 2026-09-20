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
- Em dashes unspaced — like this. *(Campus override, ratified by
  use: narration dashes SPACED; the book's register wins per the
  override rule above.)*
- **Dialogue interruptions cut with an UNSPACED em dash** before
  the closing quote (`she—"`) — ruled 2026-08-28 (D15.3);
  precedent conformed.
- Scene breaks are a centered `***` on its own line.
- Numbers under one hundred spelled out in narration; numerals in dialogue only
  where a character would say them that way.

## After a jump, the date is said plain (author, 2026-09-13)

"The date of the last whole scene is confusing. Is this the day
after New Year's Eve? It just says Friday, but I can't remember
which day that is." When a section opens on a different day from
the one before it, its establishing line says the date in words a
listener keeps: "the first of January, the night after," not the
weekday alone. A weekday is a fact only the calendar knows.

## The epigraph is the non-football reader's door (author, 2026-09-14)

Where a book opens its chapters on a community board post, the post
is for the reader who does not care about the sport: a parent's-eye
picture of the town or college life that week — the drive, the dorm,
the diner, the cold, the laundry, the grandmother's parking question.
Light; a smile in it. It may rhyme with the chapter's mood. It never
carries a plot beat, a count, a rule, or a named plot object; those
belong on the page. (1.2 ch 19, #164: "I want them to be much
lighter… a mom who doesn't care about sports but has a kid coming
home for the holiday break can feel some connection.")

## It's just a romance novel — say it plain (author law, 2026-09-13)

The author, on 1.2 ch 18 (#161): "This chapter has a lot of paras
that almost read like a weird poem. It's like the writer is just
trying to tie in too many things." · "It's like the writer is trying
too hard to make this into some glorious mystery to unravel. It's
just a romance novel. It doesn't need to have all of these weird
connected things — a paper in a file in a room, it just doesn't make
sense." · "The writer is just being too implicit. If they're joking,
make it more funny or have more reactions." · "We need to explain why
they're not together more." Four laws:

(a) **Sentences end.** A narration sentence is ordinarily under
thirty words. A sentence with more than three "and"s, or a paragraph
made of one or two such sentences, is a finding; semantic line
breaks are not hinges for chaining clauses. The chapter lint counts
both. (b) **A plot object weighs what the plot has made it weigh.**
A letter, a page, a drawer, a file carries the meaning the book has
already given it, said once in plain words ("eleven parents wrote
the athletic director; it goes in his file"), and is never carried
scene to scene as a mystery. What the reader does not yet know to
fear, the POV lead does not brood on. (c) **A joke is understood.**
Banter between minor characters carries its meaning on the page — a
plain line, a reaction, a laugh — so a stranger can say what they
are joking about. Implicit is not funny. (d) **Apart has a reason.**
When the leads could be together and are not, the page says why,
in one sentence, before the reader asks.

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

## Closeness: reaction density, not depth (author law, 2026-08-23)

> "Do we need more internal talk for the reader to get close to
> them? I don't think it needs to be ten layers deep because these
> are pretty light reading novels, but I also want to create a
> connection."

Diagnosed on campus ch 1–20, which measured ~1.3 tagged interior
moments per thousand words with three chapters at zero: the
interiority was excellent but **intermittent** — one aria per
chapter at the emotional peak, and the reader riding outside the
character the rest of the time. Root cause was systemic, not
authorial: every standing rule in the studio (hands-and-objects
register, show-don't-tell, the dialogue floor, the fun directive)
pushes emotion OUTWARD, and no brief had ever asked a drafter to
go inward.

The law, for every book here:

1. **Frequency beats depth.** Connection in commercial fiction is
   built by a running layer of the POV character's judgment — not
   psychology, not backstory. More often and shallower is the
   target; literary interiority is the wrong instrument.
2. **A reaction beat per SCENE, not per chapter.** One or two
   sentences where the POV character judges what just happened, in
   voice. Roughly forty words a scene.
3. **One private admission per chapter** — something the character
   would never say aloud, admitted to herself. The highest
   bonding-per-word device in the form.
4. **Reticent characters get motive clauses.** A closed lead who
   only acts reads as opaque, not deep. One clause of *why* per
   scene converts silence into interiority. (Campus model, ch 20:
   "which he would not have told anybody about.")
5. **The wound stays rationed — and every lead gets one.** One
   full excavation per lead per book, placed where the cost is
   real. A book that excavates only one of its two leads produces
   readers who admire one and bond to the other; in romance the
   heroine is the reader's proxy and may not be the one skipped.
6. **What this is NOT:** backstory blocks, rumination paragraphs,
   flashbacks. They break the pace these books run on. Reactions
   and admissions only, in the character's own voice.

**The curve rises.** Interiority should tighten as the book goes
on, so implementing this mid-book is legitimate design rather than
a policy seam. And because reaction beats touch no canon, no state
chain, and no fair-play row, **this rule never backpropagates** —
a book already drafted may take it going forward, and any front-
half top-up belongs to the final polish pass, judged on a
full-book read.

Measured by the CLOSENESS meter (campus METERS.md), added by
author waiver — see `studio/DRAFTING-PROTOCOL.md`, instrument
governance.

## The closeness ladder — proximity beats (author law, 2026-09-03)

> "By touch, I mean almost any close or almost-close contact: she
> walks past him and he smells her hair; he hands her a jacket and
> she sees how strong his shoulders are; they're sitting at a table
> arguing and they're so close that they can feel the attention. The
> goal is for the reader to understand that these people are getting
> closer and closer all the time, and eventually they'll be very
> close."

Diagnosed on campus 1.2 ch 5–8: the leads shared one scene in four
chapters and never spoke until a fold added the ch 8 rail exchange.
The romance was happening in two separate interiorities, and a
listener could not feel the two people approaching each other.

The law, for every romance here:

1. **One proximity beat per chapter in which both leads are on the
   page.** A proximity beat is the other person's nearness, in the
   POV character's SENSES — smell, heat, the air moved, a hand near a
   hand, the size of a shoulder as it reaches past — never a stated
   feeling and never a repeat of a beat already used. Each beat is
   NEW information about the other's body or presence.
2. **The rungs.** Beats are measured on one ladder:
   - 1 — sighted across a room; one physical fact noticed
   - 2 — same room, standing distance; the POV reads a face
   - 3 — passing close: smell, heat, the air moved
   - 4 — an object passed hand to hand, or put on the other's body;
     hands near, no skin
   - 5 — close enough to feel attention: across a table, a rail, a
     board, arguing; neither steps back
   - 6 — first incidental contact: skin, a second, unremarked
   - 7 — a deliberate touch that means it
   - 8 — the kiss, where the book's kiss chart puts it
3. **The high-water mark only rises.** A chapter may play a lower
   rung as texture, but every new high is exactly one rung up, at
   least one new high lands per quarter, and once a rung is reached
   the leads are never again written as strangers. The kiss chart
   sets each quarter's ceiling; the ladder climbs toward it, never
   past it.
4. **Two chapters with the leads apart may not run in a row.** A
   chapter without both leads on the page states in its brief why it
   earns the absence.
5. **The COUPLE LINE** carries this in every brief
   (`studio/DRAFTING-PROTOCOL.md`): whether the leads share a scene,
   speak, and which rung the proximity beat plays, in one sentence.
   The panel judges its presence the way it judges the anchor line.
6. **What this is NOT:** a heat slot. Rungs 1–5 are closed-door by
   nature; the heat map and the kiss chart govern 6–8. Nor is it the
   noticing beat — the noticing beat describes a body; the proximity
   beat measures a distance.

## Romance first — the rule (author law, 2026-09-04)

> "I think the writers don't understand fundamentally that this is a
> romance novel. They are writing great plots, but we have to
> remember that the reader here doesn't care about the plot, they
> care about the feeling of romance. The plot is a nice to have and
> I want it to be great, but every chapter has to have multiple
> romance aspects to it. They can be tiny, but they need to be. That
> should be a fundamental wall." And, the same day, on being shown
> the wall: "Rule not wall. It's like I have to work to convince the
> writers to include romance where it should be a core fundamental
> piece."

Not a gate the chapter is checked against afterward — the thing the
writer is told the job is before starting. The romance is the book;
the plot is what the two of them are doing while they fall. So the
rule lives at the front: in the drafter's persona
(`studio/agents/personas/drafter-campus.md`, the first thing every
campus brief hands the drafter), in the first line of every brief,
and only then in the count. The count exists so nobody has to argue
for the romance chapter by chapter; it is not where the rule lives.

**The floor.** Every chapter of a romance carries at least THREE
romance beats, of at least TWO different kinds, with at least one in
the first third of the chapter and one in the last third. A beat may
be one sentence. A chapter in which the leads are apart still owes
three; apartness is not an exemption, it is the harder case.

**The kinds** (a beat is one of these, in the POV character's
experience, on the page):
1. **Proximity** — the other's nearness in the POV's senses (the
   closeness ladder; this is the rung the chapter plays).
2. **Noticing** — one physical fact about the other, seen.
3. **Wanting** — the POV's want for the other, plain once or slant.
4. **The other in absence** — apart, the absent lead present in the
   POV's head as a person: a line remembered, an object that is
   them, a habit caught. Never as an obstacle only.
5. **Between them** — a line of dialogue between the leads, or an
   object passed hand to hand.
6. **The town ships them** — the chorus notices the pair: a look, a
   line, a post, within the realism rulebook.
7. **The want against its wall** — jealousy, a rival's flicker, the
   forbidden rule felt in the body; the want pressing on what
   forbids it.
8. **The private admission** — the thing about the other the POV
   would never say aloud (Closeness, rule 3).
9. **The body answering** — the POV's OWN body reacting before the
   POV has decided anything: heat, pulse, breath, a hand that stops,
   the cost of holding still. Not the other person described; the
   *viewer* reported. (Added 2026-09-15 — see "The viewer has a body"
   below.)

### The viewer has a body (the density survey, 2026-09-14)

Two instruments, run blind to each other, measured the same
deficiency and returned the same three lines. Across Book 1.1 and
Book 1.2 — **131,000 words — the POV character's own body reports
back three times**: 1.1 ch 5 (*"Heat arrived at the back of her neck
and stayed, on no schedule she had approved"*), 1.1 ch 13 (*"her
pulse loud in her ears"*), 1.2 ch 17 (*"felt her pulse where her
hand was going to go"*).

Everything else describes the *other* person as capability — Cal's
forearms, Dan's shoulders. Standard 25 is satisfied and the books
are still not hot, because:

> **The reader does not get warm from looking at a man. She gets warm
> from being in a body that is looking at a man and having trouble.**
> Both books show the view and almost never the viewer. That is the
> whole gap between "romance-forward" and "hot," and it costs nothing
> structural to close.

**The rule.** Kind 9 counts toward the floor like any other kind, and
**every chapter in which the leads share the page owes at least one.**
A beat is one sentence. It is the cheapest heat in the book and it
never touches standard 9 — the body answers long before any garment
does.

**The failure mode to watch: the mind filing the body.** This house
has a reflex of answering every involuntary beat with a competent
one — *"elected to blame the smoke," "declined to itemize," "declined
to examine."* Individually charming; fifty times it is a thermostat,
and it is why the wanting in these books reads as *admired* rather
than *felt*. One filing per chapter, maximum. Sometimes the body just
wins.

### The touch has a body (author, #177, 2026-09-20)

Kind 9 is the body answering before she decides. This is the body
answering TO THE TOUCH, and it is a different beat: the author read a
hand beat with nine sentences of approach and the whole choreography
of two hands, and asked for "the sheer physical reaction that happens
when two people in love touch — she felt electricity flow through her
body." The romance craft word is the *visceral response*.

**The rule.** Every touch between the leads gets at least one plain
sentence of the POV lead's physical reaction — where it lands in the
body (the stomach, the chest, the back of the neck, the breath), what
it does — and the sentence is a body, not a thought about a body.
"She noticed she wanted to" is a filing; "her stomach dropped like the
truck had" is a body. The panel counts a touch with no body as a
finding (the TOUCH test).

**The touch is a scene, not a sentence (author, 2026-09-20, rereading
ch 21).** At a key proximity moment — the leads pressed together, a
witness in the room — one sentence of body is a finding: "we just
have one line that her arm goes warm." The body runs across the
beats (the arm, the heart and where she feels it, the breath, the
hands held still, the face inside the hood), and the POV lead says
the confusion plain to herself: wanting him, with the wrong person a
foot away and able to read it. Love mixed with awkwardness is the
moment; the awkwardness is on the page, not around it. The panel
counts the body sentences at the chapter's highest touch (three or
fewer is a finding); `chapter-lint.sh` TOUCH SPAN counts them too.

### Nobody says where a thing was said (author, #177, 2026-09-20)

Banned: a character remarking on WHERE a thing was said, or that it
has now been said — "I wanted to say it in this truck," "it's been
said where you were," "I said so in this room," "before anything else
happens in this room." The house had nine of these on accepted pages
before the author named it. Say the thing. Never annotate the saying.

### The awkward beat (instrumenting taste 16, 2026-09-15)

Taste entry 16 has said it since the beginning — *"This type of
conversation should be a little bit awkward"* — and the survey found
it had never been instrumented: the awkward beat is present in 1.1
ch 23, 1.2 ch 17 and 1.2 ch 18, and **absent from every pre-kiss
chapter in both books.** Before the kiss, all four leads are only
ever competent.

**The rule.** Every book plants **at least two awkward beats before
its first kiss** — two serious adults being briefly fourteen: a look
held past the line and caught, a sentence that comes out wrong, a
laugh at nothing, a hand that arrives somewhere it did not plan to.
Competence is these leads' charm; the crack in it is the romance.
The survey's verdict: *the largest untapped source of clothes-on
charge in the series, and every gram of it is free.*

### Objects: a gift discharges, a debt accrues

The series' best heat engine is an object. Book 1.1's wrench is a
**debt** — he has it, he owes it back, and it accrues charge for
fifteen chapters until the return IS the kiss scene. Book 1.2's
parka is a **gift**, and a gift discharges on delivery, which is
exactly why the coat stops raising temperature after ch 10.

**The rule for every book from 1.3 on:** the book's central object is
a **debt**, planted by ch 3, held by the wrong person, and not
discharged until the ladder's top rung. Gifts are welcome as
texture. They are never the engine.

*(1.2 already has an unclaimed debt on the page: the facemask bolts
in her coat pocket, ch 3, never returned, never mentioned again.)*

### The ending register belongs to the couple

A binge reader decides whether to start the next chapter in the last
six lines. Measured across the first twelve chapters of each book:
**1.1 ends eight of twelve on feeling; 1.2 ends four of twelve on the
couple** — the rest on a latched suitcase, a kickoff time, a
whiteboard, a game date. *"1.1 sends her on; 1.2 hands her a
football."*

**The rule.** Across any run of four chapters, **at least half end on
the couple** — the feeling, the other in absence, or an object that
is them. The plot object may have the last word in a chapter; it may
not have it in three of four. **This is usually a reordering, not a
new line:** the material is already in the penultimate paragraph.

**One shape this rule must not produce:** the chapter-ending want
paragraph (*"She wanted him."*). Book 1.2 has three, and the retail
instrument named it *"the single most obvious retrofit shape in this
genre — it is where the fix goes because it is the easiest place to
put it, and that is exactly why we spot it."* End on the couple by
ending on a **thing**, not on a verdict.

**And escalate the kind, never restate the verb.** 1.2 names the same
want five times in twelve chapters ("she wanted him" / "he wanted
her" / "I want Dan"). Volume rose; kind never changed, and a reader
feels that as a stall. 1.1 escalates the *object* instead — the
wrench, the place card, the thermos lid, the zinnias watered, the
twine in his back pocket, her pen, a new pane of glass in her
handwriting's place. Each a different kind of possession. **That is
escalation. Restating the verb is not.**

**The reframe that comes with it.** The first line of every chapter
brief is THE ROMANCE MOVE: one sentence saying what this chapter
does to the feeling between the leads — closer, farther, or a new
thing known. The plot's argument comes second. A drafter who cannot
say the romance move has not been briefed.

**The build check (author, 2026-09-05).** The floor is per chapter;
the romance also has to add up across the book, and the floor
cannot see that. Ch 8 of 1.2 passed the count with thirteen beats
and the author still asked, "Have we earned the right for Dan to
think that he wants her? It almost seems to come out of nowhere."
So: the book's romance arc doc (PIPELINE §3b) stages the romance —
hidden, admitted inside, shown between them, seen, public — and the
inside may run ahead of the outside by at most one stage. A want is
not named until the reader has watched the two of them enjoy each
other twice on the page. A kiss waits for help accepted. A public
claim waits for a private repair. The reader must be able to point
to the scene where the next step started.

**Woven, not counted (author, 2026-09-06).** Ch 9 of 1.2 passed the
floor — six beats, four kinds, both edge thirds — and the author
returned it: *"She doesn't think about Dan the entire chapter and
then just says to herself that she wants him. Too abrupt. This book
seems to have none of the romance vibe of book one. There's nothing
woven in to the various scenes."* The floor counts thirds; the
reader feels scenes. So the rule is per SCENE, not per third: the
other lead is present in every scene of the chapter — in the POV's
head or senses, as a person, warm, physical, and said plainly — and
a want named at the end is the sum of what every scene before it
carried. An apart chapter is the hard case and gets no exemption:
the coat he was cut for, the line of his she kept, the place she
looks for him and he is not, the couple she watches and measures
against a rail. A chapter whose beats sit at the two ends with a
cold middle fails, whatever the count says.

**How it is counted.** The brief plans the beats as a numbered list
with kinds. The drafter delivers them and reports each with its line
number. The romance-reader-panel finds them independently, counts,
names the kinds, and checks the spread; its count is the one that
stands. Fewer than three, fewer than two kinds, or a first or last
third with none: the chapter goes back to the drafter with the
persona re-read, before staging. The orchestrator may not waive it;
only the author may, by a WAIVED line on the chapter's PR.

**Instrument governance.** Added on the author's word; the
one-in-one-out rule is honored by folding the COUPLE LINE into this
rule (kind 1 is the ladder beat; the couple line becomes part of the
ROMANCE BEATS list rather than a separate line).

## Names are relationships (author, 2026-09-07 — "a light idea")

> "I like your idea how only the man calls her Mac. I think having
> different people call different characters by unique names is
> kind of a good signature. We could have across many books. Sort
> of like how Aisha should always call a quarterback by his name,
> but other people can call him by number seven or the boy."

Who calls a character what is a relationship the reader can hear.
So every major character carries a **name map** in the book's
characters doc: the name each other character uses for them, and
the one name that belongs to one person only (the doctor says
"Trey" while the town says "7"; only Ty says "Mack"; Verna's "my
winter doctor"). The naming rule that is a full list (below) is
the enforcement; this is the design. A name that only one person
uses is a spend: it goes in the registry the first time it is
said, and it is never handed to a second speaker by accident.

## Rules are full lists; rations are per book (author, 2026-09-03)

Two lessons from the same listen, generalized:

- **A name rule names every speaker class**, including the ones
  nobody expected to speak. The campus quarterback rule listed
  parents, doctor, rail, board, and one old man; the athletic
  director was on no list and his email had to be ruled at the gate.
  From here a naming rule is written as narration + every speaker
  class + a default for everyone else, and the chapter lint reports
  every use with its speaker.
- **A phrase the author names is once per BOOK, not once per
  chapter**, and the book's ledger records which chapter spent it.
  Where the phrase already sits in accepted pages, the earliest
  accepted use is the spend and the rest are polish-pass debt, logged
  at the fold, never silently rewritten.
- **The modernity register is a grep, not a taste.** Each book keeps
  a furniture blacklist in the chapter lint (campus 1.2: casserole,
  foil, pans, "them oxygen chambers" register, grandma-at-the-elbow);
  a hit is a finding before any panel reads.

## The bookkeeper's register (D16.1, 2026-08-28)

Marisol prices things. Costs said in her voice as COUNTING —
"I counted it too," sums that balance and are hated for
balancing — are her licensed professional register, not a
scrub violation. The line she and the book may not cross is the
container: feelings filed, foldered, drawered, or kept in
ledgers-as-hearts stay banned in every POV. Cal's ledger tic
stays Cal's, capped at two per chapter, never the final ten
lines.

## The explicitness dial — varnish and the on-the-nose ration
## (author law, 2026-08-30; amended 2026-08-31 by author ruling)

> "It's almost like 'too witty', or too small-talkish."
> "Another way to say varnish I realized: 'too NOT on the
> nose.' We need a good mix of on-the-nose writing, which is
> more explicit — but if we use too much of it, it'll be
> boring. We have to be more on the nose sometimes."

ONE DIAL, TWO FAILURE ENDS. Every beat sits somewhere on the
explicitness dial:
- **Too on-the-nose** → boring; plainness creep (the anchor-line
  law already counts this direction: a chapter with three plain
  stakes lines is a miss the same as a chapter with zero).
- **Too oblique** → the reader can't decode the beat at all —
  and AUDIO is the reference reader for this end, because a
  listener cannot flip back. If a beat's decode depends on text
  sixty lines away, it fails the audio test.
Varnish (wit serving the writer) and obliqueness (subtlety
serving the writer) are the same sin at opposite ends: the line
serves its author, not its reader.

THE DECODE DUTY (the oblique end's ration): each chapter's
briefs name its LOAD-BEARING BEATS — the one or two things every
reader must hold leaving the chapter. Each load-bearing beat
owes ONE plain decode within a page: **the LAYERED RENDER —
image first, plain gloss second, consequence third** ("Twelve
names on that roll. Twelve kitchens attached to them, / twelve
tables' worth of mouths, / and the hours on that letter would
feed them all."). Say it slant, then say it straight once.
Texture beats stay slant — that is the mix. Modern mechanics the
whole audience may not carry (sock-puppet accounts, portal
windows, return-to-play categories) get their decode
chorus-voiced, in dialect, once ("some of these new users ain't
real users… they can sway a riled-up group with just a few
clicks").

THE SAY-IT TEST (author law, 2026-09-03 — "if you don't actually
tell the reader what the heck you're talking about, it's just
babble"):

> The orchestrator proposed the book's goal line as: "three
> weeks, one signature, twelve thousand people who wanted it
> Friday. What she wants, what he wants, what stands between."
> The author: "Notice how you don't actually say anything. It's
> just a bunch of phrases. Great for the visual concept, but if
> you don't tell the reader what you're talking about, it's
> babble. Your writing style is completely off the nose. It's
> what makes some chapters seem long and boring — too much
> flutter back and forth between people, and it's hard to tell
> what they're actually talking about, because we never state
> it."

The failure has a shape: a STACK OF NOUN PHRASES standing where a
SENTENCE should be. Fragments evoke; they do not inform. A reader
(and a listener, who cannot reread) needs, once per scene, one
complete sentence with a subject, a verb, and an object that a
stranger could repeat back: who wants what from whom, and what
happens if they don't get it.

The test, applied to any scene, brief, or proposal: **cover the
page and say out loud what the two people are arguing about.**
If the answer is a sentence, the scene has passed. If the answer
is "it's about the porch, and the date, and what she won't
lend," the scene has not said anything yet.

The goal line above, said: *Trey Gault will not play again until
Dr. Cole signs a form saying his brain has healed. The playoff
is in three weeks. The whole county wants the form signed by
then, and she will not sign it until it is true.* That is the
plot of the first half of Book 1.2 in three sentences, and by
chapter eight somebody on the page should say it.

Where the rule bites:
1. **Every scene states its argument once, in a sentence, before
   the subtext starts.** Subtext is what people do around a thing
   they have said; it is not a substitute for saying it.
2. **Briefs and staging orders write beats as sentences**, never
   as noun-phrase clusters. "The coat: XXL, A. COLE, a lost-order
   shrug" is a shopping list; a drafter cannot tell what happens.
   "He gives her his own coat and lies about where it came from,
   and she lets him" is a beat.
3. **The orchestrator's proposals to the author obey the same
   rule.** A recommendation the author cannot repeat back is not a
   recommendation.
4. The anchor-line law and the decode duty are this rule's
   special cases. This is the general one.
5. **The explicit opening (author, 2026-09-04).** *"I really liked
   how the very first paragraph was very explicit, that gets us off
   the hook and we can do a lot of implicit stuff later."* The
   chapter's first paragraph states plainly what today is and what
   is at stake in it (campus 1.2 ch 6: a committee names twelve
   teams; by noon the county has a season or nothing). That paragraph
   is the chapter's one mandatory on-the-nose beat; it buys the
   subtext that follows. Briefs carry it as THE OPENING, SAID.
   **Said, not recited (author, 2026-09-07):** campus 1.2 ch 10–12
   opened on the same calendar recital, one stake sentence in all
   three word for word. The opening begins on a thing, mid-motion;
   the day and the stake come inside it in fresh words; the opening
   check (`studio/tools/opening-check.py`) fails a repeat.
   **The establishing line (author, 2026-09-08):** and every scene
   break after the first owes the reader the room — where, when, what
   is in the POV's hand — inside its first three lines, in plain
   words ("a printed sheet of paper," "back in her office at the warm
   end of the annex"). Mid-motion is fine; unlocated is not.
   **AMENDED (author, 2026-09-09, #153: "The last section doesn't
   even say that Ayesha is there. It just starts with saying
   'she'"):** the establishing line also names WHO is in the room —
   the other lead by name before any pronoun for them.
   **The other lead has a face (author, 2026-09-09, #153: "it's a
   little too cold… It almost seems like she's a robot"; the same
   note on ch 13):** in the POV lead's scenes the other lead's FACE
   is on the page at every turn of the talk — eyes, a half smile, a
   look away and back. "She did not move" or "said nothing" with no
   face is a blank, and a blank reads as cold. Keep the lines; add
   the face.
   **No staccato endings (author, 2026-09-09, #153: "that last
   dialogue is way too robotic and confusing to read. It's too
   staccato. And it doesn't seem to do anything to help the romance
   or character arc"; the same note on ch 13):** a chapter's last
   exchange is full sentences, and it moves the romance or an arc.
   Two-word volleys close a scene in the middle of a chapter, never
   the chapter. `studio/tools/ending-check.py` warns.
   **Slow the good parts (author, 2026-09-10, #156 on 1.2 ch 16):**
   "The kiss is too fast. We could easily have a number of more
   sentences describing how they walk close to each other. They
   slowly looked at each other in the eye she moved his hand slowly
   to her face or vice versa and they kiss." And: "Much of this seems
   so terse." The semantic-line style pulls toward clipped, and
   clipped is wrong at the moments the reader bought the book for.
   Four rules. (a) THE SLOW BEAT — any touch or kiss gets its
   approach on the page: at least four sentences between the
   decision and the contact — the distance closed, the eyes held,
   the hand moving, the pause — before the touch itself; the panel
   counts them. (b) AWKWARD IS ALLOWED — "even though these are both
   very serious people… they feel a little bit like middle
   schoolers": when the leads are alone, the page shows it at least
   once — a look held too long, a line that comes out wrong, a laugh
   at nothing, a hand that does not know where to go. (c) THE ENDING
   THINKS — the POV lead's last scene carries interiority in plain
   sentences: what they think about the other lead, and the thing
   they are afraid of, said; a button is never a bare object — AND
   THEN COMES BACK: after the thinking, the last lines return to the
   other lead and the room, so the reader closes the chapter inside
   the romance and not inside the worry (author, #158 on 1.2 ch 17:
   "add a few more sentences at the very end so the reader is fully
   back in the romance rather than still thinking about some of the
   other stuff in her head"). (d) NO
   VOLLEYS BETWEEN THE LEADS — a run of three dialogue lines under
   four words each, anywhere in a scene the leads share, is a
   finding ("I heard them go by the window. They were talking." /
   "They were." — "either this dialogue is super deep and I don't
   understand it, or it's a little bit boring"); `ending-check.py`
   reports volley runs chapter-wide.

6. **A lead is named in the other lead's POV.** "The doctor" and
   "the coach" are the chorus's words and the POV lead's private
   register; the name still appears at least once in narration per
   chapter, before pronouns do the work, or a listener cannot tell
   which "she" is the woman he wants (ch 6, caught 2026-09-04).

THE VARNISH: dialogue or narration whose real purpose is to be
enjoyed rather than meant. The test, per exchange: WHAT DOES THE
SPEAKER WANT FROM THIS LINE? If the only honest answer is "to be
enjoyed by the reader," it's varnish. Three costs: voices flatten
(when everyone is equally clever, everyone is the author); stakes
evaporate (a character performing for the reader wants nothing
from the person across the table — "too small-talkish" is the
same failure at zero wit); trust erodes (a run of rewarded lines
is a tell, exactly like a run of composed chapter endings).

The audited diagnosis (notes/varnish-audit-2026-08-30.md, card
C3): this house's varnish concentrates in the REPLY POSITION in
chorus scenes — a second clever line capping a first that already
did the work. Crisis scenes and two-handers discipline
themselves; the wants are loud enough.

The law:

1. **When a line lands, the next speaker's job is to want, not
   to match it.** The first witty line in a beat belongs to the
   character; the second usually belongs to the writer. Cut
   yours. One epigram per beat.
2. **Rewarded lines are rationed and CAST-CONCENTRATED.** The
   chorus's licensed performers (per the book's roster) hold the
   wit; a witty line from a character with no performing bone is
   the author's hand. A flat line from a witty character is
   characterization.
3. **Performance can BE the want** — holding court, disarming a
   room, handing someone a way to stand back up. Wit at full
   load is the house voice and is protected; this law prosecutes
   decoration, not charm.
4. **Small talk earns its place only when its emptiness is
   dramatized** (the thing not being said must be on the page as
   weather).
5. **Gate hooks:** panels ask "who in this scene is performing
   for me instead of wanting something?"; line passes flag
   reply-position quips; drafting briefs carry rule 1 verbatim.
