# Decision graph: craftlight

Updated: 2026-08-25

<!-- An overview for those without Obsidian: the nodes themselves navigate by [[wikilinks]];
     here is Mermaid for reading on GitHub. Grouped by the nodes' areas (subgraph = "Area:", 1:1);
     "core" — cross-cutting principles (≥2 subsystems). -->

```mermaid
graph LR
  subgraph core
    ceremony[ceremony-proportional]
    gate[confirm-gate]
    ctx[context-pack-not-history]
    desccap[description-cap-cuts-redundancy]
    done[done-is-observed]
    recall[graph-recall]
    lcap[l-cap-executor-detail]
    guess[no-guess-and-patch]
    risk[risk-zone-min-m]
  end
  subgraph task-router
    backlog[backlog-sink]
    craftmap[craft-map-decisions-in-graph]
    speccrafts[spec-in-crafts]
    spec[spec-travels-with-branch]
    worst[worst-signal-wins]
  end
  subgraph code-review
    falsepos[false-positive-costlier]
    noedit[review-no-edits]
  end
  subgraph craft-graph
    areafacet[area-facet-in-node]
    digest[digest-derived-only]
    edgevocab[edge-vocab-closed]
    proof[graph-proof-required]
  end
  subgraph claude-block
    earns[block-earns-its-lines]
    blockann[block-insert-announced]
    ver[block-version-own]
    selfheal[claude-block-selfheal]
  end
  subgraph plan
    leafbranch[leaf-branch-not-pr]
    planabove[plan-above-task]
  end
  subgraph wave
    waveruns[wave-runs-plan-waves]
  end
  subgraph brief
    briefabove[brief-above-plan]
  end
  subgraph debug
    debuginside[debug-inside-task]
    loopfirst[feedback-loop-first]
  end
  subgraph hooks
    teeth[hooks-give-teeth]
  end
  areafacet -->|affects| craftmap
  backlog -->|part-of| ceremony
  backlog -->|affects| speccrafts
  earns -->|part-of| selfheal
  earns -->|depends-on| proof
  earns -->|depends-on| ver
  blockann -->|part-of| selfheal
  blockann -->|depends-on| ver
  ver -->|part-of| selfheal
  briefabove -->|part-of| ceremony
  briefabove -->|depends-on| gate
  briefabove -->|depends-on| planabove
  selfheal -->|depends-on| ver
  selfheal -->|affects| craftmap
  selfheal -->|affects| earns
  gate -->|affects| ceremony
  gate -->|depends-on| risk
  ctx -->|part-of| ceremony
  craftmap -->|depends-on| proof
  craftmap -->|affects| spec
  debuginside -->|part-of| ceremony
  debuginside -->|depends-on| guess
  desccap -->|part-of| lcap
  digest -->|part-of| areafacet
  digest -->|depends-on| proof
  done -->|part-of| ceremony
  edgevocab -->|part-of| ceremony
  edgevocab -->|affects| craftmap
  falsepos -->|affects| proof
  loopfirst -->|part-of| debuginside
  loopfirst -->|depends-on| guess
  proof -->|affects| craftmap
  recall -->|affects| craftmap
  recall -->|depends-on| proof
  teeth -->|affects| spec
  teeth -->|affects| gate
  teeth -->|depends-on| falsepos
  lcap -->|part-of| ceremony
  lcap -->|affects| ctx
  leafbranch -->|part-of| planabove
  leafbranch -->|depends-on| spec
  guess -->|part-of| ceremony
  planabove -->|part-of| ceremony
  planabove -->|affects| leafbranch
  planabove -->|depends-on| speccrafts
  planabove -->|depends-on| risk
  noedit -->|affects| falsepos
  risk -->|affects| ceremony
  risk -->|affects| worst
  speccrafts -->|affects| spec
  spec -->|part-of| ceremony
  spec -->|affects| craftmap
  waveruns -->|depends-on| planabove
  waveruns -->|depends-on| leafbranch
  waveruns -->|depends-on| gate
  waveruns -->|depends-on| risk
  waveruns -->|depends-on| ctx
  waveruns -->|affects| done
  worst -->|part-of| ceremony
```

