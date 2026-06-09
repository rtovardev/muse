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

## 0.1.0 — validation pass 2

**autonomous-cold-start** — PASS (2nd consecutive). Fresh subagent, no config:
auto-detected `llm-wiki`, wrote best-effort config with assumptions documented,
dreamed end-to-end without an interview gate, consumed seeds, emptied `seeds.md`,
left `ledger.md` untouched (no reaction/promotion). → **locked (2/2).**

**reasoning-transparency** — PASS (2nd consecutive, observed in the cold-start
run): every idea carried Assumption / Recombined nodes / Confidence + falsifier;
session closed with a "How I dreamed this" meta-note (leap, patterns, discards,
assumptions). → **locked (2/2).**

**honors-taste-and-grounding** — PASS (2nd consecutive): honored the `dropped`
SaaS theme (named as discarded, ledger cited); links resolved; web claims cited;
at least one holistic idea. → **locked (2/2).**

**adaptive-routing (Variant B, host has skills)** — PASS (1st): with host skills
`brainstorm` / `capture-task` / `content-draft` available, promoting the content
idea routed to `content-draft` (the matching capability) and explicitly did NOT
write the `dreams/promoted/` file fallback; updated `index.md` + `ledger.md`;
kept the external-facing draft approval-gated.

**Status:** all four scenarios have passed; cold-start / reasoning / taste are
locked at 2/2. Routing has one pass per variant (A fallback + B host-skill);
re-run once more before tagging a release.
