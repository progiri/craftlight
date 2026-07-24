# block-version-own: the block version is its own, not the plugin version

Type: decision
Area: claude-block
Proof: `plugins/craftlight/skills/task/templates/CLAUDE-block.md:32`

## Gist
The block version is incremented only when the block text changes, not on every plugin bump (currently `v8`).

## Rationale
Otherwise every plugin update would rewrite CLAUDE.md for all users without a substantive reason — needless noise in their working tree.

## Risks
Tying the block version to the plugin version → mass no-op edits to CLAUDE.md on every release.

## Edges
- part-of [[claude-block-selfheal]]
