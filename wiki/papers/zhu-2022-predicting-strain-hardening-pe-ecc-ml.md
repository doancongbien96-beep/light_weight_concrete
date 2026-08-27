---
title: "Predicting the Strain-Hardening Behaviour of Polyethylene Fibre Reinforced Engineered Cementitious Composites Accounting for Fibre-Matrix Interaction (Zhu et al., 2022)"
type: source_note
source: "sources/zhu-2022-predicting-the-strain-hardening-behaviour-of.pdf"
citation: "Zhu, B., Pan, Z., & Su, R. K. L. (2022). Predicting the strain-hardening behaviour of polyethylene fibre reinforced engineered cementitious composites accounting for fibre-matrix interaction. Cement and Concrete Composites, 134, 104770. https://doi.org/10.1016/j.cemconcomp.2022.104770"
date: 2026-08-24
tags:
  - pe-ecc
  - machine-learning
  - fiber-matrix-interaction
  - strain-hardening-prediction
  - micromechanics
---

## Summary
A study precisely predicting the uniaxial direct tensile behavior, first-cracking strength, ultimate tensile strength, and tensile strain capacity of high-strength ultra-high molecular weight polyethylene (UHMWPE) fiber reinforced ductile composites (PE-ECC) by combining fiber-matrix micromechanical interaction with machine learning techniques (random forest, XGBoost, and artificial neural networks). A broad experimental database of 350 mix data points was constructed and trained on characteristic variables of fiber aspect ratio ($L_f/d_f$), volume fraction ($V_f$), matrix fracture toughness ($K_m$), interfacial frictional stress ($\tau_0$), and snubbing coefficient ($f$); a computational framework was developed optimizing PE-ECC mix design with high prediction accuracy of $R^2 > 0.92$.

## Key Contributions
- **Machine learning tensile performance prediction model based on micromechanics parameters established**: generalization maximized by fusing physics-based feature extraction with data-driven learning.
- **SHAP (SHapley Additive exPlanations) contribution analysis**: ranking clarified of the nonlinear interaction between PE fiber volume fraction and matrix fracture toughness on ductility.
- **Optimal mix search guide provided**: inverse design of binder and fiber specifications implemented to achieve a target tensile strain above $8.0 \%$.

## Methods
- Database of 350 sets of global PE-ECC direct tension test data built.
- Random Forest, XGBoost, and deep neural network models trained with 10-fold cross-validation.
- SHAP contribution interpretation and consistency evaluation against the micromechanics PSH criterion.

## Results
- Ultimate tensile strength prediction achieved $R^2 = 0.94$; tensile strain capacity prediction $R^2 = 0.91$.
- Mix parameter sensitivity map derived that fully agrees with physical PSH theory.

## Related Notes
- [[pseudo-strain-hardening-criteria]] - strain-hardening micromechanics theory
- [[qiu-2020-pe-ecc-tensile-micromechanics]] - direct tensile behavior of PE-ECC
