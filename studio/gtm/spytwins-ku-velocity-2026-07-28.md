# Spytwins — KU-Velocity Operating Playbook — 2026-07-28

_Prepared by gtm-strategist. The strategy decision is made and binding
(banner in `books/spytwins/roadmap/go-to-market.md`): Spytwins runs the
Emerson / *6th Grade Ninja* continuous-delivery path — AI-centric studio,
target one book per month, no launch until four books exist, Kindle
Unlimited, parent-facing channels. This document is the operating playbook
that makes that path work as well as it can work. Realism here serves
execution — true costs, true rates, true risks — not path re-selection._

_Variance card A1 (adversary-first, translated to business per the card
rules): every stage below is structured from its failure mode outward —
name what kills the stage, build the countermeasure in. The card shifted
emphasis only; no standard, remit rule, or output format was changed by
it. No banned moves are on file for this agent._

**Label key.** [VERIFIED] = sourced fact, source given, accessed
2026-07-28 unless noted. [ESTIMATE] = reasoning from verified facts,
shown. [AUTHOR DATA NEEDED] = only the author knows; asked in §7, never
assumed. Builds on the research stand of
`studio/gtm/gtm-overview-2026-07-28.md` (same-day sources carry over).

---

## 1. THE MODEL, OBSERVED

### What Emerson's machine verifiably looks like

- **Origin and scale.** *Diary of a 6th Grade Ninja* was Emerson's first
  self-published book, launched as a Kindle edition October 2012; the
  flagship series ran to 13 books; the catalog now spans multiple
  series — *Secret Agent 6th Grader* (4 books, 2013–14), *Recess
  Warriors* (2 books, 2017), *Kid Youtuber* (10 books, 2020–23) — plus
  a traditional deal (*The Super Life of Ben Braver*, Roaring Brook,
  2018) that came AFTER self-pub success: agent Dan Lazar at Writers
  House reached out to him off the self-published Ninja books.
  [VERIFIED — Goodreads editions/series pages; Book Series In Order;
  From the Mixed Up Files interview]
- **Cadence.** Observable from publication dates: at peak, roughly 4–6
  books per year across series (Kid Youtuber shipped 10 books in ~3
  years; Secret Agent 6th Grader shipped 4 in ~18 months alongside the
  Ninja series). [VERIFIED dates; cadence arithmetic is mine]
- **Pricing and KU.** Ebooks at $4.99, enrolled in Kindle Unlimited
  ("Free with Kindle Unlimited membership" on listings). [VERIFIED —
  Amazon listings for Secret Agent 6th Grader, Kid Youtuber]
- **Packaging.** First-person diary format, interior illustrations
  (illustrator David Lee), cartoon character-forward covers. [VERIFIED —
  listings, study guides]
- **Cover/metadata language.** Every spinoff cover and listing carries
  the brand line "From the Creator of Diary of a 6th Grade Ninja," and
  listing titles carry keyword-stuffed parentheticals: "(a hilarious
  adventure for children ages 9-12)," "(a funny book for kids age
  9-12)." [VERIFIED — Amazon listing titles]
- **Box sets.** 3-book collections exist throughout the catalog (Ninja
  Books 1–3, 4–6; Kid Youtuber Books 1–3). [VERIFIED — Amazon listings]
- **Social proof at scale.** 20,000+ five-star reviews across the Ninja
  series on Amazon/Goodreads. [VERIFIED — as reported in author
  coverage]
- **Length.** Ninja Book 1 word-count estimates range ~14–26k words
  depending on edition — i.e., short, fast MG reads, the same length
  class as Spytwins Book 1 (~22k). [VERIFIED estimates — Reading
  Length / BookRags; the range is wide, treat midpoint ~20k]
- **Credited collaborators** (Sal Hunter, Noah Child) appear on
  listings — a small-studio production model, not a lone artisan.
  [VERIFIED credits; their exact roles are not public — ESTIMATE that
  this is a collaborative studio]
- His site (marcusemerson.com) and newsletter could not be fetched
  (403); newsletter/back-matter specifics below are [ESTIMATE] from
  standard indie practice, not observed from his files.

### Is the diary format load-bearing? (the prose question)

Research could not surface a non-diary, non-illustrated prose MG series
with Emerson-class KU velocity. The visible indie MG winners cluster in
first-person, illustrated, Wimpy-Kid-adjacent packaging; community
consensus (kboards threads on self-publishing MG) is that MG is hard for
indies EXCEPT via rapid-release complete series and that kids binge
series once hooked. [VERIFIED that the discourse says this; the absence
of prose exemplars is an absence of evidence, not proof — ESTIMATE:
packaging is roughly half the strategy, and heavily illustrated
first-person packaging is the observed winning uniform.]

