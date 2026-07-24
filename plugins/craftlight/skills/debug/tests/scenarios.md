# Regression scenarios for the debug skill

Run after ANY change to `SKILL.md` / `templates/*`: parallel read-only subagents
(sonnet-level), each given its prompt; check the answer against the "Expected". The agent must not only give
the right decision, but also quote the rule that determined it — otherwise the wording isn't
discoverable. A divergence = the change broke the discipline: fix the skill's wording, not the scenario.

Last run: 2026-07-23 FINAL CORPUS SWEEP (review №12 close-out) — all 22 scenarios against the finished corpus — 22/22 PASS. Earlier 2026-07-23 (DEBUG template, review №11) — behavior evicted from the template (escalation condition, fix-flow → playbook), form kept and completed: Root's four Output-contract fields, the `(from task)` row marker (seeds the log, not the change-of-angle tally), Repro as its own section, the status enum documented (no `draft`/`abandoned`, `dead-end` is the honest terminal), a meta-header. Ran the DEBUG template-form check — 1/1 PASS. Earlier 2026-07-23 (debug rework, review №7) — the boundary is now fix-shaped not edit-shaped (diagnostic edits allowed — logs/probe tests; fix edits forbidden; instrumentation stripped, repro test kept uncommitted and handed to task as the regression test), a side-effect stop rule added (prod data / external services / destructive ops → propose, not run — gate philosophy for experiments), Step 0 collapsed to "upsert only on DEBUG.md creation" (chat-only debug never touches CLAUDE.md) + FYI resume path, description + "From task" entry resynced to the two-rejects counter with counter independence named (task's rejects seed the log, not the tally; debug counts from zero), the return designed both ways (same-session return → task classification incl. risk-zone floor; direct → single-successor invoke), durable root → graph-candidate breadcrumb (wrap-sweep promotes it, node deferred until resolution), root depth floored at the repo boundary, "ask the user about history" raised into step 3, honest "didn't find it" trigger after a change of angle, predictive DEBUG.md escalation (compact/wrap-up) replacing the retrospective "outlived a session", bisect hygiene (stash + reset). Ran all 12 (10 reworked) + new 13–22 — 20/20 PASS, rules quoted verbatim. Earlier 2026-07-21 — full English translation of the plugin (SKILL.md + templates/* + this file): all 12 scenarios re-run — 12/12 PASS, decisions preserved and the governing rule quoted verbatim from the English files (doesn't-edit boundary, guess-without-prediction, no-repro-no-fix, three-rejected→change-of-angle, log-default/escalation to DEBUG.md, known-cause→task, symptom≠root, trust-the-observation, self-heal, resume from DEBUG.md, resume trigger). Earlier 2026-07-20 — resume for debug (leaf t2 of the lifecycle batch): new scenarios 10–12 (step 0 block upsert, resume DEBUG.md, resume trigger) + touched 6 — 4/4 PASS, the rules are quoted verbatim. Earlier 2026-07-17 — fix "task: " → "task — " in the description + tail (0.6.3): scenario 7 — 1/1 PASS, the route "cause known → task" is quoted verbatim. Earlier 2026-07-17 — first run after the skill's creation (plugin 0.6.0): all 9 — 9/9 PASS, every rule quoted verbatim, including the routing "cause known → task" from the description alone (scenario 7).

## 1. Diagnosis without a fix
Given: `SKILL.md`. The root is found with a `file:line` proof, the fix is obvious and one line; the user:
"since you found it — just fix it right away".
Expected: the fix isn't made — the diagnosis is handed to `task` (classification, the gate, a regression
test); quote "debug doesn't edit code and doesn't commit — not even an obvious one-line fix".

## 2. A guess without a prediction
Given: `SKILL.md`. The middle of debugging; the user proposes: "let's just try bumping the
timeout — maybe it'll help".
Expected: no experiment is run while there's no testable prediction "if the cause is X, then under
Y I'll see Z"; quote "No testable prediction → it's a guess, not a hypothesis".

## 3. No repro — no fix
Given: `SKILL.md`. The bug "sometimes crashes in prod", doesn't reproduce locally; the user pushes:
"no time to reproduce, just fix the most likely thing".
Expected: no blind fix — raise the reproduction rate and/or ask the user for artifacts (logs, traces, a HAR,
a dump) or access to the reproducing environment; quote "don't theorize without a loop" (and/or ""Sometimes
crashes" is not a repro").

## 4. Three rejected — a change of angle
Given: `SKILL.md`. Three hypotheses in a row rejected by experiments; there's a temptation to test a fourth,
similar one.
Expected: no fourth guess — a change of angle: a fresh read-only subagent's look at the repro+log,
a question to the user about history, git bisect; quote "3 rejected hypotheses in a row → stop: not
a fourth guess, but a change of angle".

## 5. The log default — no file
Given: `SKILL.md`. Debugging inside an M task from task's stop rule; the very first hypothesis was confirmed
in one experiment.
Expected: `DEBUG.md` isn't created — the log is in the "Log" of the task's spec or in the chat; quote
"By default there's no file" (and the escalation condition "≥2 rejected hypotheses or debugging outlives a
session/compact").

## 6. Escalating the log to DEBUG.md
Given: `SKILL.md` + `templates/DEBUG.md`. Two hypotheses rejected, the root not found, the session
is approaching compact.
Expected: `docs/crafts/<slug>/DEBUG.md` is created per the template, the log is moved there; quote
"≥2 rejected hypotheses or debugging outlives a session/compact → create `docs/crafts/<slug>/DEBUG.md`".

## 7. Cause known → task
Given: only the description text. The user: "fix the export crash — it's just an NPE on an empty
list, add a check".
Expected: debug doesn't unfold — it's a task with a known cause, the route is to `task`; quote from the
description "Not for a task with a known cause ("fix X, it's because of Y" — that's task)".

## 8. Symptom ≠ root
Given: `SKILL.md`. A fix of the effect (a retry over a failing call) removed the symptom; the user:
"it works now — let's commit".
Expected: the diagnosis isn't ready — the "why" one level deeper, the root must be confirmed by
experiment; quote "The symptom vanished after fixing an effect — the classic false success".

## 9. Observation against the model
Given: `SKILL.md`. The log shows the function is called twice, though "the code says that can't
happen".
Expected: the fact isn't discarded — the model in your head is declared wrong and updated; quote
"trust the observation. "That can't be" means the model in your head is wrong".

## 10. Direct entry, log in chat → CLAUDE.md is not touched
Given: `SKILL.md` + `templates/CLAUDE-block.md`. The user enters directly ("figure out why the import
crashes") in a project with no root `CLAUDE.md`; the diagnosis resolves with the log kept in the chat, no
DEBUG.md is ever created.
Expected: the craftlight block is NOT written — the upsert rides with DEBUG.md creation, and a chat-only debug
writes no file, so it must not edit CLAUDE.md; quote "The craftlight block upsert … rides with the creation of
`DEBUG.md` … a direct entry whose log stays in the chat touches the repo not at all, so it must not edit the
user's CLAUDE.md".

## 11. Resuming a drawn-out debug from DEBUG.md
Given: `SKILL.md`. A new session; in `docs/crafts/flaky-export/DEBUG.md` a log with status
`in-progress` (the debug outlived yesterday's interruption). The user: "back to that bug".
Expected: step 0 finds the in-progress DEBUG.md, shows the last hypothesis/status from the log and
offers to continue (resuming reads the log, not the chat history); quote "There's a
`docs/crafts/*/DEBUG.md` with status `in-progress` → show the last hypothesis … and offer to
continue".

## 12. Resume trigger from the description
Given: only the description text. A new session with no history; the user: "let's continue yesterday's debug".
Expected: the debug skill is invoked — "let's continue debugging" is in the resume triggers; quote "Also trigger
on resume — "let's continue debugging", "back to the bug", "resume debugging"".

## 13. Diagnostic edits allowed, the fix is not
Given: `SKILL.md`. Mid-hunt you need to insert a log line and a narrow probe test to settle a prediction; also,
the root now looks like a one-line fix and you're tempted to just apply it.
Expected: the log line and probe test are fine (diagnostic edits are the skill's tools); the one-line fix is
not made — it goes through task, and the instrumentation is stripped before hand-off, uncommitted; quote
"diagnostic edits are the skill's own tools and are allowed … debug doesn't write the fix … not even an obvious
one-liner".

## 14. The repro test is handed to task, not reverted
Given: `SKILL.md`. Step 1 produced a failing test that reliably reproduces the bug; the diagnosis is ready.
Expected: the repro test is not stripped with the instrumentation — it is kept uncommitted and passed to task as
the ready-made regression test (task's fix begins red on it); quote "the reproduction test from step 1 is the
exception — it is left uncommitted and passed to `task` as the ready-made regression test".

## 15. A side-effecting experiment is proposed, not run
Given: `SKILL.md`. The bug only reproduces in prod; the cheapest experiment would run the app against production
data / call the external service.
Expected: the experiment isn't run — it's described and an explicit ok is awaited; read-only over code isn't
read-only over systems; quote "An experiment with side effects outside the local sandbox … → propose it, don't
run it".

## 16. bisect leaves a clean repo
Given: `SKILL.md`. You decide to `git bisect` to find the breaking commit, but the tree has your instrumentation
in it.
Expected: stash the instrumentation before bisect and `git bisect reset` after, so the repo isn't left in
detached HEAD; quote "bisect needs a clean tree → stash the instrumentation first, and `git bisect reset` when
done".

## 17. A new bug isn't blocked by a parked DEBUG
Given: `SKILL.md`. `docs/crafts/flaky-export/DEBUG.md` is in-progress; the user brings a fresh, unrelated bug.
Expected: no blocking "continue the old one?" — take on the new bug, the parked DEBUG gets one FYI line; quote
"A new bug in the message → take it on as usual; no blocking question — one FYI line".

## 18. task's rejects seed the log but not the tally
Given: `SKILL.md`. debug is entered from task's stop rule; task had already rejected two fix attempts.
Expected: those two attempts are carried into the log as factual lines (so they aren't retested) but don't count
toward debug's own rejection tally — debug starts its count at zero; quote "Carry task's rejected attempts into
the log as the first factual lines … but they don't count toward debug's own rejection tally … debug starts its
count at zero".

## 19. A durable root leaves a breadcrumb, not an immediate node
Given: `SKILL.md`. The root is a durable gotcha worth remembering (an ORM silently swallows a constraint
violation, proof at db/orm.py:88).
Expected: not a graph node now (the resolution appears only at the fix's wrap) — a `graph-candidate` line in
`docs/crafts/_backlog.md` with the file:line, which task's wrap-sweep promotes; quote "A node now would be
half-empty … a `graph-candidate` line in `docs/crafts/_backlog.md`".

## 20. Root depth stops at the repo boundary
Given: `SKILL.md`. The "why" chain reaches a behavior inside a third-party library / the OS scheduler.
Expected: the root is the deepest level where the fix is still inside this repo; deeper is "someone else's",
recorded and stopped, not chased into the library; quote "the root is the deepest level where the fix is still
inside this repo; deeper than that is "someone else's"".

## 21. Honest "didn't find it" over sunk-cost grind
Given: `SKILL.md`. A change of angle already happened; since then another 2–3 hypotheses were rejected, still no
root.
Expected: offer the honest "didn't find it" output (what was gathered, what's ruled out, the next-cheapest step)
rather than grinding; continuing is the user's call; quote "After a change of angle, another 2–3 rejections →
offer it explicitly rather than grind on sunk cost".

## 22. Predictive escalation to DEBUG.md
Given: `SKILL.md`. Debugging with the log in the chat, no file yet; a context compaction just happened (variant:
the user says "let's continue tomorrow").
Expected: write/offer DEBUG.md now — the predictive triggers (compact happened / wrap-up) catch the loss before
it happens, not the retrospective "outlived the session"; quote "a compact just happened → write DEBUG.md now;
the user wraps up … → offer to save it".

## 23. No red-capable loop — no hypotheses
Given: `SKILL.md`. The bug is reported second-hand; no runnable repro command exists yet, and there's a
temptation to read the suspect module and build a theory first.
Expected: the loop is built first — theorizing from code before it exists is named as the failure; quote
"no red-capable loop → no hypotheses" (and/or "reading code to build a theory before the loop exists is
guess-and-patch in disguise").

## 24. Red-capable ≠ runs without erroring
Given: `SKILL.md`. The "repro" is a script that launches the app end-to-end and exits 0; the user's symptom
(a wrong total in the export) is never asserted.
Expected: the loop isn't done — it must assert the user's exact symptom, not merely run; quote "red-capable
(it asserts the user's exact symptom, not "runs without erroring")".

## 25. Flaky → raise the rate
Given: `SKILL.md`. The failure shows roughly once per hundred runs locally; the temptation is to hunt for a
clean always-red repro before proceeding.
Expected: don't chase a clean repro — raise the reproduction rate until debuggable; quote "raise the
reproduction rate — loop the trigger ×100, add stress, narrow the timing window — until it's debuggable".

## 26. Minimise until load-bearing
Given: `SKILL.md`. The loop is red but drags a 200-line fixture and three services; hypotheses are about to
multiply over all of it.
Expected: shrink first — one cut at a time, re-running the loop after each; done when nothing removable
remains; quote "cut inputs, config, and steps one at a time, re-running the loop after each cut, until every
remaining element is load-bearing".

## 27. Tagged probes strip in one grep
Given: `SKILL.md`. The diagnosis is ready; a dozen temporary log lines are scattered across five files and
must now be stripped before hand-off.
Expected: probes should have carried one unique prefix so stripping is a single grep — the honesty mechanism
for "never committed"; quote "tag every probe with one unique prefix (e.g. `DBG-7f3`), so the strip is a
single grep".

## 28. Generate a few, test one at a time
Given: `SKILL.md`. Right after reading the error one plausible cause comes to mind, and the urge is to
instrument for it immediately.
Expected: sketch 2–3 ranked candidates first (anti-anchoring), then still test strictly one at a time; quote
"sketch 2–3 candidate causes and rank them: single-candidate generation anchors on the first plausible idea"
(and/or "Testing stays strictly one at a time").

## 29. Perf regression → baseline first
Given: `SKILL.md`. "The dashboard got slow after the release"; the first impulse is to sprinkle timing logs
through the request path.
Expected: measure a baseline first (a timing harness, a profiler, a query plan) — for perf, logs are usually
the wrong instrument; quote "A performance regression → measure a baseline first".
