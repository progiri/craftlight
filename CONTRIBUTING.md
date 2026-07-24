# Contributing to craftlight

Thanks for your interest in the plugin. Here the skills are **developed**, not applied to a third-party
project — so the rules below are about how to change the skills themselves without breaking the discipline.

## Start
1. Read `CRAFT.md`, then `docs/graph/_overview.md` — the plugin's decision map ("why it's this way").
2. `CLAUDE.md` — how the repository is organized and how to "test" without automated tests.

## Structure
- `.claude-plugin/marketplace.json` — the marketplace manifest.
- `plugins/craftlight/.claude-plugin/plugin.json` — the plugin manifest (**the single source of the version**).
- `plugins/craftlight/skills/{task,plan,brief,debug,code-review,craft-graph}/` — skills:
  `SKILL.md` + `templates/` + `tests/` (+ `modes/` for the multi-mode ones).
- `docs/graph/` — the decision graph; `docs/crafts/<slug>/{BRIEF,SPEC,PLAN}.md` — briefs, tasks, and plans of initiatives.

## How to "test"
There are no automated tests. After **any** edit to `SKILL.md` / `modes/*` / `templates/*`, run this skill's
regression scenarios (`skills/<skill>/tests/scenarios.md`):

- parallel read-only sonnet-level subagents, each given its prompt **without** the "Expected" block;
- the agent decides on its own and **cites the rule** that determined the decision;
- compare the answer against "Expected", update the "Last run" line.

Validate the JSON manifests:

```bash
python3 -c "import json; json.load(open('.claude-plugin/marketplace.json')); json.load(open('plugins/craftlight/.claude-plugin/plugin.json')); print('ok')"
```

CI (`.github/workflows/validate.yml`) runs the official `claude plugin validate` (plugin and
marketplace), JSON validation, the description limit (≤1024, no ": " — it breaks strict YAML), the presence of
`SKILL.md` and `tests/scenarios.md`, the version sync with CHANGELOG, and the graph lint (`[[wikilinks]]` resolve,
overview ↔ nodes, proof paths exist) — but the regression scenarios stay manual (a human runs them via subagents).

## Release (version bump)
1. Bump `version` in `plugins/craftlight/.claude-plugin/plugin.json` per SemVer.
2. Add an entry to `CHANGELOG.md` (move it from `Unreleased`, set the date).
3. The `homepage`/`repository` links in the manifests are static — no need to touch them.
4. Tag `vX.Y.Z` on the release commit.

> `marketplace.json` **doesn't duplicate** the plugin version — it's read from `plugin.json` via `source`.
> This way the version has a single source and there's no drift.

## Commits
Style as in the repo's history: `type(scope): summary` (`feat`, `fix`, `docs`, `test`, `chore`), in English,
naming the affected skill in the scope. Commit a skill edit together with a run of its scenarios.

## Discipline boundaries
- Changing code → the `task` skill (risk zone: auth, money, migrations, concurrency, data deletion
  — minimum mode M).
- Durable decisions and gotchas → a node in the graph (`craft-graph`), a `file:line` proof is mandatory.
- A fix hypothesis didn't work → stop, reproduce, read the error, hunt for the root — no guess-and-patch.
