# RBE Test Registry

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

This registry is append-only in spirit: every scientifically meaningful mechanism, comparison, robustness, calibration, fairness, burden, leakage, or predictive-validity test added to RBE should be recorded here. Constructed/synthetic tests must never be presented as human educational evidence.

| ID | Test | Scientific question | Data | Expected interpretation |
|---|---|---|---|---|
| T001 | Artifact-only CARG | Can identical artifact evidence leave worlds requiring opposite certification decisions observationally compatible? | Constructed W1-W4 | Structural non-identifiability construction. |
| T002 | Cheapest full separator | Which minimum cost+leakage intervention separates every unresolved certification-incompatible pair? | Constructed W1-W4 | Cheapest feasible full separator, not cheapest raw probe. |
| T003 | Resolution restoration | Does selected MRRP remove CARG? | Constructed W1-W4 | Decision-homogeneous cells after resolving intervention. |
| T004 | Leakage sensitivity | Can lambda alter selected experiment? | Constructed competing probes | Burden/leakage tradeoff. |
| T005 | No-CARG resolved control | Does already-resolved protocol report no CARG? | Constructed W1-W4 | Control. |
| T006 | Initial decision entropy | Does balanced benchmark begin with one bit decision uncertainty? | Probabilistic W1-W4 | Probabilistic sanity check. |
| T007 | Positive probe information | Do noisy perturbations reduce certification uncertainty? | probabilistic benchmark | Positive decision information gain. |
| T008 | Resolution-threshold dependence | Does cheapest qualifying experiment change with stricter resolution requirement? | probabilistic benchmark | Cheapest is conditional on sufficient resolution. |
| T009 | Resolution efficiency vs generic viva | Can targeted probe yield more decision information per burden? | probabilistic benchmark | Mechanism efficiency comparison. |
| T010 | Artifact zero-information control | Does identical artifact distribution yield zero decision information? | probabilistic benchmark | Probabilistic CARG/AIRC control. |
| T011 | Adaptive resolution rate | Does adaptive RBE resolve more noisy episodes than fixed targeted and one-viva protocols? | 20,000 seeded synthetic episodes | Adaptive RBE: 96.45%; targeted: 77.355%; viva: 46.86%. |
| T012 | Adaptive burden vs viva | Is adaptive RBE lower burden than generic viva? | same simulation | Mean 2.4455 vs 6.0; mechanism-level burden advantage. |
| T013 | Adaptive stopping efficiency | Does adaptive stopping use fewer probes than fixed targeted sequence? | same simulation | Mean 1.8261 vs 2.3415 probes. |
| T014 | Error-tradeoff falsification | Does adaptive RBE fail to dominate fixed targeted assessment on resolved-case error? | same simulation | Yes: 8.61% vs 6.45%; motivates risk-constrained resolution. |
| T015 | OULAD real-data CARG proxy | Does coarse early assessment evidence leave real students with opposite eventual certification outcomes in the same observational cells? | OULAD >30k student-module records | Real observational test of decision-incompatible cells; not causal RBE evidence. |
| T016 | OULAD cheapest added evidence | Which equally costed logged evidence channel most reduces unresolved mass beyond assessment score? | OULAD assessment + VLE data | Select highest resolution gain per declared unit cost. |
| T017 | OULAD refinement monotonicity | Does adding a genuine evidence dimension avoid increasing unresolved mass under the benchmark partition? | OULAD logic + offline fixture | Structural implementation check. |

## Current significant results

### Deterministic benchmark
Artifact-only evidence leaves four cross-decision pairs unresolved. At lambda=1, wrong-AI-check is cheapest raw burden (0.55) but is not a full separator. Constraint-shift is the cheapest feasible full separator (1.10), versus transfer 1.25 and generic viva 6.00.

### Probabilistic benchmark
Probe eligibility depends on a declared minimum decision-information threshold. The cheapest useful experiment can therefore change as the required resolution becomes stricter. Artifact-only evidence is zero-information in the constructed collapse case.

### Adaptive Monte Carlo benchmark
At seed 20260916, n=20,000 and posterior decision threshold 0.90: adaptive RBE resolves 96.45% with mean burden 2.4455 and 1.8261 probes; fixed targeted resolves 77.355% with burden 2.0769 and 2.3415 probes; one generic viva resolves 46.86% with burden 6.0. Crucially, adaptive RBE has higher resolved-case error (8.61%) than fixed targeted (6.45%). This negative result is retained as a falsification constraint: resolution must be jointly controlled with decision risk.

### Real OULAD benchmark
T015-T017 use the public Open University Learning Analytics Dataset. The executable benchmark downloads the official dataset at runtime, uses early/mid-course assessment and VLE evidence, and compares equally costed additional evidence channels by reduction in decision-incompatible observational mass. Because OULAD is observational, predates modern GenAI, and contains no designed RBE perturbations, this benchmark is explicitly a real-data proxy validation rather than a causal test of RBE. Aggregate numerical results are to be committed after a successful full-data run.

## Rule for future work
Whenever a test has scientific significance: (1) commit executable test code, (2) commit the input dataset or deterministic generator or official retrieval procedure, (3) commit/save numerical results, (4) commit/report interpretation and limitations, and (5) append a row here. Human-study results must identify provenance, sample, protocol, uncertainty, and ethics/consent status where applicable.
