#!/usr/bin/env bash
# hook-check.sh — guardrails are code and need tests too.
#
#   bash studio/tools/hook-check.sh
#
# Feeds every hook in .claude/settings.json a known-bad input and asserts
# it refuses (exit 2), then a known-good input and asserts it passes.
# A hook that lets the bad input through is reported as DEAD. Runs in
# guardrails.sh. (The doc's /hook-check; L034.)
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
export CLAUDE_PROJECT_DIR="$ROOT"
export COMMIT_SCOPE_NO_INDEX=1      # the commit-scope cases judge the command line, not whatever is staged
T="$(mktemp -d)"; trap 'rm -rf "$T"' EXIT
: > "$T/n"; : > "$T/fails"          # counters survive the pipe subshells

expect() {  # expect <want-rc> <name> <command…>  (payload on stdin)
  local want="$1" name="$2"; shift 2
  local out rc
  out="$("$@" 2>&1)"; rc=$?
  echo x >> "$T/n"
  if [[ "$rc" == "$want" ]]; then
    printf '  ok    %-58s (exit %s)\n' "$name" "$rc"
  else
    printf '  DEAD  %-58s (exit %s, wanted %s)\n' "$name" "$rc" "$want"
    printf '%s\n' "$out" | sed 's/^/        /' | head -6
    echo x >> "$T/fails"
  fi
}
payload_file() { printf '{"tool_input":{"file_path":"%s"}}' "$1"; }

echo "hook-check  ($ROOT)"

# --- prose-guard (PostToolUse Edit|Write) ------------------------------
mkdir -p "$T/manuscript"
printf 'He said it in this room and meant it.\n' > "$T/manuscript/ch98.md"
payload_file "$T/manuscript/ch98.md" | expect 2 "prose-guard refuses a banned idiom" bash "$ROOT/studio/tools/prose-guard.sh"
printf 'She put the cup down and went in.\n' > "$T/manuscript/ch97.md"
payload_file "$T/manuscript/ch97.md" | expect 0 "prose-guard passes clean prose" bash "$ROOT/studio/tools/prose-guard.sh"
printf 'It was late. The thing on the table was this:\n\nA note.\n' > "$T/manuscript/ch96.md"
payload_file "$T/manuscript/ch96.md" | expect 2 "prose-guard refuses a paragraph ending on a colon" bash "$ROOT/studio/tools/prose-guard.sh"

# --- pr-lint (PreToolUse create/update PR) ----------------------------
printf '{"tool_input":{"title":"[campus][CHAPTER] x","body":"No ask section here. Just words."}}' \
  | expect 2 "pr-lint refuses a body with no Ask" python3 "$ROOT/studio/tools/pr-lint.py"
python3 - "$T" <<'PY'
import json,sys
long=" ".join(["word"]*40)+"."
open(sys.argv[1]+"/pr-long.json","w").write(json.dumps({"tool_input":{"title":"[campus][FOLD] x","body":"## Ask\n\nMerge it.\n\n"+long+"\n\nplan → actual 7 → 8"}}))
open(sys.argv[1]+"/pr-ok.json","w").write(json.dumps({"tool_input":{"title":"[campus][FOLD] x","body":"## Ask\n\nMerge it.\n\nA short body.\n\nplan → actual 7 → 8"}}))
open(sys.argv[1]+"/pr-norow.json","w").write(json.dumps({"tool_input":{"title":"[campus][CHAPTER] x","body":"## Ask\n\nRead it.\n\nNo targets row here."}}))
PY
expect 2 "pr-lint refuses a 40-word sentence" python3 "$ROOT/studio/tools/pr-lint.py" < "$T/pr-long.json"
expect 2 "pr-lint refuses a [CHAPTER] PR with no matrix row" python3 "$ROOT/studio/tools/pr-lint.py" < "$T/pr-norow.json"
expect 0 "pr-lint passes a plain [FOLD] body with plan → actual" python3 "$ROOT/studio/tools/pr-lint.py" < "$T/pr-ok.json"

# --- card-lint (PreToolUse SendUserFile) -------------------------------
mkdir -p "$T/notes/cards"
python3 - "$T" <<'PY'
import sys
body=" ".join(["word"]*400)
open(sys.argv[1]+"/notes/cards/ch99-card.md","w").write("# Chapter 99 — X\n\nAisha, Monday.\n\n**The plot.**\n\n"+body+"\n\n**Your calls.**\n\n1. A or B.\n")
PY
printf '{"tool_input":{"files":["%s/notes/cards/ch99-card.md"]}}' "$T" | expect 2 "card-lint refuses a 400-word card" python3 "$ROOT/studio/tools/card-lint.py"