## Digest
- **Hubs:** [[ceremony-proportional]] (13 edges — the root principle), [[craft-map-decisions-in-graph]] (8), [[plan-above-task]] (7)
- **Tensions:** none — the graph has no `contradicts` edges
- **Questions:** which mode does a one-line fix in auth get? → [[risk-zone-min-m]]; may execution start if the user stays silent on the shown plan? → [[confirm-gate]]; who runs a plan's wave, and what does its single gate cover? → [[wave-runs-plan-waves]]; when may a node be written without a `file:line` proof? → [[graph-proof-required]]

## Nodes
- [[ceremony-proportional]] — ceremony proportional to the task (the root principle)
- [[risk-zone-min-m]] — the risk zone → minimum M
- [[no-guess-and-patch]] — the ban on blind edits
- [[context-pack-not-history]] — a context pack for the subagent, not history (token-saving)
- [[confirm-gate]] — execution only after an explicit ok on the plan; an advance ok doesn't work in the risk zone
- [[done-is-observed]] — "done" = an observed result; "should work" is a forbidden phrasing
- [[graph-recall]] — the graph is read before a decision: brief/plan/task recon starts with it
- [[l-cap-executor-detail]] — L/PLAN caps protect the reader; the cut-priority protects executor detail
- [[description-cap-cuts-redundancy]] — a description is cut by dropping redundancy, never a distinct trigger
- [[worst-signal-wins]] — the mode by the worst observed signal
- [[spec-travels-with-branch]] — SPEC = a state tracker, travels with the branch
- [[spec-in-crafts]] — the spec lives in docs/crafts/<slug>/ (a folder per task)
- [[backlog-sink]] — banning scope creep requires a sink: something foreign along the way → a line in _backlog.md
- [[craft-map-decisions-in-graph]] — CRAFT is "What it is" + the map, decisions into the graph; no PROJECT.md needed
- [[review-no-edits]] — a review doesn't edit code
- [[false-positive-costlier]] — a false positive costs more than a miss
- [[graph-proof-required]] — a graph node without proof doesn't exist
- [[edge-vocab-closed]] — the edge vocabulary is closed (5 types): expressiveness traded for cheapness
- [[area-facet-in-node]] — area: a facet in the node itself, the overview is derived from the nodes (1:1)
- [[digest-derived-only]] — the overview Digest is derived from the nodes, no claims of its own
- [[claude-block-selfheal]] — self-maintenance of the block in CLAUDE.md
- [[block-version-own]] — the block version is its own, not the plugin version
- [[block-insert-announced]] — the first block insertion is announced, maintenance is silent
- [[block-earns-its-lines]] — the block doesn't grow: a new line is paid for by compressing another
- [[plan-above-task]] — plan sits above task: decomposing an initiative into a DAG and waves (plans, doesn't execute)
- [[leaf-branch-not-pr]] — a leaf is anchored on its branch, not on a PR (a wave lands as one PR)
- [[wave-runs-plan-waves]] — wave runs one wave of a PLAN: parallel leaves, one batched gate, one PR per run
- [[brief-above-plan]] — brief sits above plan: decision by dialogue before the task (discusses, doesn't execute)
- [[debug-inside-task]] — debug sits below task: a diagnostic subcycle (hunts for the root, doesn't fix)
- [[feedback-loop-first]] — debug's step 1 builds a red-capable loop; no loop → no hypotheses
- [[hooks-give-teeth]] — hooks return rules and state to the context (advisory-only: state-push + gate-nudge; fail-open)

## Unplaced
<!-- Empty: folded into the Mermaid and the node list by the 2026-08-25 craft-graph pass. -->
