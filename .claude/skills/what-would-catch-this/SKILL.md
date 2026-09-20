---
name: what-would-catch-this
description: Before pushing or opening a PR, name for every changed file the hook, lint, gate or reader that would fail if the change were wrong — and where nothing would. Gaps feed /lesson. Use on any diff, and always before a [CHAPTER] or [FOLD] PR.
---

# /what-would-catch-this

The doc's question, asked of a writing repo: if this change were
wrong, what would fail?

1. Run `python3 studio/tools/catch-map.py` (the working tree) or
   `python3 studio/tools/catch-map.py origin/main` (the whole branch).
2. Read the table. Every row names what catches it. A row marked
   `gap:` is a change only a human would notice.
3. For each gap, decide: is this one worth a check? If yes, it is a
   `/lesson` (a BAN with a fixture, a CHECK in a tool, a GATE, a
   READER test, a CANON row, or a hook). If no, say so in the PR body
   in one line — "the registry rows are read by the keeper at the
   next fold" — so the author knows what nobody checked.
4. Paste the table's last line in the PR body under a heading "What
   would catch this." pr-lint does not demand it yet; the showrunner
   does.

The map lives in `catch-map.py` and is short on purpose. When a new
check lands, add its path pattern there the same day, or the map
lies.
