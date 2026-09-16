# Conversion audit — the taste sheet, entry by entry

**Mined 2026-09-15 from `raw/01-kickoff-taste-sheet-ch5.md`** (session
`01QTG1FrnesYj8GqPKzMQrXC`, Sep 3–4). One question per entry: the sheet
names a *Check* — **is that check a mechanism, or another document?**

## The finding

The ledger works. `AUTHOR-NOTES.md` caught every rejection in this
transcript, verbatim, including the author's own Sep-4 request for the
system and his definition of "touch." Nothing was lost.

**And the conversion is where it breaks.** Of nineteen taste entries,
**four are enforced by something that runs.** The other fifteen name a
"check" that is a law in `STYLE.md`, a field in a brief template, or a
reader who has to be remembered.

The author asked for this system on **2026-09-04** — *"I want to set up
a system where my comments are regularly reviewed by the agents as
another mechanism to avoid pitfalls that I don't like."* It was built
inside two hours, thoroughly, and it is good work. It was built as **two
markdown files that agents are instructed to read.** Eleven days later a
thread forgot the superfan, a drafter self-counted 43 words as 27, and
five contradictions reached main.

The request was right. The build answered it with the strongest
available instruction instead of the weakest available guardrail.

## The audit

| # | Entry | Its stated check | Kind | Runs? |
|---|---|---|---|---|
| 1 | Say the actual thing | say-it test (STYLE.md) + naming report in the lint | mixed | **partly** |
| 2 | Ups and downs | REVERSAL slot, END REGISTER in the brief | instruction | `ending-check.py` exists and is not wired to this |
| 3 | Real wounds, real stakes | arc gate (PIPELINE §3b), ARC BEAT line | instruction | no |
| 4 | The leads get closer | closeness ladder (STYLE.md), COUPLE LINE | instruction | no |
| 5 | Modern, not campy | furniture blacklist + beverage **grep** | **guardrail** | **yes** |
| 6 | Once a book | RECENT.md bans + chapter lint | **guardrail** | **yes** |
| 7 | Upbeat, light, hot | FUN/ROMANCE meters, panel inventories | reader | ungated |
| 8 | Romance first | the floor: three beats, two kinds | **guardrail** | **yes** (`romance-build-check.py`) |
| 9 | Don't make it perfect | imperfection law (VISION), endings budget | instruction | `ending-check.py` covers half |
| 10 | Easy to read and hear | audio reference, listening file per PR | **evidence** | **yes** (`listening-file.py`) |
| 11 | The leads are seen | one noticing beat, the age grep | mixed | partly |
| 12 | Show the fight | staged clash in the directive | instruction | no |
| 13 | **Talk to me like an author** | every message passes the say-it test | instruction | **no — and unenforceable as written** |
| 14 | **Make it an instrument** | every lesson becomes a ban/template/check the same day | instruction | **no** |
| 15 | Root for them | ROOTING FOR line, the beer test | instruction + reader | ungated |
| 16 | Slow down the good parts | STYLE "Slow the good parts" | instruction | no |
| 17 | Weather that forces a thing | outline audit against the checklist | instruction | no |
| 18 | Not a poem, not a mystery | lint's long-sentence and and-chain counts | **guardrail** | **yes** |
| 19 | The board | STYLE "The epigraph", brief line, keeper audit | instruction | now partly (`prose-guard` word cap) |

**Enforced: 5, 6, 8, 18, plus 10 as evidence. Four checks and one
artifact, against nineteen standing wants.**

## The two entries that matter most

**Entry 14 is the ratchet, written as an instruction.** *"Every lesson
the author's ear catches becomes, the same day, one of three things: a
greppable ban, a kit template, a check."* That is exactly the right
rule. It is a sentence in a markdown file, and nothing verifies that any
lesson became any of the three. **The rule that creates guardrails is
itself an instruction** — which is why the count is four.

*Fix:* every `AUTHOR-NOTES` row carries a `became:` field, and a weekly
report lists rows where it is empty, oldest first. That is a query, not
a virtue.

**Entry 13 is about the agent, not the prose.** *"Talk to me like an
author, not an engineer"* — the author ruled on Sep 3 that the say-it
test *"applies to your writing to me as much as to the manuscript."*
Nothing checks agent output to the author. This is the entry most likely
to decay silently, because no reader panel reviews a status message.

*Fix:* the PR template already exists. Lint the PR body — banned
noun-phrase stacks, a first line that says the actual thing.

## Process failures in this transcript (nobody's fault, all mechanical)

| Where | What happened | Kind |
|---|---|---|
| Sep 3 22:06 | *"One line in the changelog runs to 81 columns; I'll wrap it"* | caught by eye — now `prose-guard` |
| Sep 4 01:41 | *"the audit notes file on disk is a stub (my extraction missed the report)"* | **silent data loss, caught by luck** |
| Sep 4 02:32 | *"The script failed on a quoting error before writing anything"* | no failure check |
| Sep 4 14:14 | restart interrupted three background waits | the restart problem, twice in two weeks |
| Sep 4 14:15 | *"another thread has folded ch 7… my duplicate fold commit was redundant"* | **two threads did the same work** |

The stub-file one is the worst and the most quietly dangerous: an agent
wrote a report, the extraction dropped it, and a file existed on disk
with nothing in it. **`accept-gate.sh` currently checks that a verdict
file exists. It should check that it is non-trivial.** Filed as a fix.

## What this says about the corpus

The mining premise needs correcting, and that is worth more than being
right. **I expected to find rejections the ledger had missed. There are
none in this file.** The ledger is excellent.

So the corpus's job is not capture — it is **conversion tracking**: for
every recorded want, what runs? The rejection corpus becomes a coverage
report, and the `became: NONE` rows are the backlog, ranked by how many
times the author has had to say the same thing.

His strongest through-line, *say the actual thing*, appears on **nine
dates between Aug 8 and Sep 3.** Nine repetitions is the price of a
missing check.
