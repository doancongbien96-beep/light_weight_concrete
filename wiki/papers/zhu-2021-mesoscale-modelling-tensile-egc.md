---
title: "Mesoscale Modelling of Tensile Strain-Hardening Behavior of EGC (Zhu et al., 2021)"
type: source_note
source: "sources/zhu-2021-mesoscale-modelling-of-tensile-strain-hardening.pdf"
citation: "Zhu, H., Zhang, Z., & Wu, C. (2021). Mesoscale modelling of tensile strain-hardening behavior of engineered geopolymer composites (EGC) with 3D discrete lattice model. Construction and Building Materials, 295, 123680. https://doi.org/10.1016/j.conbuildmat.2021.123680"
date: 2026-08-24
tags:
  - engineered-geopolymer-composites
  - mesoscale-modeling
  - discrete-element-method
  - 3d-lattice-model
  - pva-fiber
  - computational-micromechanics
---

## Summary
A study by Dr. H. Zhu's research team at the University of Western Australia, Australia that developed a mesoscale computational mechanics analysis framework integrating a three-dimensional discrete lattice network model (3D Discrete Lattice Model) with the single PVA fiber pullout bridging law ($\sigma-\delta$), in order to interpret numerically the fine crack propagation, saturated multiple crack spacing, and macroscopic stress-strain responses of eco-friendly strain-hardening geopolymer composites (PVA-EGC) under uniaxial direct tension. By fully simulating the three-dimensional random orientation of tens of thousands of fibers inside the composite and alkali geopolymer interfacial friction slip, it proved that the tensile strain-hardening envelopes and fracture crack width evolution histories were predicted with **96 % accuracy against measurements**.

## Key Contributions
- **Geopolymer-dedicated 3D discrete lattice mesoscale model developed**: brittle matrix fracture and interface slip bridging formalized as beam-spring coupled lattices.
- **Multiple fine crack initiation and saturation simulation demonstrated**: opening of more than 40 individual fine cracks and stress redistribution behavior compared one-to-one with DIC experiments.
- **PSH envelope sensitivity analysis by fiber volume fraction ($V_f = 1.0 \sim 2.5 \%$)**: hardening initiation threshold content derived as $V_f^{crit} = 0.85 \%$.
- **Computational mix design platform for eco-friendly ductile composites completed**: new mix development time cut by 75 %.

## Methods
- Numerical model: 3D irregular lattice mesh (mean cell size 1.5 mm) + nonlinear fracture dissipation springs.
- Bridging constitutive relation: chemical bond $G_d = 1.25 J/m^2$, frictional stress $\tau_0 = 1.65 MPa$, slip-hardening coefficient $\beta = 0.20$.
- Experimental verification: comparison against full-field DIC strain tensor data from dogbone direct tension tests.

## Results
- Comparison of tensile mechanical data between 3D lattice simulation and experimental measurement:

| Property | Experimental value | 3D lattice mesoscale prediction | Error (%) |
| :--- | :---: | :---: | :---: |
| First-crack tensile strength (MPa) | 3.80 | 3.72 | -2.1 % |
| Ultimate direct tensile strength (MPa) | 5.60 | 5.75 | +2.7 % |
| Ultimate tensile strain capacity (%) | 4.80 % | 4.68 % | -2.5 % |
| Number of saturated fine cracks | 42 | 40 | -4.8 % |
| Mean crack opening width (µm) | 35 | 33 | -5.7 % |

## Related Notes
- [[zhou-2021-mesoscale-modelling-tensile-ecc]] - ECC mesoscale numerical model
- [[one-part-shgc]] - high-ductility geopolymer design theory
- [[pseudo-strain-hardening-criteria]] - PSH micromechanics theory
