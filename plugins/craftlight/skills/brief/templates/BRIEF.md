<!-- Form only: sections, field enums, formats, cap. Behavior (the commit gate, discussion, hand-off) lives in
     brief/SKILL.md — on conflict the playbook wins. These comments are write-time guidance, NOT copied into the
     artifact (inline enums excepted). Template edits stay read-compatible. -->
# BRIEF: <decision title>

Status: draft <!-- draft | decided | abandoned. Family enum: draft = commit gate ("ok, commit it") not passed
     (a saved unfinished discussion); decided = the decision is fixed; abandoned = dropped on explicit request.
     No `in-progress` — brief goes draft → decided, there is no post-gate "work" phase. -->
Verdict: — <!-- go | no-go | deferred; filled in at status decided -->

## Context
<!-- 3–5 lines: where the question came from, what already exists. No more. -->

## Question
<!-- 1–2 lines: what exactly we're deciding. A good question admits a "no-go" answer. -->

## Options and trade-offs
<!-- ALL discussed options, including the rejected ones and WHAT rejected them — the most valuable section.
     For each: the gist, pros, cons, verdict (chosen: why / rejected: by what). -->
- **A: <option>** — pros: …; cons: …; rejected: <by what> / chosen: <why>
-

## Decision
<!-- One paragraph: what was decided and why — a conclusion, not a retelling of the discussion. -->

## Assumptions
<!-- Reasonable assumptions adopted in the discussion instead of questions. -->
-

## Non-goals
<!-- What is deliberately outside the decision. An anchor against scope creep at hand-off. -->
-

## Success criteria
<!-- 2–4 verifiable statements: how we'll know the decision was right — in system/user terms. -->
-

## Open questions
<!-- What remains unresolved and why it doesn't block the verdict. -->
-

## Log
<!-- For a draft: the last pulse "Decided: … / Remaining: …" + a paragraph on the discussion — enough to resume.
     For decided, usually empty. -->

## Spawned
<!-- After hand-off: links to docs/crafts/<slug>/SPEC.md or PLAN.md. With a "no-go" verdict — empty. -->
-

<!-- File form: cap ≤150 lines (the Log doesn't count); hitting it → cut prose, NEVER the rejected options (the
     most valuable section). Lives in docs/crafts/<slug>/BRIEF.md (a folder per craft: BRIEF, then SPEC or PLAN,
     side by side). After decided it stays in place, only "Spawned" is appended. -->
