<!-- Form only: sections, the finding block shape, the cap and cut-priority. Behavior (verification, publishing,
     git fate) lives in code-review's playbooks — on conflict the playbook wins. These comments guide the write
     and are NOT copied into the report — only the inline enum values stay. Template edits stay read-compatible. -->
# Review: <object>

Status: done <!-- draft | done. No `in-progress` — a review is atomic; a `draft` exists only via the
     compact-tripwire save (full.md), and resurfacing after the reset is its whole purpose. -->
Date: <YYYY-MM-DD>
Verdict: <ok | ok with notes | changes needed>
Object: <branch X against Y / PR #N / diff — N files, ~M lines> <!-- a snapshot of the state reviewed: the file:line below go stale after the first fix -->
Excluded from review: <lock files, generated — or "nothing">

## Blockers
<!-- ### B1. <gist> — `file:line`   (append `(hypothesis)` to the heading if severity was lowered under doubt)
Failure scenario: <concrete inputs/state → wrong result>
Fix (direction): <1–2 lines>
Verification: <what the skeptic checked and why it didn't refute | without a skeptic | disputed (unproven objection, kept at full severity)> -->

## Major
<!-- ### M1. — same structure as a blocker -->

## Suggestions
<!-- one line + `file:line`; optional to act on -->
-

## Looked at and clean
<!-- lenses/zones with no findings: "nothing found" is a result, not emptiness.
     Also the home of "checked and safe: <finding> (refuted at `file:line`)" — a cleared scary-looking finding. -->
-

## For task
<!-- findings as a checklist in severity order — ready-made input for the task skill, if the user asks to fix -->
- [ ]

<!-- File form: cap ≤120 lines including markup; blockers aren't cut, suggestions are cut first; every finding
     with a `file:line` proof; saved to docs/reviews/<date>-<slug>.md -->
