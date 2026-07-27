# Persona set: top-down analysis briefs

Used as one-off workflow agents (not `.claude/agents/` definitions) in the
2026-07-26 pipeline — three per book, in parallel, each writing a full report
to the book's `notes/` before a synthesizer built the snowflake. Reuse these
briefs when a book needs a fresh top-down pass.

## Fiction set (Spytwins, Young Nicholas)

- **Plot & structure** — map the draft beat-by-beat against the book's own
  engine/bible; find summary-instead-of-scene; name what the opening must
  plant for later payoffs; end with a numbered requirements list.
- **Character** — agency, distinguishability, interiority against the
  character canon; who acts vs who is acted upon; end with numbered
  requirements. (For Young Nicholas this analyst also carried the delegated
  audience ruling, with comps and costs.)
- **Continuity** — build the definitive fact sheet the next draft must
  respect: names, props, geography, timeline; verify known errors and sweep
  for new ones.

## Non-fiction set (MYBYB)

- **Argument & structure** — the argument is the plot: what each chapter must
  claim, its evidence, what it hands to the next chapter.
- **Voice & comedy** — extract the voice fingerprint (rhythm, joke
  construction, devices) as a spec a ghostwriter could follow; audit the tone
  rule.
- **Lexicon & brand** — proprietary vocabulary placement; rule on
  canon-vs-draft conflicts citing the concept doc as authority.

Shared frame for all six: read workspace CLAUDE.md + the book's canon + the
primary text + any existing critique (verify it against the page, don't
inherit it); write the full report to `notes/analysis-<role>-<date>.md`;
return a compact numbered summary. Never modify existing files.
