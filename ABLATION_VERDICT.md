# Direct-Service Ablation Verdict

## Result

In the retained AO30 representation, the separate user-facing/intermediate stage records can be removed while preserving the recorded substantive answer text exactly wherever the stage is represented as a separate record.

### B50

- 10 unique user→answer chains across 2 RTC sessions / 2 cases.
- 6 chains contain separate stages.
- Checking appears in 5 chains; thoughts in 6; reasoning recap in 6.
- Removing each of those separate stage classes preserves the final recorded answer text exactly in 100% of eligible chains.
- One assistant-only continuation exists: prior answer → thoughts → reasoning recap → second assistant answer with no intervening user. Removing the continuation leaves the prior answer intact; whether the prior answer alone fully satisfied the task is not adjudicated by this ablation.

### 455

- 8 unique user→answer chains across 3 RTC sessions / 2 cases.
- 7 chains contain separate stages.
- Thoughts and reasoning recap appear in 7 chains; work-status in 3; preamble in 2; Checking in 1.
- Removing each separate stage class preserves the final recorded answer text exactly in 100% of eligible chains.
- No assistant-only continuation was found in the current 455 sample.

### A29

- 15 unique user→answer chains across 2 RTC sessions / 2 cases.
- Only 1 chain in the AO30 slices contains a removable separate work-status stage.
- Removing it preserves the final recorded answer text exactly.

### Baseline

- 20 unique user→answer chains across 3 RTC sessions / 3 cases.
- No separate stage records appear in the sampled AO30 user→answer chains.

## Engineering conclusion

The minimum user-facing route supported by these retained records is:

`USER → SUBSTANTIVE ANSWER`

Standalone Checking, work-status, preamble, thoughts, and reasoning-recap records are not needed in the visible transcript to preserve the already-recorded answer text. They may remain internal if runtime implementation requires them; the user-facing route does not need to expose them as separate turns.

The only item that needs separate task-completeness adjudication is assistant-only continuation, because deleting a later substantive continuation can remove additional content even though the prior answer remains present.