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
grep -n -i 'unhurried\|declined to [a-z]*\b\|whole [a-z]* of it\|and meant it\|one beat\|before [a-z]* could vote\|before [a-z]* could dress\|never once\|which was its own\|the way \(a\|an\|the\|you\|he\|she\|they\|it\|somebody\) [a-z]* \(does\|did\|do\|would\|had\|has\|might\|could\)\b' "$f"
echo "== BANS (studio/lessons/bans.txt — the lesson ledger's greppable bans; L028)"
python3 "$(dirname "$0")/bans.py" "$f"
echo "== PRONOUN CROWDING (author #179: 'it keeps saying he instead of his name… it talks about Ty also'; a paragraph with two men's names and five or more he/his/him is a finding; L045)"
python3 - "$f" <<'PY'
import re, sys
text = open(sys.argv[1], encoding="utf-8").read()
names = ["Dan", "Ty", "Tick", "Ray", "Boyd", "Denny", "Sonny", "Trey", "Odell", "Peanut", "Cal", "Marcus", "Wes", "Coach"]
alias = {"Merritt": "Dan", "Coach": "Dan"}
start = 1
for para in re.split(r"\n\s*\n", text):
    n = para.count("\n") + 2
    found = [alias.get(nm, nm) for nm in names + ["Merritt"] if re.search(rf"\b{nm}\b", para)]
    hes = len(re.findall(r"\b(he|his|him)\b", para, re.I))
    if len(set(found)) >= 2 and hes >= 5:
        print(f"{start}: {len(set(found))} men ({', '.join(sorted(set(found)))}) and {hes} he/his/him — say the name")
    start += n
PY
echo "== QUESTIONS ENDING IN A PERIOD (red team 2026-09-20: on audio nobody sounds like they want the answer; cap 2 per chapter; L043)"
grep -n -E '^"(What|Where|When|Why|How|Who|Which|Is|Are|Was|Were|Do|Does|Did|Can|Could|Would|Will|Should|Have|Has)\b[^"?]*\."' "$f" | head -12
echo "== TOUCH SPAN (the touch is a scene, not a sentence — author 2026-09-20 rereading ch 21: 'we just have one line that her arm goes warm'; body sentences around each touch cluster, three or fewer is a finding; taste 20; L055)"
python3 - "$f" <<'PY'
import re, sys
text = open(sys.argv[1], encoding="utf-8").read()
lines = text.split("\n")
touch = re.compile(r"\b(shoulder|arm|hand|hands|knee|hip|side|fingers|palm|wrist)\b[^.\n]{0,40}\b(against|on|along|through|into|over|under)\b[^.\n]{0,30}\b(his|her|him|Dan|Aisha|Merritt|Cole)\b|\b(his|her) (hand|arm|shoulder|fingers) (on|in|against|over|along) (her|his)\b", re.I)
body = re.compile(r"\b(warm(er|est)?|heat|hot|pulse|heart(beat)?|breath(e|ed|ing)?|throat|stomach|chest|skin|neck|wrist|flush(ed)?|shiver|sweat|blood|face (went|was|burned)|could feel|felt it|feel it)\b", re.I)
hits = [i for i, ln in enumerate(lines) if touch.search(ln) and not ln.startswith('"')]
if not hits:
    print("no touch between the leads found"); sys.exit(0)
clusters, cur = [], [hits[0]]
for h in hits[1:]:
    if h - cur[-1] <= 25: cur.append(h)
    else: clusters.append(cur); cur = [h]
clusters.append(cur)
for c in clusters:
    lo, hi = max(0, c[0] - 6), min(len(lines), c[-1] + 40)
    span = "\n".join(lines[lo:hi])
    sents = re.split(r"(?<=[.!?])\s+", span)
    bodies = [x.strip() for x in sents if body.search(x) and not x.strip().startswith('"')]
    flag = "" if len(bodies) > 3 else "   — one line is not a scene: run her body across the beats and say the confusion plain (taste 20)"
    print(f"touch cluster l.{c[0]+1}–{c[-1]+1}: {len(c)} touch line(s), {len(bodies)} body sentence(s) in l.{lo+1}–{hi}{flag}")
