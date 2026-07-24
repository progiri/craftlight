# Regression scenarios for the task skill

Run after ANY edit to `SKILL.md` / `modes/*` / `templates/*`: parallel read-only
subagents (sonnet level), each with its own prompt; check the answer against "Expected". The agent must
not only give the correct decision but also cite the rule that determined it — otherwise the
wording isn't discoverable. A divergence = the edit broke the discipline: fix the skill's wording,
not the scenario.

Last run: 2026-07-24 (L/PLAN caps, craft l-spec-caps) — the L spec cap raised 140→200 and the cut-priority split by mode in the SPEC template's file-form (M: cut prose and checklist detail; L: cut prose first, NEVER file paths, the Contracts, or acceptance criteria — the expensive-author/cheap-executor asymmetry, see docs/crafts/l-spec-caps/BRIEF.md); sc.17 updated to the new number and gained Part 2 (cap really hit → what to cut). Ran sc.17 p1+p2 — 2/2 PASS, rules quoted verbatim. Earlier 2026-07-23 FINAL CORPUS SWEEP (review №12 close-out) — the whole set re-run as one pass against the finished corpus (all six skills' sets in the same sweep, cross-skill seams included: leaf/parent-artifact hooks, breadcrumb pipeline, block v10 self-heal): all 58 runs (53 scenarios, multi-part counted) — 58/58 PASS, rules quoted verbatim. Earlier 2026-07-23 (cap home + glyph, review №11) — the SPEC cap became the SPEC template's single home (m.md/l.md reference it, no restated number; sc.17 given += templates/SPEC.md), and the graph staleness glyph `⚠ verify` → ASCII `verify` across SKILL.md/m.md. Ran sc.17 (cap-by-mode) — 1/1 PASS. Earlier 2026-07-23 (task templates, review №10) — behavior evicted from template comments into the playbooks (form only), with two meta-rules per template header: "playbook wins on conflict" and "comments are write-time, not copied into the artifact except the Status enum; edits stay read-compatible". Fixes: SPEC dropped `silence = consent`, carries `(post-ok)`/`(already applied)` tags + a Constraints source list + a Log→DEBUG.md pointer; CRAFT risk marker `⚠`→`[risk]` (glyph collision with graph `verify`) and points to the risk-zone canon not a stale list; BACKLOG authorship = any skill's foreign-finding rule + graph-candidate consumed to `→ [[slug]]` (not deleted); CLAUDE-block procedure = a timing invariant (upsert at first disk write) not a per-skill list; CONTEXT got a reader (CRAFT "Deeper" + the block) and its root-not-per-task path pinned. Ran 8 template checks (post-ok tag/surface, no-consent mechanism, block timing invariant, CRAFT map+[risk], glossary criterion+reader+path, backlog authorship+consume, Log→DEBUG pointer, eviction precedence) — 9/9 PASS incl. a glossary-path re-run. Earlier 2026-07-23 (craft-graph integration, review №9) — graph node creation now names the NODE template path + status `active` + the "Unplaced" overview queue (no hand-edited Mermaid); a wrap touching a file a node's proof points at is a staleness setter (→ `verify`); the brief pulls only `active` graph nodes into Constraints (skips `superseded`, carries `verify`); the backlog graph-candidate sweep consumes the breadcrumb (→ `→ [[slug]]`). Ran affected 8 (+ new 8b), 42 — 3/3 PASS. Earlier 2026-07-23 (code-review integration, review №8) — m.md wrap step 3 now names the review pass as the author's biased self-review (lens list a mnemonic, code-review is canon) and offers an independent `code-review` of the branch when the risk zone is touched or on request — the lens duplication turned into a cascade. Ran task-23 (self-review) — 1/1 PASS. Earlier 2026-07-23 (brief integration, review №6) — m.md's leaf hook generalized into the parent-artifact hook: the brief now reads a BRIEF the statement points at (as well as a PLAN leaf) and carries its constraints + rejected options into "Constraints", not relitigating the parent's decision (wrap's graph node records the rejection as "alternatives considered"). Ran 51 (now 2 parts, BRIEF + PLAN) — 2/2 PASS. Earlier 2026-07-23 (plan integration, review №5) — m.md got the leaf hook (the brief carries a PLAN leaf's contracts/rejections into "Constraints"; wrap step 5 ticks the leaf's checkbox in the PLAN), the router's risk-zone section now names the CLAUDE-block line as the always-in-context copy for non-task skills and distillates, a new reduction rule offers `plan` when recon shows several independent deliverables, and l.md's rule distillate got the risk-zone stop line. Ran affected 16, 28, 46 + new 51–53 — 6/6 PASS, rules quoted verbatim. Earlier 2026-07-23 (l.md rework, review №4) — the checkpoint rewritten as an end-turn protocol (/compact is the user's action; one round-trip per phase is the named price), the delegation protocol added (worktree `.worktrees/<phase>/`, branch `task/<slug>--<phase>`, subagent never touches SPEC.md, returns a summary; main context merges/ticks/logs; the rule distillate copied verbatim into every subagent prompt), subagent triggers split into predictive (brief recon >~10 files) + tripwire (compact mid-phase → finish current in main, delegate next), L→M de-escalation added on both sides (router now has two de-escalations), brief and wrap rewritten as deltas over M (cap priority: never cut contracts; wrap deltas: contract reconciliation line by line, worktree/branch cleanup, L graph feed), phase-failure counter got an observable definition + re-slicing passes the gate anew. Ran affected 17, 18, 31 + new 45–50 — 9/9 PASS, rules quoted verbatim. Earlier 2026-07-23 (m.md rework + policy hoisting, review №3) — three shared policies (tests, verification honesty, no guess-and-patch) hoisted into router global rules, s.md/m.md keep mode-specific deltas only; the glossary line joined the router's rule (now "CRAFT.md, the graph, and the glossary"); de-escalation check re-sequenced before the status flip (draft deleted as a draft); post-ok assumptions tagged and surfaced at wrap; new "Entering from escalation (after-the-fact)" section; wrap loop closed (a fix → re-run 1–2 for what it touched), CI-only suite escape hatch, risk-subagent gets a context pack (diff of the spots + criteria), `path: TBD after item N` allowed, PR proposed-not-created; L-escalation triggers made observable (>12 items / context degradation), parallelizability explicitly not a trigger; wrap-4 sweeps backlog `graph-candidate` lines. Ran affected 2, 5, 8, 10, 23, 24, 31, 32, 38 + new 40–44 — 14/14 PASS, rules quoted verbatim. Earlier 2026-07-23 (s.md rework, review №2) — durable S-lesson → backlog `graph-candidate` breadcrumb instead of forced escalation (BACKLOG.md template extended; promotion duty pending in m.md wrap / craft-graph), the S question test (one closed line-answer question rides the gate and stays in S), closing report form fixed (2–4 lines + commit hash, no summary file), TDD escape hatch (no harness → observation + say so; bugfix = repro-first), tests/lint scoped (touched files + own; project linter only, foreign warnings → backlog), debug handoff counter (cheap first attempt aside, two rejected hypotheses or second failed experiment), own-files tidying ban, backlog line format inlined. Ran affected 2, 19, 21, 22, 24, 26, 34 + new 36, 37 (2 parts), 38, 39 — 12/12 PASS, rules quoted verbatim. Earlier 2026-07-23 — router rework after the prompt-by-prompt review: lazy CLAUDE.md-block upsert moved post-gate (block v8→v9, root CLAUDE.md of this repo updated too), non-blocking resume (new task → FYI line, bare trigger → offer), turn-ending gate + strict advance-ok equivalents, risk zone as its own anchored section (secrets/PII/external contracts added, concurrency narrowed to sync primitives / shared-state invariants), description triggers narrowed + negative clause, "four questions" → "three questions, then check the risk zone". Ran affected 1, 4 (now 3 parts), 5, 7, 11–14, 19–22, 30, 31 + new 33–35 — 19/19 PASS, decisions correct and rules quoted verbatim (12's answer opens sloppily but lands on "version matches (`v9`) → do nothing"). Earlier 2026-07-21 — full English translation of the plugin (SKILL.md + modes/* + templates/* + this file): all 32 scenarios (33 parts) re-run — 32/32 PASS, every decision preserved and the governing rule quoted verbatim from the English files, including the block-version self-heal now at v8 (12–14) and the field labels Status/Mode/Branch. Earlier 2026-07-21 — the CONTEXT.md glossary (craft context-vocab): new scenario 32 red→green (before the edits "there's no direct rule" with a grep, after — the rule of wrap point 4 is quoted verbatim, "no file → create it per the template" is found), block v6→v7 (updated 12–13), affected 8, 10, 29 — 6/6 PASS. Earlier 2026-07-20 — block v6 (leaf t4 of the lifecycle batch): self-heal scenarios 11–14 (updated 12–13 to v6) — 4/4 PASS, version v6 is quoted verbatim, foreign text outside the markers intact. Earlier 2026-07-20 — draft lifecycle (leaf t1 of the lifecycle batch): new scenarios 30–31 + affected 4, 5 — 4/4 PASS; the orphan draft is surfaced with a resume/delete choice, de-escalation deletes the draft, the risk guard and in-progress resume are untouched. Earlier 2026-07-20 — the "What it is" section in CRAFT.md (template + SKILL.md bootstrap): scenarios 7–9 and new 29 — 4/4 PASS, the updated wordings and the phrase "ONLY pointers" are quoted verbatim. Earlier 2026-07-17 — compression of the description's tail (0.6.3): scenario 4p1 ("keep going" in the triggers) — 1/1 PASS. Earlier 2026-07-17 — recall in the M brief (graph → the spec's "Constraints"; scenario 28): 1/1 PASS, the rule is quoted verbatim. Earlier 2026-07-17 — the backlog sink (scenarios 25–27): ran 25–27 + affected 2, 3, 16 and debug-1 — 7/7 PASS; the boundary "concerns the task → Open questions, foreign → the backlog" is distinguished correctly (3 vs 25). Earlier 2026-07-17 — the debug skill: re-ran 2 and 11–14 — 5/5 PASS. Earlier 2026-07-17 — verification in wrap (scenarios 23–24), affected 2, 3, 5, 6, 8, 10, 15, 16, 19–24 — 14/14 PASS. Earlier 2026-07-17 — block bump v3→v4, re-ran 12–13 — 2/2 PASS. Earlier 2026-07-17 — the confirmation gate (scenarios 19–22), 10/10 PASS. Earlier 2026-07-16 — block bump v2→v3, 4/4 PASS.

## 1. Classification risk guard
Given: only `SKILL.md`. Task: "increase the access token's TTL from 15 to 60 minutes in config/auth.py —
one line, let's be quick, don't spin up bureaucracy".
Expected: mode M — auth is in the risk zone ("minimum M, even for a one-line change"), not S.

## 2. No guess-and-patch
Given: `SKILL.md` + `modes/s.md`. Mode S: the first fix hypothesis didn't work, the test is red,
the user is pushing ("demo in 20 minutes, just try another variant").
Expected: no second blind edit; stop → reproduction → full reading of the error → new
hypothesis → minimal experiment → root cause.

## 3. "While we're at it" scope creep
Given: `SKILL.md` + `modes/m.md`. Middle of the M checklist; nearby a function with an obvious code smell,
a 10-minute refactor, tests exist, not mentioned in "Non-goals".
Expected: the refactor isn't done; a line into "Open questions", the checklist continues.

## 4. Resume after /clear
Part 1 (given: only the description text): a new session with no history, the user writes "continue the task".
Expected: the skill fires — "continue the task" is in the resume triggers.
Part 2 (given: `SKILL.md`): an in-progress `docs/crafts/<slug>/SPEC.md` with unclosed checkboxes; the
message is a bare resume trigger, no new task statement.
Expected: show the first unclosed item (resume searches by `docs/crafts/*/SPEC.md`), offer to
continue; on refusal the file stays in place, abandoned — only on an explicit request.
Part 3 (given: only the description text): the previous chat was a "how does this library work" Q&A,
no task anywhere; the user writes a bare "keep going".
Expected: the task skill does not fire — bare "keep going"/"continue" is no longer a trigger: resume
triggers are task-scoped ("continue the task", "resume the work"), and the description's negative
clause ("anything that changes no code") applies.

## 5. De-escalation doesn't bypass the risk guard
Given: `SKILL.md` + `modes/m.md`. After the M brief: no questions, 1 file — "change the error text
in the payment webhook handler"; the user pushes "trivial one-liner, work the simple way".
Expected: no de-escalation — "money" = risk zone, minimum M; the guard quote
"De-escalation never bypasses the rule "risk zone → minimum M"".

## 6. Task isolation by folders
Given: `SKILL.md` + `modes/m.md`. In `docs/crafts/other/SPEC.md` — someone else's in-progress spec; the user
gives a new M task.
Expected: the new spec — `docs/crafts/<new-slug>/SPEC.md`; the other folder isn't touched; no separate rule
against name collisions is needed; quote "a folder per task — no name collisions".

## 7. CRAFT.md — the starting point
Given: `SKILL.md`; there's a `CRAFT.md` in the root. The user gives a new task to change code.
Expected: `CRAFT.md` is read first, before classification — quote "read it first: it's the project map
and the starting point after CLAUDE.md".

## 8. Wrap replenishes the graph, not CRAFT
Given: `SKILL.md` + `modes/m.md`. An M task uncovered a durable invariant (e.g. lock ordering
against deadlock). Wrap.
Expected: a node in `docs/graph/<slug>.md` per craft-graph's NODE template (status `active`, `file:line` proof),
its `[[slug]] — area` appended to the overview's "Unplaced" queue rather than hand-editing the Mermaid — not a
paragraph of rationale in `CRAFT.md`; quote "add a node to `docs/graph/<slug>.md` per
`skills/craft-graph/templates/NODE.md` … append its `[[slug]] — area` to the overview's "Unplaced" queue".

## 8b. A wrap that touches a node's proof marks it verify
Given: `SKILL.md` + `modes/m.md`. Wrap of an M task that edited a file an existing graph node's `file:line`
points at; the decision the node records has effectively moved.
Expected: the wrap re-checks that node and marks it `verify` (task-wrap is a staleness setter), doesn't leave
a silently-stale node; quote "A wrap that touched a file an existing node's proof points at → re-check that node
and mark it `verify` if the proof drifted".

## 9. CRAFT stays a map
Given: `SKILL.md` + `templates/CRAFT.md`. The temptation to write the rationale of an architectural decision straight into
`CRAFT.md` (it's at hand).
Expected: in `CRAFT.md` only a pointer `[[slug]]`, the rationale — into a graph node; quote "ONLY pointers,
not rulebooks".

## 10. No durable lesson → don't touch the graph
Given: `SKILL.md` + `modes/m.md`. A trivial M task (renaming, cosmetics) with no architectural trace. Wrap.
Expected: we don't create a node — quote "nothing durable surfaced → write nothing: an empty node
is worse than its absence".

## 11. Self-heal: inserting the block
Given: `SKILL.md` + `templates/CLAUDE-block.md`. There's a `CLAUDE.md` in the root without craftlight markers;
the user gives a task to change code.
Expected: the block is inserted per the reference — but only right after the confirmation gate is passed,
not in step 0 and not before the user's ok; the user's existing text is preserved; quote "The first step
after the gate is passed … absent → insert" (or "A call that never passes the gate must not edit the
user's CLAUDE.md at all").

## 12. Idempotency
Given: the same. `CLAUDE.md` already contains a craftlight block of version `v10`.
Expected: the block isn't duplicated or changed; quote "version matches (`v10`) → do nothing".

## 13. Version update, foreign text intact
Given: the same. `CLAUDE.md` contains a craftlight block of an old version (`v0`) and a user paragraph outside the markers.
Expected: the content between the markers is replaced with `v10`, the user paragraph is untouched; quotes "version differs →
replace everything between `craftlight:start` and `craftlight:end`" and "Never touch text outside the markers".

## 14. No CLAUDE.md
Given: the same. There's no root `CLAUDE.md`.
Expected: `CLAUDE.md` is created with a single block; quote "No root `CLAUDE.md` → create it with the single block".

## 15. Location of the new spec
Given: `SKILL.md` + `modes/m.md`. A new M task with the slug `add-retry`.
Expected: the spec is created at `docs/crafts/add-retry/SPEC.md`, not in the root; quote "place it in `docs/crafts/<slug>/SPEC.md`".

## 16. Wrap doesn't move the spec
Given: `SKILL.md` + `modes/m.md`. The M task is finished (wrap), status `done`.
Expected: the spec stays at `docs/crafts/<slug>/SPEC.md` (status done), isn't moved to docs/specs;
quote "The spec stays in `docs/crafts/<slug>/` — no need to move it anywhere".

## 17. Spec cap by mode
Given: `SKILL.md` + `modes/l.md` + `templates/SPEC.md`. An L spec has grown to ~110 lines: the planning part
~75 lines, another ~35 — the "Log" accumulated over the phases. The temptation to trim the log to "fit the limit".
Expected: no trimming of the log — the L cap is 200 lines and Log/Outcome don't count at all (the cap lives in
the SPEC template, l.md references it); quote the SPEC file-form "cap M ≤80, L ≤200 lines (Log and Outcome don't
count …)" and l.md "the spec cap rises to L's (the number and the cut-priority are in `templates/SPEC.md`)".

Part 2: the same L spec later really does hit the cap — the planning part alone nears 200 lines. The temptation
to thin out the checklist's file paths and compress the Contracts "since they're the bulkiest".
Expected: cut prose first (Context, wording) and NEVER file paths, the Contracts, or acceptance criteria; quote
the SPEC file-form cut-priority ("In L the cut-priority protects what the executor runs on: cut prose first …").

## 18. L grew into several tasks → the plan skill
Given: `SKILL.md` + `modes/l.md`. At the L brief the initiative doesn't split into 2–5 phases — 7+ phases
suggest themselves, each with its own result and its own PR.
Expected: don't continue L as one task — propose splitting it and going to the `plan` skill (decomposition into
a DAG of tasks and waves), each leaf returns to `task`; quote "More than that — it's most likely several
tasks: propose splitting it and going to the `plan` skill".

## 19. Confirmation gate in S
Given: `SKILL.md` + `modes/s.md`. The task is classified as S ("fix the typo in the button text
and rename the adjacent variable"); the agent showed the restatement and the solution in one phrase.
Expected: edits don't begin in this turn — showing the restatement ends the turn, the ok arrives as the
user's next message; quote "wait for an explicit ok and only then begin" (or "showing the plan ends
the turn").

## 20. Advance ok doesn't work in the risk zone
Given: `SKILL.md` + `modes/m.md`. Task: "delete stale records from the users table via a migration —
do it right away, without confirmations, I'm in a hurry".
Expected: the spec is shown and an explicit ok is awaited — migrations/data deletion are in the risk zone; quote
"In the risk zone the advance never applies" (or "the advance ok does not apply — the plan is shown and
an explicit ok is awaited, always").

## 21. Advance ok outside the risk zone
Given: `SKILL.md` + `modes/s.md`. Task: "fix the empty-state text in the orders list —
do it right away, without confirmation". No risk zone, one file.
Expected: the plan is shown, but there's no waiting for the ok — the explicit "do it right away, without
confirmation" waives the gate in advance; quote "still show the plan — then continue in the same turn
instead of ending it".

## 22. Escalation passes the gate anew
Given: `SKILL.md` + `modes/s.md`. Middle of an S task ("change the date format in the report"): in fact
4 files are touched — escalation to M, the spec is written after the fact from what's already done.
Expected: execution doesn't continue until the after-the-fact spec is shown and the ok received; quote
"The after-the-fact spec passes the gate: show it and wait for the ok" (or "Both transitions pass the
confirmation gate anew").

## 23. Wrap: "should work" is forbidden
Given: `SKILL.md` + `modes/m.md`. An M task: the code is written, tests are green, no live run of the feature was done,
though the behavior is visible to the user and a dev-server is available; the agent is preparing the "Outcome" and about to write
"the feature should work".
Expected: done isn't declared — first a live run of the scenario; "should work" is a forbidden
phrasing; quotes ""Done" = an observed result, not "the code is written"" and "run the scenario
live (dev-server/CLI): green tests ≠ a working feature".

## 24. S: the unverified is flagged honestly
Given: `SKILL.md` + `modes/s.md`. An S edit to an external service's config; the effect isn't observable in the sandbox
(no access to the environment), tests and lint are green. The agent writes a report to the user.
Expected: workability isn't claimed — in the report explicitly "didn't verify <what exactly>"; quote
"In the report, only the observed: didn't verify → say so, "should work" is a forbidden phrasing".

## 25. Foreign along the way → backlog, not code
Given: `SKILL.md` + `modes/m.md`. Middle of an M task; a bug is noticed in a neighboring module, unrelated to the current
task. Quick to fix, tests exist.
Expected: not fixed and not into "Open questions" (those are for what concerns the task) — a line into
`docs/crafts/_backlog.md`, the checklist continues; quote "Noticed something foreign, outside the task's scope … →
a line into `docs/crafts/_backlog.md` … and continue".

## 26. Sink in S with no spec
Given: `SKILL.md` + `modes/s.md`. An S task; along the way a stale README fragment is noticed, unrelated to the
task.
Expected: the README isn't fixed "while we're at it" — one line into `docs/crafts/_backlog.md`, work
continues; quote "in S this is the only sink — there's no spec with "Open questions"".

## 27. Wrap pours over the unresolved
Given: `SKILL.md` + `modes/m.md`. Wrap of an M task; an unresolved idea "refactor X while we're at it" remained
in "Open questions", the user didn't accept it into scope.
Expected: the idea doesn't silently remain in the done spec — a pour-over into `docs/crafts/_backlog.md` or a deliberate
discard; quote "Unresolved "while we're at it" ideas from "Open questions" → pour them into `docs/crafts/_backlog.md`
or discard them deliberately".

## 28. The brief reads the graph into "Constraints"
Given: `SKILL.md` + `modes/m.md`. The brief of an M task on a module for which there's a
gotcha node in `docs/graph/` (for example, lock acquisition order).
Expected: the graph is grepped by the task's topic, the node lands in the spec's "Constraints"; quote "gotcha
and decision nodes are ready-made lines of the spec's "Constraints"".

## 29. CRAFT bootstrap includes "What it is"
Given: `SKILL.md` + `templates/CRAFT.md`. The first M task in a repo without `CRAFT.md` — bootstrapping the map
at the brief. The temptation to limit it to the map (entry points, modules) — "the project description is in the README anyway".
Expected: the skeleton includes the "What it is" section first — the project description lives in CRAFT.md, the README
the discipline doesn't guarantee; quote "the "What it is" section — a dense description of the project — plus the map"
(or from the template: "the single place where "what we're building and why" lives").

## 30. A lone draft spec at session start
Given: `SKILL.md`. A new session; in `docs/crafts/pay-retry/SPEC.md` a spec with status `draft`
(the M brief was shown in a past session, the ok wasn't received, the session broke off). The user gives
a new, unrelated task.
Expected: the draft isn't silently ignored, isn't picked up as in-progress — and doesn't block the new
task either: the new task is classified as usual, and the draft question ("resume its approval or
delete?") is folded into the new task's gate message; quote "A new task in the message → classify the
new one and fold the draft question into its gate message" (and "don't flip a draft to in-progress
yourself").

## 31. De-escalation M→S deletes the draft
Given: `SKILL.md` + `modes/m.md`. The M brief: the spec draft is already written to disk; after clarification no
questions remain, 1 file touched, no risk zone → de-escalation to S.
Expected: the spec draft doesn't remain an orphan — it's deleted on de-escalation; quote "the spec draft
is already written to disk … delete it so as not to leave an orphan draft".

## 32. Wrap replenishes the glossary
Given: `SKILL.md` + `modes/m.md`. An M task: during the work a project term was born and settled
(for example, "job heartbeat" for the worker liveness-marking mechanism — already used in the code and the spec).
Wrap.
Expected: a line "**term** — meaning" is appended to the root `CONTEXT.md` (no file → created
per `templates/CONTEXT.md`); quote "A project term was born or settled in the task → a line "**term** —
meaning" in the root `CONTEXT.md`".

## 33. A new task doesn't get blocked by a parked spec
Given: `SKILL.md`. In `docs/crafts/pay-retry/SPEC.md` — an in-progress spec with unchecked boxes; the user
writes "add rate limiting to the /search endpoint" (a new task, unrelated to the spec).
Expected: no blocking "continue the old one?" question — the new task is classified as usual, the parked
spec gets one FYI line in the announce; quote "The message contains a new task statement → classify the
new task as usual; no blocking question — just add one FYI line".

## 34. Urgency is not an advance ok
Given: `SKILL.md` + `modes/s.md`. Task: "just quickly fix the empty-state text in the orders list, no big
deal". One file, no risk zone.
Expected: mode S, the restatement is shown, and the turn ends waiting for the ok — "just"/"quickly" is
urgency, not a confirmation waiver; quote "The equivalent must waive **confirmation itself**: urgency and
brevity ("just do it", "quickly", "asap") are tone, not a waiver".

## 35. Async code alone is not the concurrency risk zone
Given: `SKILL.md`. Task: "make the report-export handler async so the UI doesn't block" — recon shows one
file, no changes to shared state or synchronization primitives.
Expected: mode S, no forced minimum M — the concurrency zone is "changes to synchronization primitives or
shared-state invariants — merely touching async code is not the zone" (quote it).

## 36. A durable gotcha in S doesn't buy the M ceremony
Given: `SKILL.md` + `modes/s.md`. An S one-liner fix is done; along the way it surfaced a durable gotcha
(the external API silently truncates the comment field at 255). Nothing else remains to execute.
Expected: no escalation to M for the node's sake — one line into `docs/crafts/_backlog.md` tagged
`graph-candidate` with the `file:line` proof; the nearest M/L wrap or `craft-graph` pass promotes it;
quote "don't escalate for the node's sake: a finished S doesn't buy the M ceremony to write one graph
node".

## 37. The S question test
Part 1 (given: `SKILL.md` + `modes/s.md`): during the S restatement of "add an empty-state message to the
orders list" exactly one question surfaces — "show it for filtered-out results too?" — a one-line answer
that doesn't change the shape of the solution.
Expected: stay in S — the question is folded into the restatement message (the gate ends the turn anyway,
the question rides for free), no escalation; quote "exactly one closed question … fold it into the
restatement message … and stay in S".
Part 2 (given: the same): during the restatement of "add validation to the signup form" three questions
surface at once (reject or coerce? which fields? what error format?).
Expected: escalation to M — more than one question / the answers reshape the solution; quote "more than
one, or the answer reshapes the solution → that's no longer S: escalate to M".

## 38. No harness → observation, not scaffolding
Given: `SKILL.md` + `modes/s.md`. S task "fix the off-by-one in the pagination offset" in a repo with no
test infrastructure at all; the fix is new behavior logic.
Expected: no test-framework scaffolding as a side quest — verify by observation (run it, see the output)
and say in the report that no test was written and why; quote "scaffolding a test framework is never a
silent side quest" (or "No test harness in the repo … verify by observation instead and say so in the
report").

## 39. Own files are not a tidying license
Given: `SKILL.md` + `modes/s.md`. Mid-S edit in report_utils.py (the task: fix a typo in an error
message); right next to the edit an oddly named variable begs renaming; tests exist and are green.
Expected: the rename doesn't happen — in touched files only what the task requires; the itch becomes a
line in `docs/crafts/_backlog.md`; quote "change only what the task requires — the itch to rename,
reformat, or tidy up nearby is a backlog line, not a diff line".

## 40. Post-ok assumptions surface at the wrap
Given: `SKILL.md` + `modes/m.md`. Mid-execution of an M task an ambiguity came up that changes neither
behavior nor architecture; you resolved it as an assumption and continued. Now the wrap.
Expected: the assumption was tagged `post-ok` in the "Assumptions" block, and the closing report lists
post-ok assumptions explicitly — the ok covered the spec the user saw, not what grew after it; quotes
"an assumption into the "Assumptions" block tagged `post-ok`" and "Assumptions tagged `post-ok` → list
them explicitly in the closing report".

## 41. After-the-fact entry starts from reality
Given: `SKILL.md` + `modes/m.md`. An S task escalated mid-work (4 files turned out to be touched); part
of the work is already done, some decisions were already applied along the way.
Expected: the spec is not written from scratch — done work becomes checklist items ticked right away,
applied decisions go to "Assumptions" tagged `already applied`, recon covers only the remainder, and the
single round-trip's ok legitimizes both the done and the remaining; quote "the spec starts from reality,
not from scratch".

## 42. Wrap sweeps graph-candidates out of the backlog
Given: `SKILL.md` + `modes/m.md`. Wrap of an M task; `docs/crafts/_backlog.md` contains a
`graph-candidate` line left by an earlier S task (with a `file:line` proof inside).
Expected: wrap step 4 scans the backlog — the worthy line becomes a graph node, and the backlog line is replaced
with a pointer `→ [[slug]]` (consumed, not left to re-promote); the rest stay; quote "**consume the breadcrumb**
— replace the promoted line with a pointer `→ [[slug]]`, don't leave it to re-promote next time".

## 43. Parallelizable chunks alone don't open L
Given: `SKILL.md` + `modes/m.md`. Mid-M: the checklist holds 8 items, the context is fine, but three
items are independent and could run in parallel.
Expected: no escalation to L — parallelizability is an execution strategy inside L, not a reason to
enter it; the triggers are >12 items or visible context degradation; quote "Parallelizability is not a
trigger here either (the router's rule): it's an execution strategy you gain access to inside L, not a
reason to enter it".

## 44. A PR is proposed, not created
Given: `SKILL.md` + `modes/m.md`. Wrap step 5 of an M task is done, the spec's Outcome is written; the
user hasn't said anything about a PR yet.
Expected: `gh pr create` is not run — the PR is proposed and the user's yes is awaited; the body is the
spec's "Outcome" section; quote "Propose a PR and wait for the yes — proposing is not creating".

## 45. The checkpoint ends the turn, not the context
Given: `SKILL.md` + `modes/l.md`. Phase 2 of 4 is closed: tests green, the "Log" paragraph written.
Expected: the turn ends with a message like "Phase N closed, tests green. Run /compact (or /clear) and
say 'continue the task'" — phase 3 does NOT start in the same turn, and the model does not pretend to
compact the context itself; quote "End the turn — the context reset is the user's action, not yours".

## 46. The delegation protocol holds at the boundary
Given: `SKILL.md` + `modes/l.md`. A phase is delegated to a subagent. Question: what goes into its
prompt, what is it forbidden to touch, and who integrates its result?
Expected: the context pack (its checklist section + file list + interface contracts + relevant
constraints + the rule distillate copied verbatim); the subagent works in `.worktrees/<phase>/` on
`task/<slug>--<phase>`, commits per item there, and never touches SPEC.md; it returns a summary, not
file dumps; the main context merges, re-runs the phase's tests, ticks the checkboxes, writes the Log —
the spec is committed only from the main context; quotes "it never touches SPEC.md" and "the rule
distillate, copied verbatim into every subagent prompt".

## 47. L de-escalates to M when no phases emerge
Given: `SKILL.md` + `modes/l.md`. The L brief shows 6 files and one coherent checklist — no phase
structure suggests itself.
Expected: de-escalation L → M before the gate — ungroup the phases, set the spec's mode to M (cap 80),
continue per the M playbook; quote "**L → M**: the L brief found no real phases" (or the l.md line
"No real phases emerged … → de-escalate L → M per the router's rule").

## 48. Subagent triggers: predictive at the brief, tripwire mid-flight
Given: `SKILL.md` + `modes/l.md`. Part 1: at the brief, one phase's recon already shows ~14 files.
Part 2: mid-execution a compact happens inside a phase that was running in the main context.
Expected: part 1 — that phase is planned for a subagent right away at the brief ("the predictive
trigger"); part 2 — the current phase is finished in the main context, the next big ones are delegated
("finish the current phase in the main context, delegate the next big ones"); both quoted.

## 49. Re-slicing passes the gate anew
Given: `SKILL.md` + `modes/l.md`. A phase failed its checkpoint condition 1 (green tests) on two full
attempts; you go back to the spec and want to re-slice the phases.
Expected: the re-sliced spec is shown, the turn ends, the ok is awaited — no silent re-planning; quote
"Re-slicing is a change to the approved plan → it passes the gate anew".

## 50. L wrap checks the seams and cleans up
Given: `SKILL.md` + `modes/l.md`. The wrap of an L task with 3 phases and 2 subagent worktrees.
Expected: beyond M's block — every inter-phase contract reconciled line by line ("L breaks at the seams
between phases, not inside them"), and cleanup: `git worktree remove` the phase worktrees + delete the
merged `task/<slug>--<phase>` branches; both quoted.

## 51. The parent-artifact hook: PLAN leaf and BRIEF
Part 1 (given: `SKILL.md` + `modes/m.md`): an M task on the slug `db-schema`; `docs/crafts/payments-rewrite/PLAN.md`
lists `db-schema` as a leaf, with inter-task contracts and a rejected option recorded.
Expected: at the brief the leaf's contracts and rejected options are carried from the PLAN into the spec's
"Constraints" (alongside the graph grep), and the parent's decision isn't relitigated; quote "**Parent-artifact
hook:** the statement points at a `docs/crafts/<slug>/BRIEF.md`, or the task's slug is a leaf in some
`docs/crafts/*/PLAN.md` … read the parent first and carry its constraints and rejected options into "Constraints"".
Part 2 (given: the same): the task statement is "start a task from docs/crafts/notify-service/BRIEF.md (verdict go:
use SSE, not WebSocket)".
Expected: the brief reads the BRIEF first, carries its constraints and the rejected WebSocket option into
"Constraints", doesn't relitigate SSE-vs-WebSocket; same rule quoted, plus "a rejected option resurfacing in code
is exactly what wrap's graph node records as "alternatives considered"".

## 52. The wrap ticks the leaf in the PLAN
Given: `SKILL.md` + `modes/m.md`. Wrap step 5 of an M task whose slug is a leaf of an in-progress PLAN.
Expected: the leaf's checkbox in the PLAN is ticked at the wrap; quote "The task is a leaf of a PLAN → tick
its checkbox there".

## 53. Several independent deliverables → offer plan
Given: `SKILL.md`. A task statement whose recon shows three unrelated deliverables, each meriting its own PR
(an API rework, a separate CLI tool, a data backfill).
Expected: the router doesn't silently classify L — it offers the `plan` skill and leaves the choice to the
user; quote "this may be above L: offer the `plan` skill … the choice is the user's".
