# Interpreting the harness's scratch evaluation cycle

In this guide, you will learn how to identify the roles the harness's
scratch evaluation dimension uses to move a draft from a first version to a
final score, and how the deterministic gate decides whether another round
runs. This dimension is a fixture used to exercise the round loop's
mechanics, not a real content-quality check.

## Identifying the roles in the cycle

The scratch evaluation dimension defines three roles, each with one job.

1. The drafting child writes the first version of a file from a brief.
2. The evaluator child reads that draft together with a rubric and reports
   a score.
3. The deterministic gate decides whether the cycle repeats or ends. It
   makes that decision from the score, the round number, and the cap
   alone, with no other input.

The evaluator child also needs at least one source to read alongside the
artifact and the rubric it is scoring. That source's own content is not
itself scored. It exists only so the evaluator child has something to
read.

## Following the gate's decision

After the evaluator child reports a score, the deterministic gate compares
it against the criteria set for the run.

1. Check the score the evaluator child reported.
2. Check the current round number against the cap set for the run.
3. When it meets the threshold set for ending the cycle, the gate ends
   the cycle without another revision round.
4. If it falls short and the cap has not been reached, the gate
   starts another round instead.

The exact threshold and round cap values for a given run are configured in
the run's own configuration or contract file. Refer to your harness setup
or test fixture to find these specific values for your evaluation.

Once the gate's decision is made, you can confirm the cycle's current state
by checking which of these two outcomes applies: the cycle stopped because
the score cleared the threshold, or it continued because the score fell
short and rounds remained under the cap.
