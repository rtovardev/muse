# Changelog

All notable changes to Muse are documented here.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/).

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