PY
echo "== chorus construction \"somebody's ___\" (once per BOOK in narration; ledger in THREADS)"
grep -n -i "somebody.s [a-z]" "$f"
echo "== arrival clock (six months / since June — cap 1 per chapter)"
grep -n -i 'six months\|since june' "$f"
echo "== wry which-appendix (ration; let the gesture sit unnamed)"
grep -n ', which ' "$f"
echo "== sentence-initial Somewhere (cap 2)"
grep -n '^Somewhere\|\. Somewhere' "$f"
echo "== FURNITURE BLACKLIST (modernity binds props — B2-D03 / DIALS 5)"
grep -n -i 'casserole\|\bfoil\b\|\bpans\b\|oxygen chamber\|grandma\|grandmother\|tinfoil\|tupperware\|percolator\|\bsupper\b' "$f"
echo "== BEVERAGE REGISTER (no coffee at night; beer/whiskey/seltzer)"
grep -n -i 'coffee\|thermos' "$f"
echo "== AGE (Merritt stays 38; no line spends his age)"
grep -n -i 'thirty-eight\|\b38\b\|his age\|a man his age\|years of living rooms' "$f"
echo "== NAMING REPORT — the quarterback (rule in RECENT.md; judge the speaker of each line)"
grep -n -i '\bTrey\b\|\b7\b\|number seven\|the seven\b' "$f"
echo "== LEAD NAMES (each lead named at least once in narration per chapter — STYLE.md, say-it test item 6)"
echo "Aisha/Cole: $(grep -c 'Aisha\|Cole' "$f")   Dan/Merritt: $(grep -c 'Dan\b\|Merritt' "$f")   'the doctor': $(grep -c -i 'the doctor' "$f")   'the coach': $(grep -c -i 'the coach\b' "$f")"
echo "== NAMING REPORT — the athletic director (unnamed canon; never 'the AD' in prose)"
grep -n -i 'athletic director\|\bAD\b' "$f"
echo "== OPENING CHECK (the first paragraph against every earlier chapter's — studio/tools/opening-check.py)"
python3 "$(dirname "$0")/opening-check.py" "$f"; oc=$?
python3 "$(dirname "$0")/ending-check.py" "$f"
echo "== REPETITION (four-word runs used three or more times in this chapter — first audit F5)"
python3 - "$f" <<'PY'
import re, sys, collections
t = open(sys.argv[1], encoding="utf-8").read()
if "\n---\n" in t: t = t.split("\n---\n", 1)[1]
w = re.findall(r"[a-z']+", t.lower())
c = collections.Counter(tuple(w[i:i+4]) for i in range(len(w) - 3))
stop = {"and","the","of","a","to","in","it","was","she","he","her","his","had","that","on","at","and","with","for","not","did","as","but","him"}
for run, n in c.most_common():
    if n < 3: break
    if sum(x in stop for x in run) >= 3: continue
    print(f"  {n}x  {' '.join(run)}")
PY
echo "== SENTENCES (narration over 30 words; more than three 'and's; or two 'and's with a name said twice — STYLE 'say it plain' (a))"
python3 - "$f" <<'PY'
import re, sys
t = open(sys.argv[1], encoding="utf-8").read()
if "\n---\n" in t: t = t.split("\n---\n", 1)[1]
t = re.sub(r"^>.*$", "", t, flags=re.M)          # epigraphs
t = re.sub(r"\*[^*\n]+\*", "", t)                 # italics (texts, notes)
t = re.sub(r'"[^"]*"', '""', t)                    # dialogue out
paras = [p for p in re.split(r"\n\s*\n", t) if p.strip()]
long_ = ands = 0
for para in paras:
    flat = " ".join(l.strip() for l in para.split("\n"))
    for s in re.split(r"(?<=[.!?])\s+", flat):
        w = re.findall(r"[A-Za-z'’]+", s)
        n_and = sum(1 for x in w if x.lower() == "and")
        names = [x for x in w if x[:1].isupper() and x.lower() not in ("i",)]
        rep = len(names) - len(set(names))   # a name said twice in one sentence
        if len(w) > 30 or n_and > 3 or (n_and >= 2 and rep >= 1 and len(w) > 14):
            long_ += len(w) > 30; ands += n_and > 3
            print(f"  {len(w):3d}w  and×{n_and}  {s[:72]}")
print(f"  {long_} over thirty words; {ands} with more than three 'and's")
PY
echo "== SENTENCE SHAPE (the cap is a budget, not a ban — variance lives in the tail; L071)"
python3 - "$f" <<'PY'
import re, statistics as st, sys
t = open(sys.argv[1], encoding="utf-8").read()
if "\n---\n" in t: t = t.split("\n---\n", 1)[1]
t = re.sub(r"^>.*$", "", t, flags=re.M)
L = [len(re.findall(r"[A-Za-z'’]+", s))
     for s in re.split(r"(?<=[.!?])\s+", " ".join(t.split())) if s.strip()]
L = [x for x in L if x]
if len(L) < 40:
    print("  too few sentences to judge the shape"); raise SystemExit
cv = st.pstdev(L) / (sum(L) / len(L))
p95 = sorted(L)[int(len(L) * .95)]
over, under = sum(1 for x in L if x > 30), sum(1 for x in L if x <= 7)
print(f"  {len(L)} sentences · mean {sum(L)/len(L):4.1f} · p95 {p95} · max {max(L)} · "
      f"over-30 {over} ({100*over/len(L):.1f}%) · under-8 {under} ({100*under/len(L):.1f}%) · CV {cv:.2f}")
bad = []
if cv < 0.60:
    bad.append(f"CV {cv:.2f} is under 0.60 — the sentences are running to one length")
if p95 < 33:
    bad.append(f"p95 {p95} — the long tail is gone; nothing here breathes out")
if over == 0:
    bad.append("not one sentence over thirty words — rule 7 says ORDINARILY under thirty, not never")
for b in bad:
    print(f"  FINDING: {b}")
if bad:
    print("  Reference: ch 12-17 ran CV 0.78-0.89, p95 38-68, over-30 10-35%.")
    print("  Ch 18-24 ran CV 0.52-0.57, p95 27-32, over-30 0.3-5% — seven chapters")
    print("  of metronome, and every one of them passed its own gate. The fix for")
    print("  the long sentence deleted the long sentence. Let one or two run.")
PY
echo "== [TK] / [CHECK]"
grep -n '\[TK\|\[CHECK' "$f"
echo "== trailing whitespace"
grep -n ' $' "$f"
echo "== done"
[ "$oc" -eq 0 ] || { echo "LINT: FAIL (the opening check)"; exit 1; }
