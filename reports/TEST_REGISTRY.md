# RBE Test Registry

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

This registry is append-only in spirit: every scientifically meaningful mechanism, comparison, robustness, calibration, fairness, burden, leakage, or predictive-validity test added to RBE should be recorded here. Constructed/synthetic tests must never be presented as human educational evidence.

| ID | Test | Scientific question | Data | Result / interpretation |
|---|---|---|---|---|
| T001 | Artifact-only CARG | Can identical artifact evidence leave worlds requiring opposite certification decisions observationally compatible? | Constructed W1-W4 | Structural non-identifiability construction. |
| T002 | Cheapest full separator | Which minimum cost+leakage intervention separates every unresolved certification-incompatible pair? | Constructed W1-W4 | Constraint-shift cheapest feasible full separator at declared costs. |
| T003 | Resolution restoration | Does selected MRRP remove CARG? | Constructed W1-W4 | Decision-homogeneous cells after resolving intervention. |
| T004 | Leakage sensitivity | Can lambda alter selected experiment? | Constructed competing probes | Burden/leakage tradeoff. |
| T005 | No-CARG resolved control | Does already-resolved protocol report no CARG? | Constructed W1-W4 | Control. |
| T006 | Initial decision entropy | Does balanced benchmark begin with one bit decision uncertainty? | Probabilistic W1-W4 | Probabilistic sanity check. |
| T007 | Positive probe information | Do noisy perturbations reduce certification uncertainty? | Probabilistic benchmark | Positive decision information gain. |
| T008 | Resolution-threshold dependence | Does cheapest qualifying experiment change with stricter resolution requirement? | Probabilistic benchmark | Cheapest is conditional on sufficient resolution. |
| T009 | Resolution efficiency vs generic viva | Can targeted probe yield more decision information per burden? | Probabilistic benchmark | Mechanism efficiency comparison. |
| T010 | Artifact zero-information control | Does identical artifact distribution yield zero decision information? | Probabilistic benchmark | Probabilistic CARG/AIRC control. |
| T011 | Adaptive resolution rate | Does adaptive RBE resolve more noisy episodes than fixed targeted and one-viva protocols? | 20,000 seeded synthetic episodes | Adaptive 96.45%; targeted 77.355%; viva 46.86%. |
| T012 | Adaptive burden vs viva | Is adaptive RBE lower burden than generic viva? | Same simulation | Mean 2.4455 vs 6.0. |
| T013 | Adaptive stopping efficiency | Does adaptive stopping use fewer probes than fixed targeted sequence? | Same simulation | Mean 1.8261 vs 2.3415 probes. |
| T014 | Error-tradeoff falsification | Does adaptive RBE fail to dominate fixed targeted assessment on resolved-case error? | Same simulation | Yes: 8.61% vs 6.45%; motivates risk-constrained resolution. |
| T015 | OULAD real-data CARG proxy | Does coarse early assessment evidence leave real students with opposite eventual certification outcomes in the same observational cells? | OULAD 32,593 student-module records | At cutoff 120, q=5, score-only unresolved mass = 1.000. |
| T016 | OULAD cheapest added evidence | Which equally costed logged evidence channel most reduces unresolved mass beyond assessment score? | OULAD assessment + 10,655,280 VLE rows | VLE clicks largest gain, 0.000368; effect is extremely small. |
| T017 | OULAD refinement monotonicity | Does adding a genuine evidence dimension avoid increasing unresolved mass under benchmark partition? | OULAD + implementation logic | Yes for tested channels; active-days gain = 0. |
| T018 | OBE-style baseline vs resolution layer | Does adding resolution-oriented evidence materially outperform assessment-score evidence on the current real-data endpoint? | OULAD | No practical advantage on coarse mixed-cell endpoint; negative result retained. |
| T019 | Enhanced OBE control requirement | Is score-only a sufficient comparator for an OBE claim? | OULAD protocol + OBE literature | No. Future comparison must include score + assessment-count/direct-evidence control. |
| T020 | Real-data supremacy falsification gate | Can current OULAD partition result justify 'RBE is superior to OBE'? | OULAD | No. Supremacy claim is blocked pending out-of-sample predictive/calibration/risk comparison. |

## Current significant results

### Deterministic benchmark
Artifact-only evidence leaves four cross-decision pairs unresolved. At lambda=1, wrong-AI-check is cheapest raw burden (0.55) but is not a full separator. Constraint-shift is the cheapest feasible full separator (1.10), versus transfer 1.25 and generic viva 6.00.

### Probabilistic benchmark
Probe eligibility depends on a declared minimum decision-information threshold. The cheapest useful experiment can therefore change as the required resolution becomes stricter. Artifact-only evidence is zero-information in the constructed collapse case.

### Adaptive Monte Carlo benchmark
At seed 20260916, n=20,000 and posterior decision threshold 0.90: adaptive RBE resolves 96.45% with mean burden 2.4455 and 1.8261 probes; fixed targeted resolves 77.355% with burden 2.0769 and 2.3415 probes; one generic viva resolves 46.86% with burden 6.0. Crucially, adaptive RBE has higher resolved-case error (8.61%) than fixed targeted (6.45%). This negative result is retained as a falsification constraint: resolution must be jointly controlled with decision risk.

### Real OULAD benchmark
The full GitHub Actions run succeeded on 32,593 student-module records and the 10,655,280-row VLE table. At cutoff 120 days and q=5, score-only unresolved mass was 1.000. VLE engagement was the best equally costed additional channel but reduced unresolved mass only to 0.999632 (absolute gain 0.000368). Assessment count and VLE-record count each gained 0.000061, submission timing 0.000031, and active days 0. This is a negative practical result for the coarse partition metric. It does not establish RBE superiority and motivates a stronger out-of-sample OBE-vs-RBE comparison using discrimination, calibration, selective risk/coverage, false-certification rates, and matched evidence budgets.

## Rule for future work
Whenever a test has scientific significance: (1) commit executable test code, (2) commit the input dataset or deterministic generator or official retrieval procedure, (3) commit/save numerical results, (4) commit/report interpretation and limitations, and (5) append a row here. Human-study results must identify provenance, sample, protocol, uncertainty, and ethics/consent status where applicable.
