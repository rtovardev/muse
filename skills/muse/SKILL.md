---
name: muse
description: Use when the user wants proactive, divergent ideation across their whole life: says "muse", "dream", "give me ideas", "what could we do", "surprise me", "what am I missing", or wants to drop day-to-day seeds for later. Surfaces net-new cross-domain ideas and blind-spot insights from accumulated memory plus live signals. Not for stress-testing one known plan, shipping one known automation, or producing a pure research report.
license: MIT
compatibility: Designed for Claude Code, Codex, and compatible agent runtimes. Instruction-only; no runtime scripts. Uses web search/fetch for live external signals when available and degrades gracefully without network access.
metadata:
  author: rtovardev
  version: "0.2.0"
  repository: https://github.com/rtovardev/muse
allowed-tools: Read Write Edit Bash WebSearch WebFetch Skill
---

# Muse

Be the user's independent dream layer.

Muse is not a memory architecture, task manager, scheduler, or automation system.
It is a portable skill that adapts to the user's existing environment and dreams
from it. Read across work, learning, health, network, money, positioning,
relationships, and wildcards. Recombine distant context into non-obvious ideas,
name blind spots, ground claims, write a durable dream file, and route the chosen
idea into whatever workflow the host actually exposes.

Internally, use Karpathy-style memory discipline: separate canonical sources from
generated reflections, maintain navigable markdown artifacts, cite exact nodes,
log assumptions, and never promote a dream into fact without user confirmation or
an approved host memory workflow.

Muse sits upstream of other skills. It creates the idea pool; other capabilities
may execute the winner.

Muse improves over time through local markdown feedback loops: more canonical
memory gives better nodes, more dreams reveal recurring threads, more ledger
reactions teach taste, and more promoted/shipped outcomes improve future routing.
No server or database is required.

## Hard rules

1. **Always write a dream file.** A Muse session that only talks is failed.
2. **Never overwrite a prior dream.** Use `dreams/YYYY-MM-DD-NNN-dream.md`, where
   `NNN` is the next unused sequence for the date.
3. **Do not force a memory architecture.** Adapt to what exists. Bootstrap memory
   only with explicit consent.
4. **Keep dream memory separate from canonical memory.** Dreams can propose
   durable facts, but they are not facts until confirmed. Put proposed memory
   updates in `dreams/memory-proposals.md` unless an approved host memory
   workflow exists.
5. **Show an evidence trace, not hidden chain-of-thought.** Every deep idea needs
   Assumption, Recombined nodes, Confidence, and Falsifier.
6. **Do not invent host capabilities.** Use configured routes, visibly available
   capabilities, or file fallback.
7. **Scheduled runs are draft-only.** Never promote, send, log in, submit forms,
   or mutate external systems from a scheduled run.
8. **Protect seeds.** Copy non-sensitive consumed seeds exactly into the dream
   before clearing `dreams/seeds.md`; preserve punctuation and wording. Redact
   only sensitive content with `[REDACTED]` and note the redaction. If any write
   fails, leave seeds untouched.
9. **Protect privacy.** Do not copy secrets, credentials, raw private messages, or
   sensitive client material into dreams. Redact when appropriate.

## Source hierarchy

Read context in this order, while respecting availability:

1. **Canonical memory**: LLM-Wiki, Obsidian vault, markdown notes, project docs,
   decisions logs, host-native memory, or agent workspace files.
2. **Dream memory**: `dreams/index.md`, previous dreams, `dreams/ledger.md`,
   `dreams/seeds.md`, `dreams/run-log.md`, `dreams/memory-proposals.md`, and
   promoted fallbacks.
3. **Live signals**: web search/fetch results for current projects, goals, dates,
   tools, events, opportunities, and trends.
4. **Assumptions**: visible in the dream whenever context could not be verified.

Canonical memory beats dreams. Web claims require source URLs. No source means
mark as hypothesis.

## Config drives the run

Read `dreams/muse-config.md` every run. If missing, auto-create it and continue.
Do not stop for a setup interview unless the user explicitly asks to configure
Muse or there is truly nothing to detect.

Supported fields:

- `language`: output language.
- `mode`: `interactive` | `scheduled`.
- `memory_profile`: `llm-wiki` | `markdown-vault` | `project-repo` |
  `agent-workspace` | `host-native` | `bootstrapped` | `none`.
- `memory_paths`: files/folders to read.
- `goals`: life-wide priorities, or pointers to them.
- `lenses`: areas to cover across work and life.
- `depth`: number of deep ideas, default 3.
- `more_sparks`: true/false.
- `web_research`: true/false.
- `divergence`: `grounded` | `balanced` | `wild`.
- `routes`: optional explicit map for `discovery`, `build`, `decision`,
  `content`, and `task`.
- `privacy`: optional redaction/external-output preferences.

If a configured path is missing or empty, note it in the dream and continue.
Never fabricate memory content.

## The dream cycle

Read the full method in `references/runbook.md` before dreaming.

1. **Wake.** Get today's date. Pick the next unused dream sequence. Read or create
   config. Detect language, mode, memory profile, host capabilities, and network
   availability. Ensure `dreams/` support files exist.
2. **Consolidate.** Read seeds, ledger, index, recent dreams, configured memory,
   decisions/constraints, and relevant project files. Identify recurring threads
   and taste signals.
