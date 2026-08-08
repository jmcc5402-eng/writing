# The Newsroom Kit

_A self-contained port of the book studio's architecture to a news
blog. Copy this file into the news repo and build from it — it
assumes nothing from the source repo. The pattern: one human (the
EDITOR-IN-CHIEF) supplies editorial judgment through a narrow PR
interface; a roster of versioned agents does the gathering, drafting,
verification, and overnight momentum. Proven in book production; the
newsroom mapping is below._

## Why this ports cleanly

A newsroom already runs on this architecture under older names: the
fact-checker is a continuity gate, the budget meeting is the morning
nudge, the style guide is canon, the assignment editor is the
showrunner, and "publish" is a merge. The port is mostly renaming —
plus two genuinely new forces books don't have: **deadlines that
expire content** and **analytics that score every decision after the
fact.**

## The role mapping

| Studio role | Newsroom role | Notes |
|---|---|---|
| Director / author | **Editor-in-chief** (the human) | rules by PR merge |
| Showrunner (nightly) | **Night editor** | gathers, drafts, preps the morning budget |
| Plot architect | **Assignment desk** | pitches: angle, why-now, sources |
| Drafting assistant | **Staff writer** | drafts ONLY from an approved pitch + voice sample |
| Continuity keeper | **Fact-checker** | the load-bearing gate — see Source Manifest |
| Developmental editor | **Story editor** | structure, angle, buried ledes |
| Line/copy editor | **Copy desk** | mechanical applied, style proposed |
| Red-team critic | **The lawyer read** | libel, fairness, "how will this be attacked" |
| Reader panel | **Audience panel** | 2–3 named reader personas, pre-publish |
| Culture researcher | **Reporter/researcher** | web access; gathers, never asserts |
| Market/GTM agents | **Growth desk** | SEO, headlines, distribution |
| Junior critic | **Public editor** | periodic outside read of the whole site |

## Canon → the editorial stack (write these first)

1. **CHARTER.md** (= VISION.md): the beats you cover, the POV, what
   you never cover, who the reader is, cadence targets. The night
   editor re-reads it every shift; one edited sentence re-aims the
   whole newsroom by morning.
2. **STANDARDS.md** (= the bible): the WALLS — no unsourced factual
   claims; no fabricated quotes, ever; attribution format; AI
   disclosure policy; corrections policy; libel/fairness rules.
   Walls never bend; style items below them are warnings.
3. **STYLEBOOK.md**: voice, banned phrases, the AI-tics sweep
   (mechanical linters — anything greppable gets grepped).
