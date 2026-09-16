# RBE Novelty and Performance Report

Copyright (C) 2026 Mohammad Amir Khusru Akhtar  
Licensed under the Apache License, Version 2.0.

## Scope

This report evaluates Resolution-Based Education (RBE) against neighboring educational-assessment ideas. It distinguishes the framework's proposed contribution from established methods and separates structural performance demonstrated in toy models from educational performance that still requires human validation.

## RBE core claim

RBE treats a submitted artifact as evidence rather than as automatic proof of learner capability. It asks whether the assessment protocol can distinguish learner states that the certification rule treats differently. If not, it detects a Certification–Assessment Resolution Gap (CARG) and seeks a Minimum Resolution-Restoring Perturbation (MRRP).

## Comparison with established approaches

| Approach | Established focus | Overlap with RBE | Proposed RBE distinction |
|---|---|---|---|
| Bloom / higher-order assessment | Cognitive process levels | Higher-order tasks, transfer | RBE focuses on certification-relevant distinguishability, not taxonomy level |
| IRT / CAT | Latent ability estimation and informative item selection | Adaptive assessment | RBE adapts interventions to resolve decision-incompatible learner worlds |
| Cognitive diagnostic assessment | Attribute mastery profiles | Mechanism diagnosis | RBE stops once certification-relevant ambiguity is resolved |
| Evidence-Centered Design | Student/evidence/task models | Validity-oriented design | RBE adds an explicit resolution criterion over certification decisions |
| Dynamic assessment | Learning potential under mediation | Interactive/adaptive support | RBE separates low-leakage certification probes from teaching interventions |
| Authentic assessment | Realistic performance and process | Tool-rich tasks, process evidence | RBE formalizes when authentic evidence remains insufficient for certification |
| AI viva / epistemic ownership | Verify understanding of AI-assisted work | Follow-up questioning | RBE is broader than ownership and selects probes by unresolved certification distinctions |
| GenAI assessment literacy | AI-use judgment, verification, integrity | Verification and responsible AI use | RBE is an assessment architecture rather than a learner self-report construct |
| Blackwell / value-of-information / OED | Informativeness and experiment choice | Cost-sensitive evidence acquisition | RBE does not claim these mathematics as novel; it applies them to educational certification resolution |
| Teaching dimension / test cover / distinguishing sequences | Efficient state discrimination | Minimum discriminating tests | RBE's proposed novelty is the education-specific certification-resolution formulation and AI-induced collapse mechanism |

## Novelty boundary

RBE should **not** claim invention of adaptive testing, information gain, minimum-cost testing, decision trees, optimal experimental design, observational equivalence, dynamic assessment, authentic assessment, viva voce, or ECD.

The narrower and more defensible novelty hypothesis is the integrated educational theory:

1. **CARG** — a credential may demand distinctions that its own assessment protocol cannot observe;
2. **AIRC** — AI-mediated production can collapse previously visible certification-relevant distinctions;
3. **MRRP** — restore only the missing decision-relevant resolution using a minimum-burden, low-leakage perturbation;
4. **Resolution Episodes** — operationalize this process inside teaching and assessment;
5. **RBE** — connect the CCVRT learning cycle with certification-resolution logic in one educational architecture.

## Structural performance demonstrated by the reference tests

The included deterministic toy tests verify three properties:

- an artifact-only protocol can contain a CARG when all learner worlds produce the same artifact but require different certification decisions;
- a follow-up observation that separates pass/fail world classes removes that CARG;
- among interventions that fully restore the required resolution, MRRP chooses the lowest burden under the specified cost + leakage objective.

These are **logical/computational properties**, not evidence that RBE improves real student learning or psychometric validity.

## Performance hypotheses for empirical testing

A university pilot should compare at least three conditions:

1. fixed conventional assessment;
2. AI-enabled artifact + fixed follow-up viva;
3. RBE adaptive resolution assessment.

Primary endpoints should include:

- accuracy for predicting independently measured future transfer performance;
- false-certification and false-rejection rates;
- assessment minutes per learner;
- number of probes per learner;
- calibration of certification confidence;
- robustness to misleading AI and changed constraints;
- fairness across learner groups;
- assessment leakage;
- inter-rater / model-assisted decision reliability;
- student and faculty burden.

A strong empirical result would show that RBE reaches equal or better certification validity with fewer probes/minutes than a fixed follow-up protocol. Until such a study is run, no claim of superior educational performance is warranted.

## Current conclusion

RBE is best described as a **novel, testable educational-framework candidate with a defensible conceptual residue**, not yet as a proven superior pedagogy. The repository currently establishes a formal kernel, explicit novelty boundary, executable structural tests, and a roadmap for empirical validation.
