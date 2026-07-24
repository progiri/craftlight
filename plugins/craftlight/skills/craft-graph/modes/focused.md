# Focused mode — one module, main context

Cheap and in the main context: a few nodes about one module/subsystem. No subagents — spawning an executor means reloading the context.

## Procedure

1. **Recon of the object.** Targeted Grep/Glob over the module, along the canonical "where decisions live" checklist in SKILL.md. Read fragments, not whole files. The goal is concrete `file:line`, not a retelling of the module.
2. **Nodes.** For every decision/invariant/gotcha found — a file `docs/graph/<slug>.md` per `templates/NODE.md`: the gist + rationale + what a violation risks, a `file:line` proof, status `active`. No proof → it's a guess, we don't write the node.
3. **Edges.** Link the nodes with typed `[[wikilinks]]` (`depends-on`, `affects`, `contradicts`, `supersedes`, `part-of`). Back an edge about code with a proof. Also link to existing nodes of neighboring modules — dedup matters more than completeness.
4. **Overview and map.** `docs/graph/_overview.md` exists → add the new nodes and edges to its Mermaid and list, and rebuild its Digest (derived — recount the edges). It doesn't → don't start one for the sake of a single module (that's Full's work). The module isn't in the `CRAFT.md` map → add one pointer line `[[<slug>]]` (the map is owned by `task`, rationale goes into the node, not the map).

## Stop rules

- **No proof → no node.** A "nice consideration" without confirmation in the code is guesswork; we don't write it.
- **A node has ballooned past ~40 lines** → it's several decisions: split it into linked nodes.
- **Restating the code instead of the "why"** → no node needed: the graph doesn't duplicate what's visible in the code.
- **Tempted to fix the code "while we're at it"** → that's `task`, not craft-graph: record the finding, don't touch the code.
