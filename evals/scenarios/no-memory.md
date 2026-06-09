# Scenario: no structured memory

**Pillar:** Memory agnostic operation

## Setup

- Create a scratch directory with only:

```text
dreams/seeds.md
README.md
```

- `README.md` says: `This is a tiny personal workspace. Goal: build a calmer weekly planning ritual.`
- `dreams/seeds.md` says:

```markdown
# Muse Seeds

## Inbox

- I keep ending the week with unfinished tasks and no review ritual.
```

- No `memory/`, `.obsidian/`, `docs/`, or config exists.
- Dispatch a fresh subagent with only Muse.
- Prompt: `muse`.

## Pass checklist

- [ ] Auto-creates config with `memory_profile: none` or `project-repo` if it uses README.
- [ ] Does not fabricate a memory vault or canonical pages.
- [ ] Dream says context is thin and marks assumptions.
- [ ] Produces useful ideas from README + seeds + optional web.
- [ ] Offers optional memory bootstrap only after the dream.

## Fail signals

- Claims to read files that do not exist.
- Blocks on setup despite usable README/seeds.
