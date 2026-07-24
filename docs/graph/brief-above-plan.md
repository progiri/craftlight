# brief-above-plan: brief — a decision layer above plan and task (discusses, doesn't execute)

Type: decision
Area: brief
Proof: `plugins/craftlight/skills/brief/SKILL.md:8` <!-- the ladder; the commit gate — :48; the hand-off with invocation — :67 -->

## Gist
The `brief` skill sits ABOVE `plan` and `task` — the ladder: brief ("what we're doing and whether to") → plan ("how
to break it down") → task ("how to execute"). Taken on when the choice of direction is itself the work; a multi-round
dialogue (a stance not a survey, the duty to push back, the convergence pulse) converges to a decision, which is
recorded in `docs/crafts/<slug>/BRIEF.md` only after an explicit "ok, commit it"
(`plugins/craftlight/skills/brief/SKILL.md:48`). The hand-off is a task/plan recommendation and an invocation of the
chosen skill in the same session with a pointer to the BRIEF (`plugins/craftlight/skills/brief/SKILL.md:67`); the
receiving skill's confirmation gate stays in force.

## Rationale
There was no place to discuss "is it even worth it and what exactly": the spec-brief phase of task M/L refines an
already-stated task, plan's step 1 discusses an already-chosen initiative — the choice of direction either overloaded
them or was lost in the chat without an artifact. A file only after the gate — ceremony is proportional: a dead
discussion is free. Rejected: (1) a separate `docs/briefs/` folder — a second convention and a break in the craft's
history, BRIEF and the SPEC/PLAN it spawns should sit in one folder; (2) keeping a file from the first round — a file
for every fleeting "let's discuss"; (3) "propose and stop" at the hand-off (as in plan) — an extra manual step: the
invocation is safe because the receiving skill's gate isn't going anywhere.

## Risks
brief intercepts stated tasks ("do X" with an open question) → a double brief and bloated ceremony: the task is
stated → straight to `task`. A graph node from brief → a node without a `file:line` proof (the discussion's decisions
are picked up by task at wrap). Interrogation or rubber-stamping in the dialogue → the skill doesn't earn back its
tokens (the mechanics — Step 1 of SKILL.md).

## Edges
- part-of [[ceremony-proportional]]
- depends-on [[confirm-gate]]
- depends-on [[plan-above-task]]
