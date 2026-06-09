# Contributing to Muse

Muse is an instruction-only skill. Changes should improve portability, autonomy,
grounding, privacy, routing, or dream quality without adding host lock-in.

## Principles

- Keep Muse independent and environment-adaptive.
- Do not hardcode a person, company, repo, assistant, or workflow.
- Do not require a specific memory architecture.
- Keep canonical memory separate from generated dream memory.
- Prefer markdown contracts and behavioral evals over runtime dependencies.
- Preserve privacy and scheduled-run safety.

## Before opening a PR

1. Update `skills/muse/SKILL.md` for behavior changes.
2. Update `skills/muse/references/runbook.md` for method/schema changes.
3. Update `README.md` and `DESIGN.md` if the public contract changes.
4. Add or update an eval scenario under `evals/scenarios/`.
5. Run the lightweight checker on sample outputs:

```bash
python3 evals/check_dream.py examples/sample-output/2025-01-15-001-dream.md
```

6. Record manual eval results in `evals/RESULTS.md` when applicable.

## Release checklist

- [ ] All release-gate scenarios pass twice consecutively.
- [ ] No personal/private context is hardcoded.
- [ ] No broken local markdown links.
- [ ] Changelog updated.
- [ ] Skill metadata version updated.
- [ ] README install instructions still work.
