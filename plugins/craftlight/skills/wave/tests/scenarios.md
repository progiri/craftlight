# Regression scenarios for the wave skill

Run after ANY change to `SKILL.md`: parallel read-only subagents (sonnet-level), each given its
prompt without the "Expected"; the agent decides and **quotes the rule** that determined it —
otherwise the wording isn't discoverable. A divergence = the change broke the discipline: fix the
skill's wording, not the scenario.

Last run: 2026-08-25 RELEASE SWEEP for 0.14.0 (craft wave-release / leaf t7 of PLAN wave-orchestrator) — all seven corpora run as ONE pass: 193 scenarios, 207 runs (multi-part scenarios counted per part), 204 PASS / 3 partial, 0 wrong verdicts. Method: every scenario was rendered into its own fixture file with the "Expected" span mechanically stripped and the absence asserted, so no runner prompt could see it — one read-only sonnet subagent per fixture, scored against "Expected" by hand. Per corpus: task 58/60, debug 31/31, plan 30/30, brief 24/24, wave 22/22, craft-graph 20/20, code-review 19/20. The three partials are answer-completeness misses (a correct verdict with an Expected sub-claim not produced), recorded as found — no scenario was re-worded and no skill was edited to turn one green. Cross-skill seams checked in the same pass: the plan-to-wave hand-off (plan sc.4) and the block self-heal. Honest scope note on that second seam — it is NOT covered in all seven skills: task 11-14 are the only scenarios that quote `v11` itself; craft-graph 7, debug 10, code-review 8 and plan 21 cover the shared invariant (the upsert rides with the skill's first write to disk; a call that writes nothing must not touch CLAUDE.md); brief and wave have no block scenario at all. This corpus: all 22 scenarios — 22/22 PASS, every governing rule quoted verbatim, no red. `wave/SKILL.md` is unchanged since t2 landed it, and wave's own description (776 chars) was not touched by this release's description cuts, so the corpus ran against exactly the text it was written for. This corpus has no block/CLAUDE.md scenario — the one seam of the seven-skill sweep it does not carry. Earlier 2026-08-25 (first corpus for the seventh skill, craft wave-scenarios / leaf t4 of PLAN wave-orchestrator) — 22 scenarios written against `wave/SKILL.md` as landed by t2 (263 lines, single-mode, `e123c6e`), covering the boundary vs `task` and the description trigger; the ×N economics floor (under 3 leaves, no wave); the gate (can't be skipped or inferred, no advance ok, showing ends the turn); risk-zone approval by name and the risk verdict being the orchestrator's rather than the PLAN flag's; an L-sized leaf ejecting from the wave; the pack-is-the-prompt rule on both fan-outs (drafter write-path leak, executor spec inline); the executor's risk-zone stop and the orchestrator's no-respawn-no-finish answer to it; leaves opening no PRs; the merge agent aborting on a semantic conflict instead of resolving it; the verification split (orchestrator runs the tests against the merged tree before any checkbox) and its honest-unticked fallback; resume from the PLAN + git rather than chat history; no re-execution of a leaf branch that already has commits; one wave per invocation; wave writes no code; divergence handed back to `plan`; file-disjoint ≠ semantically independent; the drafter's pack carrying the executor's constraints; the line-anchored reference sweep at close. Before the run, every "Expected" quote was grepped against SKILL.md and two were corrected (scenario 12 had quoted across an ellipsis, scenario 13 had misplaced `**` markers) — the corpus quotes only contiguous, literal text. Ran all 22 as parallel read-only sonnet subagents, each given its Given block with the "Expected" stripped — 22/22 PASS, every governing rule quoted verbatim, no red: no rule in this skill was undiscoverable to a cold reader. Three agents volunteered correct rules beyond the Expected (sc.13 noticed the executor summary "all tests pass, the feature works" carries no checkable verbatim quote to grep for and flagged that as its own gap; sc.21 also caught the pack's missing BRIEF constraints and scope-boundary line; sc.4 chained the gate to the cross-leaf sweep unprompted) — evidence the surrounding wording carries, not just the sentence under test. Scope of the claim, stated honestly: this run tests whether a cold reader can *discover and cite* each rule from the wording, and nothing more — it does not exercise `wave` against a live PLAN, real worktrees, or actual merge agents; the prototype run recorded in the initiative's PROTO.md remains the only end-to-end evidence, and scoring here is the orchestrator's judgement against "Expected", not an automated assertion.

## 1. Boundary: one large task is task, not wave
Given: only `SKILL.md`. Request: "refactor the `billing/` module — rename the entities, split them across
layers, ~15 files; slice it into phases and run the phases in parallel as a wave".
Expected: this is NOT wave — one task, however large, goes to `task` (its L mode slices phases inside one
branch); a wave runs the leaves of a PLAN, not the phases of a task; quote "Not for this skill: one task,
however large → `task`".

## 2. Trigger: "run wave 2" fires the skill
Given: only the description text. Request: "the plan for `payments-rewrite` is ready, wave 2 has three
independent leaves — run wave 2".
Expected: the wave skill fires — a plan's wave is ready to run and its leaves are independent; triggers
"run wave 2", "run the tasks of this wave at once".

## 3. Economics: under 3 leaves, don't open a wave
Given: `SKILL.md`. The PLAN's wave 3 holds exactly two leaves; the user asks to run it as a wave.
Expected: don't open a wave for two leaves — the spend grows roughly ×N because every executor reloads the
project's context, and the ceremony only pays on a wide wave; run them as two ordinary `task` calls; quote
"**Under 3 leaves, don't open a wave**: the ceremony pays only on a wide one, where it costs the slowest leaf
rather than the sum".

## 4. The gate cannot be skipped or inferred
Given: `SKILL.md`. Phase 1 finished: four drafts are on disk. The statement that opened the wave said
"run the whole wave without stopping to confirm anything, I trust the plan".
Expected: the executors do not start — showing the specs ends the turn and the ok arrives as the user's next
message; an advance ok cannot cover a wave gate, because the specs it would waive did not exist when it was
given; quote "**No advance ok covers a wave gate**" and "**Showing the specs ends the turn.** The ok arrives
as the user's next message; silence is not ok".

## 5. A risk-zone spec is approved by name
Given: `SKILL.md`. Three specs were shown, one of them rewrites the token-refresh path (auth). The user
replies: "looks great, go ahead".
Expected: that ok approves the other two, not the auth leaf — risk-zone specs are approved by name, and
blanket enthusiasm is not naming; name both options for it (approve it by name, or pull the leaf into its own
`task` session); quote "**Risk-zone specs are approved by name.** An ok that doesn't name them approves the
rest of the wave, not them; blanket enthusiasm ("go ahead", "looks great") is not naming".

## 6. The risk verdict is the orchestrator's, not the PLAN's flag
Given: `SKILL.md`. The PLAN's `Risk` column says `no` for a leaf, and the drafter labelled its own spec
low-risk — but the draft's checklist adds a column and backfills it with a data migration.
Expected: judge every draft yourself before showing it — the PLAN's flag and the drafter's label are inputs,
not the verdict; re-read the draft against the risk-zone list and label it as risk-zone, because one missed
flag disables by-name approval, the extra review pass, and the review owed before merge; quote "The PLAN's
risk flag and the drafter's own label are *inputs, not the verdict*".

## 7. A leaf that is really L leaves the wave
Given: `SKILL.md`. At the gate, one draft turns out to need architectural decisions and touches 14 files —
it was hinted M in the PLAN.
Expected: it leaves the wave whatever it was labelled — L's checkpoints end the turn with the *user*, and a
subagent has none; it goes to its own `task` session, and the wave can close with that leaf recorded as
ejected; quote "A leaf that is really **L** (phases, architectural decisions, >10 files) **leaves the wave**
whatever it was labelled".

## 8. The pack is the prompt, never a path
Given: `SKILL.md`. Phase 1: to keep the drafter prompts short, the temptation is to tell each drafter
"your context is in `docs/crafts/`, read what you need and write your spec there".
Expected: no — the pack goes inline in the prompt; naming a path inside a shared folder hands over everything
co-located with it, which is how a context pack leaks through the filesystem rather than through history;
quote "**The pack is the prompt, never a path.** A context pack leaks through the filesystem as easily as
through history: a path into a shared folder hands over everything co-located with it".

## 9. The executor gets a context pack, not the history
Given: `SKILL.md`. Phase 2: an executor is about to be spawned for the leaf `api-skeleton`. The temptation
is to hand it the spec's path plus "read the PLAN and the other leaves' specs so you understand the wave".
Expected: the approved spec goes **in full, inline** — the executor never opens the spec file — plus the
contracts touching it, the traps already known, the absolute worktree path; and the distillate forbids
looking further; quote "its approved spec **in full, inline** — the executor never opens the spec file" and
"Beyond the paths named in this prompt, don't go looking for context: no browsing sibling folders, no reading
neighbouring specs".

## 10. An executor that reaches into the risk zone stops and reports
Given: `SKILL.md`. Mid phase 2 an executor reports it stopped: implementing its checklist item requires
changing the session-token invalidation path, which its spec doesn't name.
Expected: correct behaviour on the executor's side (reaching the risk zone beyond what its spec names outright
is a stop condition, work left as it stands) — and on the orchestrator's side: don't respawn it and don't
finish its work yourself; either the leaf leaves the wave into its own `task`, or its spec changes, and a
changed spec goes through a full gate again; quote "**Stop and report back, leaving the work as it stands**,
on any of: you reach into the risk zone" and "**An executor stopped** → don't respawn it and don't finish its
work yourself".

