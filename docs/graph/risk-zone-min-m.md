# risk-zone-min-m: the risk zone → minimum M

Type: invariant
Area: core
Proof: `plugins/craftlight/skills/task/SKILL.md:36`

## Gist
auth, money, migrations, concurrency, data deletion → minimum mode M, even for a one-line edit. The canonical list; playbooks point here.

## Rationale
In these zones the cost of an error is disproportionate to the size of the diff; the light mode (S) gives no spec, no criteria check, no review pass.

## Risks
De-escalation or classifying as S on a risky edit → a silent miss of an auth/money bug with no artifact and no check. The guard isn't bypassed by user pressure.

## Edges
- affects [[ceremony-proportional]]
- affects [[worst-signal-wins]]
