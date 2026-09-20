#!/usr/bin/env bash
# prose-guard.sh — the PostToolUse guard for manuscript edits.
#
# Reads the hook's JSON on stdin, finds the edited file, and if it is a
# manuscript chapter, runs the mechanical checks that until now depended
# on an agent remembering to run them.
#
# Exit 0 = silent pass. Exit 2 = findings, fed back to the agent.
#
# Why this exists: on 2026-09-15 a drafting run reported "longest added
# sentence 27 words" and had written a 43-word one, because it had no
# shell and self-counted. The lint existed. Nothing invoked it.

set -uo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

payload="$(cat)"
file="$(printf '%s' "$payload" | grep -o '"file_path"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 | sed 's/.*"file_path"[[:space:]]*:[[:space:]]*"//; s/"$//')"

[[ -z "${file:-}" ]] && exit 0
case "$file" in
  */manuscript/ch*.md) ;;
  *) exit 0 ;;
esac
[[ -f "$file" ]] || exit 0

findings=()

# --- 1. Column width (STYLE: wrap at 80) -------------------------------
while IFS= read -r hit; do
  findings+=("80-col: $hit")
done < <(awk 'length>80 {print FILENAME":"FNR" ("length" cols)"}' "$file")

# --- 2. AI drafting tic: paragraph ending in a colon or dash ----------
while IFS= read -r hit; do
  findings+=("AI-tic (paragraph ends on : or —): $hit")
done < <(awk 'prev ~ /[:—]$/ && $0=="" {print FILENAME":"NR-1": "prev} {prev=$0}' "$file")

# --- 3. Banned idioms — DATA, not a list in this script (L028) ---------
# studio/lessons/bans.txt is the source; a ban added there with a fixture
# is enforced here the same day. Until 2026-09-20 six phrases from August
# were hardcoded below while RECENT.md carried twenty.
if [[ -f "$REPO/studio/tools/bans.py" ]]; then
  while IFS= read -r hit; do
    [[ -n "$hit" ]] && findings+=("$hit")
  done < <(python3 "$REPO/studio/tools/bans.py" "$file" 2>/dev/null)
fi

# --- 4. Sentence discipline on ADDED lines only -----------------------
# STYLE 'say it plain' (a): narration under ~30 words; no more than
# three 'and's. Checked against the added side of the diff so an
# accepted chapter's existing long sentences are not the editor's
# problem — only what this pass introduced.
if git -C "$REPO" rev-parse --git-dir >/dev/null 2>&1; then
  rel="${file#$REPO/}"
  added="$(git -C "$REPO" diff -- "$rel" 2>/dev/null | grep '^+' | grep -v '^+++' | sed 's/^+//')"
  if [[ -n "$added" ]]; then
    while IFS= read -r line; do
      [[ -n "$line" ]] && findings+=("$line")
    done < <(printf '%s\n' "$added" | python3 -c '
import sys, re
text = re.sub(r"\s+", " ", " ".join(l.strip() for l in sys.stdin if l.strip()))
for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"“>])", text):
    w, a = len(s.split()), len(re.findall(r"\band\b", s))
    if w > 30 or a > 3:
        print(f"sentence discipline: {w}w and*{a} -> {s[:70]}...")
' 2>/dev/null)
  fi
fi

# --- 5. Accepted-chapter warning --------------------------------------
# An ACCEPTED chapter is folded: THREADS entries, plants and payoffs
# point at it. Editing one without a continuity read is how the
# 2026-09-15 heat pass put five contradictions on main.
if head -12 "$file" | grep -qi "ACCEPTED"; then
  findings+=("ACCEPTED chapter edited — folded prose. A continuity-keeper read is owed before this is re-accepted (see notes/heat-continuity-sweep-2026-09-15.md for what gets missed without one).")
fi

# --- 6. Epigraph word cap (35) ----------------------------------------
cap="$(python3 - "$file" <<'PY' 2>/dev/null
import sys, re
lines = open(sys.argv[1]).read().splitlines()
buf = []
for l in lines[:40]:
    if l.startswith(">"):
        buf.append(re.sub(r"^>\s*", "", l))
    elif buf:
        break
text = re.sub(r"\*\*.*?:\*\*", "", " ".join(buf))
n = len(text.split())
if n > 35:
    print(f"epigraph is {n} words, cap is 35")
PY
)"
[[ -n "$cap" ]] && findings+=("$cap")

if ((${#findings[@]})); then
  printf 'prose-guard: %s\n' "$(basename "$file")" >&2
  printf '  - %s\n' "${findings[@]}" >&2
  exit 2
fi
exit 0
