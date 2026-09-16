# RBE Final LaTeX Submission Package

Main manuscript: `main.tex`  
Bibliography: `references.bib` (biblatex APA, Biber backend)

Compile with:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
biber main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The manuscript source is self-contained: all figures are generated in LaTeX/TikZ/PGFPlots and all tables/algorithms are embedded in `main.tex`. No external figure files are required.

The final empirical stop gate is recorded in `reports/OULAD_BURDEN_BOOTSTRAP_RESULT.md` and `reports/oulad_burden_bootstrap_results.csv`. The paper deliberately retains negative controls and does not claim predictive superiority over strong fixed-evidence baselines.
