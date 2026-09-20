#!/usr/bin/env python3
"""matrix-strip.py — the chapter's row of the targets matrix, where eyes are.

    python3 studio/tools/matrix-strip.py books/<book>/book2 21        # the row, and plan → actual if actuals exist
    python3 studio/tools/matrix-strip.py books/<book>/book2 21 --row  # the one-line row only (what a card carries)
    python3 studio/tools/matrix-strip.py --current                     # every book with a matrix: the chapter in progress

The author (2026-09-19): "what tool can we build to ensure that this
matrix is viewed before and after each chapter?" The matrix is
`canon/TARGETS.md`. This prints one row of it, and it is wired into the
four moments a chapter passes through, so nobody has to remember it:

  SessionStart  — prints the strip for the chapter in progress (the
                  highest-numbered card), so every session opens on it.
  brief-gate    — a drafting-assistant launched on a chapter brief must
                  have the row in its prompt, or it does not launch.
  card-lint     — the card's Targets line must equal the row (already).
  pr-lint       — a [CHAPTER] PR body must carry the row; a [FOLD] PR
                  body must carry the plan → actual lines.

"Viewed" is not a hope here: before, the drafter cannot start without
it and the author cannot be sent a card without it; after, the PR
cannot open without the comparison, and the accept gate runs it.
"""
from __future__ import annotations
import glob, os, re, subprocess, sys

COLS = ["ch", "pov", "romance", "heat", "aisha", "dan", "wound", "fun", "town", "menace", "ends", "talk", "words", "pays"]


def read(p):
    return open(p, encoding="utf-8").read() if os.path.isfile(p) else ""


def row(book: str, ch: int) -> dict:
    tp = os.path.join(book, "canon", "TARGETS.md")
    for line in read(tp).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 14 and cells[0] == str(ch):
            return dict(zip(COLS, cells[:14]))
    return {}


def row_line(r: dict) -> str:
    if not r:
        return ""
    return (f"Romance {r['romance']} · Heat {r['heat']} · Aisha {r['aisha']} · Dan {r['dan']} · "
            f"Wound {r['wound']} · Fun {r['fun']} · Town {r['town']} · Menace {r['menace']} · "
            f"Ends {r['ends']} · Talk {r['talk']} · Words {r['words']} · Pays {r['pays']}")


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("Laughs", "Fun").replace(",", "")).strip().lower()


def current_chapter(book: str) -> int:
    cards = glob.glob(os.path.join(book, "notes", "cards", "ch*-card.md"))
    nums = [int(re.search(r"ch(\d+)", os.path.basename(p)).group(1)) for p in cards]
    return max(nums) if nums else 0


def strip(book: str, ch: int, repo: str) -> str:
    r = row(book, ch)
    if not r:
        return f"MATRIX ch {ch}: no row in {os.path.relpath(os.path.join(book, 'canon', 'TARGETS.md'))} — plan it before the card"
    out = [f"MATRIX ch {ch} ({r['pov']}) — {row_line(r)}"]
    # after: plan → actual, if the readers have run
    have_actuals = glob.glob(os.path.join(book, "notes", f"ch{ch:02d}-panel-*.md")) or \
                   os.path.isfile(os.path.join(book, "notes", "scores", f"ch{ch:02d}-score.md"))
    if have_actuals:
        try:
            res = subprocess.run(["python3", os.path.join(repo, "studio/tools/targets-check.py"), book, str(ch)],
                                 capture_output=True, text=True)
            body = (res.stdout or "").strip()
            if body:
                out.append(body)
            elif res.stderr:
                out.append("  " + res.stderr.strip().splitlines()[0])
        except Exception as e:
            out.append(f"  (targets-check did not run: {e})")
    else:
        out.append("  actuals: none yet — the panel's ACTUALS line and the score file come after the draft")
    return "\n".join(out)


def main() -> int:
    repo = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    if "--current" in flags:
        for tp in glob.glob(os.path.join(repo, "books", "*", "*", "canon", "TARGETS.md")) + \
                  glob.glob(os.path.join(repo, "books", "*", "canon", "TARGETS.md")):
            book = os.path.dirname(os.path.dirname(tp))
            ch = current_chapter(book)
            if ch:
                print(strip(book, ch, repo))
        return 0
    if len(args) < 2:
        print(__doc__); return 2
    book = args[0] if os.path.isabs(args[0]) else os.path.join(repo, args[0])
    ch = int(args[1].lstrip("ch"))
    if "--row" in flags:
        print(row_line(row(book, ch)))
        return 0
    print(strip(book, ch, repo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
