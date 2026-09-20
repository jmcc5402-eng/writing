# The lesson ledger — every author catch, and what now enforces it

The author (2026-09-20): "every bug does two things: fix the bug, and
fix the environment guardrails." `studio/AUTHOR-NOTES.md` keeps the
author's words. This ledger keeps the second half: for each catch,
what was built so it cannot recur — and `lesson-check.py` refuses a
row whose enforcer does not exist. A [FOLD] PR cannot open while an
author note from the last week has no row here (`pr-lint.py`).

## Kinds, and what "enforced by" has to be

| Kind | The catch is | Enforced by (what lesson-check verifies) |
|---|---|---|
| BAN | a phrase or shape a grep can find | a line in `bans.txt` with the ID, and a fixture in `fixtures.tsv` that fires (`bans.py --test`) |
| CHECK | a mechanical property (length, share, count, column) | a tool under `studio/tools/` that contains the ID in a comment, plus a fixture line |
| GATE | a stage that must not be skippable | a line in `accept-gate.sh`, `brief-gate.py`, `card-lint.py` or `pr-lint.py` containing the ID |
| READER | a judgment only a reader can make | a row in `reader-tests.txt` and the named test in the agent file; the gate demands the token in the verdict file |
| CANON | a fact the page must not contradict | a row in the book's `canon/FACTS.md` or `DECISIONS.md` containing the ID, read by `fact-check.py` |
| PROCESS | a step people forget | a hook in `.claude/settings.json` or a skill under `.claude/skills/` containing the ID |
| INSTRUCTION | nothing can enforce it | allowed only with the reason in the Enforced-by column; the instrument-auditor re-asks every four chapters |

## The ledger

