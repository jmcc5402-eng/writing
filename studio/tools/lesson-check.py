#!/usr/bin/env python3
"""lesson-check.py — every author catch has an enforcer, or says why not.

    python3 studio/tools/lesson-check.py            # audit the ledger; exit 2 on a gap
    (from pr-lint.py on a [FOLD] PR)                # also: no AUTHOR-NOTES row from the
                                                    # last 7 days without a LEDGER row

Reads studio/lessons/LEDGER.md. For each row, by Kind:
  BAN         the ID is in bans.txt and has a fixture that fires (bans.py --test)
  READER      the ID is in reader-tests.txt and the named test is in the agent file
  CHECK/GATE/PROCESS/CANON
              the Enforced-by column names a file that exists and contains the ID,
              or a file under studio/tools/ / .claude/ that exists
  INSTRUCTION allowed only when the Enforced-by column says why nothing can enforce it
The author (2026-09-20): every bug does two things — fix the bug, fix the
environment. This is the check that the second half happened. (L028)
"""
from __future__ import annotations
import glob, os, re, subprocess, sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LESSONS = os.path.join(REPO, "studio", "lessons")


def rows():
    out = []
    for line in open(os.path.join(LESSONS, "LEDGER.md"), encoding="utf-8"):
        if not line.startswith("| L"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 8:
            continue
        out.append(dict(id=cells[0], date=cells[1], source=cells[2], catch=cells[3],
                        kind=cells[4].upper(), fix=cells[5], enforcer=cells[6], status=cells[7]))
    return out


def ids_in(r):
    m = re.match(r"L(\d+)(?:–L(\d+))?", r["id"])
    if not m:
        return [r["id"]]
    a = int(m.group(1)); b = int(m.group(2) or a)
    return [f"L{n:03d}" for n in range(a, b + 1)]


def file_has(path, token):
    try:
        return token in open(path, encoding="utf-8").read()
    except OSError:
        return False


def ban_ids():
    s = set()
    for line in open(os.path.join(LESSONS, "bans.txt"), encoding="utf-8"):
        if line.startswith("L"):
            s.add(line.split("\t")[0].strip())
    return s


def reader_rows():
    out = {}
    for line in open(os.path.join(LESSONS, "reader-tests.txt"), encoding="utf-8"):
        if line.startswith("L"):
            p = line.rstrip("\n").split("\t")
            if len(p) >= 5:
                out[p[0]] = dict(agent=p[1], test=p[2], glob=p[3], token=p[4])
    return out


def audit():
    problems = []
    bans = ban_ids()
    readers = reader_rows()
    for r in rows():
        for lid in ids_in(r):
            k = r["kind"]
            if k == "BAN":
                if lid not in bans:
                    problems.append(f"{lid} ({r['catch'][:40]}): kind BAN but not in bans.txt")
            elif k == "READER":
                rr = readers.get(lid)
                if not rr:
                    problems.append(f"{lid}: kind READER but not in reader-tests.txt")
                else:
                    agent = os.path.join(REPO, ".claude", "agents", rr["agent"] + ".md")
                    if not file_has(agent, rr["test"]):
                        problems.append(f"{lid}: reader-tests names test '{rr['test']}' but {rr['agent']}.md does not carry it")
            elif k in ("CHECK", "GATE", "PROCESS", "CANON"):
                named = re.findall(r"`([^`]+)`", r["enforcer"]) + re.findall(r"\b([\w./-]+\.(?:py|sh|md|json))\b", r["enforcer"])
                ok = False
                for n in named:
                    for cand in (n, os.path.join("studio/tools", n), os.path.join(".claude/skills", n),
                                 os.path.join(".claude/skills", n, "SKILL.md"), os.path.join("studio", n)):
                        p = os.path.join(REPO, cand)
                        if os.path.isfile(p):
                            ok = True
                            break
                    if ok:
                        break
                if k == "CANON":
                    # F47 (audit 3): a CANON row is enforced only when a fact file carries the ID
                    ok = False
                    for cand in glob.glob(os.path.join(REPO, "books", "*", "canon", "FACTS.md")) + glob.glob(os.path.join(REPO, "books", "*", "*", "DECISIONS.md")) + glob.glob(os.path.join(REPO, "books", "*", "*", "canon", "*.md")):
                        if file_has(cand, lid):
                            ok = True; break
                if not ok:
                    problems.append(f"{lid}: kind {k} but the Enforced-by column names no file that exists{' (a CANON row needs a FACTS/DECISIONS/canon row carrying the ID)' if k == 'CANON' else ''}: '{r['enforcer'][:60]}'")
            elif k == "INSTRUCTION":
                if "why" not in r["enforcer"].lower():
                    problems.append(f"{lid}: kind INSTRUCTION with no 'Why not enforced' reason in the Enforced-by column")
            else:
                problems.append(f"{lid}: unknown kind '{k}'")
    # the bans must fire
    res = subprocess.run([sys.executable, os.path.join(REPO, "studio/tools/bans.py"), "--test"], capture_output=True, text=True)
    if res.returncode != 0:
        problems.append("bans.py --test: " + (res.stdout.strip().splitlines() or ["failed"])[0])
    return problems


def notes_without_lessons(days=7):
    """AUTHOR-NOTES rows dated within `days` whose row number is cited by no LEDGER row."""
    import datetime
    today = datetime.date.today()
    cited = set()
    for r in rows():
        cited |= set(re.findall(r"\b(\d{3})\b", r["source"]))
    gaps = []
    for line in open(os.path.join(REPO, "studio", "AUTHOR-NOTES.md"), encoding="utf-8"):
        m = re.match(r"\|\s*(\d{3})\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|", line)
        if not m:
            continue
        n, d = m.group(1), datetime.date.fromisoformat(m.group(2))
        if (today - d).days <= days and n not in cited:
            gaps.append(n)
    return gaps


def main():
    problems = audit()
    gaps = notes_without_lessons()
    for p in problems:
        print("✗ " + p)
    if gaps:
        print(f"✗ AUTHOR-NOTES rows from the last 7 days with no LEDGER row (what enforces them?): {', '.join(gaps)}")
    n = len(rows())
    if problems or gaps:
        print(f"lesson-check: {n} ledger rows — {len(problems) + (1 if gaps else 0)} gap(s)")
        return 2
    print(f"lesson-check: {n} ledger rows, every enforcer present; every recent author note has a lesson")
    return 0


if __name__ == "__main__":
    sys.exit(main())
