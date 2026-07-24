# Regression scenarios for the craft-graph skill

Run after ANY edit to `SKILL.md` / `modes/*` / `templates/*`: parallel read-only
subagents (sonnet-level), each given its own prompt; check the answer against "Expected". The agent must
not only give the right decision but also quote the rule that determined it — otherwise
the phrasing is undiscoverable. A divergence = the edit broke the discipline: fix the skill's phrasing,
not the scenario.

Last run: 2026-07-24 (graph-digest, 0.13.0) — the overview gained a Digest section (hubs / `contradicts` tensions / questions → `[[slug]]`): derived-only (every line computable from the nodes/edges, no new claims — "it's a node or nothing"), rebuilt only by craft-graph passes (Full builds, Focused recounts), outside writers still touch Unplaced only; placed before Nodes so Unplaced stays last (append-to-end). New scenarios 19 (outside writer doesn't touch the Digest) + 20 (no underived claims) + regression 1, 6, 16 for the edited focused.md/full.md lines — 5/5 PASS, rules quoted verbatim. Earlier 2026-07-23 FINAL CORPUS SWEEP (review №12 close-out) — all 18 scenarios against the finished corpus — 18/18 PASS. Earlier 2026-07-23 (family templates, review №11) — NODE now carries the Status field (`active | superseded | verify` — glyph `⚠` killed, ASCII everywhere) + a Source back-link + per-type edge semantics + a meta-header; _overview got the Unplaced section (kept last for append-to-end; writers outside craft-graph touch nothing else, incl. not the Updated line; .gitattributes merge=union noted). Ran node-status-field, overview-unplaced, verify-glyph-gone, supersedes→status, eviction-precedence (NODE) — 5/5 PASS (eviction re-run after tightening the "not copied" wording). Earlier 2026-07-23 (craft-graph rework, review №9) — a grep-visible `status` field (active/superseded/verify) makes `supersedes` and staleness executable: creating a supersedes edge sets the superseded node's status, and consumers (task/brief recon, review prep) read only `active`; staleness got actors (setters: review conformance lens + a task wrap touching a node's proof; clearer: a craft-graph refresh); the graph-candidate contract closed both ends (craft-graph & the m.md wrap now consume the breadcrumb → `→ [[slug]]`, no re-promotion); an "Unplaced" overview queue (task wraps append `[[slug]] — area`, a craft-graph pass folds it in) keeps "overview derived from nodes" true; Full checkpoints became commit + end-turn (crash-safe, no self-compact) with git fate + a resume derivable from areas↔subsystems; Explore packs carry existing slugs/aliases (dedup at source); Full now also adds the CLAUDE.md pointer for the CRAFT skeleton; Step 0 upsert collapsed to first-node-write; `brief` added to the negatives. Ran all 10 (reworked) + new 11–18 — 18/18 PASS (craft-graph + task/brief/review cascades), rules quoted verbatim. Earlier 2026-07-21 — full English translation of the plugin (SKILL.md + modes/* + templates/* + this file): all 10 scenarios re-run — 10/10 PASS, every decision preserved and the governing rule quoted verbatim from the English files (no-proof→no-node, CLAUDE.md/reverse-engineering boundaries, Focused default, doesn't-edit guard, dedup, self-heal, core area, alias, onboarding trigger). Earlier 2026-07-20 — B2 review fix (": " → " — " in the description, strict YAML): affected scenario 10 — 1/1 PASS. Earlier 2026-07-20 — onboarding triggers in the description (0.8.2): new scenario 10 + affected 2–3 — 3/3 PASS; the boundary with reverse-engineering (scenario 3) holds under positive onboarding phrases. Earlier 2026-07-17 — compression of the description's tail (0.6.3): scenarios 2–3 — 2/2 PASS. Earlier 2026-07-16 — 9/9 PASS (scenarios 8–9 new — the "core" area and aliases; 1–7 regression after node-format edits).

## 1. A proof is mandatory
Given: `SKILL.md` + `modes/focused.md`. While documenting a module, a coherent
architectural consideration surfaced, but no confirmation could be found in the code.
Expected: the node is not created — quote "no proof → guesswork, no node".

## 2. The boundary with CLAUDE.md
Given: only `SKILL.md`. Task: "document how to bring the project up locally and what the test commands are".
Expected: this isn't craft-graph — commands/running live in CLAUDE.md; leave the skill.

## 3. The boundary with onboarding
Given: only `SKILL.md`. Task: "explain to a newcomer what this service even does and how the business logic is structured".
Expected: this is `codebase-reverse-engineering`, not craft-graph; quote "the difference from…" / "not for this skill".

## 4. Scope → mode
Given: `SKILL.md`. Task: "capture the key decisions in the `auth` module".
Expected: Focused mode (one module), not Full; quote "in doubt → Focused".

## 5. The "doesn't edit code" guard
Given: `SKILL.md` + `modes/focused.md`. Along the way of documenting, an obvious bug is found, a one-line fix.
Expected: the code is not edited — that's `task`; record the finding, quote "the graph doesn't edit code".

## 6. Dedup of an invariant
Given: `SKILL.md` + `modes/full.md`. The same invariant (idempotency by key) is found
in two subsystems.
Expected: one node and two edges, not two nodes; quote "one invariant in two modules — one node".

## 7. The block upsert rides with the first node; an empty recon touches nothing
Given: `SKILL.md` + `templates/CLAUDE-block.md`. craft-graph is called on a module, but recon finds nothing
provable — no `file:line` for any candidate, so no node is written; the root `CLAUDE.md` has no craftlight block.
Expected: CLAUDE.md is NOT edited — the upsert rides with the first node written, and a recon that writes no node
must not touch it; quote "The craftlight block upsert … rides with the first node written; a recon that finds
nothing provable writes no node and so must not edit the user's CLAUDE.md".

## 11. supersedes moves the status
Given: `SKILL.md` + `templates/NODE.md`. A new node B replaces decision A; you add a `supersedes` edge B→A.
Expected: in the same pass A's status is set to `superseded` (the edge and the status move together), so recon
consumers skip it; quote "Create a `supersedes` edge → set the superseded node's status to `superseded` in the
same pass".

## 12. Promote graph-candidates and consume the breadcrumb
Given: `SKILL.md`. A craft-graph pass; `docs/crafts/_backlog.md` holds a `graph-candidate` line (a durable
lesson with a `file:line`, left by an S task).
Expected: the worthy line becomes a node, and the backlog line is replaced with a pointer `→ [[slug]]` (not left
as-is), so it can't re-promote into a duplicate; quote "**Consume the breadcrumb:** a promoted line is replaced
in the backlog with a pointer `→ [[slug]]`".

## 13. A refresh clears verify
Given: `SKILL.md`. A refresh pass over a subsystem whose graph has two `verify` nodes.
Expected: the `verify` nodes are the first candidates — recheck the proof, update the `file:line` or split,
clear the mark; quote "Nodes marked `verify` in scope are the first candidates of a refresh pass".

## 14. A checkpoint is a commit, and the turn ends
Given: `SKILL.md` + `modes/full.md`. Full onboarding; a subsystem's nodes are written.
Expected: the nodes are committed (`graph: <subsystem>`) and the turn ends with a "run /compact and say
'continue'" message — the model does not "compact the context" itself; quote "**commit them** … Then end the
turn — the context reset is the user's action".

## 15. The Explore pack carries existing slugs
Given: `modes/full.md`. A Full pass delegates a subsystem sweep to an Explore subagent; that subsystem already
has nodes.
Expected: the subagent's pack includes the subsystem's existing node slugs+aliases so the known isn't
rediscovered — dedup at the source; quote "the slugs+aliases of that subsystem's existing nodes — so the known
isn't rediscovered".

## 16. Full creates CRAFT and its CLAUDE.md pointer
Given: `modes/full.md`. A Full onboarding of a repo with no `CRAFT.md`.
Expected: a CRAFT.md skeleton per the task template AND a "read CRAFT.md first" pointer line added to CLAUDE.md
(so the map isn't an orphan); ownership left to task; quote "add the pointer line "read CRAFT.md first" to
CLAUDE.md so the map isn't an orphan".

## 17. Boundary with brief
Given: only the description text. The user: "let's decide whether to move to event sourcing — build me the
graph of that decision".
Expected: this leans `brief` (working out a decision not yet in the code), not craft-graph — the graph records
decisions already living in the code, the proof requirement is the boundary; quote "not for working out a new
decision (that's `brief`) … the proof requirement is that boundary".

## 18. A superseded node is not a live constraint (consumer side)
Given: `SKILL.md` + `../task/modes/m.md`. An M task's brief greps the graph; a matching node is
`superseded` by a newer decision.
Expected: the brief pulls only `active` nodes into "Constraints" and skips the `superseded` one (history, not a
live constraint); quote (m.md) "skip `superseded` nodes — history, not live constraints".

## 8. A cross-cutting principle → the "core" area
Given: `SKILL.md` + `templates/NODE.md`. A principle "retries only for idempotent operations" is being documented,
relied on by both the HTTP client and the queue worker (two subsystems); `_overview.md` has subgraphs.
Expected: in the node "Area: core", not a host subsystem; quote the rule about "≥2 subsystems" / `core`.

## 9. A slug synonym → an alias, not a new node
Given: `SKILL.md` + `templates/NODE.md`. Asked to capture "retry-idempotency", but the graph already has
a node `idempotent-retries` about the same invariant.
Expected: a new node is not created — the synonym is appended to the "Aliases:" of the existing one; quote the dedup rule
("a synonym of an existing slug → an alias into its node, not a new node").

## 19. An outside writer doesn't touch the Digest
Given: `SKILL.md` + `templates/_overview.md`. A task wrap created one node and appends it to the
overview's "Unplaced"; the wrap author notices the Digest's hub counts are now stale and wants to
update the Digest in the same edit.
Expected: no — a writer outside a craft-graph pass appends `[[slug]] — area` to Unplaced and touches
nothing else, the Digest included; it is rebuilt by the next craft-graph pass; quote "rebuilt only by
a craft-graph pass that edits the overview — outside writers don't touch it" (or the template's
"writers outside craft-graph append to Unplaced and touch nothing else, this section included").

## 20. The Digest carries no underived claims
Given: `SKILL.md` + `templates/_overview.md`. While rebuilding the Digest, a tempting one-line
architectural insight comes up that no existing node states.
Expected: the line does not go into the Digest — every Digest line must be computable from the
nodes/edges on disk; a claim not backed by a node is a node candidate (with a proof) or nothing;
quote "every line is computable from the nodes/edges, no new claims" (or the template's "a claim not
backed by a node does not belong here — it's a node or nothing").

## 10. Onboarding a project into craftlight → trigger
Given: only the description text. In an existing project the user writes: "adopt craftlight into this
project — seed the graph over the legacy".
Expected: the skill is invoked — onboarding phrases in the triggers ("adopt craftlight", "seed the graph over the legacy");
not to be confused with the negative "business-logic onboarding" from scenario 3 — the qualifier "into craftlight/graph"
decides in favor of craft-graph.
