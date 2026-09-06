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
