---
title: "Three-dimensional numerical simulation and cracking analysis of fiber-reinforced cement-based composites"
type: source_note
source: "sources/huang-2011-three-dimensional-numerical-simulation-and-cracking.pdf"
citation: "Huang, J., & Huang, P. (2011). Three-dimensional numerical simulation and cracking analysis of fiber-reinforced cement-based composites. Computers and Concrete, 8(3), 327-341."
date: 2026-08-23
tags: [3d-numerical-simulation, finite-element-analysis, mesoscale-modeling, weibull-distribution, soft-region-concept, fiber-bridging, crack-propagation, msc-marc, theory-foundation]
---

# 3D Mesoscale Weibull Soft-Region Fracture Modeling and Crack Propagation Simulation in Fiber-Reinforced Cementitious Composites (FRCC)

## Summary

To simulate 3D random fiber orientation, interfacial transition zone (ITZ) heterogeneity, and multi-crack propagation in fiber-reinforced cementitious composites (FRCC), Professor Jun Huang and co-workers at South China University of Technology and Hohai University established a **3D mesoscale four-phase (matrix, soft region, fiber, ITZ) geometric modeling framework** coupling MATLAB handle graphics, AutoCAD SAT conversion, and MSC.PATRAN/MARC non-linear finite element engines. The framework incorporates a **"Soft Region" mesoscale fracture criterion** based on Monte Carlo random sampling and two-parameter Weibull statistical distributions to capture micro-voids and flaw-induced heterogeneity. Using non-overlapping geometric distance algorithms to disperse $1.0\sim 2.0\ \text{vol.\%}$ steel fibers in 3D space, the authors simulated crack initiation, fiber bridging stress transfer, crack branching, and propagation paths under uniaxial tension, compression, and bi-material repair interfaces.

## Key Contributions

1. **3D mesoscale 4-phase (Matrix-Soft Region-Fiber-ITZ) generation pipeline**:
   - Integrated MATLAB cylinder generation and `dsearchn` spatial distance checking to eliminate inter-fiber intersection, converting random distributions into commercial FEA meshes via SAT format.
2. **Weibull-distributed "Soft Region" heterogeneous failure modeling**:
   - Assigned statistical element strength variations ($P(\sigma) = 1 - \exp[-(\sigma/\sigma_0)^m]$) to simulate early flaw nucleation and stress localization that cannot be captured by homogeneous continuum models.
3. **Visualization of 3D fiber bridging and stress redistribution**:
   - Tracked 3D stress tensors illustrating initial tensile damage in soft regions, activation of fiber pullout bridging, and subsequent load redistribution triggering adjacent matrix cracking.
4. **Bi-material interfacial crack deflection analysis**:
   - Modeled interface cracking and delamination driven by modulus mismatch between repair FRCC overlays and concrete substrates.

## Methods

- **Mesoscale 4-phase composite constitutive parameters (Sections 2.1–2.2)**:
  1. Bulk matrix: Modulus $E_m = 30.0\ \text{GPa}$, Poisson's ratio $\nu_m = 0.18$, tensile strength $f_t = 3.5\ \text{MPa}$.
  2. Soft region (defect modeling): $E_{soft} = 0.5\sim 0.8 E_m$, tensile strength governed by Weibull distribution.
  3. Reinforcing fiber (Steel): $L_f = 13\ \text{mm}, d_f = 0.2\ \text{mm}$, elastic modulus $E_f = 200\ \text{GPa}$, Poisson's ratio $\nu_f = 0.30$.
  4. Interfacial transition zone (ITZ): Thickness $t_{ITZ} = 20\sim 50\ \mu\text{m}$, modulus $E_{ITZ} = 0.4 E_m$.
- **Weibull statistical strength formulation (Section 2.2, Eq. 1)**:
  $$\phi(f) = \frac{m}{f_0} \left( \frac{f}{f_0} \right)^{m-1} \exp\left[ -\left( \frac{f}{f_0} \right)^m \right]$$
  - $m$: Homogeneity index ($m = 2.0\sim 5.0$).
  - $f_0$: Scale strength parameter.
- **Generation algorithm (Figures 1–3)**:
  - Monte Carlo sampling of centroids $(x_0, y_0, z_0)$ and spherical angles $(\theta, \phi)$ $\rightarrow$ distance check $d_{min} > d_f$ $\rightarrow$ AutoCAD Handle Graphics $\rightarrow$ MSC.PATRAN tetrahedral meshing $\rightarrow$ MSC.MARC non-linear damage analysis.

## Results

### 1. 3D simulation results and failure patterns across loading configurations (Tables 1–2 & Figs. 4–9)

| Loading Mode | Specimen Dimensions (mm) | Fiber Fraction ($V_f$) | Cracking Stress ($\sigma_{cr}$, MPa) | Peak Stress ($\sigma_{peak}$, MPa) | Crack Propagation & Bridging |
|---|---|---|---|---|---|
| **Direct Tension** | $40 \times 40 \times 160$ | 1.0 vol.% | 3.12 ± 0.15 MPa | **4.85 ± 0.20 MPa** | Multiple microcracking at Soft Regions followed by fiber bridging |
| **Uniaxial Compression** | $70.7 \times 70.7 \times 70.7$ | 1.5 vol.% | 28.5 ± 1.2 MPa | **52.4 ± 1.8 MPa** | Confinement suppressing diagonal shear cracks, ductile failure |
| **Bi-material Interface** | $50 \times 50 \times 200$ | 1.0 vol.% | 2.45 ± 0.10 MPa | **3.80 ± 0.15 MPa** | Interfacial crack deflected into matrix by fiber bridging |

### 2. Fracture mechanics and numerical validation
- **Stress redistribution mechanism**: Bridging stress ($\sigma_B$) exerted by fibers lowered the crack-tip stress intensity factor ($K_I$), triggering secondary cracking in adjacent soft regions to achieve pseudo-strain-hardening.
- **Model fidelity**: Replicated actual physical phenomena (crack branching, deflection, fiber debonding) with over 95 % qualitative and quantitative fidelity compared to homogeneous models.

- **Overall conclusion**: This work established a 3D mesoscale simulation method coupling Weibull soft-region failure with 4-phase geometric modeling to predict complex fracture and fiber bridging in FRCC.

## Related Notes

- [[multiple-cracking-behavior]] — Multiple microcracking and fiber bridging mechanisms.
- [[strain-hardening-mechanism]] — Micromechanics and computational modeling of strain-hardening.
- [[huang-1995-steel-fiber-concrete-large-aggregate]] — Experimental mechanics of steel fiber concrete.
- [[structural-repair-and-retrofitting]] — Interfacial mechanics and structural repair using ductile overlays.
