#!/usr/bin/env python3
"""card-lint.py — the chapter card, checked before the author reads it.

    python3 studio/tools/card-lint.py books/<book>/notes/cards/chNN-card.md
    (as a hook)  reads the SendUserFile JSON on stdin; lints every file
                 under notes/cards/; exit 2 blocks the send.

The card is the one document the author reads for every chapter, and
the one with the most repeated notes against it: "reads like a list,"
"too much to read," "don't be so clever," a 40-word sentence read
aloud (the ch 20 audit, item 27). Until 2026-09-17 the rules lived in
the showrunner's remit and the kit template — instructions. This runs.

Rules (STANDARDS 26's card, kit 12, taste 13):
  1. BODY under 350 words — the title, the byline and the bold section
     labels do not count; the calls do.
  2. Every sentence under 30 words (STYLE "say it plain" (a)); a call
     may run to 40, because a call carries its alternative.
  3. Each call is ONE line and ONE sentence, numbered.
  4. The sections are present, in order: the plot; each lead by name;
     the romance; the town/antagonist/clock; the calls.
  5. No ledger words in the prose: no thread IDs (B2-T##, F##, S##),
     no "rung," no doc names (dossier, arc-docs, THREADS). "Register"
     and "beat" are English words too and are not caught.
  6. No `[TK` on a card — an open question is a call, not a marker.
  7. A **Targets.** section with the one-line definition of done
     (author, 2026-09-17): 'Romance N · Heat N · Laughs N · Ends X ·
     Talk X · Words N · Pays X' — read by studio/tools/targets-check.py.

Exit 0 = pass (WARNs allowed). Exit 1 = FAIL on the command line;
exit 2 = FAIL as a hook (the send is blocked).
"""
from __future__ import annotations
import json, re, sys, os

MAX_BODY = 350
MAX_SENT = 30
MAX_CALL = 40
LEDGER = re.compile(r"\b(B2-T\d+|F\d{1,2}\b|S\d{2}\b|SC\d\b|rung|dossier|arc-docs|THREADS|romance-arc|boyd-arc)\b", re.I)


def sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def lint(path: str) -> tuple[list[str], list[str]]:
    fails, warns = [], []
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except OSError as e:
        return [f"cannot read {path}: {e}"], []

    body_words = 0
    prose: list[str] = []
    calls: list[str] = []
    labels: list[str] = []
    in_calls = False
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if not s:
            continue
        if s.startswith("# "):
            continue                                   # the title
        if i <= 4 and re.match(r"^[A-Z][a-z]+, ", s):  # the byline
            continue
        m = re.match(r"^\*\*(.+?)\*\*$", s)
        if m:
            labels.append(m.group(1).rstrip(".").lower())
            in_calls = m.group(1).lower().startswith("your calls")
            continue
        body_words += len(s.split())
        if in_calls:
            if not re.match(r"^\d+\. ", s):
                fails.append(f"l.{i}: a call that is not a numbered one-liner: \"{s[:60]}\"")
            else:
                calls.append(s)
        else:
            prose.append(s)
        if "[TK" in s or "[CHECK" in s:
            fails.append(f"l.{i}: a marker on the card — make it a call or settle it: \"{s[:60]}\"")

    # 1. length
    if body_words > MAX_BODY:
        fails.append(f"body is {body_words} words (max {MAX_BODY}) — cut, don't compress")
    elif body_words > MAX_BODY - 20:
        warns.append(f"body is {body_words} words — near the ceiling of {MAX_BODY}")

    # 2. sentences
    for s in sentences(" ".join(x for x in prose if not re.search(r"Romance\s+\d+\s*·", x))):
        n = len(s.split())
        if n >= MAX_SENT:
            fails.append(f"{n}-word sentence: \"{s[:70]}…\"")
        ands = len(re.findall(r"\band\b", s))
        if ands > 3:
            fails.append(f"{ands} 'and's in one sentence: \"{s[:70]}…\"")

    # 3. calls
    if not calls:
        fails.append("no calls — a card ends on the author's calls, one line each")
    for c in calls:
        text = re.sub(r"^\d+\. ", "", c)
        ss = sentences(text)
        if len(ss) > 1:
            fails.append(f"a call in {len(ss)} sentences (one only): \"{text[:60]}…\"")
        n = len(text.split())
        if n > MAX_CALL:
            fails.append(f"a {n}-word call (max {MAX_CALL}): \"{text[:60]}…\"")
        if " or " not in text and "; or" not in text:
            warns.append(f"a call with no alternative in it: \"{text[:60]}…\"")

    # 4. sections
    want = ["the plot", "the romance", "your calls"]
    for w in want:
        if not any(l.startswith(w) for l in labels):
            fails.append(f"missing section: **{w.title()}.**")
    if len(labels) < 5:
        warns.append(f"only {len(labels)} sections — the card names each lead and the town/clock")

    # 7. the targets line (the definition of done, set before the draft)
    tline = [s for s in prose if re.search(r"Romance\s+\d+\s*·\s*Heat\s+\d+", s)]
    if not any(l.startswith("targets") for l in labels) or not tline:
        fails.append("no **Targets.** line — 'Romance N · Heat N · Laughs N · Ends X · Talk X · Words N · Pays X' (the definition of done, set before the draft; targets-check.py reads it)")
    else:
        t = tline[0]
        if not re.search(r"Romance\s+(10|[1-9])\b", t): fails.append(f"Targets: Romance must be 1–10: \"{t[:60]}\"")
        if not re.search(r"Heat\s+[0-8]\b", t): fails.append(f"Targets: Heat must be 0–8: \"{t[:60]}\"")
        if not re.search(r"Laughs\s+[013]\b", t): fails.append(f"Targets: Laughs is 0, 1 or 3: \"{t[:60]}\"")
        if not re.search(r"Ends\s+(up|down|flat|button)\b", t, re.I): fails.append(f"Targets: Ends is up/down/flat/button: \"{t[:60]}\"")
        if not re.search(r"Talk\s+(quiet|normal)\b", t, re.I): fails.append(f"Targets: Talk is quiet/normal: \"{t[:60]}\"")
        if not re.search(r"Words\s+[\d,]{3,6}\b", t): fails.append(f"Targets: Words is a number: \"{t[:60]}\"")
        if not re.search(r"Pays\s+\S", t): fails.append(f"Targets: Pays names who loses: \"{t[:60]}\"")

    # 5. ledger words
    for s in [x for x in prose if not re.search(r"Romance\s+\d+\s*·", x)] + calls:
        m = LEDGER.search(s)
        if m:
            fails.append(f"ledger word on the card: '{m.group(0)}' in \"{s[:60]}…\"")

    return fails, warns


def report(path: str, fails: list[str], warns: list[str]) -> None:
    name = os.path.relpath(path)
    for w in warns:
        print(f"WARN  {name}: {w}", file=sys.stderr)
    for f in fails:
        print(f"FAIL  {name}: {f}", file=sys.stderr)
    print(f"CARD LINT {name}: {'FAIL' if fails else 'PASS'} ({len(fails)} fail, {len(warns)} warn)",
          file=sys.stderr)


def main() -> int:
    if len(sys.argv) > 1:
        rc = 0
        for p in sys.argv[1:]:
            fails, warns = lint(p)
            report(p, fails, warns)
            rc = rc or (1 if fails else 0)
        return rc
    # hook mode
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    ti = payload.get("tool_input") or {}
    files = ti.get("files") or []
    if isinstance(files, str):
        files = [files]
    root = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    blocked = False
    for f in files:
        if "/notes/cards/" not in f or not f.endswith(".md"):
            continue
        p = f if os.path.isabs(f) else os.path.join(root, f)
        fails, warns = lint(p)
        report(p, fails, warns)
        if fails:
            blocked = True
    if blocked:
        print("BLOCKED: fix the card before it goes to the author (studio/tools/card-lint.py).",
              file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
