# Acknowledged findings — what the suite has already said

**Read by `studio/tools/ack.py`.** A finding matching a row here is not
printed as a block by `guardrails.sh`; the run says how many it
suppressed and under which row. Nothing is deleted and nothing is
silent.

On 2026-09-23 the suite printed **39 findings against 11 passes**, and
most of the 39 it had printed every day for a week. A suite that reports
thirty-nine things every run is a suite people stop reading — and a
check nobody reads is an instruction again.

## The two kinds

| Kind | Means | Who may add it | When it comes back |
|---|---|---|---|
| `TRACKED` | already an open row on the handoff board — the board is carrying it to the thread that must act | either thread | **automatically**, the moment the cited row is closed. `ack.py` checks, so closing a row can never hide a finding |
| `RULED` | the author has decided it; the finding is correct and the answer is no | **the author only** — the row names him and the date | when `Until` is met |

A `RULED` row without an author and a date is not honoured. An agent
acknowledging its own findings is an agent marking its own homework.

## In force

| Pattern (glob, matched case-insensitively against the finding line) | Kind | Ruled by | Why | Until |
|---|---|---|---|---|
| `*sentence lengths too uniform*` | TRACKED | environment thread 2026-09-23 | H001 carries the flat-rhythm finding to the book thread with the measurement and the cause; the per-chapter repeat adds nothing | H001 closes |
| `*a table in february*` | TRACKED | environment thread 2026-09-23 | H003 records this as a deliberate motif, not a tic — the contract-review refrain, four uses on purpose | H003 closes |

## Candidates, for the author

`python3 studio/tools/ack.py --propose` lists what the suite repeats.
These are the ones that need a ruling rather than a row:

- **Book 1.1's prose findings** (`campus-series/ch01` em dash, `ch25`/`ch26`
  para-final fragments, `ch26`/`ch28` antithesis openers — five per run).
  Book 1.1 is finished and the author has said the expensive surface is
  not worth touching. If that is a ruling, these should be `RULED` and
  stop reporting. Until he says so they keep printing, because an agent
  does not get to retire its own findings.
- **The Modernity gap** (measures 1.5 / 2.1 against a sheet saying 3 / 5).
  Deliberately still printing: it is on the author's own next-list, and
  the answer is either "lower the sheet" or "change the rooms in ch 25+".
  It should be acked the day he rules, not before.
