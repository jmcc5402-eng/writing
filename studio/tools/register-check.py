#!/usr/bin/env python3
"""register-check.py — does the signal register hold?

    python3 studio/tools/register-check.py books/campus-series/book2

Exit 0 = every register holds. Exit 2 = one has drifted.

A signal register is a recurring ordinary detail whose variation
carries the feeling — Dan drinks beer, and on New Year's Eve in a
house rather than a motel room he drinks red wine out of a jelly jar,
and nobody says why. Spec: studio/craft/registers.md.

The device is fragile in one specific way, and it is the reason this
tool exists: **a substitution spent early, months before its planned
beat, silently devalues the beat.** Nobody notices, because the early
use is perfectly good prose in its own chapter. It only fails later,
and by then the chapter is accepted.

Found on its first run: Book 1.2 reserves bourbon for the dark night at
ch 26, and ch 4 already hands Dan a whiskey, two fingers, unasked.

WHAT IT CANNOT DO
It cannot tell you whether a substitution lands. That is the panel and
the author. It checks that the default holds, the spend is where it was
declared, and nobody spent it twice.
"""
from __future__ import annotations
import argparse, pathlib, re, sys


def body(p: pathlib.Path) -> str:
    t = p.read_text(encoding="utf-8", errors="replace")
    parts = t.split("\n---\n", 1)
    return parts[-1] if len(parts) > 1 else t


