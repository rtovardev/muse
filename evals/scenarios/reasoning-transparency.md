# Scenario: evidence transparency

**Pillar:** Evidence trace

## Setup

- Copy `examples/sample-vault/` to a scratch dir.
- Keep or create config with `depth: 3`.
- Dispatch a fresh subagent with only the Muse skill.
- Prompt: `dream`.

## Expected behavior

Every idea explains its evidence trail without exposing hidden chain-of-thought.
The session explains the creative leap.

## Pass checklist

For each deep idea:

- [ ] Has `Idea ID` using `muse-YYYYMMDD-NNN-{letter}`.
- [ ] Has `Assumption` stating what was taken as given and why.
- [ ] Has `Recombined nodes` naming specific memory pages, seeds, prior dreams,
      or web signals crossed.
- [ ] Has `Confidence` with high/medium/low and a reason.
- [ ] Has `Falsifier` with a concrete disconfirming observation.
- [ ] Memory paths/wikilinks resolve to real vault pages.
- [ ] Web claims, if any, carry source URLs.

For the session:

- [ ] Ends with `How I dreamed this` covering central creative leap,
      recombination pattern(s), deliberate discards, and assumptions.

## Fail signals

- Any idea missing one of the trace labels.
- Recombined nodes point to pages not in the vault.
- The meta-note merely restates the ideas instead of explaining the creative leap.
