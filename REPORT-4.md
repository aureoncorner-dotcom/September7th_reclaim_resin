# Sector memory — executed follow-up v0.1

**8 September 2026 · TD-COS-FH-001 · Separate companion · CC0**

## Result

**A direct argument rules out every finite Markov order for the sector process of the specified ideal kernel. The conclusion holds at attempted microticks, saved sweeps, and every other fixed finite sampling interval.**

This strengthens the previous result without replacing it. The earlier packet showed that parity, signed winding, and all reference-cycle currents fail as an autonomous reduced state. That does not by itself settle whether a finite window of sector history might work. This companion addresses that additional question with a different argument.

[Full proof](PROOF.md) · [Exact certificates](CERTIFICATES.json) · [Execution results](RESULTS.json) · [Independent verification](INDEPENDENT_VERIFICATION.json)

## Scope at a glance

| Item | Scope |
|---|---|
| Kernel | Ideal TD-COS-FH-001, J=1, t=1/2, h6=0, fixed-reference Z000 ensemble |
| State space | Unbounded signed integer currents, mod-two membrane, sector constraints retained |
| Proven lattice family | Cubic side L>=2 |
| Observation | Three-bit sector q |
| Sampling clock | Every fixed integer stride s>=1; microticks s=1 and sweeps s=8L^3+7 included |
| Probability law | Stationary law; extension excludes fixed finite-order behavior after finite burn-in from any initial law |
| Evidence type | Written proof plus exact finite certificates and independently coded checks |
| Not claimed | Typical equilibrium effect size, mixing time, finite latent-state impossibility, physical-time dynamics, historical replay |

A finite-current cutoff, different move weights, accepted-update-only clock, or adaptive stopping rule changes the problem and is not covered automatically.

## 1. Why this is more than another two-step discrepancy

A process is finite-order Markov when some fixed number r of its most recent observations contains everything the older observations can contribute to predicting its next observation. A one-step failure only rejects r=1. A two-step example does not reject every r.

The proof instead constructs an obstruction for arbitrarily long observed blocks. Under the stationary model, an older sector event and a future sector event remain conditionally dependent across all-zero sector blocks of every odd length. For any proposed order r, choose an odd block at least that long. Finite-order Markov behavior would require conditional independence; the proof gives strictly positive conditional covariance.

This is an exact probability statement, not a claim that finite data can empirically test every possible memory length.

## 2. The two state families

Both families consist of admissible closed, even integer currents with zero membrane and sector 000. For each positive integer N, both have identical signed winding (2N,-2N,2N).

Family A has reference-cycle currents all in the same direction on each axis. Family B adds a multiple of one closed plaquette boundary, redistributing the x and y reference currents into opposing directions without changing winding.

For L=2, the cycle lists are particularly simple:

| Family | x cycle | y cycle | z cycle |
|---|---|---|---|
| A | (2N,2N) | (-2N,-2N) | (2N,2N) |
| B | (-2N,2N) | (2N,-2N) | (2N,2N) |

At large N, a unit sector proposal in family A has one favorable orientation and one strongly suppressed orientation. On family B's x and y cycles, the increase on one part is balanced by the decrease on another; both orientation acceptance probabilities tend to one.

Every microtick changes a stored current by at most two. Therefore, for any fixed number of microticks, the large-current contrast persists uniformly over all reachable states. The proof uses this bounded-change fact, not an assumption that the hidden currents remain frozen.

## 3. Saved sweeps do not remove the obstruction

Let B=8L^3+7 and sample after s microticks. In the two limiting regimes, the probability that the x sector bit is one at the next observation, starting from sector 000, is respectively

    alpha_s = (1-(1-1/B)^s)/2,
    beta_s  = (1-(1-2/B)^s)/2.

Their difference is positive for every finite s>=1. For one full saved sweep:

| L | Microticks per sweep | Family A limiting probability | Family B limiting probability |
|---|---:|---:|---:|
| 2 | 71 | 0.317363285340460 | 0.434247436762799 |
| 3 | 223 | 0.316473472636713 | 0.432940150198372 |
| 4 | 519 | 0.316237627713494 | 0.432593287482928 |

These are **constructed large-current limit probabilities**, not measured sector frequencies, equilibrium-average error rates, or stationary covariance magnitudes. Intermediate flips and returns inside each sweep are included in the limit calculation.

The proof treats the actual sampled operator K^s. It does not assume that failure at K must automatically survive every power. The extension to even s is earned by the two limiting walks, not by the earlier odd-power spectral argument.

## 4. The crucial stationary argument

Unequal forecasts from two hidden starting states do not automatically prove that the stationary observation process has infinite memory. This companion explicitly supplies the missing step.

