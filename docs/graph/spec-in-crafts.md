# spec-in-crafts: the spec lives in docs/crafts/<slug>/

Type: decision
Area: task-router
Proof: `plugins/craftlight/skills/task/modes/m.md:8`

## Gist
SPEC.md is created at `docs/crafts/<slug>/SPEC.md` — a folder per task, a home for its whole life (in-progress and done). Not at the root; `docs/specs/` is abolished.

## Rationale
The root doesn't get cluttered, several tasks don't conflict. A folder per slug eliminates the name collision — the `SPEC-<slug>.md` rule is no longer needed. After done the spec stays in place: the task's whole history in one spot.

## Edges
- affects [[spec-travels-with-branch]]