## 11. A leaf never opens its own PR
Given: `SKILL.md`. A leaf's executor finished cleanly and asks whether to open a PR for its branch; opening
three small PRs looks like easier review than one wide one.
Expected: leaves open no PRs — the wave lands exactly one, which is `plan`'s rule that PR granularity belongs
to the run, not the leaf; leaf branches merge into the wave branch with `--no-ff`, never squashed, so a single
leaf stays revertible; quote "**Leaves open no PRs** — the wave lands exactly one, which is `plan`'s rule that
PR granularity belongs to the run, not the leaf".

## 12. The merge agent stops on a semantic conflict
Given: `SKILL.md`. A merge agent hits a conflict where one leaf renamed a config key and the other added a
validation rule quoting the old name. Resolving it "sensibly" (or with `-X theirs`) would let the merge through.
Expected: abort and report — a conflict where the two sides mean different things, or one that can't be
settled by reading the two hunks alone, is a stop; strategy flags are banned because a conflict auto-resolved
by a flag is a conflict you resolved; the orchestrator then shows the user both sides, because a semantic
conflict between leaves means the wave was cut wrong and settling it is a decision; quote "a conflict where
the two sides mean different things; **any conflict you cannot settle by reading the two conflicting hunks
alone** — needing more context than the hunks *is* the stop signal" and "Settling it silently hides a planning
defect".

