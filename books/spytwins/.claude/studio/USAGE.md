# Using the Writers' Room

## 1. Wire it into a book project (durable)

In the book's repo, create or edit `.claude/settings.json` and commit it:

```json
{
  "extraKnownMarketplaces": {
    "book-studio": {
      "source": { "source": "github", "repo": "jmcc5402-eng/book-studio" }
    }
  },
  "enabledPlugins": {
    "writers-room@book-studio": true
  }
}
```

The first time you open the project you'll be asked to trust the workspace; after
that the marketplace registers and the team auto-loads every session — including
on Claude Code for web, where containers are ephemeral and only committed files
persist. Update the team by pushing to `book-studio`; projects pick up changes on
the next session.

## 2. Drive the team

You rarely call agents by hand — describe the task and Claude routes it to the
right specialist. But you can also request one explicitly:

- *"Have the **plot-architect** outline Book 2."*
- *"Run the **developmental-editor** and **kid-reader-panel** on chapters 1–3."*
- *"**continuity-keeper**: check this draft against the series bible."*
- *"**red-team-critic**: why would an agent reject this query letter?"*
- *"**culture-researcher**: get me authentic Tokyo details for the festival scene."*
- *"**market-pitch-agent**: draft a query letter and find three comps."*
- `/writers-room:new-book-outline "Book 3 — the Venice canals mystery"`

Several can run in parallel — e.g. developmental + continuity + kid-reader on the
same chapter — and Claude synthesizes their reports.

## 3. What the team expects from a project

The agents look for a story bible to respect. They work best when the project has:
- a concept / premise doc,
- a series bible or "story engine,"
- character canon,
- and a `plots/` (or similar) folder for outlines.

No bible yet? The **plot-architect** and **new-book-outline** skill will help you
build one first.

## 4. Keeping it AI-native *and* yours

- **Voice is the moat.** The more drafting is AI-assisted, the harder the editing
  agents (and you) should pull prose back toward a distinct human voice. Keep a
  voice sample handy for the drafting-assistant.
- **Disclosure.** Publishers, platforms, and contests increasingly ask about AI
  involvement. Using this team as your writers' room while *you* author is very
  different from "AI wrote it" — be ready to describe your process honestly.
