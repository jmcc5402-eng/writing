# Thread scopes — what a branch may touch

**Read by `studio/tools/thread-scope.py`**, a PreToolUse hook on Edit,
Write, Bash and Agent. A branch listed here with the `environment`
scope cannot edit a manuscript, a brief or a card, cannot sweep the
working tree into a commit, and cannot launch a drafter. The refusal
is the point: an environment thread that can touch the story will,
because the story is always the more interesting job in the room.

The author (2026-09-21): *"I need an engine to hyper focus on the
environment. The other thread always reverts to the story."*

## Scopes

| Scope | May write | May not | Agents it may not launch |
|---|---|---|---|
| `story` | anything | — | — |
| `environment` | `studio/**`, `.claude/**`, `.github/**`, `CLAUDE.md`, `.gitignore`, `books/**/canon/**`, `books/**/CHANGELOG.md` | every other path under `books/` (manuscripts, plots, cards, notes, bibles) | `drafting-assistant`, `line-copy-editor`, `plot-architect` |

`books/**/canon/**` stays open because a CANON lesson is a row in the
book's fact manifest, and that is environment. A book's CHANGELOG stays
open so a canon row can be logged where the book's rule 6 says to.

## Branches

First match wins; `*` is a glob. A branch that matches nothing is
`story`. The environment variable `STUDIO_THREAD_SCOPE` overrides the
table for one shell (hook-check uses it to test the lock; a person may
use it to lock an unlisted branch). `--unlock-thread-scope` anywhere in
a Bash command lets that one command through, and it is visible in the
transcript — the same shape as commit-scope's `--allow-mixed-scope`.
Ledger: L068.

| Branch | Scope | Note |
|---|---|---|
| `claude/model-fable-y2vo9s` | environment | the guardrails thread (2026-09-21) |
| `claude/vibrant-sagan-xvho2l` | environment | the delivery thread — packaging and launch, never a chapter (2026-09-23) |
| `studio/*` | environment | studio branches carry no prose |
| `agents/*` | environment | writers'-room branches carry no prose |
| `campus/*` | story | |
| `claude/ch5-recut-campus-*` | story | the campus 1.2 thread |

## Waivers — story paths a branch already carries

`thread-scope.py --push` refuses a push while an environment branch's
diff against `origin/main` contains a story path. A path listed here is
allowed anyway. A waiver names its reason and what ends it; it is meant
to look like debt, because it is.

| Branch | Paths (comma-separated globs) | Why | Until |
|---|---|---|---|
| *(none — the 2026-09-16 waiver was retired when #183 merged, which accepted those ten chapters onto main)* | | | |

## Changing a scope

Edit the row and say why in the commit. A thread that needs to touch
the story is not locked wrong; it is the wrong thread for that job.
Leave the page fix on the board (the book's BACKLOG line or the open
PR) for the book thread, and build the check here.
