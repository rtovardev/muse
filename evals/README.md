# Muse Evals

Application scenarios for iterating on Muse. Each scenario is run by dispatching a
**fresh subagent** that has *only* the Muse skill loaded (no prior conversation),
pointed at a copy of `examples/sample-vault/`, then scored against a rubric.

This is test-driven skill development: the skill is the "production code", these
scenarios are the "tests". A change to `SKILL.md` or `runbook.md` should keep all
scenarios passing.

## How to run one

1. Copy `examples/sample-vault/` to a scratch directory (so the run can write to
   `dreams/`).
2. Dispatch a subagent whose context is: the Muse `SKILL.md` + `runbook.md`, the
   scenario's setup, and "the working directory is the scratch vault".
3. Let it produce `dreams/{date}-dream.md`.
4. Score the output against the scenario's checklist. All boxes = pass.

A scenario passes when it satisfies its checklist on two consecutive runs (runs
are non-deterministic; one pass can be luck).

## Scenarios

| File | Pillar exercised | What it proves |
|---|---|---|
| `scenarios/autonomous-cold-start.md` | Autonomy | Runs with no config; detects, defaults, and logs assumptions. |
| `scenarios/reasoning-transparency.md` | Reasoning | Every idea has a trace; session has a "How I dreamed this" note. |
| `scenarios/adaptive-routing.md` | Routing | Routes via host skills when present; falls back to files when not. |
| `scenarios/honors-taste-and-grounding.md` | Taste + grounding | Honors the dropped theme; no invented facts; links resolve. |

## Scoring notes

- **Grounding is pass/fail.** A single invented fact (a date, a price, a memory
  page that doesn't exist) fails the run regardless of idea quality.
- **Reasoning is pass/fail.** An idea without its Assumption/Recombined-nodes/
  Confidence trace fails the run.
- Idea *quality* (divergence, insight) is scored 1-5 and tracked over iterations,
  but the pillars above are gates.
