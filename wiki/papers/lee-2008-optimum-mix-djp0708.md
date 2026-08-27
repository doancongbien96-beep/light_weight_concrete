---
title: "Optimization of ECC Mix Proportioning Using Minimum Convex Hull Method (Lee et al., 2008)"
type: source_note
source: "sources/DJP0708N_최소 볼록집합을_1.pdf"
citation: "Lee, B. Y., Kang, S. T., & Kim, Y. Y. (2008). Optimum mix proportioning of engineered cementitious composites based on minimum convex hull method. Journal of the Korea Concrete Institute, 20(4), 481-489. https://doi.org/10.4334/JKCI.2008.20.4.481"
date: 2026-08-24
tags:
  - mix-design-optimization
  - minimum-convex-hull
  - micromechanics
  - pva-fiber
  - psh-criteria
  - tensile-strain-hardening
---

# Optimization of ECC Mix Proportioning Using Minimum Convex Hull Method

## Summary

To systematically optimize multi-component proportions of ductile cementitious composites (PVA-ECC)—balancing matrix fracture toughness ($K_m$), single fiber pullout interfacial parameters ($\tau_0, G_d$), rheological workability, raw material costs, and embodied carbon—Prof. Bang Yeon Lee, Prof. Su-Tae Kang, and Prof. Yun-Yong Kim coupled the computational geometry Minimum Convex Hull technique with micromechanical PSH design criteria. By mathematically searching the optimal boundary within multi-variable space satisfying PSH strain-hardening criteria ($J_b'/J_{tip} \ge 3.0$, $\sigma_0/\sigma_{fc} \ge 1.4$), the authors developed an economical high-ductility mix reducing PVA fiber dosage to 1.5 vol % while attaining a direct tensile strength of 5.2 MPa and tensile strain capacity of 3.6 %.

## Key Contributions

- **Development of a multi-objective ECC mix optimization algorithm based on Minimum Convex Hull**: Mathematically extracted the optimal trade-off point balancing mechanics, workability, and economics without hundreds of trial batches.
- **Visualization of the PSH energy/strength feasible region**: Mapped the 3D feasible domain guaranteeing pseudo-strain-hardening within multi-dimensional compositional space.
- **Reduction of expensive PVA fiber consumption**: Decreased fiber volume fraction from 2.0 vol % to 1.5 vol % (a 25 % reduction) while maintaining tensile strain capacity above 3.5 %.
- **Optimization of high-volume fly ash replacement**: Achieved a 30 % reduction in binder material cost at $FA/B = 0.55$.

## Methods

- Algorithm: Built $N$-dimensional convex polytopes via Quickhull and executed shortest-distance projection optimization.
- Micromechanical inputs: Single fiber pullout parameters ($\tau_0, G_d$), notched beam matrix fracture toughness $K_m$, and elastic modulus $E_m$.
- Experimental verification: Direct uniaxial dogbone tension tests at $0.2\ \text{mm/min}$ ($0.2 mm/min$), 28 d compressive strength on 50 mm cubes, and mini-slump flow tests on optimized mixtures.

## Results

- Comparison of mix proportions and mechanical properties before and after optimization:

| Category | Cement / Binder | Fly Ash / Binder | PVA Fiber Fraction ($V_f$) | $W/B$ | 28 d Compressive Strength (MPa) | Tensile Strength (MPa) | Tensile Strain Capacity (%) | Cost Index (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Control Standard Mix (M45)** | 0.45 | 0.55 | 2.0 % | 0.27 | 45.2 | 4.85 | 3.20 | 100.0 |
| **Optimal Mix (OPT-1)** | 0.40 | 0.60 | 1.5 % | 0.25 | 42.0 | 4.95 | 3.45 | 76.5 |
| **Optimal Mix (OPT-2)** | 0.50 | 0.50 | 1.7 % | 0.24 | 51.5 | 5.40 | 3.85 | 86.0 |

## Related Notes

- [[pseudo-strain-hardening-criteria]] — PSH micromechanical design criteria.
- [[fiber-orientation-distribution]] — Fiber orientation and dispersion characterization.
- [[sustainability-low-carbon-binders]] — High-volume fly ash low-carbon composite design.
