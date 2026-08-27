---
title: "Simulation of Flexural Performance of Layered ECC-Concrete Composite Beam (Zhang et al., 2014)"
type: source_note
source: "sources/zhang-2014-simulation-of-flexural-performance-of.pdf"
citation: "Zhang, J., Wang, Z., & Ju, X. (2014). Simulation of flexural performance of layered ECC-concrete composite beam with fracture mechanics approach. ASCE Journal of Engineering Mechanics, 140(9), 04014068. https://doi.org/10.1061/(ASCE)EM.1943-7889.0000780"
date: 2026-08-24
tags:
  - layered-ecc-concrete-beam
  - fracture-mechanics-simulation
  - cohesive-crack-model
  - interface-debonding
  - flexural-behavior
  - damage-mitigation
---

## Summary
An ASCE Journal of Engineering Mechanics landmark paper by Professor J. Zhang's research team at Tsinghua University clarifying, through a fracture-mechanics cohesive crack model and nonlinear finite element analysis (FEA), the crack dispersion of two-layer beams (Layered ECC-Concrete Beams) that composite a high-ductility ECC layer onto the tension side of reinforced concrete flexural members, the substrate-ECC interface shear debonding, and the flexural load-deflection responses. The mechanism by which the stress concentration at the substrate concrete crack tip is dispersed by the multiple fine-crack bridging network of the tension-side ECC layer, preventing interfacial shear delamination and increasing the ultimate flexural load by **38 %**, was modeled with complete mathematical rigor.

## Key Contributions
- **Three-dimensional fracture mechanics finite element framework for crack propagation in two-layer composite beams established**: the discontinuous cracks of the substrate and the continuous multiple-cracking damage field of the ECC integrated through cohesive contact elements.
- **Formula derived for the interface debonding initiation limit shear stress ($\tau_{int}$) between substrate and ECC**: critical fracture energy $G_{int}$ formulated as a function of substrate surface roughness.
- **Optimal flexural efficiency curve presented versus ECC layer thickness ratio ($h_{ecc}/h = 0.1 \sim 0.4$)**: maximum cost-to-capacity improvement ratio found at $h_{ecc}/h = 0.25$.
- **Perfect consistency with full-scale flexural experiments verified**: load-deflection curves and crack widths achieved within a 4 % error rate between analysis and measurement.

## Methods
- Numerical model: ABAQUS nonlinear solver with user subroutine UMAT implementing the ECC tensile strain-hardening constitutive equation.
- Interface model: bilinear cohesive zone model ($G_c = 150 J/m^2$, $\tau_{max} = 3.5 MPa$).
- Verification: comparison against four-point bending test data of $150 \times 250 \times 2000 mm$ composite beams.

## Results
- Comparison table of flexural performance between numerical simulation and experimental measurements:

| Item | Experimental value | Cohesive fracture mechanics FEA | Prediction error (%) |
| :--- | :---: | :---: | :---: |
| Initial flexural crack load (kN) | 36.5 | 35.8 | -1.9 % |
| Rebar yield load (kN) | 98.0 | 99.5 | +1.5 % |
| Ultimate flexural load (kN) | 125.4 | 128.0 | +2.1 % |
| Midspan deflection at failure (mm) | 52.5 | 50.8 | -3.2 % |
| Maximum tension-side crack width (mm) | 0.035 | 0.032 | -8.5 % |

## Related Notes
- [[yun-2013-flexural-behavior-crack-mitigation-shcc-layer]] - origin experiment of SHCC layer composite beam flexure
- [[khan-2016-hsc-shcc-layer-beam]] - behavior of high-strength composite beams
- [[shin-2011-strengthening-dfrcc-layers-rc-flexural-members]] - DFRCC overlay flexural strengthening
