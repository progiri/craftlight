# CRAFT: craftlight

<!-- Repo hub-map: the starting point after CLAUDE.md. "What it is" is prose; the rest are only
     pointers; "why it's this way" lives in docs/graph/. -->

## What it is
craftlight is a plugin for Claude Code: six skills of one discipline for developing with an AI agent
(the ladder brief → plan → task with a debug subcycle, plus code-review and craft-graph). The problem:
an agent's prompt discipline degrades — rules fall out of context under the pressure of compaction,
decisions and state are lost between sessions, ceremony either smothers the small stuff or is absent where
it's risky. The point: to make the agent's work predictable — ceremony proportional to the task, state living
in artifact files (BRIEF/SPEC/PLAN, the decision graph) and surviving any context break. For whom: developers
running projects through Claude Code. This repository is a marketplace where the skills are developed and
tested; they are applied in target projects after the plugin is installed. Doesn't do: hard enforcement — the
hooks are advisory-only, the discipline rests on prompts and artifacts, not on blocks.

## Entry points
- The marketplace manifest — `.claude-plugin/marketplace.json`
- The plugin manifest (version) — `plugins/craftlight/.claude-plugin/plugin.json`
- Skills (entry `SKILL.md`s; task/code-review/craft-graph are mode routers, plan, brief, and debug are single-mode) — `plugins/craftlight/skills/{task,plan,brief,debug,code-review,craft-graph}/SKILL.md`

## Module map
- `skills/task/` — the S/M/L task router + owner of CRAFT.md and the craftlight block (`templates/{SPEC,CRAFT,CLAUDE-block}.md`)
- `skills/plan/` — the planner ABOVE task: initiative → DAG of tasks + waves (`templates/PLAN.md`, single-mode); [[plan-above-task]]
- `skills/brief/` — decision by dialogue ABOVE plan: discussion → BRIEF.md → hand-off to task/plan (`templates/BRIEF.md`, single-mode); [[brief-above-plan]]
- `skills/debug/` — root-cause hunt BELOW task: diagnosis without a fix, a hypothesis log (`templates/DEBUG.md`, single-mode); [[debug-inside-task]]
- `skills/code-review/` — review without edits (`modes/{express,full}.md`)
- `skills/craft-graph/` — a graph of decisions/gotchas (`modes/{focused,full}.md`)
- `hooks/` — plugin hooks (advisory-only): a state-push of specs after compact/resume + a gate-nudge on a draft spec (`hooks.json`, `*.py`, `tests/`); [[hooks-give-teeth]]
- ⚠ each skill: editing `SKILL.md`/`modes`/`templates` → running `tests/scenarios.md` is mandatory
- `docs/crafts/<slug>/{BRIEF,SPEC,PLAN}.md` — briefs, tasks, and plans of initiatives; `docs/crafts/_backlog.md` — the "noticed along the way" sink ([[backlog-sink]]); `docs/graph/` — the decision graph (below)

## Deeper
- `CONTEXT.md` — the domain glossary (discipline terms)
- `docs/graph/_overview.md` — the plugin's decision graph (Mermaid + node list)
- [[ceremony-proportional]] — the root principle of the discipline
- [[risk-zone-min-m]] — the immovable classification guard
- [[confirm-gate]] — execution only after an explicit user ok on the plan
- [[done-is-observed]] — "done" = an observed result, the unverified is flagged honestly
- [[graph-recall]] — the graph is read before a decision (brief/plan/task recon starts with it)
- [[plan-above-task]] — the planning layer above task (decomposing an initiative into waves)
- [[brief-above-plan]] — the decision layer above plan (decision by dialogue before the task, a file after the commit gate)
- [[debug-inside-task]] — the diagnostic subcycle below task (root with proof, the fix goes through task again)
- [[hooks-give-teeth]] — hooks return rules and state to the context (advisory-only, fail-open)
- [[digest-derived-only]] — the overview Digest is derived from the nodes, no claims of its own
- [[l-cap-executor-detail]] — L/PLAN caps protect the reader; the cut-priority protects executor-grade detail
