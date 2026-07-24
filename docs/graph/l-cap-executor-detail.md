# l-cap-executor-detail: L/PLAN caps protect the reader; the cut-priority protects executor detail

Status: active
Type: decision
Area: core
Source: l-spec-caps
Proof: `plugins/craftlight/skills/task/templates/SPEC.md:59-62`

## Gist
Artifact caps are a read-side budget (specs are read many times: resume, hooks, wrap), so they stay.
But in L and PLAN — where an expensive model authors once and cheap subagents execute many times —
the cut-priority on a cap hit is: prose first, NEVER file paths, Contracts, or acceptance criteria
(PLAN: never the task table, the DAG, or the Contracts between tasks; `skills/plan/templates/PLAN.md:67-69`).

## Why
The old rule cut "prose and checklist detail" — discarding exactly the executor-grade output of the
expensive author. Rejected: raising caps everywhere (M's author = executor, the premise doesn't apply;
read-tax grows for nothing) and removing caps (density beats volume for a weak reader — a load-bearing
constraint at line 250/400 is likelier lost than at 40/80). See docs/crafts/l-spec-caps/BRIEF.md.

## Risks
Cutting contracts/paths to fit the cap starves the subagent's context pack — it re-derives or guesses
paths and interfaces, the exact failure L's delegation protocol exists to avoid.

## Edges
- part-of [[ceremony-proportional]]
- affects [[context-pack-not-history]] (the pack is built from what the cut-priority protects)
