---
name: wave
description: Running one wave of a PLAN in parallel — a fan-out of spec drafters, ONE human gate over the whole wave, a fan-out of executors in their own worktrees, then sequential merges, verification, and a single PR for the wave. Use this skill when a plan's wave is ready to run and its leaves are independent — "run the wave", "run wave 2", "execute the plan's wave", "run these leaves in parallel", "kick off the wave", "run the tasks of this wave at once", "continue the wave", "where is the wave" — even without the words "wave" or "skill". Not for a single task, however large (that's `task` — its L mode slices phases inside one branch), not for building or re-cutting the DAG (that's `plan`), not for one leaf of a wave (a plain `task` call), and not for review (`code-review`).
---

# wave — running one wave of a PLAN in parallel

Principle: **wave sits BESIDE `task`, under `plan`.** `plan` lays an initiative out into waves and stops at
hand-off; `task` runs one leaf; wave runs **one wave** — N independent leaves in parallel, each a subagent in its
own worktree, **one** human gate over the whole wave, one PR at the end. It is the execution layer plan
deliberately refuses to be.

What you buy is **wall-clock, not tokens**: every executor reloads the project's context, so a wave's spend grows
roughly ×N — measured, ~23–26 subagent tokens per token of the orchestrator's own growth. The orchestrator's
context stays cheap and therefore gives you no feedback at all about the money being spent. **Under 3 leaves,
don't open a wave** — run them as ordinary `task` calls; the ceremony pays for itself only on a wide wave, and
then it costs the slowest leaf rather than the sum.

Not for this skill: one task, however large → `task`; building or re-cutting the DAG → `plan`; a single leaf → a
plain `task` call; review → `code-review`. The leaves turn out not to be independent → stop, back to `plan`.

## Step 0. Orientation and resume

There's a `CRAFT.md` → read it first, then the initiative's plan at `docs/crafts/<initiative>/PLAN.md`. **The PLAN
is the wave's external memory:** a wave interrupted mid-run resumes from the PLAN and from git, never from chat
history — a compaction eats the chat and leaves the artifacts. The craftlight block upsert in the root
`CLAUDE.md` (procedure — `skills/task/templates/CLAUDE-block.md`) rides with wave's first write to disk, whichever
comes first — the PLAN append below or phase 1's specs — and never before one of them.

- **Read the state, don't recall it:** the PLAN's checkboxes and "Wave runs" section (merge order, per-leaf
  status, what stopped) + `git branch --list 'wave/*' 'task/*'` + `git worktree list` + the leaf specs on disk
  (`draft` = gate not passed, `in-progress` = approved and running, `done` = merged and verified). That triple
  names the first unfinished stage; continue there.
- A leaf branch with commits but unmerged → its executor finished or stopped: read its spec status and
  `git log --oneline <branch>` before deciding — verify and merge it as a finished leaf (step 5), or report it
  and ask. **Never respawn an executor for a leaf whose branch already has commits, on that branch or a fresh
  one** — a finished or stopped leaf goes *through* the stop rules, not around them.
- An older PLAN without a "Wave runs" section or a `Wave branch` field → append them, don't fail on their absence.
- **Resume never rolls forward.** "Continue the wave" means the wave already in flight. Every leaf of it is
  ticked → the run is over: report and stop. The next wave is one the user names.
- A wave in flight and the message brings something else → one FYI line: `parked: wave <N> of "<initiative>" is
  in flight — say "continue the wave" to get back to it`.
- **Precondition:** every dependency of this wave's leaves is closed (earlier waves ticked) and the leaves still
  match the PLAN. Not so → say it in one line and stop; a wave started over an open dependency merges garbage.

## Step 1. Wave setup

- **Pick the wave:** the user named one → that one; otherwise the first wave with unclosed leaves. One per run.
- **Topology.** Your own checkout stays on the **default branch** — that's where PLAN edits are committed. The
  wave branch and every leaf get a worktree of their own, created by hand:

```
git switch -c wave/<initiative>-w<N> <default>   &&  git switch <default>
git worktree add <wt-root>/wave  wave/<initiative>-w<N>
git worktree add <wt-root>/<leaf> -b task/<leaf> wave/<initiative>-w<N>   # one per leaf
```

  `<wt-root>` = `.worktrees/` when it is git-ignored, otherwise `../<repo>-wt/` outside the repo — an in-repo
  worktree that git tracks would dirty the tree. A branch can only be checked out once, which is why the wave
  branch needs its own worktree: it is where every merge happens. Write the wave branch into the PLAN's
  `Wave branch` field. Never use the Agent tool's `isolation: "worktree"` — it gives the agent a *throwaway*
  worktree of its own and defeats a named-branch topology entirely.
