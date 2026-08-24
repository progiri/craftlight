# block-insert-announced: the first block insertion is announced, maintenance is silent

Status: active
Type: decision
Area: claude-block
Source: wave-proto
Proof: `plugins/craftlight/skills/task/templates/CLAUDE-block.md:13-22`

## Gist
The block upsert is not uniformly quiet. A first insertion (steps 1–2 — no CLAUDE.md, or no marker) gets one
line in chat; a version bump (step 4) stays silent. Step 3 performs no edit, so it is untagged.

## Why
Consent asymmetry, not edit size: a first insertion writes into a file the user may not know exists, while a
bump only maintains text they already consented to. Rejected: uniform silence (the original rule — it hides
the one edit the user hasn't agreed to) and a separate "task" ceremony (it is still a single Edit either way).

## Risks
Announcing every bump turns a free self-heal into recurring noise in every adopter's session; silencing the
first insertion means editing the user's CLAUDE.md without them ever being told.

## Edges
- part-of [[claude-block-selfheal]]
- depends-on [[block-version-own]]
