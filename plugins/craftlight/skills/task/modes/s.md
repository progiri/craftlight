# Mode S — straight to work

Zero artifacts: no spec, no plan, no summary file — though a closing report is owed (step 4). The whole backstop is one cheap ritual and stop rules.

## Order

1. **Restate the task in ≤2 lines** and show it to the user together with the planned solution in one phrase. This catches misunderstandings for pennies. Shown it — wait for an explicit ok and only then begin (the confirmation gate and advance ok are in the router). Questions surfacing at the restatement pass the S question test: exactly one closed question the user can answer in a line, and the answer doesn't change the shape of the solution → fold it into the restatement message (the gate ends the turn anyway — the question rides for free) and stay in S; more than one, or the answer reshapes the solution → that's no longer S: escalate to M.
2. **Do it.** Tests — the router's global rule: failing test first (a bugfix starts from a failing repro), no theater, no harness → observe and say so.
3. **Verify:** run the tests of the touched files plus any you wrote — the full suite is M/L territory — and the project's configured linter: don't introduce new tools, pre-existing foreign warnings → the backlog, not the diff. The honesty rule is the router's: in the report, only the observed. Something foreign is failing — tell the user, don't fix it silently.
4. **One atomic commit** to the task branch (the branch rule is in the router). The message — what and why, not "fix". Close with a 2–4 line report: what changed, how it was verified, the commit hash — the report is owed; it's a summary *file* that S doesn't write.

## Stop rules

- **No guess-and-patch** — the router's global rule, counter included: the cheap first attempt aside, two rejected hypotheses or a second failed minimal experiment → the `debug` skill.
- **Ambiguity → a concrete question to the user.** Don't fill in the blanks: a guess with silent continuation costs more than any question. Mid-work the same S question test applies (step 1): one closed line-answer question → ask and stay in S; the answer reshapes the solution, or questions accumulate → escalate to M.
- **Noticed something foreign along the way** (a bug nearby, a stale doc — not about your task) → one line into `docs/crafts/_backlog.md` and continue (no file → create it; a line is `- YYYY-MM-DD [task-slug or chat]: the gist in one line` — canon in `templates/BACKLOG.md`); in S this is the only sink — there's no spec with "Open questions". Your *own* touched files are under the same discipline: change only what the task requires — the itch to rename, reformat, or tidy up nearby is a backlog line, not a diff line.
- **Escalation to M** if in fact: more than 2 files are touched, the S question test failed (see step 1), you snagged the risk zone (the canonical list is in the router). `docs/crafts/<slug>/SPEC.md` in this case is written after the fact from what's already done — that's a normal path, not a sign of a classification error. The after-the-fact spec passes the gate: show it and wait for the ok before continuing.
- **A durable decision or a gotcha worth the project remembering** → don't escalate for the node's sake: a finished S doesn't buy the M ceremony to write one graph node. One line into `docs/crafts/_backlog.md` tagged `graph-candidate`, with the `file:line` proof in the line — the nearest M/L wrap or `craft-graph` pass promotes it into a node. No durable lesson → no breadcrumb: the graph doesn't collect one-off fixes.