- **The Agent tool takes no `cwd`** — every agent prompt carries the absolute worktree path, the instruction to
  prefix every git command with `git -C <abs> …`, and an explicit ban on touching any other checkout: two
  checkouts of one repo, one wrong path from corruption.
- **Recon once, for the whole wave:** the file paths each leaf will touch, the project's test command, the
  `active` nodes in `docs/graph/` on the wave's topics. What you learn here is what the packs carry — N executors
  re-deriving it is exactly the ×N multiplier.

## Step 2. Phase 1 — the drafter fan-out

One drafter per leaf, all in parallel, each a `general-purpose` subagent given its pack **inline in the prompt**.
Never hand a drafter a write path inside a shared folder: naming a path hands over everything co-located with it,
which is how a context pack leaks through the filesystem rather than the prompt.

The pack: the leaf's row from the PLAN (goal, size hint, risk flag, files/area) + the PLAN contracts touching
this leaf + the parent BRIEF's constraints and rejected options + the recon paths + the `active` graph nodes on
its topic + the form of `skills/task/templates/SPEC.md` + **the executor's constraints** + "beyond the paths named
here, don't go looking for context — no browsing sibling folders, no reading neighbouring specs".

**The executor's constraints belong in the drafter's pack** — they are the orchestrator's, not the chore's. A
drafter given only its chore writes its executor a "run the tests and tick it off" item, which the verification
split forbids. Spell out: no verification or checkbox items, no PR, no touching the PLAN or files its own spec
doesn't list, no gate of its own; scope is this leaf alone.

Output: **the spec as text in the reply**, per the SPEC template, status `draft`, with `task`'s S/M/L
classification. **The orchestrator writes the file** to `docs/crafts/<leaf-slug>/SPEC.md` — flat neighbours,
never nested, so `task`'s resume glob (`docs/crafts/*/SPEC.md`) finds them. This costs nothing (the gate makes
you read every spec in full anyway) and removes the filesystem leak.

## Step 3. The wave gate — one ok, over drafts

The gate sits over **drafts**, before any executor runs: a drafting error caught here costs a redraft; the same
error caught over a finished diff costs the wave.

- **Judge every draft yourself, before showing it.** The PLAN's risk flag and the drafter's mode are *inputs, not
  the verdict*: re-read each draft against the risk-zone list (auth/secrets, money, migrations & data deletion,
  PII, concurrency invariants, external API contracts) and against `task`'s size signals. A leaf that is really
  **L** — phases, architectural decisions, >10 files — **leaves the wave** whatever the drafter labelled it: L's
  checkpoints end the turn with the *user*, and a subagent has none. One missed risk flag disables three guards
  at once (by-name approval, the extra review pass, the mandatory `code-review`), so this judgement is yours.
- **Show every spec in one message** — the **full text of each pasted into the message**. A path, a link, or your
  own summary is not showing: a gate puts the artifact in front of the user. With them: the cross-leaf sweep, the
  proposed merge order, and anything you corrected in a draft.
- **Label each risk-zone spec as such, naming which zone it enters** — an ok that merely enumerates leaf names
  has not been told there was a risk to approve.
- **Showing the specs ends the turn.** The ok arrives as the user's next message; silence is not ok. No next
  message is possible (an unattended run) → the wave stops here, and stopping is the correct outcome.
- **No advance ok covers a wave gate:** when such an ok could be given, the specs it would waive don't exist yet.
- **Risk-zone specs are approved by name.** An ok that doesn't name them approves the rest of the wave, not them;
  blanket enthusiasm ("go ahead", "looks great") is not naming. Showing such a spec, name both options: approve
  it by name, or pull the leaf out into its own `task` session.
- **Only leaves the ok covered go to phase 2.** A leaf pulled out, judged L, or sent back for edits doesn't — and
  a **redraft re-enters a full gate**: showing it ends the turn again, however recently the others were approved.
- **The ok is written to disk before any executor starts**: approved specs → status `in-progress`, committed on
  the wave branch; the PLAN's "Wave runs" row records the wave, its leaves and their state. The gate is a stage
  boundary, and an unrecorded boundary is one a compaction erases.

**The cross-leaf sweep, before phase 2.** File-disjointness is what a wave is cut for and it is *all* it buys:
two leaves can be perfectly disjoint and still collide in meaning — one writing a reference *into* a file the
other rewrites, one relying on text the other deletes. With every draft in hand, read the file sets together and
look for references from A's new text into B's files, a shared invariant, a value one defines and another quotes.
Found one → name the dependency in both packs (who owns the final wording) or serialize the two leaves inside
this wave, recording it in the PLAN's Log. Any change to *which leaves exist or what they own* goes back to `plan`.

## Step 4. Phase 2 — the executor fan-out

One executor per approved leaf, all in parallel, `general-purpose`, pack **inline**:

