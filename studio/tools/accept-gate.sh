#!/usr/bin/env bash
# accept-gate.sh — a chapter may not be marked ACCEPTED without evidence.
#
#   studio/tools/accept-gate.sh books/campus-series/book2 14
#
# The instruments in .claude/agents/ are excellent and entirely optional:
# nothing has ever stopped a thread from skipping one. On 2026-09-14 a
# thread skipped the superfan because it forgot. On 2026-09-15 two heat
# passes skipped the continuity read, and five contradictions reached
# main.
#
# This turns "run the panel, run the superfan, run the keeper" from an
# instruction into a gate on a state transition. The evidence is a
# verdict FILE. No file, no acceptance.
#
# Exit 0 = every required verdict is on disk and the lints pass.
# Exit 2 = the gate holds, and says exactly what is missing.

set -uo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

BOOK="${1:?usage: accept-gate.sh <book-dir> <chapter-number> [--retrofit]}"
CH_RAW="${2:?usage: accept-gate.sh <book-dir> <chapter-number> [--retrofit]}"
MODE="${3:-}"
CH="$(printf '%02d' "$((10#${CH_RAW#ch}))")"

BOOKDIR="$REPO/${BOOK#"$REPO/"}"
CHAP="$BOOKDIR/manuscript/ch$CH.md"
NOTES="$BOOKDIR/notes"

missing=(); soft=()

[[ -f "$CHAP" ]] || { echo "accept-gate: no such chapter: $CHAP" >&2; exit 2; }

have() { compgen -G "$NOTES/$1" >/dev/null 2>&1; }

# ---- REQUIRED EVIDENCE ------------------------------------------------
# Each line is an instrument whose verdict must exist as a file.
# Add to this list the day an instrument becomes load-bearing; that is
# the ratchet.

have "ch${CH}-panel-*.md"     || missing+=("romance-reader-panel  → notes/ch${CH}-panel-<date>.md")
have "ch${CH}*scoreboard*.md" || soft+=("no scoreboard — fine for a single-drafter chapter, required for a competition")

# The superfan reads at wave/gate boundaries, not every chapter. Required
# whenever a chapter is the last of its wave, or on any packaging change.
if [[ "${SUPERFAN_REQUIRED:-0}" == "1" ]]; then
  compgen -G "$NOTES/*superfan*.md" >/dev/null 2>&1 \
    || missing+=("superfan-reviewer → notes/*superfan*.md  (SUPERFAN_REQUIRED=1 is set for this chapter)")
fi

# A chapter that is ALREADY accepted and is being edited again is a
# retrofit: the most dangerous class, because whole-book knowledge writes
# lines the page cannot support. It owes a continuity read, always.
if [[ "$MODE" == "--retrofit" ]] || head -12 "$CHAP" | grep -qi "ACCEPTED"; then
  compgen -G "$NOTES/*continuity*.md" >/dev/null 2>&1 \
    || compgen -G "$NOTES/*sweep*.md" >/dev/null 2>&1 \
    || missing+=("continuity-keeper → notes/*continuity*.md  (REQUIRED: this chapter is folded prose)")
fi

# Every agent run draws a variance card and logs it.
if ! grep -q "$(date +%Y-%m-%d)" "$REPO/studio/agents/variance/LOG.md" 2>/dev/null; then
  soft+=("no variance draw logged today in studio/agents/variance/LOG.md")
fi

# Hard rule 6: manuscript edits are logged in the book's CHANGELOG.
# The chapter's OWN entry (a heading naming "ch NN"), not a line dated
# today — a quiet day used to block the gate (BACKLOG F42, fixed
# 2026-09-20 on the showrunner's board).
if [[ -f "$BOOKDIR/CHANGELOG.md" ]]; then
  grep -qiE "^## .*\bch 0?$((10#$CH))\b" "$BOOKDIR/CHANGELOG.md" 2>/dev/null \
    || missing+=("CHANGELOG entry for ch $((10#$CH)) (hard rule 6) → ${BOOK}/CHANGELOG.md")
fi

# The two scores a chapter (author, 2026-09-19: "I'd like a skill that
# does that for each chapter"): /chapter-score writes notes/scores/
# chNN-score.md — the romance level and each lead's development, with
# evidence. Required from ch 21; ch 1–20 are backfilled.
SCORES_FROM=21
if (( 10#$CH >= SCORES_FROM )); then
  have "scores/ch${CH}-score.md" || missing+=("chapter score → notes/scores/ch${CH}-score.md  (/chapter-score: the romance level and each lead's development, with evidence)")
fi

# The definition of done, set on the card before the draft (author,
# 2026-09-17): targets-check.py compares the card's Targets line with the
# panel's ACTUALS line; the romance level two or more under target holds
# the chapter. From ch 21 — ch 1–20 were accepted before the rule.
TARGETS_FROM=21
if (( 10#$CH >= TARGETS_FROM )) && [[ -f "$REPO/studio/tools/targets-check.py" ]]; then
  tc="$(python3 "$REPO/studio/tools/targets-check.py" "$BOOKDIR" "$CH" --record 2>&1)" \
    || missing+=("targets-check: $(grep -m1 -E 'FAIL|HOLD' <<<"$tc" | sed 's/^ *//')")
  printf '%s\n' "$tc" | sed 's/^/  /'
fi

# The reader tests (studio/lessons/reader-tests.txt): each row names a
# reader, a test, and a token that must appear on a TESTS: line in the
# chapter's verdict file. Adding a row there makes this gate demand the
# test the same day (the lesson loop, L028; from ch 22).
READER_TESTS_FROM=22
if (( 10#$CH >= READER_TESTS_FROM )) && [[ -f "$REPO/studio/lessons/reader-tests.txt" ]]; then
  while IFS=$'\t' read -r lid agent test glob token; do
    [[ "$lid" == L* ]] || continue
    g="${glob//\{CH\}/$CH}"
    if compgen -G "$NOTES/$g" >/dev/null 2>&1; then
      if ! grep -hi "^TESTS:" $NOTES/$g 2>/dev/null | grep -qi "$token"; then
        missing+=("$agent → the verdict's TESTS: line must carry '$token' ($test, $lid) — the reader ran the test or the chapter waits")
      fi
    fi
  done < "$REPO/studio/lessons/reader-tests.txt"
fi

# ---- MECHANICAL CHECKS ------------------------------------------------
lint_out=""
if [[ -x "$REPO/studio/tools/chapter-lint.sh" ]]; then
  lint_out="$(bash "$REPO/studio/tools/chapter-lint.sh" "$CHAP" 2>&1)" || true
  if grep -qiE "^(FAIL|ERROR)" <<<"$lint_out"; then
    missing+=("chapter-lint reports a failure — run it and read the output")
  fi
fi
if [[ -f "$REPO/studio/tools/dialogue-lint.py" ]]; then
  dlg="$(python3 "$REPO/studio/tools/dialogue-lint.py" "$CHAP" 2>&1)" || \
    missing+=("dialogue-lint below floor: $(head -2 <<<"$dlg")")
fi

# ---- VERDICT ----------------------------------------------------------
echo "accept-gate: ${BOOK}/ch${CH}"
if ((${#soft[@]})); then
  printf '  note  %s\n' "${soft[@]}"
fi
if ((${#missing[@]})); then
  echo "  BLOCKED — evidence missing:"
  printf '    ✗ %s\n' "${missing[@]}"
  echo
  echo "  A chapter is not accepted because a thread believes it is good."
  echo "  It is accepted when the readers have run and left their verdicts"
  echo "  on disk. Run the missing instrument, then run this again."
  exit 2
fi
echo "  PASS — every required verdict is on disk; lints clean."
exit 0
