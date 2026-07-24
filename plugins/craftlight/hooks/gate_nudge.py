#!/usr/bin/env python3
"""craftlight hook B — PostToolUse/Edit|Write: an advisory nudge about the confirmation gate.

Never blocks. If product code is being edited (a file outside docs/) while a spec with
status draft exists (the gate hasn't been passed yet), it adds one reminder line to the
context. Self-quieting: gate passed → status in-progress → the nudge goes silent.

Deliberate limitation: the hook doesn't enforce the fact of consent (the same model flips the
status), it only returns the question "was there an ok?" to the context at the moment code is edited.

Why SPEC drafts only — deliberately asymmetric: a BRIEF/PLAN draft gates its own artifact (a
discussion, a decomposition), not the codebase, and coexists with any coding; don't "fix" the
symmetry by adding them here.

Blind spots, by design: edits made through Bash (sed, heredoc, patch) bypass PostToolUse
Edit|Write|MultiEdit entirely; S-mode leaves no spec to check. The hook is an advisory backstop —
the playbook is primary.

Input: JSON on stdin (tool_name, tool_input.file_path, cwd). Any ambiguity → stays silent.
"""
import glob
import json
import os
import re
import sys

STATUS_DRAFT_RE = re.compile(r"^Status:\s*draft\b", re.MULTILINE)
SPEC_SLUG_RE = re.compile(r"docs/crafts/([^/]+)/SPEC\.md$")


def _silent():
    sys.exit(0)


def _draft_slugs(project_dir):
    slugs = []
    pattern = os.path.join(project_dir, "docs", "crafts", "*", "SPEC.md")
    for spec in sorted(glob.glob(pattern)):
        try:
            with open(spec, encoding="utf-8") as f:
                text = f.read()
        except (OSError, UnicodeDecodeError):
            continue
        if STATUS_DRAFT_RE.search(text):
            m = SPEC_SLUG_RE.search(spec.replace(os.sep, "/"))
            slugs.append(m.group(1) if m else os.path.basename(os.path.dirname(spec)))
    return slugs


def main():
    # fail-open — a property: any exception (broken JSON, non-object, a cross-drive relpath on
    # Windows, etc.) → quiet exit 0; SystemExit from _silent() is re-raised.
    try:
        data = json.load(sys.stdin)
        if not isinstance(data, dict):
            _silent()

        file_path = (data.get("tool_input") or {}).get("file_path")
        if not file_path:
            _silent()

        project_dir = data.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()

        # an edit inside docs/ (including the spec itself) or outside the project → not product code
        rel = os.path.relpath(os.path.abspath(file_path), os.path.abspath(project_dir))
        first = rel.replace(os.sep, "/").split("/", 1)[0]
        if first == ".." or first == "docs":
            _silent()

        slugs = _draft_slugs(project_dir)
        if not slugs:
            _silent()

        listed = ", ".join(f'"{s}"' for s in slugs)
        context = (
            f"craftlight: spec {listed} has status draft — is the confirmation gate passed? "
            "Editing product code begins only after an explicit user ok on the plan. "
            "If the ok was received — move the spec's status to in-progress; if not — first show the spec and wait for the ok. "
            "The ok is a user message, not an inference."
        )
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": context,
        }}))
        sys.exit(0)
    except SystemExit:
        raise
    except Exception:
        _silent()


if __name__ == "__main__":
    main()
