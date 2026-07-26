# book-studio

A reusable, **AI-native writers' room** — a standing team of specialist agents and
skills for **writing, editing, critiquing, and selling** books. Built once, used
across every book project.

This repo is a **Claude Code plugin marketplace**. It contains one plugin,
**`writers-room`**, which you install into any book project (Spytwins, and
whatever you write next). The agents read a project's story bible when one is
present, so the same team adapts to each book.

## The team (agents)

| Agent | Job | Stage |
|-------|-----|-------|
| **plot-architect** | Turns a premise/vibe into a chapter outline (Snowflake + beat spine) | Write |
| **drafting-assistant** | Expands an approved outline into first-draft prose *in your voice* | Write |
| **developmental-editor** | Big-picture story feedback: pacing, stakes, structure, plot holes | Edit |
| **line-copy-editor** | Sentence-level polish; applies safe mechanical fixes, proposes stylistic ones | Edit |
| **continuity-keeper** | Guards canon — names, traits, timeline, facts — across chapters and books | Edit |
| **kid-reader-panel** | Simulates target-age readers: where they'd be bored, confused, or delighted | Critique |
| **red-team-critic** | The toughest fair read — why an agent/reviewer might pass, and the top fix | Critique |
| **culture-researcher** | Authentic setting/culture detail + fact-checking (web access) | Research |
| **market-pitch-agent** | Comps, query letters, synopsis, positioning, publish strategy (web access) | Sell |

## The skills

- **`/writers-room:new-book-outline`** — outline a new book from a premise using the
  project's story engine.

## Install into a book project

**Option A — one-time, per machine/session:**
```
/plugin marketplace add jmcc5402-eng/book-studio
/plugin install writers-room@book-studio
```

**Option B — durable, committed to a project (recommended, and required for
Claude Code on the web):** add this to the project's `.claude/settings.json` and
commit it. See [`USAGE.md`](USAGE.md) for the exact snippet.

## Design principle

The author owns the concept, characters, and voice. This team does the heavy
lifting — structure, consistency, critique, and the business of selling — while
keeping the author as the author. See `USAGE.md` for how to drive the team.
