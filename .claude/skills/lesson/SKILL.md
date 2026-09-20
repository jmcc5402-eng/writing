---
name: lesson
description: Turn an author comment, PR note or chat ruling into BOTH halves of a fix — the page, and the environment that lets it recur. Use on every merged PR with comments, on any chat ruling about the prose, and whenever a catch lands that no instrument caught. A [FOLD] PR cannot open until this has run (pr-lint runs lesson-check).
---

# /lesson

The author (2026-09-20): "every bug does two things: fix the bug, and
fix the environment guardrails." This is the second half, as a
procedure the environment checks. Before it, a catch became a line in
STYLE or RECENT — an instruction — and the hook that greps for bans
carried six phrases from August while the ledger carried twenty.

## The loop, per catch

1. **Write the author's words down first.** A row in
   `studio/AUTHOR-NOTES.md` (number, date, source, the quote, what it
   means, status). The words are the spec; paraphrase later.
2. **Fix the page.** A fold drafter with the comment verbatim in its
   brief (a MAIN MOVED section on the chapter brief), or a one-line
   orchestrator fix for a mechanical miss. Log it in the book's
   CHANGELOG.
3. **Classify the catch** — one Kind, from `studio/lessons/LEDGER.md`:
   - **BAN** — a grep can find it. Add a line to
     `studio/lessons/bans.txt` (ID, regex, note) AND a sentence to
     `studio/lessons/fixtures.tsv` that must trip it. Run
     `python3 studio/tools/bans.py --test`. It is now enforced by
     `prose-guard.sh` on every manuscript edit and by `chapter-lint.sh`.
   - **CHECK** — a mechanical property (a count, a share, a length).
     Add the rule to the tool that owns it under `studio/tools/`, with
     the lesson ID in a comment, and a fixture.
   - **GATE** — a stage that must not be skippable. A line in
     `accept-gate.sh`, `brief-gate.py`, `card-lint.py` or `pr-lint.py`
     with the ID.
   - **READER** — only a reader can judge it. Name the test in the
     agent file (the panel, the keeper, the superfan) and add a row to
     `studio/lessons/reader-tests.txt` (ID, agent, test name, verdict
     glob, token). The accept gate now demands the token on the
     verdict's `TESTS:` line — the reader ran it, or the chapter waits.
   - **CANON** — a fact. A row in the book's `canon/FACTS.md` with a
     regex for the contradiction; `fact-check.py` greps it. A ruling
     goes in `DECISIONS.md` too.
   - **PROCESS** — a step people forget. A hook in
     `.claude/settings.json`, or a skill.
   - **INSTRUCTION** — nothing can enforce it. Allowed only with the
     reason written in the Enforced-by column; the instrument-auditor
     re-asks every four chapters whether that is still true.
4. **Add the ledger row** to `studio/lessons/LEDGER.md`: ID, date, the
   AUTHOR-NOTES row number, the catch in a phrase, Kind, the page fix,
   the enforcer, status.
5. **Run `python3 studio/tools/lesson-check.py`.** It refuses a row
   whose enforcer does not exist, a ban with no fixture, a reader test
   the agent file does not carry, and any author note from the last
   seven days with no ledger row. `pr-lint.py` runs it on every
   [FOLD] PR; `guardrails.sh` runs it always.
6. **Then the instruments that still want words:** STYLE or STANDARDS
   for the rule in prose, AUTHOR-TASTE for a new standing want, RECENT
   for the drafter's brief. These are the map; the ledger is the
   territory.

## What "enforced" means here

A ban is enforced when its fixture fires. A reader test is enforced
when the gate demands the token. A gate is enforced when the state
transition cannot happen without it. A rule that exists only in a
Markdown file is an instruction, and the ledger says so.
