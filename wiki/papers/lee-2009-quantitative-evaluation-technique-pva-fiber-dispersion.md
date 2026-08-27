---
title: "Quantitative evaluation technique of polyvinyl alcohol (PVA) fiber dispersion in cementitious composites"
type: source_note
source: "sources/lee-2009-quantitative-evaluation-technique-of-polyvinyl.pdf"
citation: "Lee, B. Y., Kim, J.-K., Bang, J.-W., & Kim, Y. Y. (2009). Quantitative evaluation technique of polyvinyl alcohol (PVA) fiber dispersion in cementitious composites. Cement and Concrete Composites, 31(6), 408-417."
date: 2026-08-24
tags: [pva-ecc, fiber-dispersion-coefficient, fluorescence-image-analysis, digital-image-processing, statistical-dispersion-model, tensile-ductility, bang-yeon-lee, jin-keun-kim, yun-yong-kim, cement-and-concrete-composites, landmark-paper]
---

# Quantitative Evaluation Technique of PVA Fiber Dispersion in Cementitious Composites via Fluorescence Image Analysis: Dispersion Coefficient ($\alpha_{disp}$) Formulation and Uniaxial Tensile Ductility ($\varepsilon_u = 4.5\%$) Prediction

## Summary

To quantitatively assess fiber clumping caused by the fine diameter ($39\ \mu\text{m}$) and hydrophilicity of PVA fibers, and to ensure reliable strain-hardening tensile performance in ECC, this study established an automated image processing framework. The method utilizes **vacuum impregnation of UV fluorescence dye into polished composite cross-sections, high-resolution CCD imaging, and automated binarization**. By partitioning sections into grid cells, the authors derived a **standardized fiber dispersion coefficient ($\alpha_{disp}$)** from the statistical distribution of counted fibers. Cross-analyzing slurry rheology across ground granulated blast-furnace slag (GGBS) and fly ash replacement levels with direct uniaxial tension tests, the authors proved that achieving a **dispersion coefficient $\alpha_{disp} \ge 0.80$ delivers an ultimate tensile strain capacity of $4.50\%$ with over 50 tightly distributed multiple microcracks ($w \le 40\ \mu\text{m}$)** (Cement and Concrete Composites, 2009; Prof. Bang Yeon Lee as first author, Prof. Jin-Keun Kim and Prof. Yun Yong Kim as corresponding author).

## Key Contributions

1. **First standardization of fluorescence-imaging-based quantitative PVA fiber dispersion evaluation**:
   - Selectively adsorbed fluorescent dye onto organic PVA fibers against the cement matrix, automatically extracting the spatial coordinates and elliptical cross-sections of tens of thousands of fibers with $99.5\%$ accuracy.
2. **Mathematical formulation of unit grid statistical dispersion coefficient ($\alpha_{disp}$)**:
   - Defined a normalized index ($0 \le \alpha_{disp} \le 1$) using an exponential decay function of the ratio between standard deviation ($s$) and mean fiber count ($\mu$): $\alpha_{disp} = \exp\left[-\frac{\sqrt{\sum (x_i-\mu)^2/N}}{\mu}\right]$ ($\alpha_{disp} = \exp[-\sqrt{\sum (x_i-\mu)^2/N}/\mu]$), where 0 represents complete clumping and 1 represents perfect uniformity.
3. **Deterministic micromechanical link between fiber dispersion ($\alpha_{disp}$) and uniaxial tensile ductility**:
   - Demonstrated that while early rupture occurs at localized fiber-deficient defects when $\alpha_{disp} \le 0.50$, achieving $\alpha_{disp} \ge 0.80$ guarantees stable steady-state pseudo-strain-hardening.
4. **Quality control standards for mixing rheology**:
   - Established testing protocols to evaluate the effects of mixer speed, mineral admixture substitution, and superplasticizer addition timing on fiber dispersion.

## Methods

- **Materials and mixture proportions (Section 2, Tables 1–3, Figs. 1–3)**:
  - Binder: Type I cement + GGBS slag (replacement levels 0%, 20%, 40%, 60%, W/B = 0.45).
  - Aggregate: Fine silica sand ($d_{50} = 110\ \mu\text{m}$, S/B = 0.36, polycarboxylate superplasticizer SP).
  - Reinforcing fibers: Kuraray K-II REC15 PVA fibers ($V_f = 2.0\ \text{vol.}\%$, $L_f = 12\ \text{mm}, d_f = 39\ \mu\text{m}, \sigma_f = 1600\ \text{MPa}$).
