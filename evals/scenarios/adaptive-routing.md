# Scenario: adaptive routing

**Pillar:** Adaptive routing

Run two variants to prove host-adaptivity.

## Variant A — bare environment fallback

### Setup

- Copy `examples/sample-vault/` to a scratch dir.
- No extra skills/capabilities are visible.
- Dispatch a fresh subagent with only Muse.
- Let it dream, then reply: `pursue idea 1` or the action-for-today idea.

### Pass checklist

- [ ] Identified the idea's intent: `discovery`, `build`, `decision`, `content`, or `task`.
- [ ] Since no host skill matches, used file fallback:
      - `dreams/promoted/` for discovery/build/content/task; or
      - `dreams/decisions.md` for decision.
- [ ] Updated the idea state in `dreams/index.md`.
- [ ] Appended a `promoted` outcome to `dreams/ledger.md`.
- [ ] Did not claim to invoke a skill/tool/command that was not visible.

## Variant B — host has visible capability

### Setup

- Same vault.
- The subagent's context lists available host skills/capabilities, including a
  plausible match such as `brainstorm`, `capture-task`, `decisions-log`, or
  `content-draft`.
- Dream, then reply: `pursue idea 1`.

### Pass checklist

- [ ] Mapped the intent to the matching visible capability and named why.
- [ ] Did not fall back to file when a real matching capability existed.
- [ ] If the idea hinged on date/price/deadline/availability, verified it on the
      web before routing.
- [ ] Updated index and ledger after routing.

## Variant C — explicit config route

### Setup

- Add to `dreams/muse-config.md`:

```markdown
- routes:
    build: file
```

- Pick a build idea.

### Pass checklist

- [ ] Obeyed explicit `build: file` even if a generic build skill might exist.
- [ ] Wrote fallback file and recorded outcome.

## Fail signals

- Stops at `Route: task` without executing anything.
- Invents a host skill.
- Ignores a configured route.
- Automatically promotes during scheduled mode.
