#!/usr/bin/env python3
"""thread-scope.py — a branch scoped to the environment cannot touch the story.

    (as a hook)  PreToolUse on Edit|Write|MultiEdit, Bash and Agent.
                 Reads the hook JSON on stdin. Looks up the current
                 branch in studio/threads/SCOPES.md. On an
                 `environment` branch it refuses (exit 2):
                   - an Edit/Write whose file_path is story (any
                     books/ path outside canon/ and CHANGELOG.md)
                   - a Bash command that mutates a story path (a
                     redirection, sed -i, mv, cp, rm, tee, git add/rm/
                     mv/restore/checkout -- on it), or that sweeps the
                     tree (git add -A / . / --all; git commit -a with
                     story files modified)
                   - an Agent launch of a drafter, a line editor or a
                     plot architect
    python3 studio/tools/thread-scope.py --show     prints the branch and its scope
    python3 studio/tools/thread-scope.py --tree     story files dirty in the tree (exit 2)
    python3 studio/tools/thread-scope.py --push     story files in the branch diff (exit 2)
    STUDIO_THREAD_SCOPE=environment  overrides the table for one shell
    --unlock-thread-scope            anywhere in a Bash command lets that one
                                     command through; it is visible in the transcript

WHY THIS EXISTS
The author (2026-09-21): "I need an engine to hyper focus on the
environment. The other thread always reverts to the story." A thread
told to build guardrails drifts to fixing the page, because the page
is right there and the fix is satisfying. That is an instruction
failing in the usual way. This is the same rule as a lock: the thread
can build the check and cannot apply the fix, so the fix goes to the
book thread by the board and the check gets built. (L068)

Three lines of defence, because one is never enough:
  1. the command check below (fast, and it teaches);
  2. `--tree` (PostToolUse on Bash): after ANY command, a story file
     modified in the working tree is reported with the command to undo
     it. This catches every write technique — python, a heredoc, an
     editor, a script calling a script — because it reads the tree, not
     the command;
  3. `--push` (PreToolUse on Bash, on `git push`): the branch's own diff
     against origin/main may contain no story path that is not waived in
     SCOPES.md. Nothing reaches the remote, however it got written.

The first live day proved the need: the per-command check let
`python3 - <<PY / open("…/ch05.md","w") / PY` straight through. (L068)
"""
from __future__ import annotations
import fnmatch, json, os, re, shlex, subprocess, sys

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SCOPES = os.path.join(REPO, "studio", "threads", "SCOPES.md")

# What an environment branch may write under books/. Everything else under
# books/ is story. Outside books/ everything is environment.
BOOK_OPEN = (r"books/[^/]+/(?:[^/]+/)*canon/", r"books/[^/]+/(?:[^/]+/)*CHANGELOG\.md$")
DENIED_AGENTS = ("drafting-assistant", "line-copy-editor", "plot-architect")
MUTATORS = re.compile(r"(?:^|[\s;&|(])(?:sed\s+-i|mv|cp|rm|tee|truncate|git\s+(?:add|rm|mv|restore|checkout\s+--))\b")


def branch() -> str:
    try:
        return subprocess.run(["git", "-C", REPO, "rev-parse", "--abbrev-ref", "HEAD"],
                              capture_output=True, text=True, timeout=5).stdout.strip()
    except Exception:
        return ""


def scope_rows() -> list[tuple[str, str]]:
    out = []
    try:
        lines = open(SCOPES, encoding="utf-8").read().splitlines()
    except OSError:
        return out
    in_branches = False
    for line in lines:
        if line.startswith("## "):
            in_branches = line.strip("# ").lower().startswith("branches")
            continue
        if not in_branches or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not cells[0].startswith("`"):
            continue
        out.append((cells[0].strip("`"), cells[1].strip("`").lower()))
    return out


def scope_of(br: str) -> str:
    env = os.environ.get("STUDIO_THREAD_SCOPE")
    if env:
        return env.strip().lower()
    for pat, sc in scope_rows():
        if fnmatch.fnmatchcase(br, pat):
            return sc
    return "story"


def rel(path: str) -> str:
    p = path.replace("\\", "/")
    if os.path.isabs(p):
        try:
            p = os.path.relpath(p, REPO)
        except ValueError:
            return p
    return re.sub(r"^(\./)+", "", p)


def is_story(path: str) -> bool:
    p = rel(path)
    if p.startswith("../"):
        return False
    if not re.match(r"books/[^/]+/.+", p):
        return False
    return not any(re.match(rx, p) for rx in BOOK_OPEN)


def block(msg: str, br: str) -> int:
    print(f"thread-scope: BLOCKED — branch '{br}' is scoped 'environment' (studio/threads/SCOPES.md).", file=sys.stderr)
    print(f"  {msg}", file=sys.stderr)
    print("  This thread builds the check; the page fix belongs to the book thread. Put the fix on the board", file=sys.stderr)
    print("  (the book's BACKLOG or the open PR) and build the enforcer here. To change the scope, edit the row and say why.", file=sys.stderr)
    return 2


