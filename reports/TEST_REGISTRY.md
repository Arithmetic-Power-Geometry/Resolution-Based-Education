# RBE Test Registry

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

This registry is append-only in spirit: every scientifically meaningful mechanism, comparison, robustness, calibration, fairness, burden, leakage, or predictive-validity test added to RBE should be recorded here. Constructed/synthetic tests must never be presented as human educational evidence.

| ID | Test | Scientific question | Data | Expected interpretation |
|---|---|---|---|---|
| T001 | Artifact-only CARG | Can identical artifact evidence leave worlds requiring opposite certification decisions observationally compatible? | Constructed W1-W4 | Yes demonstrates structural non-identifiability in the construction. |
| T002 | Cheapest full separator | Among supplied experiments, which minimum cost+leakage intervention separates every unresolved certification-incompatible pair? | Constructed W1-W4 + candidate experiments | MRRP selects the cheapest feasible full separator, not simply the cheapest probe. |
| T003 | Resolution restoration | Does the selected MRRP remove the CARG in the constructed case? | Constructed W1-W4 | Selected full separator produces decision-homogeneous observational cells. |
| T004 | Leakage sensitivity | Can changing lambda in cost + lambda*leakage alter the selected experiment? | Constructed competing probes | Yes; makes the burden/leakage tradeoff empirically inspectable. |
| T005 | No-CARG resolved control | Does a protocol already separating pass/fail worlds correctly report no CARG? | Constructed W1-W4 | Sanity/control test. |
| T006 | Initial decision entropy | Does the balanced certify/do-not-certify benchmark begin with exactly one bit of decision uncertainty? | Probabilistic W1-W4 | Sanity check for the probabilistic decision-relative criterion. |
| T007 | Positive probe information | Do the declared noisy perturbations reduce expected certification-decision uncertainty? | `probabilistic_probe_benchmark.csv` | Each informative perturbation must have positive decision information gain. |
| T008 | Resolution-threshold dependence | Does the cheapest qualifying experiment change when the required decision-information threshold becomes stricter? | Probabilistic W1-W4 | Demonstrates that cheapest means cheapest subject to sufficient resolution, not minimum raw cost. |
| T009 | Resolution efficiency vs generic viva | Does a targeted perturbation provide more expected decision information per burden than the expensive generic viva under the declared model? | Probabilistic W1-W4 | Mechanism-level efficiency comparison; not a human-study superiority claim. |
| T010 | Artifact zero-information control | When all worlds have the same artifact response distribution, does artifact-only evidence supply zero certification-decision information? | Probabilistic W1-W4 | Probabilistic analogue of AIRC/CARG construction. |

## Current significant results

### Deterministic benchmark
For `data/cheapest_experiment_benchmark.csv`, artifact-only evidence maps W1-W4 to the same `excellent` observation while W1/W2 require certify and W3/W4 require do-not-certify. Four cross-decision pairs remain unresolved. At leakage weight lambda=1, `wrong-ai-check` has the smallest raw burden (0.55) but fails to separate all required pairs. `constraint-shift` is the cheapest feasible full separator at burden 1.10; `transfer` costs 1.25 and `generic-viva` 6.00.

### Probabilistic benchmark
For `data/probabilistic_probe_benchmark.csv`, learner responses are noisy. The test criterion becomes decision-relative expected information. A probe is eligible only if it reaches a declared minimum information threshold; among eligible probes, RBE selects the minimum burden. This explicitly falsifies the simplistic rule "always choose the cheapest probe." Targeted probes are also compared with generic viva using expected decision information per burden.

Both are mechanism results under declared observations/probabilities, not real-world educational-effectiveness claims.

## Rule for future work

Whenever a test has scientific significance: (1) commit executable test code, (2) commit the input dataset or deterministic generator, (3) commit/report its interpretation and limitations, and (4) append a row here. Human-study results must identify provenance, sample, protocol, uncertainty, and ethics/consent status where applicable.
