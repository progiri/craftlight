## What it changes
<!-- The gist. Which skill(s): task / plan / brief / debug / code-review / craft-graph. -->

## Checklist
- [ ] Ran the affected skill's regression scenarios (`skills/<skill>/tests/scenarios.md`), updated "Last run"
- [ ] JSON manifests are valid (`marketplace.json`, `plugin.json`)
- [ ] For a behavior change — bumped `version` in `plugin.json` and recorded it in `CHANGELOG.md`
- [ ] Durable decisions / gotchas carried into the graph (`docs/graph/`) as a node with a `file:line` proof

## Verification
<!-- The result of running the scenarios (N/N PASS), the JSON validation output. -->
