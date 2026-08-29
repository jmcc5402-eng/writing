# Retro instrument — production telemetry (2026-08-29)

Computed by the orchestrator from git history, the variance LOG,
and the drafts directories (no agent run; mechanical counts).

## The book

- **Accepted length: 66,077 words** across ch 1–30 (correct the
  ~59k running estimate in older notes; the fold's CHANGELOG
  entry should carry this number).
- **93 candidate drafts** produced for 30 accepted chapters —
  3.1 drafts per accepted chapter once the blind-field conveyor
  stabilized (waves 3–8 ran exactly 12/12/12/12/12/6).
- **289 logged agent runs** end to end (2026-07-27 →
  2026-08-29) ≈ **9.6 runs per accepted chapter**, including
  every panel, sweep, fold, line pass, gate read, and
  instrument.

## The learning curve (runs and commits by day)

- Production tempo doubled across the run: early August ~3–6
  runs/day (setup, spytwins-era habits); the campus conveyor at
  full speed hit 27–43 runs/day (08-21/22, 08-28) with
  4-chapter waves closing in ~24 hours each.
- Wave cadence: wave 3 (08-21) → wave 8 (08-28/29): six waves,
  24 accepted chapters, eight days — including the author-gate
  latency on every wave PR. The conveyor itself was never the
  bottleneck after wave 3; the gate was, by design.
- The quiet stretch 08-24→08-27 (2 commits, 1 run) was the
  author's pause at PR #97 — the system held state at zero cost
  and resumed at full speed, which is the multi-thread/STATE.md
  discipline working.

## For the 1.2 wave plan

At demonstrated throughput, a 30-chapter book costs ~90 blind
drafts + ~200 instrument/production runs and runs gate-limited,
not capacity-limited: **six working days of conveyor + however
many mornings of author gates.** Recommendation: plan 1.2 as
8 waves of 4 (32 slots incl. buffer), same cadence, with the
retro's gate changes (brief audit; milestone fuzz at 10/20/30)
priced in — both are single-run additions per wave/milestone,
≈ +10 runs across the book.
