# Scenario: autonomous cold start

**Pillar:** Autonomy

## Setup

- Copy `examples/sample-vault/` to a scratch dir. **Delete `dreams/muse-config.md`
  if present** — there must be no config.
- The vault has memory (`memory/wiki/`), seeds, and a ledger, but no Muse config.
- Dispatch a fresh subagent with only the Muse skill loaded. Prompt: *"muse"*.
  Working directory = the scratch vault. No other instructions.

## Expected behavior

Muse should NOT stop to interview the user. It should auto-detect and dream.

## Pass checklist

- [ ] Produced `dreams/{date}-dream.md` without asking setup questions first.
- [ ] Created a best-effort `dreams/muse-config.md` (detected `llm-wiki` from
      `memory/wiki/` + `log.md`; language English).
- [ ] The dream's "How I dreamed this" (or an assumptions note) **explicitly lists
      the assumptions it made** because there was no config (e.g. chosen language,
      detected profile, default depth/divergence/web).
- [ ] Consumed the two seeds (retainer question, productized-consulting newsletter)
      and emptied `dreams/seeds.md`.
- [ ] Offered to refine the config *after* dreaming, not before.

## Fail signals

- Asked the user to choose language / memory / lenses before producing anything.
- Produced a dream but silently — no record of what it assumed.
- Invented a config value it could have detected (e.g. wrong memory paths).