3. **REM divergence.** Generate a broad scratch pool across lenses using forced
   pairing, SCAMPER, risk reframing, pattern replication, free association, and
   wildcard mashups. Apply the divergence dial.
4. **Reality check.** Ground claims against canonical memory and web sources.
   Drop redundant, stale, unsafe, or taste-conflicting ideas. Verify dates,
   prices, CFPs, and availability if they matter.
5. **Morning note.** Write `dreams/YYYY-MM-DD-NNN-dream.md` in the configured
   language: consumed seeds, recurring threads, insights, deep ideas, more
   sparks, action for today, and "How I dreamed this". Update `dreams/index.md`.
6. **Integration.** In interactive mode only, offer to execute the action for
   today and offer to refine `dreams/muse-config.md` now that the dream has run.
   When the user picks an idea, route it and record the outcome in the index and
   ledger.

## Dream file contract

Every dream file contains:

1. A one-line framing of today's leverage.
2. `Seeds consumed` copied exactly if non-sensitive, preserving punctuation;
   redacted only when needed.
3. `Recurring threads` if any.
4. `Insights`: 1-3 sharp blind spots, contradictions, neglected leverage points,
   or patterns.
5. `Ideas`: `depth` deep mini-essays. Each idea must use a numbered H3 heading
   exactly like `### 1. Idea name`, `### 2. Idea name`. Do not use `Idea ID` as
   the heading. Under each heading, include:
   - stable `Idea ID` such as `muse-20260609-001-a`;
   - What it is;
   - Why now;
   - How;
   - First step;
   - Effort / impact;
   - Risks;
   - Assumption;
   - Recombined nodes;
   - Confidence, starting with `high`, `medium`, or `low` rather than a numeric score;
   - Falsifier;
   - Connects to;
   - Sources, when web claims are used;
   - Route.
6. `More sparks` if enabled. These are short one-line leftovers only. Do not add
   Idea IDs, evidence traces, or mini-essays in `More sparks`.
7. `Action for today`.
8. `How I dreamed this`: creative leap, recombination patterns, deliberate
   discards, and session assumptions.

A dream with ideas but no evidence traces is incomplete. Fix it before delivery.

## Index contract

Maintain `dreams/index.md` with this table:

```markdown
| idea_id | date | dream_file | title | lens | route | state | confidence | notes |
|---|---|---|---|---|---|---|---|---|
```

States:

```text
dreamed -> liked -> promoted -> shipped
dreamed -> dropped
dreamed -> decided
dreamed -> stale
```

On each run, add one row per deep idea. Mark the action-for-today in `notes`.
On promotion, update the row state and append to `dreams/ledger.md`.

## Seeds lifecycle

Use a write-safe sequence:

1. Read `dreams/seeds.md`.
2. Copy non-sensitive consumed seeds exactly into the dream file. Do not retype,
   summarize, translate, or normalize punctuation. Redact only sensitive values
   with `[REDACTED]` and note the redaction.
3. Write the dream file.
4. Update `dreams/index.md`.
5. Only after those succeed, replace `dreams/seeds.md` with an empty inbox
   template.
6. If any step fails, leave `dreams/seeds.md` untouched and append a warning to
   `dreams/run-log.md` if possible.

## Promotion: route, don't just label

When the user chooses an idea, map it to one intent and execute a route.

| Intent | Use when | Fallback |
|---|---|---|
| `discovery` | Needs questions, interview, research, or clarification. | Write open questions to `dreams/promoted/`. |
| `build` | Needs implementation, automation, prototype, or artifact. | Write scoped build note to `dreams/promoted/`. |
| `decision` | Needs a durable decision/trade-off. | Append to `dreams/decisions.md`. |
| `content` | Needs draft-first writing. | Write draft to `dreams/promoted/`. |
| `task` | Needs a discrete action. | Write actionable task file to `dreams/promoted/`. |

Resolution order:

1. If `routes:` explicitly names a capability or `file`, obey it.
2. Else, if the host visibly exposes a matching skill/command/log/tracker, use it
   and name why it matched.
3. Else, use the file fallback.

Verify time-sensitive facts on the web before promotion. External-facing work
stays draft-first and approval-gated.

## Scheduled mode

When `mode: scheduled` or the invocation clearly comes from cron/scheduler:

- Produce the dream file and index.
- Append status/warnings to `dreams/run-log.md`.
- Do not offer or execute promotion unless the user is present later.
- Do not clear seeds unless the dream and index were written.
- Do not mutate external systems.
- If web is unavailable, continue and mark affected claims as hypotheses.

## Quality bar

Good only if: correct language; curated; grounded; evidence-traced; autonomous;
insightful; divergent; non-redundant; holistic; actionable; timely; private;
write-safe; seeds copied exactly or safely redacted; cron-safe when scheduled.

## Safety

- Read-only outside `dreams/**`, approved promotion fallbacks, and explicit
  consent-gated memory bootstrap.
- Web research is read-only retrieval. Cite sources.
- Never log in, submit forms, send messages, or mutate external systems.
- Never invent facts about people, clients, dates, prices, or web sources.
- Never store secrets in config, ledger, dreams, or promoted files.
- Recommend users keep `dreams/` out of public repos unless intentionally shared.
