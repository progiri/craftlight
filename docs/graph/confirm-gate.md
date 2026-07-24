# confirm-gate: execution — only after an explicit ok on the plan

Type: invariant
Area: core
Proof: `plugins/craftlight/skills/task/SKILL.md:51`

## Gist
In every task mode, execution starts only after an explicit user ok on the shown plan
(S — a reformulation with the decision, M/L — a spec draft); silence ≠ ok; raising the mode passes the gate
again. An advance ok ("just do it" in the task statement) lifts the wait, but doesn't apply in the risk zone.

## Rationale
A misunderstanding is caught most cheaply before the first edit: one round-trip costs pennies against rolling back
execution on a misunderstood task. Rejected: "shown it — continue right away, the user will interrupt"
(the S norm before 0.4.3) — it assumes the user is watching in real time; in asynchronous work there's no one to interrupt.

## Risks
A start without an ok → execution on a misunderstood task, a rollback costlier than any ceremony. An advance ok
carried into the risk zone → a risky edit without explicit consent: there the gate isn't bypassed, just like "minimum M".

## Edges
- affects [[ceremony-proportional]]
- depends-on [[risk-zone-min-m]]
