#!/usr/bin/env python3
"""craftlight hook C — SessionStart/compact|resume: push the active discipline state.

Prompt discipline degrades after a context compaction: the model, mid-work, keeps going without
re-reading the artifact. The hook makes recovery push-based — right after compact/resume it brings
the active discipline artifacts into context. Active = Status `in-progress` (gate passed, work
running) OR `draft` (gate not passed: a saved unfinished approval/discussion — it must resurface,
or the compact-tripwire saves are pointless). Terminals (done, decided, abandoned, root-found,
dead-end) stay silent.

Two semantic guards in the pushed line:
- A draft must NOT read as "continue working": its resume point is the approval/discussion step,
  never execution — otherwise this hook injects the exact failure hook B exists to catch.
- FYI grammar, not a command: the session may have resumed about something else entirely; the line
  must not hijack it (the resume-nag was evicted from the skills' step 0 — don't reintroduce it a
  layer below).

Scanned: docs/crafts/*/{BRIEF,SPEC,PLAN,DEBUG}.md plus docs/reviews/*.md (a review draft exists
only via the compact-tripwire save — resurfacing after the reset is its whole purpose).
Per-type "current spot": SPEC/PLAN — the first unchecked box; BRIEF — the last pulse
(Decided/Remaining); DEBUG — the last hypothesis-table row. A pure injection: blocks nothing; no
active artifacts or any error → silence (fail-open).

Input: JSON on stdin (hook_event_name, source, cwd). The source filter is in the manifest.
Output: JSON hookSpecificOutput.additionalContext on stdout, or silence.
"""
import glob
import json
import os
import re
import sys

# artifact file name → type label; order is how the paths are read and sorted
ARTIFACTS = {
    "BRIEF.md": "brief",
    "SPEC.md": "task",
    "PLAN.md": "plan",
    "DEBUG.md": "debug",
}
ACTIVE_RE = re.compile(r"^Status:\s*(in-progress|draft)\b", re.MULTILINE)
MODE_RE = re.compile(r"^Mode:\s*(\S+)", re.MULTILINE)
BRANCH_RE = re.compile(r"^Branch:\s*(\S+)", re.MULTILINE)
UNCHECKED_RE = re.compile(r"^- \[ \] (.+)$", re.MULTILINE)
DECIDED_RE = re.compile(r"^Decided:\s*(.+)$", re.MULTILINE)
REMAINING_RE = re.compile(r"^Remaining:\s*(.+)$", re.MULTILINE)
HYP_ROW_RE = re.compile(r"^\|\s*\d+\s*\|.+\|\s*$", re.MULTILINE)
ITEM_LIMIT = 160


def _silent():
    sys.exit(0)


def _spot(kind, text):
    """Per-type 'current spot' — the resume entry point, not a one-size-fits-none template."""
    if kind in ("task", "plan"):
        m = UNCHECKED_RE.search(text)
        return f"first unchecked: {m.group(1)[:ITEM_LIMIT]}" if m else ""
    if kind == "brief":
        decided = DECIDED_RE.findall(text)
        remaining = REMAINING_RE.findall(text)
        parts = ([f"Decided: {decided[-1][:ITEM_LIMIT]}"] if decided else []) + \
                ([f"Remaining: {remaining[-1][:ITEM_LIMIT]}"] if remaining else [])
        return "last pulse — " + " / ".join(parts) if parts else ""
    if kind == "debug":
        rows = HYP_ROW_RE.findall(text)
        return f"last hypothesis: {rows[-1][:ITEM_LIMIT]}" if rows else ""
    return ""  # review: the slug and status are the whole story


def _describe(path, kind):
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except (OSError, UnicodeDecodeError):
        return None
    m = ACTIVE_RE.search(text)
    if not m:
        return None
    status = m.group(1)
    slug = (os.path.splitext(os.path.basename(path))[0] if kind == "review"
            else os.path.basename(os.path.dirname(path)))
    head = f'"{slug}" ({kind}, {status}'
    if kind == "task":
        mode = MODE_RE.search(text)
        branch = BRANCH_RE.search(text)
        if mode and branch:  # mode/branch exist only on a spec
            head += f", mode {mode.group(1)}, branch {branch.group(1)}"
    head += ")"
    spot = _spot(kind, text)
    if spot:
        head += f"; {spot}"
    return head


def main():
    # fail-open — a property: any exception → quiet exit 0 (SystemExit from _silent() is re-raised).
    try:
        data = json.load(sys.stdin)
        if not isinstance(data, dict):
            _silent()

        project_dir = data.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
        # glob doesn't support {…} — glob by each name and merge
        entries = []
        for name, kind in ARTIFACTS.items():
            for p in glob.glob(os.path.join(project_dir, "docs", "crafts", "*", name)):
                entries.append((p, kind))
        for p in glob.glob(os.path.join(project_dir, "docs", "reviews", "*.md")):
            entries.append((p, "review"))
        lines = [d for d in (_describe(p, k) for p, k in sorted(entries)) if d]
        if not lines:
            _silent()

        context = (
            "craftlight: active discipline artifacts — "
            + "; ".join(lines) + ". "
            "If the current work is one of them — resume it by reading the artifact, not the chat "
            "history: an in-progress one continues per its skill's playbook; a draft's gate is NOT "
            "passed — it resumes at its approval/discussion step, never straight into execution "
            "(a review draft — at its unfinished passes). Otherwise continue the user's current "
            "request; this line is advisory."
        )
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": context,
        }}))
        sys.exit(0)
    except SystemExit:
        raise
    except Exception:
        _silent()


if __name__ == "__main__":
    main()
