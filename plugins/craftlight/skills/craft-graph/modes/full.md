# Full mode — the whole base, phases by subsystem

Scope — the whole codebase or several subsystems. The Focused discipline is preserved; the differences are slicing by subsystem and context hygiene.

## 1. Subsystem map

Split the base into subsystems with cheap recon (Glob over the tree, entry points). Delegate the broad sweep to **Explore subagents — one per subsystem**: each returns a list of decisions/gotchas as `file:line` + a one-line gist, **not code dumps**. Reloading the full context by each executor is the main token multiplier; the subagent's context pack is only its subsystem, the "where decisions live" checklist, and the slugs+aliases of that subsystem's existing nodes — so the known isn't rediscovered (dedup at the source is cheaper than dedup at assembly, and it heals "subagents blind to one another" at least within a subsystem).

## 2. Assembling the nodes

- From the reports, assemble the nodes: one node per decision per `templates/NODE.md`, a `file:line` proof is mandatory. A subagent returned a "decision" without a proof → discard it, don't reread the whole code.
- **Dedup across subsystems:** a shared invariant — one node and many edges, not copies. This is Full's key work: subagents are blind to one another and will return overlaps.
- Edges — cross-module typed `[[wikilinks]]`.

## 3. Overview and map

- `docs/graph/_overview.md` per `templates/_overview.md`: a Mermaid of the whole graph + a list of nodes + a rebuilt Digest (hubs / tensions / questions — derived from the nodes, form in the template). >~40 nodes → group into `subgraph`s by subsystem, otherwise the overview is unreadable.
- **CRAFT.md.** No file → create a skeleton per `skills/task/templates/CRAFT.md` (the template is the canon of its composition — don't restate it here) out of the built subsystem map, and add the pointer line "read CRAFT.md first" to CLAUDE.md so the map isn't an orphan. Leave ownership to `task` — it maintains the map onward. It exists → fill in the missing pointers, don't drag rationale into the map.

## 4. Checkpoints

After each subsystem: nodes to disk (external memory), **commit them** (`graph: <subsystem>`) — a checkpoint is a commit, so the memory survives a crash or a branch switch, not just a compact, and a 30+-node onboarding gets reviewable granularity. Then end the turn — the context reset is the user's action (as in task-L): close with "Subsystem X — N nodes committed. Run /compact and say 'continue'". The next subsystem starts from `_overview.md` and its own report, not the chat history.

**Git fate.** An autonomous craft-graph pass writes a document → the default branch, or `graph/<scope>` + PR when the default is protected; a mass onboarding (30+ nodes) is worth a reviewer's eyes, so a branch + PR fits even on an unprotected main. Nodes created inside a task wrap ride that task's branch (its PR shows them) — that path is task's, not this one.

## Stop rules

- **A proof is mandatory** for subagent findings too: without it there's no node.
- **The overview has bloated** (>~40 nodes flat) → introduce `subgraph`s by subsystem, don't drag along an unreadable Mermaid.
- **Duplicate nodes** of one invariant → merge into one, keep the edges.
