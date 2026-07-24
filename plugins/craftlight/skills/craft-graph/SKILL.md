---
name: craft-graph
description: Documents "why it's this way" and "where the gotchas are" as a navigable graph — flat markdown nodes with `[[wikilinks]]` plus an overview Mermaid (visible on GitHub). Each node is one decision/invariant/gotcha with a `file:line` proof. Use this skill whenever the user asks to record architectural decisions, rationale, or gotchas as a graph — "build a decision graph", "document the architecture as a graph", "a graph of gotchas/traps", "the project's decision map", "capture why it was done this way", "decision graph", "map the architecture decisions", "document the gotchas" — even without the words "graph" or "skill". Also trigger on onboarding a project into the discipline — "adopt craftlight", "seed the graph over the legacy", "onboard this project into craftlight". Not for "how does this work / business-logic onboarding" (that's codebase-reverse-engineering), not for "how to build and run" (that's CLAUDE.md), not for a review (code-review), not for working out a new decision (that's `brief` — the graph records decisions already living in the code, and the proof requirement is that boundary), and not for changing code (task).
---

# craft-graph — the graph of decisions and gotchas

Three principles on top of the shared ones: (1) the graph records what the code doesn't say on its own — "why we decided it this way" and "where the trap is", not a retelling of what's already visible; (2) every node is proven by a `file:line` proof — without proof it's guesswork, there's no node; (3) the graph is dual-view for free: the `docs/graph/*.md` nodes read as ordinary text, the `[[wikilinks]]` give a live graph in Obsidian, and a single `_overview.md` with Mermaid renders right on GitHub. Zero code edits and zero runtime — in the plugin's DNA.

Not for this skill: "how does this work", business-logic onboarding → `codebase-reverse-engineering`; "how to build/run/commands/conventions" → CLAUDE.md; review without edits → `code-review`; working out a decision not yet in the code → `brief`; changing code → `task`. The difference from `code-wiki`: craft-graph is a navigable graph with typed edges, an overview Mermaid, and a **mandatory** proof, not linear notes. Realized the task isn't about recording decisions as a graph → leave the skill.

## Step 0. The object

Determine with cheap recon what we're documenting: the whole codebase / one subsystem / a specific module. Recon is targeted Grep/Glob and reading the fragments where decisions live — the canonical checklist is **error handling, concurrency, caching, transaction boundaries, data invariants, working around non-obvious constraints** (the modes point here); don't read whole files. The object isn't named and isn't obvious → one concrete question to the user.

- `docs/graph/` already exists → an addition or refresh, not an empty start: check against existing nodes, extend them, don't breed duplicates. Nodes marked `verify` in scope are the first candidates of a refresh pass — recheck the proof, update the `file:line` or split the node, clear the mark.
- `docs/crafts/_backlog.md` has `graph-candidate` lines (left by S tasks / debug — a durable lesson with a `file:line` inside) → these are ready-made node candidates; promote the worthy ones. **Consume the breadcrumb:** a promoted line is replaced in the backlog with a pointer `→ [[slug]]`, not left as-is — an unconsumed breadcrumb re-promotes on the next pass and breeds duplicate nodes.
- Resume of an interrupted Full is derivable, not stored: node areas are 1:1 with subsystems, so a subsystem with no node yet is either unvisited or decision-poor — check it and ask, don't restart the whole sweep.

The craftlight block upsert (reference and procedure — `skills/task/templates/CLAUDE-block.md`) rides with the first node written; a recon that finds nothing provable writes no node and so must not edit the user's CLAUDE.md.

## Step 1. Mode

By observable signals of scope:

| Signal | Focused | Full |
|---|---|---|
| Scope | one module/subsystem | the whole base / several subsystems |
| Nodes | a few, local edges | many, cross-module edges |
| Overview `_overview.md` | extends the existing one | builds/rebuilds |
| Recon | targeted, main context | Explore subagents per subsystem |

Reduction: in doubt → Focused (escalation is cheap). Escalation on the fly — when the scope is in fact wider than announced. Announce the mode in one line (`Mode: focused — module auth`) and load the playbook: Focused → `modes/focused.md`, Full → `modes/full.md`. The templates for both are `templates/NODE.md` and `templates/_overview.md`.

## Node format — the same across modes

- **One node = one decision/invariant/gotcha.** The file `docs/graph/<slug>.md` per `templates/NODE.md`. Cap ~40 lines: doesn't fit — it's several linked nodes.
- **Proof `file:line`** — where the decision lives or shows up in the code (a range — `:12-40`). No proof → it's guesswork, we don't create the node.
- **Status (header, grep-visible): `active` / `superseded` / `verify`.** Consumers (the task/brief recon, review prep) read only `active`; the others are history or suspect. This one field is what makes `supersedes` and staleness executable instead of decorative — an edge or a mark no reader can filter on is just decoration.
- **The gist + rationale + what a violation risks** — what the code doesn't express. Restating the code is not a node.
- **Area — a facet of the subsystem.** Mandatory; the overview's subgraphs are the nodes' areas (1:1, the overview is derived from the nodes). A principle applied by ≥2 subsystems → the area `core`, not a host subsystem.
- **Edges — typed `[[wikilinks]]`:** `depends-on`, `affects`, `contradicts`, `supersedes`, `part-of` (the per-type semantics are in `templates/NODE.md`). Back an edge about code with a proof. Create a `supersedes` edge → set the superseded node's status to `superseded` in the same pass: the edge and the status move together.

## Graph rules

- **Overview.** Full builds/rebuilds `docs/graph/_overview.md` (a Mermaid of the whole graph); >~40 nodes → group into `subgraph`s by subsystem (subgraph = the nodes' areas, cross-cutting → `core`). Focused extends the overview if it exists; it doesn't start a new overview for the sake of one module. **Unplaced queue:** a node born outside a craft-graph pass (a task wrap creating one node) appends a line `[[slug]] — area` to an "Unplaced" section instead of editing the Mermaid; any craft-graph pass folds the queue into the graph. Writers stay cheap, "the overview is derived from the nodes" stays true in batch. **Digest:** a small derived layer in the overview (hubs, `contradicts` tensions, questions → `[[slug]]`; form — `templates/_overview.md`): every line is computable from the nodes/edges, no new claims; rebuilt only by a craft-graph pass that edits the overview — outside writers don't touch it.
- **Dedup.** One invariant in two modules — one node and two edges, not two nodes. Before a new node, check the existing ones — slugs and "Aliases:"; a synonym of an existing slug → an alias into its node, not a new node.
- **Staleness has actors.** The proof diverged from the code → `verify`. Setter: a review's conformance lens (it reads nodes intersecting the diff) and a task wrap that touched a file a node's proof points at — either finds the drift and marks it. Clearer: a craft-graph refresh (Step 0). A consumer that pulls a `verify` node into its constraints carries the mark ("constraint in doubt"), never launders it silent-clean.
- **Guard: the graph doesn't edit code.** Zero code edits, including "little things along the way". Found a bug along the way → it's a task for `task`, not for craft-graph: record it as a finding, don't touch the code.
- **Link to CRAFT.md.** Root nodes are linked from the `CRAFT.md` map (owned by `task`). No file on a Full pass → create a `CRAFT.md` skeleton per `templates/CRAFT.md` (don't restate its composition — the template is the canon) and add the pointer line to CLAUDE.md, then leave ownership to `task`.