| ID | Date | Source (AUTHOR-NOTES row) | The catch, short | Kind | Page fix | Enforced by | Status |
|---|---|---|---|---|---|---|---|
| L001–L007 | 2026-08-22 | scrub bans | the committee-of-the-self shapes, "unhurried," "declined to," "and meant it," "one beat," "never once" | BAN | swept | `bans.txt` L001–L007 + fixtures (were hardcoded in prose-guard.sh; now data) | ENFORCED |
| L008 | 2026-09-10 | #155 | "name in my mouth" | BAN | ch 15 | `bans.txt` L008 | ENFORCED |
| L009–L012 | 2026-09-18 | superfan block read | "in plain words, because," "timed and short and finished," "the first Wednesday in February," Verna's light formula | BAN | ch 21 wrote around them | `bans.txt` L009–L012 | ENFORCED |
| L013 | 2026-09-17 | 213 | "Beer again" — a drink explained aloud | BAN | ch 20 fold | `bans.txt` L013; STANDARDS "Drinks as register" | ENFORCED |
| L014 | 2026-08-28 | line pass watch | "which was its own X" | BAN | — | `bans.txt` L014 | ENFORCED |
| L015 | 2026-09-03/06 | furniture blacklist | casserole, supper, tinfoil | BAN | — | `bans.txt` L015 (chapter-lint's blacklist grep stands beside it) | ENFORCED |
| L016 | 2026-09-20 | 220 | place-stamped speech: "I wanted to say it in this truck" | BAN | ch 21 fold (#178) | `bans.txt` L016 + fixture; STYLE "Nobody says where a thing was said" | ENFORCED — the sweep of nine accepted pages OPEN (the author's call) |
| L017 | 2026-09-20 | 220 | "it's been said where you were" | BAN | ch 21 fold (#178) | `bans.txt` L017 + fixture | ENFORCED |
| L018 | 2026-09-20 | 219 | the touch has a body — the POV lead's physical reaction at every touch | READER | ch 21 fold (#178) | `reader-tests.txt` L018 → panel 1.6.0 "THE TOUCH"; the verdict's TESTS line (gate from ch 22) | ENFORCED from ch 22 |
| L019 | 2026-09-20 | 216 | the reader knows what every named minor character wants | READER | ch 21 fold (#178) | `reader-tests.txt` L019 → panel "THE STANCE"; TESTS line | ENFORCED from ch 22 |
| L020 | 2026-09-20 | 222 | the apart section carries the ache, not only the arithmetic | READER | ch 21 fold (#178) | `reader-tests.txt` L020 → panel "THE ACHE"; TESTS line | ENFORCED from ch 22 |
| L021–L024 | 2026-09-13 | the ch 18 rewrite | POEM, MYSTERY, THE JOKE, APART-WHY | READER | ch 18 v2 | `reader-tests.txt` → panel 1.5.4; TESTS line (were run by habit; now demanded) | ENFORCED from ch 22 |
| L025 | 2026-09-20 | 217, 218 | the storm is on the page as weather — what falls, what it sounds like | INSTRUCTION | ch 21 fold (#178) | taste 17 amended; drafter rule 9; the brief's SCENES for any weather chapter. Why not enforced: one storm a book; a reader test on every chapter would be noise — the instrument-auditor re-asks at the next weather chapter | INSTRUCTION (reason given) |
| L026 | 2026-09-20 | 221 | coach-and-doctor gossip lives in a separate Grapevine room, never on the parents' board | INSTRUCTION | ch 21 fold (#178) | town-ashford "The gossip room"; registry row; B2-D26.5. Why not enforced yet: a FACTS regex for a pairing post on the parents' board would flag ch 12's vaguepost until the author rules whether it moves; the row lands with that ruling | INSTRUCTION (reason given; waits on the author) |
| L027 | 2026-09-19 | 210, 211, 215 | the romance level is chosen before the chapter and checked after | GATE | ch 21 | `targets-check.py` in `accept-gate.sh`; `card-lint.py` Targets line; `pr-lint.py` [CHAPTER]/[FOLD] | ENFORCED |
| L028 | 2026-09-20 | this ledger | every author catch lands as an enforcer, not a note | PROCESS | — | `/lesson` skill; `lesson-check.py` in `guardrails.sh` and in `pr-lint.py` on [FOLD] PRs | ENFORCED |
| L029 | 2026-09-14 | 209, 212 | the $50K figure is directional, not a target; publishing waits on a financial case | INSTRUCTION | — | business rulings, not prose: nothing on a page can contradict them. Why not enforced: the GTM study is the gate on the launch, and it is a document, not a script | INSTRUCTION (reason given) |
| L030 | 2026-09-17 | 214 | the board's why, lightly, every time the habit shows (why Dan reads it; the football hidden in a parent's question) | INSTRUCTION | ch 20 fold | registry row for B2-T08; the keeper reads every board scene against it. Why not enforced: a "why" line has no fixed words to grep; the keeper's page audit carries it | INSTRUCTION (reason given) |
| L031 | 2026-09-20 | 223, 224, 227 | every named character on the page has a stake the reader knows, and some of them are dark (the trainer's ten thousand; Missy's drinking) | GATE | ch 22 on | `brief-gate.py` — from ch 22 a chapter brief must carry a "## STAKES ON THE PAGE" section naming each character's stake; `canon/STAKES.md` is the sheet; FACTS.md rows for the locked facts; the panel's STANCE test asks what each one stands to lose | ENFORCED from ch 22 |
| L032 | 2026-09-20 | 224 | not cartoonish: dark and real-life, in this book and the next | READER | ch 22 on | the panel's STANCE test extended ("does anyone read as a type with nothing to lose"); taste 22; the superfan's block read asks it every four chapters | ENFORCED from ch 22 (stance token) |
| L033 | 2026-09-20 | 225 | one commit, one scope (a book, studio, or agents) with the matching prefix — the rule the showrunner broke on 2026-09-19 | PROCESS | the mixed commit split by hand | `commit-scope.py` as a PreToolUse hook on Bash (`.claude/settings.json`); `hook-check.sh` proves it refuses | ENFORCED |
| L034 | 2026-09-20 | 225 | guardrails are code and need tests — a hook nobody has watched refuse is an instruction | PROCESS | — | `hook-check.sh` (every hook fed a bad input and a good one; in `guardrails.sh`) | ENFORCED |
| L035 | 2026-09-20 | 225 | before a push, know what would catch each change if it were wrong | PROCESS | — | `catch-map.py` + `/what-would-catch-this`; run in `guardrails.sh`. Why not a gate: a gap is a judgment (worth a check or not); the PR body says which | ENFORCED (as a report) |
| L036 | 2026-09-20 | 226 | STAKE × LEVER — every future book plans stakes at the outline, dark where real, and a stake next to the plot's pressure point is a plot line | PROCESS | 1.2: two drops on ch 21 | `studio/craft/stakes.md`; `studio/series-kit/15-cast-stakes.md`; the `/new-book-outline` skill's step 5 (stakes pass); `brief-gate.py` STAKES ON THE PAGE from ch 22; the panel's STANCE test | ENFORCED (outline step + brief gate + reader test) |
| L037 | 2026-09-20 | audit 3 F56 | the accept gate's continuity requirement could be satisfied by any sweep file forever | GATE | — | `accept-gate.sh` requires `chNN-keeper-*.md` from ch 21 | ENFORCED |
| L038 | 2026-09-20 | audit 3 F50 | the talk floor could not fail (dialogue-lint always exited 0) | CHECK | — | `dialogue-lint.py` exits 2 below 8%; the accept gate reads it | ENFORCED |
| L039 | 2026-09-20 | audit 3 F48 | a reader shown the target returns it — three blind reads echoed the card to the digit | PROCESS | — | the panel is launched blind to the Targets line (the prompt, from ch 22); `targets-check.py` prints ECHO? when every field matches | ENFORCED (as a warning) |
| L040 | 2026-09-20 | audit 3 F55 | the hand-kept LRU draw was wrong more often than right | PROCESS | — | `variance-draw.py` computes the LRU card and appends the LOG row | ENFORCED |
| L041 | 2026-09-20 | audit 3 F57 | the card lint guarded SendUserFile while the card rides in the listening file | GATE | — | `listening-file.py` refuses a card that fails `card-lint.py` | ENFORCED |
| L042 | 2026-09-20 | red team (taste read 17–21) | "did not say thank you" — taste 15's check typed onto the page five times | BAN | — (the five stand on accepted pages; forward) | `bans.txt` L042 + the five exhibits as fixtures | ENFORCED |
| L043 | 2026-09-20 | red team (taste read 17–21) | questions ending in a period — on audio nobody sounds like they want the answer | CHECK | — | `chapter-lint.sh` counts them (cap 2 per chapter; the panel reads the count) | ENFORCED (as a count) |
| L044 | 2026-09-20 | red team (taste read 17–21) | everyone in town talks like the leads — a stranger could not tell who is speaking with the names covered; nobody is ever wrong | INSTRUCTION | — | RECENT WATCH for the drafter; every brief's NAMING list gains a VOICES line (who sounds how, one clause each); the superfan's block read asks the names-covered test. Why not enforced: a voice test needs a reader; the block read is the reader | INSTRUCTION (reason given) |
| L045 | 2026-09-20 | 228 | "he" for two men in one paragraph — the reader loses who is who | CHECK | ch 22 fold | `chapter-lint.sh` PRONOUN CROWDING: two men's names and five or more he/his/him in a paragraph is a finding | ENFORCED (as a count) |
| L046 | 2026-09-20 | 229 | Dan's stake — a second time ends him in college coaching — told to the reader, then hinted | CANON | ch 22 fold | `canon/STAKES.md` Dan row; FACTS F-DAN-01; B2-D28.2; every brief's STAKES ON THE PAGE carries it (brief-gate) | ENFORCED |
| L047 | 2026-09-20 | 230 | a minor character returning after an absence is re-introduced in a clause | READER | ch 22 fold | the panel's STANCE test: "would a reader who skipped a week know who this is" (panel 1.6.2) | ENFORCED (stance token) |
| L048 | 2026-09-20 | 231 | the reader is told now whether to like or hate a minor character, and every scene with one says its point | READER | ch 22 fold | the panel's STANCE test: "like or hate now, and why; what the scene was for" (panel 1.6.2); `canon/STAKES.md` "How the reader is meant to read them now" | ENFORCED (stance token) |
| L049 | 2026-09-20 | 231 | the letter is small; the trustees' February agenda is where the stakes are, and the page names its three items | CANON | ch 22 fold | FACTS F-AGD-01 (the three items; a regex against "spring agenda"); B2-D28.4 | ENFORCED |
| L050 | 2026-09-20 | 232 | the flat face — "her face did not do one thing," "her mouth was a line" — the zombie register | BAN | ch 21 Missy pass | `bans.txt` L050 + the two page exhibits as fixtures | ENFORCED |
| L051 | 2026-09-20 | 232 | the top characters carry a PULL (two wants) on the page every time they appear, with feeling | READER | ch 21 Missy pass; ch 22 (Denny's quiet) | `canon/STAKES.md` "The pull"; the panel's STANCE test (1.6.3) asks whether it showed or the character was a zombie; drafter rule 9 | ENFORCED (stance token) |
| L052 | 2026-09-20 | 232 | Missy's pull locked — safe vs playing; Denny's anger; the town she grew up in | CANON | ch 21 Missy pass | `canon/STAKES.md` Missy row (L052); B2-D29.2; the brief's STAKES ON THE PAGE | ENFORCED |
| L053 | 2026-09-20 | 233 | the clock between scenes — where each person went, how long, how the next one knew to come | READER | ch 21 (the bridge) | continuity-keeper 1.4.4: the transitions check is standing on every page audit, not a card; the panel's ENGAGEMENT map already flags a skim at a gap | ENFORCED (the keeper's remit; the gate requires the keeper file) |
