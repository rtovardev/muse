# Muse — Design

The design contract for Muse, an autonomous, environment-adaptive dream layer for
agentic coding assistants such as Claude Code, Codex, and compatible runtimes.

## Thesis

Most ideation tools ask for a topic and brainstorm around it. Muse dreams from
what the user has already accumulated: canonical memory, project artifacts,
recent seeds, prior dreams, taste signals, and live external context.

Muse should feel like a sharp partner actively developing the person, not a list
generator. The bar is:

> I noticed you are doing X. I connected it with Y and Z. Here is a non-obvious
> move, why it emerged, what could prove it wrong, and how to act on it.

## Product stance

Muse is **100% independent** as a skill and **100% adaptive** to the host
environment.

It does not require the user to adopt a specific memory architecture, task system,
agent framework, or scheduler. It detects and uses what exists. If nothing exists,
it still runs from goals, seeds, and web signals.

Internally, Muse applies **Karpathy-style memory discipline**:

1. Separate raw/canonical sources from generated reflections.
2. Use a navigable index rather than loose scattered notes.
3. Record updates and assumptions explicitly.
4. Prefer durable markdown files that a future agent can read.
5. Never promote generated reflections into canonical facts without confirmation.

This means Muse can work with an LLM-Wiki beautifully, but it must not force one.
A bootstrap LLM-Wiki is optional and consent-gated.

## Source hierarchy

Muse treats context in layers:

1. **Canonical memory** — the user's source of truth: LLM-Wiki, Obsidian vault,
   docs, decisions logs, project files, host-native memory, etc.
2. **Dream memory** — `dreams/`: generated dreams, index, taste ledger, run log,
   promoted fallbacks, and seeds.
3. **Live signals** — web search/fetch results and time-sensitive external facts.
4. **Assumptions** — explicit inferences made because something could not be
   verified.

Rules:

- Canonical memory beats dreams.
- Dreams can propose facts, but they are not facts until confirmed.
- Web claims need URLs.
- Assumptions must be visible and correctable.
- Secrets and raw sensitive communications do not belong in dream memory.

## What publishable + generalist requires

The skill must run for anyone, on any memory layout, in any host environment,
with zero hardcoded references to one person, company, or repo.

1. **Environment-adaptive.** Detects common memory and project layouts, plus host
   capabilities if exposed.
2. **Memory-agnostic.** Supports `llm-wiki`, `markdown-vault`, `project-repo`,
   `agent-workspace`, `host-native`, `bootstrapped`, and `none` profiles.
3. **Self-configuring.** Missing config does not block the run. Muse detects,
   defaults, writes config, logs assumptions, and continues.
4. **Host-adaptive routing.** Uses explicitly configured or visibly available
   capabilities; otherwise falls back to files.
5. **Language-agnostic output.** Produces dreams in the configured or detected
   language.
6. **Private by default.** Treats `dreams/` as local private data unless the user
   intentionally versions it.
7. **Safe on schedules.** Cron/scheduled runs are draft-only and never promote or
   act externally.

## The dream cycle

Muse runs a repeatable sleep-cycle loop:

### 1. Wake

Detect today's date, the next unused dream id, config, language, memory profile,
seeds, ledger, recent dreams, index, and host capabilities.

### 2. Consolidate

Read enough canonical memory to understand priorities, constraints, decisions,
projects, and recent changes. Read dream memory to avoid repetition and learn
user taste. Treat recurring threads as signal.

### 3. REM divergence

Generate a broad scratch pool across work and life lenses using recombination
techniques: forced pairing, SCAMPER, risk reframing, pattern replication, free
association, and wildcard mashups. The divergence dial controls reach:

| Dial | Behavior |
|---|---|
| `grounded` | Adjacent, near-term, lower-risk moves. |
| `balanced` | Mix of adjacent and cross-domain ideas. |
| `wild` | Distant mashups, clearly marked as speculative when needed. |

### 4. Reality check

Filter the scratch pool against canonical memory, taste ledger, decisions,
privacy constraints, web evidence, practical effort, timing, and falsifiers. Drop
ideas that are redundant, unsafe, unsupported, or contrary to explicit taste.

### 5. Morning note

Write a durable dream file with a unique filename:

```text
dreams/YYYY-MM-DD-NNN-dream.md
```

Append/update the structured row(s) in `dreams/index.md`. Never overwrite a prior
dream. If any write fails, keep seeds intact and log the failure.

### 6. Integration

When the user chooses an idea, identify its intent and route it into the host
workflow using configured/visible capabilities. If no capability exists, write a
fallback file. Record the promotion outcome in the ledger and index.

Scheduled mode stops before integration unless the user explicitly returns and
chooses an idea.

## Improvement loop

Muse improves without a central service. The user's local context becomes the
training signal for future runs:

1. **Context loop** — as canonical memory, docs, decisions, and projects grow,
   Muse has better nodes to recombine.
2. **Dream loop** — previous dreams expose recurring themes, stale ideas, and
   unresolved blocks.
