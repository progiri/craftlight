# debug-inside-task: debug — a subcycle below task, diagnosis without a fix

Type: decision
Area: debug
Proof: `plugins/craftlight/skills/debug/SKILL.md:14`

## Gist
The discipline ladder grows not only upward (brief above plan above task) but also downward: debug is a subcycle
BELOW task. task drops into debug by the no-guess-and-patch stop rule (a drawn-out root hunt,
`plugins/craftlight/skills/task/modes/s.md:14`, `plugins/craftlight/skills/task/modes/m.md:19`)
and gets back a root with a `file:line` proof; the fix — again through task. debug doesn't edit code and
doesn't commit — not even an obvious one-line fix. The hypothesis log is by default without a file (the chat /
the spec's "Log"); `DEBUG.md` — only for a drawn-out case.

## Rationale
A ban without a playbook doesn't work: "stop → hunt for the root" didn't say HOW to hunt — now the stop has an
address. The boundary "diagnoses and doesn't fix" repeats the model of the other skills (plan plans and doesn't
execute, code-review reads and doesn't edit): one skill — one job, a fix without task's gate is impossible.
Rejected: a debug mode inside task — it would bloat the router and mix diagnosis with execution; a mandatory
DEBUG.md for every debug (like state in GSD) — ceremony for every little thing, against proportionality.

## Risks
A fix from debug bypassing task → an edit without the gate and without a regression test on the root. Debugging
without an exit into a skill on a drawn-out hunt → a return to guess-and-patch under pressure ("just try one more
variant").

## Edges
- part-of [[ceremony-proportional]]
- depends-on [[no-guess-and-patch]]
