# Idea: the agentic book studio

*Captured 2026-07-27, at the author's request, after three days of building
this workspace. Status: **parked for later exploration.** Nothing here is a
commitment; it's the idea, the evidence, and the open questions, written down
so it survives.*

## The idea in one line

The system running this workspace — a versioned writers' room of AI
specialists with canon discipline, thread maps, super concepts, variance,
and working-backwards reviews — is itself a product: an **agentic writing
assistant**, or at full scale, an **agentic book production company**.

## Where it came from

This wasn't designed as a product. It accreted, decision by decision, while
actually producing three real books — which is exactly why it might be one.
In three days this workspace:

- ran a 9-specialist writers' room across three books in different genres
  (middle-grade series, adult humor non-fiction, all-ages frontier myth)
- rebuilt each book's opening chapters, with independent critics verifying
  the rewrites beat the originals
- recovered and reconciled a decade-old manuscript archive from Drive
- invented, tested, and *versioned* its own editorial machinery

The Spytwins repo had the seed first: a `book-studio` plugin plan
(now parked at `../plugin/`). This idea is that seed, grown.

## The reusable IP (all of it already exists, with receipts)

| Mechanism | Where it lives | What it does |
|---|---|---|
| The writers' room | `.claude/agents/` | 10 versioned specialists with non-overlapping remits |
| Agent project management | `../agents/` | Roster, changelog, backlog — agents managed like software, changes driven by production evidence |
| Variance system | `../agents/variance/` | Decks + LRU draw log + banned-moves ledger; "vary the lens, never the law" |
| Canon discipline | root + book `CLAUDE.md`s | Canon wins; don't invent (TK/CHECK); propose don't apply; decisions recorded not remembered |
| Thread maps | `books/*/THREADS.md` | Per-chapter carry-over ledger + greppable thread index with OWED debts |
| Super concepts | `books/*/SUPERCONCEPTS.md` | The 3–4 things that make a book sell, each with a chapter test; hard rule 8 |
| Dream reviews | `books/*/notes/dream-review.md` | Working backwards from the rave: ★ tingle-lines traced to concepts and owed scenes |
| The pipeline | `../PIPELINE.md` + workflow runs | analyze → snowflake → draft (distinct personas) → adversarial review |
| Import discipline | `books/youngnick/manuscript/` | Verbatim recovery of legacy manuscripts with canon annotation |

## Why it might matter (the theses to test later)

1. **The unit of value is the *room*, not the model.** Everyone has access
   to the same models; the editorial separation (developmental ≠ line ≠
   continuity), the canon discipline, and the evidence-driven agent
   versioning are what made output quality climb here.
2. **Authors don't want a ghostwriter; they want a staffed studio that
   protects their voice.** The hard rules that made this work are all
   protections: voice is the point, propose don't apply, canon wins. That's
   a positioning no "AI writes your novel" product has.
3. **The artifacts are the moat.** Thread maps, super concepts, and dream
   reviews are legible to a human author — the system's state is readable,
   auditable, and portable. That's rare in agent products.
4. **It's already multi-genre.** The same room served a kids' mystery, a
   gift book, and a frontier myth in one week, parameterized only by
   personas and each book's own canon docs.

## Possible shapes (undecided, deliberately)

- **A plugin/product:** the writers' room in a box — ship the agents,
  skills, doc templates, and rules as an installable studio
  (the `../plugin/` packaging is a head start).
- **A service:** an agentic book production company — authors bring a
  premise or a trunk manuscript (like the Drive recovery); the studio runs
  the pipeline; humans stay the authors of record.
- **A method + content:** the system as a documented practice (the book
  about the studio), with the tooling as companion.

## Open questions for the async exploration

- [ ] Who is the customer: authors, publishers, or IP owners?
- [ ] What's the demo? (The before/after chapter rewrites with critic
      verdicts are the obvious candidate — they're already in this repo.)
- [ ] What of this is defensible vs. instantly copyable?
- [ ] Does the variance system measurably matter? (The LOG is designed to
      answer this — keep logging.)
- [ ] Legal/positioning: "author's voice is the point" as a brand promise —
      what does that require contractually and technically?
- [ ] Name. (`book-studio` is the placeholder from the Spytwins era.)

## How to pick this up later

Start a session, point it at this file, and say "explore the studio idea."
Everything referenced above is in this repo; the three books are the living
case studies, and their git history is the demo reel.
