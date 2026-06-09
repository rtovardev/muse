# Muse — Runbook

The method behind Muse. Read this before dreaming.

Muse is a portable dream layer. It adapts to the user's existing environment and
works internally with Karpathy-style memory discipline: sources stay separate
from reflections, assumptions are logged, links are explicit, and generated ideas
are not treated as canonical facts until confirmed.

All examples below use a neutral illustrative persona — **Sam, an independent
consultant** — and are marked `EXAMPLE`. Never copy example content into a real
dream.

---

## 1. Operating model

Muse is independent and host-adaptive:

- It can run in Claude Code, Codex, or compatible agent runtimes.
- It does not require runtime scripts, a database, or a specific memory system.
- It reads whatever context the user already has.
- It writes private per-user dream artifacts under `dreams/`.
- It routes into host capabilities only when configured or visibly available.

Muse is not the user's source of truth. It is a **dream layer over the source of
truth**.

Muse improves over time through local files, not model fine-tuning: canonical
memory gives better source nodes, dreams reveal recurring patterns, the ledger
teaches taste, and promotions/shipped outcomes teach what actually creates
leverage.

### Source hierarchy

1. **Canonical memory**: LLM-Wiki, Obsidian vault, markdown notes, project docs,
   decisions logs, host-native memory, agent workspace files.
2. **Dream memory**: `dreams/index.md`, previous dreams, `dreams/ledger.md`,
   `dreams/seeds.md`, `dreams/run-log.md`, `dreams/memory-proposals.md`,
   promoted files.
3. **Live signals**: web sources, dates, pricing, tool releases, events, trends,
   public docs.
4. **Assumptions**: explicit inferences when something cannot be verified.

Rules:

- Canonical memory beats dreams.
- Dreams can propose durable facts, but they are not facts yet.
- Web claims need source URLs.
- No source = hypothesis.
- Never copy secrets or raw sensitive material into dreams.

---

## 2. The dream cycle

Every run follows this loop.

### 2.1 Wake

- Get today's date.
- Determine the next unused dream sequence for today.
- Read `dreams/muse-config.md`, or auto-create it if missing.
- Detect language, mode, memory profile, memory paths, network availability, and
  host capabilities.
- Ensure `dreams/` support files exist.

Dream filenames:

```text
dreams/YYYY-MM-DD-NNN-dream.md
```

Examples:

```text
dreams/2026-06-09-001-dream.md
dreams/2026-06-09-002-dream.md
```

Never overwrite an existing dream. If matching files exist, increment `NNN`.

### 2.2 Consolidate

Read enough context to understand:

- goals and priorities;
- current projects;
- active constraints;
- decisions already made;
- recent memory changes;
- seeds since the last run;
- prior dreams and recurring threads;
- taste signals from the ledger.

Do not try to read the entire universe. Read the index/overview files first, then
open the few most relevant pages.

### 2.3 REM divergence

Generate a broad scratch pool. Use a mix of:

- forced pairing;
- SCAMPER;
- Six Thinking Hats;
- free association;
- risk reframing;
- pattern replication;
- wildcard cross-domain mashups.

The divergence dial controls reach:

| `divergence` | Behavior |
|---|---|
| `grounded` | Adjacent moves; near-term and lower-risk. |
| `balanced` | Mix of adjacent and cross-domain ideas. |
| `wild` | Distant mashups; mark speculation clearly and lower confidence when needed. |

### 2.4 Reality check

Filter the scratch pool:

- Drop ideas that conflict with explicit dropped themes.
- Do not re-propose shipped/decided ideas; evolve them or leave them alone.
- Ground memory claims in actual files.
- Ground web claims in URLs.
- Verify dates, deadlines, CFPs, prices, and availability if relevant.
- Reject unsafe, private, or external-action ideas unless they can stay draft-first.
- Add falsifiers.

### 2.5 Morning note

Write the durable dream file and update `dreams/index.md`.

Only after both writes succeed, clear `dreams/seeds.md` using the safe lifecycle
below.

### 2.6 Integration

In interactive mode, offer the action for today, ask what the user wants to
pursue, and offer to refine `dreams/muse-config.md` after the dream has run. When
the user chooses an idea, route it and record the outcome.

In scheduled mode, stop after writing/indexing. The scheduled dream is a draft.

---

## 3. Autonomy and defaults

Do not stall on missing input that can be inferred.

On every run:

1. Try to read `dreams/muse-config.md`.
2. If absent, auto-configure from the environment and defaults.
3. Write a best-effort config.
4. Record every assumption in the dream.
5. Dream.
6. Offer config refinement after the dream, never before.

Defaults:

