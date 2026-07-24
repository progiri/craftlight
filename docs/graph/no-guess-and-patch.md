# no-guess-and-patch: the ban on blind edits

Type: invariant
Area: core
Proof: `plugins/craftlight/skills/task/modes/s.md:14`

## Gist
The first fix hypothesis didn't work → stop. Reproduce, read the error in full, a new hypothesis, a minimal experiment, the root cause.

## Rationale
The "patch at random — rerun" loops are the biggest devourer of tokens and time; they treat the symptom, not the cause.

## Risks
A second blind edit under pressure ("demo in 20 minutes") → a cascade of masking fixes on top of a wrong model of the bug.

## Edges
- part-of [[ceremony-proportional]]
