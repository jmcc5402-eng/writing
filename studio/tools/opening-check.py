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
    date, or "N days/weeks out/off" (WARN: open on a thing, not the date).

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

def opening(path):
    lines, started = [], False
    for l in body(path).split("\n"):
        if l.startswith(">"):
            continue
        if not l.strip():
            if started:
                break
            continue
        started = True
        lines.append(l.strip())
    return lines

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
    print("OPENING CHECK:", "FAIL" if fails else "PASS", f"({len(earlier)} earlier chapters)")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
