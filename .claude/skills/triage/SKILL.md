---
name: triage
description: Triage the author's open pull requests — list the decision queue by PR type, walk through any PR conversationally, and merge or comment on the author's instruction. Use when the author wants to review PRs, clear the queue, or asks "what needs me?"
argument-hint: "[optional: a PR number or type to jump to]"
---

# Triage

Run the author's PR queue per `studio/PR-WORKFLOW.md`. The author is
the engineering director: PRs are recorded decisions awaiting their
button. Your job is to make each decision take under two minutes.

## Steps

1. **Pull the queue.** List open PRs on the writing repo using the
   GitHub tools available in this session (MCP `list_pull_requests`,
   or `gh pr list` where the CLI exists). If an argument names a PR
   or type, jump straight to it after a one-line queue count.
2. **Present the queue, blockers first.** Sort by type priority:
   RULE and DECISION (they block running work) → CANON → PREMISE →
   OUTLINE → SERIES → RELEASE → AGENTS. List ADOPTION and
   AUTHOR-INPUT last, labeled "schedule, don't squeeze" — they need
   the author's reading/writing time, not a gap between meetings.
   One line per PR: number, `[book][TYPE]` title, the Ask line from
   the body, what's blocked, any deadline. Flag malformed PRs
   (missing type, bundled decisions) — the standard response is one
   comment: "split this."
3. **Walk through on request.** For any PR the author picks: give
   the ask and the recommendation first, then summarize the diff
   file by file. For OUTLINE/ADOPTION PRs, offer chapter-level
   walkthrough ("read me ch 7," "what changed in the ledger?").
   Answer questions from the diff and the canon docs — never from
   memory of what an agent probably meant.
4. **Act only on explicit instruction, one PR at a time.**
   - "Approve/merge" → merge it, then confirm in one line what just
     became canon and what work it unblocks.
   - A ruling or change → post it as a PR comment (this becomes the
     recorded ruling; the owning agent applies it). Do not apply the
     change yourself unless the author says to.
   - "Skip" → leave untouched; silence is not approval.
5. **Close the session with the tally.** Merged / commented /
   remaining, plus the single most urgent leftover.

## Guardrails

- Never merge without the author's explicit word for that specific
  PR — "approve all" must be confirmed by listing what "all" is.
- Never merge a PR this session (or its agents) authored: authors of
  a change don't approve it. Flag it and leave the button to the
  human.
- Walls are not negotiable in triage: if a PR asks to waive a wall
  (canon fact, age band, fair play, HEA, heat band, safety rail),
  say so — it needs a redesign PR, not a merge.
- One book per PR (workspace rule). A PR touching two books gets
  "split this," not a merge.
