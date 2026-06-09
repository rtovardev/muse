# Eval Results

Append a block per validation run. Each is a fresh subagent with only the Muse
skill loaded, run against a scratch copy of `examples/sample-vault/`.

---

## 0.1.0 — initial validation

**autonomous-cold-start** — PASS
- No config present. Did not stop to interview; auto-wrote `muse-config.md`
  (detected `llm-wiki`, real paths, goals lifted verbatim, every assumption
  documented in a comment block). Dreamed end-to-end, consumed both seeds,
  emptied `seeds.md`. "How I dreamed this" listed the cold-start assumptions.

**reasoning-transparency** — PASS (observed within the cold-start run)
- Every deep idea carried Assumption / Recombined nodes / Confidence + falsifier.
  Session closed with a "How I dreamed this" meta-note covering the creative leap,
  patterns fired, and deliberate discards.

**honors-taste-and-grounding** — PASS (observed within the cold-start run)
- Honored the `dropped` SaaS theme (named as discarded, ledger cited as reason);
  zero software-product ideas. All four memory wikilinks resolved to real vault
  pages; web claims carried sources; no invented facts. At least one holistic idea.

**adaptive-routing (Variant A, fallback)** — PASS
- Promoting idea 1 in a bare environment: identified `decision` intent, used the
  `dreams/decisions.md` file fallback, updated the `index.md` row and appended a
  `promoted` outcome to `ledger.md`, and did not claim any nonexistent host skill.

**adaptive-routing (Variant B, host has skills)** — not yet run.

Notes: the rubric asks for two consecutive passes per scenario before a scenario
is considered locked; the runs above are the first pass. Re-run before each
release.
