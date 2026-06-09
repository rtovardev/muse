# Scenario: same-day two runs

**Pillar:** Write safety / no overwrite

## Setup

- Copy `examples/sample-vault/` to a scratch dir.
- Run Muse once and let it write `dreams/YYYY-MM-DD-001-dream.md`.
- Add a new seed to `dreams/seeds.md`.
- Run Muse again on the same date.

## Pass checklist

- [ ] First run writes `dreams/YYYY-MM-DD-001-dream.md`.
- [ ] Second run writes `dreams/YYYY-MM-DD-002-dream.md` or next unused sequence.
- [ ] First dream file remains unchanged.
- [ ] Idea IDs use matching sequence numbers: `muse-YYYYMMDD-001-*`, then
      `muse-YYYYMMDD-002-*`.
- [ ] `dreams/index.md` contains rows for both runs.
- [ ] Seeds from the second run are copied into the second dream before clearing.

## Fail signals

- Second run overwrites the first dream.
- Idea IDs do not match the dream filename sequence.
