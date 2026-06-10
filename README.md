# Muse

**An autonomous, environment-adaptive dream layer for agentic coding assistants.**

Most ideation tools take a topic and brainstorm it. Muse takes the user's
accumulated context, taste history, and live external signals, then **dreams**:
it recombines distant ideas, names blind spots, produces a few grounded ideas,
and routes the chosen one into the workflow the host already has.

Muse is designed to feel like a sharp partner actively helping a person develop,
not a list generator. The bar: *"I noticed you're running X. Here's a
non-obvious move, why it emerged, what would prove it wrong, and how to act on it."*

Works with Claude Code, Codex, and compatible agent runtimes. Muse has no runtime
scripts or required backend. It is instruction-only, portable, and host-adaptive.

## Core idea

Muse is **not** a memory architecture you must adopt. Muse is a **dream layer**
that adapts to whatever environment already exists:

- Karpathy-style LLM-Wiki / Obsidian vaults.
- Arbitrary markdown notes or project documentation.
- Agent workspaces with local rules, inboxes, and skills.
- Bare repos with little or no memory.
- Host-native memory exposed by the assistant runtime.

Internally, Muse uses Karpathy-style memory discipline:

1. Treat canonical memory as the source of truth.
2. Keep generated dreams separate from facts.
3. Cite the exact memory nodes and web signals used.
4. Record assumptions instead of silently turning them into truth.
5. Promote durable facts back into canonical memory only with user consent or via
   the host's approved memory workflow.

If the user has no memory, Muse can optionally bootstrap a tiny LLM-Wiki scaffold,
but that is a convenience, not lock-in.

## What it does

- **Dreams across the whole life**: work, learning, health, network, money,
  positioning, projects, relationships, and wildcards.
- **Uses live external signals** when available: tools, events, courses, trends,
  competitors, communities, papers, or techniques. Every web claim is cited.
- **Explains itself with evidence traces**: assumptions, recombined nodes,
  confidence, and falsifiers. No hidden facts.
- **Runs autonomously**: missing config means detect, default, continue, and log
  the assumptions.
- **Adapts to any host workflow**: skills, slash commands, decisions logs, task
  trackers, or file fallbacks.
- **Improves over time** as context accumulates: more canonical memory, more
  dreams, more ledger reactions, and more promoted outcomes make future dreams
  less generic and more aligned.
- **Learns taste over time** through an append-only ledger of liked, shipped,
  dropped, meh, and promoted ideas.

## The dream cycle

Each run follows a sleep-cycle loop:

1. **Wake**: detect date, config, language, memory, seeds, host capabilities, and
   constraints.
2. **Consolidate**: read canonical memory, recent dreams, index, ledger, decisions,
   and seeds.
3. **REM divergence**: force non-obvious recombinations across configured lenses.
4. **Reality check**: ground against memory, web, taste, safety, and practical
   constraints.
5. **Morning note**: write a durable, unique dream file and update the index.
6. **Integration**: when the user chooses, route one idea into the host workflow
   and record the outcome.

## The four pillars

| Pillar | What it means |
|---|---|
| **Autonomy** | Runs end-to-end. Missing context → detect, default, log the assumption, continue. |
| **Evidence transparency** | Every idea carries an assumption, recombined nodes, confidence, and falsifier. |
| **Adaptive routing** | Maps the chosen idea to an intent and resolves it to configured or visible host capabilities, with file fallback. |
| **Taste** | A local append-only ledger steers future runs and prevents repeated misses. |

Plus: a **divergence dial** (`grounded` → `wild`), **recurring threads**, and a
**scheduled mode** for cron-safe dreams.

## How Muse improves

Muse gets better through four accumulating feedback loops:

1. **Context loop** — the host environment and canonical memory grow.
2. **Dream loop** — prior dreams reveal recurring threads and unresolved blocks.
3. **Taste loop** — ledger reactions teach Muse what to avoid, evolve, or pursue.
4. **Outcome loop** — promoted/shipped ideas become signal for future routing and
   idea selection.

Muse does not need a central server or database for this. The loop is local,
portable, and markdown-based.

See [`DESIGN.md`](DESIGN.md) for the full contract.

## Install

Muse is a standard skill: a folder with a `SKILL.md`.

**Option A — drop it in.** Copy `skills/muse/` into your assistant's skills
directory (`.claude/skills/` for Claude Code, `~/.agents/skills/` for Codex), so
you have `.../skills/muse/SKILL.md`.

**Option B — git submodule** (recommended if you want to pull updates):

```bash
git submodule add https://github.com/rtovardev/muse vendor/muse
ln -s ../../vendor/muse/skills/muse .claude/skills/muse
```

**Option C — lockfile import.** The `skills/muse/SKILL.md` path is compatible
with `npx skills`-style importers; pin it from `rtovardev/muse`.

