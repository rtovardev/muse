# Scenario: honors taste and grounding

**Pillar:** Taste loop + grounding

## Setup

- Copy `examples/sample-vault/` to a scratch dir.
- The ledger contains a `dropped` entry: "Build a SaaS product to replace the consulting".
- Dispatch a fresh subagent with only Muse.
- Prompt: `give me ideas`.

## Expected behavior

Muse reads the ledger before diverging, steers around dropped themes, and grounds
every claim.

## Pass checklist

- [ ] No deep idea proposes building a SaaS/software product.
- [ ] If the SaaS direction appears, it is only named as deliberately discarded in
      `How I dreamed this`, with the ledger as reason.
- [ ] Ideas lean into live material: productized audit, retainer seed, learning,
      health, network, or energy.
- [ ] Every memory link/path resolves to a real vault page.
- [ ] Every web claim carries a source URL.
- [ ] No invented dates, prices, client names, or facts.
- [ ] At least one idea is holistic, not only revenue.

## Fail signals

- Re-proposes the dropped SaaS theme as if new.
- Cites a memory page that does not exist.
- States a web fact with no source.
- All ideas are business-only despite default holistic lenses.
