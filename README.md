# Resolution-Based Education (RBE)

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**  
Licensed under the Apache License, Version 2.0.

Resolution-Based Education (RBE) is a research architecture for **curriculum, teaching, learning, assessment, certification, attainment and continuous improvement** in tool-rich and generative-AI environments. Its core question is not merely whether a learner produced a high-quality answer, but whether the available evidence resolves the distinction that the intended certification decision claims to make.

> **Outcomes remain essential, but outcomes are not self-certifying.**

## 1. Scientific-paper scope versus full framework

This repository supports two linked outputs:

1. **Paper V2 — scientific paper:** formalizes the Certification-Assessment Resolution Gap (CARG), proves the Certification Resolution Necessity result, develops burden-aware adaptive resolution, and tests the mechanisms with deterministic, probabilistic, Monte Carlo and retrospective real-data evidence.
2. **RBE framework — broader system specification:** extends the scientific core to curriculum, pedagogy, examination, attainment, programme evaluation, governance, accessibility, quality assurance, accreditation compatibility, privacy and implementation.

The paper intentionally does **not** claim to be the complete institutional framework. A separate framework paper/specification can address the full system without overloading the first scientific article.

## 2. Core formal objects

### Resolvable Capability Outcome

`RCO = (C, E, P, D)`

- `C`: capability claim;
- `E`: relevant environments and legitimate tool conditions;
- `P`: admissible perturbation/evidence family;
- `D`: certification distinction.

### Certification-Assessment Resolution Gap

Let `W` be learner worlds, `A` an assessment protocol, and `g: W -> D` the intended certification rule. Let `w_i ~_A w_j` mean that evidence obtainable under `A` cannot distinguish worlds `w_i` and `w_j`.

A **CARG** exists when:

`w_i ~_A w_j` but `g(w_i) != g(w_j)`.

Hence a necessary condition for perfect implementation of the certification rule using only `A`-evidence is:

`w_i ~_A w_j  =>  g(w_i) = g(w_j)`.

### Conservative extension / zero-additional-evidence rule

If existing evidence `K0` already satisfies the declared resolution criterion, RBE adds no further assessment:

`resolution-adequate OBE -> B_additional = 0`.

RBE is therefore designed as an extension of outcome-based assessment, not as a claim that OBE is obsolete or incapable of rich assessment.

## 3. Performance and certification resolution are separate

RBE preserves marks/grades and treats certification resolution as a separate decision variable.

For learner `i` and RCO `j`:

`A_ij = 1[S_ij >= T_j]`

where `S_ij` is performance evidence and `T_j` is the performance threshold.

For a probabilistic resolution model:

`Q+_ij = 1[r_ij <= epsilon_j and Dhat_ij = d+_j]`

where low risk must also support the **positive** certification decision. Resolved Capability Attainment is:

`RCA_ij = A_ij * Q+_ij`.

Operational states remain visible:

- `AR`: attained + resolved-positive;
- `AU`: performance-attained but unresolved;
- `RN`: performance-attained but resolved-negative, where institutionally meaningful;
- `NA`: not attained;
- `Deferred`: further authorized evidence may still be collected.

Course metrics implemented in `rbe/attainment.py` include `PAR`, `RR`, `RAR`, `UAR`, `RNR`, `DR`, and `MRB`.

## 4. One-step probe versus complete resolution policy

A one-step probe can be informative without actually restoring certification resolution. The repository therefore distinguishes:

- a **one-step discriminating/resolving probe** for toy cases where one intervention is sufficient; and
- an **adaptive resolution policy/tree** whose terminal leaves meet the declared decision criterion.

For an adaptive policy `pi`, the framework objective is conceptually:

`min E[B(pi)]`

subject to terminal decision resolution and validity, reliability, accessibility, fairness, privacy and burden constraints.

`rbe/policy.py` contains an exact small-world deterministic policy search used to test this distinction.

## 5. Teaching and assessment architecture

RBE pedagogy uses the **CCVRT cycle**:

`Construct -> Challenge -> Verify -> Revise -> Transfer`

Learning Evidence and Certification Evidence remain distinct (`LE != CE`). During learning, hints, collaboration, retries and AI assistance may be useful. Certification evidence is collected under declared conditions appropriate to the claim.

A Resolution Episode can use:

`Produce -> Perturb -> Explain -> Verify -> Adapt`.

Perturbations may include constraint shifts, transfer, contradictory evidence, misleading AI, tool/resource changes, explanation/justification, uncertainty/defer scenarios, and recovery after failure.

