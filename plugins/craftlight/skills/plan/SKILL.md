---
name: plan
description: Planning and decomposing a large initiative that breaks into several separate tasks — discuss the nuances, build a tree (DAG) of tasks with dependencies, and lay it out into waves of parallel execution. Use this skill when the scope is not "one task" but an epic of many tasks — the observable boundary is the work landing as several independent PRs — "plan this out", "break the big task down", "decompose the epic", "draft a work plan", "roadmap", "where to start in this big feature", "this is too big for one task", "split it into stages", "plan the refactor of the whole module", "break this epic down" — even without the words "plan" or "skill". Also trigger on a request to continue planning — "continue the plan", "back to the plan", "where are we in the plan". Not for a single task, even a large one (that's `task`, modes S/M/L), not for a review (`code-review`), and not for recording decisions as a graph (`craft-graph`).
---

# plan — decomposing an initiative into waves of tasks

Principle: **plan sits ABOVE `task`.** It takes an initiative whose scope is not one task but several, talks it
through, builds a DAG of separate tasks, and lays them out into waves of parallel execution. Each DAG leaf is a
future `task` call (which classifies the leaf as S/M/L and writes the code itself). Ceremony is proportional: you
take on plan only when the initiative objectively breaks into many tasks. **The planner doesn't write code and
doesn't drive execution — it plans and stops.**

Not for this skill: a single task, even a large, multi-file one → `task` (its L mode slices it into phases within
a single branch); review without edits → `code-review`; recording decisions/gotchas as a graph → `craft-graph`.
Realized along the way that you're facing one task, not a batch → leave and hand off to `task`.

## Step 0. Orientation and resume

There's a `CRAFT.md` → read it first: the project map, the starting point. The craftlight block upsert in the
root `CLAUDE.md` (reference and procedure — `skills/task/templates/CLAUDE-block.md`) rides with plan's first
write to disk — the saved pre-gate draft or step 4, whichever comes first — never earlier: until then plan
writes no files at all, and a call that never writes must not edit the user's CLAUDE.md.

A `docs/crafts/*/PLAN.md` with status `draft` (gate not passed, DAG empty) or `in-progress` (gate passed, waves running) exists:

- The message brings a new initiative → plan it as usual; no blocking question — one FYI line in the reply:
  `parked: plan "<initiative>" (<status>) — say "continue the plan" to get back to it`.
- A bare resume trigger ("continue the plan", "where are we in the plan") → resume by the plan's status.
  Several parked plans → ask which one.
- `draft` → continue the discussion from the last pulse in the "Log" (the gate is still ahead). `in-progress`
  with unclosed waves → reconcile cheaply — only the first unclosed wave's leaves plus any specs marked
  `in-progress`: earlier waves are already reconciled, later ones must not have started — check off the completed
  leaves and show the current wave (the first one with unclosed tasks). **All leaves done — no unclosed waves** →
  the initiative is complete: offer to close the plan (status `done`, fill in "Outcome").
- The plan is external memory: resuming reads the PLAN, not the chat history. Refusal → leave the plan in place;
  drop it only on an explicit request (status `abandoned` — resume won't surface it again). Resuming individual
  tasks (by `SPEC.md`) is the concern of `task`, not plan: plan operates on waves, task on its own specs.

## Step 1. Discussion — multi-turn, until an explicit "ok, build"

Here plan deliberately departs from task's "single round-trip": the cost of misdecomposing a huge initiative is
high, so we discuss iteratively.

- Recon is cheap: first the decision graph on the topic (`docs/graph/_overview.md` + grep for slugs) plus the
  verdict lines of `docs/crafts/*/BRIEF.md` — the landscape's decisions and gotchas (including a past no-go on
  this direction) may already be recorded; then targeted Grep/Glob, reading fragments, a broad search to an
  Explore subagent. The goal is to understand the initiative's landscape, not to read it end to end. A fork is
  resolved against an existing node → say so explicitly ("contradicts [[slug]], because …").
- The initiative arrived from a brief (the statement points at a `docs/crafts/<slug>/BRIEF.md`) → read it first:
  its decision, constraints, and rejected options are the discussion's starting point, not something to relitigate
  (the parent-artifact hook, mirrored in task's brief).
- Talk through the nuances: scope boundaries, risks, unknowns, decision forks, and rejected options. The
  contentious — ask the user; the reasonable — lock as an assumption.
- **Convergence is the norm of every turn:** a discussion turn ends with the current cut — a text sketch of the
  leaves — plus the open forks. Text sketches are the discussion's mandatory medium; the gate protects the
  *file*, not the sketch: sketchless abstract discussion is how planning never converges.
- **Tripwire:** a compact happened mid-discussion → offer to save the `draft` right away: an
  auto-compact silently eats nuances and rejected options while no file exists yet.
- **Gate.** The tree is NOT built until the user explicitly approves the decomposition under discussion
  ("ok, build" or an equivalent that addresses the whole cut). Mechanically: showing the final cut ends the
  turn — the ok arrives as the user's next message, it is never inferred. Enthusiasm about a fragment ("love
  that part", "good idea") approves the fragment, not the decomposition. Impatience is not approval either: a
  push for speed ("don't drag it out", "just give me the tree and waves now") means converge the discussion
  faster — show your proposed cut and the open questions, then get the explicit ok — not skip the gate. While
  the discussion is ongoing — text only, we write no files. The discussion's outcomes (including what was
  rejected) settle into the PLAN.
- **Wrapping up before the gate.** The user wraps up an unfinished discussion ("let's continue tomorrow",
  "that's enough for now") → offer to save a `draft` (status `draft`): the template filled in (Context, Discussion
  decisions) + the course of the discussion and the current pulse in the "Log", the DAG still empty. Agreement
  is the only case of writing a file before the gate (the block upsert rides with it — step 0); refusal → we
  write nothing. Resuming such a plan is picked up by step 0 (no DAG → continue the discussion).

## Step 2. The task DAG

After the gate, break the initiative into **leaf tasks**. A leaf = exactly one future `task` (one branch, one
PR). For each leaf: `id`, a one-line goal in system terms, a size estimate S/M/L (**a hint** for planning the
waves — `task` does the real classification at start), a list of dependencies, a risk-zone flag (the canonical
list is the risk-zone line of the craftlight block in the root `CLAUDE.md` — always in context).

- Strictly it's a **DAG** (a task can have several prerequisites and several successors), and the "tree" above
  is a working word for the same structure; the edges are `depends-on`.
- A leaf is itself huge and fuzzy → it's a rough task that `task`-L will slice into phases; **don't nest a plan
  inside a plan**. The DAG has ballooned (>~15 tasks or >5 waves suggest themselves) → the initiative is too
  large: propose a coarser first cut; really splitting into sub-initiatives → the successor is one line in the
  current plan's "Outcome" (`next: <initiative-2>`) — no sibling-plan web, no new machinery.

## Step 3. Waves

A wave is a topological layer of the DAG: everything in wave N depends only on waves < N, so **within a wave the
tasks are independent → they parallelize**. Record the **contracts between tasks** (signatures, data formats,
invariants) explicitly: they are exactly what lets you start the next wave without re-reading everything — an
analog of the contracts between phases in task-L, but across separate tasks.

## Step 4. Artifact and hand-off

- Record the plan in `docs/crafts/<initiative>/PLAN.md` per `templates/PLAN.md` (status `in-progress`).
- **The PLAN's git fate:** the plan lives across many task branches, so it belongs to the default branch —
  commit it there with a one-line announce (`plan: <initiative>`); the default branch is protected → branch
  `plan/<initiative>` + a PR. The same goes for the pre-gate draft and for every later PLAN write (replans,
  checkbox ticks at resume): a PLAN edit is a commit, not a floating change. The router's "a task's commits
  don't go to the default branch" is about code; the PLAN is a document.
- The leaves' child specs are **flat neighbors** `docs/crafts/<leaf>/SPEC.md`, NOT nested: the task router
  looks for active tasks with the glob `docs/crafts/*/SPEC.md`, and a single `*` doesn't catch nesting. The PLAN
  links leaves by slug; a link to a not-yet-created spec is normal (`task` creates it at the leaf's start).
- Hand-off: name wave 1 and its independent tasks, naming the plan in each launch line — `run task on <leaf>
  (PLAN: <initiative>)` — so the leaf's brief finds its contracts. And **stop**: plan doesn't spawn executors
  and doesn't call task on the user's behalf.

## Rules

- **The planner plans, doesn't execute.** Zero code edits, zero orchestration. Tempted to "start the first
  task" → that's a separate `task` call, not plan. plan doesn't call task on the user's behalf because a plan
  hand-off is a fan-out across N independent tasks — auto-invoking would be orchestration; brief's single call
  is the deliberate contrast (one successor, chosen by an explicit answer).
- **Decisions go in the PLAN, not the graph.** A discussion has no `file:line` proof; `task` will create the
  graph node at the leaf's wrap, once the decision shows up in code. plan doesn't touch the graph.
- **A leaf's size is a hint.** `task` holds the real S/M/L classification and the "risk zone → minimum M"
  guard; plan only tags them to lay out the waves.
- **The PLAN is a living document.** Reality diverged from the plan → replan the waves, update the PLAN,
  announce it in one line. Silent drift is worse than an honest edit. CRAFT.md/the graph stay with `task`.
