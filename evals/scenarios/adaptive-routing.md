# Scenario: adaptive routing

**Pillar:** Adaptive routing

Run in two variants to prove host-adaptivity.

## Variant A — bare environment (fallback)

### Setup
- Copy `examples/sample-vault/` to a scratch dir. No extra skills available.
- Dispatch a fresh subagent with only the Muse skill. Let it dream, then reply:
  *"pursue idea 1"* (or whichever it marked as the action for today).

### Pass checklist
- [ ] Identified the idea's **intent** (discovery / build / decision / content / task).
- [ ] Since no host skill matches, used the **file fallback**: wrote a file under
      `dreams/promoted/` (or `dreams/decisions.md` for a decision) with the scoped
      next action / open questions / draft.
- [ ] Updated the idea's state in `dreams/index.md` and appended a `promoted`
      outcome to `dreams/ledger.md`.
- [ ] Did NOT claim to have invoked a skill that doesn't exist.

## Variant B — host has skills (route to them)

### Setup
- Same vault, but the subagent's context lists available host skills, including a
  plausible match (e.g. a `brainstorm` or `capture-task` skill).
- Dream, then reply: *"pursue idea 1"*.

### Pass checklist
- [ ] Mapped the intent to the **matching host skill** and routed to it (named the
      skill it chose and why).
- [ ] Did not fall back to a file when a real capability existed.
- [ ] If the idea hinged on a date/price/deadline, **verified it on the web before
      routing**.

## Fail signals

- Stops at a label ("Route: task") without executing anything.
- Invents a host skill, or ignores a present one and writes a file anyway.
