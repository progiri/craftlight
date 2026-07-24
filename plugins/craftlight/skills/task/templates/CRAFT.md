<!-- Form only: sections and what each holds. Behavior (when to bootstrap, when to update, ownership) lives in
     task's playbooks and craft-graph — on conflict the playbook wins. These comments are write-time guidance,
     not copied into the artifact. Template edits stay read-compatible. -->
# CRAFT: <project>

<!-- Project hub-map: the starting point after CLAUDE.md. "What it is" is the only prose section; the rest are
     ONLY pointers, not rulebooks — "why it's this way" and gotchas live in the graph (docs/graph/), links go
     here, not rationale. -->

## What it is
<!-- A full description of the project — the single place where "what we're building and why" lives. Cover the
     facets: what the product is; what problem it solves and why (the point); for whom; what it deliberately does
     NOT do (the boundaries); the key approach, if non-obvious. Density: every line adds understanding. 5–15
     lines; much beyond that → that's documentation, its place is the README. -->
<prose: product, the point, for whom, boundaries, approach>

## Entry points
<!-- Where reading the code starts: the main processes/endpoints/CLI commands + `file:line`. -->
- <what> — `path/file:line`

## Module map
<!-- Module → one line of purpose + path. Only what's really needed for navigation.
     Mark a risky module (by the risk-zone line of the craftlight block) with `[risk]` and link the detail into the graph. -->
- <module> — <purpose> (`path/`)
- [risk] <risky module> — <purpose> (`path/`) → [[<node-slug>]]

## Deeper
<!-- Pointers into the decision graph and the glossary: [[<slug>]] — what's there. A pointer, not a retelling. -->
- `CONTEXT.md` — the domain glossary (project terms; read it for the project's vocabulary)
- `docs/graph/_overview.md` — the graph of decisions/gotchas
- [[<slug>]] — <what's captured>

<!-- File form: ≤65 lines including markup; the repo root next to CLAUDE.md; in CLAUDE.md a pointer line
     "read CRAFT.md first". Owner — task. -->
