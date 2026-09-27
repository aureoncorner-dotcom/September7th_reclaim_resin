# LBCO observed-fiber geometry — computational reproduction

Author: Anonymous · Original analysis/code: PUBLIC DOMAIN — CC0 1.0. Cited sources retain their own terms.

Run: **FG-14.9-LBCO-001-REPLAY-2026-09-08**  
Parent: **FG-14.9-LBCO-001**, frozen and executed September 4, 2026.  
Disposition: **PASS — one located empirical non-descent fiber, under the frozen reported-interval convention.**

This is a fresh computational reproduction of an existing retrospective gate. It adds a runnable calculation and execution receipt, not new experimental observations or prospective preregistration. The parent records are preserved.

## Frozen scope and source verification

The [existing gate](https://docs.google.com/document/d/1LOvu-chrNKnuz9XWWMAteF2foHM-pHE6YMnZDV0TQ3Y/edit) already selects the narrowest executable domain. Its matching Markdown record was also read in full. [New geometry](https://docs.google.com/document/d/1DVgC8ia4Z1suHmLbcrDbvw1ETuSjkTm25_5DH8OOQNI/edit), §§4 and 14.9, supplies the values and observed-fiber method.

| Freeze item | Applied rule |
|---|---|
| D | Exactly the two published LBCO x=1/8 exponent records, Tso and Tc |
| W | Reported oxygen-isotope exponent of the typed observable |
| Projection | Retain material, nominal x, isotope intervention, study/sample family; erase observable/probe identity |
| Same fiber | Exact equality of retained identifiers; no approximate bins or cross-study pooling |
| Metric | Absolute difference in dimensionless exponent units |
| Tolerance | ε=0.00; detection only |
| Uncertainty | Each reported (6) means the frozen symmetric ±0.06 interval; no added confidence level, independence, or Gaussian combination |
| Coverage | Both named records present, numerical uncertainty on each, one computable eligible pair; authorizes detection only |
| Exclusions | Vm, other observables/compositions/studies, pressure variation, new measurements and raw-data reanalysis |

The [primary paper](https://doi.org/10.1103/PhysRevLett.113.057002), printed pp. 057002-2 and -4, confirms same-batch measurements and identifies +0.46(6) specifically as **Tc1**, while −0.57(6) is the authors' averaged **Tso** exponent. The study's enriched sample contains approximately 82% oxygen-18; the frozen intervention label does not mean a pure-isotope endpoint. We preserve the two published coefficients without recomputing enrichment corrections or treating component fits as extra observations. These annotations resolve source identity; they do not expand D.

The fetched method metadata gives modification time 2026-09-03T16:24:46.632Z; the gate gives 2026-09-04T02:28:10.195Z. A same-day update was not verified. The gate cites parent revision 8; that historical revision was not independently downloaded or byte-verified here. Current extracted text hashes below identify this retrieval, not original native bytes or revision-8 identity.

## Executed geometry

| Source record | Reported exponent | Frozen interval |
|---|---:|---:|
| Tso, μSR, published average | −0.57 | [−0.63, −0.51] |
| Tc, source-specific Tc1, magnetization | +0.46 | [+0.40, +0.52] |

Both records map to qLBCO. The observed sector space of reported values is

`S_hat = {(qLBCO, −0.57), (qLBCO, +0.46)}`.

Each point retains its interval annotation. The intervals describe uncertainty; they are not additional observed sectors.

- Observed records: **2/2 required**.
- Observed quotient points: **1**.
- Eligible unordered pairs: **1/1**.
- Observed sector multiplicity: **2**, not a global sheet count.
- Observed central fiber diameter: **1.03** exponent units.
- Pair-distance interval: **[0.91, 1.15]**.

For intervals [a,b] and [c,d], the distance bounds are `L=max(0,a−d,c−b)` and `U=max(|a−d|,|b−c|)`. Here L=0.40−(−0.51)=0.91 and U=0.52−(−0.63)=1.15. Thus **L>ε**, reproducing the parent's detection result exactly.

The interval bound applies conditional on both witness values lying in their reported intervals. It has no assigned simultaneous confidence or p-value. “Certified” here retains the parent's limited reported-interval convention; it is not an unconditional bound on unknown physical truth. For the frozen two-record domain it bounds that pair's diameter; 1.15 is not an upper bound for any larger, unobserved physical fiber.

`N_hat_cert = {qLBCO}` under that convention. **Observable/probe identity: RETAIN.** Deleting the joint label loses the distinction between opposite responses. This pair does not establish that probe identity independently causes the difference, or that each part of the joint label is separately necessary.

## Preserved limits

No unobserved fiber was populated. No empirical clean fiber or DESCENT_CANDIDATE was established. Coverage is complete only for this two-record detection gate; no global sampling denominator is supplied.

Global shape, connectivity, components, holes, branching, multiscale topology, and quotient-space boundaries remain **UNRESOLVED**. Two witness values over one base point do not establish two connected sheets. No base metric, retained-base path, adjacency model, or diameter crossing was supplied, so no boundary candidate is generated. No source-space transition or refined-space branch change is measured by this static pair.

Path lifting, connection, transport, holonomy, and monodromy remain **UNRESOLVED / NOT ESTIMATED**. No zero-holonomy result is implied. Global openness, properness, smoothness, connected fibers, and minimal causal refinement remain unverified. Retaining W gives formal record-level resolution but does not prove a predictive mechanism.

**CHEMISTRY FREEZE — UNCHANGED. GLOBAL NON-DESCENT GEOMETRY — NOT YET MEASURED. UNIVERSAL PREDICTIVE CLOSURE — NOT SHOWN.**

## Reproduction receipt

The standard-library Python program below uses exact decimal arithmetic, checks the frozen record count, identities, uncertainty fields and same-fiber coverage, then computes the observed sector space and pair bound. Copy the code to `replay.py` and run `python3 replay.py`. No network, external packages, random sampling or parameter fitting is required. Input values are a source-verified transcription of the frozen records, not newly recovered raw measurements.

Executed UTC: 2026-09-08T07:47:08.520846+00:00  
Python: 3.12.13

| Hashed object | SHA-256 |
|---|---|
| Embedded replay.py, UTF-8 including final newline | b8fa547d211f8c102cb2e07cf98b82575d35c0e06fc4e05c332323f8395cbd12 |
| Current extracted new_geometry text, UTF-8 | 4422a0367355094f77b8b8708ba9926e18515a064f614412b9ad6e37768e2221 |
| Current extracted gate text, UTF-8 | 1e4b984ed4e4ac384bf9268f52768d2aed7c9524cfcc1e24ba67ebe8b4e97cb9 |

Actual recomputed output:

```json
{
  "run_id": "FG-14.9-LBCO-001-REPLAY-2026-09-08",
  "coverage": "PASS_DETECTION_ONLY",
  "records": 2,
  "observed_fibers": 1,
  "eligible_pairs": 1,
  "observed_sector_multiplicity": 2,
  "sector_space": [
    {
      "q": "qLBCO",
      "observable": "Tso",
      "source_observable": "Tso (published average)",
      "witness": "-0.57",
      "interval": [
        "-0.63",
        "-0.51"
      ]
    },
    {
      "q": "qLBCO",
      "observable": "Tc",
      "source_observable": "Tc1",
      "witness": "0.46",
      "interval": [
        "0.40",
        "0.52"
      ]
    }
  ],
  "pairs": [
    {
      "pair": [
        "Tso",
        "Tc"
      ],
      "central_distance": "1.03",
      "distance_interval": [
        "0.91",
        "1.15"
      ],
      "detected": true
    }
  ],
  "certified_locus_under_reported_interval_convention": [
    "qLBCO"
  ],
  "coordinate_classification": "RETAIN",
  "chemistry_freeze": "UNCHANGED",
  "global_shape_connectivity_boundaries_holonomy": "UNRESOLVED",
  "universal_predictive_closure": "NOT_SHOWN"
}
```

Executable program:

```python
from decimal import Decimal as D
from itertools import combinations
import hashlib, json
from pathlib import Path

# CC0 1.0; Author: Anonymous. Retrospective reproduction only.
SPEC = {
    'parent_gate': 'FG-14.9-LBCO-001',
    'run_id': 'FG-14.9-LBCO-001-REPLAY-2026-09-08',
    'material': 'La2-xBaxCuO4', 'x': '1/8',
    'intervention': '16O/18O exchange, published same-batch sample family',
    'study': '10.1103/PhysRevLett.113.057002',
    'witness': 'reported oxygen isotope exponent of typed observable',
    'metric': 'absolute distance', 'epsilon': '0.00',
    'projection_keys': ['material', 'x', 'intervention', 'study'],
    'uncertainty': 'reported symmetric intervals only; no confidence level added',
    'required_observables': ['Tso', 'Tc'],
    'coverage': 'both records, numerical uncertainty, same fiber; detection only',
}
DATA = [
    dict(observable='Tso', source_observable='Tso (published average)',
         probe='muSR', value='-0.57', uncertainty='0.06'),
    dict(observable='Tc', source_observable='Tc1',
         probe='magnetization', value='0.46', uncertainty='0.06'),
]
for row in DATA:
    row.update({k: SPEC[k] for k in SPEC['projection_keys']})

def run():
    assert len(DATA) == 2
    assert sorted(r['observable'] for r in DATA) == sorted(SPEC['required_observables'])
    fibers = {}
    for row in DATA:
        v, u = D(row['value']), D(row['uncertainty'])
        assert v.is_finite() and u.is_finite() and u >= 0
        q = tuple(row[k] for k in SPEC['projection_keys'])
        fibers.setdefault(q, []).append((row, v, v-u, v+u))
    assert len(fibers) == 1, 'Frozen same-fiber rule failed'
    pair_results, sectors = [], []
    for q, rows in fibers.items():
        for row, v, lo, hi in rows:
            sectors.append({'q': 'qLBCO', 'observable': row['observable'],
                            'source_observable': row['source_observable'],
                            'witness': str(v), 'interval': [str(lo), str(hi)]})
        for a, b in combinations(rows, 2):
            lower = max(D(0), a[2]-b[3], b[2]-a[3])
            upper = max(abs(a[2]-b[3]), abs(a[3]-b[2]))
            pair_results.append({'pair': [a[0]['observable'], b[0]['observable']],
                'central_distance': str(abs(a[1]-b[1])),
                'distance_interval': [str(lower), str(upper)],
                'detected': lower > D(SPEC['epsilon'])})
    detected = any(p['detected'] for p in pair_results)
    return {'run_id': SPEC['run_id'], 'coverage': 'PASS_DETECTION_ONLY',
        'records': len(DATA), 'observed_fibers': len(fibers),
        'eligible_pairs': len(pair_results),
        'observed_sector_multiplicity': len(set((s['q'],s['witness']) for s in sectors)),
        'sector_space': sectors, 'pairs': pair_results,
        'certified_locus_under_reported_interval_convention': ['qLBCO'] if detected else [],
        'coordinate_classification': 'RETAIN' if detected else 'UNRESOLVED',
        'chemistry_freeze': 'UNCHANGED',
        'global_shape_connectivity_boundaries_holonomy': 'UNRESOLVED',
        'universal_predictive_closure': 'NOT_SHOWN'}

if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
```
