# claude-block-selfheal: self-maintenance of the block in CLAUDE.md

Type: decision
Area: claude-block
Proof: `plugins/craftlight/skills/task/templates/CLAUDE-block.md:6`

## Gist
Every craftlight skill, in its Step 0, does an idempotent upsert of the managed block in the root CLAUDE.md (markers + version). Text outside the markers isn't touched.

## Rationale
CLAUDE.md is auto-loaded into every context → the discipline is known to Claude before the skill even fires. A one-time insertion, free thereafter.

## Risks
Editing text outside the markers or a non-idempotent insertion → overwriting the user's notes or duplicating the block.

## Edges
- depends-on [[block-version-own]]
- affects [[craft-map-decisions-in-graph]]
