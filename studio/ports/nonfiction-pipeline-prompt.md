# Port prompt — the non-fiction pipeline

_Paste everything below the line into the first session of the
`non-fiction-pipeline` repo. It assumes that session has READ access
to `jmcc5402-eng/writing` (the source repo). Written 2026-09-24._

---

You are setting up `non-fiction-pipeline`: an agentic pipeline that
produces short non-fiction books for Kindle, many of them, repeatably.
One human (the author) supplies judgment; agents do research,
drafting, checking and packaging. All state lives in this repo as
plain Markdown — never in chat.

**The topics.** History of extreme weather · Allergies around the
world · Weather in ancient Rome · a fourth [TK — the author will
name it]. Kindle only for now. No revenue target — do not optimize
for money; optimize for a book the author is proud of, made fast.

**The source repo.** `jmcc5402-eng/writing` runs this architecture for
fiction and has learned its rules the hard way. You may READ it. You
may NOT write to it, open PRs on it, or copy its book content
(`books/`) — only its ideas and, where noted, its tools as a
starting point. It is heavily tuned to one romance series; most of
its machinery does not belong here. Your job is to take the
load-bearing ideas and leave the rest.

## Read these, in this order

1. `studio/AGENTIC-WRITING.md` — the three kinds (instruction,
   guardrail, evidence) and the one idea that matters most: *an
   unlintable rule is enforced by requiring a named reader's verdict
   file on disk.*
2. `studio/MECHANISM.md` — spec / declaration / checker / trigger, and
   the eight rules learned the hard way.
3. `studio/ENVIRONMENT.md` — the table "The guardrails, and the failure
   each one killed," and "What is deliberately NOT enforced."
4. `studio/PR-WORKFLOW.md` — "The core mechanic" and "One open PR at a
   time." Skip the per-series criteria.
5. `studio/DRAFTING-PROTOCOL.md` — only "Instrument governance — the
   over-tooling guard."
6. `CLAUDE.md` — the hard rules and "Working style: forward, not
   backward."
7. `studio/AUTHOR-TASTE.md` — entries 1, 9, 10, 13, 14 only. The rest
   are romance taste and do not transfer.
8. `.claude/agents/` — skim `continuity-keeper`, `developmental-editor`,
   `line-copy-editor`, `red-team-critic`, `culture-researcher`,
   `market-pitch-agent` as starting shapes.
9. `studio/series-kit/README.md` — how a new series is started from
   templates.

Do not read further unless one of these points you there for a
specific reason.

## PORT — take these as they are

- **The repo is the brain.** Decisions are committed the day they are
  made; a ruling that lives only in chat does not exist.
- **A PR is a decision with an approval button.** The PR carries the
  doc edit, not just the question. One open PR at a time.
- **Instruction → guardrail → evidence.** Any rule that keeps being
  broken gets promoted from a sentence to a check or a gate.
- **The verdict-file gate.** A stage cannot be marked done unless the
  named reviewer's verdict file exists and is non-trivial (a gate
  checks content, not attendance).
- **Spec / declaration / checker / trigger.** Checkers take a book
  directory and know nothing else about the book. A checker with no
  trigger (hook or one-command suite) is a script someone has to
  remember.
- **The eight rules from MECHANISM.md,** especially: measure before you
  set a threshold; narrow a check until it is silent on clean text;
  never ban a shape, measure its rate; report coverage, never assume
  it; say in the checker what it cannot do.
- **`[TK ...]` and `[CHECK: ...]` markers,** greppable.
- **The lesson loop.** Every author catch becomes two fixes: the page,
  and the check that stops it recurring (`LEDGER.md`).
- **Author notes → taste sheet.** Author comments are logged verbatim
  (`AUTHOR-NOTES.md`) and distilled (`AUTHOR-TASTE.md`); every drafting
  or judging agent reads the taste sheet.
- **Versioned agents.** Roster, changelog, backlog. Never edit an
  agent without citing the run that showed the gap.
- **Talk to the author like an author, not an engineer.** PR bodies
  are short, plain, and readable by a stranger.
