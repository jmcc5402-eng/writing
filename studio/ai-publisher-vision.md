# Vision: The Transparent AI-Driven Publisher

**Status:** working vision doc, drafted 2026-08-02 for conversations with
a small publisher exploring an AI-driven workforce. Prior-art research
is folded in at the end. This describes a company that does not exist
yet; everything here is a design proposal, not a report.

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

**Copyright requires demonstrated human authorship.** Under current US
Copyright Office guidance, purely AI-generated text is not
copyrightable; protection attaches to human creative contribution —
selection, arrangement, revision, and creative control that shapes the
output. A house whose humans genuinely drive concept, bible, outline,
load-bearing scenes, and every merge — *and can prove it from the git
history* — has a defensible copyright position and an audit trail most
publishers couldn't produce. The SDLC isn't just efficient; it's the
evidence. [CHECK: exact protectability boundaries are still being
litigated; counsel review needed before launch, and the registration
strategy (registering the human-authored expression and compilation)
needs a specialist.]

**Retail disclosure already applies.** Amazon KDP requires disclosing
AI-generated content at publication (its AI-generated vs. AI-assisted
distinction matters and should be tracked per-book from the repo, not
reconstructed later). The house standard should exceed platform
minimums everywhere, so policy changes never threaten the catalog.

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

[TK: research agent findings to be folded in — existing AI-first
publishers and their track records, KDP policy detail, copyright
position, reader-sentiment data, tooling landscape, and where the
white space actually is.]

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
