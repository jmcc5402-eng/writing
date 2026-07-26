# Spytwins — Project Context

**This repo is a book series, not software.** No code, no builds, no tests.
The deliverables are manuscripts, outlines, canon docs, and go-to-market material.

## What this is

A middle-grade (ages 8–12) mystery-adventure series: twins **Amanda and Andrew
Wilson** travel the world with their consultant parents, solving a mystery in
each new city — never suspecting their parents are secretly spies. Planned as
**40 books in 4 ten-book arcs**, ending with the twins rescuing their kidnapped
parents.

## Canon — read before writing anything

| File | Authority on |
|------|--------------|
| [`concept/premise.md`](concept/premise.md) | Premise, the 40-book arc, tone/audience, **locked canon decisions** |
| [`series-bible/story-engine.md`](series-bible/story-engine.md) | The reusable story engine: per-book checklist, beat structure, skills ladder, idea menus |
| [`characters/characters.md`](characters/characters.md) | Every character's name, traits, tells, and role |
| [`roadmap/go-to-market.md`](roadmap/go-to-market.md) | The agile launch plan (books → graphic novel → comic → screen) |
| [`STATUS.md`](STATUS.md) | Where the project stands right now and what's next |

**Never contradict canon.** If a draft conflicts with these docs, the docs win —
flag the conflict rather than silently "fixing" the canon. If new canon gets
established (a new place, gadget, or recurring character), add it to the docs.

## Hard rules

1. **Names are locked.** Amanda & Andrew Wilson (twins), Erin & Adam (parents),
   Jenny & Jacob (aunt/uncle), Blazer (dog), Moonbeam (cat). Earlier drafts used
   other names — those are retired. See the canon decisions in `concept/premise.md`.
2. **The author's voice is the point.** The author writes the concept, characters,
   and vibe. Assist with *structure, continuity, critique, and selling* — do not
   overwrite their voice or rewrite their vision.
3. **Every setup pays off.** No solutions by luck or coincidence; the twins must
   earn the answer from planted clues.
4. **Age-appropriate always.** Real stakes, never scary or violent. Problems are
   solved with brains, curiosity, and teamwork.
5. **Propose structural changes; don't apply them unasked.** Mechanical copy fixes
   can be applied directly. Plot changes need author approval first.
6. **Log manuscript edits** in that book's `CHANGELOG.md` so the author can always
   see what changed and why.

## Working style

Agile: one small, finished increment at a time. Ship it, learn, pick the next one.
Don't try to perfect everything at once.

## The writers' room

The nine specialist agents now live at the **workspace root**, in
[`../../.claude/agents/`](../../.claude/agents/) — plot-architect,
drafting-assistant, developmental-editor, line-copy-editor, continuity-keeper,
kid-reader-panel, red-team-critic, culture-researcher, market-pitch-agent. Plus
the `/new-book-outline` skill. Route work to the right specialist; several can
run in parallel on the same draft.

They were promoted out of this book so all three books can use them, which is
what the `book-studio` plan was for. That plan is done — no separate repo is
needed. The plugin packaging is kept at [`../../studio/plugin/`](../../studio/plugin/)
in case the team is ever published for use outside this workspace.

## This book inside the workspace

Spytwins used to be its own repo. Its history is intact here, but it is now a
directory in the `writing` workspace and the old `Spytwins` repo is archived.
See the workspace [`CLAUDE.md`](../../CLAUDE.md) for cross-book rules; where it
disagrees with this file, **this file wins** — it is the canon for this book.
