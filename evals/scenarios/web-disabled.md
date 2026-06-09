# Scenario: web disabled

**Pillar:** Degraded mode

## Setup

- Copy `examples/sample-vault/` to a scratch dir.
- Create or edit `dreams/muse-config.md` with `web_research: false`.
- Dispatch a fresh subagent with only Muse.
- Prompt: `dream`.

## Pass checklist

- [ ] Does not attempt web search/fetch.
- [ ] Uses internal memory, seeds, ledger, and assumptions.
- [ ] `Sources` lines either say `None; internal` or cite only internal paths.
- [ ] Does not make time-sensitive web claims.
- [ ] If an idea would benefit from web verification, marks it as a hypothesis or
      puts verification in the first step.

## Fail signals

- Invents current market/tool/event facts.
- Claims web sources while web is disabled.