**What that means for Spytwins, priced.** Spytwins is third-person prose
by canon, and the author's voice is the point — we do not convert it to
diary format. We close the packaging gap instead:

1. **Character-forward cartoon covers** in a rigid series template
   (same artist, same layout, number badge, brand line). Human
   illustrator: ~$300–600/cover [ESTIMATE — going indie rates].
2. **Interior spot illustrations**, 8–12 per book, B&W (Emerson-density
   is modest, not graphic-novel density). Human: ~$40–80/spot →
   $400–900/book [ESTIMATE]. AI-generated: near-$0 cash but carries the
   §3 disclosure obligation and market risk.
3. **Short chapters, big trim, generous leading** in the print edition —
   free, formatting only.
4. **Emerson-style metadata**: keyword parenthetical in the subtitle,
   brand line on covers from Book 2 on.

### The delta table — his assets vs ours

| Emerson had | We have | Cost to close |
|---|---|---|
| 2012–14 entry: near-empty kids' Kindle shelf, KU launch tailwind (2014), Wimpy Kid wave | 2026: AI-flooded store, KDP velocity caps, discovery is paid | Paid discovery: ~$250–500/mo ads + promo stacks (§3, §4) |
| Diary format + David Lee illustrations | Third-person prose (canon; kept) | Illustration budget ~$700–1,500/book human, or AI + disclosure + risk (§3) |
| Human author-illustrator brand; school-visit-able; trad crossover | AI-centric studio; must file KDP AI disclosures | Honesty posture + human cover artist as brand anchor; owned email list as platform hedge |
| Years of review accretion (20k+ five-stars) | Zero reviews | ARC machine within TOS (§3) + time; nothing buys this |
| One author's throughput ceiling | Studio throughput: Book 1's 12-chapter rewrite took ~2 days wall-clock (recorded) | Already ours — the ONE structural advantage; the plan protects it |

---

## 2. THE RELEASE TRAIN

**Adversary first: what kills a release train.** Not the writing — the
recorded bottleneck is author decision latency and the culture-researcher
gate (`studio/PIPELINE.md` evidence: 12 chapters in ~2 days of pipeline
wall-clock). A train that needs an author decision on a random Tuesday
stalls; a culture gate that runs after drafting forces rewrites. So: all
author decisions batch into one weekly window, and the culture gate moves
BEFORE outlining.

### The weekly decision window (the DevOps insight)

One fixed 2–3 hour block per week — proposed: **Friday**. Everything the
author must decide queues for that window: adoption reads (a ~22k-word
book reads in ~2–2.5 h), outline approvals (~20 min), cover approvals,
canon locks, TK resolutions. Nothing interrupts the author mid-week; the
studio never waits more than 6 days for a decision. Target steady-state
author load: **4–6 h/week total** (the window plus reading).

### Per-book production line (steady state, ~3 weeks wall-clock)

| Days | Stage | Owner | Gate to pass |
|---|---|---|---|
| 1–2 | Culture brief for the city | culture-researcher | No [CHECK] blockers on load-bearing setting facts |
| 2–4 | Outline (Snowflake + engine worksheet) | plot-architect | Engine checklist complete; ledger row opened; SC1–SC4 named; millimeter named |
| — | **Window: author approves outline** | author | Approved or returned with notes |
| 5–8 | Draft, 12 chapters | drafting-assistant (drafter-spytwins persona) | No [TK] at emotional peaks; banned moves respected |
| 9–11 | Structure pass | developmental-editor | No spine-beat failures; SC2 (twins earn it) passes |
| 11–12 | Audience pass | kid-reader-panel | No drift zones flagged red |
| 12–13 | Line pass | line-copy-editor | Mechanicals applied |
| 13–14 | Continuity pass (last) | continuity-keeper | Clean vs canon + ledger |
| 14 | Adversarial read | red-team-critic | No SC cheapening; findings triaged |
| — | **Window: author adoption read** | author | Adopted; CHANGELOG + THREADS + ledger updated together |
| 15–18 | Package: cover, interiors placed, blurb, keywords, back matter | market-pitch-agent (copy) + illustrator | Metadata QA; AI-disclosure form answers recorded |

Three weeks against a one-month cadence = **one week of slack per book**,
which is the burnout and quality buffer, not free capacity. Do not
schedule it.

### The dated schedule

Start condition: Book 1 v2 complete, pending adoption read (recorded in
`concept/premise.md` process note). Today is Tue 2026-07-28.

