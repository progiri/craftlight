# description-cap-cuts-redundancy: a description is cut by dropping redundancy, never a distinct trigger

Status: active
Type: gotcha
Area: core
Source: wave-release
Proof: `.github/workflows/validate.yml:46-60` <!-- the cap itself; a cut surface — `plugins/craftlight/skills/brief/SKILL.md:3` -->

## Gist
CI caps every skill `description` at 1024 characters. A cut must take redundancy — a clause the preceding one
already routes, an aside the skill body still states, a synonym of a trigger that stays — and never a distinct
trigger phrase or negative clause. The description-only regression scenarios pin what has to survive verbatim.

## Why
The description is the routing surface: it is what decides the skill fires at all, and it is loaded in every
context whether or not the skill runs. So a phrase deleted to buy characters is routing lost *silently* —
nothing goes red, no test fails, and the loss shows up only as a wrong skill firing later. Rejected: raising
the cap (it is the platform's constraint, not the repo's) and trimming by feel — three corpora quote
description text verbatim (brief 1/2/3/8, craft-graph 10/17, debug 7/12), and a felt-safe cut drifts them
without a signal. The check that actually guards a cut is narrow and exact: does the shortened description
still contain every fragment its own description-only scenarios quote?

## Risks
Cutting a trigger costs recall; cutting a negative clause costs precision — the skill fires where it should
have declined. Neither has a red test, so both are found by a user, not by CI.

## Edges
- part-of [[l-cap-executor-detail]] <!-- the same cap-with-a-cut-priority shape: the budget stays and the priority protects what the consumer actually runs on — there a subagent's file paths and contracts, here the router's triggers -->
