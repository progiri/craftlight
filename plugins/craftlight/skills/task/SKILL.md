---
name: task
description: Entry point for any development task — feature, bugfix, refactor, integration, migration. Use this skill whenever the user sets a task to change code — "do it", "add", "fix", "correct", "rewrite", "refactor", "implement", "fix this", "add feature" — even without the words "task" or "skill". Also trigger on the flags --s/--m/--l and on a request to resume task work — "continue the task", "resume the work", "back to the task", "where did we stop". Not for "how does this work" questions, review without edits, or research — anything that changes no code.
---

# task — the mode router

Principle: ceremony proportional to the task. Start light by default, escalate on explicit triggers — not the other way around. The router only classifies: it asks no questions about the task's substance, writes no files, and spawns no subagents. Cheap recon is allowed — 1–2 Glob/Grep calls so the file estimate rests on the repository rather than a guess; don't read whole files and don't dig further "to be sure": underestimating is safe — escalation catches it mid-flight.

Not for this skill: a "how does this work" question, reviewing someone else's code, research — anything that doesn't change code. Realized there will be no code changes → leave the skill and answer as usual.

## Step 0. Orientation and resume

There's a `CRAFT.md` in the root → read it first: it's the project map and the starting point after CLAUDE.md (what the project is, entry points, modules, pointers into the `docs/graph/` graph). No file → don't create it at this step: bootstrapping the map happens after the gate (see "Global rule: CRAFT.md, the graph, and the glossary").

Resume interrupts classification only when there is nothing new to classify. A spec matching `docs/crafts/*/SPEC.md` with status `in-progress` and unchecked boxes:

- The message contains a new task statement → classify the new task as usual; no blocking question — just add one FYI line to the step 3 announce: `parked: "<slug>" is in-progress — say "continue the task" to get back to it`.
- A bare resume trigger ("continue the task", "where did we stop") or no task statement → show the first unchecked item and offer to continue. Agreement → open the playbook of the mode named in the spec and continue from that item. Several in-progress specs → ask which one.
- "Not now" ≠ "abandoned": the spec stays in place; mark status `abandoned` only on an explicit request.
- Deliberate gap: only M/L leave a spec, so only M/L resume — an interrupted S has no artifact to resume from.

A spec with status `draft` is an approval interrupted at the gate (the M/L brief was shown, the ok never arrived), not active work. A bare resume trigger → show it and ask: resume the approval or delete the draft. A new task in the message → classify the new one and fold the draft question into its gate message ("also parked: draft spec `<slug>` — resume its approval or delete?"). Either way: don't flip a draft to in-progress yourself (that's the confirmation gate) and don't delete it without an answer — no silent orphans.

## Step 1. Manual override

A `--s` / `--m` / `--l` flag from the user always beats classification: lock the mode and move to step 3.

## Step 2. Classification by observable signals

Don't estimate time — agents' time estimates are unreliable. Answer three questions, then check the risk zone:

| Signal | S | M | L |
|---|---|---|---|
| Files touched (by recon) | 1–2 | 3–10 | >10 |
| Acceptance criteria | unambiguous | open questions | architectural decisions needed |
| Reversibility | trivial rollback | care needed | migrations / irreversible data |

An open question is any decision you would have to make **for** the user. Closing one with a silent assumption doesn't make the criteria "unambiguous" — it hides an M-signal: "unambiguous" means the statement left you nothing to decide, not that you've decided everything yourself.

