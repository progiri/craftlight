# Full — lenses by subagents, verification by a skeptic, a report

## 1. Preparation: what we review against

Gather context surgically, without reading the whole repository, in order of value:

- **Spec:** `docs/crafts/*/SPEC.md` → the diff is checked against the acceptance criteria and the "Non-goals"; scope creep is a finding.
- **Graph:** there's a `docs/graph/` → grep `active` nodes by the diff's paths; a node whose `file:line` intersects the diff is a ready-made review checklist item — these are gate-passed, proof-carrying decisions, so a silent violation of one without a revision is at minimum a Major (stronger than the wiki: a node outranks a doc). The conformance lens is also the graph's staleness **setter**: a node whose proof points into the changed code → check it; the proof drifted (the decision moved, the node didn't) → a finding, and mark the node `verify`.
- **Wiki / reverse-engineering:** a `wiki/` (topics whose `code-paths` intersect the diff) or `docs/reverse-engineering/03-business-rules.md` (the invariants of the affected entities) → a documented decision or invariant is review material too.
- **Brief verdicts:** grep the verdict lines of `docs/crafts/*/BRIEF.md` by the diff's topic → a diff that implements a direction already recorded `no-go` is a rare but diamond finding.

Something of this is missing — skip it silently: don't ask the user where the spec is.

## 2. Lenses

All four lenses are mandatory; subagents are not:

- correctness and edge cases;
- security and risk zones;
- tests and testability;
- conformance to the spec/graph/wiki/invariants + diff hygiene.

The diff after excluding junk is small (≲ ~400 lines) → go through the lenses yourself, sequentially, each as a separate pass. The diff is large or the context is already tight → parallel read-only subagents, one lens each; give the subagent a context pack, not history: its chunk of the diff, the list of affected files, the relevant extracts from step 1, **the risk-zone line from the craftlight block** (the security lens needs the canonical list, a subagent has no context otherwise), and the finding format from SKILL.md (severity, `file:line` proof, failure scenario — free text is not accepted, send it back to redo). The diff is over ~1500 lines → split it among subagents by files/domains, not by adding lenses. Came here as an escalation from Express → run only the Full delta (Express playbook), not a re-review.

## 3. Verification by a skeptic

Merge duplicates: one `file:line` from different lenses is one finding, we don't verify it twice. Then the blockers/majors go to fresh skeptic subagents with the task to refute: "find in the code why this scenario won't happen" — batch by file (one file's findings to one skeptic: freshness is preserved, N subagents for 15 findings is not); give it the findings and their files, not the whole context. The point is a fresh eye: the skeptic didn't see the lens's reasoning and isn't invested. **Proof symmetry (SKILL.md):** a refutation is accepted only with its own `file:line`, and the main context checks that line before dropping the finding — an unproven "it's handled upstream" doesn't discard anything, the finding stays `disputed` at full severity. No subagents → refute yourself by the SKILL.md rule and mark the report "verification: without a skeptic". Refuted with a checked proof → out of the report. Not refuted → into the report plus a line on what the skeptic checked. `disputed` (unproven objection) keeps severity; `hypothesis` (the reviewer's own scenario never firmed up) drops a notch — the two are not the same.

## 4. Report and verdict

- Fill in `templates/REVIEW.md` → `docs/reviews/<date>-<slug>.md` (the cap and cut-priority are in that template — restating the diff means you overran it).
- **Git fate:** the report is a document → commit it to the default branch (`review: <slug>`); protected default → branch `review/<slug>` + PR. It's a snapshot: its `file:line` references are the state reviewed and go stale after the first fix — the report says so, it isn't kept in sync.
- To the chat: the object, the verdict (the reduction is in SKILL.md), the count of findings by severity, the blockers in full, a link to the report.
- The object is a PR and the user asked for comments in the PR → publish only after showing the report and an explicit "ok": nothing goes out silently.

## Stop rules

- A compact happened mid-review of a large diff → save the report draft now (`Status: draft`; findings so far + which lenses are done), before subagent results are lost; a review doesn't resume, but a half-finished large Full shouldn't evaporate either — the session hook resurfaces the draft after the reset.
- The diff is too big to survey (over ~3000 lines, unrelated topics mixed together) → propose splitting it by commits/topics. You can't split attention silently: review quality drops quietly.
- A lens with no findings is a valid result: write "nothing found" in "Looked at and clean", don't invent findings for the report's weight.
