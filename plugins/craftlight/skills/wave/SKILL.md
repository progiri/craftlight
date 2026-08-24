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
context stays cheap and therefore gives you no feedback at all about the money being spent. Two small leaves
rarely repay the ceremony; a wide wave of genuinely independent leaves does, and it costs the slowest leaf rather
than the sum.

Not for this skill: one task, however large → `task` (L slices it into phases inside one branch); building or
re-cutting the DAG → `plan`; a single leaf → a plain `task` call; review → `code-review`. The leaves turn out not
to be independent → stop and hand back to `plan`.

## Step 0. Orientation and resume

There's a `CRAFT.md` → read it first, then the initiative's `PLAN.md`. **The PLAN is the wave's external memory:**
a wave interrupted mid-run resumes from the PLAN and from git, never from chat history — a compaction eats the
chat and leaves the artifacts. The craftlight block upsert in the root `CLAUDE.md` (procedure —
`skills/task/templates/CLAUDE-block.md`) rides with wave's first write to disk (phase 1's spec drafts), never
earlier.

- **Read the state, don't recall it:** the PLAN's checkboxes and "Wave runs" section (merge order, per-leaf
  status, what stopped) + `git branch` (which `wave/…` and leaf branches exist) + `git worktree list` + the leaf
  specs on disk (`draft`/`in-progress`/`done`). That triple names the first unfinished stage; continue there.
- A leaf branch with commits but unmerged → its executor finished or stopped: read its spec status and the
  branch log first. **Never respawn an executor over a branch that already has commits** — you'd clobber work.
- An older PLAN without a "Wave runs" section or `Wave branch` field → append them, don't fail on their absence.
- A wave in flight and the message brings something else → one FYI line: `parked: wave <N> of "<initiative>" is
  in flight — say "continue the wave" to get back to it`.
- **Precondition:** every dependency of this wave's leaves is closed (earlier waves ticked) and the leaves still
  match the PLAN. Not so → say it in one line and stop; a wave started over an open dependency merges garbage.

## Step 1. Wave setup

- **Pick the wave:** the user named one → that one; otherwise the first wave with unclosed leaves. One per run.
- **Wave branch** `wave/<initiative>-w<N>` cut from the default branch, written into the PLAN's `Wave branch`
  field. Leaf branches `task/<leaf>` are cut **from the wave branch** and merged back into it.
- **A worktree per leaf, created by hand.** `.worktrees/` is git-ignored → `.worktrees/<leaf>/`; it isn't →
  `../<repo>-wt/<leaf>/`, outside the repo, since an in-repo worktree would dirty the tree. Never use the Agent
  tool's `isolation: "worktree"`: it gives the agent a *throwaway* worktree of its own and defeats a named-branch
  topology entirely.
- **The Agent tool takes no `cwd`** — every leaf prompt carries the absolute worktree path, the instruction to
  prefix every git command with `git -C <abs> …`, and an explicit ban on touching any other checkout: two
  checkouts of one repo, one wrong path from corruption.
- **Recon once, for the whole wave:** the file paths each leaf will touch, the project's test command, the
  `active` graph nodes on the wave's topics. What you learn here is what the packs carry — N executors
  re-deriving it is exactly the ×N multiplier.

## Step 2. Phase 1 — the drafter fan-out

One drafter per leaf, all in parallel, each a `general-purpose` subagent given its pack **inline in the prompt**.
Never hand a drafter a write path inside a shared folder: naming a path hands over everything co-located with it,
which is how a context pack leaks through the filesystem rather than the prompt.

The pack: the leaf's row from the PLAN (goal, size hint, risk flag, files/area) + the PLAN contracts touching
this leaf + the parent BRIEF's constraints and rejected options + the recon paths + the `active` graph nodes on
its topic + the form of `skills/task/templates/SPEC.md` + **the executor's constraints** + an explicit "do not
read, list, or search any directory other than the ones named here".

**The executor's constraints belong in the drafter's pack** — they are the orchestrator's, not the chore's. A
drafter given only its chore writes its executor a "run the tests and tick it off" item, which the verification
split forbids. Spell out: no verification or checkbox items, no PR, no touching the PLAN or another leaf's files,
no gate of its own; scope is this leaf alone.

Output: **the spec as text in the reply**, per the SPEC template, status `draft`, mode by `task`'s own signals
(risk zone → minimum M). **The orchestrator writes the file** to `docs/crafts/<leaf>/SPEC.md` — flat neighbours,
never nested, so `task`'s resume glob finds them. This costs nothing (the gate makes you read every spec in full
anyway) and removes the filesystem leak.

A leaf that drafts as **L leaves the wave**: L's checkpoints end the turn with the *user*, and a subagent has
none. Say so at the gate; the user runs it as its own `task` session.

## Step 3. The wave gate — one ok, over drafts

