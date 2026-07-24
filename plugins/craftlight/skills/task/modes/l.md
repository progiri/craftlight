# Mode L — phases, checkpoints, external memory

The spec format and all of M's discipline are preserved. The differences: the slicing into phases, context hygiene, and the delegation protocol.

## 1. Brief

As in M. The deltas: the spec cap rises to L's (the number and the cut-priority are in `templates/SPEC.md`) — L is the most capacious mode. The checklist is grouped into phases:

- A phase is a coherent result that ends with green tests and makes sense on its own.
- 2–5 phases. More than that — it's most likely several tasks: propose splitting it and going to the `plan` skill
  (it decomposes the initiative into a DAG of tasks and waves of parallel execution; each leaf returns here, to `task`).
  No real phases emerged — one coherent checklist, an M-scale file count → de-escalate L → M per the router's rule.
- Order by dependencies. Fix the interface contracts between phases explicitly in the spec (signatures, data formats, invariants): they're exactly what lets you do the next phase in a clean context.
- A phase whose recon already shows >~10 files → plan it for a subagent now, at the brief (the predictive trigger; the mid-flight tripwire is in step 2).

## 2. Phase execution

- By default — in the main context, with the same cycle as M: test → code → commit per item → checkbox. Risky experiments — in a git worktree, so they don't jostle the working tree.
- **Delegate a phase to a subagent** when the brief planned it so, or the tripwire fired: a compact happened inside a phase → finish the current phase in the main context, delegate the next big ones.
- The delegation protocol — the discipline doesn't evaporate at the boundary:
  - The subagent works in its own worktree `.worktrees/<phase>/` on a branch `task/<slug>--<phase>` cut from the task branch; commits per checklist item there; **it never touches SPEC.md**.
  - It returns a summary — items done, files touched, test status, deviations, foreign findings — not file dumps.
  - The main context integrates: merge the phase branch, re-run the phase's tests, tick the checkboxes, write the "Log" paragraph. The spec is committed only from the main context.
  - Pass a **context pack, not the history**: its checklist section + the file list + the interface contracts + the relevant constraints from the spec + the rule distillate below. No log, no other phases, no restating the project — reloading the full context by each executor is exactly the main token multiplier in heavy pipelines.
  - The rule distillate, copied verbatim into every subagent prompt:
    > Test-first for new behavior logic; a bugfix starts from a failing repro test; configs, texts, and cosmetics need no new tests. One atomic commit per checklist item, staged with an explicit `git add <files>`, never `-A`. Scope = your checklist section only — nothing "while we're at it"; foreign findings go into your summary, not into code. Report only the observed: didn't verify → say so; "should work" is forbidden. A fix hypothesis failed → stop: reproduce, read the error in full, form a new hypothesis, test it minimally; the second rejected hypothesis → stop and report back. The risk zone — auth/secrets, money, migrations & data deletion, PII, concurrency invariants, external API contracts — is not yours to enter: touched it → stop and report back.

## 3. Checkpoint after each phase

1. The phase's tests are green — otherwise the phase isn't closed.
2. A state paragraph into the spec's "Log": what was done, key decisions, what's next, known gotchas.
3. End the turn — the context reset is the user's action, not yours: close with "Phase N closed, tests green. Run /compact (or /clear for a full reset) and say 'continue the task'" and stop there. The next phase enters through the router's resume path; **SPEC.md is the external memory** — the phase starts from reading the spec and its own context pack, not from the chat history. One round-trip per phase is the design's price: it buys every following phase a clean context.

A side bonus: resuming after a day-or-two break is free — the router will find the in-progress spec and continue from the first unclosed item.

## 4. Wrap

As in M — the full block applies, including "a fix → re-run 1–2", the backlog `graph-candidate` sweep, and the PR by proposal. The L deltas:

- **Contract reconciliation:** go through every inter-phase contract like the criteria — line by line, where and by what it's honored. L breaks at the seams between phases, not inside them; M's block doesn't check the seams.
- **Cleanup:** `git worktree remove` the phase worktrees, delete the merged `task/<slug>--<phase>` branches — an L task doesn't leave `.worktrees/` behind.
- **The graph's L feed:** the phases' architectural decisions and the inter-phase contracts that outlived the task → nodes; don't drag one-off implementation details into the graph — only what's important to know before the next edit. (The mechanics — the `file:line` proof, CONTEXT.md, CRAFT pointers — are the router's rule.)

## Stop rules

- **A phase failed twice** — the checkpoint's condition 1 (green phase tests) wasn't met on two full attempts → don't hammer at it. Go back to the spec: most likely the slicing or a contract between phases is wrong. Re-slicing is a change to the approved plan → it passes the gate anew (the router's rule): show the updated spec, end the turn, wait for the ok.
- The plan has diverged from the code's reality → update the spec (it's a living document) and announce the change to the user in one line. A silent deviation from the spec is worse than an honest edit to the spec.
