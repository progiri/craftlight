# Regression scenarios for the plan skill

Run after ANY change to `SKILL.md` / `templates/*`: parallel read-only subagents (sonnet-level),
each given its prompt without the "Expected"; the agent decides and **quotes the rule** that
determined it — otherwise the wording isn't discoverable. A divergence = the change broke the
discipline: fix the skill's wording, not the scenario.

Last run: 2026-08-25 RELEASE SWEEP for 0.14.0 (craft wave-release / leaf t7 of PLAN wave-orchestrator) — all seven corpora run as ONE pass: 193 scenarios, 207 runs (multi-part scenarios counted per part), 204 PASS / 3 partial, 0 wrong verdicts. Method: every scenario was rendered into its own fixture file with the "Expected" span mechanically stripped and the absence asserted, so no runner prompt could see it — one read-only sonnet subagent per fixture, scored against "Expected" by hand. Per corpus: task 58/60, debug 31/31, plan 30/30, brief 24/24, wave 22/22, craft-graph 20/20, code-review 19/20. The three partials are answer-completeness misses (a correct verdict with an Expected sub-claim not produced), recorded as found — no scenario was re-worded and no skill was edited to turn one green. Cross-skill seams checked in the same pass: the plan-to-wave hand-off (plan sc.4) and the block self-heal. Honest scope note on that second seam — it is NOT covered in all seven skills: task 11-14 are the only scenarios that quote `v11` itself; craft-graph 7, debug 10, code-review 8 and plan 21 cover the shared invariant (the upsert rides with the skill's first write to disk; a call that writes nothing must not touch CLAUDE.md); brief and wave have no block scenario at all. This corpus: 28 scenarios / 30 runs (7 and 8 two-part) — 30/30 PASS. Includes the plan-to-wave hand-off seam (sc.4): plan still refuses to run the wave, names `wave` one level down as orchestration's home, and stops. sc.21 carries this corpus's share of the block seam (no write -> no CLAUDE.md edit). Description unchanged this release (980 chars). Earlier 2026-08-25 (M1 revision for wave runs, craft plan-boundary) — the PR-granularity wording revised, not bypassed: the description's observable boundary is now "the work splitting into several independent tasks, each classified and branched on its own" (was "landing as several independent PRs"), and the leaf rule is "one future `task` call, on its own branch" (deliberately not "one spec" — an S leaf leaves no SPEC.md) with PR granularity depending on the run (solo → own PR; inside a wave → the wave lands as one PR, the leaf keeps its branch). The planner-only rule keeps "zero code edits, zero orchestration" and now names where orchestration lives — the `wave` skill one level down, started by the user; step 3 gained the wave branch `wave/<initiative>-w<N>` plus the file-disjoint ≠ semantically-independent caveat, step 4's hand-off offers both routes, the living-document rule names `wave` as the PLAN's other writer. PLAN template: a `Files/area` hint column, a per-wave `Wave branch` field, a "Wave runs" section (per-run block: merge order, per-leaf status, what stopped) exempt from the cap as append-only. Scenario 4 rewritten (it expected "plan doesn't orchestrate, full stop"); new 26–28 (leaf branch vs wave PR, the Files/area hint and what disjointness doesn't buy, "Wave runs" laid out not filled). Ran 2, 4, 9, 19, 25, 26, 27, 28 — 8/8 PASS, the rules quoted verbatim; self-review then caught the "one spec" claim (false for an S leaf) and reworded it, so 2 and 26 were re-run against the corrected text — 2/2 PASS. Earlier 2026-07-24 (L/PLAN caps, craft l-spec-caps) — the PLAN cap raised 180→250 and a cut-priority added to the template's file-form (cut prose first — Context, Discussion-decisions wording; NEVER the task table, the DAG, or the Contracts between tasks); new scenario 25 (cap + cut-priority). Ran sc.25 — 1/1 PASS, the rule quoted verbatim. Earlier 2026-07-23 FINAL CORPUS SWEEP (review №12 close-out) — all 25 runs (24 scenarios, 8 two-part) against the finished corpus — 25/25 PASS. Earlier 2026-07-23 (PLAN template + state machine, review №11) — the family status enum unified: PLAN gains `draft` (gate not passed, DAG empty) and `abandoned` (drop on explicit request, stops the FYI resurfacing); `in-progress` now means gate-passed only; Step 0 + draft-save wording resynced; cap ≤180 stays the template's single home. Ran draft-resume, draft-save, abandoned — 3/3 PASS. Earlier 2026-07-23 (brief integration, review №6) — recon now greps prior BRIEF verdicts alongside the graph, the parent-artifact hook reads a BRIEF the initiative arrived from (step 1), and the planner-doesn't-execute rule carries the fan-out rationale for why plan doesn't auto-call task (brief's single-successor call is the named contrast). Ran new 23–24 — 2/2 PASS. Earlier 2026-07-23 (plan rework, review №5) — the leaf hook closes the hand-off loop (task/m.md brief now carries the leaf's contracts/rejections from the PLAN into Constraints, its wrap ticks the leaf's checkbox; hand-off names the plan in each launch line), the PLAN's git fate defined (commit to default, protected → `plan/<initiative>` + PR, every PLAN write is a commit), the risk-list canon anchored to the CLAUDE-block line (plan cites it; the router and L's distillate carry it too), Step 0 reworked (block upsert rides with the first disk write; new initiative → FYI instead of a blocking resume; several plans → ask; reconciliation scoped to the first unclosed wave + in-progress specs), the discussion got convergence-per-turn (text sketches mandatory, the gate protects the file) and a mid-discussion compact tripwire, gate turn mechanics + fragment enthusiasm ≠ approval, sub-initiative successor as an Outcome line, description: bare "decompose" dropped, the "several independent PRs" boundary added. Ran 2, 3, 5, 7, 8 (2 parts), 9–13 + new 14–22 — 20/20 PASS, rules quoted verbatim. Earlier 2026-07-21 — plan gate wording tightened (Step 1 gate: "impatience is not that approval"), closing the scenario-3 divergence: scenario 3 re-run red→green (the agent now holds the gate under "just give me the tree now", converges faster, and waits for the explicit ok — cites the new rule verbatim), scenario 11 unaffected (still offers the pre-gate draft) → plan now 13/13. Earlier 2026-07-21 — full English translation of the plugin (SKILL.md + templates/* + this file): 12/13 PASS. Scenarios 1, 2, 4–13 preserved, each governing rule quoted verbatim (task boundary, epic trigger, planner-only, flat leaf specs, decisions-in-PLAN, no-nested-plan, resume triggers/waves, size-is-a-hint, recon-from-graph, pre-gate draft, close-plan, pre-DAG resume). Scenario 3 DIVERGED: two independent sonnet reads both BUILD the DAG on the user's impatient "just give me the tree right now", treating it as the "(or equivalent)" gate signal, vs Expected "hold the gate, keep discussing until an explicit 'ok, build'". NOT a translation regression — the gate wording is a faithful, unchanged rendering of the RU original (the "(or equivalent)" qualifier is present identically in RU); this is a latent ambiguity surfaced by current model behavior. Tightening the gate wording (so impatience ≠ approval) deferred to a separate task. Earlier 2026-07-20 — lifecycle plan (leaf t3 of the batch): new scenarios 11–13 (draft on wrap-up, closing PLAN→done, resuming a pre-DAG draft) + 8p2 touched by the resume — 4/4 PASS, the rules are quoted verbatim. Earlier 2026-07-17 — compression of the description tail (0.6.3): scenarios 2, 8p1 — 2/2 PASS. Earlier 2026-07-17 — recall (recon starts with the graph, scenario 10): ran 10 and 3 (the gate) touched by the Step 1 change — 2/2 PASS, the new rule is quoted verbatim. Earlier 2026-07-16 — 9/9 PASS (first run of the new skill); after rewording Step 2 — a follow-up run of 3 and 7 PASS.

## 1. Boundary: a large single task is task, not plan
Given: only `SKILL.md`. Task: "refactor the `billing/` module — rename the entities, split them
across layers, ~15 files, but one coherent result, one PR".
Expected: this is NOT plan — a single task, even a large, multi-file one, goes to `task` (its L mode
slices it into phases within a single branch); quote "Not for this skill: a single task, even a large, multi-file one → `task`".

## 2. Boundary: an epic of several tasks is plan
Given: only the description text. Request: "we need to rewrite billing entirely — new DB schema, new API,
frontend, data migration, notifications; where to start".
Expected: the plan skill fires — the scope is not one task but an initiative of many separate tasks/branches;
triggers "rewrite … where to start", "an epic of many tasks".

## 3. Gate: the tree isn't built until an explicit "ok, build"
Given: `SKILL.md`. A discussion of the initiative is under way; the user pushes: "don't drag it out, just give me the task tree
and waves right now".
Expected: first the discussion of the nuances, the tree — only after an explicit "ok, build"; we write no files before the
gate; quote "The tree is NOT built until the user explicitly says "ok, build"".

## 4. Planner-only: we don't execute — but we name the route
Given: `SKILL.md`. The plan is ready, the waves are laid out. The user: "great, now do the first wave".
Expected: plan still doesn't execute and doesn't orchestrate — the ban is unchanged; running a whole wave is the
`wave` skill one level down and **the user** starts it (leaf by leaf it's a separate `task` call), plan stops and
calls neither on the user's behalf; quote "Zero code edits, zero orchestration — the ban is unchanged; what
changed is that orchestration now has a home one level down: running a whole wave is the `wave` skill".

## 5. Flat leaf specs
Given: `SKILL.md` + `templates/PLAN.md`. Initiative `payments-rewrite`, leaf `db-schema`. The temptation to
put the leaf's spec in a nested folder `docs/crafts/payments-rewrite/db-schema/SPEC.md`.
Expected: the leaf's spec is a flat neighbor `docs/crafts/db-schema/SPEC.md`, not nested; quote "the task router
looks for active tasks with the glob `docs/crafts/*/SPEC.md`, and a single `*` doesn't catch nesting".

## 6. Discussion decisions — in the PLAN, not the graph
Given: `SKILL.md`. A long-lived architectural decision surfaced in the discussion (e.g. "we go with event
sourcing, not CRUD, because …"). The temptation to create a node in `docs/graph/` right away.
Expected: the decision settles into the "Discussion decisions" section of the PLAN, we don't create a graph node — there's
no `file:line` proof; `task` will create the node at the leaf's wrap; quote "Decisions go in the PLAN, not the graph".

## 7. We don't nest a plan inside a plan
Given: `SKILL.md`. The initiative broke into ~25 leaves and 8 waves suggest themselves; one of the leaves is itself
huge and fuzzy.
Expected: we don't nest a plan inside a plan — a ballooned DAG means "the initiative is too large": propose
a coarser first cut / split it into sub-initiatives; a huge fuzzy leaf → a rough task that `task`-L will slice into phases;
quote "don't nest a plan inside a plan" / "The DAG has ballooned … propose a coarser first cut".

## 8. Resume by the PLAN
Part 1 (given: only the description text): a new session with no history, the user writes "continue the plan".
Expected: the plan skill fires — "continue the plan" is in the triggers.
Part 2 (given: `SKILL.md`): there's a `docs/crafts/<initiative>/PLAN.md` with status `in-progress` and
unclosed tasks; the message is a bare resume trigger, no new initiative.
Expected: show the current wave (the first one with unclosed tasks), offer to continue; resuming individual tasks
by `SPEC.md` is the concern of `task`; quote "show the current wave (the first one with unclosed tasks)".

## 9. A leaf's size is a hint, classification is task's job
Given: `SKILL.md` + `templates/PLAN.md`. The planner tagged the leaf "fix the token check" as size
S, though it's in the risk zone (auth).
Expected: plan sets the risk flag, but the real classification and the "risk zone → minimum M" guard are held by
`task` at the leaf's start — size S stays a hint, plan doesn't impose it; quote "A leaf's size is
a hint … `task` holds the … "risk zone → minimum M" guard".

## 10. The landscape starts with the graph
Given: `SKILL.md`. Starting to plan an initiative for a module that has nodes in `docs/graph/` (a decision
and a gotcha with proofs).
Expected: recon starts with the graph (overview + grep for slugs); the recorded decisions and gotchas feed into
the discussion of the nuances, a fork against a node is named explicitly; quote "first the decision graph on the topic".

## 11. Wrapping up the discussion before the gate → a draft
Given: `SKILL.md`. A multi-turn discussion of the initiative's decomposition is under way; "ok, build" hasn't been said yet.
The user: "listen, let's continue tomorrow".
Expected: the discussion isn't lost and the tree isn't built — offer to save a `draft` (status `draft`:
the filled-in template + the pulse in the "Log", the DAG empty); the file is written only on agreement, otherwise nothing; quote
"Wrapping up before the gate … offer to save a `draft`".

## 12. All leaves done → closing the plan
Given: `SKILL.md`. A new session; `docs/crafts/big-init/PLAN.md` with status `in-progress`, but all its
child specs are already `done` (no unclosed waves).
Expected: the plan doesn't stay "active" forever — step 0 recognizes completion and offers to close it
(status `done`, fill in "Outcome"); quote "all leaves done — no unclosed waves → the initiative
is complete: offer to close the plan".

## 13. Resuming a draft → continue the discussion
Given: `SKILL.md`. A new session; `docs/crafts/init-x/PLAN.md` with status `draft` (the plan was saved at the
discussion stage, before the gate; the DAG is empty).
Expected: resume doesn't show a nonexistent "current wave" — a `draft` means the gate is still ahead, so it
continues the discussion from the last pulse in the "Log"; quote "`draft` → continue the discussion from the
last pulse in the "Log" (the gate is still ahead)".

## 14. A new initiative isn't blocked by a parked plan
Given: `SKILL.md`. `docs/crafts/big-init/PLAN.md` is in-progress with unclosed waves; the user describes a
brand-new initiative to decompose.
Expected: no blocking "continue the old plan?" question — the new initiative is planned as usual, the parked
plan gets one FYI line; quote "The message brings a new initiative → plan it as usual; no blocking question —
one FYI line".

## 15. The PLAN is committed, not floating
Given: `SKILL.md`. Step 4: PLAN.md is written for initiative `payments-rewrite`; the repo's default branch is
unprotected.
Expected: the PLAN is committed to the default branch with a one-line announce (`plan: payments-rewrite`);
protected default → branch `plan/<initiative>` + PR; later PLAN writes (replans, checkbox ticks) are commits
too; quote "the plan lives across many task branches, so it belongs to the default branch" (or "a PLAN edit is
a commit, not a floating change").

## 16. Mid-discussion compact → offer the draft
Given: `SKILL.md`. A long decomposition discussion, no file saved yet; a context compaction just happened.
Expected: offer to save the `draft` right away — an auto-compact silently eats nuances and rejected
options while no file exists; quote "a compact happened mid-discussion → offer to save the `draft`
right away".

## 17. Every discussion turn ends with the cut
Given: `SKILL.md`. Mid-discussion, second turn; nothing contentious is left to ask this turn.
Expected: the turn still ends with the current cut — a text sketch of the leaves — plus the open forks;
sketches are the mandatory medium, the gate protects the file, not the sketch; quote "a discussion turn ends
with the current cut — a text sketch of the leaves — plus the open forks".

## 18. Fragment enthusiasm is not the gate
Given: `SKILL.md`. You showed the current cut; the user replies "love the migration part, good idea" — and
nothing else.
Expected: the tree is not built — enthusiasm about a fragment approves the fragment, not the decomposition;
the ok must address the whole cut; quote "Enthusiasm about a fragment ("love that part", "good idea") approves
the fragment, not the decomposition".

## 19. Hand-off names the plan
Given: `SKILL.md`. The waves are laid out for `payments-rewrite`; wave 1 holds `db-schema` and `api-skeleton`.
Expected: the hand-off names the plan in each launch line — `run task on db-schema (PLAN: payments-rewrite)` —
so the leaf's brief finds its contracts; and plan stops; quote "naming the plan in each launch line … so the
leaf's brief finds its contracts".

## 20. Reconciliation is scoped to the active wave
Given: `SKILL.md`. Resume of a 12-leaf plan: waves 1–2 were closed at earlier resumes, wave 3 has unclosed
leaves.
Expected: reconciliation reads only wave 3's leaves plus any specs marked in-progress — not all 12; quote
"only the first unclosed wave's leaves plus any specs marked `in-progress`".

## 21. No write — no CLAUDE.md edit
Given: `SKILL.md`. A plan discussion ran two turns and the user dropped it; nothing was saved, no draft
accepted.
Expected: CLAUDE.md was never touched — the block upsert rides with plan's first write to disk, and this call
never wrote; quote "rides with plan's first write to disk … a call that never writes must not edit the user's
CLAUDE.md".

## 22. A real split leaves a successor line
Given: `SKILL.md`. The DAG balloons to ~20 leaves; a coarser cut genuinely doesn't work, and the user agrees
to split into two initiatives.
Expected: the successor is recorded as one line in the current plan's "Outcome" (`next: <initiative-2>`) — no
nested plan, no sibling-plan machinery; quote "the successor is one line in the current plan's "Outcome"".

## 23. Recon greps prior brief verdicts
Given: `SKILL.md`. Beginning to plan an initiative; `docs/crafts/` holds a `BRIEF.md` with a `deferred` verdict
touching the same area.
Expected: recon greps the verdict lines of `docs/crafts/*/BRIEF.md` alongside the graph — the prior decision
feeds the discussion instead of being rediscovered; quote "plus the verdict lines of `docs/crafts/*/BRIEF.md`".

## 24. The initiative arrived from a brief
Given: `SKILL.md`. The planning request is "break down docs/crafts/billing-rewrite/BRIEF.md (verdict go)".
Expected: the BRIEF is read first — its decision, constraints, and rejected options are the discussion's starting
point, not relitigated; quote "read it first: its decision, constraints, and rejected options are the discussion's
starting point, not something to relitigate (the parent-artifact hook…)".

## 25. PLAN cap and the cut-priority
Given: `templates/PLAN.md`. A PLAN's planning part has grown near the cap; the bulkiest sections are the task
table and "Contracts between tasks". The temptation to compress the contracts and drop table columns "to fit".
Expected: the cap is 250 lines (Log, Wave runs and Outcome don't count) and the cut goes at prose first (Context,
Discussion-decisions wording), NEVER the task table, the DAG, or the Contracts between tasks; quote the PLAN
file-form "cut prose first … NEVER the task table, the DAG, or the Contracts between tasks".

## 26. A leaf keeps its branch; PR granularity depends on the run
Given: `SKILL.md`. Leaves `db-schema` and `api-skeleton` sit in one wave, and the user intends to run that wave
as a wave — one PR for the whole wave. The temptation: "one PR = one task", so the two leaves should be merged
into a single leaf.
Expected: no — a leaf is one future `task` call on its own branch; PR granularity is not the leaf's property —
run inside a wave, the wave lands as one PR while each leaf still keeps its own branch and stays separately
revertible; quote "A leaf = exactly one future `task` call, **on its own branch** … PR granularity is not the
leaf's property".

## 27. The Files/area hint, and what disjointness does not buy
Given: `SKILL.md` + `templates/PLAN.md`. Wave 2 holds three leaves; their `Files/area` cells don't overlap, and
the planner is about to declare the wave safe to run in parallel on that basis alone.
Expected: the hint is filled per leaf (the folders it is expected to touch) and it is exactly what lets a wave be
sanity-checked before the run — but it's a hint, not a fence: file-disjoint is not the same as semantically
independent (a leaf can write a reference into another's file, or shift the line an anchor elsewhere points at);
quote "file-disjoint is not the same as semantically independent".

## 28. "Wave runs" is laid out, not filled
Given: `SKILL.md` + `templates/PLAN.md`. Writing the PLAN at step 4; no wave has been run yet. The temptation to
pre-fill "Wave runs" with the planned merge order — or to drop the section as empty ceremony.
Expected: plan lays the section out empty (and the per-wave `Wave branch` field with it); filling it — merge
order, per-leaf status, what stopped — is the `wave` run's job, plan plans and doesn't run waves; quote "Laid
out EMPTY by plan and filled by the `wave` skill as a wave is run — plan plans, it doesn't run waves".
