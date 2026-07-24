# false-positive-costlier: a false positive costs more than a miss

Type: decision
Area: code-review
Proof: `plugins/craftlight/skills/code-review/SKILL.md:8`

## Gist
A false finding burns trust in the whole report, so the unproven doesn't make it into the report: every finding is a `file:line` proof + a failure scenario, and verification filters out the disputable.

## Rationale
A single false Blocker devalues the whole report more than a missed nit does. Trust is a review's main asset.

## Edges
- affects [[graph-proof-required]]