- its approved spec **in full, inline** — the executor never opens the spec file;
- the absolute worktree path, its branch name, `git -C <abs> …`, the ban on other checkouts;
- the PLAN contracts touching it, and the constraints that apply (graph nodes, the test command);
- **the traps you already know** in its files — a file that can't be read whole, a formatting tool that corrupts
  under the wrong locale, a generated section. A trap the orchestrator knows and the pack omits is a trap the
  leaf walks into;
- the summary contract with its reason: quote the **final text verbatim**, don't paraphrase — the orchestrator
  checks the merged tree against those quotes. A summary is checkable exactly to the extent the pack demanded;
- the rule distillate, copied **verbatim** into every executor prompt:

> You are one leaf of a wave. Work only inside the worktree at `<abs path>`, on branch `<task/leaf>`; every git
> command as `git -C <abs> …`; never touch another checkout of this repo, and never merge, rebase, push, or open
> a PR. **Do not spawn subagents** — everything in your scope you do with your own hands. Scope = your spec's
> checklist only; never edit SPEC.md, the PLAN, or any file your spec doesn't list, and nothing "while we're at
> it" — foreign findings go into your summary, not into code. Beyond the paths named in this prompt, don't go
> looking for context: no browsing sibling folders, no reading neighbouring specs (running the project's tests
> and git commands is not browsing). Test-first for new behaviour logic; a bugfix starts from a failing repro
> test; configs, texts, and cosmetics need no new tests. One atomic commit per checklist item, staged with an
> explicit `git add <files>`, never `-A`, never squashed. Do not run the wave's verification and do not tick
> anything off — the orchestrator runs the tests and owns the checkboxes. Report only the observed: didn't
> verify → say so; "should work" is forbidden; quote the final text of what you wrote verbatim instead of
> paraphrasing it. **Stop and report back, leaving the work as it stands**, on any of: you reach into the risk
> zone (auth/secrets, money, migrations & data deletion, PII, concurrency invariants, external API contracts)
> beyond what your spec names outright; a second rejected fix hypothesis or a second failed experiment; the
> change needs a file or a decision outside your spec; you find another leaf's work colliding with yours — a
> collision between leaves is a planning signal, not yours to resolve.

Wall clock is the slowest leaf, and leaf size isn't knowable in advance — a leaf that read as one file becomes
three at recon. Don't re-plan the wave around the straggler; the barrier is what a wave costs.

## Step 5. Integration — one merge agent per merge, sequential

- **Topology (M1).** Leaf branches merge back into the wave branch with `--no-ff` and **never squashed**, so a
  single leaf stays revertible as its own commits. **Leaves open no PRs** — the wave lands exactly one. This is a
  deliberate revision of `plan`'s "a leaf = one branch, one PR" for leaves run inside a wave.
- **Order:** the **referenced** leaf merges first, so the text pointing at it lands on final wording; otherwise
  smallest blast radius first. Merges are **sequential** — parallel merge agents race on one branch.
- **A throwaway merge agent per merge**, working in the wave branch's worktree. A clean merge costs the
  orchestrator nothing; a dirty one would drag the whole conflict into its context. Its pack: the two branch
  names, the wave worktree's absolute path, the leaf's file list, **which of those paths are risk-zone** (it
  cannot classify them itself), and the distillate, verbatim:

> Merge `<task/leaf>` into `<wave branch>` in the worktree at `<abs>`. Plain `git -C <abs> merge --no-ff` only —
> never squash, never rebase, never push, never open a PR, and never `-X ours/theirs`, `-s ours`, or
> `checkout --ours/--theirs`: a conflict auto-resolved by a strategy flag is a conflict you resolved. Resolve
> only **mechanically trivial** textual conflicts — both sides appended to the same list, an import block, a
> changelog line — keeping both sides' text, and report exactly what you resolved and how. **Abort
> (`git -C <abs> merge --abort`) and report** on any of: a conflict touching a path this prompt lists as
> risk-zone; a conflict where the two sides mean different things; **any conflict you cannot settle by reading
> the two conflicting hunks alone** — needing more context than the hunks *is* the stop signal. Do not run tests,
> do not fix code, do not touch files outside the conflict. Report: the merge commit, the files changed, every
> conflict and how it went.

- **A merge that stopped stops that leaf, not the wave's other merges.** Show the user both sides: a semantic
  conflict between leaves means the wave was cut wrong, and resolving it is a decision — an ordinary `task` on
  the wave branch, or back to `plan`. Resolving it silently hides a planning defect.
