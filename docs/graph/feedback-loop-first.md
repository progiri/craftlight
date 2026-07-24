# feedback-loop-first: the repro is a red feedback loop, and it comes before any theory

Status: active
Type: decision
Area: debug
Source: debug-feedback-loop
Aliases: red-capable-loop
Proof: `plugins/craftlight/skills/debug/SKILL.md:54-65`

## Gist
debug's step 1 builds one command — red-capable (asserts the user's exact symptom, not "runs without
erroring"), deterministic, fast, agent-runnable — and every later step only consumes it: no red-capable
loop → no hypotheses. Once red, the repro is minimised until every element is load-bearing; flaky bugs get
a raised reproduction rate instead of a "clean" repro.

## Why
The earlier "minimal reliable repro" prose had no verifiable completion criterion — an agent could claim a
repro without ever running one command; the loop's four checkable properties (red-capable, deterministic,
fast, agent-runnable) close that hole. Rejected: a heavier multi-phase protocol with dedicated fix/cleanup
phases — it would violate the fix-shaped boundary, and the phase ceremony contradicts proportionality (the
"obvious from the first error" escape hatch stays).

## Risks
A green-only "repro" (runs, asserts nothing) gives false confidence — every experiment downstream measures
nothing. Demanding the loop on trivial cases would be ceremony creep; the escape hatch caps it.

## Edges
- part-of [[debug-inside-task]]
- depends-on [[no-guess-and-patch]]
