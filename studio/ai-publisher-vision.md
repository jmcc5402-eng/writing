# Vision: The Transparent AI-Driven Publisher

**Status:** working vision doc, drafted 2026-08-02 for conversations with
a small publisher exploring an AI-driven workforce. Prior-art research
(web, 2026-08-02) is folded in at §10. This describes a company that
does not exist yet; everything here is a design proposal, not a report.

**The one-line pitch:** a publishing house that runs book production the
way good software teams run software — agents do the volume, named
humans own the taste, every creative decision is logged in version
control, and the AI/human mix is printed where readers can see it.

**The prototype already exists.** This workspace — nine versioned
agents, a staged pipeline, canon docs, changelogs, variance decks,
thread ledgers — is the single-seat version of this company. The vision
below is mostly "that, times four seats, with a front door."

---

## 1. The thesis

Three claims, each load-bearing:

1. **Frontier models can draft genre fiction at competent-midlist
   level** when constrained by a strong bible, a voice spec, and
   adversarial editorial passes. They cannot yet *choose* what is worth
   writing, or feel when a scene is dead. That split — machines for
   throughput, humans for taste — is stable enough to build on.
2. **Cadence wins in genre publishing** (see
   `romance-market-study.md`: the difference between $100/month and a
   living is catalog size and release rhythm, not lightning). A
   one-book-per-month house competes on the one axis where AI is
   unambiguously superhuman.
3. **Transparency is a moat, not a confession.** The gray market hides
   its AI use and races to the bottom. A house that publishes its
   process — named human producers, logged checkpoints, a per-book
   provenance page — is betting that trust compounds. Nobody
   currently owns "honest AI publishing" as a brand. (Research below
   confirms the lane is genuinely empty.)

## 2. The org chart

Small on purpose. Headcount ~5–6 humans at a 12-book/year run rate.

