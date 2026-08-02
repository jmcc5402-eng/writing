# The Agentic Studio — a portable blueprint

_A generic, anonymized description of a working system: one human
directing a team of AI agents that runs a small publishing operation
around the clock. The products here are book series; the architecture
transfers to any domain where a small number of humans own judgment
and a team of agents owns throughput. Written 2026-08-02, after the
system's first full end-to-end week._

## The one-paragraph version

The human is not the maker; the human is the **engineering director**.
Agents do the making — planning, drafting, research, review, market
analysis — asynchronously, including overnight. All state lives in
versioned plain-text documents in one git repository (never in anyone's
chat history), and every decision that belongs to the human arrives as
a **pull request** whose diff already contains the recommended change.
The human's entire job compresses to: read short PRs, merge or comment,
and occasionally do the one thing only they can do (final read,
voice-defining passage, taste call). Merging a PR is simultaneously
the approval AND the bookkeeping — there is nothing to remember.

## Principle stack (the load-bearing rules)

1. **Docs are canon; chat is not.** Every product has a small set of
   authoritative documents (concept, rulebook, cast/glossary, status
   ledgers). If work contradicts a doc, the doc wins; conflicts get
   flagged, never silently "fixed."
2. **Decisions get recorded, not remembered.** Every settled question
   becomes a dated, append-only entry in a decision log. Open
   questions live in the same docs, marked with greppable tags
   (`[TK ...]` = unresolved, `[CHECK: ...]` = needs verification), so
   nothing is re-litigated from memory and nothing is silently
   invented.
3. **Propose, don't apply.** Agents apply mechanical fixes directly;
   anything structural or judgment-bearing ships as a PROPOSED
   artifact awaiting the human's flip. Drafts never overwrite the
   deliverable-of-record until a formal adoption step.
4. **Warnings, not walls.** Two rule tiers. Walls always block:
   the product's non-negotiables (factual canon, audience contract,
   quality invariants, the human's voice/vision). Everything numeric
   or cadence-based is a warning — bendable per instance with one
   recorded waiver line: `WAIVED: <rule> — <reason> (owner, <date>)`.
   Auditors report waived violations as compliant-by-waiver; unwaived
   ones as findings. Bending is fine; bending must be on purpose and
   on the record.
5. **Honest ledgers.** A per-product ledger records what was actually
   DELIVERED, not what plans aspire to ("feature X: NOT delivered —
   claimed in the spec, absent from the artifact" is a valid,
   valuable cell). The ledger, not the roadmap, is the audit trail.
6. **Compute state, store nothing.** Status dashboards rot (a stale
   "✅ Complete" cost more than no dashboard). The program-manager
   agent derives every product's true position fresh from the
   documents on every run.
7. **One small finished increment at a time.** Ship, learn, pick the
   next one.

## The team

About a dozen specialist agents with narrow remits, plus process
machinery. Roles, genericized:

- **Planner** — turns an approved premise into a structured plan
  (with a required audit: every setup mapped to its payoff).
- **Maker** — expands an APPROVED plan into first-draft product, in
  the human's voice; hard-gated (refuses to run without an approved
  plan and a voice/style sample).
- **Three reviewers, run separately and in order** — structure-level,
  sentence/surface-level, then facts-vs-canon LAST (earlier passes
  invalidate fact checks). Keeping them separate is deliberate:
  their value comes from not blurring.
- **Audience simulator** — reacts as the target audience would.
- **Red team** — the harshest fair read before anything goes out.
- **Researcher** — verifies real-world facts with sources; flags
  representation/sensitivity issues; everything uncertain gets a
  `[CHECK]`, never a guess.
- **Market strategist** — channel economics and sequencing, with
  claims labeled verified / estimate / owner-data-needed.
- **Outside critic** — a two-part verdict + prioritized
  recommendations, each with costs.
- **Showrunner (program manager)** — surveys every product line,
  ranks next jobs, dispatches agent work that needs no human, and
  specs the PRs for what does. Never makes decisions, never merges.

**The team is managed like software.** Agents are versioned (semver)
in a roster; every change requires a changelog entry citing the
production evidence that drove it; known weaknesses live in a backlog.
Generic agents are specialized per product via small **persona**
files (a voice brief + standing constraints + known failure modes) —
personas ride on agents, they aren't new agents.