Per-user data lives in the user's own workspace under `dreams/`, never inside the
skill. The skill and the user's private dreams stay separate.

## Quickstart — see it run

Try Muse against the bundled sample vault (Sam, an independent consultant) without
touching your own data:

```bash
cp -r examples/sample-vault /tmp/muse-demo && cd /tmp/muse-demo
# point your assistant here, then run:  /muse
# inspect the generated dream:          ls dreams/*-dream.md
python3 /path/to/muse/evals/check_dream.py dreams/2025-*-dream.md
```

You should get a dated dream file with insights, deep ideas (each carrying an
evidence trace), and an "action for today" — and a `PASS` from the checker.

## First run

Invoke it:

```text
/muse
```

Or say: *"muse"*, *"dream"*, *"give me ideas"*, *"what am I missing"*.

On the first run with no config, Muse detects what it can, writes
`dreams/muse-config.md`, creates the supporting dream files if missing, and runs.
It records every assumption so the user can correct the config later.

Drop day-to-day context into `dreams/seeds.md` between runs; the next dream safely
copies non-sensitive consumed seeds exactly into the dream file before clearing
the seed inbox. Sensitive seeds are redacted instead of reproduced.

## Configuration

`dreams/muse-config.md` is auto-created and hand-editable:

```markdown
# Muse Config

- language: English
- mode: interactive              # interactive | scheduled
- memory_profile: llm-wiki       # llm-wiki | markdown-vault | project-repo | agent-workspace | host-native | bootstrapped | none
- memory_paths:
    - memory/wiki/index.md
    - docs/
- goals:
    - {priority 1}
    - {priority 2}
- lenses:
    - current work
    - learning & skills
    - health & performance
    - network & relationships
    - wildcards
- depth: 3
- more_sparks: true
- web_research: true
- divergence: balanced           # grounded | balanced | wild
- routes:
    discovery: auto              # auto | file | {explicit host skill/command}
    build: auto
    decision: auto
    content: auto
    task: auto
- privacy:
    redact_sensitive: true
    external_outputs: draft-first
- updated: YYYY-MM-DD
```

## Output

Every run writes a **unique** dream file. Muse never overwrites a prior dream:

```text
dreams/2026-06-09-001-dream.md
dreams/2026-06-09-002-dream.md
```

It also updates:

- `dreams/index.md` — stable dream and idea index.
- `dreams/ledger.md` — taste and promotion outcomes.
- `dreams/seeds.md` — safely cleared only after the dream and index are written.
- `dreams/run-log.md` — scheduled runs, warnings, and failures.
- `dreams/memory-proposals.md` — optional user-approved candidates for canonical memory.
- `dreams/promoted/` — file fallbacks for promoted ideas when no host capability exists.

## Compatibility

| Environment | Status |
|---|---|
| Claude Code skills folder | Designed path: `.claude/skills/muse/SKILL.md`. |
| Codex/agent skills folder | Designed path: `~/.agents/skills/muse/SKILL.md` or repo mirror. |
| Generic agent runtime | Works if the runtime can read/write files and expose tool/capability context. |
| Bare markdown workspace | Works with file fallbacks. |
| No memory yet | Works from seeds/goals and can offer optional memory bootstrap. |

## Scheduled runs

Muse can be invoked by cron or any assistant scheduler. Scheduled mode must be
safe and draft-only:

- Write the dream and index.
- Log warnings to `dreams/run-log.md`.
- Do not promote ideas automatically.
- Do not send external messages.
- Do not log in, submit forms, or mutate external systems.
- If a write fails, keep `dreams/seeds.md` untouched.

The scheduler is host-specific. Muse only defines the safe behavior.

## Privacy

`dreams/` may contain sensitive personal, client, health, money, or career
reflections. For public repos, add it to `.gitignore` unless you intentionally
want to version it:

```gitignore
# Muse private dream data
dreams/
```

Muse should not copy secrets, credentials, private messages, or raw sensitive
communications into dreams. It should redact sensitive names when appropriate and
mark unverified claims as hypotheses.

See [`SECURITY.md`](SECURITY.md).

## Known limitations

- Muse cannot access memory, tools, or skills that the host does not expose.
- Web grounding depends on the host's available search/fetch tools.
- Behavioral evals are partly manual because dream quality is qualitative.
- Instruction-only portability means there is no built-in scheduler; scheduling is
  provided by the host environment.
- Private `dreams/` data is only as safe as the user's workspace and git hygiene.

## Iterating on the skill

Muse is meant to be improved. `evals/` holds application scenarios for checking
that a fresh run is autonomous, self-explaining, correctly routed, grounded,
private, and cron-safe. See [`evals/README.md`](evals/README.md).

A lightweight structure checker lives at `evals/check_dream.py`.

## License

MIT — see [`LICENSE`](LICENSE).
