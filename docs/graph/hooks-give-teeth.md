# hooks-give-teeth: hooks return rules and state to the context

Type: decision
Area: hooks
Proof: `plugins/craftlight/hooks/session_state.py:65`

## Gist
The craftlight plugin hooks are advisory-only: they deterministically return to the context what the
prompt might have lost, and block nothing. Hook C (SessionStart/`compact|resume`) pushes in-progress
specs — slug, mode, branch, the first unclosed item (`plugins/craftlight/hooks/session_state.py:65`);
hook B (PostToolUse/Edit|Write) nudges about the gate when a draft spec is unclosed
(`plugins/craftlight/hooks/gate_nudge.py:70`). Any ambiguity → silence (fail-open).

## Rationale
Prompt discipline degrades under context pressure (compact, long sessions), and after compaction the
model keeps working without re-reading the spec — recovery must be push-based rather than relying on
the skill's Step 0. Rejected: a blocking commit guard (hook A, lived in 0.7.0, removed in 0.8.0) — the
bypass instruction sat in the deny message itself (a self-served override: the model could set the
flag without the user's ok, i.e. the block guarded against forgetting but created an illusion of
protection against choice), plus a false deny on the compound `git checkout -b … && git commit`.
Rejected earlier (the hooks-enforcement brief): blocking Edit/Write before the gate — false positives
on S mode, and the status is flipped by the same untrusted model.

## Risks
A return to blocking hooks without a trusted consent signal → a repeat of gotcha A: the bypass is
self-served, and false blocks hit honest paths ([[false-positive-costlier]]). Betting on pull-based
resume (the model will go grep specs on its own after compact) → quietly continuing work past the
checklist and gates — exactly what hook C closes.

## Edges
- affects [[spec-travels-with-branch]]
- affects [[confirm-gate]]
- depends-on [[false-positive-costlier]]