**Anti-staleness (the variance system).** Repeated identical prompts
converge on the same moves. Fix: small decks of "emphasis cards" per
agent family (e.g., "weight pacing above all this read," "start from
the weakest section"). Each run draws the least-recently-used card —
logged, so card→quality effects stay observable — plus a "banned
moves" list of tics reviewers recently caught. Cards shift emphasis,
never standards; deterministic runs (schedulers, transcription) are
exempt because variance there is damage.

## The decision interface: pull requests

Every human decision is a PR. The mechanics that make it work:

- **The diff contains the edit, not just the question.** The
  recommended option is already applied in the files; alternatives
  are one-liners in the body. Merge = approved = recorded, one tap.
  Comments become rulings the agents apply.
- **One PR = one decision.** Bundling is a process bug (learned the
  hard way: a five-decision bundle left the owner unsure what they'd
  approved). The standard rejection is one comment: "split this."
- **Show the actual artifact lines.** The body quotes the affected
  product passage — not just rule text — so the owner decides from
  the body alone, on a phone, in under a minute.
- **If it's the human's action, it's a PR.** Reading assignments,
  writing stubs, sign-offs — the open-PR queue IS the human's to-do
  list. A review-and-accept task ships as the acceptance PR itself,
  with the reading materials linked in the body, so finishing the
  task and recording the outcome are one motion.
- **A typed taxonomy (~10 types) with a triage title format:**
  `[product][TYPE] one-line ask` — e.g. plan approval, canon
  ratification, rule waiver, blocked-decision, human-input request,
  ADOPTION (the big acceptance gate), release decisions, and changes
  to the agent system itself. Blockers (rules/decisions) triage
  first; big reads get scheduled, not squeezed.
- **A volume budget:** more than ~5–7 open gates means the gates are
  cut too fine; agents stop opening PRs when the queue saturates.
- **Guardrails:** agents never merge; walls are never waived in
  triage; silence is not approval.

## The pipeline (stages with exit gates)

Premise ("survives being said out loud") → Rulebook/canon docs
("rewrite-forcing questions locked") → Plan ("no element exists only
to move information") → Draft ("there is an ending; bad counts") →
Ordered review → **Adoption** (one PR updates the deliverable, its
changelog, its cross-reference maps, and the honest ledger together;
until then everything is tagged unadopted) → Out the door.

Two support artifacts worth copying anywhere:

- **The thread map** — a per-section ledger of what each unit of the
  product introduces, carries, pays off, and hands forward, with
  every long-running thread carrying a greppable ID and `OWED:`
  markers for promises not yet kept. Updated on ACCEPTANCE, not on
  drafting.
- **The dream review** — before building, write the ideal external
  review the finished product would earn, mark the sentences that
  would thrill the owner, then reverse-engineer the table: each ★
  sentence → what must exist for it to be true → EXISTS / PARTIAL /
  OWED. (Cousin of the working-backwards press release; the ★
  dependency table is the teeth.)

## Asynchronous operation

- **Nightly scheduled runs per product line:** a fresh session wakes,
  reads any PRs the human merged (= new rulings), computes state,
  executes at most TWO dispatchable jobs, opens at most TWO new PRs
  (zero if the queue is saturated), and ends with a push notification:
  what the team did, what's waiting, and THE ONE THING — the single
  highest-leverage action the human can take today in under 15
  minutes.
- **Consumption pipelines for human review:** long reads are
  auto-rendered into a clean private web page and locally-generated
  audio (good-enough TTS), delivered alongside the acceptance PR —
  the human reads at a desk or listens on a commute; both match the
  diff exactly.
- **A triage console** (a session command) lists the queue by type
  priority and walks through any PR conversationally, acting only on
  explicit per-item instruction.

## Porting notes (books → any domain)

| Studio concept | Generic equivalent |
|---|---|
| Manuscript | Any complex deliverable (spec, codebase, campaign, filing) |
| Series bible / canon docs | Source-of-truth specs + glossary + decision log |
| Ingredient checklist | Definition-of-done, held as lenses not line items |
| Thread map + OWED | Cross-deliverable dependency ledger + promise tracking |
| Dream review | Working-backwards review/press-release with a ★ dependency table |
| Continuity reviewer | Consistency/QA against the spec, run LAST |
| Culture/fact researcher | Compliance, legal, or domain fact-check gate |
| Adoption pass | Release/acceptance: artifact + changelog + ledgers in one merge |
| Suspicion dial / voice rules | Brand and tone invariants (walls) |

**Start-up order that worked:** principles doc → 3–4 canon docs for
one product → the PR workflow doc → one specialist agent at a time,
versioned from day one → the showrunner LAST (it needs real state to
read). Resist building dashboards; build ledgers.

**Failure modes observed (avoid):** stored status boards rot in a
day; bundled decision PRs destroy informed consent; agents drafting
without an approved plan produce confident wrong work; rules without
a waiver mechanism get silently broken; a scheduler with "creative
variance" churns priorities. Every one of these is designed against
above because every one of them actually happened.
