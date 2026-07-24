# edge-vocab-closed: the edge vocabulary is closed and small — deliberately

Type: decision
Area: craft-graph
Aliases: typed-edges, edge-vocabulary
Proof: `plugins/craftlight/skills/craft-graph/SKILL.md:35`

## Gist
The graph's edges are exactly five types (`depends-on`, `affects`, `contradicts`, `supersedes`, `part-of`);
no new types are introduced.

## Rationale
The triangle "precision × expressiveness × cost": edge expressiveness is traded for cheap maintenance
and precise navigation. Rejected: arbitrary named edges — drift into an ontology, the cost of design and
consistency an order of magnitude higher (against "zero runtime" in the plugin's DNA); untyped edges — semantics
lost, drift into tag soup.

## Risks
Vocabulary growth → each new edge type makes reading the overview, dedup, and every future node costlier;
a jumble of types breaks the predictability of graph navigation.

## Edges
- part-of [[ceremony-proportional]]
- affects [[craft-map-decisions-in-graph]]
