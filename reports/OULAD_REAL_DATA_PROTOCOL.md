# Real Big-Dataset Validation Protocol: OULAD

## Dataset
Open University Learning Analytics Dataset (OULAD), an anonymised public educational dataset containing more than 30,000 student-module records, assessment submissions and a VLE interaction table with more than 10 million interaction rows.

Official source: Open University Learning Analytics Dataset (OU Analyse).
Citation: Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics Dataset OULAD. Scientific Data, 4, 170171.

The repository does not redistribute the dataset. `benchmarks/oulad_resolution_benchmark.py` downloads it from the official source at runtime and saves only aggregate benchmark results.

## RBE question
Given an assessment-score evidence language that leaves groups of students with opposite eventual certification outcomes observationally compatible, which additional already-recorded evidence channel most cheaply reduces those decision-incompatible cells?

Candidate evidence channels are assessment count, VLE clicks, active VLE days and submission timing. For this observational benchmark each logged channel receives equal declared acquisition cost 1, so the cheapest useful experiment is the channel with greatest reduction in unresolved mass per declared unit cost.

## Why this is only a proxy experiment
OULAD was not collected under RBE, contains no designed MRRP perturbations and predates contemporary generative-AI use. Therefore these variables are observational evidence channels, not randomized interventions. Final result is used only as the retrospective certification label. No causal claim is permitted.

## Falsification conditions
The real-data benchmark weakens the current empirical case if: (1) baseline assessment evidence has essentially no decision-incompatible cells; (2) additional evidence does not reduce unresolved mass; (3) gains disappear under reasonable binning/split sensitivity; or (4) a claimed advantage is driven only by outcome leakage.

## Required follow-up
Run sensitivity across quantile counts, modules/presentations, early evidence cutoffs, and held-out presentations. Then build a prospective RBE dataset where perturbations are deliberately administered and learner responses are recorded. That prospective study is required for causal educational claims.