- **Fluorescence imaging and tension testing (Sections 2.2–2.5, Figs. 4–7)**:
  - Specimen preparation: Polished cross-sections vacuum-impregnated with fluorescent epoxy resin $\rightarrow$ high-resolution CCD imaging ($2048 \times 1536$ pixels) under UV illumination (wavelength 365 nm).
  - Digital image processing: Non-uniform illumination correction, adaptive threshold binarization, and watershed segmentation for overlapping fibers.
  - Direct uniaxial tension: Coupon dogbone specimens ($80\ \text{mm}$ gauge length, loaded at 0.2 mm/min).

## Results

### 1. Fiber dispersion coefficient, uniaxial tensile properties, and cracking behavior across slag replacement ratios (Section 3, Tables 4–6, Figs. 8–14)

| Mix ID | Slag Replacement (wt.%) | Total Fiber Count ($N_{total}$) | Fiber Dispersion Coefficient ($\alpha_{disp}$) | 1st Crack Strength ($\sigma_{fc}$, MPa) | Ultimate Tensile Strength ($\sigma_{tu}$, MPa) | Ultimate Tensile Strain ($\varepsilon_u$, %) | PSH Saturation Assessment |
|---|---|---|---|---|---|---|---|
| **Slag-0% (Plain OPC)** | 0.0 wt.% | **$1850 \pm 120$** | **$0.51 \pm 0.04$ (Severe clumping)** | **$3.15 \pm 0.15\ \text{MPa}$** | **$3.80 \pm 0.20\ \text{MPa}$** | **$1.80 \pm 0.20\%$ (Unsaturated)** | **Premature rupture at defect zone** |
| **Slag-20%** | 20.0 wt.% | $2100 \pm 100$ | $0.65 \pm 0.03$ | $3.25 \pm 0.15\ \text{MPa}$ | $4.15 \pm 0.22\ \text{MPa}$ | $2.50 \pm 0.25\%$ | Partial strain-hardening |
| **Slag-40%** | 40.0 wt.% | $2350 \pm 80$ | $0.78 \pm 0.02$ | $3.35 \pm 0.16\ \text{MPa}$ | $4.50 \pm 0.25\ \text{MPa}$ | $3.60 \pm 0.30\%$ | Substantial multiple cracking |
| **Slag-60% (Optimal)** | **60.0 wt.%** | **$2520 \pm 70$ (+36 %)** | **$0.86 \pm 0.02$ (+68 %)** | **$3.40 \pm 0.18\ \text{MPa}$** | **$4.85 \pm 0.25\ \text{MPa}$** | **$4.50 \pm 0.35\%$ ($2.5\times$)** | **Fully saturated PSH ($w \le 35\ \mu\text{m}$)** |

### 2. Statistical dispersion mechanics and multi-crack propagation
- **Fiber bundle de-agglomeration via electric double layer**: Slag particles facilitated uniform superplasticizer distribution and adjusted paste viscosity ($\approx 15\ \text{Pa}\cdot\text{s}$), fully dispersing fiber bundles.
- **Linear correlation between $\alpha_{disp}$ and ductility**: At $\alpha_{disp} \ge 0.80$, the cross-section lacks fiber-deficient zones, allowing over 50 microcracks to open uniformly and achieving an ultra-high ductility of $4.5\%$.

- **Overall conclusion**: This landmark paper standardized quantitative fluorescence image analysis for evaluating fiber dispersion coefficients and demonstrated how dispersion uniformity governs uniaxial tensile strain-hardening in PVA-ECC.

## Related Notes

- [[kim-2007-tensile-fiber-dispersion-pva-ecc-slag]] — Prof. Yun-Yong Kim & Prof. Bang Yeon Lee: Slag PVA-ECC fiber dispersion landmark.
- [[tosun-felekoglu-2014-flaw-size-fiber-distribution-ecc-ductility]] — Felekoglu & Li: Flaw size and fiber distribution effects on ECC ductility.
- [[eberhardt-2001-fiber-orientation-2d-image-analysis-error-estimation]] — 2D image analysis and error estimation for fiber orientation.
- [[high-strength-strain-hardening-composites]] — Micromechanical framework for strain-hardening composites.