def parse(path: pathlib.Path) -> list[dict]:
    """Blocks of: heading, default, established-by, and spend rows."""
    regs, cur = [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            if cur:
                regs.append(cur)
            cur = {"name": line[3:].strip(), "default": None,
                   "established": None, "spends": []}
            continue
        if cur is None:
            continue
        m = re.match(r"-\s*\*\*default:\*\*\s*`([^`]+)`", line)
        if m:
            cur["default"] = m.group(1)
            continue
        m = re.match(r"-\s*\*\*established by:\*\*\s*(?:1\.\d\s*)?ch\s*(\d+)", line)
        if m:
            cur["established"] = int(m.group(1))
            continue
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 3 and re.match(r"^\d+$", cells[0]):
                sub = re.match(r"`([^`]+)`", cells[1])
                if sub:
                    says = cells[2]
                    cur["spends"].append({
                        "ch": int(cells[0]), "sub": sub.group(1),
                        "says": says,
                        "planned": "not yet written" in says.lower(),
                        # A SHIFT is permanent: the substitution becomes the
                        # new default from that chapter on. Aisha puts on the
                        # staff parka at ch 7 and never takes it off, which
                        # the first build read as "spent eleven times".
                        "shift": "[shift]" in says.lower(),
                    })
    if cur:
        regs.append(cur)
    return [r for r in regs if r["default"] and r["spends"]]


def build_rx(spec: str):
    """`a|b` are alternatives; `!x` after a term excludes it.

    "wine !wine night" matches the drink and not the event — which the
    first run needed, because it reported Dan's ch-18 wine as spent
    early on the strength of two mentions of *wine night*.

    The canon docs write alternation the way the CLAUDE.md grep line
    does — `her coat\\|own coat` — so a backslash-pipe has to mean the
    same thing here as a bare pipe. It did not, and the cost was a
    silent lie: splitting on a bare `|` left the first alternative
    ending in a backslash, `\\bher coat\\\\\\b` matched nothing, and the
    checker reported Aisha's coat as having ZERO ordinary uses before
    its ch-7 spend. It has five. A check that reads its own spec
    wrongly is worse than no check, because it is believed.
    """
    spec = spec.replace("\\|", "|")
    parts = [p.strip() for p in spec.split("!")]
    pos = [t.strip() for t in parts[0].split("|") if t.strip()]
    neg = [t.strip() for t in parts[1:] if t.strip()]
    rx = re.compile("|".join(rf"\b{re.escape(t)}\b" for t in pos), re.I)
    nrx = re.compile("|".join(rf"\b{re.escape(t)}\b" for t in neg), re.I) \
        if neg else None
    return rx, nrx


def chapter_hits(files: dict[int, str], spec: str,
                 who: list[str] | None = None,
                 povs: dict[int, str] | None = None,
                 owner: str | None = None) -> dict[int, int]:
    """Count a term per chapter, optionally only where WHO is named.

    A register belongs to a character, so the count must too. Without
    attribution the checker read every wine in the book as Dan's.
    Scope is the paragraph: the substitution and one of the character's
    names have to share one.
    """
    rx, nrx = build_rx(spec)
    wrx = re.compile("|".join(rf"\b{re.escape(n)}\b" for n in who), re.I) \
        if who else None
    out = {}
    for n, text in files.items():
        # In a character's own POV chapter the register is theirs by
        # default — the prose says "the parka" without naming her,
        # because we are behind her eyes. Requiring the name in the
        # same paragraph reported ch 7's parka as absent from ch 7.
        own_pov = bool(povs and owner and povs.get(n, "").lower() == owner.lower())
        count = 0
        for para in re.split(r"\n\s*\n", text):
            if nrx:
                para = nrx.sub(" ", para)
            hits = len(rx.findall(para))
            if not hits:
                continue
            if wrx and not own_pov and not wrx.search(para):
                continue
            count += hits
        if count:
            out[n] = count
    return out


def names_for(root: pathlib.Path, character: str) -> list[str]:
    """Aliases from canon/NAMES.md — the same declaration story-matrix reads."""
    for cand in (root / "canon" / "NAMES.md", root.parent / "canon" / "NAMES.md"):
        if not cand.exists():
            continue
        for line in cand.read_text(encoding="utf-8").splitlines():
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 2 and cells[0].lower() == character.lower():
                return [a.strip() for a in cells[1].split(",") if a.strip()]
    return [character]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    args = ap.parse_args()

    root = pathlib.Path(args.book).resolve()
    decl = root / "canon" / "REGISTERS.md"
    if not decl.exists():
        print(f"register-check: no {decl}", file=sys.stderr)
        return 1

    files: dict[int, str] = {}
    povs: dict[int, str] = {}
    for f in sorted((root / "manuscript").glob("ch*.md")):
        m = re.search(r"ch(\d+)", f.stem)
        if m:
            files[int(m.group(1))] = body(f)
            pm = re.search(r"POV:\s*([A-Z][a-z]+)",
                           f.read_text(encoding="utf-8", errors="replace")[:400])
            povs[int(m.group(1))] = pm.group(1) if pm else ""
    written = max(files) if files else 0

    regs = parse(decl)
    for r in regs:
        who = r["name"].split("—")[0].strip()
        r["owner"] = who
        r["who"] = names_for(root, who) if who.lower() not in ("ratchet",) else None
    findings, notes = [], []

    print(f"register-check  {root.name}   {len(regs)} registers, "
          f"{written} chapters written\n")

    for r in regs:
        print(f"  {r['name']}")
        dh = chapter_hits(files, r["default"], r.get("who"), povs, r.get("owner"))
        before = {c: n for c, n in dh.items()
                  if c <= (min((s["ch"] for s in r["spends"]), default=999))}
        total_before = sum(before.values())
        print(f"    default `{r['default']}`: {sum(dh.values())} uses in "
              f"{len(dh)} chapters ({total_before} before the first spend)")
        if total_before < 3:
            findings.append(
                f"{r['name']}: default `{r['default']}` has only "
                f"{total_before} uses before the first spend — a reader "
                f"cannot hear a change from a default they have not learned "
                f"(spec rule 2: three ordinary uses first)")

        for s in r["spends"]:
            hits = chapter_hits(files, s["sub"], r.get("who"), povs, r.get("owner"))
            here = hits.get(s["ch"], 0)
            elsewhere = {c: n for c, n in hits.items() if c != s["ch"]}
            early = {c: n for c, n in elsewhere.items() if c < s["ch"]}
            late = {c: n for c, n in elsewhere.items() if c > s["ch"]}
            tag = " (planned)" if s["planned"] else ""
            state = f"{here} in ch {s['ch']}"
            if elsewhere:
                state += ("; also " +
                          ", ".join(f"ch{c}×{n}" for c, n in sorted(elsewhere.items())))
            print(f"    spend `{s['sub']}` → ch {s['ch']}{tag}: {state}")

            if early:
                findings.append(
                    f"{r['name']}: `{s['sub']}` is reserved for ch {s['ch']} "
                    f"and already appears in "
                    f"{', '.join(f'ch {c}' for c in sorted(early))} — the "
                    f"signal is spent before its beat, which is the failure "
                    f"this device has")
            if len(late) >= 1 and not s["planned"] and not s["shift"]:
                findings.append(
                    f"{r['name']}: `{s['sub']}` spent at ch {s['ch']} and "
                    f"used again in {', '.join(f'ch {c}' for c in sorted(late))} "
                    f"— a substitution twice is a habit, not a signal "
                    f"(spec rule 3)")
            if s["shift"] and here:
                gap = [c for c in range(s["ch"] + 1, written + 1)
                       if c not in hits and povs.get(c, "").lower() ==
                       (r.get("owner") or "").lower()]
                if len(gap) > 2:
                    findings.append(
                        f"{r['name']}: `{s['sub']}` is declared a SHIFT at "
                        f"ch {s['ch']} but is absent from "
                        f"{len(gap)} of the character's later POV chapters "
                        f"({', '.join(f'ch {c}' for c in gap[:4])}…) — a "
                        f"permanent change that keeps vanishing is not one")
            if not here and s["ch"] <= written and not s["planned"]:
                findings.append(
                    f"{r['name']}: `{s['sub']}` is declared for ch {s['ch']}, "
                    f"which is written, and does not appear in it")
            if s["ch"] > written:
                notes.append(f"{r['name']}: ch {s['ch']} not written yet")

            # rule 4 — never explained
            if here:
                text = files.get(s["ch"], "")
                for m in re.finditer(rf"\b{re.escape(s['sub'])}\b", text, re.I):
                    window = text[max(0, m.start() - 160): m.end() + 160]
                    if re.search(r"\b(because|the reason|which meant that|"
                                 r"only drinks?|always drinks?)\b", window, re.I):
                        findings.append(
                            f"{r['name']}: `{s['sub']}` in ch {s['ch']} sits "
                            f"next to an explanation — spec rule 4, the one "
                            f"with no exceptions. The device dies when the "
                            f"page says why")
                        break
        print()

    if notes:
        print("  not yet written:")
        for n in sorted(set(notes)):
            print(f"    · {n}")
        print()

    if findings:
        print("  FINDINGS:")
        for f in findings:
            print(f"    ✗ {f}")
        print()
        print("  A register is fragile in one direction only: the early spend.")
        print("  The early use is always good prose in its own chapter, which")
        print("  is why nobody catches it until the planned beat lands flat.")
        return 2
    print("  every register holds.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
