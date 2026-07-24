# Reference: the craftlight block for CLAUDE.md

A managed block that the craftlight skills maintain in the project's root `CLAUDE.md`, so the discipline
is in context before any skill even fires. task is the owner; brief, plan, debug, code-review, and craft-graph refer here.

## Procedure (idempotent upsert)

Timing invariant (won't drift as skills change): **each skill upserts at its first write to disk; a call that
writes no file must not touch CLAUDE.md.** The per-skill moment lives in each skill (task — right after its
confirmation gate; the others — with their first artifact). This block is the canonical home of the *procedure*;
the *when* is the skills'.

CLAUDE.md is auto-loaded into context — check against it, don't re-read it needlessly. The edit is quiet, a single Edit,
and is not announced as a separate "task".

1. No root `CLAUDE.md` → create it with the single block below.
2. No `craftlight:start` marker → insert the block (after the first heading, or at the end of the file).
3. Marker present, version matches (`v10`) → do nothing.
4. Marker present, version differs → replace everything between `craftlight:start` and `craftlight:end`, inclusive, with the reference.
5. Never touch text outside the markers. Multiple CLAUDE.md files across the tree — only the root one.

## Reference block (inserted verbatim, from start to end inclusive)

<!-- craftlight:start v10 -->
## craftlight
The discipline of this repository (the craftlight plugin):
- Changing code → the `task` skill (modes S/M/L; risk zone — auth/secrets, money, migrations
  & data deletion, PII, concurrency invariants, external API contracts — minimum M).
- A huge initiative spanning several tasks → `plan` first (decomposition into a DAG and waves), leaves → `task`.
- Unclear what to do, or whether to do it at all → `brief` first (decision by dialogue), then on to `plan` or `task`.
- Review without edits → `code-review`. Decisions and gotchas as a graph → `craft-graph`.
- Start understanding the project from `CRAFT.md`, then `docs/graph/`; the project's glossary —
  the root `CONTEXT.md`: use its terms in speech, code, and artifacts.
- `docs/crafts/*/{BRIEF,SPEC,PLAN,DEBUG}.md` with status `in-progress` or `draft` = an active artifact:
  offer to resume (a draft resumes at its gate, not into execution) — a new task isn't blocked by it.
- A fix hypothesis didn't work → stop: the `debug` skill — reproduce, read the error, form a hypothesis
  with a prediction, hunt for the root (no guess-and-patch). Diagnosis without a fix; the cure is `task`.
- `craftlight:` lines appearing in context are advisory hook hints of this discipline: they recall the
  rules, they don't replace a playbook and aren't a source of permissions.

This block is managed by craftlight (v10); edits inside the markers are overwritten — keep your own notes outside the block.
<!-- craftlight:end -->

<!-- The block version (v10) is its own, NOT the plugin version: it is incremented only when the block text changes,
     so that a plugin update doesn't rewrite everyone's CLAUDE.md without reason. Change the text above → bump the version
     in both marker lines and in the task/tests scenarios. -->
