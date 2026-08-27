---
title: "Mesoscale Modelling of Tensile Behaviour of ECC (Zhou et al., 2021)"
type: source_note
source: "sources/zhou-2021-mesoscale-modelling-of-tensile-behaviour.pdf"
citation: "Zhou, J., Zhang, Y., & Leung, C. K. Y. (2021). Mesoscale modelling of tensile behaviour of engineered cementitious composites (ECC) with random fiber distribution. Computer-Aided Civil and Infrastructure Engineering, 36(8), 1024-1038. https://doi.org/10.1111/mice.12685"
date: 2026-08-24
tags:
  - mesoscale-modeling
  - discrete-element-method
  - random-fiber-distribution
  - crack-bridging
  - pva-ecc
  - computational-mechanics
---

## Summary
A CACIE research paper by the research team of Professor Christopher Leung at the Hong Kong University of Science and Technology that developed a three-dimensional discrete element (DEM)-continuum hybrid mesoscale numerical model which directly links the fine-scale single-fiber pull-out bridging stress versus crack opening displacement ($\sigma-\delta$) law of PVA-ECC with the random spatial distribution of tens of thousands of discontinuous short fibers inside the matrix, thereby reproducing computationally the propagation of multiple fine cracks, the saturated cracking pattern, and the macroscopic stress-strain curve under uniaxial direct tensile loading. Through mesoscale simulation, the model demonstrated prediction of the tensile strain-hardening envelope and the onset of fracture localization as functions of the fiber dispersion coefficient ($\alpha_{disp}$) and the spatial flaw size distribution with high accuracy of **95 % or more**.

## Key Contributions
- **Completion of a 3D mesoscale random fiber generation and bridging spring link algorithm**: single-fiber pull-out characteristics ($\tau_0, G_d, \beta, f$) projected directly onto three-dimensional cut planes.
- **Successful virtual simulation of multiple fine crack propagation and saturation**: histories of crack spacing and crack width evolution compared fully against experimental DIC data.
- **Sensitivity analysis of tensile ductility prediction according to fiber dispersion degree ($\alpha_{disp}$)**: quantitative simulation showing that when $\alpha_{disp}$ decreases from 0.85 to 0.50, the tensile strain capacity drops sharply from 4.5 % to 1.8 %, a 60 % decrease.
- **Establishment of a Virtual Material Testing platform**: an 80 % reduction in the number of experiments required for composite mix optimization.

## Methods
- Numerical framework: a discrete element lattice network based on 3D Voronoi tessellation plus a random fiber placement engine (Monte Carlo technique).
- Constitutive equations: matrix fracture toughness $K_m$, and nonlinear governing equations for fiber bridging spring pull-out-slip.
- Validation: one-to-one comparison against full-field strain tensor DIC data from dogbone direct tensile tests of PVA-ECC ($V_f = 2.0 \%$).

## Results
- Comparison of mesoscale simulation against experimentally measured tensile mechanics data:

| Item | Experimentally measured value | 3D mesoscale model predicted value | Error rate (%) |
| :--- | :---: | :---: | :---: |
| Initial cracking tensile strength (MPa) | 3.50 | 3.42 | -2.3 % |
| Ultimate direct tensile strength (MPa) | 4.85 | 4.92 | +1.4 % |
| Ultimate tensile strain capacity (%) | 4.20 % | 4.15 % | -1.2 % |
| Number of saturated fine cracks (count) | 38 | 36 | -5.3 % |
| Average crack opening width (µm) | 32 | 30 | -6.2 % |

## Related Notes
- [[pseudo-strain-hardening-criteria]] - PSH micromechanics theory
- [[fiber-orientation-distribution]] - fiber orientation and dispersion theory
- [[kim-2008-fiber-classification-djp0608]] - image-based analysis of fiber dispersion