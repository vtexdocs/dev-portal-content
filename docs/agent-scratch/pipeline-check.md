# Running the scratch drafting and evaluation cycle

The scratch drafting and evaluation cycle moves a file from draft to evaluation to a gate decision that either repeats or ends the cycle. This cycle exercises round-loop mechanics, not a real content-quality process.

## Roles in the cycle

Three roles take part in the cycle, each with a distinct responsibility:

- **Drafting child**: writes the first version of a file from a brief.
- **Evaluator child**: reads a draft and a rubric and reports a score.
- **Deterministic gate**: decides whether the cycle repeats or ends, from the score, the round number, and the cap alone.

## Instructions

1. The drafting child writes the first version of the file from the brief it receives.
2. The evaluator child reads that draft together with the rubric and reports a score back.
3. The deterministic gate evaluates three inputs to decide whether the cycle repeats or ends: the score (compared against a passing threshold), the current round number (compared against a maximum round cap), and the harness configuration that defines those threshold and cap values. The gate outputs a yes/no decision that either triggers another draft round or halts the cycle.

After the gate's decision, you know whether another draft round begins or whether the cycle stops at the current draft.