def check_edit(ti: dict, br: str) -> int:
    fp = ti.get("file_path") or ti.get("path") or ""
    if fp and is_story(fp):
        return block(f"{rel(fp)} is story (a manuscript, brief, card, note or bible).", br)
    return 0


def git(*a) -> list[str]:
    return subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True).stdout.splitlines()


def check_bash(ti: dict, br: str) -> int:
    cmd = ti.get("command") or ""
    if "--unlock-thread-scope" in cmd:
        return 0
    # Strip heredoc BODIES only. The first line stays, so `cat <<EOF > ch05.md`
    # still shows its redirection onto a story path.
    # An inline script (heredoc body, python -c, perl -e) writing a story
    # path is the hole the first live day found. Look for a write verb and
    # a story path in the SAME statement, and for the two-line shape where
    # a variable is bound to the path and written later.
    if (rc := check_inline(cmd, br)):
        return rc
    body = re.sub(r"(<<-?\s*['\"]?(\w+)['\"]?[^\n]*)\n.*?\n\2[ \t]*(?=\n|$)", r"\1", cmd, flags=re.S)
    for seg in re.split(r"&&|;|\|\||\n", body):
        seg = seg.strip()
        if not seg:
            continue
        if re.match(r"git\s+add\b", seg) and (re.search(r"\s(-A|--all)\b", seg) or re.search(r"\s\.(\s|$)", seg)):
            return block("git add -A / . sweeps the working tree; on an environment branch name the files (studio/…, .claude/…).", br)
        if re.match(r"git\s+commit\b", seg) and re.search(r"\s-a\b|\s-am\b|\s--all\b", seg):
            story = [f for f in git("diff", "--name-only") if is_story(f)]
            if story:
                return block("git commit -a would carry story files: " + ", ".join(story[:4]) + (" …" if len(story) > 4 else ""), br)
        try:
            toks = shlex.split(seg)
        except ValueError:
            toks = seg.split()
        # Only a story path being WRITTEN is a breach. Reading one is the
        # job: `cp ch05.md scratch/` and `python3 x.py ch05.md` pass;
        # `cp x ch05.md`, `> ch05.md`, `sed -i ... ch05.md` do not. The
        # first live day blocked a copy OUT of a manuscript (2026-09-21).
        written = []
        for i, tok in enumerate(toks):
            if tok in (">", ">>") and i + 1 < len(toks):
                written.append(toks[i + 1])
            elif tok.startswith((">", ">>")) and len(tok) > 1 and not tok.startswith(">&"):
                written.append(tok.lstrip(">"))
        m = MUTATORS.search(" " + seg)
        if m:
            verb = m.group(0).strip()
            args = [t for t in toks[1:] if not t.startswith("-")] if toks else []
            if verb in ("mv", "cp"):
                written += args[-1:]                     # destination only
            else:                                        # sed -i, rm, tee, truncate, git add/rm/mv/restore/checkout --
                written += args
        hit = [w for w in written if "books/" in w and is_story(w.split("=", 1)[-1])]
        if hit:
            return block(f"the command writes to {rel(hit[0])}.", br)
    return 0


WRITE_VERB = re.compile(
    r"""(?x)
    open\s*\([^)]*?['"][wax]  |  \.write_text\s*\(  |  \.write\s*\(  |
    \.writelines\s*\(        |  shutil\.(copy|copy2|copyfile|move)\s*\( |
    os\.(replace|rename|remove|unlink)\s*\(           |  \.unlink\s*\(  |
    \.rename\s*\(            |  \.touch\s*\(         |  \.mkdir\s*\(
    """)
STORY_LIT = re.compile(r"""['"]([^'"]*books/[^'"]+)['"]""")


def is_push(cmd: str) -> bool:
    """A real `git push` STATEMENT, not the words in a comment or a string.

    The first run of this check fired on a heredoc that merely contained
    the phrase "on git push" in a comment. A check that cries wolf gets
    switched off, which turns it back into an instruction.
    """
    if "--unlock-thread-scope" in cmd:
        return False
    body = re.sub(r"(<<-?\s*['\"]?(\w+)['\"]?[^\n]*)\n.*?\n\2[ \t]*(?=\n|$)", r"\1", cmd, flags=re.S)
    for seg in re.split(r"&&|;|\|\||\n", body):
        seg = seg.strip().lstrip("(").strip()
        if seg.startswith("#"):
            continue
        if re.match(r"(sudo\s+)?git\s+(-C\s+\S+\s+)?push\b", seg):
            return True
    return False