| Setting | Detect from | Default if undetectable |
|---|---|---|
| `language` | recent user messages, repo/system locale | English |
| `mode` | prompt/scheduler context | `interactive` |
| `memory_profile` | `memory/wiki/`, `.obsidian/`, `notes/`, `docs/`, agent workspace files | `none` |
| `memory_paths` | detected index/root files | invocation directory |
| `goals` | goals/priorities/README files | infer 2-3 from recent activity; mark as assumption |
| `lenses` | config | default holistic set |
| `depth` | config | 3 |
| `more_sparks` | config | true |
| `web_research` | network availability | true if available |
| `divergence` | config | `balanced` |
| `routes` | config/visible host capabilities | `auto` with file fallback |
| `privacy.redact_sensitive` | config | true |

Run the optional setup interview only when the user explicitly asks to configure
Muse, or there is truly nothing to detect and no goals/seeds to dream from.

---

## 4. Config schema

Auto-created file: `dreams/muse-config.md`.

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
    - current clients/customers
    - prospects
    - offers / productization
    - positioning
    - content
    - personal automations
    - learning & skills
    - health & performance
    - network & relationships
    - money & resilience
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

If paths are missing, note them and continue. Never fabricate missing context.

---

## 5. Memory profiles

### `llm-wiki`

Karpathy-style memory with index/log/pages. Read:

- wiki index;
- overview/goals/current project pages;
- recent log entries;
- decisions log if present;
- most relevant linked pages.

### `markdown-vault`

Arbitrary markdown or Obsidian-style vault. Read:

- index/home/readme files if present;
- folder names;
- recent or relevant markdown pages;
- decision/goals files if discoverable.

### `project-repo`

A software/project repository with docs and local rules. Read:

- `README.md`;
- `AGENTS.md`, `CLAUDE.md`, or equivalent if present;
- `docs/`, `decisions/`, `CHANGELOG.md`, project plans;
- recent git context when available.

### `agent-workspace`

Assistant workspace with inbox/outbox/rules/skills. Read:

- local operating rules;
- inbox/seeds;
- permissions;
- available skills or routes;
- recent outputs/logs.

### `host-native`

The runtime exposes memory or tools but not necessarily files. Use only what is
visible in the host context. Do not claim hidden access.

### `bootstrapped`

Muse created a minimal memory scaffold with explicit user consent. Treat it as
thin and provisional.

### `none`

No structured memory. Dream from goals, seeds, current repo/docs, and web. Say so
plainly in the dream.

---

## 6. Bootstrap memory, optional and consent-gated

Only with explicit consent. Muse may create a minimal LLM-Wiki-style scaffold:

```text
memory/
  raw/
  wiki/
    index.md
    log.md
    overview.md
    goals.md
  schema.md
```

Minimum rules:

- wiki pages have frontmatter: `title`, `type`, `status`, `created`, `updated`;
- index lists pages;
- log headings use `## [YYYY-MM-DD] action | Title`;
- raw stores immutable sources or source pointers;
- generated dreams stay in `dreams/`, not `memory/`.

Set `memory_profile: bootstrapped` and add the new memory paths to config.

---

## 7. Dream memory files

Muse may create these files if missing:

```text
dreams/
  muse-config.md
  seeds.md
  index.md
  ledger.md
  run-log.md
  memory-proposals.md
  promoted/
```

### `dreams/seeds.md`

Inbox for context between runs.

Template:

```markdown
# Muse Seeds

Day-to-day context for the next Muse run. One bullet per thought.

## Inbox

```

### `dreams/index.md`

Structured idea index:

```markdown
# Muse Index

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

Add one row per deep idea. Mark the action-for-today in `notes`.

### `dreams/ledger.md`

Append-only taste and outcomes:

```markdown
# Muse Ledger

Append-only taste log. Heading shape:
`## [YYYY-MM-DD] {signal} | {idea}`.

Signals: liked · shipped · dropped · meh · promoted.
```

### `dreams/memory-proposals.md`

Optional holding area for facts or patterns Muse thinks may belong in canonical
memory. Do not write directly to canonical memory unless the user approved it or
the host exposes an approved memory workflow.

```markdown
# Muse Memory Proposals

