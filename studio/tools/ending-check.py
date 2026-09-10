#!/usr/bin/env python3
"""ending-check.py CHAPTER.md — two author catches, both twice (1.2 ch 13, ch 14):
  1. the last section must NAME who is in it inside its first three prose lines
     (STYLE, the establishing line: "It just starts with saying 'she'");
  2. no staccato endings: the chapter's last exchange is full sentences
     ("that last dialogue is way too robotic… too staccato").
Warns; never fails the lint. Names are read from the chapter's own header
(POV: Name) plus every Capitalized word that appears 3+ times in narration."""
import re,sys,collections
p=sys.argv[1]; txt=open(p).read()
body=txt.split('\n---\n',1)[1] if '\n---\n' in txt else txt
sections=[s.strip() for s in re.split(r'\n\*\*\*\n',body) if s.strip()]
last=sections[-1]
lines=[l for l in last.split('\n') if l.strip() and not l.startswith('>')]
first3=' '.join(lines[:3])
# candidate names: capitalized tokens seen 3+ times in the whole chapter, minus sentence starters that are common words
words=re.findall(r"\b[A-Z][a-z]+\b",body)
common={'The','She','He','It','They','Then','And','But','Nobody','Not','There','That','This','In','On','At','By','A','Her','His','When','What','You','I','No','One','Two','Under','Down','Around','So','If','Every','Nothing','Around','Because','Win','Go','Tuesday','Monday','Saturday','Sunday','Wednesday','Thursday','Friday','December','February','August','June','Doc','Coach','Doctor','Miss'}
cnt=collections.Counter(w for w in words if w not in common)
names=[w for w,c in cnt.items() if c>=3]
present=[n for n in names if re.search(r'\b'+n+r'\b',first3)]
pov=re.search(r'POV:\s*([A-Z][a-z]+)',txt); pov=pov.group(1) if pov else None
others=[n for n in present if n!=pov]
print("== ENDING CHECK (studio/tools/ending-check.py)")
print("last section's first three lines name: "+(', '.join(present) if present else 'NOBODY')+(f"  (POV: {pov})" if pov else ""))
if not present: print("WARN: the last section names nobody in its first three lines (STYLE: the establishing line names who is in the room)")
elif not others: print("WARN: the last section names only the POV lead in its first three lines; if anyone else is in the room, name them before a pronoun (STYLE: the establishing line)")
# staccato: dialogue lines in the last section
dl=[re.sub(r'[^A-Za-z\' ]',' ',l) for l in lines if l.lstrip().startswith(('"','“'))]
if dl:
    avg=sum(len(l.split()) for l in dl)/len(dl)
    short=sum(1 for l in dl if len(l.split())<=3)
    print(f"last section dialogue: {len(dl)} lines, avg {avg:.1f} words, {short} of three words or fewer")
    if avg<6 or (len(dl)>=4 and short>=len(dl)/2): print("WARN: staccato ending (STYLE: the last exchange is full sentences and moves the romance or an arc)")
else: print("last section has no dialogue")
# volley runs anywhere (STYLE "slow the good parts" (d)): three consecutive dialogue lines of four words or fewer
allq=[re.sub(r'[^A-Za-z\' ]',' ',l) for l in body.split('\n') if l.lstrip().startswith(('"','“'))]
runs=0; streak=0
for l in allq:
    n=len(l.split())
    streak = streak+1 if n<=4 else 0
    if streak==3: runs+=1
if runs: print(f"WARN: {runs} run(s) of three short volleys (dialogue lines of four words or fewer, consecutive) — STYLE: no volleys between the leads; run the sentences out")
