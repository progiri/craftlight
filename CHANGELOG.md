# Changelog

All notable changes to the `craftlight` plugin. The format is [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
versioning is [SemVer](https://semver.org/). The version is stored in
`plugins/craftlight/.claude-plugin/plugin.json`.

## [Unreleased]

## [0.12.0]
A full prompt-by-prompt review of the corpus (12 passes: 6 skills + modes, the template family, the hooks),
each pass critiqued externally, fixed, and regression-run; closed with a single 166-run sweep of all six
scenario sets against the finished corpus — 165 PASS, 1 recorded divergence (below).
### Changed
- task router: lazy CLAUDE.md-block upsert (post-gate; a call that never writes touches nothing) — the same
  invariant ported to every skill; non-blocking resume everywhere (a new task/topic/bug gets an FYI line, a
  bare trigger resumes); the confirmation gate made mechanical ("showing the plan ends the turn") with strict
  advance-ok equivalents (urgency ≠ waiver); the risk zone got its own anchored section (secrets/PII/external
  contracts added, concurrency narrowed to sync primitives/shared-state invariants) with the CLAUDE-block line
  as the always-in-context copy; three shared policies (tests, verification honesty, no-guess-and-patch with a
  counter-based debug handoff) hoisted into router global rules; description triggers narrowed + negative
  clauses; "several independent deliverables → offer plan".
- S playbook: the S question test (one closed line-answer question rides the gate), durable lessons →
  `graph-candidate` backlog breadcrumbs instead of forced escalation, own-files tidying ban, TDD escape hatch,
  scoped tests/lint, a 2–4-line closing report.
- M playbook: de-escalation re-sequenced before the status flip, post-ok assumption tags surfaced at wrap, an
  "Entering from escalation" section, the parent-artifact hook (BRIEF/PLAN → spec Constraints, wrap ticks the
  PLAN leaf), wrap loop closed (fix → re-run), self-review named biased with an independent code-review offer,
  PR proposed-not-created, the backlog graph-candidate sweep with breadcrumb consumption.
- L playbook: checkpoints became commit + end-turn (no self-compact), a delegation protocol (worktree/branch
  conventions, subagents never touch SPEC.md, a verbatim rule distillate incl. the risk-zone stop), predictive
  + tripwire subagent triggers, L→M de-escalation (both sides), wrap deltas (contract reconciliation, cleanup).
- plan: the leaf hook closes the hand-off loop, PLAN git fate defined, convergence-per-turn with text sketches,
  gate turn mechanics + fragment enthusiasm ≠ approval, scoped reconciliation, sub-initiative successor line.
- brief: the commit skeleton precedes the gate, recon greps prior BRIEF verdicts (the no-go read path), a
  "what did we decide" read path, self-consistency rule (new facts beat your own stance), convergence proposes
  the commit, duty-to-push-back allows reasoned conceptual arguments, git fate, edit-vs-new-brief rule.
- debug: the boundary made fix-shaped (diagnostic edits allowed, instrumentation stripped, the repro test
  handed to task), a side-effect experiment gate, counter independence from task, both return paths designed,
  durable roots leave graph-candidate breadcrumbs, predictive DEBUG.md escalation, bisect hygiene.
- code-review: proof symmetry for refutations (disputed ≠ hypothesis), untracked files in the default object,
  the graph + brief verdicts joined Full prep (a violated node ≥ Major; the conformance lens sets `verify`),
  the Express→Full escalation delta spelled out, suggestion noise capped, report git fate + snapshot semantics.
- craft-graph: a grep-visible node `Status` (active/superseded/verify) making supersedes and staleness
  executable with named setters/clearers and consumer filters everywhere, breadcrumb consumption (`→ [[slug]]`),
  the "Unplaced" overview queue, checkpoint commits + derivable resume, Explore packs carry existing slugs.
- Templates: behavior evicted to playbooks (form only, "playbook wins", write-time comments, read-compatible
  edits), caps + cut-priorities single-homed in templates, the family status machine unified
  (draft = gate not passed; abandoned everywhere resumable; REVIEW got draft|done), NODE gained
  Status/Source/edge semantics, the `⚠` glyph replaced with ASCII `verify`, CONTEXT.md got a reader and a
  pinned root path, BACKLOG authorship widened to any skill's foreign-finding rule.
- Hooks: session_state pushes draft artifacts with per-status semantics (a draft resumes at its gate, never
  into execution), FYI grammar (no session hijack), per-type current-spot extractors, and scans review drafts;
  gate_nudge gained "the ok is a user message, not an inference", documented blind spots, and a
  MultiEdit matcher; the CLAUDE block bumped v8→v10 (risk-zone line as canon, draft-aware resume line,
  hook-provenance line). Hook tests 26 → 30, all green.
### Known
- code-review sc.18p2 (a hypothesis-major reducing to verdict "ok") diverges under current sonnet reads after
  three wording iterations — recorded in the scenario set as an open maintainer decision.
### Added
- SECURITY.md — private vulnerability reporting via GitHub plus the hooks' security model
  (advisory-only, fail-open, stdlib-only, no network, read-only on `docs/crafts/*`) — and
  CODE_OF_CONDUCT.md (Contributor Covenant 2.1, contact via GitHub).
### Changed
- plan: the Step 1 gate tightened — an impatient "just give me the tree/waves now" is not the
  "(or equivalent)" approval; it means converge the discussion faster and still get the explicit ok
  on the decomposition.
- Manifests: the contact email removed from the marketplace `owner` and plugin `author` — contact
  goes through GitHub; both manifests pass `claude plugin validate` without it.

## [0.10.0]

### Added
- The domain glossary `CONTEXT.md` (brief `docs/crafts/context-vocab/`): the project's shared language as a
  separate root file — cross-agent markdown "**term** — meaning", readable by any agent without craftlight.
  The `task/templates/CONTEXT.md` template (the selection criterion is in the header), replenishment at M/L
  wrap ("a term was born or settled → a line"), a pointer from the map template. A deliberate revision of the
  `craft-map-decisions-in-graph` node — the exception is documented. Regression scenario 32 (red→green).
  Self-application: the discipline's glossary in the repo root (13 terms).
- brief: depth-first traversal of branches — a round's questions come from a single discussion branch, the
  next opens after the current one is closed, a neighboring one is parked in the pulse's "Remaining". Tuned
  to a cadence of 2–3 questions per round; regression scenario 13 (red→green).
### Changed
- CLAUDE block raised to v7: the project-understanding line was extended with the glossary — "the project's
  glossary — the root `CONTEXT.md`: use its terms in speech, code, and artifacts".

## [0.9.0]
The "lifecycle" batch: the lifecycle of the discipline artifacts was brought up to the resume promises
(following the full review `docs/reviews/2026-07-20-plugin-full-audit.md`, findings V2–V7).
### Added
- debug got "Step 0. Orientation and resume": the craftlight block upsert (now all six skills do it) + a
  search for an in-progress `DEBUG.md` with an offer to continue; in the description — resume triggers
  ("let's continue debugging", "back to the bug", "resume debugging").
- plan got external memory before the gate (a draft provision when wrapping up a discussion, as in brief)
  and a definite closure: step 0 resumes by state (no DAG → discussion; unclosed waves → show the wave; all
  leaves done → offer to close the plan as `done`).
- Hook C pushes all four discipline artifacts `{BRIEF,SPEC,PLAN,DEBUG}` (previously — only `SPEC`), aligned
  with the block.
### Changed
- CLAUDE block raised to v6: the resume line declares `{BRIEF,SPEC,PLAN,DEBUG}`; brief and debug were added
  to the list of referring skills.
- task: the spec's `draft` status stopped being an orphan — step 0 offers to resume the approval or delete
  the draft; the M→S de-escalation deletes the written draft; the status enum gained `abandoned`.
### Fixed
- Hooks: fail-open became a property of the code (`main()` in try/except → exit 0) — a non-UTF-8 spec and a
  valid non-object JSON no longer crash the hook with a traceback; the hook tests assert the returncode and
  an empty stderr (previously they were blind to crashes). Finding V2 of the full review.

## [0.8.2]
### Added
- craft-graph onboarding triggers ("adopt craftlight", "onboard the project into craftlight", "seed the
  graph over the legacy", "onboard this project into craftlight") — discoverability of adoption in an
  existing project without a commands/ layer (brief `docs/crafts/commands-layer/` — verdict "no commands").
  The "Adopting in an existing project" section in the README.
### Fixed
- craft-graph description: a ": " in the added tail broke strict YAML (the CI lint) — replaced with a dash;
  the CHANGELOG entries 0.8.1/0.8.2, missed during the release commits (found by the full review,
  `docs/reviews/2026-07-20-plugin-full-audit.md`, B1/B2).

## [0.8.1]
### Added
- The "What it is" section first in the `CRAFT.md` template — a project description (product, the point, for
  whom, boundaries, approach; a guideline of 5–15 lines) lives in the map, a separate PROJECT.md isn't needed
  (brief `docs/crafts/project-context/`). CRAFT.md cap ~50→~65 lines; the bootstrap in task/SKILL.md was
  aligned; regression scenario 29.

## [0.8.0]
### Added
- Hook C (SessionStart/`compact|resume`) — push-based recovery of the discipline's state: after a context
  compaction or resume, the in-progress specs (slug, mode, branch, the first unchecked item) come into
  context on their own via `additionalContext`, without waiting for the model to go and grep them. It strikes
  the root cause (context degradation), not its consequences.
### Removed
- Hook A (a PreToolUse block on `git commit` to the default branch) — removed after review: the bypass
  instruction sat in the deny message itself (a self-serve override — the model could set
  `CRAFTLIGHT_ALLOW_MAIN=1` without the user's ok), plus a false deny on the compound
  `git checkout -b … && git commit`. The direction of the hooks is advisory-only: return rules and state to
  the context, block nothing. The env variables `CRAFTLIGHT_ALLOW_MAIN` / `CRAFTLIGHT_GUARD_BRANCH` no longer
  do anything.

## [0.7.0]
### Added
- Discipline enforcement hooks — the first craftlight plugin hooks (`plugins/craftlight/hooks/`), giving
  teeth to two mechanical rules where the prompt degrades under context pressure.
  - Hook A (PreToolUse/Bash) — a block on `git commit` to the default branch (main/master). Per-commit
    override: `CRAFTLIGHT_ALLOW_MAIN=1 git commit …` (parsed from the command text, since the hook isn't a
    child of bash); repo opt-out: `CRAFTLIGHT_GUARD_BRANCH=off` in the env. A guard, not a jail: any
    ambiguity (detached HEAD, `git -C`, a non-git repo) → fail-open.
  - Hook B (PostToolUse/Edit|Write) — an advisory nudge about the confirmation gate when product code is
    edited with an unclosed draft spec. Never blocks, self-quieting.
  - 21 fixture tests (python3 stdlib, `hooks/tests/`) — the repo's first real automated tests; run in CI.
    The design decision was made by the brief `docs/crafts/hooks-enforcement/`.

## [0.6.3]
### Fixed
- `debug`: a "task: " in the unquoted description broke the strict YAML frontmatter — found by
  `claude plugin validate`; the runtime is lenient for now, but a strict parser would silently drop the
  skill's auto-triggering. The class was closed by a CI check.
- `brief`: description 1053 → 1010 characters — within the Agent Skills spec limit (1024).
- `marketplace.json`: the marketplace description moved to `metadata.description` — the schema doesn't
  recognize a root key.
- Showcase: `debug` was added to the enumerations in CONTRIBUTING.md and the `.github/` templates (a tail of 0.6.0).
### Changed
- The six skills' descriptions: the tail "even if the words … aren't spoken" → "even without the words …"
  (total 5068 → 4962 characters); the trigger phrases were left untouched.
- Graph nodes: the proofs in the bodies of six nodes were brought to repo-root paths.
### Added
- CI: the official `claude plugin validate` (plugin and marketplace), the description limit ≤1024 and the
  ": " ban, the presence of `tests/scenarios.md` for each skill, the version sync with CHANGELOG, the graph
  lint (`[[wikilinks]]` resolve, overview ↔ nodes 1:1, proof paths exist).

## [0.6.2]
### Changed
- Recall: the graph loop is closed — decision recon starts from `docs/graph/` at all three points (`brief` a
  stance, `plan` the landscape, the `task` brief — nodes in the spec's "Constraints"); a proposal against an
  existing node is named explicitly ("contradicts [[slug]], because …"). Regression scenarios brief-12,
  plan-10, task-28.

## [0.6.1]
### Added
- The backlog sink `docs/crafts/_backlog.md` — a channel for "noticed along the way": the scope-creep ban
  got a sink (one line per entry; a sink, not a tracker — triage is the human's job). Written by `task` (all
  modes; wrap pours unresolved "while we're at it" ideas from "Open questions") and `debug`; the
  `task/templates/BACKLOG.md` template. Regression scenarios 25–27.

## [0.6.0]
### Added
- The sixth skill **`debug`** — a systematic hunt for the root cause without editing code: the protocol
  (repro → reading the error in full → checking the obvious → a hypothesis with a testable prediction → a
  minimal experiment → the root, not the symptom), a log of rejected hypotheses (a drawn-out case —
  `docs/crafts/<slug>/DEBUG.md`), stop rules. The diagnosis goes back to `task` — debug doesn't fix.
### Changed
- CLAUDE block v5: the no-guess-and-patch line leads to the `debug` skill.
- `task`'s stop rules (S and M) point to `debug` for a drawn-out root hunt.

## [0.5.1]
### Changed
- `task`: verification before "done" — the M wrap opens with the principle "done = an observed result, not
  'code written'"; "should work" is a forbidden phrasing, the unverified is flagged explicitly ("didn't
  verify …"). In S the "Verify" step requires seeing the effect of the change and an honest report.
  Regression scenarios 23–24.

## [0.5.0]
### Added
- The fifth skill **`brief`** — working out a decision by dialogue before any task: options with trade-offs,
  the verdict go / no-go / deferred, `BRIEF.md` only after an explicit "ok, commit it", a hand-off to `task`
  or `plan`. The discipline ladder `brief → plan → task`.

## [0.4.3]
### Added
- The confirmation gate in `task`: execution only after an explicit user ok on the plan.

## [0.4.2]
### Added
- `craft-graph`: the **Area** facet in nodes, the "core" area, and slug aliases (scenarios 9/9 PASS).

## [0.4.1]
### Changed
- `plan`: the `PLAN.md` cap raised 120 → 180 lines.

## [0.4.0]
### Added
- The **`plan`** skill — the planner above `task`: initiative → task DAG → execution waves.
- Wiring into the discipline: the CLAUDE.md craftlight block v3, a pointer from `task`.

## [0.3.1]
### Changed
- `task`: the `SPEC.md` cap by mode (M ≤ 80 / L ≤ 140 lines); the Log and Outcome don't count.

## [0.3.0]
### Added
- `CLAUDE.md` self-maintenance: a description of the managed block in the README.

## [0.2.0]
### Added
- The **`craft-graph`** skill — documenting decisions and gotchas as a graph.
- `keywords` in the marketplace and plugin manifests.

## [0.1.0]
### Added
- The plugin's base: the skills **`task`** (the S/M/L router + owner of `CRAFT.md`) and **`code-review`** (review without edits).

[Unreleased]: https://github.com/progiri/craftlight/compare/v0.11.0...HEAD
[0.11.0]: https://github.com/progiri/craftlight/releases/tag/v0.11.0
[0.10.0]: https://github.com/progiri/craftlight/releases/tag/v0.10.0
[0.9.0]: https://github.com/progiri/craftlight/releases/tag/v0.9.0
[0.8.2]: https://github.com/progiri/craftlight/releases/tag/v0.8.2
[0.8.1]: https://github.com/progiri/craftlight/releases/tag/v0.8.1
[0.8.0]: https://github.com/progiri/craftlight/releases/tag/v0.8.0
[0.7.0]: https://github.com/progiri/craftlight/releases/tag/v0.7.0
[0.6.3]: https://github.com/progiri/craftlight/releases/tag/v0.6.3
[0.6.2]: https://github.com/progiri/craftlight/releases/tag/v0.6.2
[0.6.1]: https://github.com/progiri/craftlight/releases/tag/v0.6.1
[0.6.0]: https://github.com/progiri/craftlight/releases/tag/v0.6.0
[0.5.1]: https://github.com/progiri/craftlight/releases/tag/v0.5.1
[0.5.0]: https://github.com/progiri/craftlight/releases/tag/v0.5.0
[0.4.3]: https://github.com/progiri/craftlight/releases/tag/v0.4.3
[0.4.2]: https://github.com/progiri/craftlight/releases/tag/v0.4.2
[0.4.1]: https://github.com/progiri/craftlight/releases/tag/v0.4.1
[0.4.0]: https://github.com/progiri/craftlight/releases/tag/v0.4.0
[0.3.1]: https://github.com/progiri/craftlight/releases/tag/v0.3.1
[0.3.0]: https://github.com/progiri/craftlight/releases/tag/v0.3.0
[0.2.0]: https://github.com/progiri/craftlight/releases/tag/v0.2.0
[0.1.0]: https://github.com/progiri/craftlight/releases/tag/v0.1.0
