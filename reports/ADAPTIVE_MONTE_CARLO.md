# Adaptive RBE Monte Carlo — Saved Result

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Purpose
Stress-test the RBE question: *find the cheapest experiment that reduces decision-relevant ambiguity among currently compatible learner worlds*, now over 20,000 noisy synthetic learner episodes.

## Reproducible setup
Seed: 20260916. Four equally likely learner worlds. W1/W2 certify; W3/W4 do not. Decision posterior threshold: 0.90. Response probabilities and burdens are declared in the benchmark code/data.

Compared protocols:
1. Adaptive RBE: constraint-shift -> wrong-AI -> transfer -> generic viva, stopping immediately when certification posterior crosses the threshold.
2. Fixed targeted: wrong-AI -> constraint-shift -> transfer, with the same early decision rule.
3. Fixed viva: one generic viva.

## Saved results
| Protocol | Resolved | Unresolved | Error/all | Error/resolved | Mean burden | Mean probes |
|---|---:|---:|---:|---:|---:|---:|
| Adaptive RBE | 0.9645 | 0.0355 | 0.08305 | 0.08611 | 2.4455 | 1.8261 |
| Fixed targeted | 0.77355 | 0.22645 | 0.04990 | 0.06451 | 2.0769 | 2.3415 |
| Fixed viva | 0.46860 | 0.53140 | 0.03600 | 0.07682 | 6.0000 | 1.0000 |

## Significant mechanism findings
Adaptive RBE resolves 96.45% of episodes versus 77.36% for fixed targeted and 46.86% for one generic viva. Its mean burden is about 59% lower than generic viva (2.4455 vs 6.0), and adaptive stopping uses fewer probes on average than the targeted sequence (1.826 vs 2.342).

## Crucial falsification result
Adaptive RBE does **not** dominate every metric. Its error among resolved cases is 8.61%, versus 6.45% for fixed targeted in this declared synthetic model. This negative result is deliberately preserved. It shows that maximizing resolution alone can over-resolve uncertain cases. A publishable RBE algorithm therefore needs an explicit joint constraint on ambiguity, error/risk and burden rather than a resolution-only objective.

## New research consequence
The next candidate principle is **Risk-Constrained Minimum Resolution**: choose the minimum-burden adaptive experiment policy that reaches sufficient decision resolution *without exceeding a declared posterior decision-risk bound*. This is not claimed as new generic mathematics; constrained sequential decision/testing has established ancestors. The potentially novel contribution remains its role inside CARG/AIRC/MRRP educational certification.

## Evidence boundary
All results are synthetic mechanism validation. No claim about real students, educational effectiveness, fairness, predictive validity or institutional superiority follows from these numbers.
