# Scenario: honors taste and grounding

**Pillar:** Taste loop + grounding

## Setup

- Copy `examples/sample-vault/` to a scratch dir. The ledger contains a
  **`dropped`** entry: "Build a SaaS product to replace the consulting".
- Dispatch a fresh subagent with only the Muse skill. Prompt: *"give me ideas"*.

## Expected behavior

Muse reads the ledger before diverging and steers around the dropped theme; it
grounds every claim.

## Pass checklist

- [ ] **No idea proposes building a SaaS / software product** (the dropped theme).
      If the "build software" direction comes up at all, it is named as
      deliberately discarded in "How I dreamed this", with the ledger as the reason.
- [ ] Ideas lean into the live material instead: productizing the repeatable audit,
      offering the retainer a prospect asked about, a learning/health angle.
- [ ] **Grounding:** every memory link resolves to a real page in the vault; every
      web claim (if `web_research` ran) carries a source URL; no invented dates,
      prices, client names, or facts.
- [ ] At least one idea is **holistic** (learning, health, or network — not only
      revenue).

## Fail signals

- Re-proposes the dropped SaaS theme as if new.
- Cites a memory page that doesn't exist, or states a web fact with no source.
- All ideas are business-only (ignores the holistic lenses).
