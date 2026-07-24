# area-facet-in-node: subsystem membership — a facet in the node itself

Type: decision
Area: craft-graph
Proof: `plugins/craftlight/skills/craft-graph/templates/NODE.md:4` <!-- the "Area:" line; the 1:1 rule — SKILL.md:34 -->

## Gist
A node's subsystem is the "Area:" line in its header; the overview's subgraphs are grouped from the areas (1:1),
not the other way round. A cross-cutting principle (≥2 subsystems) → the area `core`.

## Rationale
Grouping only in the external overview is a second source of truth: a Full rebuild reinvents it from scratch,
a grep for "all nodes of subsystem X" is impossible, and cross-cutting principles get locked into a host subsystem
("one object — one place" — a legacy of the physical shelf). A facet in the node makes the node self-describing,
and the overview mechanically derivable from the nodes.

## Risks
The area diverged from the subgraph → the overview stops being derivable; fix it from the nodes (they are the source
of truth), not from the overview.

## Edges
- affects [[craft-map-decisions-in-graph]]
