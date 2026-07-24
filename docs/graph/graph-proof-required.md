# graph-proof-required: a graph node without proof doesn't exist

Type: invariant
Area: craft-graph
Proof: `plugins/craftlight/skills/craft-graph/SKILL.md:8`

## Gist
Every graph node is backed by a `file:line` proof — where the decision lives or shows up in the code. Without proof it's guesswork, there's no node. The graph records "why it's this way", not restating the code.

## Rationale
An unproven "pretty" node misleads worse than its absence does; a proof makes the graph verifiable and updatable.

## Risks
Guessed nodes → over time the graph drifts from the code and loses trust (like a false Blocker in a review).

## Edges
- affects [[craft-map-decisions-in-graph]]
