# OULAD OBE–RBE Comparison Protocol

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Purpose
This protocol provides a real-data comparison for the first RBE paper without mislabeling OULAD as an RBE intervention trial.

## Data
Open University Learning Analytics Dataset (OULAD): 32,593 student-module records, 173,912 assessment records, and 10,655,280 VLE interaction records. Final result is reduced to certify = Pass/Distinction versus non-certify = Fail/Withdrawn.

## Comparator definition
The baseline is an **OBE-style outcome-evidence baseline**, not a claim that all OBE implementations use only scores. It uses evidence naturally aligned with conventional outcome-attainment measurement available in OULAD: assessment score and assessment completion/count up to a declared cutoff.

RBE is operationalized as a **resolution layer added to the same outcome evidence**. It asks whether students who remain observationally compatible under the baseline nevertheless have opposite eventual certification outcomes, then searches additional admissible evidence channels for the lowest-burden channel that reduces this decision-incompatible mass.

## Primary comparison
1. OBE-style baseline: early/mid-course assessment evidence.
2. Enhanced OBE control: assessment score + assessment count.
3. RBE observational proxy: baseline plus candidate evidence channels selected by decision-resolution gain per declared burden.

Candidate channels available in OULAD are VLE clicks, active days, VLE record count, and submission timing. These are observational proxies, not designed perturbations.

## Primary endpoint
Unresolved decision mass: fraction of student-module records lying in an observational cell containing both eventual certify and non-certify outcomes.

## Cheapest-experiment criterion
For candidate evidence e,

    efficiency(e) = [U(A) - U(A + e)] / burden(e)

where U is unresolved decision mass. The cheapest useful evidence is the minimum-burden candidate meeting a prespecified resolution-gain requirement; with equal unit burdens, it is the candidate with greatest gain.

## Required robustness
Report cutoffs (30, 60, 90, 120 days), partition resolutions (q = 3, 5, 10), module/presentation strata, bootstrap confidence intervals, and sensitivity to declared evidence cost. Do not claim RBE superiority unless the RBE proxy improves a prespecified decision-resolution or predictive-validity endpoint robustly over both baseline and enhanced OBE controls.

## Current full-data finding
At cutoff 120 and q=5, assessment-score-only evidence leaves unresolved mass 1.000. Adding VLE clicks reduces it to 0.999632 (gain 0.000368); assessment count and VLE-record count each gain 0.000061; submission timing gains 0.000031; active days gains 0.000000. Thus the current coarse partition benchmark does **not** establish practical superiority of RBE. Its near-zero gains are a scientifically important negative result and show that the original partition endpoint is too coarse for the claimed comparison.

## Next test
Replace the coarse mixed-cell endpoint with out-of-sample decision metrics: AUC, Brier score, log loss, calibration error, selective risk/coverage, and false-certification/false-non-certification rates. Compare score-only OBE-style evidence, enhanced OBE evidence, all-evidence fixed model, and an adaptive RBE evidence-acquisition policy under matched evidence budgets.

## Limitation
OULAD predates current generative AI and contains no randomized perturbations. It can support a real-data comparison of evidence architectures and decision resolution, but cannot by itself prove causal superiority of RBE pedagogy or AI-era perturbations.