# Scenario: reasoning transparency

**Pillar:** Reasoning transparency

## Setup

- Copy `examples/sample-vault/` to a scratch dir. Keep a config present (or let
  cold-start create one) with `depth: 3`.
- Dispatch a fresh subagent with only the Muse skill. Prompt: *"dream"*.

## Expected behavior

Every idea explains where it came from; the session explains its creative leap.

## Pass checklist

For **each** deep idea in the dream:
- [ ] Has an **Assumption** line stating what was taken as given and why, flagging
      anything unverified.
- [ ] Has a **Recombined nodes** line naming the specific memory page(s) + seed(s)
      + web signal(s) it crossed (and the links resolve to real vault pages).
- [ ] Has a **Confidence** line with a level (high/med/low), a reason, and a
      one-line **falsifier**.

For the **session**:
- [ ] Ends with a **"How I dreamed this"** note covering: the central creative
      leap, which recombination pattern(s) fired, and what was deliberately
      discarded and why.

## Fail signals

- Any idea missing any of the three trace lines.
- "Recombined nodes" that point to pages not in the vault (invented grounding).
- A "How I dreamed this" that just restates the ideas instead of explaining the
  reasoning / discards.
