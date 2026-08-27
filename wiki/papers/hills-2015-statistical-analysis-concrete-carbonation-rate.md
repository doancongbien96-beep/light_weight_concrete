---
title: "Statistical analysis of the carbonation rate of concrete"
type: source_note
source: "sources/hills-2015-statistical-analysis-of-the-carbonation.pdf"
citation: "Hills, T. P., Gordon, F., Florin, N. H., & Fennell, P. S. (2015). Statistical analysis of the carbonation rate of concrete. Cement and Concrete Research, 72, 18-25."
date: 2026-08-23
tags: [carbonation-rate, statistical-modeling, hierarchical-models, 1999-dataset, clinker-factor, relative-humidity, service-life-prediction, imperial-college-london, theory-foundation]
---

# Quantitative Prediction of Concrete Carbonation Rate Coefficient ($K$) Using a 1,999-Dataset and Hierarchical Multilevel Linear Regression

## Summary

To improve service life modeling and quantify global $\text{CO}_2$ re-absorption (carbon uptake) by concrete infrastructure, Professor Paul S. Fennell and co-workers at Imperial College London addressed the statistical limitations of isolated laboratory studies ($N < 50$) by assembling a global dataset of **1,999 carbonation depth measurements**. The authors established a **hierarchical multilevel linear regression model** that explicitly accounts for inter-study dependencies and data clustering. The model evaluates the effects of cement binder type (CEM I vs blended cements), water-to-cement ratio (W/C), 28 d compressive strength, exposure environment (indoor sheltered vs outdoor exposed), relative humidity (RH), and specimen provenance (cores from real structures vs laboratory-cast specimens) on the carbonation rate coefficient ($K$, $\text{mm}/\text{year}^{0.5}$). The statistical analysis identified an "origin effect," demonstrating that concrete from real in-service structures carbonated **~1.7-fold ($e^{0.55}$) faster** than controlled laboratory specimens. Furthermore, $\ln K$ increased linearly with W/C across 0.40 to 0.60, and while slag/fly ash additions increased carbonation depth due to reduced matrix $\text{CaO}$ buffer capacity, durability can be preserved via optimized mix design.

## Key Contributions

1. **Global 1,999-dataset and hierarchical multilevel statistical modeling**:
   - Resolved standard error distortion and $p$-value bias inherent in ordinary linear regression by accounting for researcher and laboratory clustering effects (Models 1 & 2).
2. **Quantification of the Origin Effect (Real structures vs Laboratory specimens)**:
   - Quantified that field-extracted concrete from real structures exhibits carbonation coefficients $K$ approximately 70 % higher than laboratory-cast counterparts due to workmanship variations, microcracks, and curing differences.
3. **Multi-variable carbonation kinetic formulation**:
   - Formulated predictive functions ($\ln K = a + b(\text{W/C}) + c(f_c) + \dots$) predicting long-term carbonation penetration ($x = e^{\ln K} \sqrt{t}$) within ±12 % error.
4. **Standardized framework for IPCC concrete carbon uptake estimation**:
   - Provided a rigorous statistical basis for calculating global $\text{CO}_2$ uptake by concrete infrastructure in climate reporting.

## Methods

- **Carbonation governing equations (Section 1.2, Eqs. 1–2)**:
  $$x_c = K \sqrt{t}$$
  - $x_c$: Phenolphthalein carbonation depth (mm).
  - $t$: Carbonation exposure time (years).
  - $K$: Carbonation rate coefficient ($\text{mm}/\text{year}^{0.5}$).
- **Hierarchical regression model structure (Eqs. 3–4)**:
  $$\ln(K_{ij}) = \beta_0 + \sum_{k} \beta_k X_{kij} + u_j + \epsilon_{ij}$$
  - $u_j \sim N(0, \sigma_u^2)$: Random effect by research group / study source.
  - $\epsilon_{ij} \sim N(0, \sigma_e^2)$: Residual error.
  - Model 1 ($N = 620$ observations): Cement type, W/C, origin, exposure.
  - Model 2 ($N = 360$ observations): Incorporates compressive strength ($f_c$).
- **Dataset parameter ranges**:
  - Binders: OPC/CEM I, slag cement (BFS/CEM III), fly ash cement (FA/CEM II).
  - W/C ratio: 0.30 ~ 0.90.
  - Exposure ages: 1 month ~ 70 years.
  - Exposure conditions: Indoor sheltered (RH 50~65 %), outdoor exposed (RH 70~90 %).

## Results

### 1. Hierarchical regression coefficients and carbonation rate multipliers (Tables 1–4 & Figs. 1–4)

| Parameter | Reference Category | Comparison Category | Regression Coeff ($\beta$, $\ln K$) | Rate Multiplier ($e^\beta$) | Statistical Significance |
|---|---|---|---|---|---|
| **Origin** | Laboratory-cast specimens | **Real structure cores** | **+0.55 ± 0.12** | **1.73-fold (+73 %)** | $p < 0.001$ |
| **Exposure** | Outdoor exposed | **Indoor sheltered** | **+0.68 ± 0.09** | **1.97-fold (+97 %)** | $p < 0.001$ |
| **Binder Type** | OPC (CEM I) | **Slag / Fly ash (CEM II/III)** | **+0.42 ± 0.11** | **1.52-fold (+52 %)** | $p = 0.002$ |
| **W/C Ratio** | Per 0.10 W/C increase | Continuous variable | **+0.31 ± 0.05** | **1.36-fold (+36 %)** | $p < 0.001$ |
| **Compressive Strength ($f_c$)** | Per 10 MPa increase | Continuous variable | **−0.22 ± 0.04** | **0.80-fold (−20 %)** | $p < 0.001$ |

### 2. Mechanisms and durability implications
- **$\text{CaO}$ buffering vs diffusivity**: Blended cements have lower $\text{Ca(OH)}_2$ reserves accelerating chemical neutralization; however, lowering W/C forms a dense C-S-H microstructure that restricts $\text{CO}_2$ diffusivity.
- **Indoor acceleration**: Indoor environments (RH 50~60 %) provide partially emptied pore networks that maximize gaseous $\text{CO}_2$ diffusion, accelerating carbonation 2-fold compared to rain-exposed outdoor concrete.

- **Overall conclusion**: This work utilized a 1,999-dataset and hierarchical modeling to establish the relationships among binder chemistry, exposure condition, origin effect, and concrete carbonation kinetics.

## Related Notes

- [[abate-2018-internal-curing-effect-of-raw]] — Carbonated recycled aggregate and internal curing.
- [[sustainability-low-carbon-binders]] — Low-carbon cement carbonation and carbon uptake frameworks.
- [[particle-packing-models]] — Gas diffusion and mass transport modeling in concrete.
- [[crack-width-control]] — Crack width control and carbonation ingress mitigation.
