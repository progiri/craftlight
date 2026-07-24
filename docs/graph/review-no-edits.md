# review-no-edits: a review doesn't edit code

Type: invariant
Area: code-review
Proof: `plugins/craftlight/skills/code-review/SKILL.md:54`

## Gist
Zero edits to code files — including "little things along the way". The only exception is the Full mode's report file. "Fix what's found" → a new task for `task`.

## Rationale
Mixing review and edits blurs the verdict and the object: a review should hand back findings as a checklist, not silently change code.

## Risks
An edit "along the way" during a review → an undeclared behavior change outside the checklist and without checking against the criteria.

## Edges
- affects [[false-positive-costlier]]
