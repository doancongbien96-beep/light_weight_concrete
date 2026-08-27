---
title: "Dynamic Characteristics of Right-Angle Viscoelastic Dampers (Xu et al., 2023)"
type: source_note
source: "sources/xu-2023-dynamic-characteristics-of-a-novel.pdf"
citation: "Xu, Z., Zhang, C., & Li, V. C. (2023). Dynamic characteristics of a novel right-angle viscoelastic damper for seismic mitigation of building structures. Engineering Structures, 275, 115280. https://doi.org/10.1016/j.engstruct.2022.115280"
date: 2026-08-24
tags:
  - viscoelastic-damper
  - right-angle-damper
  - dynamic-characteristics
  - fractional-derivative-model
  - energy-dissipation
  - seismic-mitigation
---

## Summary
A study in which a research team from Southeast University and the University of Michigan clarified the displacement dependence, frequency dependence ($0.1 \sim 5.0 Hz$), temperature dependence ($-10 \sim +40 °C$), and equivalent damping ratio behavior of a novel right-angle viscoelastic damper (RAVED) that laminates a high-damping viscoelastic polymer matrix (loss factor $\eta > 0.85$) between right-angle steel plates, through dynamic shear fatigue tests and a five-parameter fractional derivative constitutive model, in order to simultaneously control seismic and wind-induced vibration responses of building and civil structures. It was demonstrated that the right-angle arrangement absorbs two-directional seismic displacements simultaneously and increases the equivalent damping ratio up to **28.5 %**.

## Key Contributions
- **Structural mechanism of the novel right-angle two-directional viscoelastic damper (RAVED) established**: orthogonal two-axis interstory displacements absorbed and dissipated independently by a single device.
- **Fractional derivative viscoelastic constitutive equation established**: prediction accuracy of 96 % achieved for frequency-temperature coupled shear stiffness $G'(\omega, T)$ and loss factor $\eta(\omega, T)$.
- **Ultra-high energy dissipation stability demonstrated**: energy degradation kept below 5 % after 30 repeated cycles at 100 % shear strain.
- **Interstory displacement of frame structures reduced by 65 % demonstrated**: seismic performance verified through shaking-table tests of a five-story full-scale frame.

## Methods
- Damper fabrication: high-damping acrylic rubber matrix (thickness 10 mm, shear area $150 \times 150 mm$), Q345 steel frame.
- Test conditions: MTS high-performance actuator, displacement amplitude $\gamma = 20 \sim 200 \%$, frequency $f = 0.1, 0.5, 1.0, 2.0, 5.0 Hz$, temperature $-10, 0, 20, 40 °C$.
- Analysis: MATLAB/Simulink-based nonlinear hysteresis loop fitting and development of an ABAQUS user subroutine.

## Results
- Damper dynamic parameter data by excitation frequency and shear strain:

| Frequency $f$ (Hz) | Shear strain $\gamma$ (%) | Storage shear stiffness $K'$ ($kN/mm$) | Loss shear stiffness $K''$ ($kN/mm$) | Loss factor $\eta$ | Dissipated energy per cycle $E_D$ ($kJ$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.1 Hz | 100 % | 4.25 | 3.65 | 0.86 | 2.85 |
| 1.0 Hz | 100 % | **6.80** | **6.12** | **0.90** | **4.78** |
| 5.0 Hz | 100 % | 9.45 | 7.85 | 0.83 | 6.15 |
| 1.0 Hz | 200 % | 5.80 | 5.25 | 0.91 | 9.85 |

## Related Notes
- [[orban-2011-damping-materials-members-structures]] - structural and material damping theory
- [[muthusamy-2010-graphite-network-damping]] - graphite high-damping composites
- [[xue-2013-rubberized-concrete-energy-dissipation-structural]] - energy dissipating structural materials