3. **Taste loop** — ledger reactions teach Muse which themes are liked, dropped,
   meh, shipped, or worth promoting.
4. **Outcome loop** — promotions and shipped ideas tell Muse which routes create
   actual leverage.

The skill stays independent because all learning artifacts live in portable
markdown under the user's workspace.

## The four pillars

### 1. Autonomy

Muse runs end-to-end. Missing config or context is handled by detection,
defaults, and explicit assumptions. The setup interview is optional and only runs
when the user asks to configure Muse or there is truly nothing to detect.

Defaults when unconfigured:

| Setting | Auto-detected from | Fallback default |
|---|---|---|
| `language` | recent user text / repo locale | English |
| `mode` | prompt/scheduler context | `interactive` |
| `memory_profile` | `memory/wiki/`, `.obsidian/`, `docs/`, agent workspace files | `none` |
| `memory_paths` | detected index/root files | invocation directory |
| `goals` | goals/priorities/readme files | infer from recent activity; mark as assumption |
| `lenses` | config | holistic default set |
| `depth` | config | 3 |
| `more_sparks` | config | true |
| `web_research` | network availability/config | true if available |
| `divergence` | config | `balanced` |
| `routes` | config/visible skills | `auto` with file fallback |

### 2. Evidence transparency

Muse does not expose hidden chain-of-thought. It provides an **evidence trace**
that lets the user audit the dream:

- **Assumption** — what was taken as given, and why.
- **Recombined nodes** — specific memory pages, seeds, prior dreams, and web
  signals crossed to form the idea.
- **Confidence** — high / medium / low, with the reason.
- **Falsifier** — what observation would make the idea wrong or not worth doing.

Every session ends with a **How I dreamed this** note: creative leap, patterns
used, what was deliberately discarded, and the assumptions the session rests on.

### 3. Adaptive routing

When the user picks an idea, Muse maps it to one intent:

| Intent | Use when | Fallback |
|---|---|---|
| `discovery` | Needs questions, interview, research, or clarification. | Write open questions to `dreams/promoted/`. |
| `build` | Needs implementation, automation, prototype, or artifact. | Write scoped build note to `dreams/promoted/`. |
| `decision` | Needs a durable decision or trade-off. | Append to `dreams/decisions.md`. |
| `content` | Needs draft-first external/internal writing. | Write draft to `dreams/promoted/`. |
| `task` | Needs a discrete action in a task system. | Write actionable task file to `dreams/promoted/`. |

Routing is deterministic:

1. Use an explicit `routes:` mapping from config if present.
2. Else use a capability visibly exposed by the host/runtime.
3. Else use the file fallback.
4. Never invent a host skill or claim one was invoked if it was not visible.
5. Verify time-sensitive facts before routing.

### 4. Taste

A per-user append-only ledger records reactions and outcomes:

- `liked`
- `shipped`
- `dropped`
- `meh`
- `promoted`

Muse reads it every run. It avoids dropped themes, evolves shipped ideas, leans
into liked patterns, and treats repeated meh as weak signal.

Taste is not canonical fact memory. If a durable fact emerges, Muse may propose a
memory update, but the user or host memory workflow must approve it.

## Dream files and state

Every deep idea gets a stable id:

```text
muse-YYYYMMDD-NNN-a
muse-YYYYMMDD-NNN-b
muse-YYYYMMDD-NNN-c
```

`dreams/index.md` uses this schema:

```markdown
| idea_id | date | dream_file | title | lens | route | state | confidence | notes |
|---|---|---|---|---|---|---|---|---|
| muse-20260609-001-a | 2026-06-09 | dreams/2026-06-09-001-dream.md | Idea name | build | build | dreamed | medium | action for today |
```

States:

```text
dreamed → liked → promoted → shipped
dreamed → dropped
dreamed → decided
dreamed → stale
```

## Safety and privacy

- Read-only everywhere except `dreams/**`, approved promotions, and explicit
  consent-gated memory bootstrap.
- Web research is read-only. Cite sources.
- Never log in, submit forms, send messages, or mutate external systems.
- External-facing outputs stay draft-first and approval-gated.
- Do not copy secrets, credentials, raw private messages, or sensitive client
  communications into dreams.
- Scheduled mode is draft-only and stops after writing/indexing.

## Non-goals

- Not a research report generator.
- Not a single-plan stress tester.
- Not a replacement for canonical memory.
- Not a task manager.
- Not an automation executor.
- No required runtime scripts, backend, database, or vendor-specific integration.

## Repo layout

```text
muse/
  skills/muse/SKILL.md
  skills/muse/references/runbook.md
  examples/sample-vault/
  examples/sample-output/
  evals/
  README.md
  DESIGN.md
  CHANGELOG.md
  CONTRIBUTING.md
  SECURITY.md
  LICENSE
```

`skills/muse/SKILL.md` follows the common skill import convention so a host repo
can pin it via lockfile, copy it, or consume it via submodule/symlink.