Inside the full-state fiber with q=000, let T be the sampled kernel K^s killed on leaving that fiber at observation times. Let p be the next-observation probability of an x bit equal to one. Set

    u_k=T^k 1,       v_k=T^k p.

Reversibility turns the covariance across a central block of 2k+1 zeros into

    ( ||u_k||^2 ||v_k||^2 - <u_k,v_k>^2 ) / ||u_k||^4.

The norm and inner product use the true stationary weights restricted to the zero-sector fiber. The two current families show that v_k/u_k is not constant for any fixed k. Every admissible finite-current state has positive stationary weight, and the identity branch gives positive survival probability. Strict Cauchy–Schwarz therefore makes the displayed covariance positive.

That proves the all-orders statement. It requires neither a finite-current truncation nor a numerical estimate of the equilibrium mixture.

The extension to other initializations follows by convergence of each fixed late-time block to its stationary distribution. A finite-order conditional-independence identity at all sufficiently late times would survive that limit and contradict the positive stationary covariance.

## 5. What actually ran

The predecessor archive was inspected and preserved. All **19 manifest-listed file hashes** matched, and its report, results, and verification matched the separately attached copies. Both prior calculation programs were freshly executed in another directory; their scientific results matched. See [integrity](PREDECESSOR_INTEGRITY.json) and [replay](PREDECESSOR_REPLAY.json). This replays only the attached equation-level work, not any historical Monte Carlo sampler.

The new main program passed:

| Check | Executed result |
|---|---|
| State construction and geometry | 40 family states at L=2,3,4,5; divergence, evenness, all cuts, winding, and preserved-validator agreement |
| Bounded increments and sector-changing family | All descriptors at those four sizes checked |
| Positive-series ratio bounds | 9 orders checked against tighter exact rational Bessel enclosures |
| Finite conditional-forecast certificates | 72 cases, L=2/3/4, strides 1/2/B, central block lengths through 65 |
| Saved-stride limiting walks | 18 exact matrix-power checks against the parity-character formulas |
| Reversible bridge identity | 21 exact comparisons against direct finite-block probabilities |

The independent program imports none of the main or predecessor calculation code. It independently reconstructed **144 family states**, recomputed all **72 certificates**, checked **2,160 cycle-probability enclosures** with 220-digit normalized Bessel series, and repeated the **21 bridge checks**. All passed.

Independent coding is not independent peer review. The full all-orders argument remains a written mathematical proof rather than a proof-assistant-certified theorem.

## 6. A control that really has finite memory

The suite includes an irreducible reversible three-state chain whose two-label observation is second-order Markov but not first-order. It has a rank-one within-label transition matrix, so two observations really do remove the relevant hidden distinction.

The checker finds 254 first-order discrepancies among 508 inspected longer histories, and zero second-order discrepancies among 504 histories. Its conditional covariance is positive at central length one and zero at all longer tested odd lengths. A direct rank-one reset argument establishes its genuine order-two property; the finite checks corroborate it.

This is important: reversibility, self-loops, and a first-order failure alone do **not** establish an all-orders obstruction. The toroidal proof needs the state families and the strict bridge calculation.

## 7. The practical limit is substantial

The constructive certificates deliberately favor transparent bounds over small witnesses. Their N values range from 10^2 to **10^38**. Those huge currents are legitimate states of the stated unbounded model but can carry extraordinarily small equilibrium probabilities.

Accordingly, the theorem excludes an **exact universal finite-memory sector law**. It does not show that a short-memory approximation performs poorly on the high-probability part of the equilibrium distribution. The approximately 0.117 contrast between the limiting one-sweep forecasts is not a typical prediction-error estimate.

Infinite observed Markov order also does not mean that every latent representation must have infinitely many states. A finite hidden Markov model can have an infinite-order observed process. Minimal latent representation remains a separate question.

The next scientific target is therefore narrower: quantify approximation error for a declared prediction horizon, tolerance, initialization/distribution, and state-mass coverage. A causal filter over hidden states remains a sufficient construction when its kernel and prior are supplied; its smallest useful approximation has not been determined here.

## Disposition

**Upgrade within this companion:** for the stated ideal unbounded kernel, exact finite-order Markov closure of the sector is ruled out at microticks and saved sweeps, with a stronger extension to every fixed positive integer sampling stride.

**Preserved:** the prior same-parity, same-winding, and reference-cycle state counterexamples; all historical sampler and mismatch records; production NOT_AUTHORIZED; physical Q2 NOT_RUN. No connected Google document was modified.

**Not measured:** equilibrium memory magnitude, production mixing, or any physical, chemical, or platform-mechanism effect.

See [PROOF.md](PROOF.md) for complete assumptions, proof, finite-certificate derivations, references, and scope limits.
