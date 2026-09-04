#!/bin/bash
# Chapter lint battery — one manuscript chapter per run.
#   bash studio/tools/chapter-lint.sh books/<book>/.../chNN.md
# Everything greppable gets grepped, never proofread (STYLE.md). Reports
# only; a hit is a finding for the orchestrator, not an auto-fix.
# Adopted 2026-09-03 with the ch 5 re-cut (campus 1.2); the furniture
# blacklist and the naming report answer the author's 2026-09-03 go
# (STYLE.md, "Rules are full lists; rations are per book").
f="$1"; [ -f "$f" ] || { echo "usage: $0 FILE"; exit 2; }
echo "== dialogue floor (15%; quiet band 8-10% once per quarter)"
python3 "$(dirname "$0")/dialogue-lint.py" "$f"
echo "== over-80-column lines"
awk 'length($0)>80 {print FNR": "length($0)}' "$f"
echo "== dangling colon/dash paragraph ends (must be zero)"
awk 'prev ~ /[:—]$/ && $0=="" {print NR-1": "prev} {prev=$0}' "$f"
echo "== sentences with 2+ em dashes (budget ONE per chapter)"
tr '\n' ' ' < "$f" | tr '.!?' '\n\n\n' | grep '—.*—' | sed 's/^ *//' | cut -c1-120
echo "== banned words / scaffolds (campus scrub + RECENT.md)"
grep -n -i 'unhurried\|declined to [a-z]*\b\|whole [a-z]* of it\|and meant it\|one beat\|before [a-z]* could vote\|before [a-z]* could dress\|never once\|which was its own\|the way [a-z]* [a-z]* [a-z]*' "$f"
echo "== chorus construction \"somebody's ___\" (once per BOOK in narration; ledger in THREADS)"
grep -n -i "somebody.s [a-z]" "$f"
echo "== arrival clock (six months / since June — cap 1 per chapter)"
grep -n -i 'six months\|since june' "$f"
echo "== wry which-appendix (ration; let the gesture sit unnamed)"
grep -n ', which ' "$f"
echo "== sentence-initial Somewhere (cap 2)"
grep -n '^Somewhere\|\. Somewhere' "$f"
echo "== FURNITURE BLACKLIST (modernity binds props — B2-D03 / DIALS 5)"
grep -n -i 'casserole\|\bfoil\b\|\bpans\b\|oxygen chamber\|grandma\|grandmother\|tinfoil\|tupperware\|percolator' "$f"
echo "== BEVERAGE REGISTER (no coffee at night; beer/whiskey/seltzer)"
grep -n -i 'coffee\|thermos' "$f"
echo "== AGE (Merritt stays 38; no line spends his age)"
grep -n -i 'thirty-eight\|\b38\b\|his age\|a man his age\|years of living rooms' "$f"
echo "== NAMING REPORT — the quarterback (rule in RECENT.md; judge the speaker of each line)"
grep -n -i '\bTrey\b\|\b7\b\|number seven\|the seven\b' "$f"
echo "== NAMING REPORT — the athletic director (unnamed canon; never 'the AD' in prose)"
grep -n -i 'athletic director\|\bAD\b' "$f"
echo "== [TK] / [CHECK]"
grep -n '\[TK\|\[CHECK' "$f"
echo "== trailing whitespace"
grep -n ' $' "$f"
echo "== done"
