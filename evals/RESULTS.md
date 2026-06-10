# Eval Results

Append a block per validation run. Each is a fresh subagent with only the Muse
skill loaded, run against a scratch copy of `examples/sample-vault/`.

---

## 0.2.0 — pragmatic validation (2026-06-10)

One solid pass of each release-gate scenario before tagging `v0.2.0`. Each run was
a fresh subagent loaded with only the Muse skill, executed against a scratch copy
of `examples/sample-vault/`, then scored against the scenario checklist plus
`check_dream.py`. Web was disabled for determinism except `honors-taste-and-grounding`
(web on, to exercise sourcing). This is the pragmatic gate (1 pass each); the
strict 2x-consecutive gate remains the bar for a future hardening pass. Cold-start,
reasoning-transparency, and taste were already locked 2/2 in 0.1.0.

Scenarios already covered by 0.2.0 smoke runs (below): `autonomous-cold-start` (2
runs), `same-day-two-runs`, `privacy`, `scheduled-safe`, `adaptive-routing` A.

New passes this round (`check_dream.py` PASS + checklist verified by inspection):

- **reasoning-transparency** — PASS. All 3 ideas carry the full evidence trace
  (Assumption / Recombined nodes / Confidence+reason / Falsifier) under numbered
  `### N.` H3 headings; session closes with a "How I dreamed this" meta-note that
  explains the creative leap (not a restatement). All memory links resolve.
- **honors-taste-and-grounding** — PASS. Zero SaaS/software-product ideas; the
  dropped theme appears only as an explicit discard citing `dreams/ledger.md`.
  3 ideas grounded; every web claim carries a source URL (4 distinct URLs); ≥1
  holistic idea (solo-worker energy/time). No invented facts.
- **spanish-language** — PASS (2nd attempt; see note). Dream fully in Spanish,
  depth 2, full evidence trace, IDs `…-001-a/-001-b`, no setup interview. First
  attempt failed only on a self-inflicted idea-sequence slip (`002-b` instead of
  `001-b`); a fresh re-run produced correct sequences.
- **no-memory** — PASS. Auto-created config with `memory_profile: project-repo`,
  invented no vault/pages, flagged thin context, produced useful ideas from
  README + seed, offered (not performed) optional bootstrap.
- **web-disabled** — PASS. No web calls; every `Sources` line is `None; internal`;
  no time-sensitive web facts; verification pushed into first steps/falsifiers.
- **adaptive-routing — Variant B (host capability)** — PASS. Promoted idea routed
  to a visible host capability (`capture-task`) with a named reason; the
  `dreams/promoted/` file fallback was NOT used; index + ledger updated.
- **adaptive-routing — Variant C (explicit `build: file` route)** — PASS. Obeyed
  the config override and wrote the file fallback at
  `dreams/promoted/2026-06-09-001-audit-sprint-kit.md`; index + ledger updated.

Validator finding (fixed this round): the `spanish-language` run exposed that the
bilingual checker recognized Spanish idea-label aliases for presence but the
ID-extraction regex (`RE_ID_LABEL`) and one section heading were English-only. A
correctly-formed Spanish dream using `ID de idea` / `Acción para hoy` failed. Fixed
in `check_dream.py`; bundled sample and all 7 scenario dreams re-validate PASS.

---

## 0.2.0 — hardening validation

Status: pragmatic gate completed above (1 pass per scenario). This release adds new
release-gate scenarios and a lightweight structure checker. The strict gate (each
scenario twice consecutively) remains for a future hardening pass.

Initial static checks:
- `python3 evals/check_dream.py examples/sample-output/2025-01-15-001-dream.md` — PASS.
- `python3 -m py_compile evals/check_dream.py` — PASS.
- `git diff --check` — PASS.

Smoke eval notes:
- `autonomous-cold-start` first Codex subagent run produced a structurally valid
  dream and correct files, but exposed two instruction gaps: seed punctuation was
  normalized instead of copied exactly, and the final response did not offer
  config refinement. v0.2 instructions were tightened after this run.
- `autonomous-cold-start` second Codex subagent run — PASS: produced
  `dreams/2026-06-09-001-dream.md`, auto-configured, copied seeds exactly,
  cleared seeds after writes, updated index, and offered config refinement.
- `same-day-two-runs` smoke run — PASS: second run wrote
  `dreams/2026-06-09-002-dream.md`, preserved the first dream hash, used `002`
  idea IDs, copied the new seed exactly, and appended index rows.
- `privacy` smoke run — PASS: fake API key absent from all `dreams/` files,
  private client quote absent, redaction noted, checker passed.
- `scheduled-safe` smoke run — PASS: scheduled run wrote dream/index/run-log,
  cleared seeds after writes, created no promoted files, recorded no promotion,
  checker passed.
- `adaptive-routing` Variant A smoke run — PASS: selected decision idea routed to
  `dreams/decisions.md`, index state changed to `promoted`, ledger got a
  `promoted` entry, and no nonexistent host skill was claimed.

Required manual scenarios:
- autonomous-cold-start
- reasoning-transparency
- adaptive-routing variants A/B/C
- honors-taste-and-grounding
- spanish-language
- no-memory
- web-disabled
- same-day-two-runs
- scheduled-safe
- privacy

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
