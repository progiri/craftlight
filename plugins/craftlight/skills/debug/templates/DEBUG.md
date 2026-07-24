<!-- Form only: sections, field enums, the hypothesis-table schema. Behavior (when to create the file, the
     protocol, the return to task) lives in debug/SKILL.md — on conflict the playbook wins. These comments are
     write-time guidance, NOT copied into the artifact (inline enums excepted). Template edits stay read-compatible. -->
# DEBUG: <symptom in one line>

Status: in-progress <!-- in-progress | root-found | dead-end. No `draft` — debug has no gate; `dead-end` is the
     honest terminal (didn't find it). No `abandoned` — a dead-end already names an honest stop. -->
Task: <docs/crafts/<slug>/SPEC.md or "standalone"> <!-- the bidirectional link to the parent, if debug came from a task -->

## Symptom
<!-- What is observed vs. expected. When it started, if known. 2–3 lines. -->

## Repro
<!-- Minimal steps / the repro command or test; frequency (always / N of M runs); significant env conditions.
     Its own section because resume re-runs it first (stop rule: repro gone → back to step 1). -->

## Observations
<!-- Facts with proofs only: error messages, stack traces, log fragments, `file:line`. Interpretations → hypotheses. -->
-

## Hypotheses
<!-- One row per hypothesis. Prediction mandatory: "if the cause is X, under Y I'll see Z".
     Verdict: confirmed / rejected — with the experiment's fact, not an opinion.
     A row carried in from task's failed attempts → tag it `(from task)`: it seeds the log but does NOT count
     toward debug's change-of-angle tally (the counting rule is in the playbook). -->
| # | Hypothesis | Prediction | Experiment | Verdict |
|---|---|---|---|---|
| 1 |  |  |  |  |

## Root
<!-- The diagnosis, the four fields of the Output contract:
     root `file:line` — the breakage mechanism in one phrase — a minimal repro — the direction of the fix (not a patch).
     Status → root-found. A dead end → Status dead-end: what was ruled out, the next-cheapest step. -->

<!-- File form: sits in docs/crafts/<slug>/ next to the task's spec if debug came from task, else its own slug.
     After the diagnosis it stays in place as the history of the hunt. -->
