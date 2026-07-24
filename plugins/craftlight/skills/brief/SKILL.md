---
name: brief
description: Working out a decision by dialogue before any task — discuss the idea, weigh options with trade-offs, record the decision in BRIEF.md, and hand it to task or plan. Use this skill when the user wants to discuss first and only then (maybe) act — "let's discuss", "before doing it let's talk", "help me decide", "help me pick an approach", "which approach is better", "let's weigh the options", "I have an idea but I'm not sure", "is it even worth it", "let's think this through" — even without the words "brief" or "skill". Also trigger on a request to continue a discussion — "let's continue the discussion", "back to the brief", "what did we decide there". Not for a stated code-change task, even with open questions — that's `task` (a "let's discuss the approach" that surfaces inside a running task stays in task's ambiguity rules, it doesn't spawn a brief); not for decomposing an already-chosen initiative (that's `plan`); not for "how does this work" (a normal answer) and not for a one-off opinion question with no prospect of work. brief is justified only when the choice of direction is itself the work.
---

# brief — decision by dialogue before the task

Principle: **brief sits ABOVE `plan` and `task`.** The discipline ladder: brief answers "what are we doing and
is it even worth it" (the result is a decision), plan answers "how to break the epic down" (the result is a DAG of
tasks and waves), task answers "how to execute" (the result is code). You take on brief when the direction isn't
chosen yet and the choice itself is the work. Ceremony is proportional: a discussion is just a conversation, until
the commit gate not a single file exists, a dead discussion is free. **The one discussing neither executes nor
decomposes — they work out a decision, commit it, and hand it off.**

Not for this skill: a stated task, even with a couple of open questions → `task` (inside its M/L there's a "spec
brief" — a phase that refines an already-accepted direction, don't confuse it with this skill); a chosen initiative
that just needs breaking into tasks → `plan`; "how does this work", a review, a one-off opinion question → a normal
answer. Realized along the way that the direction is already chosen and there's nothing to discuss → leave and hand
off to `task` or `plan`.

## Step 0. Orientation and resume

There's a `CRAFT.md` → read it first: the project map, the starting point. The craftlight block upsert in the root
`CLAUDE.md` (reference and procedure — `skills/task/templates/CLAUDE-block.md`) rides with brief's first write to
disk — the saved pre-gate draft or the Step 3 artifact, whichever comes first — never earlier: until then brief
writes no files, and a call that never writes must not edit the user's CLAUDE.md.

- The message is a **question about a past decision** ("what did we decide about X") → this is a read, not a
  resume: grep the verdict lines of `docs/crafts/*/BRIEF.md`, answer from the matching brief, no resume ceremony.
- A `docs/crafts/*/BRIEF.md` with status `draft` (an unfinished discussion saved before the commit gate) and
  the message is a **bare resume trigger** ("continue the discussion", "back to the brief") → show the last
  "Decided: … / Remaining: …" from the Log and offer to continue: the brief is external memory, resuming reads
  the BRIEF, not the chat history. Several draft briefs → ask which one.
- The message brings a **new topic** while a draft brief exists → discuss the new one; no blocking question —
  one FYI line: `parked: brief "<slug>" is a draft — say "back to the brief" to resume it`.
- Refusal to resume → leave the draft in place; drop it only on an explicit request (status `abandoned`).
  Resuming specs and plans is the concern of `task` and `plan`; brief operates only on briefs.

## Step 1. Discussion — a stance, not a survey

The skill is justified only if the dialogue converges to a decision. Two degenerations are forbidden: interrogation
(questions without a stance) and rubber-stamping (formalizing the first idea without checking it).

- **Recon before opinion** — it's cheap: first the decision graph on the topic (`docs/graph/_overview.md` +
  grep for slugs/aliases; `active` nodes only — a `superseded` one is history, useful only as "we already
  moved off this"), plus the verdict lines of `docs/crafts/*/BRIEF.md` — a past decision (including a
  no-go) is a ready-made stance and "we already decided this" saves a whole round; then targeted Grep/Glob,
  reading fragments; a broad search goes to an Explore subagent. The decision lives outside the code (a vendor
  choice in a greenfield, a policy call) → nothing to recon: say so and discuss on the merits, don't cargo-grep.
  Stances rest on the repository, not on generalities. Proposing something that contradicts an existing node →
  say so explicitly ("contradicts [[slug]], because …") — a deliberate revision, not a silent bypass.
- **Bring a stance each round**: options with trade-offs and your own recommendation. Questions — at most
  2–3 per round and only those where the answer truly changes the decision; the contentious — ask the user,
  the reasonable — lock it as an assumption and state it aloud.
- **Follow your own evidence, not your own past stance.** A new branch turns up a fact that undercuts your
  earlier recommendation → name that first and switch, out loud. Loyalty to an earlier position of your own is
  worth nothing; sycophancy toward it is the failure mode here, the mirror of rubber-stamping the user.
