# Studio Operations — the nightly shift, and how to revive it

_Runbook for the automation that drives the studio. Anything a thread
needs in order to start, fire, or rebuild the nightly showrunner lives
here — because a session is disposable and the repo is the brain._

## Author priority window — EXPIRED 2026-08-21

**STATUS, recorded on the nightly shift of 2026-09-04.** The window
expired fifteen days ago and the job it created — reopening the three
parked PRs — was never done. The shift that expired the window went
straight back to campus work and nobody read this section again.
That is the failure this block now records so it cannot repeat: an
expiry date with a job attached is not self-executing.

| Parked PR | Branch (verified present, 2026-09-04) | Reopened as | State |
|---|---|---|---|
| #43 | `mybyb/part2-rung3` @ `5371712` | **#120**, 2026-09-04 | at the author |
| #42 | `youngnick/dock-ruling` @ `6942db2` | **#121**, 2026-09-04 | at the author |
| #41 | `spytwins/b3-vote-mechanism` @ `065833b` | — | **STILL PARKED** |

All three branches are intact. #43 could not be merged as a branch —
it predated the Part I revision and would have reverted four adopted
chapters — so it was re-lifted file by file; expect the other two to
need the same treatment rather than a straight reopen. #41 is the last one, and it
is the first non-campus job on the next shift.

Note for whoever picks up #42: tonight's youngnick decision sheet
(`books/youngnick/notes/decision-sheet-2026-09-04.md`, D7) lands on
the same ground — it recommends retiring the ch2 balk upgrade and
spending the leads' dialogue budget at the dock instead. The dock
ruling parked in #42 *is* that decision. Read them together.

### The window as it was called (historical)

**Strengthened by the author, 2026-08-13: FULL focus.** Through
2026-08-21 the studio works `books/campus-series` exclusively — the
romance program is the portfolio's best shot at Amazon/KU traction,
and this window converts that judgment into momentum. No new
non-campus jobs, drafts, instrument runs, or PRs; the nightly shift
spends its whole budget on the campus queue.

**Parked PRs (closed 2026-08-13, work preserved on branches; REOPEN
when the window ends):**

| PR | Branch | What it holds |
|---|---|---|
| #41 | `spytwins/b3-vote-mechanism` | Book 3 vote-mechanism decision |
| #42 | `youngnick/dock-ruling` | Grace-hears-Nick-at-60% decision |
| #43 | `mybyb/part2-rung3` | Part II ch. 5–8 outline + lexicon questions |

Reopening these (and re-listing them in the author's queue) is the
FIRST job after expiry — parked is not forgotten.

The campus work list, in order (SUPERCONCEPTS ratified via #45):
the Ashford town census (name, economy, the civic venue for the
Book-4 vote), naming/localizing the coordinator–counsel pair,
Set-1-scoped age math, the culprit-bench Set-1 slice, then the 1.1
outline. Campus PRs are written under PR-WORKFLOW rule 9 (for a
stranger). After 2026-08-21 the window expires automatically and
dispatch reverts to normal ranking — renewing it is an author call,
never a default.

*(Original 2026-08-11 ruling was 80/20; superseded by the author's
full-focus call, 2026-08-13.)*

## The nightly showrunner Routine

| Field | Value |
|---|---|
| Trigger ID | `trig_01CvgZHJhX1p9pJp9rDApU7v` |
| Name | Studio Showrunner — nightly shift (all books, in-session) |
| Schedule | `0 7 * * *` (UTC) |
| Binding | **fires into a standing session**, `persist_session: true` |
| Bound session | `session_01DgPqPifEqymJpeH4jNZeaX` |

Its prompt is the shift checklist (process merges → MINOR lane →
compute all books' state → ≤3 instrument jobs → ≤2 PRs → morning
nudge + push notification). The current text is stored on the
trigger; `list_triggers` prints it verbatim.

## Why it is bound to one session (the failure that taught us)

The first version fired a **fresh session per run** (an
`environment_id` Routine with no session binding). It fired on
2026-08-04 and 2026-08-06 and produced nothing at all — no commits,
no branches, no PRs, no nudge. Nothing in the repo moved.

**Working hypothesis, never confirmed from logs:** a fresh headless
session does not inherit this workspace's authenticated toolchain
(GitHub MCP in particular), so the shift died at its first step —
and died silently, because a session with no way to report has no
way to report that either. Rebinding to a standing session fixed it
immediately (three consecutive shifts delivered), which is
consistent with the hypothesis without proving it.

**Rule of thumb for every studio Routine (books, newsroom, anything
ported):** bind long-running agent work to a standing session.
Fresh-session Routines are for work that needs no authenticated
tools.

## How ANY thread can fire the shift on demand

Session binding means only the bound session *receives* the wake-up —
but any session on this account can *fire* it:

    fire_trigger(trigger_id: "trig_01CvgZHJhX1p9pJp9rDApU7v")

Optionally pass `text:` to append run-specific context for that one
firing. The shift still executes inside the bound session, which is
the point: that is where the working tree, credentials, and context
live.

## If the bound session dies (the single point of failure)

A standing session is mortal — archived, expired, or replaced. When
that happens the Routine keeps firing into a dead address and the
studio silently stops moving. Symptoms: `last_fired_at` advances,
but no commits, no PRs, no nudge.

**Recovery, from whatever session is now the standing one:**

1. `list_triggers` → confirm the ID above and read its prompt.
2. `delete_trigger(trigger_id)` — do not leave two nightly shifts
   racing on the same repo.
3. `create_trigger` with the same name, cron `0 7 * * *`, the same
   prompt text, and **`persist_session: true`** so it binds to the
   session issuing the call.
4. Update the "Bound session" row in this file and commit.

## Health check (any thread, any time)

- `list_triggers` — is the shift `enabled`, and is `last_fired_at`
  within the last ~24h?
- `git log origin/main --since=2.days` — did the shift's work land?
- Open PRs — did it leave decisions in the queue?

If it fired but nothing landed, the binding is stale: run the
recovery above. If it never fired, the Routine is disabled or
deleted.

## Related automation

- **Self check-ins** (`send_later`) are one-shot Routines that
  re-arm themselves; they expire with `ended_reason:
  run_once_fired` and are harmless to leave in the list.
- **The newsroom port** (`studio/NEWSROOM-KIT.md`) uses the same
  pattern for its night editor. Its Routine is created only after
  the newsroom's own activation PR merges — so if that PR is
  unmerged, no newsroom nightly agent exists yet. That is a gate,
  not a bug.

## Hazard: parallel agents share ONE working tree

Background agents run in the same checkout as the orchestrator. An
agent that runs `git checkout` / `git checkout -b` moves HEAD and the
working tree **for everyone**, and work can appear to vanish
mid-sequence. Observed 2026-08-10: an orchestrator commit chain
reported success while a concurrent agent was creating a branch, and
the file was never actually recorded — `git log --all -- <path>`
returned nothing.

Rules that follow:
- **Never dispatch two agents that both change branches.** Prefer
  briefs that only read and return text, or that edit files in place
  on the current branch.
- **Agents that need a branch get it prepared for them** by the
  orchestrator, one at a time.
- **Verify, don't trust the exit code:** after any commit that matters,
  confirm with `git log --oneline -- <path>` before reporting it done.
