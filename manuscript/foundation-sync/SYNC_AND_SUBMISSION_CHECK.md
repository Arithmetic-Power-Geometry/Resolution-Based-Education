# Synchronization and Submission Audit

## Synchronized with the companion architecture paper

The foundation paper now uses the same core semantics as the architecture paper:

- RCO = (C, E, P, D)
- assessment partition vs certification partition
- CARG
- Certification Resolution Necessity
- conservative extension / evidence reuse
- deterministic and probabilistic resolution
- one-step discriminating probe separated from a complete MRRP/adaptive policy
- finite burden and defer state
- AR / AU / RN / NA / Deferred
- positive resolution Q+
- RCA
- PAR / RR / RAR / UAR / RNR / MRB
- PPO / RPO / UPO
- separate performance mark and Resolution Gate
- no claim of broad predictive superiority

## Paper 1 / Paper 2 division

Paper 1 is the scientific foundation and empirical falsification paper.
Paper 2 is the complete operating architecture, software/workbook validation, governance, audit, accreditation, and implementation paper.
Paper 2 should cite Paper 1 for the formal foundation rather than claim the same formalism as an independent novelty contribution.

## Cross-reference audit

Foundation paper contains four numbered tables:
- Table 1 deterministic resolving benchmark - cited in text
- Table 2 Monte Carlo mechanism test - cited in text
- Table 3 held-out OULAD comparison - cited in text
- Table 4 matched-coverage falsification - cited in text

No numbered figures are used in the synchronized foundation paper, so no figure cross-reference is missing.

## Reference cleanup

Key contemporary references were checked against publisher/DOI records, including:
- Ali & Maroulis (2026), DOI 10.1080/02602938.2026.2683046
- Bannister, Santamaria Urbieta & Brufau Alvira (2025), DOI 10.37074/jalt.2025.8.1.20
- Bearman et al. (2024), DOI 10.1080/02602938.2024.2335321
- Fok & Weld (2024), DOI 10.1002/aaai.12182
- Khlaif et al. (2025), DOI 10.3390/educsci15020174
- Kuzilek et al. (2017), DOI 10.1038/sdata.2017.171
- Luo (2024), DOI 10.1080/02602938.2024.2309963
- Mislevy, Almond & Lukas (2003), DOI 10.1002/j.2333-8504.2003.tb01908.x
- Xia et al. (2024), DOI 10.1186/s41239-024-00468-z

## Generic author/submission requirements

The package includes:
- author name and affiliation
- abstract and keywords
- Data and Code Availability
- Reproducibility Statement
- Funding statement
- Competing interests statement
- Ethics statement
- Author contributions statement

Still journal-specific and therefore intentionally not hard-coded:
- corresponding-author email/ORCID
- journal-specific AI-use disclosure wording
- exact article template/style
- line numbering if required
- word-count limits
- graphical abstract/highlights if required
- title page separation/blinding if double-anonymous review is required

These should be applied only after a target journal is selected.

## Build/QA

- Compiled successfully with LaTeX + biber.
- 9-page PDF.
- No unresolved references or overfull-box warnings in final build.
- PDF visually rendered and checked.
