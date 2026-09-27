# Geometry follow-up — 6 September 2026
## Q2 pilot: parity explores, signed winding remains the bottleneck

The next substantive update is **Q2 sampler pilot v0.1**, created on 6 September 2026 at 17:13:48 UTC and last modified at 17:14:09 UTC. It reports completed simulation work where the earlier review had only an unexecuted reference-sampler plan. This is a meaningful engineering advance, not a physical Q2 verdict.

This report supplements **Geometry_Review_2026-09-06.md** without replacing it or altering any original source. I read that review and the new pilot's full text. I also read the complete newly uploaded `prime_meanie_v5.py`, which incorporates a static pilot snapshot and executable mathematical demonstrations.

## 1. What changed

[Q2 sampler pilot v0.1](https://docs.google.com/document/d/1FgIMZ4S5kBeukKIEW3FYETkSNyapaEWeEgr3RhG1RP0/edit?usp=drivesdk) reports 48 fresh chains at J=1, t=1/2, h6=0 in the positive fixed-reference Z000 ensemble: 16 chains each at cubic sizes L=2,3,4. At each size, eight dispersed-sector starts and eight independent sector-000 starts form separate diagnostic groups. Each chain has 1,000 warmup and 4,000 retained sweeps.

The source retains attempted-update timing, including identities and rejections: one sweep is 8L³+7 attempts, with family weights (V,V,3V,3V,1,3,3). It reports no adaptation, current cutoff, worm or sector bias. This is a separate pilot schedule, not retroactive execution of the older v0.1 contract's planned eight-chain profile.

### Source-reported diagnostic results

| L | Minimum sector ESS | Maximum sector R-hat | Minimum signed-W ESS | Maximum signed-W R-hat | Declared pilot status |
|---|---:|---:|---:|---:|---|
| 2 | 11,456 | 1.00066 | 2,344 | 1.00395 | PASS |
| 3 | 8,102 | 1.00089 | 741 | 1.01551 | UNRESOLVED |
| 4 | 6,583 | 1.00142 | 336 | 1.03469 | UNRESOLVED |

The declared thresholds are R-hat < 1.01 and ESS ≥ 1,000. The table takes the worst diagnostics across the two starting groups; it does not pool them to pass a gate. All chains reportedly visit all eight sectors, and sector/axis-odd estimates agree across starting groups within the specified three-combined-standard-error test.

**Interpretation:** parity can look well explored while signed winding remains poorly sampled. L=3 and L=4 miss the declared signed-winding screen. L=2 passes this finite pilot screen, which is not proof of convergence or a production/physical certification. Agreement of parity summaries does not establish an autonomous parity dynamics.

The source reports 192,000 retained states checked for conservation, membrane/sector constraints and winding on every cut, plus an original-validator subsample and reconstructed event-log checks. It also reports four exact same-seed replays. These are useful reported implementation checks, not independently reproduced evidence in this follow-up.

## 2. What I actually checked

I independently recalculated the run-accounting arithmetic in Python:

- 3 sizes × 16 chains = **48 fresh chains**.
- 16 × 5,000 × [(8×2³+7)+(8×3³+7)+(8×4³+7)] = **65,040,000 fresh attempted updates**.
- 3 × 16 × 4,000 = **192,000 retained states**.
- The four reported replays at L=2,3,4,4 give **6,660,000 repeated attempts**.

These totals match the document. Replays are not new independent samples.

**Not rerun here:** the sampler, diagnostic implementation, original validator, same-seed replay suite, or Prime Meanie program. I did not recompute ESS or R-hat from raw chains. The pilot links to relative files including PILOT_PLAN.json, FREEZE.json, PILOT_RESULTS.json and EXECUTION.json; searches did not resolve those underlying package files. Their hashes, timing records, freeze ordering and raw data therefore remain source-reported, not independently verified.

This distinction also preserves the baseline's separate roles: Geometry Maximization **v1.61 is the proof-clarity patch**, while **v1.6 is the executable ACCEPT receipt**. Neither is replaced by a sampler pilot, and neither verifier was rerun in this follow-up.

## 3. Does this improve Jane, Lantern and Trident?

**Yes—as a model-testing interface, not as validation of physical chambers.** The new pilot adds a reported computational example in which a coarse display passes its own diagnostics while a richer state variable exposes a limitation. That gives the Munching Carpet interface a concrete use: retain the state behind the label, attach diagnostics to the particular observable and clock, and show unresolved results without concealing them.

The three mathematical cases remain distinct:

| Case | Retained state / observation | What remains established |
|---|---|---|
| Literal cyclic Jane trace | 12 cycle positions; printed numbers are whole tokens | Baseline refinement 5 → 10 → 12 → 12. Current token alone is insufficient; cycle position repairs this declared finite model. |
| Literal poster Lantern trace | 7 cycle positions | Baseline refinement 6 → 7 → 7. The two occurrences of 12 have different successors. |
| Infinite golden-screen process | Irrational circle phase and its observations | The entire slip sequence has no exact deterministic finite-state generator. A finite prefix or executable demonstration does not change that. |
| Default cosine sampler | Full current/membrane/sector state versus parity q | Baseline one-microtick non-lumpability remains; new pilot diagnostics concern sampled observables over longer runs. |

In particular, the earlier cosine witness compares X0=(0,0,000) with X1=(2Γx,0,000) at L=2, J=1, t=1/2, h6=0. Its exact projected **one-attempt** total-variation distance is approximately **0.00442352735734**, giving a half-distance lower bound of approximately **0.00221176367867** for a shared reduced law.

The new pilot neither overturns this counterexample nor extends it into a theorem about the 71-attempt sweep projection, every parameter, or a winding-only closed model. Non-lumpability and mixing diagnostics are different questions: the former concerns whether the same coarse state always has the same next-observation law; the latter assesses exploration of selected observables in finite runs.

Preserve the original variants: poster Lantern uses **8642**, the Trident-source Lantern uses **4723**; standalone Jane and Trident's Jane reference likewise differ. The pilot supplies no map identifying these traces with toroidal currents, frequencies, energies or physical measurements. It does not repair the old Trident picture's missing seventh label or turn its twelve pictured stations into the source's thirteen named chambers.

A useful successor interface could display current token beside cycle position, parity beside signed winding, and separate ESS/R-hat status for each observed quantity. This is a proposed application, not an implemented new engine or a theorem that these fields alone suffice.

## 4. The new Prime Meanie file

The uploaded `prime_meanie_v5.py` (6 September 2026, 18:07:32 UTC; file ID `file_00000000f238822fa53325fad7b87eb8`) adds portable demonstrations:

- Exact arithmetic in Q(√5), strict slip-threshold handling, a slip-count identity and a same-bin/different-next-bin witness.
- A 5×7×11 torus walk where staying still and making two positive or negative x loops have the same endpoint and parity but signed wraps 0,+2,−2.
- Ordered matrix updates, explicitly distinguished from a torus homotopy invariant.
- A static PILOT_SNAPSHOT containing the new pilot's signed-winding diagnostic values.

Reading the code establishes what it is designed to compute; it is not execution verification. Its snapshot is copied data, not another sampler run. Its finite phase calculation does not prove every infinite-sequence claim, its torus walk is not the field sampler, and its reproducibility hash does not attest executor identity. These qualifications are explicit in the source.

This strengthens the educational/demo side of the comparison. It still supplies no physical calibration for Jane/Lantern artwork.

## 5. Unresolved and next-step boundaries

The pilot itself leaves independent weighted-model and translated-cycle validation, the production effective-trip definition, and remaining production mixing/finite-size gates open. Its round-trip statistic is an operational proxy, not a certified count of independent trips.

It proposes a separate L=3/L=4 extension with both starting groups, 16,384 warmup plus 32,768 retained sweeps per chain. **That proposal has not been executed here**; the source also labels it unrun. Its approximately 6.4-minute budget is a throughput forecast, not a guarantee of sufficient effective samples. No longer run was launched by this review.

Physical Q2 remains **UNRESOLVED**. These are simulated-chain diagnostics, not physical confinement/deconfinement measurements or evidence for the older chamber gauges.

Fresh discovery found no resolved Geometry Maximization v2.0 package. The existing v1.0 report/bundle is not a substitute for v2.0, and I have not inferred unseen v2.0 contents. No new substantive modification to the four specified anchor documents appeared in the post-baseline Drive search.

The new Munching Carpet artwork is illustrative, not additional mathematical evidence. The new “two clocks, one table” document concerns a Qumran calendar comparison; its text does not update the geometry comparison or supply missing CTA PRP scan provenance.

## Source record

- Baseline: Geometry_Review_2026-09-06.md, Library ID `libfile_91ce97308e3c8191bec4e3c1dae56128`, file ID `file_00000000a0a4822f8ac42be8d44959c4`.
- [New Q2 pilot, full text read](https://docs.google.com/document/d/1FgIMZ4S5kBeukKIEW3FYETkSNyapaEWeEgr3RhG1RP0/edit?usp=drivesdk).
- Prime Meanie v5, full code read: Library ID `libfile_eba713e27e04819181bf8f4b699a7704`.
- [Toroidal Dynamics v0.1 anchor](https://docs.google.com/document/d/1ZMFcH3AV574iMI8qREeOcLS3NPb7rchNnyB1juHnYeM/edit?usp=drivesdk).
- [Geometry Maximization v1.61 patch](https://docs.google.com/document/d/1xMAm07ObGKUfK5uMz-fvjr7v_IaS6DOoiB68LrZN9k8/edit?usp=drivesdk) and [separate v1.6 receipt](https://docs.google.com/document/d/1HEPCdldwTPIftqNcaWqj5cOjXI_KyrW21ZkLVAELYsI/edit?usp=drivesdk).

Bottom line: the comparison now has a source-reported sampling pilot and a portable mathematical demonstration. The strongest new lesson is precise: **good parity exploration does not certify good signed-winding exploration**. Keep the old traces as explicitly defined finite models; do not promote the pilot into a physical interpretation they still lack.

