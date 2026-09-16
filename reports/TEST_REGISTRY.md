# RBE Test Registry

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

This registry is append-only in spirit: every scientifically meaningful mechanism, comparison, robustness, calibration, fairness, burden, leakage, or predictive-validity test added to RBE should be recorded here. Constructed/synthetic tests must never be presented as human educational evidence.

| ID | Test | Scientific question | Data | Result / interpretation |
|---|---|---|---|---|
| T001 | Artifact-only CARG | Can identical artifact evidence leave worlds requiring opposite certification decisions observationally compatible? | Constructed W1-W4 | Structural non-identifiability construction. |
| T002 | Cheapest full separator | Which minimum cost+leakage intervention separates every unresolved certification-incompatible pair? | Constructed W1-W4 | Constraint-shift cheapest feasible full separator at declared costs. |
| T003 | Resolution restoration | Does selected MRRP remove CARG? | Constructed W1-W4 | Decision-homogeneous cells after resolving intervention. |
| T004 | Leakage sensitivity | Can lambda alter selected experiment? | Constructed competing probes | Burden/leakage tradeoff. |
| T005 | No-CARG resolved control | Does already-resolved protocol report no CARG? | Constructed W1-W4 | Control. |
| T006 | Initial decision entropy | Does balanced benchmark begin with one bit decision uncertainty? | Probabilistic W1-W4 | Probabilistic sanity check. |
| T007 | Positive probe information | Do noisy perturbations reduce certification uncertainty? | Probabilistic benchmark | Positive decision information gain. |
| T008 | Resolution-threshold dependence | Does cheapest qualifying experiment change with stricter resolution requirement? | Probabilistic benchmark | Cheapest is conditional on sufficient resolution. |
| T009 | Resolution efficiency vs generic viva | Can targeted probe yield more decision information per burden? | Probabilistic benchmark | Mechanism efficiency comparison. |
| T010 | Artifact zero-information control | Does identical artifact distribution yield zero decision information? | Probabilistic benchmark | Probabilistic CARG/AIRC control. |
| T011 | Adaptive resolution rate | Does adaptive RBE resolve more noisy episodes than fixed targeted and one-viva protocols? | 20,000 seeded synthetic episodes | Adaptive 96.45%; targeted 77.355%; viva 46.86%. |
| T012 | Adaptive burden vs viva | Is adaptive RBE lower burden than generic viva? | Same simulation | Mean 2.4455 vs 6.0. |
| T013 | Adaptive stopping efficiency | Does adaptive stopping use fewer probes than fixed targeted sequence? | Same simulation | Mean 1.8261 vs 2.3415 probes. |
| T014 | Error-tradeoff falsification | Does adaptive RBE fail to dominate fixed targeted assessment on resolved-case error? | Same simulation | Yes: 8.61% vs 6.45%; motivates risk-constrained resolution. |
| T015 | OULAD real-data CARG proxy | Does coarse early assessment evidence leave real students with opposite eventual certification outcomes in the same observational cells? | OULAD 32,593 student-module records | At cutoff 120, q=5, score-only unresolved mass = 1.000. |
| T016 | OULAD cheapest added evidence | Which equally costed logged evidence channel most reduces unresolved mass beyond assessment score? | OULAD assessment + 10,655,280 VLE rows | VLE clicks largest gain, 0.000368; effect is extremely small. |
| T017 | OULAD refinement monotonicity | Does adding a genuine evidence dimension avoid increasing unresolved mass under benchmark partition? | OULAD + implementation logic | Yes for tested channels; active-days gain = 0. |
| T018 | OBE-style baseline vs resolution layer | Does adding resolution-oriented evidence materially outperform assessment-score evidence on the current real-data endpoint? | OULAD | No practical advantage on coarse mixed-cell endpoint; negative result retained. |
| T019 | Enhanced OBE control requirement | Is score-only a sufficient comparator for an OBE claim? | OULAD protocol + OBE literature | No. Future comparison must include score + assessment-count/direct-evidence control. |
| T020 | Real-data supremacy falsification gate | Can current OULAD partition result justify 'RBE is superior to OBE'? | OULAD | No. Supremacy claim blocked pending out-of-sample predictive/calibration/risk comparison. |
| T021 | Full held-out OULAD execution | Does the corrected final benchmark execute on official OULAD with student-disjoint splits? | Official OULAD; held-out n=6,505 (all) / 4,491 completers | PASS. Workflow run 35070743794; offline falsification tests 4/4; numerical artifact saved. |
| T022 | Fixed evidence improves score baseline | Does enhanced fixed evidence improve held-out prediction over score-only evidence? | OULAD cutoff 120, all outcomes | YES: risk 0.239662 -> 0.214297; Brier 0.159473 -> 0.140343; AUC 0.834737 -> 0.880163. Important control: richer fixed evidence is already strong. |
| T023 | Adaptive selective resolution | Can adaptive RBE identify a lower-risk resolved subset at lower burden than collecting all six channels? | OULAD cutoff 120, epsilon 0.20 | YES descriptively: coverage 0.527287, risk 0.088047, burden 3.633205 vs fixed-all burden 6. Selection caveat applies. |
| T024 | Temporal sensitivity | Does the selective-resolution pattern occur before cutoff 120? | OULAD cutoffs 60/90/120 | YES descriptively. At epsilon 0.20: risk/coverage/burden = 0.1747/0.5279/3.602 (60), 0.0837/0.4446/3.968 (90), 0.0880/0.5273/3.633 (120). |
| T025 | Completer-only sensitivity | Does selective-resolution behavior persist after excluding Withdrawn outcomes? | OULAD cutoff 120, completer-only n=4,491, epsilon 0.20 | YES descriptively: coverage 0.641283, risk 0.138889, burden 2.955689. |
| T026 | Forced-decision falsification | Does adaptive acquisition improve full-coverage classification risk over enhanced fixed-all evidence? | OULAD cutoff 120 | NO: both classification risk 0.214297. Adaptive benefit cannot be claimed from forced decisions. |
| T027 | Selective-comparison validity gate | Can RBE resolved-only risk be compared directly with 100%-coverage fixed baselines? | OULAD analysis | NO. Must match coverage and add confidence-based fixed/selective and random-order controls before comparative claim. |
| T028 | Matched-coverage confidence falsification | At identical coverage, does adaptive acquisition consistently reduce selective risk relative to a fixed-all-evidence confidence selector? | Official OULAD; n=6,505 / 4,491; cutoffs 60/90/120 | NO consistent risk dominance. Examples: cutoff120 all eps=.20 RBE risk .088047 vs fixed confidence .073178; completers .138889 vs .129514. At eps=.10 all, RBE .022761 vs fixed .023256, a tiny reversal. Comparative superiority claim is rejected. |
| T029 | Adaptive burden advantage | Does adaptive acquisition use less evidence than fixed-all confidence selection at matched coverage? | Same OULAD falsification | YES consistently in tested settings. At cutoff120 all: burden 4.581706 vs 6 at eps=.10 and 3.633205 vs 6 at eps=.20; completers 4.544645 and 2.955689 vs 6. This is an efficiency result, not a risk-superiority result. |
| T030 | Random-order acquisition control | Does the learned adaptive acquisition order clearly dominate random evidence orders? | Same OULAD; 100 random orders | NO clear risk dominance. RBE is generally near the random-order mean and the best random order can have lower risk. Example cutoff120 all eps=.20: RBE .088047 vs random mean .089970, best .087678. Order-specific superiority is not established. |
| T031 | Final empirical claim boundary | Does current OULAD evidence justify claiming RBE is predictively superior to enhanced OBE/fixed evidence? | All real-data tests through workflow 35071457218 | NO. What survives is lower evidence burden for selective resolution at comparable—not uniformly better—risk, plus the formal certification-resolution framework. OULAD remains retrospective observational proxy evidence. |
| T032 | Paired bootstrap burden stop gate | Is the observed evidence-burden saving stable under held-out resampling in the primary OULAD configuration? | OULAD cutoff120, all outcomes, epsilon=.20, n=6,505, 5,000 bootstrap resamples | YES. Mean saving 2.366795 channels (39.45%); 95% percentile CI [2.311145, 2.423682]; empirical one-sided p(saving<=0)=0.0002. This supports evidence efficiency, not predictive superiority. Workflow 35074988489. |

