#!/usr/bin/env python3
"""targets-check.py — the chapter's definition of done, set before the draft.

    python3 studio/tools/targets-check.py books/<book>/book2 NN [--record]

The author (2026-09-17, after ch 20 counted twenty romance beats and
read as "a normal old book"): "choose the rank of the romance before
the chapter's written, giving us a definition of done." So the card
carries a TARGETS line, written before a word is drafted; the panel
writes an ACTUALS line after it reads; this compares them. The accept
gate runs it. `--record` appends the pair to `notes/targets.md`.

The card's line (under **Targets.**), seven values, one line:

    Romance 6 · Heat 4 · Laughs 2 · Ends down · Talk quiet · Words 3200 · Pays Dan

  Romance  1–10, the reader's scale (notes/romance-levels.md)
  Heat     0–8, the CHARGE scale (the density survey, l.50)
  Laughs   0, 1 or 3 — the fun inventory's count
  Ends     up | down | flat | button
  Talk     quiet (8–15%) | normal (15–25%)
  Words    the prose budget; ±15% is on target
  Pays     who loses something this chapter (the reversal)

The panel's line, anywhere in its verdict block:

    ACTUALS: romance 6 · heat 4 · laughs 2 · ends down

Talk and Words are measured here, not by the panel. Pays is planned
here and JUDGED by the developmental editor's THE BILL test from ch 25
(reader-tests L078) — "recorded" was the gap that let ch 24 be scored
"the cost is felt, never paid".

GATE: romance actual two or more under target → exit 2. Everything
else is reported. A chapter whose card carries no Targets line fails
here too — from ch 21 on the card lint refuses to send such a card.
"""
from __future__ import annotations
import glob, os, re, subprocess, sys

T_RE = re.compile(r"Romance\s+(\d+)\s*·\s*Heat\s+(\d+)\s*·(?:\s*Aisha\s+\d\s*·\s*Dan\s+\d\s*·\s*Wound\s+\d\s*·)?\s*(?:Laughs|Fun)\s+(\d+)\s*·(?:\s*Town\s+\d\s*·\s*Menace\s+\d\s*·)?\s*Ends\s+(\w+)\s*·\s*Talk\s+(\w+)\s*·\s*Words\s+([\d,]+)\s*·\s*Pays\s+(.+?)\s*$", re.I | re.M)
S_RE = re.compile(r"^(AISHA|DAN|WOUND|TOWN|MENACE):\s*([0-3])", re.M)
A_RE = re.compile(r"ACTUALS:\s*romance\s+(\d+)\s*·\s*heat\s+(\d+)\s*·\s*laughs\s+(\d+)\s*·\s*ends\s+(\w+)", re.I)


def read(p):
    return open(p, encoding="utf-8").read() if os.path.isfile(p) else ""


