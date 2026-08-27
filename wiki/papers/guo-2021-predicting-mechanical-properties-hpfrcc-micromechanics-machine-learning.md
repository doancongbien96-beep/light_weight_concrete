---
title: "Predicting Mechanical Properties of HPFRCC by Micromechanics and ML (Guo et al., 2021)"
type: source_note
source: "sources/materials-14-03143_HPFRCC ML.pdf"
citation: "Guo, P., Meng, W., Xu, M., Li, V. C., & Bao, Y. (2021). Predicting mechanical properties of high-performance fiber-reinforced cementitious composites by combining micromechanics and machine learning. Materials, 14(12), 3143. https://doi.org/10.3390/ma14123143"
date: 2026-08-24
tags:
  - hpfrcc
  - machine-learning
  - micromechanics
  - xgboost
  - svr
  - artificial-neural-network
---

# Predicting Mechanical Properties of HPFRCC by Combining Micromechanics and Machine Learning

## Summary

To accurately predict the compressive strength ($f_c$), direct tensile strength ($\sigma_{tu}$), and ultimate tensile strain capacity ($\epsilon_u$) of high-performance fiber-reinforced cementitious composites (HPFRCC/ECC) by integrating mix design proportions and fiber physical parameters, Professors Y. Bao at Stevens Institute of Technology and Victor C. Li at the University of Michigan compiled a **387-experiment benchmark database** from the international literature (yielding 238 compressive strength, 247 tensile strength, and 266 tensile strain data points after anomaly cleaning) and evaluated artificial neural networks (ANN), support vector regression (SVR), classification and regression trees (CART), and extreme gradient boosting (XGBoost). Among the four algorithms, XGBoost demonstrated superior predictive accuracy, achieving test set determination coefficients of **$R^2 = 0.921$ for compressive strength**, **$R^2 = 0.957$ for tensile strength**, and **$R^2 = 0.896$ for tensile strain capacity** (with training set $R^2$ values of 0.984, 0.993, and 0.989, respectively).

## Key Contributions

- **Compilation of 387-entry multi-dimensional benchmark database**: Encompassed 14 input variables covering binder fractions (cement, fly ash, slag, limestone powder, silica fume) and fiber characteristics (diameter, length, modulus, volume fraction).
- **Data sanitization via anomaly detection**: Filtered out 23 unphysical outliers ($W/B > 0.8$) to ensure database reliability.
- **Comparative evaluation of four ML algorithms**: Ranked generalization predictive performance in the order XGBoost > SVR > ANN > CART.
- **Hyperparameter optimization via grid search**: Determined optimal learning rates (0.1) and number of estimators (100 ~ 1877) for each target property.

## Methods

- Input variable statistics (Table 1):
  - Cement/binder ratio: range 0.152 ~ 1.0 (mean 0.463)
  - Fly ash/binder ratio: range 0 ~ 0.848 (mean 0.362)
  - Slag/binder ratio: range 0 ~ 0.808 (mean 0.120)
  - Sand/binder ratio: range 0 ~ 1.40 (mean 0.410)
  - Water/binder ratio ($W/B$): range 0.11 ~ 0.80 (mean 0.270)
  - Superplasticizer dosage: range 0 ~ 2.7 % (mean 0.78 %)
  - Fiber volume fraction ($V_f$): range 0 ~ 3.0 % (mean 1.9 %)
- Model training (Table 3): 10-fold cross-validation minimizing mean squared error (MSE) loss.

## Results

- Coefficients of determination ($R^2$) across machine learning models for HPFRCC properties (Table 4 & Text):

| ML Model | Compressive $R^2$ Train | Compressive $R^2$ Test | Tensile Strength $R^2$ Train | Tensile Strength $R^2$ Test | Tensile Strain $R^2$ Train | Tensile Strain $R^2$ Test |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **CART** | Poor | Lowest | Poor | Lowest | Poor | Lowest |
| **ANN** | 0.892 | 0.815 | 0.910 | 0.842 | 0.885 | 0.765 |
| **SVR** | 0.945 | 0.882 | 0.962 | 0.915 | 0.930 | 0.824 |
| **XGBoost (Optimal)** | **0.984** | **0.921** | **0.993** | **0.957** | **0.989** | **0.896** |

## Related Notes

- [[guo-2026-egc-intelligent-design]] — Intelligent mix design of EGC via machine learning.
- [[pseudo-strain-hardening-criteria]] — PSH micromechanics theory.
- [[high-strength-strain-hardening-composites]] — High-performance composite design frameworks.
