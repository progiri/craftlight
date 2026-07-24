# CONTEXT: domain glossary

<!-- The project's shared language: "**term** — meaning", one line per term. Selection criterion: the term is
     project-specific or non-obvious; it saves a sentence of explanation; it has settled in the code or artifacts,
     rather than being invented just now. A pointer to code is optional. Replenished as tasks complete; grown too
     large or gone stale → cleanup on the next replenishment. The file is plain markdown, readable by any agent
     and human. -->

- **craft** — a unit of work with an artifact folder `docs/crafts/<slug>/`: the BRIEF, SPEC, PLAN, DEBUG
  of one intent sit side by side.
- **wrap** — a task's closing block: proof by observed result, line-by-line reconciliation against the
  criteria, replenishment of the map/graph/glossary, status done.
- **pulse** — the two-line summary of a brief-discussion round, "Decided: … / Remaining: …".
- **risk zone** — auth, money, migrations, concurrency, data deletion; a task's classification is
  minimum M, and de-escalation does not bypass it.
- **digest** — the derived analytical layer of the graph overview (hubs, tensions, questions →
  `[[slug]]`), computable from the nodes/edges; rebuilt only by craft-graph passes.
- **block** — the managed craftlight block in CLAUDE.md between markers; its version is its own (currently v8),
  not the plugin version.
- **self-heal** — the idempotent upsert of the block that every skill performs in its Step 0.
- **node** — a decision/invariant/gotcha file in `docs/graph/` with a `file:line` proof, linked by
  `[[wikilink]]`s.
- **backlog sink** — `docs/crafts/_backlog.md`: one line per "noticed along the way", with no statuses
  or owners.
- **confirmation gate** — a task executes only after an explicit "ok" on the shown plan/spec.
- **commit gate** — BRIEF.md is written only after an explicit "ok, commit it"; until then the discussion
  is text only.
- **de-escalation** — the only permitted descent M→S: no open questions, ≤2 files, outside the risk
  zone; the spec draft is deleted in the process.
- **orphan draft** — a spec draft on disk without a received ok; it is surfaced with a "resume or delete"
  choice, it does not live silently.
- **run** — a skill's regression check: parallel read-only subagents solve the scenarios and cite the
  rule; a rule that can't be discovered = red.
