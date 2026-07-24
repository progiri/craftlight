---
name: debug
description: Systematic hunt for a bug's root cause without fixing it — reproduce, read the error in full, hypotheses with testable predictions, minimal experiments, a log of what was rejected; the root, once found, goes back to task for the fix. Use this skill when the cause of a breakage is unknown and needs to be found — "figure out why it doesn't work", "why does it crash", "strange behavior", "I can't tell what's going on", "flaky bug", "only reproduces in prod", "debug this", "why is this failing", "investigate this bug", "find the root cause" — even without the word "debug". Also trigger on resume — "let's continue debugging", "back to the bug", "resume debugging". Also self-select here from task's no-guess-and-patch stop rule — two fix hypotheses rejected, or a second failed experiment. Not for a task with a known cause ("fix X, it's because of Y" — that's task), not for a code review (code-review), and not for "how does this work" (a normal answer). debug makes the diagnosis — the cure is in task.
---

# debug — the systematic root-cause hunt

Principle: **debug sits BELOW task** — a diagnostic subcycle that task drops into by the no-guess-and-patch stop
rule and returns from with a root cause. Observation over guessing: a hypothesis must yield a testable prediction
before the experiment, and every rejected option is recorded. Blind loops of "tweaked at random — reran" are the
main token-eater; a systematic pass is cheaper than three guesses.

**The boundary is fix-shaped, not edit-shaped.** debug doesn't write the fix and doesn't commit one — not even an
obvious one-liner; the root found → the fix goes through `task` (classification, the gate, a regression test).
But diagnostic edits are the skill's own tools and are allowed: temporary log lines, probe tests, a narrow
assertion. Two rules keep them honest: instrumentation is never committed and is stripped before the diagnosis is
handed off; the reproduction test from step 1 is the exception — it is left uncommitted and passed to `task` as
the ready-made regression test (task's fix begins red on it). The discipline's symmetry: plan plans and stops,
code-review reads and doesn't edit, debug diagnoses and doesn't fix.

Not for this skill: the cause is known, only the fix remains → `task`; "how does X work" → a normal answer;
assessing code quality → `code-review`. The cause became obvious from the very first error → don't unfold the
ceremony: return the diagnosis in one phrase and hand off to `task`.

## Step 0. Orientation and resume

The craftlight block upsert (reference and procedure — `skills/task/templates/CLAUDE-block.md`) rides with the
creation of `DEBUG.md` — the only file debug writes. A direct entry whose log stays in the chat touches the repo
not at all, so it must not edit the user's CLAUDE.md; an entry from task finds the block already ensured by task.

There's a `docs/crafts/*/DEBUG.md` with status `in-progress`:
- A bare resume trigger ("back to the bug", "resume debugging") → show the last hypothesis and current status
  from the log and offer to continue: DEBUG is external memory, resuming reads the log, not the chat history.
  Several in-progress DEBUGs → ask which one.
- A new bug in the message → take it on as usual; no blocking question — one FYI line: `parked: debug
  "<slug>" is in-progress — say "back to the bug" to resume it`.

## Two entries

- **From task** (the stop rule fired — two hypotheses rejected, or a second failed experiment): a repro often
  already exists (a red test); keep the log in the task spec's "Log" (M/L) or in the chat (S). Carry task's
  rejected attempts into the log as the first factual lines — so you don't retest them — but they don't count
  toward debug's own rejection tally: task rejected them before the prediction discipline, they're data, not
  protocol cycles. Entering, debug starts its count at zero. The DEBUG.md slug, if it comes to a file, is the
  task's folder — one craft's artifacts sit together.
- **Directly**: "figure out why X". There are no modes — debug is single-mode; the log lives in the chat under
  its own slug.

## Protocol

The order is mandatory — a skipped step is exactly guess-and-patch:

1. **Reproduce.** A minimal reliable repro before any edits. Doesn't reproduce → don't fix blindly: gather
   data (logs, traces, environment conditions) and narrow the conditions of occurrence. "Sometimes crashes"
   is not a repro. This repro, as a test, is the regression test task will inherit — write it to keep.
2. **Read the error in full.** The complete text, the stack trace to the end, the logs around the moment of
   failure. An error message is data, not noise: half of all roots are visible from a literal reading.
3. **Check the obvious.** The right branch, the right env, a fresh build, a clean cache, the right dependency
   versions — and recent history: "when did it break, what changed?" is 'obvious' too, and asking the user is
   one of the cheapest experiments there is. A minute on "is it plugged in" saves an hour of false hypotheses.
4. **One hypothesis at a time.** The formula: "if the cause is X, then under Y I'll see Z". No testable
   prediction → it's a guess, not a hypothesis — don't test it with an experiment.
5. **Minimal experiment.** The cheapest way to settle the prediction: a targeted log, a narrow probe test, a
   binary search (over commits — git bisect, over data, over code). One factor at a time: change two and you
   won't know which one worked. bisect needs a clean tree → stash the instrumentation first, and `git bisect
   reset` when done, so the repo doesn't end stranded in detached HEAD.
6. **Rejected → a line in the log, next.** Hypothesis, prediction, experiment, fact. The log keeps you from
   testing the same thing twice and makes the hunt resumable.
7. **Root, not symptom.** The symptom vanished after fixing an effect — the classic false success: ask "why"
   one level deeper. The floor is the territory rule: the root is the deepest level where the fix is still
   inside this repo; deeper than that is "someone else's" (a library, the OS, the scheduler), not your root.
   Confirmed by experiment → the diagnosis is ready.

## Output

The diagnosis: the root with a `file:line` proof, the breakage mechanism in one phrase, a minimal repro, the
direction of the fix (not a patch). Strip the instrumentation; keep the repro test uncommitted for task. Then
the return, by the entry:
- **Back to task (same session):** this is a return, not an invocation — the task context is alive, continue by
  its playbook. The diagnosis is an input to task's own classification: the root sits in the risk zone →
  minimum M however one-line the fix, the plan changed → the gate again.
- **Direct entry or a later resume:** one successor, the user's explicit choice — ask "fix it through task?"
  and invoke task in-session on a yes. The fix begins with the regression test, red on the root.

A durable root worth the project remembering (the s.md test — a one-off config typo doesn't qualify) → a
`graph-candidate` line in `docs/crafts/_backlog.md` (format — task's `templates/BACKLOG.md`), with the
`file:line` in the line. A node now would be half-empty: the resolution (how it was worked around or fixed)
only appears at the fix's wrap — task's wrap backlog-sweep promotes the breadcrumb into a node then. Something
unrelated noticed along the way (an off-topic bug, a stale doc) → a plain backlog line, don't chase it.

"Didn't find it" is a legitimate output when honest: what was gathered, what the log ruled out, the
next-cheapest step. After a change of angle, another 2–3 rejections → offer it explicitly rather than grind on
sunk cost; continuing is the user's call.

## Log and escalation to DEBUG.md

By default there's no file: the log lives in the chat or in the "Log" of the current task's spec. Move it to
`docs/crafts/<slug>/DEBUG.md` (per `templates/DEBUG.md`, external memory and resume like the specs) when the
case runs long — **≥2 rejected hypotheses** — or predictively, before the log can be lost: a compact just
happened → write DEBUG.md now; the user wraps up ("let's continue tomorrow") → offer to save it. A retrospective
"it outlived the session" detects the loss after it's happened; these catch it before.

## Stop rules

- **An experiment with side effects outside the local sandbox** (production data, an external service, a
  destructive or irreversible operation) → propose it, don't run it: describe the experiment and wait for an
  explicit ok. Read-only over code is not read-only over systems, and "only reproduces in prod" is a case this
  skill invites — the gate philosophy applies to experiments too.
- **3 rejected hypotheses in a row** → stop: not a fourth guess, but a change of angle — a fresh read-only
  subagent's look at the repro+log, a question to the user about history, git bisect from the last working state.
- **The repro is gone or flaky** → return to step 1: experiments without a stable repro mean nothing.
- **The root is in someone else's territory** (a library, infrastructure, an external service) → record the
  proof and stop: whether to work around it or fix upstream is the user's decision.
- **An observation contradicts expectation** → trust the observation. "That can't be" means the model in your
  head is wrong: update the model, don't discard the fact.