def prose_words(chap: str) -> int:
    text = read(chap)
    body = text.split("---", 1)[1] if "---" in text else text
    body = "\n".join(l for l in body.splitlines() if not l.startswith(">") and l.strip() != "***")
    return len(body.split())


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__); return 2
    book, ch = sys.argv[1].rstrip("/"), f"{int(sys.argv[2].lstrip('ch')):02d}"
    record = "--record" in sys.argv
    repo = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    book = book if os.path.isabs(book) else os.path.join(repo, book)
    card = os.path.join(book, "notes", "cards", f"ch{ch}-card.md")
    chap = os.path.join(book, "manuscript", f"ch{ch}.md")
    panels = sorted(glob.glob(os.path.join(book, "notes", f"ch{ch}-panel-*.md")))

    # the matrix is the source; the card's line is its copy
    tp = os.path.join(book, "canon", "TARGETS.md")
    mrow = {}
    if os.path.isfile(tp):
        for line in open(tp, encoding="utf-8"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 14 and cells[0] == str(int(ch)):
                mrow = dict(zip(["ch","pov","romance","heat","aisha","dan","wound","fun","town","menace","ends","talk","words","pays"], cells[:14]))
    m = T_RE.search(read(card))
    if mrow and not m:
        class _M:
            def groups(self_):
                return (mrow["romance"], mrow["heat"], mrow["fun"], mrow["ends"], mrow["talk"], mrow["words"], mrow["pays"])
        m = _M()
    if not m:
        print(f"targets-check ch{ch}: FAIL — the card has no Targets line "
              f"(notes/cards/ch{ch}-card.md, under **Targets.**): "
              f"'Romance N · Heat N · Laughs N · Ends X · Talk X · Words N · Pays X'", file=sys.stderr)
        return 2
    t_rom, t_heat, t_laugh, t_end, t_talk, t_words, t_pays = m.groups()
    t_rom, t_heat, t_laugh = int(t_rom), int(t_heat), int(t_laugh)
    t_words = int(t_words.replace(",", ""))

    a = None
    for p in panels:
        a = A_RE.search(read(p)) or a
    if not a:
        print(f"targets-check ch{ch}: FAIL — no ACTUALS line in any notes/ch{ch}-panel-*.md "
              f"('ACTUALS: romance N · heat N · laughs N · ends X'); the panel writes it after it reads", file=sys.stderr)
        return 2
    a_rom, a_heat, a_laugh, a_end = int(a.group(1)), int(a.group(2)), int(a.group(3)), a.group(4).lower()

    words = prose_words(chap)
    dlg = ""
    try:
        out = subprocess.run(["python3", os.path.join(repo, "studio/tools/dialogue-lint.py"), chap],
                             capture_output=True, text=True).stdout
        mm = re.search(r"(\d+(?:\.\d+)?)%", out)
        dlg = float(mm.group(1)) if mm else ""
    except Exception:
        pass
    a_talk = "quiet" if dlg != "" and dlg < 15 else ("normal" if dlg != "" else "?")

    # the score file (developmental editor): Aisha, Dan, Wound, Town, Menace
    sf = read(os.path.join(book, "notes", "scores", f"ch{ch}-score.md"))
    sc = {k.lower(): int(v) for k, v in S_RE.findall(sf)}
    extra = []
    for k in ("aisha", "dan", "wound", "town", "menace"):
        if mrow.get(k) not in (None, "·", ""):
            tv = int(mrow[k]); av = sc.get(k)
            verdict = "no score file" if av is None else ("ok" if av >= tv else ("under" if av == tv - 1 else "TWO UNDER"))
            extra.append((k.capitalize(), tv, av if av is not None else "—", verdict))
    rows = [
        ("Romance", t_rom, a_rom, "GATE" if a_rom <= t_rom - 2 else ("ok" if a_rom >= t_rom - 1 else "under")),
        ("Heat", t_heat, a_heat, "ok" if a_heat <= t_heat else "OVER the ceiling"),
        ("Laughs", t_laugh, a_laugh, "ok" if a_laugh >= t_laugh else "under"),
        ("Ends", t_end.lower(), a_end, "ok" if a_end == t_end.lower() else "differs"),
        ("Talk", t_talk.lower(), f"{a_talk} ({dlg}%)", "ok" if a_talk == t_talk.lower() else "differs"),
        ("Words", t_words, words, "ok" if abs(words - t_words) <= 0.15 * t_words else "off budget"),
        ("Pays", t_pays, "—", "see THE BILL in the score"),
    ] + extra
    print(f"targets-check ch{ch}   target → actual")
    fail = False
    for k, t, v, verdict in rows:
        flag = "✗" if verdict in ("GATE", "OVER the ceiling") else " "
        print(f"  {flag} {k:<8} {str(t):<10} → {str(v):<16} {verdict}")
        if verdict == "GATE":
            fail = True
    if record:
        led = os.path.join(book, "notes", "targets.md")
        if not os.path.isfile(led):
            open(led, "w").write("# Targets — set on the card before the draft; actuals after the panel\n\n"
                                 "Written by `studio/tools/targets-check.py --record`. The romance level gates acceptance (two or more under target holds the chapter); the rest is the record.\n\n"
                                 "| Ch | Romance T→A | Heat T→A | Laughs T→A | Ends T→A | Talk T→A | Words T→A | Pays | Date |\n|---|---|---|---|---|---|---|---|---|\n")
        import datetime
        line = (f"| {int(ch)} | {t_rom}→{a_rom} | {t_heat}→{a_heat} | {t_laugh}→{a_laugh} | {t_end}→{a_end} | "
                f"{t_talk}→{a_talk} | {t_words}→{words} | {t_pays} | {datetime.date.today()} |\n")
        s = read(led)
        s = re.sub(rf"^\| {int(ch)} \|.*\n", "", s, flags=re.M)
        open(led, "w").write(s.rstrip("\n") + "\n" + line)
        print(f"  recorded → {os.path.relpath(led)}")
    # F48 (audit 3): a reader shown the target returns it. When every
    # panel field equals the card, say so — the panel is launched blind
    # to the Targets line from ch 22.
    if a_rom == t_rom and a_heat == t_heat and a_laugh == t_laugh and str(a_end).lower() == str(t_end).lower():
        print("  ECHO? the panel's actuals equal the card's targets in every field — a reader shown the target returns it (audit 3, F48); launch the panel blind to the Targets line", file=sys.stderr)
    if fail:
        print(f"  HOLD — the romance level is two or more under its target; back to the drafter, or the author lowers the target on the card and says why.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