AI is not automatically prohibited. Depending on the capability claim, an assessment can be AI-free, AI-permitted, AI-required, AI-adversarial, or AI-uncertain.

## 6. Resolution Engine

The core loop is:

`K_t -> compatible worlds / posterior -> resolved?`

- If yes: stop.
- If no: identify certification-incompatible alternatives and acquire the least-burdensome admissible discriminating evidence.
- Repeat only within the declared burden cap.
- If resolution remains insufficient: return `Unresolved/Deferred` rather than manufacture certainty.

This is naturally variable-length. Fairness therefore requires equivalent decision standards, accessibility, calibration and burden audits rather than an assumption that identical question counts are always fair.

## 7. Deterministic benchmark

The repository includes `data/cheapest_experiment_benchmark.csv`. In the declared toy model, four worlds initially produce the same excellent artifact while two require a positive and two a negative certification decision.

At `lambda = 1`:

| Candidate | Cost | Leakage | Burden | Full decision separator? |
|---|---:|---:|---:|---|
| wrong-ai-check | 0.50 | 0.05 | 0.55 | No |
| constraint-shift | 1.00 | 0.10 | **1.10** | **Yes** |
| transfer | 1.20 | 0.05 | 1.25 | Yes |
| generic-viva | 5.00 | 1.00 | 6.00 | Yes |

The constraint shift is therefore the cheapest **feasible full separator** in this constructed benchmark. This is a mechanism result under declared observations, not evidence of human educational superiority.

## 8. Current evidence and falsification boundary

The repository retains negative results. Current evidence includes:

- deterministic and probabilistic mechanism tests;
- a 20,000-episode Monte Carlo stress test;
- retrospective analysis of OULAD;
- matched-coverage confidence controls;
- random acquisition-order controls;
- a paired bootstrap uncertainty analysis of the surviving burden effect.

The present evidence **does not establish that adaptive RBE is more accurate than strong fixed evidence**. The retrospective OULAD result that survives falsification is narrower: selective adaptive acquisition reduced the number of evidence channels used under the declared proxy setup. OULAD predates GenAI and RBE and is not causal evidence of educational benefit.

A prospective human study remains necessary.

## 9. Novelty boundary

RBE does **not** claim invention of:

- outcome-based education;
- authentic or programmatic assessment;
- oral defence/viva;
- adaptive testing or sequential analysis;
- equivalence relations or partitions;
- Bayesian updating or information gain;
- Blackwell experiment comparison;
- selective classification/abstention;
- Pareto frontiers;
- dynamic assessment or evidence-centered design.

The proposed scientific contribution is the integration of these established ideas around a specific educational object: **compatibility between the resolution supplied by assessment evidence and the distinction required by a certification rule**.

## 10. Repository map

- `rbe/core.py` — deterministic CARG and one-step resolving-probe kernel.
- `rbe/probabilistic.py` — decision information and probabilistic probe selection.
- `rbe/system.py` — reference RCO, learner-world, resolution-episode and ledger objects.
- `rbe/attainment.py` — framework-synchronized performance/resolution states and course/programme metrics.
- `rbe/policy.py` — exact adaptive resolution-policy search for small deterministic world sets.
- `tests/` — executable tests, including attainment and policy-tree corrections.
- `benchmarks/` — Monte Carlo and OULAD studies.
- `reports/TEST_REGISTRY.md` — append-only scientific test ledger.
- `manuscript/main.tex` — scientific paper source.
- `manuscript/framework_sync.tex` — frozen-framework insert used for Paper V2 synchronization.
- `manuscript/SUBMISSION_CHECK.md` — submission/build QA record.
- `LICENSE`, `NOTICE` — Apache-2.0 licensing and attribution.

## 11. Reproducibility

Run the repository tests with:

```bash
pytest -q
```

The paper build is:

```bash
cd manuscript
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

Scientifically meaningful new tests should be preserved with executable code, data or deterministic generators, interpretation/limitations, and a test-registry entry. Synthetic results must not be represented as human educational evidence.

## 12. Research sequence

`Formal definitions -> constructed counterexamples -> deterministic tests -> noisy simulation -> retrospective real-data proxy -> prospective course study -> multi-course/institution replication -> validated institutional framework`

The first paper establishes the scientific core and its falsification boundary. The complete RBE educational operating framework is a separate, broader research output.

## License

Apache License 2.0. See `LICENSE` and `NOTICE`.