Reduction rules:
- The worst signal determines the mode (the max across the table's rows) — and only positively observed signals join the max; uncertainty resolves downward. "Unclear" after recon is M, not L; torn between two modes → take the lower. Escalation is cheap, excess ceremony is an unrecoverable spend of tokens.
- **Risk zone** (the canonical list below) → minimum M, even for a one-line change.
- Parallelizability of the chunks is a property of the execution strategy within L, not a size signal: on its own it does not raise the mode.
- Recon shows several independent deliverables — several unrelated PRs → this may be above L: offer the `plan` skill (it decomposes an initiative into a DAG of tasks); the choice is the user's, classification alone doesn't open an epic.

## Risk zone — the canonical list

The single anchor the playbooks, the gate, and the reduction rules point to; its always-in-context copy is the risk-zone line of the craftlight block in `CLAUDE.md` — non-task skills and subagent rule distillates cite that line. In the zone:

- auth, secrets, credentials;
- money;
- irreversible data: migrations, deletion, PII handling;
- concurrency: changes to synchronization primitives or shared-state invariants — merely touching async code is not the zone;
- breaking changes to externally consumed API contracts.

Consequences: minimum M, and the advance ok does not apply — the plan is shown and an explicit ok is awaited, always.

## Step 3. Announce and load the playbook

In one line, no reasoning: `Mode: M — ~5 files, 2 open questions on the criteria.` (Plus the parked-spec FYI line when step 0 produced one.) Then read the playbook and follow it:

- S → `modes/s.md`
- M → `modes/m.md` + the `templates/SPEC.md` template
- L → `modes/l.md` + the `templates/SPEC.md` template

## Global rule: the confirmation gate

In every mode, execution begins only after an explicit "ok" from the user on the shown plan: in S that's a restatement with the decision in one phrase, in M/L a spec draft. Mechanically: **showing the plan ends the turn** — the ok arrives as the user's next message. Writing "I'll wait for your ok" and proceeding in the same turn is the classic failure this rule exists against; silence or a missing answer ≠ ok. Raising the mode means the scope has exceeded the approved plan: show the updated (or after-the-fact) spec, end the turn, wait for the ok again.

Why a gate even on a one-liner: the S restatement is one phrase — the cheapest point in the whole system to catch a misread task; every later point costs rework, not a phrase.

Advance ok: the statement explicitly waives confirmation — "do it right away, without confirmation" or a direct equivalent. The equivalent must waive **confirmation itself**: urgency and brevity ("just do it", "quickly", "asap") are tone, not a waiver. With an advance ok, still show the plan — then continue in the same turn instead of ending it. In the risk zone the advance never applies (see the canonical list).

## Global rule: the CLAUDE.md block

task owns the craftlight block in the root `CLAUDE.md` (procedure and reference — `templates/CLAUDE-block.md`). The first step after the gate is passed, before touching product code: check the block — absent → insert, version differs → update, matches → leave alone; never change text outside the markers. One quiet Edit, not a separate "task". A call that never passes the gate must not edit the user's CLAUDE.md at all.

## Global rule: the branch

In every mode, before the first commit: you're on the default branch (main/master) → create `task/<slug>`; in M/L write it into the spec's "Branch" field. `task/<slug>` already exists and isn't this task's own → take `task/<slug>-2`, don't reuse a foreign branch. A task's commits don't go to the default branch — otherwise an S→M escalation leaves the wrap with no material for a PR.

## Global rule: tests

New behavior logic → first a failing test, see it red, then the code; a bugfix is new behavior — start from a failing repro test. Test behavior, not implementation. No theater: configs, texts, cosmetics, and refactoring under existing green tests don't require new tests. No test harness in the repo, or standing one up would outgrow the task → verify by observation instead and say so in the report; scaffolding a test framework is never a silent side quest.

## Global rule: verification honesty

"Done" = an observed result, not "the code is written": "works" is said only of what you saw yourself — a run, output, the screen. Behavior is visible to the user → run the scenario live (dev-server/CLI): green tests ≠ a working feature. In the report, only the observed: didn't verify → say so, "should work" is a forbidden phrasing — an honestly flagged gap is a legitimate outcome.

## Global rule: no guess-and-patch

The first attempt is deliberately cheap — no reproduction ritual up front: that's proportionality, a decision, not an oversight. But the first fix hypothesis didn't work → stop. Reproduce, read the error message in full, form a new hypothesis, test it with a minimal experiment, find the root cause. The handoff is a counter, not an adjective: the cheap first attempt aside, two rejected hypotheses or a second failed minimal experiment → the `debug` skill (it returns a diagnosed root; the fix comes back to the task).

## Global rule: CRAFT.md, the graph, and the glossary

`CRAFT.md` (the project map in the repo root) is the starting point after CLAUDE.md; task owns it. No file and mode M/L → right after the gate (alongside the block upsert), create a skeleton per `templates/CRAFT.md` (the "What it is" section — a dense description of the project — plus the map: entry points, modules, pointers into `docs/graph/`) and add a pointer line to CLAUDE.md, "read CRAFT.md first". At wrap: structure or entry points changed → update the map; the task uncovered a durable decision, invariant, or gotcha → add a node to `docs/graph/<slug>.md` per `skills/craft-graph/templates/NODE.md` (a `file:line` proof is mandatory, status `active`), link it from CRAFT.md and adjacent nodes, and append its `[[slug]] — area` to the overview's "Unplaced" queue rather than editing the Mermaid by hand (a craft-graph pass folds it in). A wrap that touched a file an existing node's proof points at → re-check that node and mark it `verify` if the proof drifted. A project term was born or settled in the task → a line "**term** — meaning" in the root `CONTEXT.md` (no file → create it per `templates/CONTEXT.md`; the selection criterion is in the template's header). Decisions go into the graph — CRAFT.md holds only pointers; nothing durable surfaced → write nothing: an empty node is worse than its absence. The node format, the status field, and the overview Mermaid are the `craft-graph` skill.

## Changing mode on the fly

Escalation applies in any mode, at any moment. If the actual signals have exceeded the mode — there turned out to be more files, ambiguity in the criteria surfaced, you touched the risk zone — stop, announce it in one line, and raise the mode:

- S → M: write `SPEC.md` after the fact for what's already done and continue per the M playbook.
- M → L: group the existing checklist into phases, change the mode in the spec to L.

The spec format is the same for M and L, so escalation is an append, not a restart of the process. Silently continuing in the old mode is not allowed: silent drift eats more in rework than any ceremony. Both transitions pass the confirmation gate anew: show the changed spec, end the turn, and wait for the ok before continuing (see the global rule).

There are two de-escalations, both at the brief — before execution starts. **M → S**: after the brief every open question is closed by the user's answers (not by your own assumptions — the detector in step 2 applies), ≤2 files are touched, **and** the risk zone isn't involved — announce it in one line; the spec draft is already on disk (see the M playbook), delete it so as not to leave an orphan draft. **L → M**: the L brief found no real phases — one coherent checklist, an M-scale file count — ungroup the phases, set the spec's mode to M (cap 80), continue per the M playbook; before the gate this is free, the draft simply changes. De-escalation never bypasses the rule "risk zone → minimum M".
