# Studio

Everything that belongs to the writing, not to any one book.

If a note only makes sense for a single project, it lives in that book's
directory. If it would still be true on the next book, it lives here.

## What's here

- **[STYLE.md](STYLE.md)** — prose and formatting conventions across all books
- **[PIPELINE.md](PIPELINE.md)** — the stages a book moves through, and what
  "done" means at each one
- **[plugin/](plugin/)** — packaging to publish the writers' room as a
  distributable Claude Code plugin

## About `plugin/`

These manifests came from Spytwins, where the plan was to extract the agents
into a standalone `book-studio` repo so other books could use them. That's no
longer needed — the agents now live in `.claude/agents/` at the workspace root
and already work on all three books.

The packaging is kept for one remaining case: publishing the writers' room for
use *outside* this workspace. See [plugin/USAGE.md](plugin/USAGE.md). Until
then, nothing here needs maintaining.

## What belongs here later

- Query letters, synopses, and pitch material
- Comp title research
- Agent and publisher submission tracking
- Craft reference worth keeping — structure notes, revision checklists
