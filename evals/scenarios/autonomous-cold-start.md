# Scenario: autonomous cold start

**Pillar:** Autonomy

## Setup

- Copy `examples/sample-vault/` to a scratch dir.
- Delete `dreams/muse-config.md` if present. There must be no config.
- The vault has memory (`memory/wiki/`), seeds, and a ledger, but no Muse config.
- Dispatch a fresh subagent with only the Muse skill loaded.
- Prompt: `muse`.
- Working directory = scratch vault.

## Expected behavior

Muse should not stop to interview the user. It should auto-detect, write config,
run the dream cycle, and log assumptions.

## Pass checklist

- [ ] Produced `dreams/YYYY-MM-DD-NNN-dream.md` without asking setup questions first.
- [ ] Created `dreams/muse-config.md` with detected `llm-wiki`, English language,
      default depth/divergence, and `mode: interactive`.
- [ ] Created missing support files if needed: `index.md`, `run-log.md`, `promoted/`.
- [ ] Dream explicitly lists assumptions made because config was missing.
- [ ] Consumed the two seeds and copied them verbatim into the dream.
- [ ] Emptied `dreams/seeds.md` only after writing the dream and index.
- [ ] Offered to refine config after dreaming, not before.

## Fail signals

- Asked the user to choose language/memory/lenses before producing anything.
- Produced a dream but silently omitted assumptions.
- Used wrong memory paths it could have detected.
- Wrote `dreams/{date}-dream.md` instead of the non-overwriting sequence format.
