---
title: "최소 볼록 집합을 이용한 데이터베이스 기반 콘크리트 최적 배합 (Lee et al., 2008)"
type: source_note
source: "sources/2008-concrete-optimum-mixture-proportioning-based.pdf"
citation: "이방연, 김재홍, 김진근. \"최소 볼록 집합을 이용한 데이터베이스 기반 콘크리트 최적 배합.\" 한국콘크리트학회 논문집, Vol. 20, No. 5 (2008), pp. 627~634. (Lee, B.-Y., Kim, J.-H., Kim, J.-K. \"Concrete Optimum Mixture Proportioning Based on a Database Using Convex Hulls.\")"
date: 2026-08-22
tags: [mix-optimization, genetic-algorithm, neural-network, convex-hull, database-driven-design]
---

# Database-Driven Concrete Mix Optimization: Convex Hull Feasible Region Constraints

## Summary

When optimizing concrete mix proportions using database-trained predictive models, this study proposes constraining the search space to the minimum convex hull of the training database rather than simplistic min-max component bounding boxes. Implemented using a 3-element pipeline—Genetic Algorithms (optimization) + Artificial Neural Networks (strength prediction) + QuickHull (feasible region evaluation)—the method was validated on least-cost mixture design problems targeting specified compressive strengths. Experimental trials demonstrated that candidate mixtures outside the convex hull suffered severe strength collapse, quantitatively verifying the risks of machine learning extrapolation.

## Key Contributions

1. **Effective region concept**: Defined search bounds strictly within the database interpolation envelope. For a candidate proportion vector $x$, if the convex hull of the database alone equals the convex hull of the database plus $\{x\}$ ({x}), $x$ is valid; otherwise it is rejected. Unlike arbitrary windowing, this domain is determined automatically without user hyperparameters.
2. **Experimental validation of extrapolation risks**: Min-max search mixtures (CX series) appeared ~16 % cheaper than convex hull mixtures (CO series), but the measured strength of CX40 was only 3.81 MPa (predicted 41.1 MPa, relative error 978 %) due to inadequate paste volume, resulting in zero slump (KS F 2402) and severe segregation. In contrast, CO series mixtures achieved errors $\le 8.13\%$ and satisfied all target strengths.
3. **Integrated implementation framework**: ANN (4 component weights as input, 1 hidden layer, 4-4-1 architecture selected via cross-validation, jack-knife correlation coefficient $R = 0.954$) + real-coded GA (population 100, roulette selection 10 % / crossover 70 % / mutation 20 %, termination after 50 generations without improvement) + penalty objective function (cost minimization, total volume tolerance ±0.1 % / 0.1 %).

## Methods

- Database: 179 selected mixtures from over 3,000 (3000) data points in the Japanese New RC project. Criteria: 4 components only (cement, water, fine aggregate, coarse aggregate), Type 1 Portland cement, 28 d compressive strength, no admixtures. Ranges: W/C 20.0~70.0 % (mean 40.0), water 108~225 kg/m^3, cement 252~900, fine aggregate 349~1074, coarse aggregate 452~1416, strength 11.0~145 MPa (mean 54.5). Over 80 % cured under 20 °C water.
- ANN: Hyperbolic tangent hidden transfer function, linear output. Trained via Levenberg-Marquardt with weight decay. Architecture 4-4-1 selected across 1~7 hidden nodes $\times$ 10 cross-validations $\times$ 20 repeats.
- Convex Hull: Quickhull algorithm (Barber et al. 1996).
- Objective function: $\text{fitness} = f_{\text{cost}} + f_{\text{vol}} + f_{\text{reg}} + f_{\text{str}}$ (fitness = f_cost + f_vol + f_reg + f_str). Unit costs (KRW/kg): water 0, cement 79.2, fine aggregate 3.70, coarse aggregate 2.83.
- Experimental testing: $\varnothing 100 \times 200\ \text{mm}$ (Ø100 × 200 mm) cylinders, KS F 2405 compression tests, 8 specimens per mix.

## Results

| Series | Search Method | Target Strength | W/C (%) | Mix Proportions (Water / Cement / Sand / Gravel, kg/m^3) | Unit Cost (KRW/m^3) | Predicted Strength (MPa) |
|---|---|---|---|---|---|---|
| **CX40** | min-max | 40 MPa | 45.5 | 138 / 303 / 1027 / 1003 | 31,635 | 41.1 |
| **CX50** | min-max | 50 MPa | 37.7 | 117 / 310 / 863 / 1227 | 32,428 | 53.2 |
| **CX60** | min-max | 60 MPa | 37.6 | 140 / 372 / 764 / 1210 | 36,838 | 61.2 |
| **CO40** | convex hull | 40 MPa | 49.4 | 193 / 391 / 935 / 875 | 37,763 | 43.9 |
| **CO50** | convex hull | 50 MPa | 39.6 | 155 / 391 / 825 / 1090 | 38,203 | 54.5 |
| **CO60** | convex hull | 60 MPa | 34.5 | 166 / 481 / 840 / 969 | 44,865 | 64.5 |

- Measured strengths (relative error vs predicted): CO40 = 40.6 MPa (std dev 0.91, 8.13 %), CO50 = 51.3 MPa (1.93, 6.24 %), CO60 = 61.2 MPa (1.07, 5.39 %) — all met target requirements. In contrast, CX40 reached only 3.81 MPa (978 % error); CX50 and CX60 were omitted due to obvious batching failure.
- Conclusion: Unconstrained search space expansion lowers apparent cost but fails constructability and strength requirements. Convex hull bounding is essential for data-driven mix proportioning reliability.

## Related Notes

- [[kan-2025-hybrid-pe-low-cost-egc]] — Cost-optimized EGC mix design and trade-offs.
- [[feng-2024-chloride-egc-mix-parameters]] — Empirical mapping between mixture factors and performance.
- [[artyk-2024-low-activity-fly-ash-hybrid-fiber-egc]] — Micromechanics-based mix design charts.
- [[bagheri-2019-ann-gp-boroaluminosilicate-geopolymer]] — ANN+GP function approximation for geopolymer strength.
