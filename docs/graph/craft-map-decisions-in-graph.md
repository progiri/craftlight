# craft-map-decisions-in-graph: CRAFT — the map, decisions — into the graph

Type: decision
Area: task-router
Proof: `plugins/craftlight/skills/task/SKILL.md:67`, `plugins/craftlight/skills/task/templates/CRAFT.md:8`, `plugins/craftlight/skills/task/templates/CONTEXT.md:1`

## Gist
CRAFT.md holds the project description (the "What it is" section — the only prose one) and a map with
pointers (entry points, modules, links). Rationale, invariants, and gotchas go as nodes into
`docs/graph/`, not into CRAFT.md. There's no separate PROJECT.md — "what we're building and why" lives in
that same map.

Exception (0.10.0, a deliberate revision of the boundary "everything contextual — into the map", brief
`docs/crafts/context-vocab/`): the domain glossary lives as a separate root `CONTEXT.md`, not a map
section — for the sake of cross-agent use (the file is readable by any agent without craftlight). The map
points to it, the reading rule is delivered by block v8, replenishment — wrap M/L
(`plugins/craftlight/skills/task/modes/m.md:30`).

## Rationale
A split of roles: CRAFT.md is read on every task (the token tax → minimum), while "why it's this way"
keeps growing — its place is in the graph. This way there's no duplication with CLAUDE.md and no desync. The
"What it is" section was added in 0.8.1 (brief `docs/crafts/project-context/`): the project description lived
nowhere — the discipline doesn't guarantee a README; a separate PROJECT.md was rejected as a file without a
consumer and a third place to desync.

## Edges
- depends-on [[graph-proof-required]]
- affects [[spec-travels-with-branch]]
