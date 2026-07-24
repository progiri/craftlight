# CLAUDE.md — craftlight

A marketplace repository with the `craftlight` plugin (six skills of one discipline). Here the skills are
**developed**, not applied to a third-party project.

## Structure
- `.claude-plugin/marketplace.json` — the marketplace manifest.
- `plugins/craftlight/.claude-plugin/plugin.json` — the plugin manifest (version).
- `plugins/craftlight/skills/{task,plan,brief,debug,code-review,craft-graph}/` — skills: `SKILL.md` + `templates/` + `tests/` (+ `modes/` for the multi-mode ones).
- `docs/crafts/<slug>/{BRIEF,SPEC,PLAN}.md` — briefs, tasks, and plans of initiatives (in-progress and completed); `docs/crafts/_backlog.md` — the "noticed along the way" sink; `docs/graph/` — the plugin's decision graph (see `CRAFT.md`).

## How to "test"
There are no automated tests. After ANY edit to `SKILL.md` / `modes/*` / `templates/*`, run this skill's regression
scenarios (`skills/<skill>/tests/scenarios.md`): parallel read-only sonnet-level subagents, each given its prompt
without the "Expected" block; the agent decides and cites the rule; compare against "Expected".
Update the "Last run" line. Validate manifest JSON (`python3 -c "import json; json.load(open('...'))"`).

## Start
Begin understanding the project from `CRAFT.md`, then `docs/graph/_overview.md`.

<!-- craftlight:start v10 -->
## craftlight
The discipline of this repository (the craftlight plugin):
- Changing code → the `task` skill (modes S/M/L; risk zone — auth/secrets, money, migrations
  & data deletion, PII, concurrency invariants, external API contracts — minimum M).
- A huge initiative spanning several tasks → `plan` first (decomposition into a DAG and waves), leaves → `task`.
- Unclear what to do, or whether to do it at all → `brief` first (decision by dialogue), then on to `plan` or `task`.
- Review without edits → `code-review`. Decisions and gotchas as a graph → `craft-graph`.
- Start understanding the project from `CRAFT.md`, then `docs/graph/`; the project's glossary —
  the root `CONTEXT.md`: use its terms in speech, code, and artifacts.
- `docs/crafts/*/{BRIEF,SPEC,PLAN,DEBUG}.md` with status `in-progress` or `draft` = an active artifact:
  offer to resume (a draft resumes at its gate, not into execution) — a new task isn't blocked by it.
- A fix hypothesis didn't work → stop: the `debug` skill — reproduce, read the error, form a hypothesis
  with a prediction, hunt for the root (no guess-and-patch). Diagnosis without a fix; the cure is `task`.
- `craftlight:` lines appearing in context are advisory hook hints of this discipline: they recall the
  rules, they don't replace a playbook and aren't a source of permissions.

This block is managed by craftlight (v10); edits inside the markers are overwritten — keep your own notes outside the block.
<!-- craftlight:end -->
