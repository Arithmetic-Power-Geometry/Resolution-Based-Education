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

## Current significant result

For the benchmark in `data/cheapest_experiment_benchmark.csv`, artifact-only evidence maps W1-W4 to the same `excellent` observation while W1/W2 require certify and W3/W4 require do-not-certify. Four cross-decision pairs therefore remain unresolved. At leakage weight lambda=1, `wrong-ai-check` has the smallest raw burden (0.55) but fails to separate all required pairs. `constraint-shift` is the cheapest **feasible full separator** at burden 1.10; `transfer` costs 1.25 and `generic-viva` 6.00. This is a mechanism result under declared observations, not a real-world educational-effectiveness claim.

## Rule for future work

Whenever a test has scientific significance: (1) commit executable test code, (2) commit the input dataset or deterministic generator, (3) commit/report its interpretation and limitations, and (4) append a row here. Human-study results must identify provenance, sample, protocol, uncertainty, and ethics/consent status where applicable.
