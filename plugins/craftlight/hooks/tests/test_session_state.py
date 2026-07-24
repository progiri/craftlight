"""Fixture tests for hook C (session_state): pushing active discipline artifacts after compact/resume.

Active = Status in-progress OR draft (the family state machine, review №11); terminals stay silent.
The pushed line must carry per-status semantics (a draft resumes at its gate, not into execution)
and FYI grammar (it must not hijack an unrelated session).

Each test spins up a temporary project folder, feeds the hook JSON on stdin, and checks
additionalContext. Run: python3 -m unittest discover -s plugins/craftlight/hooks/tests
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
HOOK = os.path.join(os.path.dirname(HERE), "session_state.py")


def _spec(root, slug, status, mode="M", branch="task/x",
          boxes=("- [x] one", "- [ ] two", "- [ ] three")):
    d = os.path.join(root, "docs", "crafts", slug)
    os.makedirs(d, exist_ok=True)
    body = f"# SPEC: {slug}\n\nStatus: {status}\nMode: {mode}\nBranch: {branch}\n\n## Checklist\n"
    body += "\n".join(boxes) + "\n"
    with open(os.path.join(d, "SPEC.md"), "w", encoding="utf-8") as f:
        f.write(body)


def _artifact(root, slug, filename, status, body_extra=""):
    """A minimal discipline artifact (BRIEF/PLAN/DEBUG) with a status line."""
    d = os.path.join(root, "docs", "crafts", slug)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, filename), "w", encoding="utf-8") as f:
        f.write(f"# {filename[:-3]}: {slug}\n\nStatus: {status}\n{body_extra}")


def _review(root, name, status):
    d = os.path.join(root, "docs", "reviews")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, name), "w", encoding="utf-8") as f:
        f.write(f"# Review: x\n\nStatus: {status}\nVerdict: —\n")


def _run(cwd=None, source="compact", raw=None):
    if raw is None:
        raw = json.dumps({"hook_event_name": "SessionStart", "source": source, "cwd": cwd})
    p = subprocess.run([sys.executable, HOOK], input=raw,
                       capture_output=True, text=True)
    # fail-open — a property: any input → quiet exit 0 with no stderr (otherwise the test is red)
    assert p.returncode == 0, f"returncode={p.returncode}, stderr={p.stderr!r}"
    assert p.stderr == "", f"fail-open violated, stderr={p.stderr!r}"
    return p


def _ctx(p):
    out = p.stdout.strip()
    if not out:
        return ""
    try:
        j = json.loads(out)
    except json.JSONDecodeError:
        return ""
    return j.get("hookSpecificOutput", {}).get("additionalContext", "")


class SessionState(unittest.TestCase):
    def test_pushes_in_progress_spec(self):
        d = tempfile.mkdtemp()
        _spec(d, "foo", "in-progress")
        ctx = _ctx(_run(d))
        self.assertIn('"foo" (task, in-progress', ctx)
        self.assertIn("task/x", ctx)
        self.assertIn("two", ctx)          # first unchecked
        self.assertNotIn("three", ctx)     # the second unchecked isn't needed

    def test_multiple_in_progress_lists_all(self):
        d = tempfile.mkdtemp()
        _spec(d, "alpha", "in-progress")
        _spec(d, "beta", "in-progress", mode="L", branch="task/b")
        ctx = _ctx(_run(d))
        self.assertIn("alpha", ctx)
        self.assertIn("beta", ctx)

    def test_draft_pushed_with_gate_wording(self):
        # review №11 state machine: draft is ACTIVE (a saved unfinished gate) and must resurface —
        # but with the draft semantics, never as "continue working".
        d = tempfile.mkdtemp()
        _spec(d, "new", "draft")
        _spec(d, "old", "done")
        ctx = _ctx(_run(d))
        self.assertIn('"new" (task, draft', ctx)
        self.assertNotIn("old", ctx)                       # terminal stays silent
        self.assertIn("gate is NOT passed", ctx)           # the draft clause
        self.assertIn("never straight into execution", ctx)

    def test_mixed_draft_and_in_progress_both_listed(self):
        d = tempfile.mkdtemp()
        _spec(d, "alpha", "in-progress")
        _spec(d, "beta", "draft")
        ctx = _ctx(_run(d))
        self.assertIn('"alpha" (task, in-progress', ctx)
        self.assertIn('"beta" (task, draft', ctx)

    def test_terminals_silent(self):
        # one per terminal of the family state machine (№11)
        d = tempfile.mkdtemp()
        _spec(d, "t-done", "done")
        _spec(d, "t-drop", "abandoned")
        _artifact(d, "b-decided", "BRIEF.md", "decided")
        _artifact(d, "p-drop", "PLAN.md", "abandoned")
        _artifact(d, "d-root", "DEBUG.md", "root-found")
        _artifact(d, "d-dead", "DEBUG.md", "dead-end")
        self.assertEqual(_ctx(_run(d)), "")

    def test_pushes_brief_draft_with_pulse(self):
        d = tempfile.mkdtemp()
        _artifact(d, "auth-approach", "BRIEF.md", "draft",
                  body_extra="## Log\nDecided: use SSE\nRemaining: fallback story\n")
        ctx = _ctx(_run(cwd=d))
        self.assertIn('"auth-approach" (brief, draft', ctx)
        self.assertIn("use SSE", ctx)              # the last pulse is the current spot
        self.assertIn("fallback story", ctx)

    def test_pushes_plan(self):
        d = tempfile.mkdtemp()
        _artifact(d, "big-rewrite", "PLAN.md", "in-progress",
                  body_extra="## Tasks\n- [x] t1\n- [ ] t2\n")
        ctx = _ctx(_run(cwd=d))
        self.assertIn('"big-rewrite" (plan, in-progress', ctx)
        self.assertIn("t2", ctx)

    def test_pushes_debug_with_last_hypothesis(self):
        d = tempfile.mkdtemp()
        _artifact(d, "flaky-x", "DEBUG.md", "in-progress",
                  body_extra="## Hypotheses\n| # | H | P | E | V |\n|---|---|---|---|---|\n"
                             "| 1 | cache | a | b | rejected |\n| 2 | race | c | d | open |\n")
        ctx = _ctx(_run(cwd=d))
        self.assertIn('"flaky-x" (debug, in-progress', ctx)
        self.assertIn("race", ctx)                 # the LAST table row, not the first
        self.assertNotIn("cache", ctx)

    def test_review_draft_pushed_done_silent(self):
        # the compact-tripwire draft report (№12/№8) must resurface; a done report must not
        d = tempfile.mkdtemp()
        _review(d, "2026-07-23-auth.md", "draft")
        _review(d, "2026-07-01-old.md", "done")
        ctx = _ctx(_run(cwd=d))
        self.assertIn('"2026-07-23-auth" (review, draft', ctx)
        self.assertNotIn("2026-07-01-old", ctx)

    def test_fyi_grammar_present(self):
        # the line must not hijack an unrelated session: advisory, with an explicit "otherwise"
        d = tempfile.mkdtemp()
        _spec(d, "foo", "in-progress")
        ctx = _ctx(_run(d))
        self.assertIn("Otherwise continue the user's current request", ctx)
        self.assertIn("advisory", ctx)

    def test_mixed_artifacts_all_listed(self):
        d = tempfile.mkdtemp()
        _spec(d, "task-a", "in-progress")
        _artifact(d, "brief-b", "BRIEF.md", "draft")
        _artifact(d, "plan-c", "PLAN.md", "in-progress")
        _artifact(d, "debug-d", "DEBUG.md", "in-progress")
        ctx = _ctx(_run(cwd=d))
        for s in ("task-a", "brief-b", "plan-c", "debug-d"):
            self.assertIn(s, ctx)

    def test_silent_when_no_crafts_dir(self):
        d = tempfile.mkdtemp()
        self.assertEqual(_ctx(_run(d)), "")

    def test_silent_on_malformed_stdin(self):
        self.assertEqual(_ctx(_run(raw="not json{")), "")

    def test_failopen_json_not_object(self):
        # valid JSON, but not an object: data.get must not crash the hook
        self.assertEqual(_ctx(_run(raw="[1, 2, 3]")), "")

    def test_failopen_non_utf8_spec(self):
        # a spec with bytes that aren't valid UTF-8 — skip silently, don't crash
        d = tempfile.mkdtemp()
        craft = os.path.join(d, "docs", "crafts", "bad")
        os.makedirs(craft)
        with open(os.path.join(craft, "SPEC.md"), "wb") as f:
            f.write(b"# SPEC: bad\n\nStatus: in-progress\nMode: M\nBranch: task/x\n\n## Checklist\n- [ ] \xff\xfe\n")
        self.assertEqual(_ctx(_run(cwd=d)), "")

    def test_all_boxes_closed_still_pushes_spec(self):
        # an in-progress spec with no unchecked items — rare but valid (right before wrap)
        d = tempfile.mkdtemp()
        _spec(d, "tail", "in-progress", boxes=("- [x] one", "- [x] two"))
        self.assertIn("tail", _ctx(_run(d)))

    def test_long_item_truncated(self):
        d = tempfile.mkdtemp()
        _spec(d, "big", "in-progress", boxes=("- [ ] " + "x" * 500,))
        ctx = _ctx(_run(d))
        # the item is cut to ITEM_LIMIT; the fixed FYI tail is longer than the old one, hence 900
        self.assertLess(len(ctx), 900)


if __name__ == "__main__":
    unittest.main()
