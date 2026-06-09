# Muse — Design

The design contract for Muse, an autonomous, memory-agnostic ideation skill for
agentic coding assistants (Claude Code, Codex, and compatible runtimes).

## Thesis

Most ideation tools take a topic and brainstorm it. Muse takes the user's
**accumulated memory + live web signals** and *dreams* from it: it recombines
distant nodes into non-obvious ideas, names blind spots, and surfaces what the
user is not seeing — then curates a few deep, actionable ideas, **explains its
own reasoning**, and routes the chosen one into whatever workflow the host has.

Muse should feel like a sharp partner actively developing the person, not a list
generator. The bar: "I noticed you're running X — here's a non-obvious move, and
here's exactly why I dreamt it."

## What "publishable + generalist" requires

The skill must run for anyone, on any memory layout, in any host environment,
with zero hardcoded references to one person, company, or repo.

1. **Memory-agnostic.** Adapts to a Karpathy-style LLM-Wiki, an arbitrary
   markdown vault, or no structured memory at all (which it can bootstrap).
2. **Self-configuring.** Detects what exists and writes its own config. The
   first-run interview is *optional*, not a gate.
3. **Host-adaptive routing.** It does not assume the host has any particular
   skills. It discovers what the environment offers and routes to it, with a
   generic file-based fallback that always closes the loop.
4. **Language-agnostic output.** Generates in the user's configured language.
5. **No personal leakage.** Examples use a neutral illustrative persona, clearly
   marked. Dev history lives in `CHANGELOG.md`, not in the skill body.

## The four pillars

### 1. Autonomy (emulate dreaming without being woken)

Muse runs end-to-end on its own. When config or context is missing, it
**auto-detects what it can and assumes sensible defaults**, recording every
assumption in the dream so the user can see and correct them. It never stalls
waiting for input it can reasonably infer.

Defaults when unconfigured:

| Setting | Auto-detected from | Fallback default |
|---|---|---|
| `language` | recent user text / repo locale | English |
| `memory_profile` | presence of `wiki/`, `.obsidian/`, `notes/`… | `none` → offer bootstrap, else dream from goals only |
| `memory_paths` | detected vault root | the directory it was invoked in |
| `lenses` | — | the default holistic lens set |
| `depth` | — | 3 |
| `web_research` | network availability | `true` |
| `divergence` | — | `balanced` |

### 2. Reasoning transparency (explain why it assumed / chose)

Every idea carries an explicit reasoning trace:

- **Assumption** — what Muse took as given and *why* (especially anything it
  could not verify).
- **Recombined nodes** — the specific memory pages + web signals it crossed to
  reach this idea. This is the "where the dream came from."
- **Confidence** — high / medium / low, with the reason, plus a one-line
  **falsifier** ("what would prove this wrong").

Every session ends with a **"How I dreamed this"** meta-note: the creative leap
of the session, which patterns fired, what was deliberately discarded and why.
This is the skill explaining its dream the way a person recounts one.

### 3. Adaptive routing (fit any workflow)

When the user picks an idea, Muse executes a route rather than just labelling it.
It maps the idea to one of five **intents** and resolves each intent to a host
capability discovered at runtime:

| Intent | Resolves to (if present) | Generic fallback |
|---|---|---|
| discovery | a brainstorming/interview skill | write open questions to `dreams/promoted/` |
| build | an automation/shipping skill | write a scoped build note |
| decision | a decisions log | append to `dreams/decisions.md` |
| content | a content/drafting skill | write a draft, marked draft-first |
| task | a task/capture skill or tracker | write an actionable task file |

The fallback guarantees the loop always closes, even in a bare environment.

### 4. Taste (get better over time)

A per-user append-only ledger records reactions (`liked`/`shipped`/`dropped`/
`meh`) and executed-route outcomes (`promoted`). Muse reads it every run: never
re-proposes a dropped theme, evolves shipped ideas, leans into liked patterns.

## New features beyond parity

- **Divergence dial** (`grounded` | `balanced` | `wild`) — how far recombination
  reaches. Emulates dream depth. Grounded = adjacent moves; wild = forced
  cross-domain mashups.
- **Recurring threads** — a reflection pass over recent dreams: ideas that keep
  resurfacing are flagged as signal (a "recurring dream"), and shipped/decided
  ideas are checked for follow-through instead of being re-proposed.
- **Falsifier per idea** — folded into confidence; forces honest, checkable
  claims instead of plausible-sounding ones.

## Non-goals (YAGNI)

- Not a research report generator (that's a deep-research tool).
- Not a single-plan stress-tester (that's an interview/brainstorm tool).
- No runtime scripts — instruction-only for maximum portability.
- No host-specific integrations baked in; everything is discovered or falls back.

## Repo layout

```
muse/
  skills/muse/SKILL.md            # the skill contract (import-compatible path)
  skills/muse/references/runbook.md  # the method (deep reference)
  examples/sample-vault/          # a tiny neutral memory vault for tests/demos
  evals/                          # application scenarios for iteration
  README.md  DESIGN.md  CHANGELOG.md  LICENSE
```

`skills/muse/SKILL.md` matches the `npx skills` import convention so any host
repo can pin it via a lockfile, or consume it via git submodule / symlink.