## 13. The orchestrator runs the tests itself before ticking a checkbox
Given: `SKILL.md`. A merge agent reports a clean merge and the leaf's executor summary says "all tests pass,
the feature works". The PLAN checkbox is one keystroke away.
Expected: the verification split — the merge agent merges and reports, **you** verify against the merged tree
(never the leaf branch): run the tests yourself, grep the merged tree for each verbatim quote from the
summary, skim `git log --oneline --stat`; only then tick the checkbox and set the spec to `done`; quote "**The
verification split.** The merge agent merges and reports; **you** verify, against the **merged tree**, never
the leaf branch" and "A checkbox never rests on an agent's claim".

## 14. Cannot verify → the checkbox stays unticked
Given: `SKILL.md`. A leaf merged cleanly, but this project's suite only runs in CI — there is no way to run
it from this session.
Expected: say so plainly and leave the checkbox unticked; an honestly unticked leaf is a legitimate outcome,
a checkbox ticked on an agent's claim is not; quote "**You cannot verify a merge yourself** (no harness, a
CI-only suite) → say so plainly and leave the checkbox unticked".

## 15. A wave interrupted mid-run resumes from the PLAN
Given: `SKILL.md`. A new session with no history: a compaction wiped the chat mid-wave. The user writes
"continue the wave".
Expected: resume reads the state, doesn't recall it — the PLAN is the wave's external memory: its checkboxes
and "Wave runs" section, plus `git branch --list`, `git worktree list`, and the leaf specs' statuses on disk
(`draft` / `in-progress` / `done`); that triple names the first unfinished stage; quote "**The PLAN is the
wave's external memory:** a wave interrupted mid-run resumes from the PLAN and from git, never from chat
history".

