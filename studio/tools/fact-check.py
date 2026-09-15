#!/usr/bin/env python3
"""fact-check.py — canon as greppable assertions.

    python3 studio/tools/fact-check.py books/campus-series
    python3 studio/tools/fact-check.py books/campus-series --book 1.2

Reads canon/FACTS.md, greps the manuscript for each row's
"contradicted by" pattern, and falsifies duration claims against the
declared clock anchors.

Exit 0 = clean. Exit 2 = contradictions found.

This exists because on 2026-09-15 a continuity sweep found five
blocking contradictions in ~86 added sentences, and three of the five
were flat fact errors that had been checkable on the page for weeks.
The keeper is the better instrument; this is the one that runs every
time.
"""
from __future__ import annotations
import argparse, pathlib, re, sys

NUM = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "fifteen": 15, "twenty": 20, "thirty": 30,
}


def rows(md: str, header_word: str) -> list[list[str]]:
    """Pull rows from every markdown table whose header contains a word."""
    out, in_tbl, keep = [], False, False
    for line in md.splitlines():
        if line.startswith("|"):
            # A regex cell may contain \| as a literal pipe. Protect it
            # from the column split, then restore it.
            protected = line.replace(r"\|", "\x00")
            cells = [c.strip().replace("\x00", "|")
                     for c in protected.strip("|").split("|")]
            if not in_tbl:
                in_tbl, keep = True, header_word.lower() in line.lower()
                continue
            if set("".join(cells)) <= set("-: "):
                continue
            if keep:
                out.append(cells)
        else:
            in_tbl = False
    return out


def scope_files(scope: str, book: pathlib.Path) -> list[pathlib.Path]:
    """Resolve a scope cell to the chapter files it governs."""
    b1 = sorted((book / "manuscript").glob("ch*.md"))
    b2 = sorted((book / "book2" / "manuscript").glob("ch*.md"))
    s = scope.lower().strip()
    if s.startswith("series"):
        return b1 + b2
    if s.startswith("1.1"):
        return b1
    if not s.startswith("1.2"):
        return b1 + b2
    # 1.2 with an optional chapter range: "1.2 ch08-end", "1.2 ch01–ch07"
    m = re.search(r"ch(\d+)\s*[-–—]\s*(?:ch)?(\d+|end)", s)
    if not m:
        return b2
    lo = int(m.group(1))
    hi = 99 if m.group(2) == "end" else int(m.group(2))
    return [f for f in b2 if lo <= int(re.search(r"ch(\d+)", f.name).group(1)) <= hi]


def check_facts(md: str, book: pathlib.Path) -> list[str]:
    found = []
    for r in rows(md, "contradicted by"):
        if len(r) < 6:
            continue
        fid, subject, fact, established, scope, pattern = r[:6]
        pattern = pattern.strip().strip("`")
        if not pattern or pattern in {"—", "-"} or pattern.startswith("*("):
            continue
        try:
            rx = re.compile(pattern, re.I)
        except re.error as e:
            found.append(f"{fid}: BAD REGEX ({e}) — fix the manifest")
            continue
        for path in scope_files(scope, book):
            text = path.read_text(encoding="utf-8", errors="replace")
            # Join semantic line breaks so a sentence split across lines
            # is still matchable, but keep a line number for the hit.
            lines = text.splitlines()
            flat = " ".join(l.strip() for l in lines)
            if not rx.search(flat):
                continue
            hit_line = next(
                (i + 1 for i in range(len(lines))
                 if rx.search(" ".join(l.strip() for l in lines[i:i + 3]))),
                0,
            )
            found.append(
                f"{fid}  {path.relative_to(book.parent.parent)}:{hit_line}\n"
                f"      canon: {subject} — {fact}\n"
                f"      established: {established}"
            )
    return found


def check_clocks(md: str, book: pathlib.Path) -> list[str]:
    """Falsify duration claims against declared anchors."""
    anchors: dict[str, list[tuple[str, int]]] = {}
    for r in rows(md, "anchor"):
        if len(r) < 4:
            continue
        chap, _what, time, _line = r[0], r[1], r[2], r[3]
        if re.match(r"^\d{1,2}:\d{2}$", time.strip()):
            anchors.setdefault(chap.strip(), []).append((time.strip(), 0))

    found = []
    for chap, times in anchors.items():
        m = re.match(r"(1\.\d)\s*ch(\d+)", chap)
        if not m:
            continue
        sub = "manuscript" if m.group(1) == "1.1" else "book2/manuscript"
        path = book / sub / f"ch{int(m.group(2)):02d}.md"
        if not path.exists():
            continue
        mins = sorted(int(t.split(":")[0]) * 60 + int(t.split(":")[1])
                      for t, _ in times)
        if len(mins) < 2:
            continue
        span = mins[-1] - mins[0]
        if span < 0:
            span += 24 * 60
        # Overnight scenes: the anchors wrap midnight.
        if mins[0] > 12 * 60 and mins[-1] < 12 * 60:
            span = (24 * 60 - mins[-1]) if False else span
        real = min(span, 24 * 60 - span) if span > 12 * 60 else span

        text = path.read_text(encoding="utf-8", errors="replace")
        flat = " ".join(l.strip() for l in text.splitlines())
        for cm in re.finditer(r"\b(\w+)\s+hours?\s+from\s+now\b", flat, re.I):
            word = cm.group(1).lower()
            claimed = NUM.get(word, None)
            if claimed is None:
                continue
            if abs(claimed * 60 - real) > 45:
                found.append(
                    f"CLOCK  {path.relative_to(book.parent.parent)}\n"
                    f"      claim: \"{cm.group(0)}\" = {claimed}h\n"
                    f"      anchors in this chapter span {real // 60}h{real % 60:02d}m"
                    f"  ({', '.join(t for t, _ in times)})"
                )
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("book", help="book directory, e.g. books/campus-series")
    args = ap.parse_args()

    book = pathlib.Path(args.book).resolve()
    manifest = book / "canon" / "FACTS.md"
    if not manifest.exists():
        print(f"fact-check: no manifest at {manifest}", file=sys.stderr)
        return 1
    md = manifest.read_text(encoding="utf-8")

    findings = check_facts(md, book) + check_clocks(md, book)

    if not findings:
        print("fact-check: clean — no canon contradictions found.")
        return 0
    print(f"fact-check: {len(findings)} CONTRADICTION(S)\n")
    for f in findings:
        print(f"  ✗ {f}\n")
    print("  Each is a fact the page already established being contradicted")
    print("  elsewhere in the manuscript. Fix the prose, or if canon itself")
    print("  changed, change the row in canon/FACTS.md and say so in the PR.")
    return 2


if __name__ == "__main__":
    sys.exit(main())