## [YYYY-MM-DD] proposed | {title}
- proposed fact/pattern:
- evidence:
- why it may matter:
- needs approval: yes
```

### `dreams/run-log.md`

Append scheduled runs, warnings, write failures, degraded web, missing paths, or
other operational notes:

```markdown
## [YYYY-MM-DD HH:MM] status | Summary
- mode: scheduled
- dream_file: dreams/YYYY-MM-DD-NNN-dream.md
- warnings: ...
```

---

## 8. Seeds lifecycle, write-safe

Never lose seeds.

1. Read `dreams/seeds.md`.
2. Copy non-sensitive consumed seeds exactly into the dream file. Preserve
   punctuation, casing, and wording. Do not retype from memory, summarize,
   translate, or normalize punctuation. Redact only sensitive values with
   `[REDACTED]` and note the redaction.
3. Write the dream file.
4. Update `dreams/index.md`.
5. Only after both writes succeed, replace `dreams/seeds.md` with the empty inbox
   template.
6. If any step fails, keep `dreams/seeds.md` untouched and append a warning to
   `dreams/run-log.md` if possible.

If no seeds exist, keep or create the empty template.

---

## 9. Web research

When `web_research: true`, run 3-6 targeted searches tied to current memory,
goals, or seeds.

Search for:

- current tools or techniques;
- events, CFPs, dates, deadlines;
- courses, communities, grants, accelerators;
- competitors, examples, pricing;
- trends connected to the user's work/life context.

Rules:

- Connect web signals to the user's situation; do not dump links.
- Cite every web claim with a URL.
- Verify time-sensitive facts before using or promoting them.
- If network is unavailable, continue and mark affected ideas as hypotheses.
- Web actions are read-only.

---

## 10. Recurring threads

Before diverging, skim recent dreams and `dreams/index.md`:

- A resurfacing theme is a signal, not just repetition.
- If the same idea appears repeatedly without action, surface the block.
- Ideas marked `dropped` should not be re-proposed.
- Ideas marked `shipped` or `decided` should become next steps only when useful.

---

## 11. Lenses

Default holistic lenses:

Work:

1. Current clients/customers.
2. Prospects.
3. Offers / productization.
4. Positioning.
5. Content.
6. Personal automations.

Life:

7. Learning & skills.
8. Health & performance.
9. Network & relationships.
10. Money & resilience.

Wildcard:

11. Wildcards: deliberate cross-domain mashups.

Cover several lenses each session. Do not let every idea become work-only unless
config says so.

---

## 12. Insights before ideas

Name 1-3 observations before proposing ideas:

- blind spots;
- contradictions;
- neglected leverage;
- recurring patterns;
- constraints the user is not accounting for.

An insight earns its place if it could change a decision.

---

## 13. Evidence trace

Muse should not expose hidden chain-of-thought. It should provide an auditable
evidence trace.

Each deep idea needs:

- **Assumption**: what was taken as given and why; flag unverified context.
- **Recombined nodes**: specific memory pages, seeds, prior dreams, and web
  signals crossed to create the idea.
- **Confidence**: high / medium / low with a reason.
- **Falsifier**: what would prove the idea wrong or not worth doing.

Session close:

- **How I dreamed this**: central creative leap; recombination patterns used;
  deliberate discards; session-level assumptions.

---

## 14. Dream file structure

```markdown
# Muse — YYYY-MM-DD — NNN
{one-line framing: today's leverage}

## Seeds consumed
{non-sensitive seeds copied exactly from dreams/seeds.md, preserving punctuation; redact only sensitive values; omit if none}

## Recurring threads
{themes from recent dreams/index; omit if none}

## Insights
1. {sharp observation}

## Ideas

### 1. {Idea name}
**Idea ID:** muse-YYYYMMDD-NNN-a
**Lens:** {lens}
**What it is:** {2-4 concrete sentences}
**Why now:** {timing from memory/seeds/web}
**How:** {execution shape}
**First step:** {one concrete next action}
**Effort / impact:** {low|med|high / low|med|high}
**Risks:** {honest risks or unknowns}
**Assumption:** {taken as given and why}
**Recombined nodes:** {real memory paths/wikilinks + seeds + web signals}
**Confidence:** {high|medium|low — reason}
**Falsifier:** {one-line test that would make this wrong}
**Connects to:** {real memory links or paths}
**Sources:** {URLs for web claims, or "None; internal/hypothesis"}
**Route:** {discovery|build|decision|content|task}

## More sparks
- [{lens}] {one-liner}

## Action for today
{single best idea + why + route}

## How I dreamed this
{creative leap, patterns fired, what was discarded, assumptions}
```

Do not pad with weak ideas. If fewer than `depth` ideas are strong, write fewer
and say why.

### Abbreviated EXAMPLE

```markdown
# Muse — 2025-01-15 — 001
EXAMPLE — Today's leverage is turning Sam's repeated audit shape into a calmer,
more predictable offer.

## Ideas

### 1. Package the audit as a fixed-scope starter offer
**Idea ID:** muse-20250115-001-a
**Lens:** offers / productization
**What it is:** Turn Sam's recurring audit deliverable into a named fixed-scope
package so prospects buy a known thing instead of negotiating scope every time.
**Why now:** Three audits shared the same report structure, and a prospect asked
about retainers.
**How:** Extract the repeated report sections, name the offer, draft scope limits,
and test it with the next prospect.
**First step:** List which audit sections were identical across the last three reports.
**Effort / impact:** low / high
**Risks:** Over-fitting to one client type.
**Assumption:** Assumes the reports are structurally similar, inferred from audit notes.
**Recombined nodes:** `memory/wiki/clients/audit-notes.md` × `dreams/seeds.md` retainer seed × `memory/wiki/offers/index.md`.
**Confidence:** medium — visible pattern, not yet diffed file-by-file.
**Falsifier:** If the three reports differ structurally, there is no template to extract.
**Connects to:** `memory/wiki/offers/index.md`
**Sources:** None; internal example.
**Route:** build
```

---

## 15. Promotion routing

When the user picks an idea, do real routing.

### Intents

| Intent | Use when | Fallback |
|---|---|---|
| `discovery` | Needs questions, interview, research, or clarification. | `dreams/promoted/YYYY-MM-DD-NNN-{slug}.md` with open questions. |
| `build` | Needs implementation, automation, prototype, or artifact. | `dreams/promoted/YYYY-MM-DD-NNN-{slug}.md` with scoped build note. |
| `decision` | Needs durable decision/trade-off. | Append to `dreams/decisions.md`. |
| `content` | Needs draft-first writing. | `dreams/promoted/YYYY-MM-DD-NNN-{slug}.md` with draft. |
| `task` | Needs a discrete action. | `dreams/promoted/YYYY-MM-DD-NNN-{slug}.md` with task details. |

### Resolution order

1. If `routes:` explicitly names a capability or `file`, obey it.
2. Else if a matching host capability is visibly exposed, use it and state why.
3. Else use fallback.

Never claim to invoke a skill/tool/command that is not visible. Never ignore a
configured explicit route unless unsafe.

After promotion:

- update the idea's state in `dreams/index.md`;
- append a `promoted` entry to `dreams/ledger.md`;
- include resulting file/route path;
- keep external outputs draft-first.

---

## 16. Scheduled mode

Scheduled mode is for cron/nightly runs.

Detect it from `mode: scheduled` or clear scheduler context. Behavior:

- create dream file;
- update index;
- append run status to `dreams/run-log.md`;
- clear seeds only after successful dream + index writes;
- do not promote or execute routes;
- do not ask questions unless the user is present;
- do not mutate external systems;
- continue without web if needed and log degradation.

Suggested run-log entry:

```markdown
## [2026-06-09 23:00] success | Scheduled dream
- dream_file: dreams/2026-06-09-001-dream.md
- ideas: 3
- seeds_consumed: 2
- warnings: web unavailable; web-derived ideas marked hypotheses
```

---

## 17. Privacy

Treat `dreams/` as private by default. Recommend `.gitignore` for public repos:

```gitignore
# Muse private dream data
dreams/
```

Rules:

- Do not store secrets, credentials, tokens, private keys, session paths, or API
  values.
- Do not quote raw private communications unless the user explicitly provides and
  asks to use them; prefer summaries.
- Redact client/person names when appropriate.
- External-facing content stays draft-first.
- If a source is sensitive, cite a safe pointer and summarize safely.

---

## 18. Optional setup interview

When explicitly invoked with "configure Muse" or similar:

1. Ask language first, in English plus the most likely local language.
2. Confirm memory style: adapt to existing, bootstrap, or none.
3. Capture 2-4 priorities across work and life.
4. Confirm lenses, depth, web, divergence, scheduled mode, and route preferences.
5. Write `dreams/muse-config.md`.

Keep it short. Recommend defaults.

---

## 19. Quality rubric

A dream passes when it is:

| Criterion | Pass | Fail |
|---|---|---|
| Language | Configured/detected language | Wrong or mixed language |
| Curated | Few deep mini-essays | One-line dump |
| Grounded | Links resolve; web claims cited | Invented facts or dead links |
| Evidence-traced | Each idea has assumption/nodes/confidence/falsifier | Missing trace |
| Autonomous | Detects/defaults/logs assumptions | Blocks for inferable input |
| Divergent | Non-obvious recombinations | Reworded goals |
| Non-redundant | Honors ledger/index/decisions | Repeats dropped/decided ideas |
| Holistic | Work + life lenses | Business-only unless configured |
| Actionable | First step + route | Vague exploration |
| Timely | Action-for-today has reason now | Arbitrary pick |
| Write-safe | No overwrite; non-sensitive seeds copied exactly or sensitive seeds redacted safely | Overwrite, data loss, or seed text silently changed |
| Private | No secrets/raw sensitive content | Leaks sensitive material |
| Cron-safe | Scheduled run is draft-only | Scheduled run promotes or mutates external systems |

Two consecutive passes per relevant eval scenario are required before release.
