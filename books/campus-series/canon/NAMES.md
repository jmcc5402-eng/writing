# Name map — who the page calls whom

STYLE's rule, made machine-readable: *"Names are relationships. Every
major character gets a name map: who calls them what, and the one name
only one person uses."*

`story-matrix.py` reads this to measure how much of a chapter each lead
is present on. Without it the tool auto-derives aliases and gets them
wrong — the first run gave Aisha "Coach" and Dan "Doc," because they
appear in the same scenes and "Doc" is what *he calls her*. A heuristic
that is subtly wrong is worse than a declaration.

**Format:** one row per character. `aliases` is every form the narration
or dialogue uses, comma-separated. `sole` is a name only one person is
allowed to use — spending it in a second mouth is a canon error.

## Book 1.1 — Ashford

| Character | Aliases | Sole use |
|---|---|---|
| Marisol | Marisol, Marisol Pruett, Pruett, Ms. Pruett | — |
| Cal | Cal, Cal Sutter, Sutter, Mr. Sutter | "the tall one from facilities" (Marisol, ch 23) |

## Book 1.2 — Ashford, the following year

| Character | Aliases | Sole use |
|---|---|---|
| Aisha | Aisha, Aisha Cole, Cole, Dr. Cole, Doc, the doctor | "Doc" (Dan); "my winter doctor" (Verna) |
| Dan | Dan, Dan Merritt, Merritt, Coach, the coach | "Dan" to his face (Aisha, spent ch 15) |

## Offstage and supporting

| Character | Aliases | Sole use |
|---|---|---|
| Trey Gault | Trey, Trey Gault, 7, seven, the boy, your quarterback | "Trey" — narration, his parents, and the doctor only; the rail, the board, Tick and the trainer say "7" (B2-D25.6, locked 2026-09-19) |
| Mackenzie Doyle | Mackenzie, Mackenzie Doyle, Doyle | "Mack" (Ty only) |

## Why `sole use` matters

A one-person name is a spend. When it drifts into a second mouth the
book loses a relationship without anyone deciding to — which is the
same shape as every other drift this studio has had. Adding a row here
costs a minute; the alternative is a reader noticing that the name
stopped meaning anything.
