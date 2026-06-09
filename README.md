# Muse

**An autonomous, memory-agnostic ideation skill for agentic coding assistants.**

Most ideation tools take a topic and brainstorm it. Muse takes *your accumulated
memory + live web signals* and **dreams** from it — it recombines distant ideas
into non-obvious ones, names the blind spots you can't see, **explains its own
reasoning**, and routes the winner into whatever workflow you already have.

It is designed to feel like a sharp partner actively helping you develop, not a
list generator. The bar: *"I noticed you're running X — here's a non-obvious
move, and here's exactly why I dreamt it."*

Works with Claude Code, Codex, and compatible runtimes. No runtime scripts — it's
instruction-only, so it's fully portable.

## What it does

- **Dreams across your whole life** — work, learning, health, network, money,
  positioning. Not just a business tool.
- **Scans the live web** for external signals (tools, courses, events, trends)
  and ties them to what you're doing *right now*. Every web claim is cited.
- **Explains itself.** Every idea shows what it assumed, which memory + web nodes
  it recombined, how confident it is, and what would prove it wrong. Every
  session ends with a "How I dreamed this" note.
- **Runs autonomously.** No config? It detects what it can, assumes sensible
  defaults, and records every assumption in the dream so you can correct it.
- **Adapts to any memory** — a Karpathy-style LLM-Wiki, any markdown vault, or
  nothing at all (it can bootstrap one).
- **Fits any workflow.** It discovers the skills your host already has and routes
  ideas into them; if it finds none, it falls back to files so the loop always
  closes.
- **Learns your taste** over time via an append-only ledger.

## The four pillars

| Pillar | What it means |
|---|---|
| **Autonomy** | Runs end-to-end. Missing context → detect + default + log the assumption. |
| **Reasoning transparency** | Per-idea trace (assumption / recombined nodes / confidence + falsifier) and a session "How I dreamed this" meta-note. |
| **Adaptive routing** | Maps the chosen idea to one of five intents and resolves each to a host capability, with a file fallback. |
| **Taste** | A ledger of liked / shipped / dropped / promoted that steers every future run. |

Plus: a **divergence dial** (`grounded` → `wild`) for how far it reaches, and a
**recurring-threads** pass that treats a repeating idea as a signal.

See [`DESIGN.md`](DESIGN.md) for the full contract.

## Install

Muse is a standard skill: a folder with a `SKILL.md`.

**Option A — drop it in.** Copy `skills/muse/` into your assistant's skills
directory (`.claude/skills/` for Claude Code, `~/.agents/skills/` for Codex), so
you have `.../skills/muse/SKILL.md`.

**Option B — git submodule** (recommended if you want to keep iterating and pull
updates):

```bash
git submodule add https://github.com/rtovardev/muse vendor/muse
ln -s ../../vendor/muse/skills/muse .claude/skills/muse
```

**Option C — lockfile import.** The `skills/muse/SKILL.md` path is compatible
with `npx skills`-style importers; pin it from `rtovardev/muse`.

Per-user data (your config, dreams, and taste ledger) lives in a `dreams/` folder
in your own workspace — never in the skill. The skill and your data stay separate,
so you can update one without touching the other.

## First run

Just invoke it:

```
/muse
```

or say *"muse"*, *"dream"*, *"give me ideas"*, *"what am I missing"*. On the first
run with no config, Muse auto-detects your language and memory layout, assumes
sensible defaults, writes `dreams/muse-config.md`, and dreams — recording every
assumption it made so you can correct them. Edit the config by hand anytime.

Drop day-to-day context into `dreams/seeds.md` between runs; the next dream
consumes it.

## Configuration

`dreams/muse-config.md` (auto-created):

```markdown
- language: English
- memory_profile: llm-wiki | custom | bootstrapped | none
- memory_paths: [ ... ]
- goals: [ ... ]            # work AND life
- lenses: [ ... ]
- depth: 3
- more_sparks: true
- web_research: true
- divergence: grounded | balanced | wild
```

## Output

Each run writes `dreams/{date}-dream.md`: insights, a few deeply-developed ideas
(each with sources + a reasoning trace), "more sparks", an "action for today",
and a "How I dreamed this" note. It updates `dreams/index.md` and, when you pick
an idea to pursue, executes its route and records the outcome in `dreams/ledger.md`.

## Safety

Read-only everywhere except your `dreams/` folder and routes you approve. Web
research is read-only and cited. It never logs in, submits forms, or sends
anything. External-facing outputs stay draft-first and approval-gated. It never
invents facts; an unsourced claim is marked a hypothesis. Keep secrets out of your
config and ledger.

## Iterating on the skill

Muse is meant to be improved. `evals/` holds application scenarios you can run
against a subagent with only the skill loaded, to check that a fresh run is
autonomous, self-explaining, correctly routed, and grounded. See
[`evals/README.md`](evals/README.md).

## License

MIT — see [`LICENSE`](LICENSE).
