# Resolution-Based Education (RBE)

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**  
Licensed under the Apache License, Version 2.0.

Resolution-Based Education (RBE) is an AI-era educational framework for developing and certifying learner capability through adaptive perturbation, verification, transfer, and the minimum evidence required to distinguish educationally consequential learner states.

> Do not certify what a student produced. Certify the capabilities that remain distinguishable as belonging to the student when tools, evidence, constraints, and context change.

## Core architecture

RBE combines:

- **CCVRT learning cycle** — Construct → Challenge → Verify → Revise → Transfer.
- **CARG** — Certification–Assessment Resolution Gap: detects when an assessment cannot distinguish learner states that a certification rule treats differently.
- **AIRC** — AI-Induced Resolution Collapse: studies when AI-mediated production enlarges observational-equivalence classes and hides certification-relevant learner differences.
- **MRRP** — Minimum Resolution-Restoring Perturbation: chooses the lowest-burden, lowest-leakage intervention that restores a missing certification distinction.
- **Resolution Episodes** — short adaptive assessment episodes that perturb evidence, constraints, representation, or AI reliability until decision-relevant ambiguity is resolved.

## Formal kernel

Let `W` be a set of learner worlds, `A` an assessment protocol, and `g: W → D` the intended certification decision. Let `w_i ~_A w_j` mean that `A` cannot distinguish the two learner worlds from evidence available under the protocol.

A Certification–Assessment Resolution Gap exists when

```text
w_i ~_A w_j  but  g(w_i) != g(w_j).
```

Necessary condition for perfect implementability of the certification rule using only evidence available under `A`:

```text
w_i ~_A w_j  =>  g(w_i) = g(w_j).
```

MRRP searches for an intervention `e*` such that

```text
e* = argmin_e [cost(e) + lambda * leakage(e)]
```

subject to certification-incompatible learner worlds becoming observationally distinguishable to a required confidence level.

## Why this is not simply another AI-proof exam

RBE permits legitimate use of AI and other professional tools during authentic production. The submitted artifact is evidence, not automatically a direct measurement of learner capability. When the artifact leaves certification-relevant explanations unresolved, RBE chooses a targeted perturbation rather than automatically adding more conventional questions.

The framework therefore separates:

1. **system performance** — what learner + AI can produce;
2. **learner-attributable capability** — what the learner can explain, verify, adapt, transfer, and responsibly control;
3. **certification resolution** — whether available evidence is sufficient for the decision the institution claims to make.

## Novelty boundary

RBE does **not** claim novelty for the underlying mathematics of optimal experimental design, decision trees, information gain, teaching dimension, test cover, adaptive distinguishing sequences, Blackwell informativeness, evidence-centered design, item-response theory, dynamic assessment, authentic assessment, or viva voce assessment.

The research hypothesis is narrower: the distinctive contribution is the educational formulation of **certification resolution**, **AI-induced resolution collapse**, and **minimum resolution-restoring assessment** as one integrated pedagogy–assessment–certification architecture.

This claim requires continued systematic prior-art review and empirical validation.

## Repository goals

- Formalize the RBE theory and assumptions.
- Provide reproducible toy counterexamples and simulations.
- Implement CARG detection and MRRP selection algorithms.
- Compare fixed artifact assessment, fixed multi-probe assessment, and adaptive resolution assessment.
- Add benchmark scenarios for misleading AI, changed constraints, transfer, verification, and evidence revision.
- Support university pilots layered on top of existing OBE/CBCS/credit systems.
- Report burden, leakage, classification accuracy, calibration, fairness, and transfer-prediction metrics.

## Research status

**Current status: theoretical and computational research prototype.** RBE is not yet a validated replacement for existing institutional assessment systems. Claims of improved educational performance must be established through controlled studies with students and appropriate psychometric, fairness, and validity analyses.

## License

Apache License 2.0. See `LICENSE` and `NOTICE`.
