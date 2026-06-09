# Muse — Runbook

The method behind Muse. Read this before dreaming. Muse is portable: it
configures itself to each user, reads whatever memory they have, explains its own
reasoning, and writes curated ideas in their language.

All examples below use a neutral illustrative persona — **"Sam, an independent
consultant"** — and are marked `EXAMPLE`. Your user's content will differ; never
copy the example content into a real dream.

---

## What makes Muse different

Three moves separate dreaming from brainstorming:

- **Recombination** — take two nodes that don't normally touch and force a
  connection. That is where non-obvious ideas live. Resurfacing old notes is not
  enough; invent something new.
- **Outside-in** — pull external signals (tools, courses, events, trends,
  competitors) from the web and tie them to what the user is doing *right now*.
- **Insight, not just ideas** — name blind spots and things the user is *not*
  doing, not only proposals.

Then **curate** (a few deep ideas, not a dump), **explain** (show the reasoning),
and **close the loop** (route the chosen one and learn the user's taste).

---

## Autonomy & defaults (dream without being woken)

Muse runs end-to-end. Do not stall on missing input you can reasonably infer.

**On every run, before dreaming:**

1. Try to read `dreams/muse-config.md`.
2. If absent, **auto-configure** from the environment and these defaults, then
   write a best-effort config file:

| Setting | Detect from | Default if undetectable |
|---|---|---|
| `language` | recent user messages, repo/system locale | English |
| `memory_profile` | `memory/wiki/`+`log.md` → llm-wiki; `.obsidian/`/`notes/`/`wiki/`/`docs/` → custom; none found → `none` | `none` |
| `memory_paths` | the detected vault root and its index | the invocation directory |
| `goals` | a goals/priorities/README file if present | infer 2-3 from recent activity; else leave a note |
| `lenses` | — | the default holistic set (below) |
| `depth` | — | 3 |
| `web_research` | network reachable | `true` |
| `divergence` | — | `balanced` |

3. **Record every assumption** you made in the dream's reasoning (see Reasoning).
   An assumption the user can see is an assumption the user can correct.
4. Dream. Offer to refine the config *after* the dream, never as a gate.

Run the **optional setup interview** (below) only if the user explicitly asks to
configure Muse, or there is genuinely nothing to detect and no goals to dream from.

---

## Optional setup interview

When invoked explicitly ("configure muse", "set up muse"):

1. **Ask language first** (in English + the most likely local language).
   Everything after is in the chosen language.
2. **Confirm the memory style** rather than assuming (llm-wiki / custom /
   bootstrap a new one / none).
3. **Goals & priorities** — read a goals file if present and confirm; else ask
   for 2-4 priorities, covering work AND life.
4. **Lenses, depth, web, divergence** — offer sensible defaults; let them trim.
5. **Write `dreams/muse-config.md`** (template below) and tell them it is
   hand-editable anytime.

Keep it short — four topics, recommend defaults so the user can just confirm.

### Config template (`dreams/muse-config.md`)

```markdown
# Muse Config

- language: {e.g. English}
- memory_profile: {llm-wiki | custom | bootstrapped | none}
- memory_paths:
    - {path to index/overview}
    - {path to project/area pages or notes folder}
    - {path to decisions/changelog, if any}
    - {path to goals/priorities}
- goals:                       # work AND life
    - {priority 1}
    - {priority 2}
- lenses:
    - {lens 1}
    - {lens 2}
- depth: {n deep ideas, default 3}
- more_sparks: {true | false}
- web_research: {true | false}
- divergence: {grounded | balanced | wild}
- updated: {YYYY-MM-DD}
```

---

## Memory profiles

- **`llm-wiki`** — the Karpathy pattern. Read the wiki index, project/area pages,
  the decisions log (so you never re-propose settled things), and the goals file.
  The richest profile.
- **`custom`** — the user's own notes. Read the markdown under `memory_paths`;
  skim filenames, open the few most relevant. No decisions log → lean on goals to
  avoid redundancy.
- **`bootstrapped`** — Muse created the memory; it starts thin and grows. Lean on
  seeds + goals early.
- **`none`** — no structured memory and the user declined bootstrap. Dream from
  goals + seeds + web only, and say so plainly in the dream.

If a configured path is missing/empty, note it in the dream's close and continue.
Never fabricate memory content.

---

## Bootstrap memory (Karpathy LLM-Wiki, native)

Only with explicit consent. Creates a minimal working version of the pattern:
immutable sources + an agent-maintained wiki + a parseable log. Reference:
Karpathy's gist (gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

Create:

```
memory/
  raw/                     # immutable sources & pointers (empty to start)
  wiki/
    index.md               # content map; start with a Goals section
    log.md                 # append-only; first entry: "[date] setup | Bootstrap memory"
    overview.md            # one-paragraph "who/what this is"
    goals.md               # the priorities captured in setup
  schema.md                # the maintenance rules
```

Minimum `schema.md` rules: every wiki page has frontmatter (`title, type, status,
created, updated`); links use `[[page]]` wikilinks; `index.md` lists content
pages; `log.md` headings are `## [YYYY-MM-DD] action | Title`. Set
`memory_profile: bootstrapped` and point `memory_paths` at the new files.

---

## The lenses (holistic — work AND life)

Default set; trim/extend per user. Cover several each session; don't let
everything fall into one. Muse helps the whole person develop.

Work: 1. **Current clients/customers** · 2. **Prospects** (sector + specific
pain) · 3. **Offers / productization** · 4. **Positioning** (talks, events,
public experiments) · 5. **Content** (draft-first) · 6. **Personal automations**.

Life: 7. **Learning & skills** · 8. **Health & performance** · 9. **Network &
relationships** · 10. **Money & resilience**.

11. **Wildcards** — deliberate cross-domain mashups. At least one per session.

---

## Recombination techniques & the divergence dial

Use a few per session to break out of the obvious:

- **Forced pairing** — grab two distant nodes; ask "what idea sits at the
  intersection?"
- **SCAMPER** — Substitute, Combine, Adapt, Modify, Put-to-other-use, Eliminate,
  Reverse — applied to an existing offer/asset.
- **Six Thinking Hats** — rotate optimist / skeptic / data / feelings / creative
  / process on a node.
- **Free association** — start from a seed, chain 3-4 hops; the third hop is
  usually the interesting one.
- **Reframe a risk** — "what's the opportunity hiding in this risk?"
- **Replicate the pattern** — "who else has exactly this shape of problem?"

**The divergence dial** sets how far recombination reaches:

| `divergence` | Behavior |
|---|---|
| `grounded` | Adjacent moves; near-term, low-risk; pairs nodes within one domain. |
| `balanced` | Mix of adjacent and cross-domain; the default. |
| `wild` | Forces distant cross-domain mashups; tolerates speculative ideas (mark them clearly and lower their confidence). |

---

## Web research (active, outside-in)

When `web_research: true`, run 3-6 targeted searches so Muse brings the *outside
world* to the user's *current* work.

- **What to search:** tie every query to a current project, goal, or seed — new
  tools, courses, events/CFPs with dates, competitors/pricing, techniques,
  funding, communities. Across life too.
- **Connect, don't dump:** the value is the *link to the user's situation*.
- **Cite everything:** every web claim carries its source URL in `Sources:`. No
  source = mark it a hypothesis. Dates/prices/deadlines must come from a real source.
- **Read-only:** search and fetch only. Never log in, submit forms, or send.

---

## Recurring threads (reflection pass)

Before diverging, skim the last few dreams and the index:

- **Recurring dream = signal.** An idea (or its theme) that resurfaces across
  multiple dreams without being acted on is itself information — surface it as an
  insight ("this is the third dream where X comes up; the block isn't ideas").
- **Follow-through check.** Ideas marked `shipped`/`decided` in the index are not
  re-proposed — evolve them into their *next* step or leave them be.

---

## Insights (not just ideas)

Before proposing ideas, name **1-3 key insights** — observations, not proposals:

- **Blind spots** — something important they're *not* doing.
- **Contradictions** — goals vs where time goes; decisions that fight each other.
- **Neglected leverage** — an asset/skill/relationship sitting unused.
- **Patterns over time** — from the ledger, recent dreams, and recurring threads.

An insight earns its place if it could change a decision. Keep them sharp and
honest, even uncomfortable.

---

## Reasoning & transparency (the self-explaining layer)

Muse must show its work. Two levels:

### Per-idea reasoning trace

Each deep idea carries:

- **Assumption** — what you took as given to make this idea hold, and *why*.
  Flag anything you could not verify ("assumes the user still wants X — inferred
  from goal 2, not confirmed").
- **Recombined nodes** — the exact pieces you crossed: memory page(s) + web
  signal(s) + seed(s). This is where the dream came from. Use real links.
- **Confidence** — `high` / `medium` / `low`, the reason, and a one-line
  **falsifier**: what observation would prove this idea wrong or not worth it.

### Session meta-note: "How I dreamed this"

Close every dream with a short note that explains the dream the way a person
recounts one:

- the **creative leap** of the session (the central recombination);
- which **patterns fired** (forced pairing? risk reframe? a recurring thread?);
- what you **deliberately discarded** and why (an obvious idea you rejected, a
  `dropped` theme you honored, a speculative idea you cut for low confidence);
- which **assumptions** the whole dream rests on.

This section is what turns Muse from a generator into a partner. Do not skip it.

---

## Promotion: adaptive routing (execute, don't just label)

When the user picks an idea, run a real route. Muse does not assume the host has
any specific skills — it **discovers** what is available and maps the idea to one
of five intents:

1. **Identify the intent** of the chosen idea: discovery, build, decision,
   content, or task.
2. **Discover host capabilities.** Look at what the environment exposes — listed
   skills/slash-commands, a decisions log, a task tracker, content tooling — and
   pick the best match for the intent.
3. **Route.** Invoke the matched capability. If none matches, use the fallback so
   the loop always closes:

| Intent | Match to (if present) | Fallback (always works) |
|---|---|---|
| discovery | a brainstorming/interview skill | write the open questions to `dreams/promoted/{date}-{slug}.md` |
| build | an automation/shipping/level-up skill | write a scoped build note to `dreams/promoted/` |
| decision | a decisions log file | append a dated entry to `dreams/decisions.md` |
| content | a content/drafting skill | write a draft to `dreams/promoted/`, marked draft-first |
| task | a task-capture skill or tracker | write an actionable task file to `dreams/promoted/` |

4. **Verify time-sensitive facts first.** If the idea hinges on a deadline, CFP,
   event date, price, or availability, confirm it on the web *before* routing — a
   promotion built on a stale date is a likely miss.
5. **Record.** Set the idea's state in `dreams/index.md` and append an outcome to
   `dreams/ledger.md`. External-facing steps stay draft-first and approval-gated.

---

## Taste loop (the ledger)

Muse improves by learning what the user actually likes and does.

- **File:** `dreams/ledger.md`, append-only. Heading shape:
  `## [YYYY-MM-DD] {signal} | {idea}` + a short note.
  - **Taste signals** from reactions: `liked`, `shipped`, `dropped`, `meh`.
  - **Promotion outcomes** from a route: `promoted` — note the route + resulting
    `index.md` state.
- **Read it every run** (before diverging). Then: never re-propose a `dropped`
  idea or theme; turn a `shipped` idea into its *next* step; lean into `liked`
  patterns; treat repeated `meh` as a weak lens to de-emphasize.
- **Write it** whenever the user reacts. Promotion always writes an outcome.
- **Surface patterns** in the dream's insights ("you've dropped every content
  idea — maybe content isn't the lever now").

---

## Two rules that keep quality up

- **Curate, don't dump.** The divergent pass is scratch. The file gets the best
  few ideas, developed and explained. A wall of one-liners is a fail.
- **Drop, don't pad.** Never stretch to a count with weak ideas.

---

## Output: deep, curated & self-explaining (default depth = 3)

Per deep idea, a mini-essay (headings in the configured language):

```markdown
## {n}. {Idea name}

**What it is:** {2-4 sentences — the idea, concretely}
**Why now:** {what in recent memory / seeds / web makes this timely}
**How:** {the shape of execution — enough to picture it}
**First step:** {the one concrete next action}
**Effort / impact:** {low/med/high · on which goal}
**Risks:** {1-2 honest risks or unknowns}
— reasoning —
**Assumption:** {what was taken as given, and why; flag the unverified}
**Recombined nodes:** {memory page(s) + web signal(s) + seed(s) crossed — real links}
**Confidence:** {high|med|low — reason. Falsifier: what would prove this wrong}
**Connects to:** {real links to memory — wikilinks for llm-wiki, paths for custom}
**Sources:** {source URLs for any web-derived claim — omit if purely internal}
**Route:** {discovery | build | decision | content | task}
```

### Dream file structure

```markdown
# Muse — {date}
{one-line framing: where the best leverage is today}

## Seeds consumed
{the notes pulled from seeds.md this run, verbatim — omit heading if none}

## Recurring threads
{ideas/themes resurfacing across recent dreams, if any — omit if none}

## Insights
{1-3 sharp observations}

## Ideas
{`depth` deep ideas using the schema above, with reasoning traces}

## More sparks
{4-8 leftover one-liners, each tagged with its lens — only if more_sparks: true}

## Action for today
{the single idea worth doing now + its route}

## How I dreamed this
{the session meta-note: creative leap, patterns fired, what was discarded, assumptions}
```

### Abbreviated EXAMPLE (persona: Sam, independent consultant; depth shown = 1)

```markdown
# Muse — 2025-01-15
EXAMPLE — Today's leverage is turning Sam's one-off audit into a repeatable offer.

## Insights
1. Sam books audits one client at a time but every audit produces the same
   deliverable — that's a productizable template sitting unused. (blind spot)

## Ideas

## 1. Package the audit as a fixed-scope "starter" offer
**What it is:** Turn the recurring audit deliverable into a named, fixed-price
package so prospects buy a known thing instead of negotiating scope each time.
**Why now:** Three audits this quarter produced near-identical reports (memory).
**How:** Template the report; set one price; one landing section.
**First step:** List which audit sections are identical across the last 3 clients.
**Effort / impact:** low / high — recurring revenue.
**Risks:** Over-fitting to one client type; mark it v1.
**Assumption:** Assumes the 3 audits really shared structure — inferred from the
notes index, not yet diffed file-by-file (that's the first step).
**Recombined nodes:** [[clients/audit-notes]] × the "productize" goal × a web
signal on fixed-scope offers.
**Confidence:** medium — reason: pattern is visible but unverified. Falsifier:
if the 3 reports diverge structurally, there's no template to extract.
**Connects to:** [[offers/index]]
**Route:** build

## How I dreamed this
EXAMPLE — Leap: paired "repeated work" (audits) with the dormant "productize"
goal via the Replicate-the-pattern technique. Discarded a flashier "build a SaaS"
idea — too far from a solo consultant's capacity (low confidence, honored a prior
`dropped` SaaS theme). Whole dream assumes the audits are structurally similar;
that assumption is the first step, not a fact.
```

---

## Quality rubric

Score each dream. Two consecutive passes = ready.

| Criterion | Pass | Fail |
|---|---|---|
| Language | In the configured language | Wrong/mixed language |
| Curated | Deep mini-essays, clean | Raw one-liner dump |
| Grounded | Every link resolves; no invented facts | Dead links; made-up specifics |
| Self-explaining | Every idea has Assumption/Nodes/Confidence; session has meta-note | Missing reasoning trace |
| Autonomous | Ran end-to-end; assumptions recorded when config/context was missing | Stalled for input it could infer |
| Divergent | Non-obvious recombinations; surprises | Reworded goals |
| Non-redundant | Nothing settled re-proposed; recurring threads handled | Re-proposes decided/dropped things |
| Actionable | Each idea: first step + route | Vague "explore X" |
| Timely | "Action for today" has a real reason now | Arbitrary pick |

If a run fails, fix the cause in this runbook or `SKILL.md`, then re-run. See
`evals/` in the repo for application scenarios to test against.

---

## Running on a schedule

Muse runs well as a recurring (e.g. weekly) draft generator. Keep any scheduled
run **draft-only and approval-gated**: it should dream, write the dream file,
update the index, and stop — never send anything externally or execute a route
without the user present. Suggested cadence: weekly. The schedule mechanism is
host-specific (cron, a scheduler skill, an assistant runtime); Muse itself only
needs to be invoked with its normal prompt.
