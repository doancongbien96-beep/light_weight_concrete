---
title: "The use of machine learning in boron-based geopolymers: Function approximation of compressive strength by ANN and GP (Bagheri, Nazari & Sanjayan, 2019)"
type: source_note
source: "sources/bagheri-2019-the-use-of-machine-learning.pdf"
citation: "Bagheri, A., Nazari, A., Sanjayan, J.G. The use of machine learning in boron-based geopolymers: Function approximation of compressive strength by ANN and GP. Measurement 141 (2019) 241-249. doi: 10.1016/j.measurement.2019.03.001"
date: 2026-08-23
tags: [machine-learning, ann, genetic-programming, geopolymer, boroaluminosilicate, compressive-strength-prediction, mix-design]
---

# Machine-learning function approximation of compressive strength in boron-based geopolymers (ANN + GP)

## Summary

A Swinburne University study (Bagheri, Nazari, Sanjayan) predicting the 7-day ambient-cured
compressive strength of boron-activated boroaluminosilicate geopolymer (BASG) from five mix
variables — fly ash fraction (%F), GGBS fraction (%S), and boron/silicon/sodium ion ratios in
the activating liquid (B/AA, Si/AA, Na/AA) — using MLP-ANN and genetic programming (GP)
(Measurement 141, 241-249). A database of 114 points was built from four prior publications
plus 20 new supplementary mixes. The ANN delivers black-box prediction at R²>0.99; GP yields a
closed-form strength function (R²≈0.95) computable by hand. The silicon ion ratio shows the
largest positive direct correlation, while the boron ion ratio carries the highest power in
the function — activator composition governs strength.

## Key Contributions

- **MLP-ANN**: one hidden layer (10/15/20 neurons compared → 20 optimal),
  Levenberg-Marquardt backpropagation, tansig (hidden)/purelin (output). Training R² = 0.99580,
  test R² = 0.99127, overall R² = 0.99456. Maximum error < 0.1 on the normalized scale; test
  MSE = 0.0013249 (RMSE 0.0364).
- **Genetic programming**: GeneXProTools 4, 3 genes + maximum chromosome 30 (per Table 3;
  the conclusion text inconsistently says 40), head size 8, addition linking function,
  expression-tree (ET) based. Training/test/validation R² = 0.9300/0.9515/0.9451, RMSE ≈
  0.07. It presents an explicit strength equation, Eq.(8), with constants c1(Sub-ET1)=0.4 and
  c0=3.06, c1=1.08 for Sub-ET3 — unlike the black-box ANN, extrapolation behavior can be
  inspected and design computed directly.
- **Variable importance**: the silicon ion ratio (Si/AA) has the largest positive direct
  correlation, and the boron ion ratio (B/AA) acts with the highest exponent in the predictive
  function — raising sodium silicate content (Si/AA↑, Na/AA↓) and borax dosing are the key
  levers of BASG strength design.
- **The BASG material family**: Australian fly ash + blast-furnace slag activated by sodium-
  and boron-based alkaline media, a novel AAM class targeting lower carbon footprint, energy,
  and natural resource consumption (database recycled from the group's JCP 2018 / Ceram. Int.
  2017–18 studies).

## Methods

- 114 data points: %F/%S ∈ {0, 9, 30, 50, 70, 91, 100} %, NaOH molarity 3/5/8 M, B/AA 0–0.31,
  Si/AA 0–0.5, Na/AA 0.273–1. Output is 7-day ambient-cured compressive strength, 1–56 MPa
  (mean 20.56 MPa, standard deviation 15.22 MPa).
- All variables linearly normalized to [0,1]. ANN data split 70/15/15
  (training/validation/test), 100 epochs, validation checks 20, performance goal 10⁻⁶.
- GP metrics: R², RMSE, RRSE, MAE, RAE. Residuals classified into three grades (<5 %
  high accuracy, 5–10 % accurate, >10 % low accuracy).

## Results

- ANN: regression R > 0.99 on training, test, and overall; error histogram means ≈ 0
  (training −0.00086, test −0.0107).
- GP: R² varies within 0.02 across datasets — generalization without overfitting. In residual
  3D plots most data fall in the 'accurate to highly accurate' bands.
- Recommendation: extension to other machine-learning techniques (ensembles etc.) for
  building-material property prediction.

## Related Notes

- [[lee-2008-database-mix-optimization-convex-hull]] — GA+ANN+convex-hull ECC mix optimization
  (origin of the ML-design axis)
- [[kim-2007-surface-wave-ai-engine]] — ANN+GA inverse-analysis concrete NDT (user-group ML axis)
- [[guo-2026-egc-intelligent-design]] — CatBoost+SHAP+NSGA-Ⅲ intelligent EGC design (latest
  follow-up on the ML axis)
- [[ganesan-2013-steel-fibre-reinforced-geopolymer-concrete]] — steel-fiber geopolymer concrete
  (geopolymer materials axis)
- [[nematollahi-2017-one-part-shgc-micromechanics]] — one-part SHGC micromechanics (data-driven
  versus mechanism-driven approaches)
- [[negahban-2021-pore-gradation-gpc-opcc]] — GPC versus OPCC pore structure comparison
