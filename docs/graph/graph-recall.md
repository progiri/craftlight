# graph-recall: the graph is read before a decision

Type: invariant
Area: core
Proof: `plugins/craftlight/skills/brief/SKILL.md:36`

## Gist
Recon at every decision point starts with the graph on the topic (`docs/graph/_overview.md` +
a grep of slugs/aliases): the brief's position (`plugins/craftlight/skills/brief/SKILL.md:36`), the
plan's landscape (`plugins/craftlight/skills/plan/SKILL.md:33`), the M/L brief in task — nodes into
the spec's "Constraints" (`plugins/craftlight/skills/task/modes/m.md:7`). A found node is cited
as proof; a proposal that goes against a node is named explicitly ("contradicts [[<slug>]], because …") —
a conscious revision, not a silent bypass. Recall only reads: the write path into the graph doesn't change.

## Rationale
A graph written at wrap but not read at the start is a graveyard, not a memory: the loop was left
open, the decided got re-decided, known gotchas recurred. Reading costs one glance at the overview
and a grep — cheaper than any repeat discussion ("already decided" saves a whole brief round).
The idea is mempalace-recall (GSD), without its state machinery: we read the same markdown nodes we write.
Rejected: recall as a separate step/ritual — ceremony where a line in the existing recon suffices;
an automatic index/search — runtime, against the plugin's DNA.

## Risks
Skipping recall → re-deciding what's recorded and repeating gotchas, the graph's value zeroes out
(why write what no one reads). A silent decision against a node → two conflicting "why"s in the repo,
trust in the graph falls.

## Edges
- affects [[craft-map-decisions-in-graph]]
- depends-on [[graph-proof-required]]
