# Security Policy

## Reporting a vulnerability

Report vulnerabilities privately via GitHub's private vulnerability reporting on this
repository (Security → Report a vulnerability). Do not open a public issue for a security
problem. Confirmed issues ship as a patch release with a CHANGELOG entry crediting the
reporter (unless you prefer otherwise).

## Supported versions

The latest released version (top entry of [CHANGELOG.md](CHANGELOG.md)) receives fixes;
older versions are not patched.

## What installing the plugin executes

Skills and templates are markdown instructions — they execute nothing by themselves.
The only executable code craftlight ships is two Python hooks
([`plugins/craftlight/hooks/`](plugins/craftlight/hooks/)) that Claude Code runs locally:

- `session_state.py` — SessionStart on `compact|resume`; `gate_nudge.py` — PostToolUse on `Edit|Write`.
- **Advisory-only:** they print context text to stdout; they never block a tool call.
- **Fail-open:** any error or ambiguity → silent `exit 0`.
- **python3 stdlib only** — no third-party dependencies.
- **No network access**, no subprocesses, no environment mutation.
- **Read-only:** they read only `docs/crafts/*/{BRIEF,SPEC,PLAN,DEBUG}.md` under the project
  directory and write no files.

Both hooks are covered by fixture tests (`hooks/tests/`, run in CI), including the fail-open
property (any input → exit 0, empty stderr).
