# Express — one pass, zero artifacts

Everything in the main context, findings to the chat, no files created. The whole backstop is the order of lenses and the verification from SKILL.md.

## Order

1. **Read the whole diff — and the surroundings.** A diff without context lies: for every changed function look at its contract, its callers, and error handling in the file itself, not in the diff.
2. **One pass over the lenses**, in decreasing order of the cost of a mistake:
   - correctness: edge cases (empty/null/zero/max), error handling, off-by-one, concurrent access to shared state;
   - security: unvalidated input, injections, secrets and tokens in code and logs, authz on new paths;
   - tests: new behavior logic without a test; a test that checks the implementation, not the behavior;
   - diff hygiene: debug traces, commented-out code, stray files, off-topic "while we're at it" edits;
   - simplification and reuse — record only as suggestions.
3. **Verification** of blockers and majors — the rule (incl. proof symmetry) is in SKILL.md: didn't refute it with a checked `file:line` → into the output.
4. **Deliver to the chat:** the object, the verdict, findings by severity (each one — proof + failure scenario), a one-line "checked and safe" for any scary-looking finding that verification cleared, and in one line "looked at and clean" — the lenses with no findings. "Nothing found" is a result, not emptiness. Cap the noise: top-5 suggestions, the rest as a one-line count (`+7 more suggestions`) — the Full "cut suggestions, don't cut blockers" in chat form; blockers and majors are never capped.

## Escalation to Full

The object turned out in fact larger or riskier than at classification — more files/lines, a risk zone surfaced → escalate (the trigger rule is in SKILL.md). The Full **delta** to add — not a re-review, Express already touched every lens shallowly:

- the prep context (spec / graph / wiki / invariants — full.md step 1);
- the conformance lens in full (spec/graph/invariants + scope creep), which Express doesn't run;
- skeptic verification of every blocker/major, not just self-refutation;
- the report file.

Express's already-passed lenses aren't re-read unless the object itself grew. A merely found blocker is no reason to escalate: the severity of a finding doesn't change the mode. Express creates no artifacts: a report file appears only on a real escalation to Full.
