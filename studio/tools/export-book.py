#!/usr/bin/env python3
"""export-book.py — the text a reader actually gets, and a check on THAT.

    python3 studio/tools/export-book.py books/campus-series           # build/<slug>.md + lint
    python3 studio/tools/export-book.py books/campus-series --check   # lint only, write nothing

Exit 0 = the export is clean. Exit 2 = something from the workshop would ship.

WHY THIS EXISTS
The author, 2026-09-24: *"Honestly, I'm not convinced that 1.1 is done
either."* Checking that turned up a gap no chapter check could see:
nothing in the studio turns a manuscript file into the text a reader
receives. Every chapter carries a production header above its `---`
rule — the POV line, "ACCEPTED by…", the winning drafter's card, and in
Book 1.1 two `[TK]` flags — and nothing strips it. Every check in this
repo reads the manuscript. None reads the book.

So this assembles the reader-facing text (the chapter title, then the
prose after the rule, in order) and lints the OUTPUT for anything that
belongs to the workshop. The principle generalises: check the artifact
the customer receives, not the source it was built from. (L082)

Front and back matter (title page, copyright, the series call to action
that `kdp-launch-mechanics` says is "where KU series money is actually
made") are reported as missing until `front-matter.md` and
`back-matter.md` exist in `studio/launch/<slug>/`, where the slug is the
book directory under `books/` with `/` as `-` (1.1 is `campus-series`,
1.2 is `campus-series-book2`). Launch material lives in `studio/`
because the delivery thread is scoped off `books/` (AUTHOR-NOTES 293).
A copy beside the manuscript is still read if `studio/launch/` has none.
"""
from __future__ import annotations
import os, pathlib, re, sys

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Things that belong to the workshop. Each is specific enough not to fire
# on prose: a bare word like "panel" or "draft" would, so none is here.
LEAKS = [
    (r"\[TK\b", "an open [TK] marker"),
    (r"\[CHECK\b", "an open [CHECK] marker"),
    (r"^POV:", "a production POV line"),
    (r"\bACCEPTED (#|at|by)\b", "an acceptance note"),
    (r"\b(notes|plots|drafts|studio|canon)/[\w./-]+", "a repository path"),
    (r"\bcard [A-Z]\d\b|\bvariance card\b", "a variance-card reference"),
    (r"\bblind[- ]competition\b|\bcandidate [A-C]\b", "a drafting-competition note"),
    (r"<!--|-->", "an HTML comment"),
    (r"\bB\d-D\d+(\.\d+)?\b|\bL0\d\d\b|\bF\d{2}\b(?= )", "an internal decision or ledger ID"),
]


def chapters(book: pathlib.Path) -> list[pathlib.Path]:
    return sorted((book / "manuscript").glob("ch[0-9][0-9].md"))


def launch_dir(book: pathlib.Path) -> pathlib.Path:
    """studio/launch/<slug>/ — books/campus-series/book2 -> campus-series-book2."""
    try:
        slug = str(book.relative_to(pathlib.Path(REPO, "books"))).replace("/", "-")
    except ValueError:
        slug = book.name
    return pathlib.Path(REPO, "studio", "launch", slug)


def matter(book: pathlib.Path, name: str) -> pathlib.Path:
    launch = launch_dir(book) / name
    return launch if launch.exists() or not (book / name).exists() else book / name


def reader_text(path: pathlib.Path) -> str:
    """The H1 title, then everything after the first `---` rule."""
    text = path.read_text(encoding="utf-8")
    title = next((l for l in text.splitlines() if l.startswith("# ")), f"# {path.stem}")
    body = text.split("\n---\n", 1)[1] if "\n---\n" in text else text
    return f"{title}\n\n{body.strip()}\n"


def lint(text: str) -> list[tuple[int, str, str]]:
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        for rx, what in LEAKS:
            if re.search(rx, line):
                out.append((i, what, line.strip()[:90]))
                break
    return out


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if not args:
        print("usage: export-book.py <book-dir> [--check]", file=sys.stderr)
        return 1
    book = pathlib.Path(args[0]).resolve()
    chs = chapters(book)
    if not chs:
        print(f"export-book: no manuscript/chNN.md under {book}")
        return 0
    parts = []
    front, back = matter(book, "front-matter.md"), matter(book, "back-matter.md")
    if front.exists():
        parts.append(front.read_text(encoding="utf-8").strip() + "\n")
    parts += [reader_text(c) for c in chs]
    if back.exists():
        parts.append(back.read_text(encoding="utf-8").strip() + "\n")
    out = "\n\n".join(parts)
    words = len(out.split())

    try:
        rel = book.relative_to(REPO)
    except ValueError:
        rel = book
    print(f"export-book  ({rel}: {len(chs)} chapters, {words:,} words as the reader gets them)")
    if "--check" not in sys.argv:
        dst = pathlib.Path(REPO, "build", str(rel).replace("/", "-") + ".md")
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(out, encoding="utf-8")
        print(f"  wrote {dst.relative_to(REPO)} (git-ignored; rebuild any time)")

    bad = lint(out)
    missing = [n for n, p in (("front-matter.md", front), ("back-matter.md", back)) if not p.exists()]
    for n in missing:
        print(f"  MISSING: {launch_dir(book).relative_to(REPO)}/{n} — a shippable book needs it (studio/gtm/kdp-launch-mechanics-2026-09-03.md §2b)")
    if not bad and not missing:
        print("  clean — nothing from the workshop reaches the reader")
        return 0
    if bad:
        print(f"  {len(bad)} line(s) of workshop text would ship:")
        for i, what, line in bad[:12]:
            print(f"    line {i:5d}  {what:<34} {line}")
        if len(bad) > 12:
            print(f"    …and {len(bad) - 12} more")
    return 2


if __name__ == "__main__":
    sys.exit(main())
