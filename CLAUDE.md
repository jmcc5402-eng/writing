# Writing Workspace

A multi-book workspace. Each book keeps its own history and its own upstream
repo; shared craft material and process live in `studio/`.

## Layout

```
books/           One directory per book. Each is a git subtree of its own repo.
  mybyb/
  spytwins/
  youngnick/     Young Nicholas — the secret origin of Santa Claus
studio/          Cross-book material: style, process, craft reference
.claude/agents/  Editorial subagents (continuity, line, developmental)
```

## The books

| Directory | Upstream | Status |
|---|---|---|
| `books/mybyb` | `jmcc5402-eng/MYBYB` | Stub — README only |
| `books/spytwins` | `jmcc5402-eng/Spytwins` | Stub — README only |
| `books/youngnick` | `jmcc5402-eng/Youngnick` | Story bible + multi-platform plan drafted |

Each book's own `README.md` is the entry point for that project. For
`youngnick`, `STORY_BIBLE.md` is the source of truth — read it before touching
anything in that book.

## Working on a book

Stay inside the book's directory. A change should belong to exactly one book,
or to `studio/` — not both in the same commit. That keeps subtree pushes clean.

Prefix commit subjects with the book name so history stays legible at the
workspace level:

```
youngnick: lock Nick's surname to Anderson
spytwins: draft chapter 1
studio: add query letter template
```

## Syncing with the upstream book repos

These directories are git subtrees, so each book can still travel back to its
own repo. The remotes are not configured by default — add the one you need:

```sh
git remote add youngnick https://github.com/jmcc5402-eng/Youngnick

# push work in books/youngnick back up to its own repo
git subtree push --prefix=books/youngnick youngnick main

# pull changes made in the standalone repo back into the workspace
git subtree pull --prefix=books/youngnick youngnick main
```

Do not rewrite history under `books/` — it is shared with the upstream repos.

## Conventions

- **Prose is Markdown.** Manuscripts, bibles, outlines, notes — all `.md`.
- **Wrap at 80 columns.** Diffs stay readable and reviewable line by line.
- **Semantic line breaks in drafts.** Break at clause and sentence boundaries
  rather than filling the line; a reworded sentence then shows as a one-line
  diff instead of a reflowed paragraph.
- **Decisions get recorded, not remembered.** When a story question is settled,
  write it into the book's bible and mark it locked. Open questions live in the
  bible too, so nothing gets re-litigated from memory.
- **Don't invent canon.** If a name, date, or detail isn't in the bible or the
  manuscript, it is an open question — flag it, don't quietly fill it in.

## Editorial agents

`.claude/agents/` holds three reviewers, each with a deliberately narrow remit:

- `continuity-checker` — facts against the bible; never touches prose quality
- `line-editor` — sentence-level rhythm and clarity; never changes story
- `developmental-editor` — structure, stakes, character arc; no line notes

Use them one at a time. Their value comes from not blurring together.
