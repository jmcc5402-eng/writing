#!/usr/bin/env bash
# guardrails.sh — run every check in the studio, in one command.
#
#   bash studio/tools/guardrails.sh                 # everything
#   bash studio/tools/guardrails.sh --book books/campus-series
#   bash studio/tools/guardrails.sh --quick         # skip the slow sweeps
#
# Exit 0 = clean. Exit 2 = at least one guardrail is reporting.
#
# This exists so "did we run the checks" is one command and not a memory
# test. Everything here already existed as a script somebody had to
# remember to invoke; that is the condition this repo was in on
# 2026-09-14, with seven working checkers and zero automatic invocation.

set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

BOOK="books/campus-series"
QUICK=0
while (($#)); do
  case "$1" in
    --book) BOOK="$2"; shift 2 ;;
    --quick) QUICK=1; shift ;;
    *) echo "usage: guardrails.sh [--book DIR] [--quick]" >&2; exit 1 ;;
  esac
done

fails=(); passes=()

run() {
  local name="$1"; shift
  local out rc
  out="$("$@" 2>&1)"; rc=$?
  if ((rc == 0)); then
    passes+=("$name")
  else
    fails+=("$name")
    printf '\n\033[1m── %s ─────────────────────────\033[0m\n' "$name"
    printf '%s\n' "$out"
  fi
}

echo "guardrails  ($BOOK)"

# Coverage first. A suite that silently checks nothing is worse than
# no suite: this repo has four manuscript layouts and one convention.
python3 studio/tools/coverage.py "$BOOK"
echo

# --- the machine that makes the prose -------------------------------
run "roster staleness"  python3 studio/tools/roster-staleness.py --quiet
run "thread ids"        python3 studio/tools/id-check.py --audit
run "handoff board"     python3 studio/tools/handoff.py --audit
run "proposals"         python3 studio/tools/proposal-lint.py
run "bans fire"         python3 studio/tools/bans.py --test
run "lesson ledger"     python3 studio/tools/lesson-check.py
run "hooks refuse"      bash studio/tools/hook-check.sh
python3 studio/tools/catch-map.py origin/main 2>/dev/null | tail -1
run "canon facts"       python3 studio/tools/fact-check.py "$BOOK"
run "AI tells"          python3 studio/tools/ai-tells.py "$BOOK"
run "voice dials"       python3 studio/tools/voice-dial.py "$BOOK" --compare

# --- the prose itself ------------------------------------------------
run "story shape"       python3 studio/tools/story-matrix.py "$BOOK"
run "opening sameness"  python3 studio/tools/opening-sameness.py "$BOOK"
# Every conforming book, discovered. No hardcoded subdirectory:
# adding Book 1.3 must not require editing a checker or this file.
for sub in $(python3 studio/tools/coverage.py "$BOOK" --names); do
  [[ "$sub" == "$(basename "$BOOK")" ]] && continue
  run "story shape ($sub)"      python3 studio/tools/story-matrix.py "$BOOK/$sub"
  run "opening sameness ($sub)" python3 studio/tools/opening-sameness.py "$BOOK/$sub"
  if [[ -f "$BOOK/$sub/canon/REGISTERS.md" ]]; then
    run "registers ($sub)"      python3 studio/tools/register-check.py "$BOOK/$sub"
  fi
  if [[ -f "$BOOK/$sub/canon/INGREDIENTS.md" ]]; then
    run "engine 23 ($sub)"      python3 studio/tools/engine-check.py "$BOOK/$sub"
  fi
done

if ((!QUICK)); then
  # Per-chapter mechanical checks across every accepted chapter.
  for dir in "$BOOK/manuscript" "$BOOK/book2/manuscript"; do
    [[ -d "$dir" ]] || continue
    for f in "$dir"/ch*.md; do
      [[ -e "$f" ]] || continue
      hits="$(awk 'length>80 {c++} END{print c+0}' "$f")"
      ((hits)) && { fails+=("80 cols: $f ($hits lines)"); }
      tic="$(awk 'prev ~ /[:—]$/ && $0=="" {c++} {prev=$0} END{print c+0}' "$f")"
      ((tic)) && { fails+=("AI tic: $f ($tic)"); }
    done
  done
  passes+=("columns + AI tics swept")
fi

echo
for p in "${passes[@]}"; do printf '  \033[32m✓\033[0m %s\n' "$p"; done
if ((${#fails[@]})); then
  echo
  for f in "${fails[@]}"; do printf '  \033[31m✗\033[0m %s\n' "$f"; done
  echo
  echo "  Each ✗ above printed its detail. A guardrail that reports is doing"
  echo "  its job; fix the finding, or change the rule and say why."
  exit 2
fi
echo
echo "  all clear"
exit 0
