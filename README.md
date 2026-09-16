# Resolution-Based Education (RBE)

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**  
Licensed under the Apache License, Version 2.0.

Resolution-Based Education (RBE) is an AI-era educational research architecture for **curriculum, teaching, learning, assessment, certification and feedback**. Its central question is not merely whether a student produced a high-quality answer, but whether the available evidence can resolve every learner distinction that the intended certification decision claims to make.

> **Do not certify only what a student produced. Certify the capabilities that remain distinguishable as belonging to the learner when tools, evidence, constraints and context change.**

## 1. Why RBE

A conventional educational pipeline often resembles:

`Curriculum -> Teach -> Test -> Score -> Grade`

RBE proposes a resolution-aware operating cycle:

`Define Capability -> Develop -> Produce -> Challenge -> Resolve -> Certify -> Develop Again`

The final feedback loop is essential: RBE is intended as an educational system architecture, not only an examination technique.

## 2. Six-layer architecture

### Layer 1 — Resolution Curriculum

RBE extends conventional learning outcomes into **Resolvable Capability Outcomes (RCOs)**:

`RCO = (C, E, P, D)`

where `C` is the capability claim, `E` the environments in which it should survive, `P` the permitted perturbations, and `D` the educational/certification distinction that must be resolved.

Example: rather than only “understand machine-learning algorithms,” an RCO may require a learner to select and justify a method for unfamiliar data, use permitted AI/tools appropriately, detect materially wrong recommendations, revise when assumptions change, and identify when evidence is insufficient.

### Layer 2 — Resolution Pedagogy: CCVRT

Teaching uses the **CCVRT cycle**:

`Construct -> Challenge -> Verify -> Revise -> Transfer`

Students construct a solution, encounter a meaningful challenge, verify evidence/AI/reasoning, revise the solution, and transfer the capability to a changed or unfamiliar setting. AI is not automatically prohibited; it becomes one controllable part of the epistemic environment.

### Layer 3 — Resolution Learning

RBE separates **Learning Evidence (LE)** from **Certification Evidence (CE)**. During learning, students may receive hints, collaborate, use AI, fail, retry and improve. Certification evidence has a different purpose: justify a decision about a declared capability. This separation is intended to prevent every learning interaction from becoming surveillance or examination.

### Layer 4 — Resolution Assessment

A standard instructional/assessment object is the **Resolution Episode**:

`Produce -> Perturb -> Explain -> Verify -> Adapt`

After initial evidence, RBE asks which materially different learner worlds remain compatible with it. A learner world is a hypothesis about capability sufficient to generate the observed evidence. Example constructed worlds are:

- `W1`: understands + effective AI use;
- `W2`: understands + weaker generation;
- `W3`: weak understanding + effective AI assistance;
- `W4`: weak understanding + blind AI reliance.

The point is not to identify every psychological state. RBE only needs to separate worlds that imply different educational decisions.

### Layer 5 — Resolution Certification

Let `W` be learner worlds, `A` an assessment protocol, and `g: W -> D` the intended certification rule. Let `w_i ~_A w_j` mean that evidence available under `A` cannot distinguish worlds `w_i` and `w_j`.

A **Certification-Assessment Resolution Gap (CARG)** exists when:

`w_i ~_A w_j` but `g(w_i) != g(w_j)`.

Therefore a necessary condition for perfect implementation of the certification rule using only evidence obtainable through `A` is:

`w_i ~_A w_j  =>  g(w_i) = g(w_j)`.

If a CARG remains, RBE searches for a **Minimum Resolution-Restoring Perturbation (MRRP)**:

`e* = argmin_e [ cost(e) + lambda * leakage(e) ]`

subject to the intervention separating the still-compatible certification-incompatible worlds to the required standard.

This yields the operational RBE question:

> **Find the cheapest low-leakage experiment for which the currently compatible, decision-incompatible possible worlds make mutually incompatible predictions.**

Crucially, the cheapest experiment is not the experiment with the smallest raw price. It is the cheapest **feasible resolving** experiment. A very cheap probe that separates only one problematic pair does not solve the certification problem.

RBE assessment is therefore naturally **variable-length**. Assessment stops when the remaining compatible worlds are decision-homogeneous; another learner may require additional targeted perturbations. Fairness must consequently be studied in terms of equivalent certification standards, measurement invariance and burden—not assumed from identical test length.

### Layer 6 — Resolution Feedback

Resolved evidence is summarized in a **Capability Passport**, for example conceptual foundation, tool/AI augmentation, verification, constraint adaptation, transfer, uncertainty judgment and independent floor. A **Resolution Ledger** records the RCO, evidence type, perturbations, observations, resolution state, decision, burden and leakage needed to justify certification. Privacy-preserving deployment is a separate design requirement.

## 3. CARG, AIRC and MRRP

**CARG — Certification-Assessment Resolution Gap:** the assessment merges learner worlds that the certification rule requires treating differently.

**AIRC — AI-Induced Resolution Collapse:** AI-mediated production can enlarge observational-equivalence classes, making capability states that matter for certification indistinguishable to artifact-only assessment. This is not the claim that AI necessarily harms learning; it is a claim about assessment resolution.

**MRRP — Minimum Resolution-Restoring Perturbation:** the lowest-burden, low-leakage intervention sufficient to restore the missing decision-relevant distinction.

## 4. AI as an educational variable

RBE is not an anti-AI system. Resolution Episodes may deliberately vary `AI+`, `AI-`, misleading AI, uncertain AI, supporting/conflicting evidence, changed constraints, or unfamiliar representations. The target question becomes whether the learner can appropriately accept, reject, verify, revise, defer, seek evidence and transfer—not simply whether the learner can reproduce an answer without a tool.

