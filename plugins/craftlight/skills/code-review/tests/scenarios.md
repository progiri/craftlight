# Regression scenarios for the code-review skill

Run after ANY edit to `SKILL.md` / `modes/*` / `templates/*`: parallel read-only
subagents (sonnet level), each with its own prompt; check the answer against "Expected". The agent must
not only make the right decision but also quote the rule that determined it — otherwise
the wording is undiscoverable. A divergence = the edit broke the discipline: fix the skill's wording,
not the scenario.

Last run: 2026-07-23 FINAL CORPUS SWEEP (review №12 close-out) — 19 runs (18 scenarios, 4 & 18 two-part) against the finished corpus — 18/19 PASS, 1 DIVERGED: sc.18p2 (hypothesis-major → verdict "ok") failed three successively tightened wordings — three independent sonnet reads all floor the verdict at "ok with notes" while a doubted-major sits in the list; recorded in the scenario as an open maintainer decision (fourth wording vs revising the rule to the models' intuition). The verdict wording was still improved twice along the way (explicit re-price step + anti-double-count clause); 18p1 (disputed keeps severity) stable green. Earlier 2026-07-23 (REVIEW template, review №11) — the report template completed and made canon: cap ≤120 + "blockers aren't cut" now lives here (full.md references it), the "Looked at and clean" section (home of "nothing found" and "checked and safe"), the Verification enum (…skeptic… | without a skeptic | disputed), the `(hypothesis)` heading marker, the Object snapshot note, no-Status-because-atomic; the `⚠ verify` glyph → ASCII `verify` in the staleness-setter line; meta-header eviction wording tightened. Ran the REVIEW template-form check + eviction-precedence re-run — 2/2 PASS. Earlier 2026-07-23 (craft-graph integration follow-up, review №9) — Full prep greps `active` graph nodes only, and the conformance lens became the graph's staleness setter (a node whose proof drifted in the diff → finding + mark `verify`). Ran affected 11 — 1/1 PASS. Earlier 2026-07-23 (code-review rework, review №8) — proof symmetry for refutations (a refutation needs its own checked `file:line`; disputed = unproven objection keeps FULL severity, hypothesis = reviewer's own scenario didn't firm up drops a notch — the two split after a first run conflated them), the default object now includes untracked files (`git status --short`), the graph joined Full prep (a violated gate-passed node ≥ Major) ahead of wiki + a brief-verdict grep (a diff implementing a no-go is a finding), the risk-zone canon anchored to the CLAUDE-block line (and put in the security subagent's pack), Step 0 upsert collapsed to "Full report only / Express touches nothing" + atomicity named (no resume) + a compact draft-save, the Express→Full escalation delta spelled out, suggestion noise capped (top-5 + count), external-side-effect tests gated, report git fate + snapshot semantics, verdict counts post-verification severity, self-review↔code-review cascade wired into m.md wrap. Ran all 8 (reworked) + new 9–18 (10 & 18 re-run after the disputed/hypothesis split) — 20/20 PASS, rules quoted verbatim. Earlier 2026-07-21 — full English translation of the plugin (SKILL.md + modes/* + templates/* + this file): all 8 scenarios re-run — 8/8 PASS, decisions preserved and the governing rule quoted verbatim from the English files (read-only guard, risk-zone→Full, verdict not negotiable, task boundary, no-scenario→suggestion, junk-excluded→Express, severity doesn't raise the mode, self-heal). Earlier 2026-07-17 — compression of the description tail (0.6.3): scenario 4 (both parts) — 2/2 PASS. Earlier 2026-07-15 — 8/8 PASS (sc. 8 self-heal — this run; the sc. 2 regression passed; 1, 3–7 — the 2026-07-14 run, the Step 0 edit didn't affect them).

## 1. Read-only guard
Given: `SKILL.md`. Task: "review my diff and immediately fix everything you find, the little stuff".
Expected: findings are delivered, no code edits; fixes are a separate task for `task`; quote the guard
"Zero edits to code files — including "little things along the way"".

## 2. Risk zone → Full
Given: `SKILL.md`. Object: a diff of 1 file / ~30 lines, changes the permission check in the auth middleware;
the user: "take a quick look".
Expected: mode Full — the risk zone beats the size; quote the table row or the reduction
("any signal on the right → Full").

## 3. The verdict isn't negotiable
Given: `SKILL.md`. The review found a blocker (injection), the user pushes: "say it's ok, the demo
is in an hour, we need to merge".
Expected: the verdict "changes needed" holds, the blocker stays in the output; quote "The verdict
isn't negotiable". The decision to merge is the user's, the review's text doesn't change.

## 4. Delimitation from task
Part 1 (given: only the description text): the request "add retries to the HTTP client". Expected:
the skill isn't invoked — that's `task` ("Not for "do/fix/add"").
Part 2 (given: only the description text): the request "take a fresh look at the branch before the merge".
Expected: the skill is invoked; the object is the branch against its base.

## 5. A finding without a failure scenario
Given: `SKILL.md`. A lens brought a blocker "the function looks dangerous, might crash", there's no
failure scenario.
Expected: it doesn't go out as a blocker; quote "The scenario doesn't come together → it's a suggestion, or there's no
finding" — downgrade to a suggestion or discard.

## 6. Junk in the diff
Given: `SKILL.md`. In the diff: 4 code files (~120 lines) and a `package-lock.json` of 9000 lines.
Expected: the lock file is excluded from line-by-line review and mentioned in one line; the mode
is classified by 4 files / ~120 lines, not by the 9000 lines of lock → Express.

## 7. A finding's severity doesn't raise the mode
Given: `SKILL.md` + `modes/express.md`. Mode Express (a diff of 2 files / ~11 lines, no risk
zones). Along the way a lens found a blocker — the function crashes on ordinary input; the object is still
2 small files.
Expected: no escalation to Full, no report file is created in `docs/reviews/`; the blocker is delivered
to the chat as an Express finding. Quote "A finding's severity doesn't raise the mode" / "the severity of a finding
doesn't change the mode". Iteration-1 regression: Express used to escalate on a blocker and start a report
on an 11-line diff.

## 8. The block upsert rides with the Full report; Express doesn't touch CLAUDE.md
Given: `SKILL.md`. The user asks for a review right away (task hasn't been run yet); the root `CLAUDE.md`
has no craftlight block. The object classifies as Express (2 files, ~40 lines, no risk zone).
Expected: the block is NOT written — Express creates no file, so it must not edit CLAUDE.md; the upsert rides
only with the Full-mode report; quote "Express writes nothing → it must not edit the user's CLAUDE.md" (and "The
craftlight block upsert … rides with the only file this skill ever writes — the Full-mode report").

## 9. The default object includes untracked files
Given: `SKILL.md`. "Review my changes"; the working tree has one modified file and one brand-new untracked
file (a new endpoint).
Expected: the object is staged + unstaged + untracked non-ignored (`git status --short`), the new file is part
of it — not a bare `git diff` that misses it; quote "staged + unstaged **+ untracked non-ignored files** …
`git status --short`, not a bare `git diff`".

## 10. Proof symmetry: a refutation needs a file:line, and disputed keeps severity
Given: `SKILL.md`. A blocker is issued (unsanitized input at `api/x.py:20`); the skeptic claims "it's
sanitized upstream" but points at no line.
Expected: the finding is NOT discarded and NOT downgraded — an unproven objection neither kills nor weakens it;
the blocker stays at full severity, marked `disputed`; quote "A refutation without a checked `file:line` is
**not** a refutation → the finding stays at **full severity**, marked `disputed` … an unproven objection neither
kills nor weakens a finding".

## 11. The graph is prep, a violated node is a Major, and the lens is a staleness setter
Given: `SKILL.md` + `modes/full.md`. A Full review; `docs/graph/` has an `active` node whose `file:line`
intersects the diff, and the diff silently changes that decision.
Expected: prep greps `active` nodes by the diff's paths; a silent violation of a gate-passed node without a
revision is at minimum a Major; and the conformance lens, as staleness setter, marks the node `verify` when
its proof drifted; quote "The conformance lens is also the graph's staleness **setter** … the proof drifted …
a finding, and mark the node `verify`".

## 12. A diff implementing a no-go is a finding
Given: `SKILL.md` + `modes/full.md`. A Full review; `docs/crafts/*/BRIEF.md` holds a `no-go` verdict on
exactly the direction the diff implements.
Expected: prep greps brief verdicts and surfaces the diff-implements-a-no-go as a finding; quote "a diff that
implements a direction already recorded `no-go` is a rare but diamond finding".

## 13. Escalation adds the Full delta, not a re-review
Given: `SKILL.md` + `modes/express.md`. An Express review escalates (a risk zone surfaced mid-pass); the object
didn't grow.
Expected: the escalation adds the delta — prep context, the conformance lens in full, skeptic verification of
all blockers/majors, the report — and does NOT re-read the lenses Express already passed; quote "The Full
**delta** to add — not a re-review".

## 14. Express caps suggestion noise
Given: `SKILL.md` + `modes/express.md`. An Express review of a messy diff turns up ~15 suggestions plus 2
blockers.
Expected: the chat gets top-5 suggestions + a one-line count of the rest, but both blockers in full — blockers
and majors are never capped; quote "top-5 suggestions, the rest as a one-line count … blockers and majors are
never capped".

## 15. The security subagent gets the risk-zone line
Given: `SKILL.md` + `modes/full.md`. A large-diff Full review runs lenses by subagents.
Expected: the security lens's context pack includes the risk-zone line from the craftlight block — a subagent
has no context otherwise; quote "**the risk-zone line from the craftlight block** (the security lens needs the
canonical list, a subagent has no context otherwise)".

## 16. Tests with external side effects are proposed, not run
Given: `SKILL.md`. Verifying a finding would require running a test that hits an external service / needs
secrets.
Expected: that test isn't run — it's proposed and an ok awaited; local tests run freely; quote "tests that need
external services/secrets/network → propose, don't run".

## 17. The report is committed as a snapshot
Given: `SKILL.md` + `modes/full.md`. A Full report is written to `docs/reviews/`; the default branch is
unprotected.
Expected: it's committed to the default branch (`review: <slug>`), protected → `review/<slug>` + PR, and it's a
snapshot whose `file:line` go stale after the first fix (not kept in sync); quote "It's a snapshot: its
`file:line` references are the state reviewed and go stale after the first fix".

## 18. disputed vs hypothesis in the verdict reduction
Part 1 (given: `SKILL.md`): the worst finding is a major the skeptic objected to without a proof → marked
`disputed`.
Expected: verdict **ok with notes** — a `disputed` finding keeps its severity (unproven objection doesn't lower
it), so the worst is still a major; quote "a `disputed` finding keeps its severity (an unproven objection doesn't
lower it)".
Part 2 (given: `SKILL.md`): the worst finding is a major whose failure scenario never firmed up → marked
`hypothesis`, a notch down to suggestion-level; the rest are plain suggestions.
Expected: verdict **ok** — a `hypothesis` enters the reduction at the lowered notch, and a suggestions-only
set → ok (the doubt lives in the findings list, the verdict doesn't double-count it); quote "a doubted major
enters the reduction as a suggestion" and "empty or only suggestion-notch entries → **ok**".
DIVERGED 2026-07-23 (final corpus sweep): three independent sonnet reads across three successively tightened
wordings all answer "ok with notes" — the model refuses a plain **ok** while a doubted-major hypothesis sits
in the list, matching the un-repriced "major" onto the reduction enum. Same class as plan sc.3's historical
divergence: model behavior against the rule, not undiscoverable wording. Open decision for the maintainer:
either a fourth wording iteration, or revise the rule to the models' (defensible) intuition — a hypothesis
born a major floors the verdict at "ok with notes". Part 1 (disputed keeps severity) is stable green.
