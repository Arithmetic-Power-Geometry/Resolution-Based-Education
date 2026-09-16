# OULAD fixed-vs-adaptive real-data comparison

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Execution

GitHub Actions run 35070743794 completed successfully at commit `9d2e8304853cdf7d98e76b59da33e6ac6a409f95`. The offline falsification suite passed 4/4 tests and the full OULAD benchmark completed. The workflow artifact `oulad-final-comparison-results` (artifact ID 10436227392; SHA256 `55573b5947e71d0553e627866c5998f3bc06e968948c488d7e0dd5e672f94d6f`) contains the complete comparison table and learned acquisition-order table.

OULAD is observational and predates RBE and generative AI. This experiment is therefore a retrospective computational proxy, not a randomized educational trial and not causal evidence that RBE improves learning.

## Held-out comparison

Students were group-disjoint across train/validation/test. Acquisition order was learned without test labels. Results were evaluated at 60, 90, and 120 day cutoffs, with all records and completer-only sensitivity, and posterior decision-risk thresholds epsilon = 0.05, 0.10, 0.20.

At cutoff 120, all outcomes, n=6,505 held-out student-module records:

- OBE-style score baseline: risk 0.239662, accuracy 0.760338, Brier 0.159473, AUC 0.834737, burden 1.
- Enhanced fixed all-evidence: risk 0.214297, accuracy 0.785703, Brier 0.140343, AUC 0.880163, burden 6.
- RBE adaptive, epsilon 0.20, resolved cases only: coverage 0.527287, risk 0.088047, accuracy 0.911953, burden 3.633205.
- Fixed matched-budget prefix: risk 0.216141, accuracy 0.783859, Brier 0.141077, AUC 0.879183, burden 4.

The adaptive risk/coverage pattern is repeated at cutoff 90 (epsilon 0.20: coverage 0.444581, resolved risk 0.083679, burden 3.967871) and cutoff 60 (coverage 0.527902, resolved risk 0.174723, burden 3.601998). Completer-only cutoff 120 gives coverage 0.641283, resolved risk 0.138889, burden 2.955689.

## Scientific interpretation

This is significant evidence for the *selective-resolution mechanism*: an adaptive protocol can stop on a subset for which its posterior risk criterion is satisfied while using less evidence than collecting every channel for everyone. It does **not yet establish superiority over fixed evidence**, because the reported low risk is conditional on the adaptively selected resolved subset, whereas the fixed baselines above are evaluated at 100% coverage. Comparing 8.8% selective risk with 21.4% full-coverage risk directly would be unfair.

The forced-decision RBE predictions do not materially beat enhanced fixed all-evidence; at cutoff 120 they have the same 0.214297 classification risk. This negative result is retained.

## Final falsification gate

Before making a comparative claim, compare RBE with fixed baselines at matched coverage and with matched evidence burden. Specifically:

1. For each RBE coverage level, select the most confident score-only and fixed-all-evidence cases to the same coverage and measure their held-out selective risk.
2. Compare RBE to a validation-learned fixed prefix at matched burden.
3. Add a random acquisition-order/null policy so any benefit cannot be attributed merely to abstention or feature count.
4. Repeat across 60/90/120 cutoffs and completer-only sensitivity.

Only an advantage surviving these controls should be described as evidence for adaptive resolution beyond ordinary selective prediction.