# --- brief-gate (PreToolUse Agent) -------------------------------------
mkdir -p "$T/plots"
printf '# Brief — ch 99\n\nNo addendum here.\n' > "$T/plots/brief-ch99.md"
printf '{"tool_input":{"subagent_type":"drafting-assistant","prompt":"Draft from %s/plots/brief-ch99.md"}}' "$T" \
  | expect 2 "brief-gate refuses a drafter on an unaudited brief" python3 "$ROOT/studio/tools/brief-gate.py"
printf '{"tool_input":{"subagent_type":"continuity-keeper","prompt":"Audit %s/plots/brief-ch99.md"}}' "$T" \
  | expect 0 "brief-gate lets a keeper read an unaudited brief" python3 "$ROOT/studio/tools/brief-gate.py"

python3 - "$T" <<'PY'
import sys
T=sys.argv[1]
verdict="## AUDIT ADDENDUM\n\n"+" ".join(["word"]*160)+"\n\n## VERDICT: PASS\n"
open(T+"/plots/brief-ch97.md","w").write("# Brief — ch 97\n\n## THE SCENES\n\n1. **A**\n2. **B**\n\n## STAKES ON THE PAGE\n\nx\n\n"+verdict)
open(T+"/plots/brief-ch96.md","w").write("# Brief — ch 96\n\n## THE SCENES\n\n1. **A**\n2. **B**\n\n## STAKES ON THE PAGE\n\nx\n\n## THE AUTHOR'S READ\n\n| Scene | MORE | WHO | CONFUSING | NOSE | POINT | SENSES |\n|---|---|---|---|---|---|---|\n| 1. A | a | b | c | d | e | f |\n| 2. B | a | b | c | d | e | f |\n\n"+verdict)
PY
printf '{"tool_input":{"subagent_type":"drafting-assistant","prompt":"Draft from %s/plots/brief-ch97.md"}}' "$T" \
  | expect 2 "brief-gate refuses a ch 23+ brief with no THE AUTHOR'S READ" python3 "$ROOT/studio/tools/brief-gate.py"
printf '{"tool_input":{"subagent_type":"drafting-assistant","prompt":"Draft from %s/plots/brief-ch96.md"}}' "$T" \
  | expect 0 "brief-gate passes a brief with one AUTHOR'S READ row per scene" python3 "$ROOT/studio/tools/brief-gate.py"

# --- commit-scope (PreToolUse Bash) ------------------------------------
printf '{"tool_input":{"command":"git add books/campus-series/book2/STATE.md studio/STYLE.md && git commit -m \\"campus: x\\""}}' \
  | expect 2 "commit-scope refuses a campus+studio commit" python3 "$ROOT/studio/tools/commit-scope.py"
printf '{"tool_input":{"command":"git add studio/STYLE.md && git commit -m \\"campus: x\\""}}' \
  | expect 2 "commit-scope refuses a wrong prefix" python3 "$ROOT/studio/tools/commit-scope.py"
printf '{"tool_input":{"command":"git add studio/STYLE.md && git commit -m \\"studio: x\\""}}' \
  | expect 0 "commit-scope passes one scope, right prefix" python3 "$ROOT/studio/tools/commit-scope.py"
printf '{"tool_input":{"command":"ls -la"}}' | expect 0 "commit-scope ignores a non-commit command" python3 "$ROOT/studio/tools/commit-scope.py"
printf '%s' '{"tool_input":{"command":"git add books/campus-series/book2/STATE.md && git commit -m \"campus: a\" && git add studio/STYLE.md && git commit -m \"studio: b\" && git add .claude/skills/lesson/SKILL.md && git commit -m \"agents: c\""}}' \
  | expect 0 "commit-scope passes three scoped commits on one line" python3 "$ROOT/studio/tools/commit-scope.py"
printf '%s' '{"tool_input":{"command":"git add .claude/skills/lesson/SKILL.md && git commit -m \"studio: c\""}}' \
  | expect 2 "commit-scope knows .claude/skills is the agents scope" python3 "$ROOT/studio/tools/commit-scope.py"
printf '%s' '{"tool_input":{"command":"python3 - <<EOF\nprint(\"git add a && git commit -m x\")\nEOF\n"}}' \
  | expect 0 "commit-scope ignores a git commit quoted inside a heredoc" python3 "$ROOT/studio/tools/commit-scope.py"

# --- thread-scope (PreToolUse Edit|Write|MultiEdit, Bash, Agent) — L068 -
# STUDIO_THREAD_SCOPE forces the scope so the cases hold on any branch.
TSP="$ROOT/studio/tools/thread-scope.py"
printf '{"tool_name":"Edit","tool_input":{"file_path":"%s/books/campus-series/book2/manuscript/ch05.md"}}' "$ROOT" \
  | STUDIO_THREAD_SCOPE=environment expect 2 "thread-scope refuses a manuscript edit on an environment branch" python3 "$TSP"
