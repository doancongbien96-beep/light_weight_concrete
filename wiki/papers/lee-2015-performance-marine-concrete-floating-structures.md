---
title: "Analytical Estimation of Performance of Marine Concrete Floating Structures (Lee et al., 2015)"
type: source_note
source: "sources/lee-2015-analytical-estimation-of-the-performance.pdf"
citation: "Lee, B. Y., Bang, J. W., & Kim, Y. Y. (2015). Analytical estimation of the performance of marine concrete floating structures exposed to harsh ocean environment. International Journal of Offshore and Polar Engineering, 25(3), 215-222."
date: 2026-08-24
tags:
  - marine-concrete
  - floating-structures
  - chloride-penetration
  - service-life-prediction
  - crack-width-control
  - ocean-environment
---

## Summary

When very large floating structures (VLFS) are exposed over the long term to a harsh ocean environment (repeated wave flexural loading, chloride penetration in the seawater splash zone, repeated wet-dry cycles), precise prediction of crack occurrence, chloride-ion diffusion, rebar corrosion initiation time, and residual service life demands an integrated performance-evaluation numerical framework combining fluid-structure coupled wave response analysis, crack-width-controlled nonlinear section analysis, and an unsteady-state chloride diffusion model based on Fick's second law. This landmark paper in marine civil engineering by Professors Bang Yeon Lee, Jin Wook Bang, and Yun Yong Kim demonstrated that applying high-ductility SHCC on the tension side to control crack widths to $0.05 mm$ or less can extend the structure's target service life from 50 years to **more than 100 years**.

## Key Contributions

- **Completion of a multi-physics coupled analysis model linking wave loading and chloride penetration for marine floating structures**: integration of member flexural tensile stress and chloride penetration rate as functions of significant wave height and wave period.
- **Quantification of the effective chloride diffusion coefficient as a function of fine crack width ($D_{cr} = D_0 [1 + a (w/w_0)^b]$)**: demonstration of the chloride-penetration delay effect when crack width is restrained below $0.1 mm$.
- **Limit-state service-life evaluation of floating structures by cover thickness and material**: applying high-ductility SHCC extends the rebar corrosion initiation time 2.8-fold compared with ordinary concrete.
- **Design guidance for offshore plants and sea airport/port floating structures**: establishment of economical corrosion-protection maintenance strategies.

## Methods

- Wave load analysis: hydrodynamic wave moment estimation based on the three-dimensional boundary element method (BEM) ($H_s = 4.5 m, T_p = 10.5 s$).
- Section analysis: nonlinear moment-curvature analysis and crack-width calculation for RC and SHCC composite members.
- Durability analysis: finite difference method (FDM)-based two-dimensional chloride penetration and numerical analysis of the time to reach the critical chloride concentration ($C_{cr} = 1.2 kg/m^3$).

## Results

- Comparison table of predicted service life per pontoon member:

| Member section configuration | Cover thickness (mm) | Max crack width (mm) | Effective diffusion coefficient ($10^{-12} m^2/s$) | Rebar corrosion initiation life (years) | 100-year service life achieved |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Ordinary RC (NC 35 MPa) | 50 | 0.28 | 8.5 | 28 | Not possible (early repair required) |
| High-durability RC (HPC 60 MPa) | 70 | 0.18 | 3.2 | 55 | Partially satisfied |
| **SHCC composite member** | **50** | **0.035** | **0.85** | **> 120** | **Fully satisfied (100 years guaranteed)** |

## Related Notes

- [[concrete-durability-and-service-life]] - concrete durability and service life theory
- [[crack-width-control]] - corrosion protection of marine structures through microcrack control
- [[zhu-2014-autogenous-healing-marine-ecc]] - autogenous healing composites under marine environments