| Date (2026) | Event |
|---|---|
| Fri Jul 31 | Window 0: schedule Book 1 v2 adoption read |
| Mon Aug 3 | **Book 1 ADOPTED** (read done over the weekend); adoption pass runs (manuscript, CHANGELOG, THREADS, ledger) |
| Aug 3–7 | Book 2 (Tokyo) culture brief + outline; outline approved Fri Aug 7 |
| Fri Aug 28 | **Book 2 DONE** (adopted) |
| Fri Sep 25 | **Book 3 DONE** (city: author decision, window of Aug 21) |
| Fri Oct 23 | **Book 4 DONE — the 4-book launch gate is met** |
| Nov 2 | ARC copies to review platform + parent readers; covers final |
| Fri Nov 20 | Launch-readiness gate: series page plan, back matter in all 4 files, newsletter live, Book 5 adopted |
| **Tue Dec 1** | **LAUNCH: Books 1 AND 2 released same day** (read-through measurable from day one), Book 1 at launch price |
| Tue Jan 5, 2027 | Book 3 releases |
| Tue Feb 2, 2027 | Book 4 releases; **Books 1–3 box set** prepped |
| Tue Mar 2, 2027 | Book 5 releases; box set 1–3 live |
| Monthly | First-Tuesday release thereafter |

December launch rationale: new-Kindle/gift-card season lifts kids' ebook
reading into January [ESTIMATE — seasonal pattern, widely reported; not
load-bearing, January 5 works nearly as well if the gate slips].

### Post-launch steady-state month (month N)

- **Write** Book N+4 (studio runs the line; author spends the windows).
- **Release** Book N (first Tuesday; back matter in Book N-1 updated to
  point at it — KDP allows file updates).
- **Market** Book N-1 (promo-stack it at $0.99 or free for 5 days via
  Select, refresh ads toward it; Book 1 is ALWAYS also marketed — it is
  the series' front door).
- Quarterly: box set of the trailing three; ledger + super-concept audit
  of the trailing quarter (§5, quality tripwires).

The buffer rule: production stays **4 books ahead of release, minimum
2.** If the buffer hits 2, the release cadence does NOT slip — the
marketing month simplifies instead (drop everything but the release and
the ads); if it hits 1, skip one release month. Pre-decided, no debate.

---

## 3. LAUNCH MECHANICS

**Adversary first: what kills a launch.** In MG it is invisibility — the
overview's finding stands: a quiet KDP launch measures the absence of a
marketing machine. The chosen path answers it with catalog velocity plus
paid parent-facing discovery. Second killer: an AI-content compliance
mistake, which risks the account, not the book. Both countermeasures are
built in below.

### KU exclusivity — the call

**Enroll all books in KDP Select from day one.** The model runs on
borrows: each borrow counts toward sales rank, KU books get algorithmic
visibility, and rapid-release series feed binge-borrowing [VERIFIED —
ScribeCount wide-vs-KU analysis; kboards practitioner consensus].
Accepted cost, stated plainly: Select requires ebook exclusivity — no
Kobo/Apple/Google, and **no library ebook channels (OverDrive/Libby)**,
which for a kids' series is a real sacrifice; libraries are an MG
channel. Reversibility: Select terms are 90 days; going wide later is a
checkbox, so this is a low-regret door. Revisit tripwire in §5.

### Pricing

| Item | Price | Why |
|---|---|---|
| Book 1 ebook | $2.99 (launch: $0.99 first 2 weeks) | Front door; 70% band floor; cheap trial for a skeptical parent |
| Books 2+ ebook | $3.99–4.99 | Emerson-observable is $4.99 [VERIFIED]; start $3.99, test up |
| Paperbacks (all) | $8.99–9.99 | ~110–130 pp B&W POD cost ≈ $2.50–2.80 → ~$2.90–3.50/unit royalty [ESTIMATE from KDP 60% formula, verified in overview] |
| Box set (3 books) | $7.99 ebook | Standard; also a KENP multiplier (one borrow = 3 books of pages) |

Keep illustrated ebook files compressed: delivery fees (~$0.15/MB) eat
70%-band margin on image-heavy files [VERIFIED — KDP fee structure].

### Categories and keywords

- Primary: Children's Mystery & Detectives (Kindle node exists and is a
  ranked top-100 list [VERIFIED — Amazon category pages]); secondary:
  Children's Action & Adventure / Spy & Detective niches; claim up to
  three categories via KDP.
- Keywords: parent-search phrases, not kid phrases — "mystery books for
  kids 9-12," "spy books for kids," "books for 10 year old boys/girls,"
  "detective series for kids like [comp]." Emerson-style subtitle
  parenthetical on the listing: e.g., "(a funny spy mystery for kids
  ages 8-12)" [VERIFIED pattern — his listings].
- Have market-pitch-agent build the full map (§ end).

### Covers and illustrations — with the AI question answered straight

