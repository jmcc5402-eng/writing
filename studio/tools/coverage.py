#!/usr/bin/env python3
"""coverage.py — which books the guardrails actually cover, and which
they silently do not.

    python3 studio/tools/coverage.py books
    python3 studio/tools/coverage.py books --names   # just the conforming ones

A guardrail suite that reports "all clear" on books it never opened is
worse than no suite. This repo has four manuscript layouts and only one
of them is the convention every checker requires.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import booklib as bl

target = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "books")
ok, skipped = bl.survey(target)
if "--names" in sys.argv:
    for b in ok:
        print(b.name)
    sys.exit(0)
print(f"  covering {len(ok)} book(s): " +
      (", ".join(b.name for b in ok) if ok else "NOTHING"))
for b, why in skipped:
    print(f"  NOT COVERED  {b.name}: {why}")
sys.exit(0)
