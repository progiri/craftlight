<!-- Form only: sections, field formats, enums. Behavior lives in the playbooks (modes/m.md, l.md) — on any
     conflict the playbook wins. These comments are write-time guidance, NOT copied into the artifact (the inline
     enum on Status is the one exception — it helps a later editor cheaply). Template edits stay read-compatible:
     a reader tolerates an older-form artifact (a spec with no post-ok tags → an empty list, not a failure). -->
# SPEC: <short task title>

Status: draft <!-- draft | in-progress | done | abandoned -->
Mode: M <!-- M | L -->
Branch: <branch>

## Context
<!-- 3–5 lines: what the system is, why the task arose, what already exists. No more. -->

## Goal
<!-- 1–2 lines: the result in system/user terms, not a list of actions. -->

## Assumptions
<!-- Reasonable assumptions instead of questions; the pre-ok ones first. Tag by origin:
     an assumption adopted during execution — `(post-ok)`; one applied in S before an after-the-fact escalation — `(already applied)`. -->
-

## Non-goals
<!-- What we deliberately do NOT do. A mandatory section: an anchor against "while we're at it". -->
-

## Constraints
<!-- Stack, compatibility, prohibitions, agreements. Only what really constrains the solution.
     Sources that land here: `active` graph nodes on the topic, a PLAN leaf's contracts, a parent BRIEF's constraints/rejections. -->
-

## Acceptance criteria
<!-- Verifiable statements: how we'll know it's done. One checkbox each. -->
- [ ]
- [ ]

## Checklist
<!-- An item = one atomic commit, with concrete file paths (a later item may carry `path: TBD after item N`).
     M: a flat list. L: group into "### Phase N: name"; a phase ends with green tests. -->
- [ ] <step> (`src/...`)
- [ ]

<!-- L only: contracts between phases — signatures, data formats, invariants.
## Contracts
-
-->

## Open questions
<!-- Question → answer after clarification. Also here — "while we're at it" ideas that concern the task.
     Anything foreign (outside the task's scope) — a line in docs/crafts/_backlog.md. -->
-

## Log
<!-- A paragraph after a checkpoint/phase: what was done, key decisions, what's next, known gotchas. In M usually empty.
     The hunt moved to a DEBUG.md → a pointer line here: `log: docs/crafts/<slug>/DEBUG.md`. -->

## Outcome
<!-- Filled by wrap: what was done, deviations from the plan, how it was verified; counters: round-trips, escalations, closed items. -->

<!-- File form: cap M ≤80, L ≤200 lines (Log and Outcome don't count — an append-only execution log).
     Hitting the cap in M → cut prose and checklist detail. In L the cut-priority protects what the executor
     runs on: cut prose first (Context, wording), NEVER file paths, the Contracts, or acceptance criteria —
     an L spec is authored once and executed many times by subagents; executor-grade detail is its point.
     Lives in docs/crafts/<slug>/SPEC.md (a folder per task, slug = the task's slug). This template is the single
     home of the cap for the SPEC family; the playbooks reference it, they don't restate the number. -->