| Role | Count | What they own |
|---|---|---|
| **Publisher / managing editor** | 1 | The list (what gets made), the brand, the transparency standard, final acceptance on every book |
| **Author-producers** | 3–4 | Each runs a writers' room of agents on 1–2 series; they are the named creative lead on their books — closer to showrunner than typist |
| **Ops / production** | 1 (can start as a hat) | The pipeline itself: agent roster versioning, CI gates, metadata, covers (commissioned), distribution, disclosure pages |
| Freelance | as needed | Cover art (human — it's outward-facing brand), final human proofread, sensitivity reads where warranted |

The author-producer is the keystone role. The job is: pick the hook,
lock the bible, brief the agents, read everything at the gates, make
the calls agents escalate, and put their name on it. One producer, one
book per quarter, comfortably — four producers staggered = one book
per month at house level *without anyone rapid-releasing*.

What the job is **not**: prompt-typing all day. A producer whose
fingerprints aren't on the bible, the outline decisions, and the gate
reads is a rubber stamp, and rubber stamps break both the quality
model and the copyright model (§7).

## 3. The production line, as an SDLC

Each series is a repo. Each book is a milestone. Each chapter is a
branch. The mapping is almost embarrassingly direct:

| Software | Publishing equivalent | Who does it |
|---|---|---|
| Market/user research | Category research, comp analysis, trend scan | Agents; human reads the brief |
| Product spec | Premise + hook + positioning ("why this book") | **Human decides**, agents generate candidates |
| Architecture / design doc | Story bible + series canon + voice spec | Agents draft; **human locks every structural decision** |
| Tickets / sprint plan | Chapter-by-chapter outline with scene goals | Agents (plot-architect); **human approves before drafting** |
| Feature branch + implementation | Chapter draft on a branch | Agents (drafting-assistant + persona) |
| CI: lint, typecheck, tests | Automated editorial gates: canon check, thread ledger check, voice/style check, banned-moves check, super-concept tests | Agents, deterministic and blocking |
| Code review | Developmental notes, reader-panel sim, red-team read | Agents review; findings attached to the PR |
| **PR merge** | **Chapter accepted into manuscript** | **Human producer merges — always** |
| Release candidate | Full-manuscript revision passes (structure → line → continuity, in that order) | Agents run; human triages findings |
| Staging sign-off | **Producer's full read** + publisher's acceptance read | **Humans, non-delegable** |
| Deploy | Format, metadata, disclosure page, publish | Ops + agents |
| Telemetry | Read-through rates, reviews, returns, KU page-read curves | Agents digest; feeds the next book's brief |
| Post-mortem | Book retro → agent changelog entries, backlog items | Producer + ops |

Three SDLC disciplines carry over with real force:

- **CI gates are cheap, run constantly, and block merges.** Continuity
  against canon, thread plants/payoffs (`OWED:` markers), voice-spec
  compliance, banned-move lists, per-book super-concept tests — all of
  this is mechanical enough for agents to enforce at near-CI
  reliability. No human should ever spend attention on what a gate can
  catch.
- **The PR is the unit of human attention.** A producer doesn't read
  raw model output; they read a chapter *plus* its attached reviews:
  what the dev-editor flagged, what continuity cleared, what the
  reader-panel stumbled on, and the diff against the outline promise.
  Reviewing a reviewed thing is 10x faster than reviewing a raw thing
  — that's the entire throughput trick.
- **Everything is versioned, so provenance is free.** The git history
  *is* the audit trail of who (and what) did what. The transparency
  page per book is generated from it, not written after the fact.

## 4. The bottlenecks — where human input is non-negotiable

Ranked by how expensive it is when a human *isn't* there. These are the
checkpoints; everything between them can be agents.

1. **Concept selection ("greenlight").** Models generate infinite
   plausible premises and are mediocre at ranking them. Which hook is
   worth six books is a taste-plus-market call, and it's the single
   highest-leverage decision in the company. Human, always, full stop.
2. **Bible lock.** Every structural decision locked here saves ten
   downstream arguments. Agents propose; the producer decides names,
   rules, arcs, the ending. A bible the producer can't defend from
   memory is a bible they didn't really make.
3. **Outline approval.** Last cheap checkpoint. A weak chapter costs a
   redraft; a weak outline costs the book. Agents will produce
   *structurally valid* outlines that are nonetheless inert — the
   human's job is to find the two scenes with no reason to exist and
   the one turn that's too tidy.
4. **The load-bearing scenes.** Openings, midpoint reversals, the dark
   night, the climax, the last page. Models are weakest exactly where
   books are won: the moments that must land emotionally rather than
   competently. Producers should expect to hand-touch these — rewrite,
   not just approve. Budget it: ~10–15% of the wordcount gets human
   prose or heavy human line-work.
5. **Chapter merge.** Human merges every chapter PR. Fast when gates
   and reviews are attached (§3), but never skipped — this is where
   drift gets caught while it's one chapter wide instead of ten.
6. **The acceptance read.** Producer reads the whole book like a
   reader, in as few sittings as possible — this is the only vantage
   from which "the middle sags" is visible; no gate sees the whole
   whale. Then the publisher reads it cold. Two full human reads per
   book, minimum, non-delegable, forever.
7. **Everything outward-facing.** Cover, blurb, title, pricing, the
   disclosure page itself. Public surface = human sign-off.

Notice what's *not* on the list: research, first drafts, continuity,
copyediting mechanics, formatting, metadata, comp analysis, review
digestion. That's most of the hours in traditional publishing, and
it's the part agents do at scale.

## 5. "Will it sound like AI?" — an honest confidence assessment

Split the question, because the two halves have different answers.

**Line level — high confidence, with engineering.** The recognizable
"AI sheen" (over-balanced sentences, hedged emotion, tidy paragraph
rhythm, adjective triplets, bow-tied endings) is real but treatable:
voice specs built from human-written sample prose, banned-move lists,
anti-sheen rules in the drafting agents (this workspace already ships
one), variance cards so consecutive chapters don't share tics, and a
line pass whose explicit brief is "rough this up where it's too even."
Disclosed-AI prose that has been through that gauntlet plus human
touch on the load-bearing scenes will not be flagged by readers at any
useful rate. What "sounds like AI" to readers in 2026 is mostly
*unedited* AI.

**Structural level — the real risk, medium confidence.** The tell that
survives good line editing is sameness of shape: arcs that resolve on
schedule, conflict that de-escalates politely, everyone learning their
lesson. Mitigations are process, not prompting: human-owned outlines
(bottleneck 3), a red-team pass explicitly hunting predictability, a
house rule that every book must do one thing the outline template
wouldn't predict — and the honest backstop that the producer's
acceptance read exists precisely to catch a book that is competent and
dead.

**What the evidence says (see §10 sources):** at excerpt length, the
question is already settled — a 2025/26 study found general readers
*preferred* AI prose imitating award-winning styles (experts didn't,
until models were fine-tuned on an author's corpus, which flipped even
the experts). At novel length there is no clean pass yet: the
consistent finding is that AI-heavy books can capture sales rank but
show weaker retention and re-read rates, and reader communities now
actively pattern-match for AI tells. Which localizes the problem
exactly where this design puts the humans: whole-book coherence,
earned emotion, and series loyalty — the acceptance read and the
load-bearing scenes.

**Calibrated claim:** for genre fiction with strong conventions
(romance, mystery, thriller, middle-grade adventure), this pipeline
can reliably produce books indistinguishable from a competent
midlist human author. It cannot reliably produce a *distinctive* voice
without a human deliberately building and enforcing one — which is
exactly why the voice spec is a producer-owned artifact. Aim the
company at genres where the promise kept matters more than the
sentence signature. Don't pitch it as a literary house.

## 6. Can agents do final review? — Yes for gates, no for acceptance

Where agent review is *already* as good as or better than human:

- Continuity and canon compliance (names, dates, geography, rules)
- Outline-vs-draft conformance ("did the chapter keep its promise")
- Thread accounting (plants, payoffs, orphaned setups)
- Style-spec and banned-move enforcement
- Copyediting mechanics
- Coverage-style critique: a red-team agent reliably *finds* real
  weaknesses when told to attack

Where agent review cannot be the last word:

- **Boredom.** Agents evaluate text against criteria; they do not get
  bored the way a tired human at 11pm gets bored. "Technically fine,
  emotionally inert" is the exact failure mode agent review misses.
- **Freshness.** An agent can't tell you the trope execution reads as
  last year's — its sense of "current" is its training data.
- **Correlated blind spots.** Drafting agents and reviewing agents
  share a model family's biases. Same-model review is the author
  reviewing their own PR: genuinely useful, structurally insufficient.
  Cross-model review panels reduce this but don't eliminate it.
- **Accountability.** A book carries a named human. "The agents
  approved it" is not a sentence the publisher ever gets to say — to
  a reader, a retailer, or a court.

**Design rule:** agents *gate* (blocking, mechanical, exhaustive) and
*advise* (critique attached to every PR); humans *accept* (merge,
acceptance read, greenlight). Agent review compresses human review; it
never replaces the two full human reads. Confidence in that division:
high — it's the same division software settled on with CI + human code
review, for the same reasons.

## 7. Transparency and the legal spine

Transparency here isn't just ethics branding — it's structurally
necessary, for two reasons the research (§10) makes concrete.

**Copyright requires demonstrated human authorship — and the position
is thinner than comfortable.** Under the US Copyright Office's Part 2
report (Jan 2025, still governing), purely AI-generated text is not
copyrightable and prompts alone — however detailed — do not confer
authorship. In a mixed work, only the human contributions are
protected: human-written passages, substantial human revision, and the
selection/arrangement of AI material (a thin, compilation-style
claim). Stated plainly for any pitch: an AI-drafted, human-revised
novel has *partial, untested* copyright protection, and a pirate who
strips and republishes the raw AI prose sits in a genuine gray zone.
Mitigations: heavier human line-work raises the protected share
(bottleneck 4 is a legal asset, not just a quality one); series-brand
trademark; registration with full disclosure and the git-history
evidence trail — the producer edit logs are exactly the documentation
the Office looks for. The SDLC isn't just efficient; it's the
evidence. The Office itself is institutionally unstable (the Register's
firing/reinstatement litigation ran into mid-2026), so build to
survive the *strict* reading. [CHECK: counsel review before launch; a
registration test case on book one, fully documented, is the fastest
de-risking move available.]

**Retail disclosure already applies — and it's Amazon-internal.** KDP
has required declaring AI-generated content since Sept 2023; under its
taxonomy (AI-generated vs. AI-assisted, where even heavily-edited AI
text counts as "generated"), this house's books are squarely
**AI-generated and must be declared on every title**. That declaration
is internal to Amazon and not shown to shoppers — so the public
provenance page is voluntary and on top, which is the point. Amazon
accepts disclosed AI-generated fiction; the friction is the *wide*
stack: Kobo prohibits content "generated primarily by automated tools
that lacks genuine human effort" and is building AI detection,
Draft2Digital draws a similar line, and IngramSpark (print/bookstore
reach) is tightening [CHECK: Ingram's current policy, secondhand only].
A curated human-supervised list arguably passes these tests, but
that's their call: **plan Amazon-first economics; treat wide as upside
contingent on direct policy conversations with Kobo and Ingram before
launch.** Track the per-book AI/human mix from the repo as it happens,
never reconstructed later, and exceed platform minimums everywhere so
policy changes never threaten the catalog.

The public artifact: a **provenance page** in every book and on the
site — named producer; what agents did (research, drafting, editorial
gates); what humans did (concept, bible, outline, N scenes, all
merges, acceptance reads); counts generated from the repo. One format,
every book, no exceptions, including the flattering-to-AI cases. The
brand is the honesty, not the ratio.

## 8. Capacity math for one-book-per-month

Per book (70–80k words, genre fiction), steady state per producer:

| Phase | Calendar | Producer hours (est.) |
|---|---|---|
| Concept + greenlight | 1 wk (overlapped) | 4–6 |
| Bible + outline, locked | 2 wks | 15–20 |
| Drafting: ~25 chapter PRs | 4–5 wks | 20–30 (merges + escalations) |
| Load-bearing scene work | (within drafting) | 15–25 |
| Revision passes + triage | 2 wks | 10–15 |
| Acceptance read + fixes | 1 wk | 10–12 |
| **Total** | **~10–11 wks** | **~75–110 hrs/book** |

That's a book per producer per quarter at professional intensity —
part-time hours, importantly, which is what makes the role staffable.
Four producers staggered = 13–16 books/year at house level; the
publisher's acceptance read (~8 hrs/book) is the last serial
constraint and caps out well above one/month. Model/compute cost per
book at current frontier pricing is small against even freelance-lean
production budgets [TK: real number after a pilot book — instrument
the pipeline from day one].

**The honest schedule risk** isn't agent throughput; it's producer
attention collisions (two books hitting acceptance the same week) and
the temptation to skip gate reads when the calendar squeezes. The
publisher's job is to defend the checkpoints from the cadence.

## 9. What it takes to build

1. **Pilot book, this workspace, ~one quarter.** Run one genre novel
   through the full pipeline with one producer. Instrument everything:
   hours at each checkpoint, gate catch-rates, model spend, how much
   human prose the load-bearing scenes actually needed. The pilot's
   provenance page is the company's founding document.
2. **Harden the room into a platform.** The agent roster, versioning,
   variance decks, and pipeline gates already exist here; they need
   multi-seat packaging (the plugin work already parked in
   `studio/plugin/` is the seed), plus PR templating that attaches
   agent reviews automatically.
3. **Hire producers for taste, not tech.** The interview is: here's a
   bible, here are three agent-drafted chapters with reviews attached
   — mark them up and defend your merges. Editors and showrunner-brained
   writers, not prompt engineers.
4. **Legal foundation before book one ships.** Copyright counsel on
   the registration strategy; disclosure language per platform;
   producer contracts that make the named-human model real (credit,
   royalty participation, and actual authority to kill a book).
5. **Pick the launch genre by the romance-study logic:** proven,
   KU-native, convention-forward, cadence-rewarding. The market study
   in this directory is the template for that decision.
6. **Decide the brand posture early:** the provenance page format, the
   house name, whether producers publish under their names or house
   pen names — locked before book one, because retrofitting
   transparency reads as damage control.

## 10. Prior art — does this exist? (researched 2026-08-02)

**Short answer: no. The transparent, curated, human-in-the-loop
version does not exist yet.** Every current player is one of three
things this company deliberately isn't:

- **Spines** (~$22.5M raised) — an *author-pays* AI services platform
  ($1,200–5,000 per author) that announced 8,000 books for 2025 and
  drew industry-wide condemnation. The backlash triggers were
  volume-as-mission and charging authors — a curated 12-book/year
  list where the publisher bears cost is positioned against both.
  Still operating (voice-clone audiobooks, translation); whether it
  hit its volume target is unverified.
- **Inkitt / Galatea** ($117M+ raised) — the closest proof the
  *economics* work: AI-assisted editing, A/B-tested plot rewrites,
  AI-ghostwritten sequels in romance/romantasy, claims of a new $1M
  ebook every four weeks (Bloomberg, May 2025). But it is the
  anti-transparent version — readers generally aren't told what's
  AI-written. It validates demand while leaving the trust position
  wide open.
- **The KDP/KU gray market** — anonymous AI floods that Amazon has
  been fighting since 2023; a 2026 working paper suggests AI-heavy
  books now hold a large share of top-sales slots in exposed genres
  [CHECK: paper unverified, read before citing].

Nobody credible is doing SDLC-style, version-controlled, review-gated
multi-agent book production with named humans at checkpoints — the
closest real-world analog the research found is, literally, the
workflow in this repo. The pipeline design is itself differentiating
IP, and (per §7) its audit trail doubles as the copyright evidence.

**Why the white space exists — the uncomfortable version:** everyone
monetizing AI books today profits from *hiding* the AI (KU farms,
Galatea) or from selling services to authors (Spines); transparency
breaks both models. And disclosure currently carries a real tax:
studies find disclosed AI authorship erodes perceived trust — though
the penalty *shrinks when human effort is visible*, which is this
company's entire design thesis. There is no verified case yet of a
publicly-disclosed, mostly-AI genre novel selling well on its own
transparency. That absence is the opportunity and the warning in one
fact.

**Climate to plan around:** the Authors Guild's "Human Authored"
certification (5,000+ titles by early 2026) institutionalizes the
counter-label this house will be defined against. SFWA made any LLM
drafting or rewriting a Nebula disqualifier, so award ecosystems are
closed — price that in and market direct-to-reader. The cautionary
case is *Shy Girl* (Hachette, 2026): a novel pulled after AI-pattern
accusations — the scandal was **concealment**, not use, which is the
strongest single argument for transparency-by-design. The lone
positive precedent (Rie Kudan's Akutagawa win with ~5% disclosed
ChatGPT text) is thin and not a comp for "mostly AI-written."

**Top risks, ranked (from the due-diligence pass):**

1. Copyright thinness — catalog asset value rests on documented human
   contribution and an untested compilation claim (§7).
2. Distribution ceiling — Amazon-with-disclosure works; Kobo/D2D/
   Ingram may refuse, locking in Amazon dependence.
3. The disclosure tax with no proven counter-case — year one is a bet
   that quality plus honesty beats the penalty before capital runs out.
4. Institutional hostility — no awards, an organized counter-label, a
   trade press primed for pile-ons.
5. Novel-length quality — evidence supports excerpt parity, not
   90k-word parity; a mid book three converts every reviewer into
   "I told you so."
6. Information sludge — this niche's public "data" is substantially
   AI-generated SEO content, including at least one likely-fabricated
   success story; every pitch-deck stat needs a primary source.

**Fastest de-risking moves:** (a) direct policy conversations with
Kobo and Ingram before launch; (b) a fully-documented copyright
registration test case on book one; (c) commission one methodologically
sound reader study on disclosed-AI genre fiction — none exists, so the
study itself becomes citable, ownable marketing.

## 11. Open questions

- [TK: does the publisher partner want this built inside their house,
  or as a joint venture with its own imprint?]
- [TK: launch genre — the romance study argues for a KU-native genre
  lane, but the partner's existing list may pull elsewhere]
- [TK: producer compensation model — per-book fee, royalty share, or
  salary; this decides who takes the role seriously]
- [TK: cross-model review policy — how much genuine model diversity
  the editorial panel needs before correlated-blind-spot risk is
  acceptable]
- [TK: kill criteria — what failing numbers or failed reads cancel a
  book mid-pipeline; a cadence house without kill criteria becomes a
  content mill in about six months]