printf '{"tool_name":"Edit","tool_input":{"file_path":"%s/books/campus-series/book2/canon/REGISTERS.md"}}' "$ROOT" \
  | STUDIO_THREAD_SCOPE=environment expect 0 "thread-scope lets an environment branch edit canon" python3 "$TSP"
printf '{"tool_name":"Write","tool_input":{"file_path":"%s/studio/STYLE.md"}}' "$ROOT" \
  | STUDIO_THREAD_SCOPE=environment expect 0 "thread-scope lets an environment branch edit studio" python3 "$TSP"
printf '{"tool_name":"Edit","tool_input":{"file_path":"%s/books/campus-series/book2/manuscript/ch05.md"}}' "$ROOT" \
  | STUDIO_THREAD_SCOPE=story expect 0 "thread-scope leaves a story branch alone" python3 "$TSP"
printf '{"tool_name":"Bash","tool_input":{"command":"git add -A && git commit -m \\"studio: x\\""}}' \
  | STUDIO_THREAD_SCOPE=environment expect 2 "thread-scope refuses git add -A on an environment branch" python3 "$TSP"
printf '{"tool_name":"Bash","tool_input":{"command":"sed -i s/a/b/ books/campus-series/book2/manuscript/ch05.md"}}' \
  | STUDIO_THREAD_SCOPE=environment expect 2 "thread-scope refuses sed -i on a manuscript" python3 "$TSP"
printf '{"tool_name":"Bash","tool_input":{"command":"cp books/campus-series/book2/manuscript/ch05.md /tmp/scratch/"}}' \
  | STUDIO_THREAD_SCOPE=environment expect 0 "thread-scope lets a manuscript be copied OUT (reading is the job)" python3 "$TSP"
printf '{"tool_name":"Bash","tool_input":{"command":"cp /tmp/x.md books/campus-series/book2/manuscript/ch05.md"}}' \
  | STUDIO_THREAD_SCOPE=environment expect 2 "thread-scope refuses a copy INTO a manuscript" python3 "$TSP"
printf '{"tool_name":"Bash","tool_input":{"command":"python3 studio/tools/ai-tells.py books/campus-series/book2/manuscript/ch05.md > /tmp/out.txt"}}' \
  | STUDIO_THREAD_SCOPE=environment expect 0 "thread-scope lets a tool read a manuscript and write elsewhere" python3 "$TSP"
printf '%s' '{"tool_name":"Bash","tool_input":{"command":"cat <<EOF > books/campus-series/book2/manuscript/ch05.md\nx\nEOF\n"}}' \
  | STUDIO_THREAD_SCOPE=environment expect 2 "thread-scope sees a heredoc redirected onto a manuscript" python3 "$TSP"
printf '{"tool_name":"Bash","tool_input":{"command":"git add studio/STYLE.md && git commit -m \\"studio: x\\""}}' \
  | STUDIO_THREAD_SCOPE=environment expect 0 "thread-scope passes a named studio commit" python3 "$TSP"
printf '{"tool_name":"Agent","tool_input":{"subagent_type":"drafting-assistant","prompt":"draft ch 25"}}' \
  | STUDIO_THREAD_SCOPE=environment expect 2 "thread-scope refuses a drafter on an environment branch" python3 "$TSP"
printf '{"tool_name":"Agent","tool_input":{"subagent_type":"continuity-keeper","prompt":"read ch 25"}}' \
  | STUDIO_THREAD_SCOPE=environment expect 0 "thread-scope lets an environment branch launch a keeper" python3 "$TSP"

# --- id-check (PreToolUse Bash, on git push) — L069 ----------------------
printf '{"tool_name":"Bash","tool_input":{"command":"git push -u origin x"}}' \
  | expect 0 "id-check passes a push when no ID collides with another ref" python3 "$ROOT/studio/tools/id-check.py"
printf '{"tool_name":"Bash","tool_input":{"command":"ls -la"}}' \
  | expect 0 "id-check ignores a command that is not a push" python3 "$ROOT/studio/tools/id-check.py"

# --- the bans' own fixtures --------------------------------------------
expect 0 "bans.py --test: every ban fires on its fixture" python3 "$ROOT/studio/tools/bans.py" --test

echo
n="$(wc -l < "$T/n")"; fails="$(wc -l < "$T/fails")"
if ((fails)); then
  echo "hook-check: $fails of $n DEAD — a hook that lets the bad input through is an instruction"
  exit 2
fi
echo "hook-check: $n of $n refuse what they should and pass what they should"
exit 0
