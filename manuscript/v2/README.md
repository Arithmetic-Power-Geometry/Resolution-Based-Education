# RBE Paper V2 - Framework-Synchronized Scientific Manuscript

Title: **Beyond Outcome Attainment: Resolution-Based Education and the Certification-Assessment Resolution Gap in the Generative-AI Era**

This is the first scientific RBE paper synchronized with the frozen framework. It intentionally does **not** attempt to reproduce the complete institutional RBE operating architecture. A separate framework paper is reserved for governance, accreditation, progression, faculty systems, data governance, policy templates and institution-wide implementation.

## Build

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
biber main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Scientific additions relative to Paper V1

- Resolvable Capability Outcome: `RCO=(C,E,P,D)`.
- Conservative Extension / Evidence Reuse (`B_additional=0` when existing evidence is resolution-adequate).
- Explicit distinction between one-step resolving probes and adaptive resolution-restoring policies/trees.
- Positive resolved decision required for Resolved Capability Attainment.
- Explicit AR/AU/RN/NA/Deferred terminal states.
- Course metrics `PAR`, `RR`, `RAR`, `UAR`, `MRB` with exact state semantics.
- Programme bridge metrics `PPO`, `RPO`, `UPO` with an explicit caution against treating weighted mappings as direct validation of complex programme competence.
- Worked Theory of Computation interpretation showing identical marks can carry different certification-resolution states without changing the original grade or implying misconduct.
- Existing Monte Carlo and OULAD negative controls retained; no predictive-superiority claim.

## Repository tests relevant to V2

- `tests/test_attainment.py`
- `tests/test_policy.py`

The first verifies that low decision risk is not sufficient for positive capability attainment; the resolved decision must be positive. The second verifies a case in which an adaptive policy resolves a decision even though no single probe is a complete one-step resolver.