## Current significant results

### Deterministic benchmark
Artifact-only evidence leaves four cross-decision pairs unresolved. At lambda=1, wrong-AI-check is cheapest raw burden (0.55) but is not a full separator. Constraint-shift is the cheapest feasible full separator (1.10), versus transfer 1.25 and generic viva 6.00.

### Probabilistic benchmark
Probe eligibility depends on a declared minimum decision-information threshold. The cheapest useful experiment can therefore change as the required resolution becomes stricter. Artifact-only evidence is zero-information in the constructed collapse case.

### Adaptive Monte Carlo benchmark
At seed 20260916, n=20,000 and posterior decision threshold 0.90: adaptive RBE resolves 96.45% with mean burden 2.4455 and 1.8261 probes; fixed targeted resolves 77.355% with burden 2.0769 and 2.3415 probes; one generic viva resolves 46.86% with burden 6.0. Crucially, adaptive RBE has higher resolved-case error (8.61%) than fixed targeted (6.45%). This negative result is retained as a falsification constraint: resolution must be jointly controlled with decision risk.

### Real OULAD benchmark
The first coarse partition benchmark on 32,593 student-module records and 10,655,280 VLE rows produced only tiny passive-refinement gains. The stronger held-out benchmark used student-disjoint train/validation/test splits. The final matched-coverage falsification completed successfully in workflow run 35071457218 and is saved in reports/oulad_selective_falsification_results.csv. Adaptive RBE does not consistently beat fixed-all confidence selection on selective risk and does not clearly dominate random acquisition orders. It does, however, consistently reduce evidence burden relative to collecting all six channels. At cutoff 120, all outcomes, epsilon=.20, RBE risk/coverage/burden = .088047/.527287/3.633205 versus fixed confidence .073178/.527287/6.0. At epsilon=.10, RBE = .022761/.310684/4.581706 versus fixed confidence .023256/.310684/6.0. Thus the defensible real-data result is evidence-efficiency under selective resolution, not predictive superiority. Because OULAD predates GenAI and RBE and contains passive logs rather than designed perturbations, it cannot causally validate RBE.

### Final statistical stop gate
The primary OULAD burden comparison was resampled 5,000 times. Mean evidence saving was 2.366795 channels (39.45%) with 95% percentile CI [2.311145, 2.423682] and corrected one-sided empirical probability 0.0002 for saving <= 0. The burden effect is therefore stable under the declared held-out setup. This closes the planned empirical test sequence for the current manuscript.

## Rule for future work
Whenever a test has scientific significance: (1) commit executable test code, (2) commit the input dataset or deterministic generator or official retrieval procedure, (3) commit/save numerical results, (4) commit/report interpretation and limitations, and (5) append a row here. Human-study results must identify provenance, sample, protocol, uncertainty, and ethics/consent status where applicable.
