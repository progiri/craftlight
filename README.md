# craftlight

A disciplined dev workflow for Claude Code in a single plugin. The shared principle of all the skills: **ceremony proportional to the task** — start light by default, escalate only on explicit observable signals. The main enemy is wasted tokens: subagents reloading context and blind loops of "tweaked at random — reran".

## Installation

```bash
claude plugin marketplace add progiri/craftlight
claude plugin install craftlight@craftlight
```

In interactive Claude Code — the same commands via `/plugin marketplace add …` and `/plugin install …`.

> The marketplace name (`craftlight`) is taken from `marketplace.json`, not from the repository name.

## Adopting in an existing project

Nothing needs to be pre-configured — the discipline builds up as you work:

1. **Install the plugin** (commands above) — and just set tasks as usual.
2. **The first invocation of any skill** inserts the managed block into `CLAUDE.md` itself (your text outside the markers is untouched).
3. **The first M/L-level task** bootstraps `CRAFT.md`: the "What it is" section (a project description) + the map. Specs, briefs, and the backlog will appear in `docs/crafts/` as you work.
4. **Optionally, for a large legacy**: say "adopt craftlight" / "seed the graph over the legacy" — the `craft-graph` skill (full) will immediately document the existing decisions and traps as nodes with `file:line` proofs, without waiting for the first wraps.

Don't create `docs/graph/` and `CRAFT.md` by hand in advance: an empty node is worse than its absence, and a map before the first task is a map based on the README.

## What's inside

Six skills united by one discipline and a shared "risk zone" (auth, money, migrations, concurrency, data deletion).

**CLAUDE.md self-maintenance.** On the first run of any skill in a project, craftlight sets up a minimal managed block in the root `CLAUDE.md` (in `craftlight:start/end` markers + a version): which skill when, starting from `CRAFT.md`, the immovable invariants. This way the discipline is in context before the skills even fire. The block is idempotent, updates by version, and doesn't touch your text outside the markers. The reference is [`skills/task/templates/CLAUDE-block.md`](plugins/craftlight/skills/task/templates/CLAUDE-block.md).

### `task` — the router for code-change tasks

The entry point for any work that changes code. It classifies the task and loads the mode's playbook:

| Mode | Artifacts | When |
|---|---|---|
| **S** | none — code right away + 1 atomic commit | 1–2 files, unambiguous criteria, trivial rollback |
| **M** | one `SPEC.md` in `docs/crafts/<slug>/` | 3–10 files, open questions, care needed |
| **L** | `SPEC.md` with phases + external memory | >10 files, architectural decisions, migrations |

The risk zone → minimum M even for a one-line change. Escalation is cheap and allowed at any moment; there is a single de-escalation (M→S) that never bypasses the risk guard. `SPEC.md` (in `docs/crafts/<slug>/`) travels with the git branch — it's a state tracker and the resume mechanism. A ban on guess-and-patch and silent scope creep; something foreign noticed along the way isn't lost and doesn't seep into the code — a single line in `docs/crafts/_backlog.md` (a sink, not a tracker; triage is the human's job).

task also owns **`CRAFT.md`** — the project map in the repo root, the starting point after CLAUDE.md (the "What it is" section — a dense project description, entry points, the module map, pointers into the graph). It bootstraps it on the first M/L, updates it at wrap, and carries durable decisions and gotchas into the graph as nodes (see `craft-graph`). Decisions go into the graph, CRAFT.md holds only pointers.

Triggers on "do / add / fix / refactor / implement", on the flags `--s/--m/--l`, and on "keep going / resume".

### `plan` — the planner above `task`

A layer above `task` for a huge initiative that breaks into several separate tasks. It talks through the nuances over multiple turns (until an explicit "ok, build"), builds a **DAG** of tasks with dependencies, and lays it out into **waves** of parallel execution (topological layers: within a wave the tasks are independent). The artifact is `docs/crafts/<initiative>/PLAN.md` (a living document); each DAG leaf goes back to `task` for its own S/M/L mode.

The boundary is hard: it plans and stops — **it doesn't write code and doesn't orchestrate** execution. Single-mode (no `modes/`). The discussion's decisions settle into the PLAN; they'll reach the graph at a specific task's wrap — a discussion has no `file:line` proof yet.

Triggers on "plan this out / break this epic down / decompose the epic / roadmap / where to start" and on "continue the plan".

### `brief` — decision by dialogue before the task

A step above `plan` and `task`: taken when the direction isn't chosen yet and the choice itself is the work ("is it even worth it", "which approach"). The discipline ladder: `brief` answers "what are we doing and should we" → `plan` "how to break it down" → `task` "how to execute". The dialogue must converge, not wander: each round — options with trade-offs and a recommendation (≤2–3 questions), a duty to push back with proof from the repo instead of rubber-stamping, the pulse "Decided: … / Remaining: …". Until an explicit "ok, commit it" not a single file exists — a dead discussion is free.

The artifact is `docs/crafts/<slug>/BRIEF.md`: options (including the rejected ones and by what), the decision, the verdict **go / no-go / deferred** ("no-go" is a full outcome). The finale is the hand-off: a recommendation of `task` or `plan` (the receiving skill does the classification) and the question "start a task / plan — or nothing for now?"; the chosen skill is invoked in the same session with a pointer to the BRIEF. The boundary: a stated task even with open questions goes straight to `task` (its "spec brief" will refine the details), a chosen initiative straight to `plan`. brief doesn't write to the graph: a discussion has no `file:line` proof.

