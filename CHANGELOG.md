# Changelog

All notable changes to Muse are documented here.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/).

## [0.2.0] — Operational hardening

### Added
- **Dream layer framing.** Clarified that Muse is independent and adapts to the
  user's existing environment instead of imposing a memory architecture.
- **Internal memory discipline.** Documented Karpathy-style source/reflection
  separation, source hierarchy, assumptions, and consent-gated fact promotion.
- **Dream cycle.** Added Wake → Consolidate → REM divergence → Reality check →
  Morning note → Integration as the operating loop.
- **Non-overwriting dream filenames.** Dream files now use
  `dreams/YYYY-MM-DD-NNN-dream.md` and idea IDs use matching sequences.
- **Scheduled mode.** Added cron-safe/draft-only behavior and `dreams/run-log.md`.
- **Index schema.** Formalized `dreams/index.md` rows and idea states.
- **Write-safe seeds lifecycle.** Seeds are copied into the dream before clearing;
  failures leave seeds untouched.
- **Deterministic routing.** Added explicit `routes:` config, visible-capability
  resolution, and file fallback rules.
- **Memory proposals.** Added `dreams/memory-proposals.md` as a safe holding area
  for facts/patterns Muse suggests promoting to canonical memory.
- **Privacy guidance.** Added `SECURITY.md`, `.gitignore.example`, and redaction
  rules for sensitive dream data.
- **Compatibility and limitations.** Added environment matrix and known limits to
  the README.
- **Expanded eval scenarios.** Added Spanish, no-memory, web-disabled,
  same-day-two-runs, scheduled-safe, and privacy scenarios.
- **Lightweight checker.** Added `evals/check_dream.py` for structural validation.
  The checker is bilingual (English/Spanish labels and section headings) and also
  enforces that `Confidence` starts with `high`/`medium`/`low` (no numeric scores)
  and that `More sparks` stays one-line leftovers (no idea IDs or evidence traces).
- **Sample output.** Added a complete sample dream under `examples/sample-output/`.
- **Continuous integration.** Added `.github/workflows/validate.yml` to compile
  the checker and validate the sample dream on every push and pull request.
- **Quickstart.** Added a short "see it run" walkthrough to the README using the
  bundled sample vault.

### Changed
- Reframed reasoning transparency as an auditable **evidence trace** instead of
  hidden chain-of-thought.
- Expanded memory profiles to `llm-wiki`, `markdown-vault`, `project-repo`,
  `agent-workspace`, `host-native`, `bootstrapped`, and `none`.
- Clarified the dream-file contract: ideas use numbered `### N. Name` H3 headings
  (never `Idea ID` as the heading), confidence is `high`/`medium`/`low` rather
  than a numeric score, and `More sparks` are one-line leftovers only.
- Updated skill metadata version to `0.2.0`.

## [0.1.0] — Initial generalist release

First public, generalist release. Muse began as a personal ideation skill inside
one operating system and was rebuilt to be portable and publishable for anyone.

### Added
- **Autonomy.** Runs end-to-end. When config or context is missing, it
  auto-detects what it can, assumes sensible defaults, and records every
  assumption in the dream. The setup interview is now optional, not a gate.
- **Reasoning transparency.** Every idea carries a trace — `Assumption`,
  `Recombined nodes`, `Confidence` (with a falsifier). Every session closes with
  a "How I dreamed this" meta-note explaining the creative leap.
- **Adaptive routing.** The chosen idea maps to one of five intents (discovery,
  build, decision, content, task) and resolves to a host capability discovered at
  runtime, with a file-based fallback so the loop always closes. No host skills
  are assumed.
- **Divergence dial** (`grounded` | `balanced` | `wild`) controlling how far
  recombination reaches.
- **Recurring threads** reflection pass: a repeating idea is treated as a signal,
  and shipped/decided ideas are checked for follow-through instead of re-proposed.
- **`none` memory profile** for users with no structured memory who decline a
  bootstrap.
- **README, DESIGN, evals harness, and a neutral sample vault** for installation,
  understanding, and iteration.

### Changed
- Genericized all examples to a neutral illustrative persona.
- Promotion routes are now host-agnostic intents instead of hardcoded skill names.

### Removed
- Personal/operator-specific content: private examples, internal dev iteration
  log, and assistant-runtime scheduling specifics (replaced by a generic
  "Running on a schedule" note).