**KDP disclosure obligation (current policy, 2026).** KDP requires a
declaration at publish time distinguishing AI-GENERATED (AI produced the
text/images/translation, even if heavily edited by you) from AI-ASSISTED
(human-created, AI-refined). AI-generated content — including images —
must be disclosed to Amazon; the disclosure is internal, not shown on
the product page; failure to disclose risks takedown and, repeated,
account termination; Amazon states disclosure does not affect ranking.
[VERIFIED — KDP policy as summarized across multiple 2026 policy
guides; read the live KDP content-guidelines page before first upload —
aggregators drift.] Under this definition, this studio's drafting
pipeline output is likely **AI-generated text** regardless of the
author's concept/decision ownership — plan to disclose, every book,
every update. Non-negotiable: the catalog IS the asset (§4), and the
account is the catalog's single point of failure.

**The market risk of AI art in kidlit, stated straight.** The kidlit
community (educators, librarians, illustrators, review bloggers) is
vocally hostile to AI illustration; AI-flagged kids' books draw
backlash and review damage [VERIFIED — 100 Scope Notes 2024; 2025–26
coverage]. Nuance that matters: research on parents specifically finds
most will accept AI images when the text is human-directed and images
are reviewed for accuracy [VERIFIED — phys.org, Nov 2025]. Our buyers
are parents, but our amplifiers (bloggers, teacher newsletters) are the
hostile group.

**Recommendation:** hybrid. **Human cover artist** (the brand anchor,
the thing on every ad and thumbnail): $300–600/book, series template
negotiated up front, target a multi-book rate. Interiors: EITHER human
spots at $400–900/book (safe, slower) OR launch **prose-only with
strong covers** and add illustrated editions later if economics support
it. Do not lead with AI interiors in this category; if ever used,
disclose to Amazon and do not misrepresent publicly if asked. Decision
is the author's — budget question §7.

### Series infrastructure

- **Amazon series page** from day one (both books at launch link it);
  numbered titles; rigid template covers.
- **Back matter in every book:** (1) "Read the next one" with link,
  (2) newsletter signup pitched AT PARENTS ("printable spy-skill
  activity pack" magnet — parents opt in; never collect kids' data:
  COPPA), (3) honest review ask worded to the parent, (4) series
  checklist page kids can tick off. Update back matter files each
  release month.
- **Newsletter:** the owned-channel hedge against every Amazon risk in
  §5. Starts at launch, not before (consistent with the overview's
  finding on empty newsletters). Monthly, parent-facing, ships with
  each release.

### Parent-facing channels that actually convert

Gatekeeper reality holds: 8–12s are not addressable by ads (COPPA,
platform minimums) — every dollar targets adults who buy for kids.

1. **Amazon Sponsored Products** — the workhorse: the searcher on Amazon
   for "spy books for kids" IS the parent, mid-purchase. Target comp
   ASINs (Emerson's catalog, Wimpy Kid read-alikes, Stilton, A-Z
   Mysteries) and parent keywords. Expect to lose money the first 1–2
   months while harvesting search-term data [VERIFIED — 2026 ads
   guides]; sub-30% ACOS is a strong target, kidlit realistically runs
   higher on low-priced ebooks — plan blended 60–100% ACOS early,
   judged on catalog read-through value, not single-book ROAS
   [ESTIMATE — benchmark sources give 30% as "strong," none publish
   kidlit-specific ACOS; our low price + KU-read value makes naive ACOS
   overstate loss]. Budget: $200/mo months 1–2, $300–500/mo if
   read-through validates (§5 tripwire).