Triggers on "let's discuss / help me decide / which approach is better / is it even worth it" and on "let's continue the discussion".

### `debug` — the systematic root-cause hunt

A subcycle **below** `task`: the "stop" from the guess-and-patch ban lands here, when the cause is unknown and hypotheses are rejected one after another. The protocol: reproduce → read the error in full → check the obvious (branch/env/cache) → one hypothesis with a testable prediction → a minimal experiment → a log of what was rejected → the root, not the symptom.

The boundary is hard: **it diagnoses and doesn't fix** — even a one-line fix goes to `task` (classification, the gate, a regression test on the root). The log by default has no file — in the chat or the task spec's "Log"; a drawn-out case (≥2 rejected hypotheses or debugging across sessions) → `docs/crafts/<slug>/DEBUG.md`: external memory and resume. Stop rules: three rejected in a row → a change of angle, not a fourth guess; no repro → don't fix blindly; an observation against the model in your head → trust the observation.

Triggers on "figure out why / strange behavior / flaky bug / why does it crash / why is this failing / find the root cause" and from `task`'s stop rule.

### `code-review` — review without edits

It reads and proves but **doesn't edit a single line**. It determines the object (diff / branch / PR / range / module) and picks a mode:

- **Express** — one pass over the lenses, findings into the chat, zero files;
- **Full** — lenses via subagents, verification by a fresh skeptic, a report in `docs/reviews/`.

The finding format is strict: severity + a `file:line` proof + a failure scenario. A false positive costs more than a missed nit, so the unproven is filtered out by verification. The verdict (ok / ok with notes / changes needed) isn't negotiable.

Triggers on "do a review / review this / check the diff / find bugs / is this safe to merge", the flags `--express/--full`.

### `craft-graph` — documenting decisions as a graph

Records what the code doesn't express — "why it's this way" and "where the gotchas are" — as a navigable graph. Nodes `docs/graph/*.md` (one decision / invariant / gotcha, a mandatory `file:line` proof), edges are typed `[[wikilinks]]`. A dual view: you read them as ordinary markdown text, view them as a graph in Obsidian, and the overview `_overview.md` with Mermaid renders right on GitHub. Zero runtime.

- **Focused** — one module/subsystem, in the main context;
- **Full** — the whole base, Explore subagents per subsystem, the overview Mermaid.

Proof is mandatory: a node without `file:line` is guesswork, it doesn't exist. The boundary: not "how to run" (that's CLAUDE.md), not business-logic onboarding (`codebase-reverse-engineering`), not a review (`code-review`), it doesn't edit code. The loop is closed: the graph is fed by `task` (durable decisions settle as nodes at wrap) and is read at the start of decisions — `brief`, `plan`, and the `task` brief begin recon with the graph, and a contradiction of an existing node is named explicitly.

Triggers on "build a decision graph / document the architecture as a graph / a graph of gotchas / map the architecture decisions" and on "adopt craftlight / seed the graph over the legacy".

### Hooks — a deterministic backstop for the discipline

Prompt discipline degrades under context pressure (compaction, long sessions). The plugin hooks ([`plugins/craftlight/hooks/`](plugins/craftlight/hooks/)) return rules and state to the context deterministically — exactly when a phrasing might be forgotten:

- **State-push** (SessionStart on `compact|resume`) — right after a context compaction or resume it brings in the in-progress specs (slug, mode, branch, the first unchecked item): recovery is push-based, not "we hope the model goes and greps".
- **Gate-nudge** (PostToolUse) — when product code is edited with an unclosed `draft` spec, it reminds about the confirmation gate. Self-quieting.

Both hooks are advisory: they block nothing, and stay silent on any ambiguity (fail-open) — a false positive costs more than a miss. The scripts are python3 stdlib with fixture tests (`hooks/tests/`, run in CI).

## Repository structure

```
.
├── .claude-plugin/marketplace.json     ← marketplace manifest
└── plugins/craftlight/
    ├── .claude-plugin/plugin.json      ← plugin manifest
    ├── hooks/                          ← enforcement hooks {hooks.json, *.py, tests/}
    └── skills/
        ├── task/          {SKILL.md, modes/, templates/ (SPEC.md + CRAFT.md), tests/}
        ├── plan/          {SKILL.md, templates/ (PLAN.md), tests/}
        ├── brief/         {SKILL.md, templates/ (BRIEF.md), tests/}
        ├── debug/         {SKILL.md, templates/ (DEBUG.md), tests/}
        ├── code-review/   {SKILL.md, modes/, templates/, tests/}
        └── craft-graph/   {SKILL.md, modes/, templates/, tests/}
```

## Development

All six skills have regression scenarios (`skills/*/tests/scenarios.md`). Run them after any edit to a skill: parallel read-only subagents, each given its prompt; compare the answer against "Expected". The agent must cite the rule that determined the decision — otherwise the phrasing is undiscoverable.

The procedure for contributing, releasing, and validating the manifests is in [CONTRIBUTING.md](CONTRIBUTING.md). The version history is in [CHANGELOG.md](CHANGELOG.md).

## License

MIT — see [LICENSE](LICENSE).
