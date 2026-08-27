---
title: "Intelligent Design of Ultra-High Toughness EGC via Machine Learning (Guo et al., 2026)"
type: source_note
source: "sources/guo-2026-intelligent-design-of-ultra-high-toughness.pdf"
citation: "Guo, P., Zhang, Y., Meng, W., & Bao, Y. (2026). Intelligent design of ultra-high toughness engineered geopolymer composites based on machine learning. Cement and Concrete Composites, 165, 105820."
date: 2026-08-24
tags:
  - engineered-geopolymer-composites
  - egc
  - machine-learning
  - multi-objective-optimization
  - genetic-algorithm
  - carbon-footprint
---

# Intelligent Design of Ultra-High Toughness Engineered Geopolymer Composites (EGC) Based on Machine Learning and Multi-Objective Optimization

## Summary

To simultaneously optimize the compressive strength ($f_c$), ultimate tensile strength ($\sigma_{tu}$), tensile strain capacity ($\epsilon_u$), raw material cost, and embodied carbon emissions of cement-free alkali-activated engineered geopolymer composites (EGC: GGBS + fly ash + silica fume), Professor Y. Bao and co-workers at Stevens Institute of Technology established a 452-dataset EGC experimental database (GGBS 0 ~ 1.0, FA 0 ~ 1.0, SF 0 ~ 0.12, $S/B = 0 \sim 1.6$, $W/B = 0.22 \sim 0.42$, alkali molarity 0.86 ~ 1.26 mol) and developed an intelligent EGC mix design platform coupling hyperparameter-tuned ANN models (learning rate 0.010, 4 hidden layers) with the NSGA-II multi-objective genetic algorithm. The resulting optimal low-carbon ultra-high-toughness EGC achieved a 28 d compressive strength of **52.5 MPa**, direct tensile strength of **6.85 MPa**, and tensile strain capacity of **6.45 %**, while reducing embodied carbon emissions by **68 %** compared to conventional cementitious ECC.

## Key Contributions

- **Compilation of 452-dataset multi-dimensional EGC database**: Covered 12 parameters including precursors (GGBS, FA, SF), activators (AAM molarity), sand ratio, and fiber characteristics.
- **High predictive performance via ANN hyperparameter optimization**: Achieved post-tuning determination coefficients of $R^2 = 0.82$ for compressive strength, $R^2 = 0.83$ for tensile strength, and $R^2 = 0.88$ for tensile strain capacity.
- **Pareto front discovery via NSGA-II algorithm**: Automatically identified trade-offs among the four conflicting objectives of strength, ductility, cost, and carbon emissions.
- **Experimental validation**: Measured mechanical properties of the recommended optimal mix agreed with model predictions within 5 % error.

## Methods

- Database parameters (Table 1):
  - GGBS: 0 ~ 1.0 (mean 0.43), FA: 0 ~ 1.0 (mean 0.54), SF: 0 ~ 0.12 (mean 0.01)
  - $S/B$: 0 ~ 1.60 (mean 0.38), $W/B$: 0.22 ~ 0.42 (mean 0.31), AAM molarity: 0.86 ~ 1.26 mol
- Model optimization (Table 2):
  - ANN: Learning rate 0.001 $\rightarrow$ 0.010, 4 hidden layers, $\sigma_c\ R^2 = 0.82$, $\sigma_{tu}\ R^2 = 0.83$, $\epsilon_{tu}\ R^2 = 0.88$.
- Optimization algorithm: NSGA-II genetic algorithm (population size 100, 200 generations).

## Results

- Predictive performance across ANN models before and after hyperparameter tuning (Table 2 & Results):

| Target Property | Pre-tuning $R^2$ | Post-tuning $R^2$ | Optimal Learning Rate | Hidden Layers | Experimental Validation of Optimal Mix |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Compressive strength ($\sigma_c$)** | 0.82 | **0.82** | 0.010 | 4 layers | 52.5 MPa (predicted 54.0 MPa, error 2.8 %) |
| **Ultimate tensile strength ($\sigma_{tu}$)** | 0.74 | **0.83 (+12.2 %)** | 0.010 | 4 layers | 6.85 MPa (predicted 7.10 MPa, error 3.5 %) |
| **Ultimate tensile strain ($\epsilon_{tu}$)** | 0.72 | **0.88 (+22.2 %)** | 0.010 | 4 layers | **6.45 % (ultra-ductile, error 4.6 %)** |

## Related Notes

- [[guo-2021-predicting-mechanical-properties-hpfrcc-micromechanics-machine-learning]] — HPFRCC machine learning modeling.
- [[one-part-shgc]] — One-part high-ductility geopolymer design.
- [[sustainability-low-carbon-binders]] — Low-carbon sustainable binders.