- **Forward, not backward.** A finding improves the next book; it
  revises a finished one only when it is mission-critical.
- **The over-tooling guard.** No new instrument until the existing
  ones have run on real prose; one in, one out after that.
- **Check the product, not the source.** Lint the assembled Kindle
  text (`export-book.py` is the model), not only the chapter files.

## ADAPT — same idea, non-fiction version

| Fiction original | Non-fiction version |
|---|---|
| Canon wins / don't invent canon | **Sources win / don't invent facts.** A claim with no source is `[CHECK]`, never quietly filled in |
| `canon/FACTS.md` + `fact-check.py` | **`SOURCES.md` + a claims ledger** per book: every date, number, name and quote tied to a source; a checker flags unsourced claims |
| `continuity-keeper` | **fact-checker**: claims against sources, internal consistency (dates, units, spellings) |
| `culture-researcher` | **researcher**: builds the research dossier before any outline |
| `SUPERCONCEPTS.md` | **`PROMISE.md`**: the 2–3 things this book promises the reader and a test for each chapter |
| `THREADS.md` (plants → payoffs) | **Argument map**: every question the intro raises is answered; every chapter earns its place |
| Snowflake outline / series-kit | **Book kit**: premise → dossier → outline → draft → check → package, one template set reused for every book |
| Reader panels | **Target-reader panel**, one persona per topic (the curious commuter, the allergy parent, the Rome buff) |
| `ai-tells.py`, `bans.txt`, `prose-guard.sh` | Same tools, re-measured on this repo's own prose before any threshold is set |
| `market-pitch-agent` / `gtm-strategist` | **Kindle packager**: title, subtitle, blurb, categories, keywords, cover brief |

## LEAVE BEHIND

Everything romance- or fiction-specific: the matrix, heat and romance
levels, `dialogue-lint`, `stakes-check`, `opening-sameness`,
`targets-check`, the kid and romance reader panels, the author-proxy's
seven fiction questions, the audio gate, the stagger, the release
`cycle.py`, the nightly showrunner, thread scopes. Any of these may
come back later **only** if a real failure here calls for it.

## BUILD NEW

1. **The source gate.** A chapter cannot be accepted while it carries
   an unsourced factual claim or an unverified quote. This is the
   non-fiction equivalent of the accept gate and the single most
   important check.
2. **The close-paraphrase check.** Draft prose must not track a
   source's sentences too closely. Measure first, then set the line.
3. **A research dossier stage** before outlining: sources gathered,
   graded (primary / scholarly / popular), with what each is trusted
   for.
4. **Kindle packaging** as a stage with its own verdict file: front and
   back matter, table of contents, metadata, and KDP's AI-content
   disclosure answered honestly.
5. **The repeatable book kit** — the thing that makes this a pipeline
   and not four one-off books. Book 2 should take noticeably less
   effort than Book 1.

## How to proceed

Agile: one small, finished increment at a time.

1. **First PR — the plan, not the build.** Write `PORT-PLAN.md`: the
   port / adapt / leave / build table above, corrected by what you
   actually found in the source repo, with one line per item on why.
   Add `CLAUDE.md` (hard rules, layout, conventions) and
   `PIPELINE.md` (the stages). Nothing else.
2. **Second PR — the minimum room.** Four or five agents at most
   (researcher, drafter, fact-checker, line editor, Kindle packager),
   the book kit templates, and the source gate. No other tools yet.
3. **Then one book end-to-end,** on whichever topic the author picks.
   Only after it ships do you add instruments, and only for failures
   that book actually showed.

## Questions to put to the author (in the first PR, not in chat)

- What is the fourth topic?
- Target length per book? (Short Kindle non-fiction usually runs
  10,000–30,000 words — the author decides.)
- One book per topic, or a short series per topic?
- "Extreme weather" and "weather in ancient Rome" overlap — one series
  with two books, or two separate lines?
- Voice: one consistent narrator voice across all topics, or one per
  topic? Is there a sample of the author's own writing to calibrate
  against?
- How much does the author want to read per book — every chapter, or
  only the final manuscript and the package?
