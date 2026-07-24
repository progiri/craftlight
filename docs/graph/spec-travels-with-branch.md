# spec-travels-with-branch: SPEC travels with the branch

Type: decision
Area: task-router
Proof: `plugins/craftlight/skills/task/modes/m.md:16`

## Gist
The checkbox is ticked right away, the spec goes into the same atomic commit as the item's code. State travels with the branch, progress is read from the git log.

## Rationale
SPEC.md = a state tracker and a resume mechanism (in another worktree/on another machine) without retelling the chat history. We stage with an explicit list, not `-A`.

## Edges
- part-of [[ceremony-proportional]]
- affects [[craft-map-decisions-in-graph]]
