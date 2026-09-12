#!/usr/bin/env python3
"""Opening check — does this chapter's first paragraph repeat an earlier one?

    python3 studio/tools/opening-check.py books/<book>/manuscript/chNN.md

Compares the chapter's opening paragraph (the first prose paragraph after
the `---` rule, epigraph blockquotes skipped) against the opening of every
lower-numbered chapter in the same directory:

  * shared five-word runs between the two openings (FAIL at 3 or more);
  * any sentence of six words or more in this opening that appears
    verbatim ANYWHERE in an earlier chapter (FAIL);
  * a calendar opening — the first line begins on a weekday, a month, a
    date, or "N days/weeks out/off" (WARN: open on a thing, not the date);
  * the seams (2026-09-12): every section's first and last line printed,
    and each later section's opening compared with every earlier
    chapter's section openings (WARN at 2 shared five-word runs).

Born 2026-09-07 from the author's note on campus 1.2 ch 12: "the first
paragraph seems very similar to previous first paragraphs. I don't have a
good way of checking." Now there is one. Exit 1 on any FAIL.
"""
import re, sys, os, glob, itertools

DAYS = r"(monday|tuesday|wednesday|thursday|friday|saturday|sunday)"
MONTHS = r"(january|february|march|april|may|june|july|august|september|october|november|december)"
CAL = re.compile(rf"^\s*({DAYS}|{MONTHS}|(the )?(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|\w+teenth|twentieth|\w+-\w+)\b.*(of|,)|\w+ (days|weeks) (out|off|to))", re.I)

def body(path):
    s = open(path, encoding="utf-8").read()
    if "\n---\n" in s:
        s = s.split("\n---\n", 1)[1]
    return s

def sections(path):
    """The chapter's sections, split on a `***` line; epigraph lines skipped."""
    out, cur = [], []
    for l in body(path).split("\n"):
        if l.strip() == "***":
            out.append(cur); cur = []
            continue
        if l.startswith(">"):
            continue
        cur.append(l)
    out.append(cur)
    return out

def first_paragraph(lines):
    para, started = [], False
    for l in lines:
        if not l.strip():
            if started:
                break
            continue
        started = True
        para.append(l.strip())
    return para

def last_line(lines):
    for l in reversed(lines):
        if l.strip():
            return l.strip()
    return ""

def opening(path):
    return first_paragraph(sections(path)[0])

def section_openings(path):
    return [first_paragraph(sec) for sec in sections(path)]

def words(t):
    return re.findall(r"[a-z0-9']+", t.lower())

def runs(t, n=5):
    w = words(t)
    return set(tuple(w[i:i + n]) for i in range(len(w) - n + 1))

def sentences(t):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t) if len(words(s)) >= 6]

def chapter_num(p):
    m = re.search(r"ch(\d+)", os.path.basename(p))
    return int(m.group(1)) if m else -1

def main():
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(2)
    target = sys.argv[1]
    d = os.path.dirname(target) or "."
    n = chapter_num(target)
    earlier = sorted(p for p in glob.glob(os.path.join(d, "ch*.md")) if 0 <= chapter_num(p) < n)
    op_lines = opening(target)
    op = " ".join(op_lines)
    fails = 0
    if op_lines and CAL.match(op_lines[0]):
        print(f"WARN  calendar opening: \"{op_lines[0][:70]}\" — open on a thing, not the date")
    my_runs = runs(op)
    for p in earlier:
        shared = my_runs & runs(" ".join(opening(p)))
        if shared:
            tag = "FAIL" if len(shared) >= 3 else "note"
            if tag == "FAIL": fails += 1
            ex = " | ".join(" ".join(r) for r in sorted(shared)[:3])
            print(f"{tag}  {os.path.basename(p)}: {len(shared)} shared five-word run(s) in the opening — {ex}")
    for s in sentences(op):
        norm = " ".join(words(s))
        for p in earlier:
            if norm and norm in " ".join(words(body(p))):
                fails += 1
                print(f"FAIL  sentence already on {os.path.basename(p)}: \"{s[:80]}\"")
                break
    # The seams (second instrument audit, F23; first audit F3/F14): every
    # section's first and last line, and each later section's opening
    # against every earlier chapter's section openings (WARN, not FAIL —
    # the chapter opening above is the only hard gate).
    secs = sections(target)
    if len(secs) > 1:
        print("-- seams (each section's first and last line):")
        for k, sec in enumerate(secs, 1):
            fp = first_paragraph(sec)
            print(f"   §{k} first: {(fp[0] if fp else '')[:70]}")
            print(f"   §{k} last:  {last_line(sec)[:70]}")
        earlier_secs = []
        for p in earlier:
            for so in section_openings(p):
                earlier_secs.append((os.path.basename(p), " ".join(so)))
        for k, sec in enumerate(secs[1:], 2):
            mine = runs(" ".join(first_paragraph(sec)))
            for name, text in earlier_secs:
                shared = mine & runs(text)
                if len(shared) >= 2:
                    ex = " | ".join(" ".join(r) for r in sorted(shared)[:2])
                    print(f"WARN  §{k} opens like a section of {name}: {len(shared)} shared five-word run(s) — {ex}")
    print("OPENING CHECK:", "FAIL" if fails else "PASS", f"({len(earlier)} earlier chapters)")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
