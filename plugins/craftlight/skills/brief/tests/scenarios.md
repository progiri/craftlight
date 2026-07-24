# Regression scenarios for the brief skill

Run after ANY change to `SKILL.md` / `templates/*`: parallel read-only subagents (sonnet-level),
each given its prompt without the "Expected"; the agent decides and **quotes the rule** that
determined it — otherwise the wording isn't discoverable. A divergence = the change broke the
discipline: fix the skill's wording, not the scenario.

Last run: 2026-07-23 FINAL CORPUS SWEEP (review №12 close-out) — all 24 runs (22 scenarios, 5 & 8 two-part) against the finished corpus — 24/24 PASS (sc.15's first run was invalid — the agent treated the hypothetical fixture as the real repo and grepped it; re-run with an explicit "HYPOTHETICAL fixture" preamble → green. Method note: scenario givens should be framed as fixtures in the runner prompt). Earlier 2026-07-23 (BRIEF template + state machine, review №11) — status enum unified to `draft | decided | abandoned` (no `in-progress` — brief goes draft→decided; `abandoned` on explicit drop); cap ≤150 + rejected-options-never-cut is now the template's single home (playbook references it, killing the 300-vs-150 drift); Step 0/gate draft wording resynced; consent-language gone. Ran draft-resume, cap-150, state-enum, new-topic-FYI — 4/4 PASS. Earlier 2026-07-23 (craft-graph integration follow-up, review №9) — brief recon now uses only `active` graph nodes as a live stance (a `superseded` one is history). Ran the graph-active cascade — 1/1 PASS. Earlier 2026-07-23 (brief rework, review №6) — the commit skeleton now precedes the gate (verdict + Decided + rejected-with-reasons shown before "ok, commit it"; turn ends, ok never inferred, fragment enthusiasm ≠ ok), recon greps prior BRIEF verdicts (no-go dyra closed; plan's recon got the same line), the no-go/decided read path added to Step 0 ("what did we decide" → grep verdicts, answer, no resume ceremony), Step 0 ported (block upsert rides with the first write; new topic → FYI; several briefs → ask), self-consistency rule (a new fact beats your own earlier stance), convergence proposes the commit + "Decided" = explicit agreement, compact tripwire, git fate defined, cap 150 with rejected options never cut, hand-off asymmetry rationale (single successor by explicit choice) mirrored in plan (fan-out), duty-to-push-back softened (proof best / argument ok for conceptual / vibe forbidden), edit-vs-new-brief discriminator, description mid-task cutoff. The parent-artifact hook (brief→task/plan, plan→task) generalized in m.md and plan step 1. Ran all 13 (5 now 2 parts) + new 14–22 — 22/22 PASS, rules quoted verbatim. Earlier 2026-07-21 — full English translation of the plugin (SKILL.md + templates/* + this file): all 13 scenarios re-run — 13/13 PASS, decisions preserved and the governing rule quoted verbatim from the English files (task/plan boundaries, ≤2–3 questions, duty to push back, commit gate, draft rescue, resume-by-pulse, hint hand-off, decisions-in-BRIEF, no-go a full outcome, recon-from-graph, depth-first branches). Note: scenario 11's "no-go → skip the hand-off" rests on inference from Step 4 + the no-go rule (wording unchanged by the translation, identical to the RU original) — not a translation regression. Earlier 2026-07-21 — depth-first branches (scenario 13): red→green — before the change the agent explicitly
answered "there's no direct rule", after — the quote is verbatim, the second branch goes into "Remaining"; touched
by the Step 1 change — 4, 5, 12 + the new 13 — 4/4 PASS, no conflict with the "2–3 questions" limit (scenario 4
quotes both rules coherently). Earlier 2026-07-17 — description trimmed to ≤1024 (0.6.3): scenarios 1–3, 8p1 — 4/4 PASS,
the shortened boundary-with-task rule is quoted verbatim (the quote in scenario 1 updated to the new
wording). Earlier 2026-07-17 — recall (recon starts with the graph, scenario 12): ran 12 and 4, 5 touched by the
Step 1 change — 3/3 PASS, the new rule is quoted verbatim. Earlier 2026-07-17 —
11/11 PASS (first run of the new skill): the task/plan boundaries by description, interrogation and rubber-stamping
fended off, the commit gate and rescuing a draft distinguished, resume by the pulse, the hand-off preserves the
receiving skill's gate, "no-go" recorded without a hand-off.

## 1. Boundary: a stated task is task, not brief
Given: only the description text. Request: "add retries to the HTTP client; I'm just not sure whether exponential
or fixed-step".
Expected: this is NOT brief — the task is stated, the open question will be clarified by task on its own brief; quote "Not for
a stated code-change task, even with open questions — that's `task`".

## 2. Boundary: a chosen initiative is plan, not brief
Given: only the description text. Request: "we've already decided to rewrite billing — break it into stages, where to start".
Expected: this is NOT brief — the direction is chosen, only decomposition remains; quote "not for decomposing an already-chosen
initiative (that's `plan`)".

## 3. Trigger: "let's discuss whether it's worth it"
Given: only the description text. Request: "I have an idea to extract notifications into a separate service, but I'm not sure
it's worth it — let's discuss".
Expected: the brief skill fires — the choice of direction is itself the work; triggers "let's discuss",
"I have an idea but I'm not sure", "is it even worth it".

## 4. A stance, not a survey
Given: `SKILL.md`. The first round of discussion; the agent has accumulated six questions for the user.
Expected: the six questions aren't asked — at most 2–3 per round, only those that change the decision, the rest —
assumptions; the round brings options with trade-offs and a recommendation; quote "Questions — at most 2–3 per
round and only those where the answer truly changes the decision".

## 5. Duty to push back
Part 1 (given: `SKILL.md`): the user proposes an option in which the agent, from recon, sees a hole — it breaks an
existing code invariant.
Expected: show the hole with proof (file:line, a counterexample), not formalize the idea silently; quote "A brief
that only nods along isn't worth its tokens".
Part 2 (given: `SKILL.md`): the hole is conceptual — the proposed design won't scale / couples two layers — and
there is no repo `file:line` to point at.
Expected: still push back with a reasoned argument (proof isn't available for a conceptual hole), not stay silent
and not require a repo proof; quote "a reasoned argument is fine where the hole is conceptual … an unbacked vibe
is not".

## 6. Commit gate: no file until "ok, commit it"
Given: `SKILL.md`. The discussion is in full swing, the decision hasn't matured, there was no explicit "ok, commit it"; the temptation to
create BRIEF.md ahead of time, "so as not to lose it".
Expected: the file isn't written; quote "While the discussion is ongoing — text only, we write no files".

## 7. Rescuing a draft on wrap-up
Given: `SKILL.md`. In the middle of an unfinished discussion the user: "that's it, let's continue tomorrow".
Expected: offer to save a `draft` (the course of the discussion and the pulse — in the Log); agreement —
the only case of writing a file before the gate; refusal → we write nothing; quote "offer to save a `draft`".

## 8. Resume by the BRIEF
Part 1 (given: only the description text): a new session with no history, the user writes "let's continue
the discussion about notifications".
Expected: the brief skill fires — "let's continue the discussion" is in the triggers.
Part 2 (given: `SKILL.md`): there's a `docs/crafts/notify-service/BRIEF.md` with status `draft`; the
message is a bare resume trigger.
Expected: show the last pulse and offer to continue; quote "a bare resume trigger … → show the last "Decided: …
/ Remaining: …" from the Log".

## 9. Hand-off: the recommendation is a hint, the choice is the user's
Given: `SKILL.md`. The decision is recorded (`decided`, verdict go), the scale of what was discussed — one
task, one branch.
Expected: the `task` recommendation as a hint (the receiving skill does the classification), the question "start
a task / plan from this brief — or nothing for now?"; on the answer "task" — invoke task in the same session with a
pointer to BRIEF.md; quote "This is a **hint** — the receiving skill does the classification".

## 10. Decisions — in the BRIEF, not the graph
Given: `SKILL.md`. A long-lived architectural decision was born in the discussion; the temptation to create a node
in `docs/graph/` right away.
Expected: the node isn't created — a discussion has no `file:line` proof, the decision stays in the BRIEF, `task` will
create the node at wrap; quote "Decisions go in the BRIEF, not the graph".

## 11. "No-go" — a full outcome
Given: `SKILL.md` + `templates/BRIEF.md`. The discussion converged on "no-go"; the temptation to not record the
artifact ("there won't be any work anyway") or to offer a hand-off.
Expected: the BRIEF is recorded with status `decided` and verdict no-go, no hand-off is offered, "Spawned" is empty; quote
""decided not to do it" is a full and valuable outcome, not garbage".

## 12. Recon starts with the graph
Given: `SKILL.md`. Starting a discussion of "which caching approach to choose"; the repo has a `docs/graph/`
with a node on caching (a decision with proof).
Expected: recon starts with the graph (overview + grep for slugs), the found node is quoted as proof for the stance;
a proposal against a node is named explicitly; quote "first the decision graph on the topic … past
decisions and gotchas are ready-made proof for a stance".

## 13. Branches — depth-first, not broad
Given: `SKILL.md`. A branch about the storage choice is open, not closed; the agent wants to open a second in parallel
— about the notification format; the temptation to ask one question from each branch in the round.
Expected: the round stays in the storage branch; the second branch isn't opened but goes into the "Remaining" of the
pulse; quote "A round's questions come from a single branch of the discussion; finish the current one before
opening the next".

## 14. The commit skeleton precedes the gate
Given: `SKILL.md`. The discussion has converged; you're about to ask for the commit.
Expected: before the "ok, commit it" you show the commit skeleton — verdict + "Decided" list + rejected options
with their killing reason, one line each — and end the turn; the ok is not inferred from the running conversation
and fragment enthusiasm ("love that part") is not the ok; quote "show the **commit skeleton** … The ok approves
the *document*, not just the running conversation".

## 15. Recon finds a prior no-go
Given: `SKILL.md`. Starting a discussion "should we extract notifications into a service"; `docs/crafts/` holds an
older `BRIEF.md` whose verdict was `no-go` on exactly this, with reasons.
Expected: recon greps the verdict lines of `docs/crafts/*/BRIEF.md`, surfaces the prior no-go as a ready-made
stance, and doesn't relitigate from zero; quote "the verdict lines of `docs/crafts/*/BRIEF.md` — a past decision
(including a no-go) is a ready-made stance".

## 16. The BRIEF is committed, not floating
Given: `SKILL.md`. Step 3: BRIEF.md is written for slug `notify-service`, verdict go; the default branch is
unprotected.
Expected: the BRIEF is committed to the default branch with a one-line announce (`brief: notify-service`);
protected default → branch `brief/<slug>` + PR; the draft and later edits are commits too; quote "a BRIEF is a
document that outlives branches → commit it to the default branch".

## 17. A new fact beats your own earlier recommendation
Given: `SKILL.md`. In round 1 you recommended approach A; in round 3 a new branch surfaces a fact (an existing
constraint at `core/x.py:…`) that undercuts A in favor of B.
Expected: you name the reversal first and switch to B — you don't defend A to stay consistent; quote "Follow your
own evidence, not your own past stance … Loyalty to an earlier position of your own is worth nothing".

## 18. Convergence proposes the commit; "Decided" needs explicit agreement
Given: `SKILL.md`. The discussion has converged: "Remaining" holds only verdict-neutral details; the user hasn't
asked to commit.
Expected: you propose the commit yourself rather than keep discussing (that would slide into interrogation); and a
"Decided" line reflects only what the user explicitly agreed to this round, not un-objected proposals; quotes
"Remaining is empty, or only verdict-neutral details are left → propose the commit yourself" and ""Decided" means
the user explicitly agreed this round".

## 19. Mid-discussion compact → offer the draft
Given: `SKILL.md`. A long decomposition-of-the-idea discussion, no file saved yet; a context compaction just
happened.
Expected: offer to save the `draft` right away — the rejected options would otherwise be lost; quote "a
compact happened mid-discussion → offer to save the `draft` right away".

## 20. Revisiting: edit the verdict vs a new brief
Given: `SKILL.md`. A `decided` BRIEF exists. Case A: the same question is reopened and the answer changes. Case B:
the scope has shifted / a new question appears.
Expected: A → edit the verdict + a Log line on the existing BRIEF; B → a new brief linking the old, not a silent
edit; quote "the same question with a new answer → edit the verdict + a Log line; a new question or a shifted
scope → a new brief linking the old".

## 21. A question about a past decision is a read, not a resume
Given: `SKILL.md`. No discussion is running; the user asks "what did we decide about the notification transport?"
Expected: grep the verdict lines of `docs/crafts/*/BRIEF.md`, answer from the matching brief — no resume ceremony,
no new discussion spun up; quote "a **question about a past decision** … this is a read, not a resume: grep the
verdict lines".

## 22. A new topic isn't blocked by a parked brief
Given: `SKILL.md`. `docs/crafts/caching/BRIEF.md` is a `draft`; the user opens a brand-new, unrelated idea to
discuss.
Expected: no blocking "continue the old one?" — discuss the new topic, the parked brief gets one FYI line; quote
"The message brings a **new topic** while a draft brief exists → discuss the new one; no blocking question — one
FYI line".
