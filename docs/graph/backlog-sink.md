# backlog-sink: banning scope creep requires a sink

Type: decision
Area: task-router
Proof: `plugins/craftlight/skills/task/modes/m.md:18`

## Gist
Something foreign noticed along the way (outside the current task's scope) goes as a single line into
`docs/crafts/_backlog.md` — and work continues. What concerns the task stays, as before, in the spec's "Open
questions"; wrap moves the unresolved among them into the backlog or discards it deliberately
(`plugins/craftlight/skills/task/modes/m.md:31`). In S the backlog is the only sink
(`plugins/craftlight/skills/task/modes/s.md:16`); `debug` writes to the same place. A sink, not a tracker:
no statuses or priorities, triage is on the human (a line became a brief/task → it's deleted).

## Rationale
A ban without a sink doesn't work: "don't widen the scope" with no answer to "so where does what I noticed go?"
forces either silently losing findings or silently leaking them into the code — both outcomes worse than one line
in a file. The idea is GSD's capture channel, trimmed to the craftlight idiom (flat markdown, zero automation).
Rejected: a tracker with statuses/priorities — drift into project management, foreign territory; automatic triage
or reminders — runtime against the plugin's DNA; a separate file per entry — ceremony, the backlog is read as a list.

## Risks
A sink without triage discipline → a dump people stop trusting (hence the rule in the template: taken into work or
no longer relevant → the line is deleted). Recording what concerns the task into the backlog instead of "Open
questions" → loss of the decision context at wrap.

## Edges
- part-of [[ceremony-proportional]]
- affects [[spec-in-crafts]]
