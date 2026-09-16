# OULAD burden bootstrap — final statistical stop gate

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Purpose
Quantify uncertainty in the surviving real-data result after matched-coverage falsification: adaptive RBE reduces evidence burden relative to collecting all six logged evidence channels. This test does **not** test predictive superiority.

## Execution
GitHub Actions run `35074988489` completed successfully. Offline bootstrap controls passed 3/3. The full official OULAD benchmark used cutoff 120, all outcomes, epsilon=0.20, held-out n=6,505 student-module records, and 5,000 paired bootstrap resamples.

Workflow artifact: `oulad-burden-bootstrap-results`, artifact ID `10437304387`, SHA256 `b8fdb3073a7782e1001f588c834d79f7acaab9e7a8f0b7e8e1b6c29388dbdb0e`.

## Result
- Fixed-all evidence burden: 6.000000 channels.
- RBE mean evidence burden: 3.633205 channels.
- Mean saving: 2.366795 channels.
- Relative saving: 0.394466 (39.45%).
- 95% percentile bootstrap CI for mean saving: [2.311145, 2.423682] channels.
- Empirical one-sided bootstrap probability of saving <= 0, with +1 correction: 0.0002.
- RBE resolved coverage: 0.527287.

## Interpretation
The evidence-burden reduction is stable under the declared held-out OULAD setup. This supports an evidence-efficiency claim for selective resolution. It does not establish that adaptive RBE has lower classification risk than strong confidence-based fixed evidence; the matched-coverage falsification already rejected consistent risk dominance.

## Stop decision
This completes the planned empirical stop gate. Further exploratory tests are not required for the present manuscript. The paper should now be frozen around: Certification–Assessment Resolution Gap (CARG), Certification Resolution Necessity, Minimum Resolution-Restoring Perturbation, risk-constrained adaptive resolution, and the empirically supported evidence-efficiency result with explicit negative controls.
