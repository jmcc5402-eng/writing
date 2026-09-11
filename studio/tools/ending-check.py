#!/usr/bin/env python3
"""ending-check.py CHAPTER.md — reads every section of a chapter for the author's
catches on 1.2 ch 13, 14 and 16:
  1. the LAST section names who is in it inside its first three prose lines
     (STYLE, the establishing line: "It just starts with saying 'she'");
     names come from the book's registry name map when one is found, else
     from capitalized words seen three times;
  2. no staccato ending: the last section's exchange is full sentences;
  3. ECHO REPLIES anywhere (STYLE "slow the good parts" (d)): a short reply
     whose content words all appear in the line before it ("I heard them go
     by the window. They were talking." / "They were.");
  4. per-section numbers the panel reads: words, dialogue lines, words per
     dialogue line, narration words per dialogue line.
Warns; never fails the lint (the second instrument-audit, F20)."""
import re,sys,collections,os
p=sys.argv[1]; txt=open(p).read()
body=txt.split('\n---\n',1)[1] if '\n---\n' in txt else txt
sections=[s.strip() for s in re.split(r'\n\*\*\*\n',body) if s.strip()]
STOP=set('the a an and of to in on at it is was were be been they them he she i you we his her their my your our that this there here not no yes so then than as for with by from up down out off over'.split())
def name_pool():
    # find the registry's name map beside the manuscript, if any
    d=os.path.dirname(os.path.abspath(p))
    for cand in [os.path.join(d,'..','notes','furniture-registry.md')]:
        if os.path.exists(cand):
            reg=open(cand).read()
            if '## Name map' in reg:
                part=reg.split('## Name map',1)[1]
                names=set()
                for row in part.split('\n'):
                    m=re.match(r'\|\s*([A-Z][A-Za-z\'\-]+(?:\s+[A-Z][A-Za-z\'\-]+)*)\s*\|',row)
                    if m:
                        for tok in m.group(1).split():
                            if tok[0].isupper() and tok.lower() not in ('the',): names.add(tok)
                if names: return names,'the registry name map'
    words=re.findall(r"\b[A-Z][a-z]+\b",body)
    common={'The','She','He','It','They','Then','And','But','Nobody','Not','There','That','This','In','On','At','By','A','Her','His','When','What','You','I','No','One','Two','Under','Down','Around','So','If','Every','Nothing','Because','Win','Go','Tuesday','Monday','Saturday','Sunday','Wednesday','Thursday','Friday','December','February','August','June','Doc','Coach','Doctor','Miss'}
    cnt=collections.Counter(w for w in words if w not in common)
    return {w for w,c in cnt.items() if c>=3},'capitalized words seen three times'
names,src=name_pool()
pov=re.search(r'POV:\s*([A-Z][a-z]+)',txt); pov=pov.group(1) if pov else None
print("== ENDING CHECK (studio/tools/ending-check.py)")
# 4. per-section numbers + 3. echo replies
print(f"section  words  dlg-lines  words/dlg  narr/dlg")
prev=None; echoes=[]
for i,sec in enumerate(sections,1):
    lines=[l for l in sec.split('\n') if l.strip() and not l.startswith('>')]
    dl=[l for l in lines if l.lstrip().startswith(('"','“'))]
    w=sum(len(re.sub(r'[^A-Za-z\' ]',' ',l).split()) for l in lines)
    dw=sum(len(re.sub(r'[^A-Za-z\' ]',' ',l).split()) for l in dl)
    n=len(dl)
    print(f"{i:>7}  {w:>5}  {n:>9}  {(dw/n if n else 0):>9.1f}  {((w-dw)/n if n else 0):>8.1f}")
    for l in dl:
        toks=[t.lower() for t in re.sub(r'[^A-Za-z\' ]',' ',l).split()]
        if prev is not None and 1<=len(toks)<=4:
            content=[t for t in toks if t not in STOP]
            ptoks=set(t.lower() for t in re.sub(r'[^A-Za-z\' ]',' ',prev).split())
            if content and all(t in ptoks for t in content): echoes.append((i,l.strip()))
            elif not content and all(t in ptoks for t in toks): echoes.append((i,l.strip()))
        prev=l
if echoes:
    for i,l in echoes: print(f"WARN: echo reply in section {i}: {l}  (STYLE: no volleys between the leads — a short reply that only repeats the line before it)")
# 1. last section names
last=sections[-1]
lines=[l for l in last.split('\n') if l.strip() and not l.startswith('>')]
first3=' '.join(lines[:3])
present=sorted({n for n in names if re.search(r'\b'+re.escape(n)+r'\b',first3)})
others=[n for n in present if n!=pov]
print("last section's first three lines name: "+(', '.join(present) if present else 'NOBODY')+(f"  (POV: {pov}; names from {src})" if pov else f"  (names from {src})"))
if not present: print("WARN: the last section names nobody in its first three lines (STYLE: the establishing line names who is in the room)")
elif not others: print("WARN: the last section names only the POV lead in its first three lines; if anyone else is in the room, name them before a pronoun (STYLE: the establishing line)")
# 2. staccato ending
dl=[re.sub(r'[^A-Za-z\' ]',' ',l) for l in lines if l.lstrip().startswith(('"','“'))]
if dl:
    avg=sum(len(l.split()) for l in dl)/len(dl); short=sum(1 for l in dl if len(l.split())<=3)
    print(f"last section dialogue: {len(dl)} lines, avg {avg:.1f} words, {short} of three words or fewer")
    if avg<6 or (len(dl)>=4 and short>=len(dl)/2): print("WARN: staccato ending (STYLE: the last exchange is full sentences and moves the romance or an arc)")
else: print("last section has no dialogue")
