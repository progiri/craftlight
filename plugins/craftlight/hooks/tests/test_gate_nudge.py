"""Fixture tests for hook B (gate_nudge): the advisory gate nudge on a draft spec.

Each test spins up a temporary project folder with docs/crafts/<slug>/SPEC.md,
feeds the hook JSON on stdin, and checks for the presence/absence of additionalContext.
Run: python3 -m unittest discover -s plugins/craftlight/hooks/tests
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
HOOK = os.path.join(os.path.dirname(HERE), "gate_nudge.py")


def _project(spec_status="draft", slug="foo"):
    """A project folder with one spec of the given status (or no spec, if None)."""
    d = tempfile.mkdtemp()
    if spec_status is not None:
        crafts = os.path.join(d, "docs", "crafts", slug)
        os.makedirs(crafts)
        with open(os.path.join(crafts, "SPEC.md"), "w", encoding="utf-8") as f:
            f.write(f"# SPEC: {slug}\n\nStatus: {spec_status}\nMode: M\n")
    return d


def _run(file_path=None, cwd=None, tool="Edit", raw=None):
    if raw is None:
        raw = json.dumps({"tool_name": tool, "cwd": cwd,
                          "tool_input": {"file_path": file_path}})
    p = subprocess.run([sys.executable, HOOK], input=raw,
                       capture_output=True, text=True)
    # fail-open — a property: any input → quiet exit 0 with no stderr (otherwise the test is red)
    assert p.returncode == 0, f"returncode={p.returncode}, stderr={p.stderr!r}"
    assert p.stderr == "", f"fail-open violated, stderr={p.stderr!r}"
    return p


def _nudge(p):
    out = p.stdout.strip()
    if not out:
        return ""
    try:
        j = json.loads(out)
    except json.JSONDecodeError:
        return ""
    return j.get("hookSpecificOutput", {}).get("additionalContext", "")


class GateNudge(unittest.TestCase):
    def test_nudge_on_product_edit_with_draft_spec(self):
        d = _project("draft")
        self.assertTrue(_nudge(_run(os.path.join(d, "src", "app.py"), d)))

    def test_nudge_mentions_slug(self):
        d = _project("draft", slug="hooks-enforcement")
        self.assertIn("hooks-enforcement",
                      _nudge(_run(os.path.join(d, "src", "app.py"), d)))

    def test_write_tool_also_nudges(self):
        d = _project("draft")
        self.assertTrue(_nudge(_run(os.path.join(d, "app.py"), d, tool="Write")))

    def test_silent_when_spec_in_progress(self):
        # self-quieting pinned by test: gate passed (in-progress) → the nudge goes silent
        d = _project("in-progress")
        self.assertFalse(_nudge(_run(os.path.join(d, "src", "app.py"), d)))

    def test_nudge_says_ok_is_a_user_message(self):
        # the anti-rationalization line: the model must not infer the ok it never received
        d = _project("draft")
        self.assertIn("not an inference",
                      _nudge(_run(os.path.join(d, "src", "app.py"), d)))

    def test_silent_when_no_spec(self):
        d = _project(None)
        self.assertFalse(_nudge(_run(os.path.join(d, "src", "app.py"), d)))

    def test_silent_when_editing_under_docs(self):
        d = _project("draft")
        self.assertFalse(_nudge(_run(os.path.join(d, "docs", "note.md"), d)))

    def test_silent_when_editing_the_spec_itself(self):
        d = _project("draft", slug="foo")
        spec = os.path.join(d, "docs", "crafts", "foo", "SPEC.md")
        self.assertFalse(_nudge(_run(spec, d)))

    def test_silent_when_file_outside_project(self):
        d = _project("draft")
        self.assertFalse(_nudge(_run("/tmp/elsewhere/x.py", d)))

    def test_failopen_malformed_stdin(self):
        self.assertFalse(_nudge(_run(raw="not json{")))

    def test_failopen_json_not_object(self):
        # valid JSON, but not an object: data.get must not crash the hook
        self.assertFalse(_nudge(_run(raw="[1, 2, 3]")))

    def test_failopen_missing_file_path(self):
        d = _project("draft")
        self.assertFalse(_nudge(_run(raw=json.dumps(
            {"tool_name": "Edit", "cwd": d, "tool_input": {}}))))

    def test_failopen_non_utf8_spec(self):
        # a draft spec with bytes that aren't valid UTF-8 — skip silently, don't crash
        d = tempfile.mkdtemp()
        craft = os.path.join(d, "docs", "crafts", "foo")
        os.makedirs(craft)
        with open(os.path.join(craft, "SPEC.md"), "wb") as f:
            f.write(b"# SPEC: foo\n\nStatus: draft\nMode: M\n\xff\xfe\n")
        self.assertFalse(_nudge(_run(os.path.join(d, "src", "app.py"), d)))


if __name__ == "__main__":
    unittest.main()
