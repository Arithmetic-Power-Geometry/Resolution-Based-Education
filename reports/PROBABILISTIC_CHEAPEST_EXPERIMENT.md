# RBE Test Report — Probabilistic Cheapest Experiment

Copyright (C) 2026 Mohammad Amir Khusru Akhtar  
Apache License 2.0

## Research question

Given current knowledge that leaves learner worlds W1–W4 compatible with the same strong artifact, which experiment is the cheapest one that supplies a declared minimum amount of certification-decision information under noisy responses?

## Benchmark

The synthetic benchmark is stored in `data/probabilistic_probe_benchmark.csv`. W1/W2 require certification and W3/W4 do not. All four have the same artifact score, deliberately creating artifact-level resolution collapse. Probe responses are probabilistic rather than deterministic.

The probes are:

- wrong-AI check: burden = 0.55
- constraint shift: burden = 1.10
- transfer: burden = 1.25
- generic viva: burden = 6.00

Burden = direct cost + leakage for lambda=1.

## Decision-relative information criterion

Initial decision entropy is 1 bit because the prior places equal mass on certify and do-not-certify worlds. For a probe e, define its decision information as the expected reduction in entropy of the certification decision, not entropy of the exact latent world.

This distinction is important: RBE does not need to identify every learner-world detail if all remaining worlds imply the same certification decision.

## Findings encoded as tests

1. The artifact-only observation has zero decision information in this constructed benchmark.
2. Every declared perturbation reduces decision uncertainty to some degree.
3. The identity of the cheapest useful experiment depends on the required resolution threshold. A cheap weak probe can be sufficient for a modest threshold but fail a stronger threshold.
4. Under the declared probabilities, targeted probes provide more decision information per burden than the expensive generic viva.

## Scientific significance

This test prevents the phrase "cheapest experiment" from being interpreted as "always choose the lowest monetary/time cost." The correct RBE formulation is constrained optimization:

`min burden(e)` subject to `decision_information_gain(e) >= tau`,

or an adaptive policy that continues until a declared decision-risk/resolution criterion is met.

The threshold tau must be justified by the certification context. It cannot be chosen after observing results merely to make RBE look better.

## Boundary of evidence

These probabilities are synthetic mechanism-validation assumptions, not empirical estimates of student behaviour. The result establishes software behavior and a falsifiable experimental design. It does not establish educational superiority, predictive validity, fairness, or real-world effect size.

## Next falsification step

Run Monte Carlo cohorts with response noise, unequal priors, heterogeneous probe reliability, and multiple decision thresholds. Compare adaptive RBE against fixed-viva and fixed-multi-probe protocols on decision error, unresolved rate, total burden, leakage, and calibration. Then repeat with real anonymized student data.
