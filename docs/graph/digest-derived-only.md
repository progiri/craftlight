# digest-derived-only: the overview Digest carries no claims of its own

Status: active
Type: invariant
Area: craft-graph
Source: graph-digest
Proof: `plugins/craftlight/skills/craft-graph/SKILL.md:46`

## Gist
The overview's Digest (hubs / `contradicts` tensions / questions → `[[slug]]`) is derived-only: every
line is computable from the nodes/edges already on disk. It is rebuilt only by a craft-graph pass that
edits the overview; writers outside craft-graph append to Unplaced and don't touch it.

## Why
An analytical layer (borrowed from graphify's GRAPH_REPORT) is useful, but a free-written digest would
smuggle unproven claims past the "no proof → no node" gate and give the overview a second source of
truth. Derived-only keeps "the overview is derived from the nodes" true after adding the layer.

## Risks
An underived digest line is an unproven claim that consumers may carry as a constraint; a digest every
writer rewrites breaks the cheap-writer contract of the Unplaced queue.

## Edges
- part-of [[area-facet-in-node]]
- depends-on [[graph-proof-required]]
