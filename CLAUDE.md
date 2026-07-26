# Writing Workspace

**These are book projects, not software.** No code, no builds, no tests. The
deliverables are manuscripts, outlines, canon docs, and go-to-market material.

One repo, three books, one shared writers' room.

## Layout

```
books/
  mybyb/       MYBYB — workplace survival guide (non-fiction, rebooting)
  spytwins/    Spytwins — middle-grade mystery series, 40 books planned
  youngnick/   Young Nicholas — the secret origin of Santa Claus
studio/        Cross-book material: style, process, pitch packaging
.claude/
  agents/      The writers' room — nine specialists, usable on any book
  skills/      /new-book-outline
```

This is the only home for this work. The books used to live in separate repos
(`MYBYB`, `Spytwins`, `Youngnick`); their full history was merged in here and
those repos are archived. `books/` holds plain directories — nothing syncs
anywhere, so just edit and commit.

## The books

| Book | What it is | Where it stands |
|---|---|---|
| `books/spytwins` | Middle grade (8–12), twins solving mysteries while their parents are secretly spies | Book 1 complete and edited; Book 2 outline started |
| `books/mybyb` | Adult humor / gift book: surviving your first decade at work | Concept locked, reboot chapters drafting |
| `books/youngnick` | Frontier survival-adventure that's secretly a Santa origin myth | Bible drafted, key decisions being locked |

**Read the book's own docs before touching it.** Each has its own entry point,
and where a book's docs disagree with this file, the book wins:

- `books/spytwins/CLAUDE.md` → canon table, locked names, hard rules
- `books/mybyb/README.md` → `docs/CONCEPT.md` is its north star
- `books/youngnick/README.md` → `STORY_BIBLE.md` is its source of truth

## Hard rules

These hold for every book here.

1. **Canon wins.** If a draft contradicts the book's bible or concept doc, the
   doc is right — flag the conflict, never silently "fix" the canon. When new
   canon gets established, write it into the doc.
2. **Don't invent canon.** If a name, date, or detail isn't in the bible or the
   manuscript, it's an open question. Flag it — `[TK ...]` — don't quietly fill
   it in.
3. **The author's voice is the point.** Assist with structure, continuity,
   critique, and selling. Do not overwrite the author's voice or vision.
4. **Propose structural changes; don't apply them unasked.** Mechanical copy
   fixes can be applied directly. Plot and structural changes need approval
   first.
5. **Every setup pays off.** No solutions by luck or coincidence.
6. **Log manuscript edits** in that book's `CHANGELOG.md` so the author can see
   what changed and why.
7. **Decisions get recorded, not remembered.** When a story question is settled,
   write it into the book's bible and mark it locked. Open questions live there
   too, so nothing gets re-litigated from memory.

## Working on a book

Stay inside the book's directory. A change should belong to exactly one book, or
to `studio/` — not both in the same commit.

Prefix commit subjects with the book name:

```
youngnick: lock Nick's surname to Anderson
spytwins: outline Book 2 through the midpoint
studio: add query letter template
```

## Conventions

- **Prose is Markdown.** Manuscripts, bibles, outlines, notes — all `.md`.
- **Wrap at 80 columns.** Diffs stay readable line by line.
- **Semantic line breaks in drafts.** Break at clause and sentence boundaries
  rather than filling the line; a reworded sentence then shows as a one-line
  diff instead of a reflowed paragraph.
- **`[TK ...]` marks anything unresolved**, `[CHECK: ...]` anything needing
  verification. Both are meant to be greppable:
  `grep -rn '\[TK\|\[CHECK' books/`

See `studio/STYLE.md` for prose defaults and `studio/PIPELINE.md` for the stages
a book moves through.

## The writers' room

Nine specialists in `.claude/agents/`, available to every book:

| Agent | Use it for |
|---|---|
| `plot-architect` | Turning a premise into a chapter-by-chapter outline (Snowflake) |
| `drafting-assistant` | Expanding an **approved** outline into first-draft prose |
| `developmental-editor` | Story-level critique: structure, stakes, arcs, payoffs |
| `line-copy-editor` | Sentence-level polish; mechanical fixes applied, style proposed |
| `continuity-keeper` | Facts against canon — names, ages, timeline, geography |
| `kid-reader-panel` | How 8–12s would actually react (Spytwins, Young Nicholas) |
| `red-team-critic` | The harshest fair read before anything goes out |
| `culture-researcher` | Authentic, non-stereotyped setting detail; fact-checking |
| `market-pitch-agent` | Comps, query letters, synopses, publishing strategy |

Plus the `/new-book-outline` skill.

Route work to the right specialist. Several can run in parallel on the same
draft, but keep the editorial three — developmental, line, continuity —
**separate**. Their value comes from not blurring together: run structure first,
then line, then continuity last, because earlier passes invalidate it.

Every agent reads the target book's own canon before working. They serve three
very different books; none of them should assume an audience the book's docs
haven't stated.

## Working style

Agile: one small, finished increment at a time. Ship it, learn, pick the next
one. Don't try to perfect everything at once.
