#!/usr/bin/env python3
"""pr-lint.py — the say-it test, applied to what the agent writes to the author.

Used as a PreToolUse hook on the PR-creating tools, so a body that fails
never reaches GitHub. PreToolUse is the only hook event that can block.

Reads the hook JSON on stdin. Exit 0 = pass, exit 2 = blocked with reasons
on stderr.

WHY THIS EXISTS
Taste entry 13 — "talk to me like an author, not an engineer" — is the
only entry in the sheet with no check behind it, and it has the most
repeats per week in the ledger:

  Sep  3: the say-it test "applies to your writing to me as much as to
          the manuscript."
  Sep  9: "Ha ok. Remember don't be so clever!"  (a PR named "the
          handful", which the author then had to ask about)
  Sep 10: "Remember the summaries before the chapter needs to read
          easily. Sometimes it reads like a list of things."
  Sep 11: "Too much to read make more concise"

Every other taste entry has a panel, a lint or a gate. This surface —
the agent's own output to the human — was ungoverned, which is why the
same note kept coming back.
"""
from __future__ import annotations
import json, re, sys

MAX_WORDS = 1200          # a PR body the author has to read in one sitting
MAX_FIRST_SENTENCE = 28   # STYLE "say it plain" (a), applied to us
MAX_SENTENCE = 34         # a little looser than prose; still a ceiling


def sentences(text: str) -> list[str]:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)      # drop code blocks
    text = re.sub(r"^\s*[|>#\-*].*$", " ", text, flags=re.M)  # tables, lists
    text = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    ti = payload.get("tool_input") or {}
    body = ti.get("body") or ""
    title = ti.get("title") or ""
    if not body:
        return 0

    problems, notes = [], []

    # 1. The house PR template. One PR = one decision, and the decision
    #    has to be findable without reading the whole body.
    if "## Ask" not in body:
        problems.append(
            "no '## Ask' section — studio/PR-WORKFLOW.md requires the "
            "decision to be the first thing the author reads")

    # 2. Say the actual thing, first. The opening sentence of the Ask is
    #    the one line the author is guaranteed to read.
    m = re.search(r"##\s*Ask\s*\n+(.+?)(?:\n\n|\n##|$)", body, re.S)
    if m:
        first = sentences(m.group(1))
        if first:
            n = len(first[0].split())
            if n > MAX_FIRST_SENTENCE:
                problems.append(
                    f"the Ask opens with a {n}-word sentence "
                    f"(limit {MAX_FIRST_SENTENCE}) — say the actual thing "
                    f"in one plain sentence first")
            if not re.search(r"\b(merge|accept|adopt|rule|decide|strike|"
                             r"keep|choose|approve|reject|set|confirm)\b",
                             first[0], re.I):
                notes.append(
                    "the Ask's first sentence names no action — the author "
                    "should know what he is being asked to DO from line one")

    # 3. Length. "Too much to read make more concise" (2026-09-11).
    words = len(re.findall(r"\S+", body))
    if words > MAX_WORDS:
        problems.append(
            f"body is {words} words (limit {MAX_WORDS}) — the author's "
            f"attention is the scarce resource in this studio")

    # 4. The same sentence rule the prose obeys.
    long_ones = [(len(s.split()), s) for s in sentences(body)
                 if len(s.split()) > MAX_SENTENCE]
    for n, s in long_ones[:3]:
        problems.append(f"{n}-word sentence: \"{s[:70]}…\"")
    if len(long_ones) > 3:
        problems.append(f"…and {len(long_ones) - 3} more over {MAX_SENTENCE} words")

    # 5. Don't be so clever (2026-09-09). A coined label in the TITLE that
    #    never gets defined in the body is the exact shape of "the handful".
    for coin in re.findall(r"\bthe ([a-z]{4,})\b", title):
        if coin not in body.lower().replace(title.lower(), ""):
            notes.append(
                f"the title coins \"the {coin}\" and the body never "
                f"explains it — name the work by what it does")

    # 6. The matrix, before and after (author, 2026-09-19). A [CHAPTER] PR
    #    body carries the chapter's row; a [FOLD] PR carries plan → actual.
    if re.search(r"\[CHAPTER\]", title) and not re.search(r"Romance\s+\d+\s*·\s*Heat\s+\d+", body):
        problems.append("a [CHAPTER] PR carries the matrix row (python3 studio/tools/matrix-strip.py <book> <ch> --row) — the author sees the plan before the page")
    if re.search(r"\[FOLD\]", title) and not re.search(r"target\s*→\s*actual|\d+\s*→\s*\d+", body):
        problems.append("a [FOLD] PR carries plan → actual (python3 studio/tools/matrix-strip.py <book> <ch>) — the author sees what the page did against the plan")

    if problems:
        print("pr-lint: BLOCKED — taste entry 13, talk to the author "
              "like an author", file=sys.stderr)
        for p in problems:
            print(f"  ✗ {p}", file=sys.stderr)
        for n in notes:
            print(f"  · {n}", file=sys.stderr)
        print("  Rewrite the body and try again. This is the one rule the "
              "author has had to repeat four times.", file=sys.stderr)
        return 2
    if notes:
        for n in notes:
            print(f"pr-lint note: {n}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