## 5. Resolution Engine

The executable reference implementation follows:

`Current evidence K_t -> compatible worlds W(K_t) -> certification-homogeneous?`

If yes, stop and record the resolved decision. If no, CARG remains and the engine selects the next MRRP. The process repeats until resolution or an explicit resource/uncertainty limit is reached. Production evidence is therefore a starting observation, not automatically a capability score.

## 6. Current cheapest-experiment benchmark

The repository includes `data/cheapest_experiment_benchmark.csv`. In its declared constructed world model, all four worlds initially produce the same excellent artifact, but W1/W2 and W3/W4 require opposite certification decisions. Thus four cross-decision pairs remain unresolved.

At `lambda = 1`:

| Candidate | Cost | Leakage | Burden | Full decision separator? |
|---|---:|---:|---:|---|
| wrong-ai-check | 0.50 | 0.05 | 0.55 | No |
| constraint-shift | 1.00 | 0.10 | **1.10** | **Yes** |
| transfer | 1.20 | 0.05 | 1.25 | Yes |
| generic-viva | 5.00 | 1.00 | 6.00 | Yes |

Therefore **constraint-shift is the cheapest feasible resolving experiment in this constructed benchmark**. The cheaper wrong-AI check is insufficient because some certification-incompatible worlds still make the same prediction. This is a formal/mechanism result under declared observations, not human educational evidence.

## 7. Test registry

Scientifically meaningful tests are preserved in executable form and appended to `reports/TEST_REGISTRY.md`.

Current registered tests:

1. **T001 Artifact-only CARG** — verifies structural non-identifiability when identical artifact evidence is compatible with opposite certification decisions.
2. **T002 Cheapest full separator** — verifies MRRP chooses the cheapest feasible full separator rather than the cheapest raw probe.
3. **T003 Resolution restoration** — verifies the selected perturbation removes CARG in the constructed case.
4. **T004 Leakage sensitivity** — verifies changing `lambda` can change the optimal resolving intervention.
5. **T005 No-CARG resolved control** — sanity check that already decision-resolving observations are not incorrectly flagged.

Repository rule: whenever a new test has scientific significance, save (a) executable test code, (b) its dataset or deterministic generator, (c) interpretation/limitations, and (d) an appended Test Registry entry. Synthetic evidence must never be represented as human educational evidence.

Run the current tests with:

```bash
pytest -q
```

## 8. What RBE is compared against

RBE must be empirically compared with appropriate alternatives rather than declared superior. Important comparison families include conventional OBE/fixed examinations, authentic assessment, oral/AI-viva approaches, IRT/CAT and cognitive diagnosis where applicable, Evidence-Centered Design, dynamic assessment, and fixed multi-probe assessment. The comparison target depends on the research question.

The decisive human study should compare at least:

`Conventional assessment vs fixed AI-viva/authentic assessment vs adaptive RBE`

on the same declared capability standards. Outcomes should include future unseen transfer, misleading-AI/error detection, verification, calibration, decision accuracy, unresolved/abstention rate, assessment time/burden, inter-rater reliability, subgroup measurement invariance/fairness, and predictive validity.

## 9. Novelty boundary

RBE does **not** claim invention of optimal experimental design, decision trees, information gain, teaching dimension, minimum test cover, adaptive distinguishing sequences, Blackwell informativeness, value of information, IRT/CAT, ECD, dynamic assessment, authentic assessment, selective classification or viva voce assessment.

The research hypothesis is narrower: **certification resolution, AI-induced resolution collapse, and minimum resolution-restoring assessment are integrated as an AI-era educational architecture spanning curriculum, pedagogy, learning, assessment, certification and feedback.** Continued prior-art review and empirical validation are required before stronger novelty/effectiveness claims.

## 10. Research status and evidence ladder

**Current status: theoretical and computational research prototype.**

Evidence ladder:

`Formal definitions -> constructed counterexamples -> deterministic tests -> noisy simulation -> retrospective/real dataset validation -> prospective student study -> multi-course/institution replication`

Passing software tests proves implementation properties under their assumptions; it does not prove educational effectiveness. Real-world superiority claims require controlled human evidence, psychometric analysis, fairness analysis and external replication.

## 11. Repository map

- `rbe/core.py` — formal deterministic CARG/MRRP kernel.
- `rbe/system.py` — six-layer RBE reference objects and adaptive Resolution Episode.
- `tests/test_core.py` — foundational CARG/MRRP tests.
- `tests/test_cheapest_experiment.py` — cheapest resolving-experiment, restoration and leakage-sensitivity tests.
- `data/cheapest_experiment_benchmark.csv` — auditable candidate-experiment benchmark.
- `reports/TEST_REGISTRY.md` — cumulative scientific test ledger and interpretations.
- `LICENSE`, `NOTICE` — Apache-2.0 licensing and attribution.

## 12. Next development sequence

1. Extend deterministic worlds to probabilistic observations and posterior uncertainty.
2. Compare greedy MRRP against exhaustive optimal decision trees on small world sets.
3. Add abstention/unresolved certification when no admissible probe achieves required confidence.
4. Add assessment leakage and decision-neutral admissibility constraints explicitly.
5. Add noisy synthetic cohorts and calibration/Brier/burden comparisons.
6. Add fairness and subgroup-invariance stress tests.
7. Freeze a preregistered human-study protocol before using real student outcomes.
8. Validate on real anonymized educational data with appropriate permissions/ethics.
9. Compare conventional OBE, fixed AI-viva/authentic assessment and adaptive RBE prospectively.
10. Replicate across subjects and institutions before proposing institutional replacement.

## License

Apache License 2.0. See `LICENSE` and `NOTICE`.
