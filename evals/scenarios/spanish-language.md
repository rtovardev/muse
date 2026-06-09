# Scenario: Spanish language

**Pillar:** Language adaptation

## Setup

- Copy `examples/sample-vault/` to a scratch dir.
- Create or edit `dreams/muse-config.md`:

```markdown
# Muse Config

- language: Spanish
- mode: interactive
- memory_profile: llm-wiki
- memory_paths:
    - memory/wiki/index.md
- depth: 2
- web_research: false
- divergence: balanced
```

- Dispatch a fresh subagent with only Muse.
- Prompt in Spanish: `muse, dame ideas`.

## Pass checklist

- [ ] Dream file is written in Spanish.
- [ ] Headings may remain recognizable, but content is Spanish and not mixed.
- [ ] Ideas still include `Idea ID`, `Assumption`, `Recombined nodes`,
      `Confidence`, and `Falsifier` labels or clear Spanish equivalents.
- [ ] Index is updated.
- [ ] No setup interview is required.

## Fail signals

- Dream is mostly English.
- Missing evidence trace because of translation.
