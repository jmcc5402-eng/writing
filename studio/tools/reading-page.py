#!/usr/bin/env python3
"""Generate a phone-friendly reading page from a Markdown doc.

House rule (PR-WORKFLOW, reading-page rule): any author read longer
than ~a page ships as a black-on-white single-theme HTML page,
published as a private artifact and linked in the PR body. This is
the generator. Usage:

    python3 studio/tools/reading-page.py INPUT.md OUTPUT.html \
        "Page Title" "subtitle line" [commit-hash]

Deliberately minimal Markdown: #/##/### headings, - bullets, tables,
> quotes, **bold**, *italic*, `code`, --- rules. Everything else is a
paragraph. Single-theme black-on-white per the author's ruling.
"""
import html
import re
import sys


def inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


def convert(md):
    out, lines = [], md.splitlines()
    i, para, ul, table, quote = 0, [], False, [], []

    def flush_para():
        nonlocal para
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para = []

    def flush_ul():
        nonlocal ul
        if ul:
            out.append("</ul>")
            ul = False

    def flush_table():
        nonlocal table
        if table:
            rows = [r for r in table if not re.match(r"^[\s|:-]+$", r)]
            out.append('<div class="tw"><table>')
            for n, r in enumerate(rows):
                cells = [c.strip() for c in r.strip().strip("|").split("|")]
                tag = "th" if n == 0 else "td"
                out.append(
                    "<tr>"
                    + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells)
                    + "</tr>"
                )
            out.append("</table></div>")
            table = []

    def flush_quote():
        nonlocal quote
        if quote:
            out.append(
                "<blockquote><p>" + inline(" ".join(quote)) + "</p></blockquote>"
            )
            quote = []

    def flush_all():
        flush_para(), flush_ul(), flush_table(), flush_quote()

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if s.startswith("|"):
            flush_para(), flush_ul(), flush_quote()
            table.append(s)
        elif s.startswith(">"):
            flush_para(), flush_ul(), flush_table()
            quote.append(s.lstrip("> "))
        elif m := re.match(r"^(#{1,4})\s+(.*)", s):
            flush_all()
            n = min(len(m.group(1)) + 1, 5)
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
        elif s.startswith(("- ", "* ")):
            flush_para(), flush_table(), flush_quote()
            if not ul:
                out.append("<ul>")
                ul = True
            out.append("<li>" + inline(s[2:]) + "</li>")
        elif ul and s and ln.startswith(("  ", "\t")):
            out[-1] = out[-1][:-5] + " " + inline(s) + "</li>"
        elif s in ("---", "***"):
            flush_all()
            out.append('<div class="rule">&#8226;&nbsp;&nbsp;&#8226;&nbsp;&nbsp;&#8226;</div>')
        elif not s:
            flush_all()
        else:
            flush_ul(), flush_table(), flush_quote()
            para.append(s)
        i += 1
    flush_all()
    return "\n".join(out)


SHELL = """<title>{title}</title>
<style>
/* Single-theme by author ruling: always black on white. */
:root, :root[data-theme="dark"], :root[data-theme="light"]{{
  --paper:#FFF; --ink:#111; --muted:#55606A; --accent:#0E7C7B;
  --rule:#E2DFD6; }}
html{{ background:#FFF !important; color-scheme: light; }}
body{{ margin:0; background:#FFF; color:#111;
  font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
  font-size:1.075rem; line-height:1.7; }}
.wrap{{ max-width:65ch; margin:0 auto; padding:2rem 1.15rem 5rem; }}
.sub{{ color:var(--muted); font-family:system-ui,sans-serif;
  font-size:.82rem; text-transform:uppercase; letter-spacing:.08em; }}
h1{{ font-size:1.7rem; line-height:1.25; margin:.2rem 0 1rem; }}
h2{{ font-size:1.35rem; margin:2.2rem 0 .8rem; }}
h3{{ font-size:1.15rem; margin:1.8rem 0 .6rem; }}
h4,h5{{ font-size:1rem; margin:1.4rem 0 .5rem; }}
p{{ margin:0 0 1rem; }} ul{{ margin:0 0 1rem 1.2rem; padding:0; }}
li{{ margin:0 0 .45rem; }}
blockquote{{ margin:1rem 0; padding:.2rem 0 .2rem .9rem;
  border-left:3px solid var(--accent); color:#333; }}
code{{ font-family:ui-monospace,monospace; font-size:.9em;
  background:#F4F2EC; padding:0 .25em; border-radius:3px; }}
.tw{{ overflow-x:auto; margin:0 0 1rem; }}
table{{ border-collapse:collapse; font-size:.92rem;
  font-family:system-ui,sans-serif; }}
th,td{{ border:1px solid var(--rule); padding:.4rem .6rem;
  text-align:left; vertical-align:top; }}
th{{ background:#F7F5EF; }}
.rule{{ text-align:center; color:var(--muted); letter-spacing:.4em;
  margin:1.6rem 0; font-size:.8rem; }}
.stamp{{ margin-top:3rem; padding-top:1rem; border-top:1px solid
  var(--rule); color:var(--muted); font-family:system-ui,sans-serif;
  font-size:.78rem; }}
</style>
<div class="wrap">
<div class="sub">{subtitle}</div>
<h1>{title}</h1>
{body}
<div class="stamp">Generated from the committed text{stamp}. The PR
is the source of truth; this page is the reading lens.</div>
</div>
"""


def main():
    src, dst, title = sys.argv[1], sys.argv[2], sys.argv[3]
    subtitle = sys.argv[4] if len(sys.argv) > 4 else "Studio reading page"
    commit = sys.argv[5] if len(sys.argv) > 5 else ""
    md = open(src).read()
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    stamp = f" at commit {commit}" if commit else ""
    page = SHELL.format(
        title=html.escape(title),
        subtitle=html.escape(subtitle),
        body=convert(md),
        stamp=stamp,
    )
    open(dst, "w").write(page)
    print(f"wrote {dst} ({len(page)} bytes)")


if __name__ == "__main__":
    main()
