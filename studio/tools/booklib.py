#!/usr/bin/env python3
"""booklib.py — the studio's conventions, in one place.

Every checker imports this instead of re-deriving where books live, how
chapters are named, or how a declaration table parses. When a convention
changes it changes here, once.

WHY THIS EXISTS
Eight checkers were written in two days and each one independently
hardcoded this series' layout — Book 1.1 at the series root, Book 1.2
in a `book2/` subdirectory. That is an accident of how the repo grew,
not a convention, and a new series would not have it. Four tools would
have needed editing to add Book 1.3.

Per studio/MECHANISM.md: a checker should take a book directory and know
nothing else. If it needs editing for a new book, that is a leak.
"""
from __future__ import annotations
import pathlib, re

CH_RE = re.compile(r"ch(\d+)", re.I)


def find_books(root: pathlib.Path) -> list[pathlib.Path]:
    """Every book under a path.

    A BOOK is any directory containing a `manuscript/` with chapter
    files in it. That definition works for this series' inherited
    layout and for any sane one, without either being special-cased.
    """
    root = pathlib.Path(root).resolve()
    out = []
    if (root / "manuscript").is_dir() and any((root / "manuscript").glob("ch*.md")):
        out.append(root)
    for sub in sorted(root.iterdir()) if root.is_dir() else []:
        if sub.is_dir() and not sub.name.startswith(".") \
           and (sub / "manuscript").is_dir() \
           and any((sub / "manuscript").glob("ch*.md")):
            out.append(sub)
    return out


def survey(root: pathlib.Path):
    """(books that conform, [(path, why it does not)]).

    THE CONVENTION, from CLAUDE.md: one chapter per file, named to sort,
    under `manuscript/`. Every checker requires it.

    This repo has four layouts. campus-series conforms; spytwins nests
    per book under `manuscripts/`; youngnick and mybyb keep a single
    master file. `find_books` returned an empty list for all three, in
    silence.

    A guardrail suite that reports "all clear" on books it never opened
    is worse than no suite — it is false confidence with a green tick.
    So non-conforming books are RETURNED with a reason, not skipped, and
    the runner prints them.
    """
    root = pathlib.Path(root).resolve()
    if not root.is_dir():
        return [], []
    ok, skipped = [], []
    cands = [root] + [d for d in sorted(root.iterdir())
                      if d.is_dir() and not d.name.startswith(".")]
    for c in cands:
        man = c / "manuscript"
        if not man.is_dir():
            if (c / "manuscripts").is_dir():
                skipped.append((c, "uses manuscripts/ (plural), not manuscript/"))
            continue
        if any(man.glob("ch*.md")):
            ok.append(c)
        elif any(man.rglob("*.md")):
            skipped.append((c, "manuscript/ holds whole-book files, "
                               "not one chapter per file"))
        else:
            skipped.append((c, "manuscript/ has no .md files"))
    return ok, skipped


def chapters(book: pathlib.Path) -> dict[int, pathlib.Path]:
    """{chapter number: path}, sorted."""
    out = {}
    for f in sorted((pathlib.Path(book) / "manuscript").glob("ch*.md")):
        m = CH_RE.search(f.stem)
        if m:
            out[int(m.group(1))] = f
    return dict(sorted(out.items()))


def body(path: pathlib.Path) -> str:
    """Chapter prose, with the H1, the production header and the `---`
    rule stripped. The header's continuation lines read as prose, which
    is how one tool reported every chapter opening on "accepted at the
    merge"."""
    t = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
    parts = t.split("\n---\n", 1)
    return parts[-1] if len(parts) > 1 else t


def pov(path: pathlib.Path) -> str:
    head = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")[:400]
    m = re.search(r"POV:\s*([A-Z][a-z]+)", head)
    return m.group(1) if m else ""


def tables(path: pathlib.Path, header_contains: str | None = None
           ) -> list[list[str]]:
    """Rows from markdown tables, with `\\|` preserved inside cells.

    Declarations are markdown so a human maintains them and a tool
    parses them. A regex cell may contain an escaped pipe; splitting
    naively on `|` truncated every pattern in the fact manifest.
    """
    p = pathlib.Path(path)
    if not p.exists():
        return []
    out, in_tbl, keep = [], False, True
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.startswith("|"):
            protected = line.replace(r"\|", "\x00")
            cells = [c.strip().replace("\x00", "|")
                     for c in protected.strip("|").split("|")]
            if not in_tbl:
                in_tbl = True
                keep = (header_contains is None
                        or header_contains.lower() in line.lower())
                continue
            if set("".join(cells)) <= set("-: "):
                continue
            if keep:
                out.append(cells)
        else:
            in_tbl = False
    return out


def declaration(book: pathlib.Path, name: str) -> pathlib.Path | None:
    """Find a declaration for a book, falling back to the series.

    Book-scoped declarations (BEATS, REGISTERS) live with the book;
    series canon (FACTS, NAMES) lives one level up and is shared. The
    test, per MECHANISM.md: does it change when the next book starts?
    """
    book = pathlib.Path(book).resolve()
    for cand in (book / "canon" / name, book.parent / "canon" / name):
        if cand.exists():
            return cand
    return None


def aliases(book: pathlib.Path) -> dict[str, list[str]]:
    """The name map from canon/NAMES.md: {character: [every form]}."""
    f = declaration(book, "NAMES.md")
    if not f:
        return {}
    out = {}
    for cells in tables(f):
        if len(cells) >= 2 and cells[0] and cells[0] != "Character":
            names = [a.strip() for a in cells[1].split(",") if a.strip()]
            if names:
                out[cells[0]] = sorted(names, key=len, reverse=True)
    return out


def leads(book: pathlib.Path) -> list[str]:
    """The two most frequent POV characters."""
    counts: dict[str, int] = {}
    for f in chapters(book).values():
        p = pov(f)
        if p:
            counts[p] = counts.get(p, 0) + 1
    return [n for n, _ in sorted(counts.items(), key=lambda kv: -kv[1])[:2]]


def words(text: str) -> int:
    return len(re.findall(r"\S+", text))
