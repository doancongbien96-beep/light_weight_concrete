---
title: "Optimum Concrete Mixture Proportion Based on a Database Considering Regional Characteristics (Lee, Kim & Kim, 2009)"
type: source_note
source: "sources/IJP0309S_Optimum Concrete Mixture.pdf"
citation: "Lee, B. Y., Kim, J. H., & Kim, J. K. (2009). Optimum concrete mixture proportion based on a database considering regional characteristics. Journal of Computing in Civil Engineering, 23(5), 258-265. https://doi.org/10.1061/(ASCE)0887-3801(2009)23:5(258)"
date: 2026-08-24
tags:
  - concrete-mix-design
  - optimization
  - database-driven
  - neural-networks
  - regional-characteristics
---

# Optimum Concrete Mixture Proportioning Based on a Database Considering Regional Characteristics

## Summary

This study proposes an advanced computational concrete mixture proportioning algorithm that incorporates regional variations in raw materials (cement reactivity, aggregate shape, grading, and mineralogy) into statistical databases. To prevent unrealistic predictions (extrapolation errors) outside the local database domain, the system integrates Convex Hull feasible boundary evaluation with Artificial Neural Networks (ANN). A Multi-Objective Genetic Algorithm (MOGA) is applied to simultaneously optimize strength, slump, cost, and durability, substantially improving prediction reliability and practical field applicability.

## Key Contributions

- **Prevention of overfitting and extrapolation via database boundary constraints**: Restricts candidate search strictly within the verified domain of regional ready-mix concrete production, eliminating irrational mixture outputs.
- **Multi-objective optimization framework**: Formulates comprehensive objective functions balancing target 28 d compressive strength ($f_{ck}$), slump (workability), raw material cost (economics), and $\text{CO}_2$ ($CO_2$) emissions.
- **Validation of coupled ANN-GA models**: Trained and validated on hundreds of industrial batching plant records, shrinking compressive strength prediction errors to within 5 %.

## Methods

- **Database compilation**: Production records and measured mechanical properties spanning compressive strengths of $18 \sim 60\ \text{MPa}$ ($18 \sim 60 MPa$) from ready-mix plants in specific geographical regions.
- **Input variables**: Water-to-binder ratio ($W/B$), unit water content ($W$), sand-to-aggregate ratio ($S/a$), mineral admixture replacement ratios (fly ash, slag), and superplasticizer dosage.
- **Output variables**: 28 d compressive strength, slump flow, and unit volume material cost.
- **Optimization techniques**:
  - Multi-Layer Perceptron (MLP) artificial neural networks for non-linear correlation mapping.
  - Genetic algorithms for extracting Pareto-optimal fronts.

## Results

- By incorporating actual local aggregate properties, the model achieved high predictive accuracy ($R^2 = 0.94$), significantly outperforming classical empirical equations (such as Bolomey's formula).
- For a target compressive strength of $30\ \text{MPa}$ ($30 MPa$) and slump of $150\ \text{mm}$ ($150 mm$), the optimized design saved $12 \sim 15\ \text{kg/m}^3$ ($12 \sim 15 kg/m3$) of cement while achieving equivalent performance, delivering simultaneous economic and environmental benefits.

## Related Notes

- [[particle-packing-models]] — Particle packing theory for concrete mixture optimization.
- [[sustainability-low-carbon-binders]] — Low-carbon binder design and carbon mitigation technologies.
- [[lee-2009-extruded-ecc-panel-fiber-distribution]] — Fiber distribution and mechanical performance in extruded ECC panels.
