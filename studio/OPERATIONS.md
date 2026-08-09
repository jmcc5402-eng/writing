# Studio Operations — the nightly shift, and how to revive it

_Runbook for the automation that drives the studio. Anything a thread
needs in order to start, fire, or rebuild the nightly showrunner lives
here — because a session is disposable and the repo is the brain._

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
