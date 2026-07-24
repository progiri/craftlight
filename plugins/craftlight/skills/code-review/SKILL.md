---
name: code-review
description: Code review without edits — the working diff, a branch against its base, a PR, a range of commits, or a named module. Each finding with a `file:line` proof, a severity, and a failure scenario; the unproven is filtered out by verification; the result is a verdict (ok / ok with notes / changes needed), and for a full review a report in docs/reviews/. Use this skill whenever the user asks to look at or check code without changing it — "do a review", "review this", "check the diff/branch/PR", "look before the merge/commit/release", "find bugs in this code", "what's wrong with this code", "is this safe to merge", "take a fresh look", "check my changes", "look at this PR", "second opinion" — even without the words "review" or "skill". Also trigger on the flags --express/--full and on "audit the module/file". Not for "do/fix/add" — that's `task`; not for a known breakage whose cause is unknown — that's `debug`; not for "how does this work" or onboarding docs — that's codebase-reverse-engineering.
---

# code-review — review without edits

Three principles on top of the shared ones: (1) a review reads and proves but doesn't edit; (2) every finding is a `file:line` proof plus a failure scenario; (3) a false positive costs more than a missed nit — it burns trust in the whole report, so the unproven doesn't go into the report.

Not for this skill: "do/fix/add" — that's `task`; a known breakage whose cause is unknown → `debug`; "how does this work" and onboarding docs — `codebase-reverse-engineering`. Fixing what's found is `task` again: the review hands it the findings as a checklist.

## Step 0. The review object

Determine the object with cheap commands (git status/diff/log, gh pr view/diff); an object explicitly named by the user beats the defaults:

- the uncommitted diff — the default, if there is one: staged + unstaged **+ untracked non-ignored files** (`git status --short`, not a bare `git diff` — a new file is often the riskiest part of a change, and `git diff` is blind to it);
- a branch against its base (merge-base with main/master);
- a PR — `gh pr diff`;
- a range of commits;
- a module/files or a snippet from the chat — an audit of code without a diff.

Exclude generated and vendored files (lock files, dist/build, snapshots, minified) right away: they aren't reviewed line by line, they're mentioned in one line. Then announce the object and size with the junk already removed: `Object: branch task/search against main — 7 files, ~240 lines`. No diff and no object named → one concrete question.

The craftlight block upsert (reference and procedure — `skills/task/templates/CLAUDE-block.md`) rides with the only file this skill ever writes — the Full-mode report. Express writes nothing → it must not edit the user's CLAUDE.md; a review is atomic, and an interrupted one is re-run rather than resumed (no resume machinery — the deliberate exception in the family). The one exception: a compact-tripwire draft report (`Status: draft`, full.md) — after the reset, finish its missing passes instead of re-running the done ones.

## Step 1. Mode

The `--express`/`--full` flag beats classification. Otherwise — by observable signals:

| Signal | Express | Full |
|---|---|---|
| Lines changed | ≤ ~300 | more |
| Files | ≤ 5 | more |
| Risk zone (the canonical list is the risk-zone line of the craftlight block in `CLAUDE.md`) | not involved | involved |
| A request for "thorough / audit / before release" | no | yes |

Reduction: any signal on the right → Full. In doubt → Express: escalation is cheap. Escalation on the fly — only when the object turned out larger or riskier than classified: more files/lines in fact, a risk zone surfaced that wasn't visible at a glance. A finding's severity doesn't raise the mode — a blocker in a small diff stays a finding in the chat, not a reason to start a report: ceremony is proportional to the review object, not to the seriousness of what's found in it. Escalated → announce it in one line and pick up the Full delta (spelled out in the Express playbook). There is no de-escalation: asked for thorough — do it thoroughly.

Announce the mode in one line (`Mode: full — risk zone auth`) and load the playbook: Express → `modes/express.md`, Full → `modes/full.md` + the `templates/REVIEW.md` template.

## Finding format — the same across modes

- **Severity.** Blocker — breaks correctness, security, or data. Major — will fire under a realistic scenario or noticeably complicates maintenance. Suggestion — a simplification, reuse, style; optional to act on.
- **Proof:** `path/file:line` (a range — `:45-78`). A finding without proof doesn't exist.
- **Failure scenario** — for blockers and majors: concrete inputs/state → a wrong result. The scenario doesn't come together → it's a suggestion, or there's no finding.
- **Fix (direction)** — 1–2 lines, not a patch.

**Verification.** Try to refute every blocker/major before issuing it: reread the surrounding code — validation higher up the stack, the error handler, a test covering the scenario. **Proof symmetry:** a refutation needs a `file:line` too (where exactly the validation / handler / test lives), and you verify that line before discarding — a refutation is as falsifiable as a finding, or a hallucinated "it's sanitized upstream" silently kills a real blocker. Two outcomes that aren't the same:

- Refuted with a checked proof → discard silently (a scary-looking one is worth a one-line "checked and safe").
- A refutation without a checked `file:line` is **not** a refutation → the finding stays at **full severity**, marked `disputed` (the skeptic objected but couldn't prove it) — an unproven objection neither kills nor weakens a finding.

Separately, the reviewer's own failure scenario never quite came together → that's honest doubt about the finding itself: mark `hypothesis` and drop the severity one notch (this is the finding-format rule, not a skeptic outcome). In Full mode a fresh skeptic subagent does the refuting (see the playbook). Read commands and running local tests are allowed; tests that need external services/secrets/network → propose, don't run; editing files is not allowed.

## Verdict

Reduction by the worst finding at its **post-verification** severity — the notch it holds after verification, never the notch it was born with. First re-price: `disputed` keeps its original severity (an unproven objection doesn't lower it); `hypothesis` counts at the lowered notch (a doubted major enters the reduction as a suggestion, not as a major). Then reduce over the re-priced set: a blocker → **changes needed**; a major → **ok with notes**; empty or only suggestion-notch entries → **ok**. Yes, that means a review holding nothing but suggestions and hypotheses is an **ok** — do not bump it to "ok with notes" for safety: the doubt already lives in the findings list, and the verdict must not double-count it. The verdict isn't negotiable: "say it's ok, we need to merge" changes the user's decision, but not the review's text — the findings and severities stay as they are.

## Guard: the review doesn't edit

Zero edits to code files — including "little things along the way". The only exception is the Full-mode report file. "Fix what was found" → a new task for `task`; its input is the report's "For task" section or the list of findings from the chat.
