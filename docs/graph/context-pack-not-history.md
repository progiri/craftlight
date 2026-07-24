# context-pack-not-history: for the subagent — a context pack, not history

Type: invariant
Area: core
Proof: `plugins/craftlight/skills/task/modes/l.md:16`

## Gist
The executing subagent is handed a context pack (its checklist section + files + contracts + relevant constraints), not the log/other phases/a retelling of the project.

## Rationale
Reloading the full context by every executor is the main token multiplier in heavy pipelines.

## Risks
Passing the chat history instead of a pack → quadratic token growth as the number of phases/subagents grows.

## Edges
- part-of [[ceremony-proportional]]
