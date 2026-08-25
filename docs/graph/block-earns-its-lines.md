# block-earns-its-lines: the CLAUDE block doesn't grow — a new line is paid for

Status: active
Type: invariant
Area: claude-block
Source: block-v11
Proof: `plugins/craftlight/skills/task/templates/CLAUDE-block.md:49-50`

## Gist
A routing line added between the markers is paid for by compressing another one: the marker-to-marker line
count stays where it was. The bump that added the `wave` route paid with the hooks bullet, 2 lines → 1.

## Why
Two independent reasons, and both have to hold. The block is auto-loaded into *every* context of *every*
adopter, so its length is a tax levied on all of them forever — and a version bump rewrites it in their
`CLAUDE.md` without asking ([[block-version-own]]), which is only fair if the text got better rather than
longer. Separately, the graph's `file:line` proofs ([[graph-proof-required]]) into this file — `:6`, `:13-22`,
`:46` — survive an edit only while the block's line count is stable; append and they all silently drift.

## Risks
Appending "just one more line" per skill → the block grows without bound, and every node proving into
`CLAUDE-block.md` needs re-anchoring or goes `verify` unnoticed.

## Edges
- part-of [[claude-block-selfheal]]
- depends-on [[graph-proof-required]]
- depends-on [[block-version-own]]
