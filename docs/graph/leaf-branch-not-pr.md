# leaf-branch-not-pr: a leaf is anchored on its branch, not on a PR

Status: active
Type: decision
Area: plan
Source: plan-boundary
Proof: `plugins/craftlight/skills/plan/SKILL.md:76-78` <!-- the description's boundary — same file :3 -->

## Gist
plan's leaf rule and its observable boundary with `task` are stated in **branches**, not PRs: a leaf = one
future `task` call on its own branch. A wave run lands the whole wave as one PR while each leaf keeps its
branch, so PR count no longer discriminates plan from task.

## Why
The `wave` skill merges a wave's leaves into a wave branch and opens one PR for it — the old wording ("a leaf =
one branch, one PR"; boundary = "the work landing as several independent PRs") became false the moment waves
became runnable, and the PLAN required the revision be explicit, not silently bypassed. Rejected: "one spec"
as the anchor — an S leaf leaves no `SPEC.md`; the branch is the one artifact every leaf has.

## Risks
Reasoning "one PR = one task" merges leaves that should stay separate → per-leaf classification and
revertibility are lost. Reading the revision as a licence to orchestrate → plan's zero-orchestration ban still
holds; the wave run is `wave`'s, started by the user.

## Edges
- part-of [[plan-above-task]]
- depends-on [[spec-travels-with-branch]]
