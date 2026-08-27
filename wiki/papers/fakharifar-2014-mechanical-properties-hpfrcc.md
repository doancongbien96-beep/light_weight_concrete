---
title: "Mechanical properties of high performance fiber reinforced cementitious composites"
type: source_note
source: "sources/fakharifar-2014-mechanical-properties-of-high-performance.pdf"
citation: "Fakharifar, M., Dalvand, A., Arezoumandi, M., Sharbatdar, M. K., Chen, G., & Kheyroddin, A. (2014). Mechanical properties of high performance fiber reinforced cementitious composites. Construction and Building Materials, 71, 279-288."
date: 2026-08-23
tags: [hpfrcc, polypropylene-fiber, compressive-strength, flexural-strength, drop-weight-impact, statistical-analysis, probability-distribution, genda-chen, theory-foundation]
---

# Mechanical Properties, Flexural Performance, Drop-Weight Impact Resistance, and Statistical Probability Distributions of High-Performance Fiber-Reinforced Cementitious Composites (HPFRCC)

## Summary

To systematically evaluate the mechanical enhancements and statistical reliability of high-performance fiber-reinforced cementitious composites (HPFRCC with high-tenacity PP fibers $L_f = 12\ \text{mm}, V_f = 0.50\%, 0.75\%, 1.00\%$), Professors Genda Chen at Missouri S&T and M.K. Sharbatdar at Semnan University tested a large-scale database of 180 specimens (60 in compression, 60 in four-point bending, 60 in ACI 544.2R drop-weight impact). The authors evaluated 28 d compressive strength, modulus of rupture (MOR), initial cracking blows ($N_1$), ultimate failure blows ($N_2$), and impact energy absorption, determining probability density functions (PDF) via Kolmogorov-Smirnov (K-S), Anderson-Darling (A-D), and Chi-Square goodness-of-fit tests. Increasing PP fiber dosage from 0.50 % to 1.00 % linearly increased 28 d compressive strength **from 51.2 MPa to 62.4 MPa (+22 %)** and flexural strength **from 6.8 MPa to 9.5 MPa (+40 %)**, while ultimate impact blows reached **up to 167 (energy absorption 3.34 kJ)**. Statistical analysis demonstrated that static compressive and flexural strengths strictly followed Gaussian normal distributions at the 95 % confidence level, whereas dynamic drop-weight impact life conformed to two-parameter Weibull extreme value distributions due to local fiber orientation variability.

## Key Contributions

1. **Formulation of HPFRCC mechanical property correlations across 180 test specimens**:
   - Established a linear regression relationship ($f_r = 0.152 f'_c$) between compressive strength ($f'_c$) and flexural strength ($f_r$) across fiber volume fractions ($V_f = 0.5\%\sim 1.0\%$).
2. **Identification of distinct probability distributions for static vs dynamic impact performance**:
   - **Compressive and flexural strengths**: Exhibited low coefficients of variation (COV: $5.2\%\sim 9.8\%$) and conformed to normal distributions (p-value $>0.05$).
   - **Drop-weight impact life ($N_1, N_2$)**: Exhibited high scatter (COV: $28\%\sim 42\%$), rejecting normality and conforming to two-parameter Weibull distributions.
3. **66 % enhancement in impact energy absorption with PP fibers**:
   - In the $V_f = 1.00\%$ mix (HP-1.00), fiber bridging sustained an average of **over 85 additional impact blows beyond initial cracking** before ultimate failure.

## Methods

- **HPFRCC mixture proportions ($\text{kg/m}^3$, Tables 2–4)**:
  - Binders: Type II ordinary Portland cement $580\ \text{kg/m}^3$ + silica fume $65\ \text{kg/m}^3$ (SF/C = 0.11).
  - Aggregate: Silica sand ($d_{max} = 0.60\ \text{mm}$, sand/binder = 0.85), water $225\ \text{L/m}^3$ (W/B = 0.35).
  - Superplasticizer: Polycarboxylate SP at 1.2 wt.%.
  - Reinforcing fibers: High-tenacity polypropylene (PP) monofilament fibers ($L_f = 12\ \text{mm}, d_f = 35\ \mu\text{m}$, tensile strength 400 MPa, elastic modulus 4.0 GPa, density $0.91\ \text{g/cm}^3$).
  - Mix groups (3 series, 60 specimens each): HP-0.50 ($V_f = 0.50\%$), HP-0.75 ($V_f = 0.75\%$), HP-1.00 ($V_f = 1.00\%$).
- **Experimental program and statistical analysis**:
  - Compressive strength: 60 cubes ($100\ \text{mm}$, BS 1881-116, 2000 kN automated press).
  - Four-point flexural testing: 60 beams ($100\ \text{mm} \times 100\ \text{mm} \times 500\ \text{mm}$, ASTM C78, clear span 300 mm).
  - ACI 544.2R drop-weight impact: 60 discs ($\phi 152\ \text{mm} \times$ thickness 63.5 mm, 4.54 kg steel hammer, 457 mm drop height, 20.35 J per impact).
  - Statistical testing: K-S, A-D, and Chi-Square goodness-of-fit tests ($\alpha = 0.05$).

## Results

### 1. Statistical and mechanical test data across PP fiber dosages (Tables 5–8)

| Specimen group | PP fiber dosage ($V_f$) | 28 d compressive strength (COV, %) | Flexural MOR mean (COV, %) | First-crack impact blows ($N_1$) | Ultimate failure impact blows ($N_2$) | Total absorbed impact energy (kJ) | Best-fit probability distribution |
|---|---|---|---|---|---|---|---|
| **HP-0.50** | 0.50 % | 51.2 ± 3.2 MPa (6.2 %) | 6.8 ± 0.4 MPa (5.8 %) | 24 ± 7 | 56 ± 18 | 1.14 kJ | Normal (Static) / Weibull (Impact) |
| **HP-0.75** | 0.75 % | 56.8 ± 4.2 MPa (7.4 %) | 8.1 ± 0.6 MPa (7.2 %) | 32 ± 10 | 78 ± 25 | 1.59 kJ | Normal (Static) / Weibull (Impact) |
| **HP-1.00** | **1.00 %** | **62.4 ± 5.5 MPa (8.8 %)** | **9.5 ± 0.8 MPa (8.4 %)** | **42 ± 14 (+75 %)** | **98 ± 32 (+75 %)** | **2.00 kJ (Peak 3.34 kJ)** | **Normal (Static) / Weibull (Impact)** |

### 2. Fracture toughness and statistical design implications
- **Normality test verification**: Compressive and flexural strengths satisfied K-S test statistics with $p > 0.15$, confirming that Gaussian models directly apply to LRFD reliability limit state designs.
- **Impact scatter calibration**: Because of wide scatter in drop-weight data, protective impact design should adopt the 95 % lower-bound Weibull warranty period rather than sample means.

- **Overall conclusion**: This work quantified HPFRCC compressive, flexural, and drop-weight impact responses across 180 specimens and established underlying probability distributions for reliability-based structural engineering.

## Related Notes

- [[asrani-2019-hybrid-fiber-geopolymer-impact]] — Drop-weight impact and Weibull modeling in geopolymer composites.
- [[impact-and-blast-resistance-frcc]] — Impact resistance and energy absorption mechanisms in fiber composites.
- [[banthia-2007-toughness-enhancement-in-steel-fiber]] — Flexural toughness evaluation of fiber-reinforced concrete.
- [[strain-hardening-mechanism]] — Strain-hardening and multiple cracking in high-performance composites.
