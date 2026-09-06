#!/usr/bin/env python3
"""Build the author's listening file for one chapter.

The author reads chapters as a plain Markdown file, in a car, by ear
(studio/PIPELINE.md, "The audio gate"). This strips the production
header, keeps the Grapevine epigraph as spoken lines, joins the
manuscript's semantic line breaks into paragraphs, and turns *** into
a spoken pause. Since 2026-09-06 the chapter card ("where we are")
rides on top, so the author reviews the arcs before the chapter
(studio/PIPELINE.md §3c, "The chapter card").

    python3 studio/tools/listening-file.py CHAPTER.md OUT.md "Title" [CARD.md]
"""
import sys

src, dst, title = sys.argv[1], sys.argv[2], sys.argv[3]
card = sys.argv[4] if len(sys.argv) > 4 else None
lines = open(src, encoding="utf-8").read().split("\n")
body = lines[lines.index("---") + 1:]
out = [f"# {title}", ""]
if card:
    ctext = open(card, encoding="utf-8").read().strip().split("\n")
    # drop the card's own H1 and its italic instruction line
    ctext = [l for l in ctext if not l.startswith("# ")]
    out += ["## Before you read: where we are", ""]
    para = []
    for l in ctext:
        if l.startswith("*") and l.endswith("*"):
            continue
        if l.startswith("## "):
            if para:
                out.append(" ".join(s.strip() for s in para)); out.append(""); para = []
            out.append("**" + l[3:].strip() + ".**"); out.append(""); continue
        if l.strip() == "":
            if para:
                out.append(" ".join(s.strip() for s in para)); out.append(""); para = []
            continue
        para.append(l)
    if para:
        out.append(" ".join(s.strip() for s in para)); out.append("")
    out += ["* * *", "", "## The chapter", ""]
para = []
def flush():
    if para:
        out.append(" ".join(s.strip() for s in para)); out.append("")
        para.clear()
for l in body:
    if l.startswith(">"):
        t = l.lstrip("> ").strip()
        if not t:
            flush(); continue
        t = t.replace("**", "").rstrip(" —").rstrip("—").strip()
        para.append(t)
        continue
    if l.strip() == "***":
        flush(); out.append("* * *"); out.append(""); continue
    if l.strip() == "":
        flush(); continue
    para.append(l)
flush()
open(dst, "w", encoding="utf-8").write("\n".join(out).rstrip() + "\n")
print(f"wrote {dst}: {sum(len(x.split()) for x in out)} words")
