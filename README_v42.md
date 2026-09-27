DROP_IT v4.2

Frozen source, plan, runtime and marker codebook are included.

Read SEQUENTIAL_TRIAL_REPORT.md for counts and transitions. Raw stdout/stderr/stdin and final files are retained in the receipt blobs.

Use `python DROP_IT_v4.2.py sequential validate --output .` from this directory to validate the frozen receipt chain and bindings.

The original DROP_IT single-prompt interface remains available: `python DROP_IT_v4.2.py --index 1 --condition D --request task.txt`.

A started sequential cohort cannot be resumed or retried by this harness.
