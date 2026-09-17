# Resolution-Based Education (RBE)

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**  
Licensed under the Apache License, Version 2.0.

Resolution-Based Education (RBE) is a certification-resolution framework for educational assessment in the generative-AI era. Its central question is not merely whether a learner has demonstrated an outcome, but whether the available evidence is sufficient to resolve the capability distinction that the credential claims to certify.

The scientific foundation is presented in:

**Akhtar, M. A. K. (2026). _Beyond Outcome Attainment: Resolution-Based Education and the Certification–Assessment Resolution Gap in the Generative-AI Era_ (Version V1). Zenodo.**  
https://doi.org/10.5281/zenodo.22797079

## Core scientific idea

Let `W` be certification-relevant learner worlds, let `g: W -> D` be the intended certification rule, and let `w_i ~_A w_j` mean that all evidence obtainable under assessment protocol `A` is observationally indistinguishable between `w_i` and `w_j`.

A **Certification–Assessment Resolution Gap (CARG)** exists when:

`w_i ~_A w_j` but `g(w_i) != g(w_j)`.

Therefore, a necessary condition for universally correct certification from protocol `A` is:

`w_i ~_A w_j  =>  g(w_i) = g(w_j)`.

RBE is formulated as a conservative extension of outcome-based education: if current evidence is already resolution-adequate, no additional assessment burden is introduced. If certification-incompatible learner worlds remain observationally equivalent, RBE seeks the least-burdensome admissible additional evidence needed to resolve the remaining decision.

## Resolvable Capability Outcomes

For capability `j`:

`RCO_j = (C_j, E_j, P_j, D_j)`

where `C_j` is the capability claim, `E_j` the relevant environments/tool conditions, `P_j` the admissible perturbation/evidence family, and `D_j` the certification distinction.

Existing examinations, laboratories, projects, assignments and other approved assessments populate the initial evidence state `K_0`. A separate Resolution Gate is needed only when that evidence is insufficient for the declared certification distinction.

## Resolution states and attainment

For learner `i` and capability `j`, conventional performance attainment is:

`A_ij = 1[S_ij >= T_j]`.

Positive resolution requires both sufficiently low decision risk and a positive resolved decision:

`Q+_ij = 1[r_ij <= epsilon_j AND Dhat_ij = d+_j]`.

Resolved Capability Attainment is:

`RCA_ij = A_ij * Q+_ij`.

The reference implementation preserves explicit states:

- `AR` — attained, resolved-positive
- `AU` — attained, unresolved
- `RN` — performance-attained, resolved-negative
- `NA` — not attained
- `Deferred` — further evidence is procedurally permitted or the burden/procedural boundary has been reached

Course-level measures implemented in `rbe/attainment.py` include PAR, RR, RAR, UAR, RNR, deferred rate and mean resolution burden.

## One-step probes versus complete policies

For a candidate probe `e`, burden can be represented as:

`B_lambda(e) = cost(e) + lambda * leakage(e)`.

A one-step probe may be informative without fully resolving the decision. The term **Minimum Resolution-Restoring Perturbation (MRRP)** is reserved for a probe or adaptive policy whose terminal evidence meets the declared resolution condition. The repository therefore includes both a deterministic full-separator kernel and an exact adaptive-policy search for small constructed world sets.

## Reproducible mechanism tests

The paper reports and the repository supports:

- deterministic CARG and cheapest-full-separator tests;
- a small adaptive policy-tree case in which no single probe fully resolves the decision;
- probabilistic and Monte Carlo mechanism tests;
- retrospective OULAD analyses and falsification controls;
- burden-focused evaluation that retains negative results rather than claiming universal predictive superiority.

The final paper reports a 20,000-episode seeded Monte Carlo experiment and retrospective analysis of 32,593 OULAD student-module records. OULAD predates GenAI and RBE and is used only as a retrospective proxy for evidence acquisition, not as causal evidence that RBE improves education.

## Important scientific boundary

RBE does **not** claim that OBE is obsolete, that AI use implies misconduct, that adaptive RBE is universally more accurate than strong fixed assessment, or that retrospective OULAD analysis establishes causal educational effectiveness. The surviving empirical result in the paper is narrower: selective adaptive acquisition can reduce evidence burden under the declared proxy setup while strong fixed-confidence controls remain competitive on risk.

## Repository map

- `rbe/core.py` — deterministic CARG and full-separator MRRP kernel
- `rbe/system.py` — reference Resolution Episode and RCO objects
- `rbe/attainment.py` — paper-aligned AR/AU/RN/NA/Deferred states and attainment metrics
- `rbe/policy.py` — exact adaptive resolution-policy search for small deterministic world sets
- `tests/` — executable mechanism tests
- `benchmarks/` — deterministic, probabilistic, Monte Carlo and OULAD experiment scripts/results where present
- `data/` — benchmark inputs
- `reports/` — test registry and interpretation notes
- `CITATION.cff` — citation metadata for the software and foundation paper
- `LICENSE`, `NOTICE` — Apache-2.0 licensing and attribution

## Citation

Akhtar, M. A. K. (2026). _Beyond Outcome Attainment: Resolution-Based Education and the Certification–Assessment Resolution Gap in the Generative-AI Era_ (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22797079

## License

Apache License 2.0. See `LICENSE` and `NOTICE`.
