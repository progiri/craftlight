# done-is-observed: "done" = an observed result

Type: invariant
Area: core
Proof: `plugins/craftlight/skills/task/modes/m.md:23`

## Gist
"Works" is said only of what you saw yourself — a run, output, a screen; "should work" is a
forbidden phrasing. The unverified is flagged explicitly in the report ("didn't check …") — a
legitimate outcome, not a failure. It applies at the output of every task mode: wrap M/L and the
"Verify" step in S (`plugins/craftlight/skills/task/modes/s.md:9`).

## Rationale
A success report without observation is the main failure of agentic tasks: green tests ≠ a working
feature, and "should work" masks the unverified as verified. An honest "didn't check X" is
cheaper than a false "works": the user knows what to check for themselves. Symmetry with
[[no-guess-and-patch]]: that one forbids fixing blind, this one — reporting blind. An adaptation of
verification-before-completion (superpowers) into the existing wrap. Rejected: a separate
verify skill or ritual — an extra entry point for a rule that lives at the end of every task;
ceremony didn't grow.

## Risks
"Works" without a run → the user is the first to learn of the breakage, and wrap's "done" verdict
stops meaning anything: the evidentiary value of the whole block is zeroed out by one unverified
phrase.

## Edges
- part-of [[ceremony-proportional]]