- **The verification split.** The merge agent merges and reports; **you** verify, against the **merged tree**,
  never the leaf branch (that tests text nobody has agreed to integrate):
  1. run the project's tests/scenarios yourself;
  2. grep the merged tree for **each verbatim quote** from the leaf's summary — `git diff --stat` shows filenames
     and confirms nothing about content, so it never settles a claim on its own;
  3. skim `git log --oneline --stat <task/leaf>` — a commit per checklist item, nothing foreign staged.
- **Only then tick the leaf's PLAN checkbox. A checkbox never rests on an agent's claim** — `[[done-is-observed]]`
  at the wave's scale. Trust doesn't remove verification; specific claims make it cheap.
- A **risk-zone leaf** gets one more pass: a fresh subagent *reviewing* just those spots (hand it that diff plus
  the leaf's criteria, not the whole context). That is a review, not the verification — the test run and the
  checkbox stay yours.

## Step 6. Closing the wave

1. **A full run of the affected suite** against the wave branch head — per-leaf runs don't cover interactions.
   "Affected" = every suite covering any file any leaf touched; can't scope it → run the whole suite. Red →
   untick nothing silently: name the leaves whose interaction it implicates and hand it to `task` (or `debug`
   when the cause is unknown). A red wave doesn't close.
2. **Line-anchored references.** A leaf's edit silently shifts every `file:line` pointer *into* that file —
   graph-node proofs, docs, cross-file references — and both the leaf and the merge are blind to it. Sweep the
   files the wave touched for inbound pointers and fix the drifted ones. This touches the *reference* only — a
   line number, a link target; anything that changes behaviour is a leaf's spec or a separate `task`.
3. **The PLAN**, committed from your default-branch checkout: leaf checkboxes (ticked in step 5, on observation),
   the "Wave runs" row (merge order, per-leaf status, what stopped), and a Log paragraph — merge order, what the
   gate corrected, what stopped and why. A leaf that left the wave is recorded there with its reason, its
   checkbox untouched; a wave can close with an ejected leaf, but never with a silent one.
4. **One PR for the wave**, by proposal (proposing is not creating). Body: the wave's goal, its leaves, how each
   was verified. Say plainly whether a Full `code-review` is owed — **it is required before this PR merges when
   the wave carried a risk-zone leaf**, offered otherwise: M1 makes one PR out of N leaves, exactly when review
   gets coarse.
5. **Cleanup, in this order:** `git worktree remove` every leaf worktree now; **keep the leaf branches until the
   wave's PR merges** — they are the revert granularity the no-squash rule bought — then delete them. Leave no
   orphaned worktrees.
6. **CRAFT.md, the graph, the glossary** — `task`'s global wrap rule, owned here: a leaf never sees the whole
   wave, so the durable decisions, invariants and gotchas that outlived it are the orchestrator's to record.
7. **Report and stop.** The next wave is a new `wave` invocation, opened by the user.

## Rules

- **One wave per run.** wave never rolls on into the next — not on resume, not after a clean close: waves exist
  to be a checkpoint, and an orchestrator that runs them back to back has removed the only place a human sees
  the initiative.
- **The gate is never weakened in the risk zone.** Batched ≠ waived: risk-zone specs by name and labelled as
  risk-zone, no advance ok, showing the specs ends the turn. `[[risk-zone-min-m]]` and `[[confirm-gate]]` hold at
  the wave's scale, and classifying the risk is the orchestrator's job, not the PLAN flag's.
- **`plan` stays planner-only, and wave stays plan-free.** wave doesn't re-cut the DAG, add leaves, or nest a
  plan. Reality diverged from the plan → stop and hand back to `plan`.
- **wave writes no code.** Its own hands do four things: setup, the gate, verification, the close. Tempted to
  "just fix this one myself" → that's a leaf's spec, or a separate `task` **the user opens after the wave
  closes** — not something you start inside this run.
- **The pack is the prompt, never a path.** `[[context-pack-not-history]]` leaks through the filesystem too: a
  path into a shared folder hands over everything co-located with it.
- **File-disjoint is not semantically independent.** Disjointness buys clean textual merges and nothing else.

## Stop rules

- **An executor stopped** → don't respawn it and don't finish its work yourself: report what it stopped on.
  Either the leaf leaves the wave (its own `task`), or its spec changes — and a changed spec goes through a full
  gate again.
- **Two executors stopped for the same reason, or leaves collided in a merge** → the cut is wrong, not the
  execution: back to `plan` with what you saw.
- **A dependency isn't closed, or a leaf's spec no longer matches the PLAN** → don't start; say what diverged.
- **A compaction mid-wave** costs nothing *if* the PLAN and the leaf specs are current — so write state to disk
  at each stage boundary, not at the end.
- **You cannot verify a merge yourself** (no harness, a CI-only suite) → say so plainly and leave the checkbox
  unticked. An honestly unticked leaf is a legitimate outcome; a checkbox ticked on an agent's claim is not.