The gate sits over **drafts**, before any executor runs: a drafting error caught here costs a redraft; the same
error caught over a finished diff costs the wave.

- **Show every spec in one message** — each read in full by you. A gate puts the *artifact* in front of the user;
  never stake an ok on a drafter's paraphrase. With them: the cross-leaf sweep, the proposed merge order, and
  anything you corrected in a draft.
- **Showing the specs ends the turn.** The ok arrives as the user's next message; silence is not ok. This is
  `[[confirm-gate]]` *batched*, not weakened — one ok covers N leaves because it covers N **shown** specs.
- **No advance ok covers a wave gate:** when such an ok could be given, the specs it would waive don't exist yet.
- **Risk-zone specs are approved by name.** An ok that doesn't name them approves the rest of the wave, not them;
  blanket enthusiasm ("go ahead", "looks great") is not naming. Showing such a spec, name both options: approve
  by name, or pull the leaf out into its own `task` session.
- Outcomes: approved leaves go to phase 2; a leaf pulled out, drafted as L, or sent back for edits does not — a
  redrafted leaf re-enters a gate. The wave never starts half-approved.

**The cross-leaf sweep, before phase 2.** File-disjointness is what a wave is cut for and it is *all* it buys:
two leaves can be perfectly disjoint and still collide in meaning — one writing a reference *into* a file the
other rewrites, one relying on text the other deletes. With every draft in hand, read the file sets together and
look for references from A's new text into B's files, a shared invariant, a value one defines and another quotes.
Found one → name the dependency in both packs (who owns the final wording), serialize the two leaves, or hand the
pair back to `plan`. Neither leaf can see this: each knows only its own files.

## Step 4. Phase 2 — the executor fan-out

One executor per approved leaf, all in parallel, `general-purpose`, pack **inline**:

- its approved spec **in full, inline** — the executor never opens the spec file;
- the absolute worktree path, its branch name, `git -C <abs> …`, the ban on other checkouts;
- the PLAN contracts touching it, and the constraints that apply (graph nodes, the test command);
- **the traps you already know** in its files — a file that can't be read whole, a formatting tool that corrupts
  under the wrong locale, a generated section. A trap the orchestrator knows and the pack omits is a trap the
  leaf walks into;
- the summary contract with its reason: quote the **final text verbatim**, don't paraphrase — "the orchestrator
  will check the merge against this without re-reading your diff". A summary is checkable exactly to the extent
  the pack demanded it be;
- "do not read, list, or search any directory other than the ones named here";
- the rule distillate, copied **verbatim** into every executor prompt:

> You are one leaf of a wave. Work only inside the worktree at `<abs path>`, on branch `<task/leaf>`; every git
> command as `git -C <abs> …`; never touch another checkout of this repo, and never merge, rebase, push, or open
> a PR. Scope = your spec's checklist only — nothing "while we're at it"; foreign findings go into your summary,
> not into code. Test-first for new behaviour logic; a bugfix starts from a failing repro test; configs, texts,
> and cosmetics need no new tests. One atomic commit per checklist item, staged with an explicit `git add
> <files>`, never `-A`, never squashed. Never edit SPEC.md, the PLAN, or another leaf's files. Do not run the
> wave's verification and do not tick anything off — the orchestrator runs the tests and owns the checkboxes.
> Report only the observed: didn't verify → say so; "should work" is forbidden; quote the final text of what you
> wrote verbatim instead of paraphrasing it. **Stop and report back, leaving the work as it stands**, on any of:
> you reach into the risk zone (auth/secrets, money, migrations & data deletion, PII, concurrency invariants,
> external API contracts) beyond what your spec names outright; a second rejected fix hypothesis or a second
> failed experiment; the change needs a file or a decision outside your spec; you find another leaf's work
> colliding with yours — a collision between leaves is a planning signal, not yours to resolve.

Wall clock is the slowest leaf, and leaf size isn't knowable in advance — a leaf that read as one file becomes
three at recon. Don't re-plan the wave around the straggler; the barrier is what a wave costs.

## Step 5. Integration — one merge agent per merge, sequential

- **Topology (M1).** Leaf branches merge back into the wave branch with `--no-ff` and **never squashed**, so a
  single leaf stays revertible as its own commits. **Leaves open no PRs** — the wave lands exactly one. This is a
  deliberate revision of `plan`'s "a leaf = one branch, one PR" for leaves run inside a wave.
- **Order:** a leaf others reference merges first, so the referencing text lands on final wording; otherwise
  smallest blast radius first. Merges are **sequential** — parallel merge agents race on one branch.
- **A throwaway merge agent per merge.** A clean merge costs the orchestrator nothing; a dirty one would drag the
  whole conflict into its context. Its pack: the two branch names, the absolute path, the leaf's file list, and
  the distillate, verbatim:

> Merge `<task/leaf>` into `<wave branch>` in the worktree at `<abs>`: `--no-ff`, never squash, never rebase,
> never push, never open a PR. Resolve only **mechanically trivial** textual conflicts — both sides appended to
> the same list, an import block, a changelog line — keeping both sides' intent, and report exactly what you
> resolved and how. **Abort (`git -C <abs> merge --abort`) and report** on any of: a conflict where the two sides
> mean different things; a conflict in the risk zone (auth/secrets, money, migrations & data deletion, PII,
> concurrency invariants, external API contracts); a conflict you'd have to understand the feature to settle. Do
> not run tests, do not fix code, do not touch files outside the conflict. Report: the merge commit, the files
> changed, every conflict and how it went.

- **A merge that stopped stops that leaf, not the wave's other merges.** Show the user both sides: a semantic
  conflict between leaves means the wave was cut wrong, and resolving it is a decision — an ordinary `task` on
  the wave branch, or back to `plan`. Resolving it silently hides a planning defect.
- **The verification split.** The merge agent merges and reports; **you** verify — against the **merged tree**,
  never the leaf branch (that tests text nobody has agreed to integrate): run the project's tests/scenarios
  yourself, then check the leaf's verbatim claims (a `git diff --stat`, a grep, a targeted diff). Trust doesn't
  remove verification, it makes it cheap.
- **Only then tick the leaf's PLAN checkbox. A checkbox never rests on an agent's claim** — `[[done-is-observed]]`
  at the wave's scale, and the reason verification is the one thing wave never delegates.
- A **risk-zone leaf** gets one more pass: a fresh subagent over just those spots (hand it that diff plus the
  leaf's criteria, not the whole context), as in `task`'s wrap.

## Step 6. Closing the wave

1. **A full run of the affected suite** against the wave branch head — per-leaf runs don't cover interactions.
2. **Line-anchored references.** A leaf's edit silently shifts every `file:line` pointer *into* that file —
   graph-node proofs, docs, cross-file references — and both the leaf and the merge are blind to it. Sweep the
   files the wave touched for inbound pointers; fix the drifted ones.
3. **The PLAN:** leaf checkboxes (ticked in step 5, on observation), the "Wave runs" row (merge order, per-leaf
   status, what stopped), and a Log paragraph — merge order, what the gate corrected, what stopped and why. A
   PLAN edit is a commit on the default branch, not a floating change (`plan`'s rule).
4. **Cleanup:** `git worktree remove` every leaf worktree, delete the merged leaf branches — no orphans.
5. **One PR for the wave**, by proposal (proposing is not creating). Body: the wave's goal, its leaves, how each
   was verified. `code-review` (Full) on it is **offered by default and mandatory when the wave carried a
   risk-zone leaf** — M1 makes one PR out of N leaves, which is exactly when review gets coarse.
6. **CRAFT.md, the graph, the glossary** — `task`'s global wrap rule, owned here: a leaf never sees the whole
   wave, so the durable decisions, invariants and gotchas that outlived it are the orchestrator's to record.
7. **Report and stop.** The next wave is a new `wave` invocation, opened by the user.

## Rules

- **One wave per run.** wave never rolls on into the next: waves exist to be a checkpoint, and an orchestrator
  that runs them back to back has removed the only place a human sees the initiative.
- **The gate is never weakened in the risk zone.** Batched ≠ waived: risk-zone specs by name, no advance ok,
  showing the specs ends the turn. `[[risk-zone-min-m]]` and `[[confirm-gate]]` hold at the wave's scale.
- **`plan` stays planner-only, and wave stays plan-free.** wave doesn't re-cut the DAG, add leaves, or nest a
  plan. Reality diverged from the plan → stop and hand back to `plan`.
- **wave writes no code.** Its own hands do four things: setup, the gate, verification, the close. Tempted to
  "just fix this one myself" → that's a leaf's spec or a separate `task`.
- **The pack is the prompt, never a path.** `[[context-pack-not-history]]` leaks through the filesystem too: a
  path into a shared folder hands over everything co-located with it.
- **File-disjoint is not semantically independent.** Disjointness buys clean textual merges and nothing else.

## Stop rules

- **An executor stopped** → don't respawn it on the same spec and don't finish its work yourself: report what it
  stopped on. Either the leaf leaves the wave (its own `task`), or its spec changes — and a changed spec goes
  through the gate again.
- **Two executors stopped for the same reason, or leaves collided in a merge** → the cut is wrong, not the
  execution: back to `plan` with what you saw.
- **A dependency isn't closed, or a leaf's spec no longer matches the PLAN** → don't start; say what diverged.
- **A compaction mid-wave** costs nothing *if* the PLAN and the leaf specs are current — so write state to disk
  at each stage boundary, not at the end.
- **You cannot verify a merge yourself** (no harness, a CI-only suite) → say so plainly and leave the checkbox
  unticked. An honestly unticked leaf is a legitimate outcome; a checkbox ticked on an agent's claim is not.