- **Branches — depth-first.** A round's questions come from a single branch of the discussion; finish the
  current one before opening the next. The pulse catches wandering after the fact — depth-first keeps it from
  starting; a neighboring branch isn't lost: put it in "Remaining" and return once the current one is closed.
- **Duty to push back.** You see a hole in the user's idea → show it. Proof is best (file:line, a counterexample
  from the repository); a reasoned argument is fine where the hole is conceptual (scaling, coupling — no repo
  proof exists); an unbacked vibe is not. A brief that only nods along isn't worth its tokens.
- **Convergence pulse.** End each round with two lines: "Decided: …" / "Remaining: …". "Decided" means the user
  explicitly agreed this round — not "I proposed it and drew no objection": a gate must never rest on a stack of
  silent non-answers. Remaining is empty, or only verdict-neutral details are left → propose the commit yourself,
  don't keep the discussion open past convergence (that slides into interrogation).
- **Tripwire:** a compact happened mid-discussion → offer to save the `draft` right away — no file
  exists yet, and an auto-compact silently eats the nuances and the rejected options. This risk is highest here:
  brief is the most conversational skill in the plugin.

## Step 2. The commit gate

- Before the gate, show the **commit skeleton**: the verdict, the "Decided" list, and the rejected options with
  their killing reason — one line each — under "here's what goes into the file". The ok approves the *document*,
  not just the running conversation; without the skeleton the user approves a decision and gets up to a page they
  never saw. Mechanically: showing the skeleton ends the turn — the "ok, commit it" arrives as the user's next
  message, never inferred. Enthusiasm about a fragment ("love that part", "good idea") approves the fragment, not
  the decision.
- BRIEF.md is written **only after that explicit "ok, commit it"** (or a direct equivalent). Silence or a missing
  answer ≠ ok. While the discussion is ongoing — text only, we write no files.
- The user wraps up an unfinished discussion ("let's continue tomorrow", "that's enough for now") → offer to
  save a `draft` (status `draft`): the template filled in as far as it goes + the course of the discussion and the
  current pulse in the Log. Agreeing to the draft is the only case of writing a file before the gate (the block
  upsert rides with it — step 0); refusal → we write nothing.

## Step 3. The artifact

Record the decision in `docs/crafts/<slug>/BRIEF.md` per `templates/BRIEF.md` — the same "folder per craft"
convention as SPEC and PLAN: the artifacts of one craft sit side by side. **Git fate:** a BRIEF is a document that
outlives branches → commit it to the default branch with a one-line announce (`brief: <slug>`); the default branch
is protected → branch `brief/<slug>` + a PR. The pre-gate draft and every later edit (a revised verdict, the
"Spawned" links) are commits too, not floating changes. Status `decided` + verdict: **go / no-go / deferred** —
"decided not to do it" is a full and valuable outcome, not garbage. The cap and its cut-priority
are in `templates/BRIEF.md` (the single home of the number; hitting it never cuts the rejected options).

## Step 4. Hand-off

- By the scale of what was discussed, give a recommendation: one task (one branch, one PR) → `task`; an
  initiative spanning several tasks → `plan`. This is a **hint** — the receiving skill does the classification.
- Ask: **"start a task / plan from this brief — or nothing for now?"**
- "Task" / "plan" → invoke the corresponding skill in the same session; the input is a pointer to
  `docs/crafts/<slug>/BRIEF.md` plus the decision in one line. brief invokes the successor directly — unlike
  plan's hand-off, this is a single successor the user just chose by an explicit answer, so the call is a
  continuation, not orchestration. The receiving skill's confirmation gate stays in force: the spec or plan is
  still shown and waits for an explicit ok, and its brief reads the BRIEF pointer (the parent-artifact hook in
  task/plan).
- "Nothing for now" → the BRIEF stays `decided`, stop. On hand-off, write links to the spawned SPEC/PLAN into
  "Spawned".

## Rules

- **The one discussing doesn't execute.** Zero code edits, zero specs or plans on behalf of the receiving
  skills — brief passes a pointer to BRIEF.md, the rest task/plan do by their own rules.
- **Decisions go in the BRIEF, not the graph.** A discussion has no `file:line` proof; `task` will create the
  graph node at wrap, once the decision shows up in code. brief doesn't touch the graph.
- **A good question admits a "no-go" answer.** If the discussion can only end in "go", that's not working out a
  decision, it's procrastination before `task`.
- **The BRIEF is the memory of a decision, not a work tracker.** After hand-off, state lives in SPEC/PLAN; only
  "Spawned" is appended. Revisiting: the same question with a new answer → edit the verdict + a Log line; a new
  question or a shifted scope → a new brief linking the old, not silent drift.
