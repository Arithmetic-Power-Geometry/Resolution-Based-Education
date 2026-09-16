# RBE Foundation Paper - Synchronized Submission Package

This folder contains the foundation paper synchronized with the companion RBE architecture manuscript.

## Paper 1 - scientific foundation

**Beyond Outcome Attainment: Resolution-Based Education and the Certification-Assessment Resolution Gap in the Generative-AI Era**

Paper 1 owns the formal scientific foundation and falsification evidence:
- CARG and assessment/certification partitions
- Certification Resolution Necessity
- conservative extension / evidence reuse
- one-step discriminating probes versus complete MRRP/adaptive policies
- positive resolved attainment and AR/AU/RN/NA/Deferred semantics
- PAR/RR/RAR/UAR/RNR/MRB and PPO/RPO/UPO compatibility metrics
- deterministic, probabilistic, Monte Carlo and OULAD falsification evidence

## Paper 2 - operating architecture

The companion architecture paper should cite Paper 1 for the above formal foundation and focus its own contribution on curriculum, pedagogy, governance, software/workbook interoperability, audit, accreditation compatibility, institutional implementation, and continuous improvement.

## Data and code

Both papers use the same public repository:
https://github.com/Arithmetic-Power-Geometry/Resolution-Based-Education

## Build

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```
