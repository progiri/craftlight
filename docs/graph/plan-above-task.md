# plan-above-task: plan — the decomposition layer above task (plans, doesn't execute)

Type: decision
Area: plan
Proof: `plugins/craftlight/skills/plan/SKILL.md:8` <!-- positioning; planner-only — same file :12 -->

## Gist
The `plan` skill sits ABOVE `task`: it takes an initiative that by scope is not one task but several,
builds a DAG of separate tasks and lays them out into waves of parallel execution; each leaf → `task`.
The planner plans and stops — it writes no code, doesn't drive execution
(`plugins/craftlight/skills/plan/SKILL.md:12`).

## Rationale
task-L cuts ONE task into phases within a single branch and itself runs into ">5 phases = several tasks"
(`plugins/craftlight/skills/task/modes/l.md:10`). A layer above is needed — decomposing an initiative
into separate tasks/branches/PRs.
Planner-only, not an orchestrator: execution stays with `task`, so that each leaf is classified and
right-sized separately; orchestration in plan would complicate things and break "ceremony is proportional".
Rejected: (1) extend task's L mode — it would bloat L's ceremony; (2) make plan an executor — it would
mix planning with execution and double the classification.

## Risks
plan starts to execute/write code → double classification, loss of leaf right-sizing, a blurred boundary
with task. Child specs nested (`docs/crafts/<initiative>/<leaf>/SPEC.md`) → the task router doesn't find
them by the glob `docs/crafts/*/SPEC.md`: leaves must be flat siblings.

## Edges
- part-of [[ceremony-proportional]]
- depends-on [[spec-in-crafts]]
- depends-on [[risk-zone-min-m]]
