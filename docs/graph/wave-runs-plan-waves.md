# wave-runs-plan-waves: wave — the execution layer for a plan's wave (parallel leaves, one batched gate)

Status: active
Type: decision
Area: wave
Source: wave-skill
Proof: `plugins/craftlight/skills/wave/SKILL.md:8` <!-- the two revisions it makes outright — same file :19-24 -->

## Gist
The `wave` skill runs **one** wave of a PLAN: a fan-out of spec drafters, ONE human gate over the whole wave,
a fan-out of executors in their own worktrees, sequential merges by throwaway agents, and one PR per wave.
It is the executor `plan` refuses to be — plan stays planner-only, and wave never re-cuts the DAG.

## Why
A wave's leaves are independent by construction, so they parallelize; nobody ran them, and the wall-clock win
on a wide wave (the wave costs its slowest leaf, not the sum) is real. It is bought with tokens: every executor
reloads the project's context, ~×N — measured at ~23–26 subagent tokens per token of orchestrator growth
(`plugins/craftlight/skills/wave/SKILL.md:15`), which is why the skill refuses waves under 3 leaves.
Two revisions are made **outright** rather than slipped past: M's ban on execution subagents (here the fan-out
is the point), and a leaf **not** entering `task`'s router — `task`'s gate waits for the *user's* next message
and a subagent has none, so a leaf executes an already-approved spec and the classification `task` owns moves
to the wave's gate (`plugins/craftlight/skills/wave/SKILL.md:104-109`). PR granularity is not among them:
[[leaf-branch-not-pr]] already puts it on the run rather than the leaf.
Rejected: a mode inside `plan` (mixes planning with execution); extending task-L's delegation (a leaf is its own
branch, task is one branch); a launcher without integration (assembly should be automatic).

## Risks
The gate is the single control point over N unattended agents: batched must never mean waived — risk-zone specs
are labelled and approved by name, no advance ok, and showing the specs ends the turn. Verification stays with
the orchestrator (`plugins/craftlight/skills/wave/SKILL.md:195-204`): a PLAN checkbox ticked on an agent's claim is
the failure this design exists against. Two silent killers the leaves cannot see: file-disjoint leaves that
collide semantically, and a leaf's edit shifting `file:line` pointers elsewhere in the repo.

## Edges
- depends-on [[plan-above-task]] <!-- wave exists because plan refuses to execute; it revises that node's "each leaf goes through task" clause, not its core -->
- depends-on [[leaf-branch-not-pr]] <!-- a leaf keeps its branch; PR granularity belongs to the run -->
- depends-on [[confirm-gate]]
- depends-on [[risk-zone-min-m]]
- depends-on [[context-pack-not-history]]
- affects [[done-is-observed]]