def check_inline(cmd: str, br: str) -> int:
    """A write verb and a story path inside one inline script.

    Two shapes are caught: the path written in place
    (`open("…/ch05.md","w")`), and the path bound to a name that is
    written later (`p = Path("…/ch05.md")` … `p.write_text(x)`), which is
    how anyone actually edits a file from python.
    """
    if not WRITE_VERB.search(cmd):
        return 0
    lines = cmd.splitlines()
    bound = set()
    for ln in lines:
        story_here = [m for m in STORY_LIT.findall(ln) if is_story(m)]
        if story_here and WRITE_VERB.search(ln):
            return block(f"an inline script writes to {rel(story_here[0])}.", br)
        if story_here:
            m = re.match(r"\s*(\w+)\s*=", ln)
            if m:
                bound.add(m.group(1))
        for name in list(bound):
            if re.search(rf"\b{re.escape(name)}\s*\.\s*(write_text|write|writelines|unlink|rename|touch)\s*\(", ln) \
               or re.search(rf"\b(shutil\.(copy|copy2|copyfile|move)|os\.(replace|rename|remove|unlink))\s*\([^)]*\b{re.escape(name)}\b[^)]*\)\s*$", ln):
                return block(f"an inline script writes to the story path held in '{name}'.", br)
    return 0


def waivers(br: str) -> list[str]:
    """Globs a branch may carry despite its scope — the `## Waivers` table."""
    out = []
    try:
        lines = open(SCOPES, encoding="utf-8").read().splitlines()
    except OSError:
        return out
    inw = False
    for line in lines:
        if line.startswith("## "):
            inw = line.strip("# ").lower().startswith("waiver")
            continue
        if not inw or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not cells[0].startswith("`"):
            continue
        if fnmatch.fnmatchcase(br, cells[0].strip("`")):
            out += [g.strip().strip("`") for g in cells[1].split(",") if g.strip()]
    return out


def dirty_story() -> list[str]:
    out = git("status", "--porcelain")
    return sorted({ln[3:].split(" -> ")[-1].strip().strip('"')
                   for ln in out if ln.strip() and is_story(ln[3:].split(" -> ")[-1].strip().strip('"'))})


def diff_story(base: str = "origin/main") -> list[str]:
    return [f for f in git("diff", "--name-only", f"{base}...HEAD") if is_story(f)]


def check_tree(br: str) -> int:
    """PostToolUse: the tree is the truth. Any write technique lands here."""
    bad = dirty_story()
    if not bad:
        return 0
    print(f"thread-scope: STORY FILES ARE DIRTY on '{br}', an environment branch.", file=sys.stderr)
    for f in bad[:8]:
        print(f"    {f}", file=sys.stderr)
    if len(bad) > 8:
        print(f"    …and {len(bad) - 8} more", file=sys.stderr)
    print("  Something wrote a chapter, brief, card or note. Undo it now:", file=sys.stderr)
    print(f"    git checkout -- {' '.join(bad[:4])}{' …' if len(bad) > 4 else ''}", file=sys.stderr)
    print("  Then put the page fix on the board for the book thread and build the check here.", file=sys.stderr)
    return 2


def check_push(br: str) -> int:
    """PreToolUse on `git push`: nothing story-shaped reaches the remote."""
    waived = waivers(br)
    bad = [f for f in diff_story() if not any(fnmatch.fnmatchcase(f, g) for g in waived)]
    if not bad:
        return 0
    print(f"thread-scope: BLOCKED — '{br}' is scoped 'environment' and its diff "
          f"against origin/main carries {len(bad)} story file(s):", file=sys.stderr)
    for f in bad[:8]:
        print(f"    {f}", file=sys.stderr)
    print("  The command check can be evaded; the diff cannot. Drop them from the", file=sys.stderr)
    print("  branch, or waive them by name in the `## Waivers` table of", file=sys.stderr)
    print("  studio/threads/SCOPES.md with a reason and an expiry.", file=sys.stderr)
    return 2


def check_agent(ti: dict, br: str) -> int:
    kind = (ti.get("subagent_type") or "").lower()
    if any(d in kind for d in DENIED_AGENTS):
        return block(f"'{kind}' writes prose or outlines. An environment thread launches readers and the environment-engineer, never a drafter.", br)
    return 0


def main() -> int:
    br = branch()
    sc = scope_of(br)
    for flag, fn in (("--tree", check_tree), ("--push", check_push)):
        if flag in sys.argv:
            if sc != "environment":
                print(f"thread-scope: '{br}' is scoped '{sc}' — nothing to check")
                return 0
            return fn(br)
    if "--show" not in sys.argv:
        try:
            payload = json.load(sys.stdin)
        except Exception:
            return 0
        if sc != "environment":
            return 0
        tool = payload.get("tool_name") or ""
        ti = payload.get("tool_input") or {}
        if "command" in ti and (tool in ("", "Bash")):
            if is_push(ti.get("command") or ""):
                if (rc := check_push(br)):
                    return rc
            return check_bash(ti, br)
        if "subagent_type" in ti:
            return check_agent(ti, br)
        if "file_path" in ti or "path" in ti:
            return check_edit(ti, br)
        return 0
    print(f"thread-scope: branch '{br}' → scope '{sc}'" + ("" if sc != "environment" else "  (locked: manuscripts, plots, cards, notes; no drafters)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