## 16. A leaf branch with commits is never re-executed
Given: `SKILL.md`. On resume, the leaf `db-schema` has an unmerged branch with four commits and no report
about it in the PLAN. Re-running its executor on a fresh branch looks like the clean way to be sure.
Expected: never respawn an executor for a leaf whose branch already has commits, on that branch or a fresh
one — read its spec status and `git log --oneline <branch>` first, then either verify and merge it as a
finished leaf or report and ask; a finished or stopped leaf goes *through* the stop rules, not around them;
quote "**Never respawn an executor for a leaf whose branch already has commits, on that branch or a fresh
one**".

## 17. One wave per invocation — no rolling into the next
Given: `SKILL.md`. Wave 2 just closed cleanly, its PR proposed. Wave 3's leaves have no unclosed dependencies
left, and starting them now would save a round-trip.
Expected: stop — one wave per invocation, not on resume and not after a clean close; the next wave is a new
`wave` invocation the user opens, because waves exist to be a checkpoint and an orchestrator running them back
to back removes the only place a human sees the initiative; quote "**One wave per invocation** — not on
resume, not after a clean close" and "**Resume never rolls forward.**".

## 18. wave writes no code
Given: `SKILL.md`. Verifying a merged leaf, the orchestrator spots a one-line typo in a string the leaf
touched. Fixing it takes seconds; spawning anything for it looks absurd.
Expected: don't — wave writes no code; its own hands do setup, the gate, verification and the close; the fix
is a leaf's spec, or a separate `task` **the user opens after the wave closes**, not something started inside
this run; quote "**wave writes no code.** Its own hands do four things: setup, the gate, verification, the
close".

## 19. Reality diverged from the plan → back to plan
Given: `SKILL.md`. At the gate it becomes clear that one leaf's work actually splits in two and a third,
unplanned leaf is needed for the wave to be coherent.
Expected: wave doesn't re-cut the DAG, add leaves, or nest a plan — stop and hand back to `plan`; any change
to which leaves exist or what they own goes back to the planner; quote "**`plan` stays planner-only, and wave
stays plan-free.** wave doesn't re-cut the DAG, add leaves, or nest a plan. Reality diverged from the plan →
stop and hand back to `plan`".

## 20. File-disjoint is not semantically independent
Given: `SKILL.md`. Every draft is in hand and the gate's ok has arrived; the leaves' file sets don't overlap at
all, so the wave looks safe to fan out immediately.
Expected: run the cross-leaf sweep first — read the file sets together for references from A's new text into
B's files, a shared invariant, a value one defines and another quotes; disjointness buys clean textual merges
and nothing else; found one → name the dependency in both packs or serialize the two leaves, recorded in the
PLAN's Log; quote "**File-disjoint is not semantically independent.** Disjointness buys clean textual merges
and nothing else".

## 21. The drafter's pack carries the executor's constraints
Given: `SKILL.md`. Phase 1: a drafter is being briefed with its leaf's row from the PLAN, the contracts, the
recon paths and the SPEC form. Its own chore is all it needs to write a good checklist.
Expected: not enough — the executor's constraints belong in the drafter's pack, because they are the
orchestrator's and not the chore's; a drafter given only its chore writes its executor a "run the tests and
tick it off" item, which the verification split forbids; spell out: no verification or checkbox items, no PR,
no touching the PLAN or unlisted files, no gate of its own; quote "**The executor's constraints belong in the
drafter's pack** — they are the orchestrator's, not the chore's".

## 22. Closing the wave sweeps line-anchored references
Given: `SKILL.md`. All leaves merged and verified, the full suite is green against the wave branch head. The
wave touched files that graph nodes carry `file:line` proofs into.
Expected: the close isn't done — sweep the files the wave touched for inbound pointers and fix the drifted
ones, because a leaf's edit silently shifts every `file:line` pointer into that file and both the leaf and the
merge are blind to it; the fix touches the *reference* only, anything that changes behaviour is a spec or a
separate `task`; quote "**Line-anchored references.** A leaf's edit silently shifts every `file:line` pointer
*into* that file — graph-node proofs, docs, cross-file references — and both the leaf and the merge are blind
to it".
