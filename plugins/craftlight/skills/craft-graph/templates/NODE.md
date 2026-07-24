<!-- Form only: sections, field enums, formats. Behavior (when to create, promote, mark stale) lives in the
     craft-graph playbooks — on conflict the playbook wins. These comments guide the write and are NOT copied
     into the written node — only the inline enum values (the Status/Type list) stay. Template edits stay read-compatible. -->
# <slug>: <decision/invariant/gotcha in one line>

Status: active <!-- active | superseded | verify (proof drifted). ASCII, grep-visible; consumers read only `active`. -->
Type: decision <!-- decision | invariant | gotcha -->
Area: <subsystem> <!-- a facet of the subsystem; the overview's subgraphs = the nodes' areas (1:1); ≥2 subsystems → core -->
Source: <task-slug | debug-slug | graph-pass> <!-- who created the node — the bidirectional link back to its full history (a spec/DEBUG) -->
Aliases: <slug-synonym> <!-- optional: synonyms comma-separated, dedup searches by them too; none → delete the line -->
Proof: `path/file:line` <!-- where it lives/shows up; a range — :12-40; no proof → no node -->

## Gist
<!-- What was decided / what the invariant is / what the trap is. 1–3 lines. -->

## Why
<!-- Rationale: why exactly this way, which alternative was rejected and by what. What the code doesn't say. 1–3 lines. -->

## Risks
<!-- What breaks when violated. For invariants and gotchas — mandatory. 1–2 lines. -->

## Edges
<!-- Typed edges; an edge about code — with a proof. Per-type semantics:
     depends-on: this node relies on that one holding.
     affects: changing this touches that.
     supersedes: this node replaces that one — set the target's Status to `superseded` (behavior: craft-graph).
     contradicts: a documented, intentional tension between two LIVE decisions; an UNintentional clash is a
                  `verify` situation, not an edge.
     part-of: this node is a facet of that larger one. -->
- depends-on [[<slug>]]
- affects [[<slug>]]

<!-- File form: ≤40 lines including markup; path docs/graph/<slug>.md; one node = one decision;
     ballooned past the cap → split into linked nodes.
     Status enum notes: no `draft` (a node exists only once proven — there is no pre-gate node). -->