2. **Promo newsletter stacks (per release/promo):** Freebooksy
   Children's feature ($40, ~30k children's-list subscribers) for
   Book 1 free days; Bargain Booksy Children's feature (requires
   $0.99–$5 price) for $0.99 promos [VERIFIED — Written Word Media
   pricing pages]. Add Book Cave / Fussy Librarian kids' lists
   (~$10–30 each [ESTIMATE]). BookBub Featured Deal (children's) is
   the heavyweight: selective, apply quarterly, take it if offered
   [VERIFIED that it's selective; kids-category price not verified —
   budget ~$150–400 if accepted, ESTIMATE].
3. **Facebook/Instagram ads to parents** (adults 28–45, interests:
   reading with kids, homeschool, Scholastic, Wimpy Kid): legal because
   the target is the adult. Secondary to Amazon ads; test $5–10/day
   only after Amazon ads have proven read-through. Homeschool Facebook
   groups and co-op newsletters allow author offers more readily than
   general parent groups [ESTIMATE — practitioner reports].
4. **Teacher/librarian/blogger outreach** (Reading Middle Grade et al.):
   slow, unpaid, worth one batch per quarter — these are amplifiers,
   and the AI posture (§ above) must be settled before courting them.

### Reviews within Amazon TOS

- ARC copies via **BookSirens or Booksprout** (built-in reader pools;
  readers acknowledge Amazon's rules; reviews must disclose the free
  copy; never require positivity or a star minimum) [VERIFIED — 2026
  ARC guides; Amazon review policy]. Kidlit wrinkle: the ARC readers
  are parents/teachers reviewing as adults — that is fine and normal.
- Back-matter ask in every book. No incentives, no swaps, no family.
- Realistic accrual: single-digit reviews per book in the first weeks;
  Book 1 needs ~10–15 before ads convert decently [ESTIMATE —
  practitioner consensus].
- ARC cycle runs Nov 2 → launch day so day-one reviews post at release.

### Box sets and audio

- Box set 1–3 at month 3 post-launch (Mar 2027), 4–6 at month 6 —
  Emerson-observable pattern [VERIFIED that his collections exist].
- Audio: NOT NOW (overview's finding stands — $1,500+ per title against
  unproven demand). Revisit at 1,000 units/month catalog velocity.

---

## 4. ECONOMICS

**Adversary first: what kills the economics.** Small-margin units times
small volume, while costs are per-book and fixed. The velocity thesis'
answer is the catalog: revenue scales with titles while per-title cost
is flat, so the machine either compounds or it bleeds monthly. Model
both, honestly.

### Unit math (current rates)

- KENP rate: $0.00482/page (April 2026); trailing range $0.004–0.005.
  [VERIFIED — KU payout trackers, 2026]
- A ~22k-word MG book normalizes to roughly 140–180 KENP (KENPC runs
  ~120–160 words/page for kids' layouts with images) [ESTIMATE — no
  official words-per-KENP figure exists; this is the practitioner
  range]. **One complete read ≈ $0.67–0.87; call it $0.72.**
- Ebook sale at $3.99 → 70% − delivery ≈ **$2.60–2.75 net**; at $2.99 ≈
  $1.95; at $4.99 ≈ $3.30 [VERIFIED formula; delivery varies with file
  size].
- Paperback at $9.99 → ≈ **$3.00–3.50 net** [ESTIMATE from verified
  KDP 60% formula and B&W print costs].

The uncomfortable core number: **a KU borrow of one of our books is
worth about 72 cents.** The machine only works if borrows come in
hundreds-to-thousands per month across a growing catalog. That is the
bet, stated plainly.

### Cost side

| Item | Human-visual build | Lean build |
|---|---|---|
| Cover | $300–600 | $300–600 (human either way — brand anchor) |
| Interior spots (8–12) | $400–900 | $0 (prose-only at launch) |
| Human proofread (final gate) | $200–300 | $200–300 |
| Per-book production | **$900–1,800** | **$500–900** |
| Ads (monthly, post-launch) | $200–500 | $200–300 |
| Promo stacks (per release month) | $50–150 | $50–100 |
| Fixed setup (newsletter tool, ARC platform, ISBNs opt.) | $300–600 one-time | same |

Twelve months at cadence: 12 books ≈ $6k–22k gross cash out depending
on build, before any revenue. [ESTIMATE — sums of the above.]
[AUTHOR DATA NEEDED — the budget ceiling decides which column, §7.]

### Monthly scenarios (catalog view — the asset is the shelf)

Assumptions shown; all are [ESTIMATE]. "Full reads" = completed-borrow
equivalents/month, catalog-wide. Read-through (RT) = share of Book N
finishers who start Book N+1.

**Pessimistic — the honest floor (modal single-book MG outcome; ads
never find traction, RT unmeasurable for lack of volume):**

| Month (post-launch) | Catalog | Full reads | Ebook+pb sales | Revenue/mo |
|---|---|---|---|---|
| 2 (Jan 27) | 3 | 60 | 15 | ~$85 |
| 6 (May 27) | 7 | 120 | 25 | ~$160 |
| 12 (Nov 27) | 12 | 180 | 35 | ~$230 |

Against ~$800–2,300/month all-in costs: **the machine never covers its
own monthly costs in this scenario** — cumulative year-one loss roughly
$8k–20k depending on build. If month-4 numbers look like this, §5's
tripwires fire long before the loss compounds.

**Median — promos and ads work adequately, RT ≈ 50%:**
Book 1 ~150 full reads/mo (ads + stacks), decaying RT down-series.

| Month | Catalog | Full reads | Sales | Revenue/mo |
|---|---|---|---|---|
| 2 | 3 | 260 | 55 | ~$390 |
| 6 | 7 | 520 | 100 | ~$780 |
| 12 | 12 | 900 | 160 | ~$1,300 |

Monthly costs covered around **month 9–12 post-launch (Aug–Nov 2027)**
on the lean build, month 14+ on the human-visual build; cumulative
payback mid-to-late 2028. Then it compounds with every title.

**Breakout — the flywheel catches (Emerson-class also-bought traction,
RT ≥ 60%):** Book 1 at ~1,000 full reads/mo by month 3.

| Month | Catalog | Full reads | Sales | Revenue/mo |
|---|---|---|---|---|
| 3 | 4 | 2,300 | 300 | ~$2,550 |
| 6 | 7 | 4,000 | 500 | ~$4,400 |
| 12 | 12 | 7,000 | 800 | ~$7,600 |

Monthly costs covered **month 2–3**; cumulative payback month 6–8. This
is the survivor case, included because it is the model being copied —
not because it is likely. Honest weighting: pessimistic is the base
rate for any single MG indie title; the whole design (velocity, KU,
packaging, paid discovery) exists to buy a draw from a better
distribution. Nobody can promise it does.

**The catalog thesis in one line:** at 40 books, median-scenario unit
economics produce roughly $3–4k/month [ESTIMATE — linear-plus-RT
extrapolation, consistent with the verified 25+-title / ~$3k-month
correlation in the ALLi data]; the same machine at 4 books produces
$400. Every month of cadence held is the compounding payment.

---

## 5. FAILURE MODES & COUNTERMEASURES (the A1 frame, made operational)

Each row: tripwire metric (measured monthly from KDP dashboards unless
noted) and the PRE-DECIDED response. Decisions made now, cheaply, so
they aren't made later, expensively.

| # | Failure mode | Tripwire | Pre-decided response |
|---|---|---|---|
| 1 | **Invisible launch** (MG discovery fails; the overview's core objection) | < 300 catalog full reads/mo AND < 15 Book 1 reviews by end of month 4 (Mar 2027) | Do NOT scale ads into silence. One repair cycle: recover/re-blurb Book 1, one BookBub application round, one free-run stack. If month 6 still under: drop to "shelf mode" — cadence continues if the author still wants the work in the world (the stated goal function), but paid spend caps at $50/mo and §4's loss stops compounding |
| 2 | **Read-through collapse** (series doesn't hook) | B1→B2 RT < 35% by end of month 3 (Feb 2027; measurable from day one because B1+B2 launch together) | Pause Book N+4 production ONE cycle; kid-reader-panel + red-team autopsy on B1's last 3 chapters and B2's first 3; fix the handoff (cliff-hook, back matter, B2 opening); resume. RT is the single most important number this business produces |
| 3 | **KU page-read economics decay** (fund dilution; rate slides) | KENP rate < $0.0040 for 3 consecutive months, or borrows shift to sales-hostile mix | Shift weight to $0.99–2.99 sales pricing + box sets (a box-set borrow triples pages per borrow); run the wide-vs-Select math at the next 90-day boundary — Select is a 90-day door, use it |
| 4 | **Amazon policy change / account risk** (AI rules tighten; disclosure reclassification; the account is the single point of failure) | Any KDP content-policy update mentioning AI (calendar: re-read policy page at every 90-day Select renewal) | Already-built: disclose accurately from day one, every book; keep clean source files + full provenance (this repo IS the provenance log); newsletter list is the portable asset; if terms turn hostile, the catalog goes wide in 90 days |
| 5 | **AI-art backlash** (amplifier community turns on the series) | Any review or blogger callout alleging AI art | Pre-empted by human covers (§3). If interiors ever go AI: never deny, never astroturf; the pre-drafted response states the human authorship of story/canon and the disclosure posture |
| 6 | **Author burnout / decision latency** (the recorded bottleneck becomes chronic) | Two consecutive missed weekly windows, or buffer < 2 books | Buffer rule fires (skip one release month — pre-authorized, no guilt); window shrinks to adoption-read-only; marketing month simplifies to release + ads only. The cadence serves the author's fulfillment goal; the plan bends before the author does |
| 7 | **Quality drift at velocity** (books pass gates but flatten; the engine becomes the rut) | Quarterly: red-team + junior-literary-critic audit of the quarter's 3 books vs SUPERCONCEPTS.md; any SC judged "cheapened," or new-book review average < 4.2 with "same-y" language | One repair sprint on the flagged book pre-release (buffer absorbs it); rotate variance cards deliberately; ledger audit — if S-threads show three books with identical cells, the next outline must break pattern |
| 8 | **Series fatigue in the market** (later books launch soft even with healthy RT) | Book N launch-month reads < 60% of Book N-1's by Book 6+ | Box-set + free-Book-1 recycle to refill the funnel top; vary settings/plot-types from the engine menus harder; consider arc-boundary event book (Book 10) as a re-launch moment |
| 9 | **Ad-cost creep** (CPCs rise; ACOS drifts up) | Blended ACOS > 100% after month 3, judged with KU read value included | Kill generic keywords, keep only comp-ASIN targets that show RT-adjusted breakeven; shift budget to promo stacks (fixed-price, measurable); never raise bids to defend rank |
| 10 | **Velocity flags at KDP** (publishing-pattern scrutiny) | Any KDP hold/review email | Monthly cadence is far under the 3-titles/day cap [VERIFIED — Sept 2023 policy], but respond same-day, never republish around a hold, keep disclosure answers consistent |

---

## 6. THE FIRST 90 DAYS (Jul 28 – Oct 25, 2026)

Author hours target: **4–6 h/wk** (windows + reads). Marketing hours:
**0 until November** — pre-launch, marketing is the studio drafting
materials, not the author doing outreach. Cash out in the 90 days:
covers ordered (2–4 × $300–600) + ARC platform + newsletter tool ≈
**$1,000–2,900** [AUTHOR DATA NEEDED — §7 Q1 gates this].

| Week of | Studio does | Author window does | Hrs |
|---|---|---|---|
| Jul 28 | Stage Book 1 v2 read packet; Book 2 culture brief (Tokyo) starts | Fri Jul 31: confirm schedule; answer §7 questions | 1 |
| Aug 3 | Adoption pass on B1 (ms/CHANGELOG/THREADS/ledger); B2 outline | Weekend read done; Mon: adopt B1. Fri: approve B2 outline; decide pen-name/imprint (Q4) | 5–6 |
| Aug 10 | B2 draft + structure/audience passes; cover-artist shortlist (market-pitch brief) | Fri: pick cover artist to contact; resolve B2 TKs | 3 |
| Aug 17 | B2 line + continuity + red-team; Book 3 city options memo | Fri: choose Book 3 city; approve artist quote | 3 |
| Aug 24 | B2 packaging; B3 culture brief + outline | **Fri Aug 28: adopt Book 2**; approve B3 outline | 5–6 |
| Aug 31 – Sep 21 | B3 through the line; B1–B2 covers in progress; keyword/category map (market-pitch) | Weekly windows: TKs, cover feedback, B4 city choice | 3–4/wk |
| Sep 21 | B3 final passes | **Fri Sep 25: adopt Book 3** | 5–6 |
| Sep 28 – Oct 19 | B4 through the line; blurbs ×4 drafted; back-matter template; newsletter magnet built from engine material (spy-skill pack) | Weekly windows; approve blurbs + magnet | 3–4/wk |
| Oct 19 | B4 final passes; ARC platform account set up | **Fri Oct 23: adopt Book 4 — LAUNCH GATE MET** | 5–6 |

Days 91–126 (Oct 26 – Nov 30) are launch runway per §2's table: ARCs
out Nov 2, readiness gate Nov 20, Book 5 stays on the line throughout
(the train does not stop for the launch). Launch Dec 1.

---

## 7. AUTHOR DATA STILL NEEDED

Carried from the overview where still open, plus new dependencies this
plan creates. Numbered for answering in a window.

1. **Budget ceiling** (the overview's Q3, now sharper): year-one cash
   for covers + interiors + ads + proofs realistically runs
   $6k–22k (§4). What is the actual ceiling? This single number decides
   the human-visual vs lean build and the ad schedule.
2. **Hours confirmation:** is 4–6 h/wk with one fixed weekly window
   sustainable? Which day is the window?
3. **Illustration posture:** human interiors, prose-only launch, or
   AI interiors with Amazon disclosure and the §3 market risk accepted?
   (Human cover is recommended regardless — confirm.)
4. **Imprint/pen name:** publish under the author's name or a studio
   imprint? (Affects the AI-posture story and future books' branding.)
5. **AI-disclosure comfort:** the KDP filings will mark the text
   AI-generated per Amazon's definition (§3). Confirm you accept this
   posture and the public-honesty stance if ever asked.
6. **KU exclusivity consent:** Select means no library ebooks and no
   other stores for enrolled titles (90-day terms). Confirm.
7. **Book 3 and Book 4 cities** (and rough Arc 1 city slate) — needed
   at the Aug 21 and Sep windows.
8. **Platform inventory** (overview Q1, still unanswered): any existing
   list/network of parents, teachers, or homeschoolers for the ARC
   team? Even 10 names changes launch-week reviews.
9. **Floor acceptance:** §4's pessimistic case is ~$230/month against
   real costs. The stated goal is fulfillment from work in the world —
   if month 6 looks pessimistic, is "shelf mode" (cadence with capped
   spend) the preferred continuation, or a full stop? Deciding now is
   failure-mode 1's countermeasure.

## What to ask market-pitch-agent to produce (sequenced)

1. Now: cover-artist brief + shortlist criteria (series template spec,
   Emerson-shelf visual comps).
2. Now: Amazon category/keyword map for MG mystery/spy (parent-search
   phrasing) + Emerson-style subtitle parentheticals for Books 1–4.
3. Aug: blurbs for Books 1–2; series-page copy; the brand line.
4. Sep: back-matter template (next-book link, parent-facing newsletter
   pitch, TOS-safe review ask, series checklist page); newsletter
   magnet copy (spy-skill activity pack).
5. Oct: ARC pitch letter (parents/teachers), promo-stack listings copy
   (Freebooksy/Bargain Booksy character counts), Amazon ads launch
   target list (comp ASINs + keyword seeds), blurbs 3–4.
6. Feb 2027: box-set 1–3 packaging copy.

---

## Sources (accessed 2026-07-28; overview sources carry over)

Emerson, observed:
- Goodreads editions/series: https://www.goodreads.com/work/editions/24327204-diary-of-a-sixth-grade-ninja-diary-of-a-6th-grade-ninja-1 ;
  https://www.goodreads.com/series/list/6429076.Marcus_Emerson.html ;
  https://www.goodreads.com/series/354702-kid-youtuber
- Amazon listings (pricing, KU, subtitle language, collections):
  https://www.amazon.com/Diary-Grade-hilarious-adventure-children-ebook/dp/B009X3BV9E ;
  https://us.amazon.com/dp/B00BCTVXJK ;
  https://www.amazon.com/Diary-6th-Grade-Ninja-Collection/dp/B0DNK4BSKH ;
  https://us.amazon.com/Kid-Youtuber-3-Book-Collection-Creator-ebook/dp/B0FYT9W7KF
- Interviews/coverage (agent outreach, Ben Braver trad deal):
  https://fromthemixedupfiles.com/marcus-emersons-the-secret-life-of-ben-braver/ ;
  https://www.thechildrensbookreview.com/marcus-emerson-author-of-the-super-life-of-ben-braver-selfie-and-a-shelfie/
- Catalog chronology: https://www.bookseriesinorder.com/marcus-emerson/ ;
  https://www.fantasticfiction.com/e/marcus-emerson/
- Length estimates: https://www.readinglength.com/book/isbn-1493527487 ;
  https://www.bookrags.com/studyguide-diary-of-a-6th-grade-ninja/
- (marcusemerson.com returned 403 to fetch tools; site/newsletter
  specifics are labeled estimates.)

KU / KDP economics:
- KENP rate trackers (2026): https://www.automateed.com/kindle-unlimited-payout ;
  https://kdptools.io/kenp-calculator ;
  https://bookbeam.io/blog/amazon-kdp-kenp-rate-guide/
- Wide vs KU: https://scribecount.com/author-resource/publishing-a-book/wide-vs-kindle-unlimited
- MG indie practitioner threads: https://www.kboards.com/threads/self-publish-middle-grade.233926/ ;
  https://hughhowey.com/middle-grade-self-pubbing-success/

KDP AI policy (2026):
- Policy guides: https://kdpbuilder.com/blog/kdp-ai-disclosure-rules ;
  https://www.inkfluenceai.com/blog/amazon-kdp-ai-disclosure-policy-2026 ;
  https://univers.studio/blog/kdp-ai-content-policy-2026/ ;
  https://pubnook.com/article/amazon-kdp-ai-content-policy-disclosure-rules-risks-and-what-authors-must-know
- 3-titles/day velocity cap (Sept 2023): https://www.publishersweekly.com/pw/by-topic/digital/content-and-e-books/article/93207-kdp-will-limit-daily-number-of-new-titles.html ;
  https://selfpublishingadvice.org/self-publishing-news-kdp-ai-new-limits-on-titles/

AI art in kidlit:
- Parent-attitude research (Nov 2025): https://phys.org/news/2025-11-parents-kids-ai-generated-images.html
- Community backlash: https://100scopenotes.com/2024/11/04/the-tidal-wave-of-a-i-childrens-books-is-upon-us/ ;
  https://lighthouse.mq.edu.au/article/2026/may-2026/ai-and-children-books

Ads / promos / reviews:
- Ads benchmarks (2026): https://salesduo.com/blog/amazon-advertising-benchmarks/ ;
  https://bookblaze.co/blog/does-amazon-book-advertising-work-in-2026-what-self-published-authors-need-to-know ;
  https://www.vappingo.com/word-blog/acos-amazon-ads-books/
- Promo lists: https://www.freebooksy.com/freebooksy-feature-pricing/ ;
  https://www.bargainbooksy.com/childrens-feature/ ;
  https://www.writtenwordmedia.com/the-best-book-promotion-sites-to-promote-your-ebook/
- Review/ARC TOS: https://www.iwrity.com/amazon-review-policy ;
  https://www.bookready.net/blog/arc-review-guide-self-published-authors
- Amazon category nodes: https://www.amazon.com/Best-Sellers-Children's-Mystery-Detectives-Books/zgbs/digital-text/155220011