4. **Beat bibles** (one per coverage area): running context, key
   players, prior coverage, OWED follow-ups (every "we'll be
   watching" is a debt with an ID, like a plot thread).
5. **CORRECTIONS.md**: public, append-only. Trust is the newsroom's
   canon; this file is its changelog.

## The Source Manifest (the port's keystone)

The book studio's fact manifest becomes the newsroom's core
discipline: **every story PR carries a source manifest** — each
factual claim in the draft mapped to its source (link, quote, date
accessed), classified VERIFIED / SINGLE-SOURCE / UNVERIFIED /
DISPUTED. The writer may assert only what the manifest holds;
anything else renders as [TK]. The fact-check gate verifies the
mapping claim by claim, with numbered findings. **No manifest, no
merge.** This one rule is most of the difference between an AI blog
and an AI blog people trust.

## The instrument battery, translated

- **Mechanical linters** (every draft): style guide, banned phrases,
  link checker, attribution format, dangling-punctuation sweep.
- **Fact-check gate** (every draft): the manifest audit above.
- **Round-trip re-derivation** (features/explainers): a BLIND agent
  reads only the finished article and reconstructs "what facts does
  this claim, and what does it want me to believe?" — diffed against
  the manifest and the pitch. The diff is **spin detection**: drift
  between what you sourced and what you implied, invisible to any
  forward reader.
- **Audience panel** (features): where readers bounce, what they
  misread, what they'd share.
- **The lawyer read** (anything naming people/companies): strongest
  adversarial reading before the editor sees it.
- **Headline tournament** (every story): 4–6 candidates scored
  against the charter (accuracy first, then pull); the draft's own
  headline must WIN, not incumbent through. Angle tournaments for
  big stories: fresh angles compete with the pitch.

## Two ladders (news moves at two speeds)

- **TIMELY lane** (news pegs): pitch → source manifest → draft →
  fact-check + linters → story PR. Hours, not days. Rungs collapse;
  gates never do.
- **EVERGREEN lane** (explainers, features): the full ladder — pitch
  → angle memo → outline with manifest → draft → full battery
  (including round-trip and audience panel) → story PR.
- **The expiry rule** (inverse of the book studio's staleness rule):
  a TIMELY story PR not merged within its stated shelf life
  auto-expires — the night editor closes it and logs it. News dies;
  don't let corpses queue.

## Governance: the PR taxonomy

`[beat][TYPE]` titles; one decision per PR; the body quotes the
draft's actual lines; recommended option applied in the diff.

| Type | Merging means |
|---|---|
| PITCH | approve the angle (cheap, plotting-mode — batch 3–5/day) |
| STORY | **publish** — merge deploys to the site via CI |
| CORRECTION | fix + public corrections entry, one motion |
| STANDARDS / CHARTER | change the rules or the aim |
| BEAT | open/close a coverage area |
| AGENTS | change the newsroom itself |
| MINOR | the trust lane — typos, links, tags, formatting |

Rules carried over verbatim: if it's the editor's action, it's a PR;
decisions parked in notes are queue debt; budget 5–7 open PRs; the
MINOR lane auto-merges on the night shift after double verification,
reported in a daily digest with "revert #N"; one revert suspends the
lane a day. **The queue-mix rule:** always offer quick approvals
(pitches, headlines) alongside any deep read (features) — the editor
clears pitches from a phone in five minutes.

## The night editor's shift (the heart of it)

Fires nightly into the standing session. In order:

1. Process merges since last shift (merged STORY = published; verify
   deploy; log analytics baseline).
2. MINOR lane: verify + merge; queue the digest lines.
3. **Scan**: each charter beat — what moved in the world overnight
   (web research), what OWED follow-ups came due, what analytics say
   about yesterday's stories.
4. **Pitch**: build the ranked story list; write the why-now line
   for each.
5. **Produce**: for the top 1–3 pitches, run the full lane overnight
   — research, source manifest, draft, fact-check, lawyer read,
   headline tournament — so the morning queue holds STORY PRs that
   are one merge from live, not homework.
6. **The morning budget** (the nudge): WHAT'S READY TO PUBLISH (each
   story: headline + one line + shelf life) / MERGED FOR YOU /
   PITCHES AWAITING / THE ONE THING / at most one steering question.
   Push notification with the counts.

## The feedback loop books never had

Analytics are ground truth. The night editor logs performance per
story (traffic, read-through, shares) into the beat bibles, and the
assignment desk ranks future pitches partly on it. Every agent
version bump cites evidence, and here evidence includes numbers.
Watch for the trap the charter must guard: metrics optimize toward
clickbait — accuracy and charter-fit outrank performance in every
tournament's scoring, by written rule.

## Porting checklist

1. Write CHARTER.md and STANDARDS.md (the walls) — one evening, the
   editor's own words.
2. Adopt the PR taxonomy + template verbatim; wire merge-to-deploy
   CI so STORY merges publish.
3. Stand up the roster as versioned agent files (ROSTER + evidence
   CHANGELOG + variance decks — keep the card system; a newsroom
   calcifies faster than a book).
4. Build the Source Manifest rule into every drafting brief from day
   one — retrofitting trust is much harder.
5. Stand up the night editor on a cron into a standing session (not
   fresh sessions — they lack the authenticated toolchain), with the
   morning budget + push notification.
6. Start with TWO beats, not ten. Ship daily within the first week;
   let the charter grow beats the way the studio grew books.
7. Hand the editor their three levers: CHARTER.md, the PR queue, and
   one steering question a day.
