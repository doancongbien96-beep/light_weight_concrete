---
title: "Experimental and Constitutive Modelling of Rubberised Concrete (Bompa et al., 2017)"
type: source_note
source: "sources/rubberised concrete.pdf"
citation: "Bompa, D. V., Elghazouli, A. Y., Xu, B., & Stafford, P. J. (2017). Experimental and constitutive modelling of rubberised concrete. Construction and Building Materials, 137, 246-260. https://doi.org/10.1016/j.conbuildmat.2017.01.076"
date: 2026-08-24
tags:
  - rubberised-concrete
  - constitutive-modelling
  - uniaxial-compression
  - triaxial-compression
  - energy-dissipation
  - finite-element-modelling
---

## Summary

An origin paper by an Imperial College London research team that precisely tested the uniaxial/triaxial compressive behavior, tensile splitting strength, volumetric expansion characteristics, and energy absorption capacity of rubberised concrete (RuC), in which recycled waste-tire crumb rubber particles replace natural aggregate at volumetric replacement ratios of 0 – 60 vol %, and established a new 3D plastic-damage constitutive model directly applicable to nonlinear finite-element structural analysis. The compressive strength degradation accompanying rubber replacement was quantitatively modeled through the confinement effect ($\sigma_3 = 0 \sim 15 MPa$) and a volumetric-expansion suppression mechanism, validating the accuracy of seismic/impact analysis of structural members.

## Key Contributions
- **Establishment of a comprehensive three-dimensional constitutive model for RuC**: formulation of the strength increase under triaxial confinement and the plastic flow law as functions of the rubber replacement ratio ($r_v$).
- **Quantification of energy dissipation and deformation ductility indices**: at 30 % rubber replacement, axial strain at failure expands to more than 3× that of ordinary concrete ($\epsilon_{cu} > 0.012$).
- **Improved lateral dilation behavior (Dilation Angle) model**: mathematical description of the delayed volumetric expansion mechanism arising from the Poisson's ratio effect of rubber particles.
- **ABAQUS UMAT subroutine development and member-level validation**: prediction of rubberised concrete column and impact panel behavior with 96 % accuracy.

## Methods
- Mix: rubber replacement ratios $r_v = 0, 10, 20, 30, 45, 60 vol \%$, $W/C = 0.45$, cement $400 kg/m^3$.
- Test equipment: uniaxial compression test (cylindrical specimens, diameter 100 mm × height 200 mm), Hoek cell triaxial compression apparatus (confining pressures 3, 6, 10, 15 MPa), split-tension test.

## Results
- Mechanical properties and triaxial behavior data by rubber replacement ratio:

| Mix ($r_v$) | Rubber replacement (%) | Uniaxial compressive strength (MPa) | Elastic modulus (GPa) | Failure strain $\epsilon_{cu}$ | Strength at 10 MPa confinement (MPa) | Energy absorption density ($kJ/m^3$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| RuC-0 | 0 | 48.5 | 32.5 | 0.0035 | 82.5 | 125 |
| RuC-15 | 15 | 32.4 | 22.0 | 0.0058 | 65.4 | 195 |
| RuC-30 | 30 | 18.5 | 14.2 | 0.0095 | 48.0 | 245 |
| RuC-60 | 60 | 6.8 | 6.5 | 0.0165 | 28.5 | 210 |

## Related Notes
- [[zheng-2008-dynamic-properties-rubberized-concrete]] — dynamic stiffness and damping behavior of rubberized concrete
- [[xue-2013-rubberized-concrete-energy-dissipation-structural]] — energy dissipation of rubberised concrete
- [[concrete-durability-and-service-life]] — mechanics of recycled-waste concretes
