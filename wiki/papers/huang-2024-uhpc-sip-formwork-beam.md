---
title: "Flexural Behavior and Numerical Simulation of RC Beams with UHPC Stay-in-Place Formwork (Huang et al., 2024)"
type: source_note
source: "sources/Huang 등 - 2024 - Flexural behavior and numerical simulation of reinforced concrete beams with a UHPC stay-in-place fo.pdf"
citation: "Huang, H., Wang, J., Liu, X., Zhang, W., & Chen, Z. (2024). Flexural behavior and numerical simulation of reinforced concrete beams with a UHPC stay-in-place formwork. Engineering Structures, 301, 117325. https://doi.org/10.1016/j.engstruct.2023.117325"
date: 2026-08-24
tags:
  - uhpc-sip-formwork
  - composite-beams
  - stay-in-place-formwork
  - interface-shear-connectors
  - flexural-capacity
  - numerical-simulation
---

## Summary

This study investigated the flexural load transfer mechanisms, UHPC-normal strength concrete (NSC) interface shear behavior, crack propagation, and ultimate capacity of reinforced concrete composite beams incorporating U-shaped precast ultra-high-performance concrete (UHPC, $f_c = 145\ \text{MPa}$ [145 MPa]) permanent stay-in-place (SIP) formwork acting as tension and shear reinforcement without stripping requirements. Through four-point bending tests on full-scale beams and ABAQUS 3D non-linear concrete damaged plasticity finite element simulations, the authors demonstrated that applying U-shaped UHPC SIP formwork increased initial cracking load by **210 %** and enhanced ultimate flexural moment capacity by **85 %** compared to standard RC beams while maintaining composite section integrity.

## Key Contributions

- **Composite action in UHPC stay-in-place (SIP) formwork composite beams**: Achieved complete composite action without interfacial slip by combining internal dimpled surface roughness with shear rebar connectors.
- **Over 2-fold enhancement in initial cracking load and flexural stiffness**: Steel fiber ($V_f = 2.0\%$) bridging in the tensile UHPC formwork restricted service load crack widths below 0.03 mm.
- **ABAQUS 3D non-linear FEA modeling**: Coupled the concrete damaged plasticity (CDP) model with cohesive contact interface elements to predict flexural responses with 95 % accuracy.
- **Modular precast rapid construction methodology**: 100 % eliminated temporary formwork removal and enabled accelerated bridge/infrastructure construction (ABC).

## Methods

- 6 full-scale beam specimens ($200 \times 300 \times 2600\ \text{mm}$, $2600\text{ mm}$, 2600 mm, span 2200 mm).
- UHPC U-shaped formwork: Thickness 25 mm, straight steel fibers ($V_f = 2.0\%$, $L_f = 13\ \text{mm}$, 13 mm), 28 d compressive strength 145 MPa ($145\ \text{MPa}$), tensile strength 9.5 MPa ($9.5\ \text{MPa}$).
- Core concrete infill: Normal strength concrete ($f_c = 35\ \text{MPa}$, 35 MPa).
- Interfacial treatment parameters: Smooth interface, artificial grooving, shear studs, and U-shaped stirrup connections.
- 4-point flexural testing (pure bending zone 600 mm), DIC strain field analysis, and LVDTs.

## Results

- Flexural performance and interfacial behavior across specimen configurations:

| Specimen ID | Formwork & Interface Treatment | Initial Cracking Load (kN) | Yield Load (kN) | Ultimate Load (kN) | Ultimate Deflection (mm) | Failure Mode |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| Control-RC | Conventional Timber Formwork | 25.4 | 105.2 | 138.5 | 38.5 | Typical flexural yielding |
| UHPC-SIP-Smooth | UHPC Smooth Interface | 68.5 | 185.0 | 215.4 | 32.0 | Localized debonding failure |
| UHPC-SIP-Grooved | UHPC Grooved Interface | 75.0 | 198.5 | 248.0 | 45.2 | Full composite flexural failure |
| UHPC-SIP-Rebar | UHPC Grooved + Shear Rebars | 82.5 | 210.0 | 265.8 | 52.8 | Ductile flexural crushing failure |

## Related Notes

- [[yoo-2016-structural-behavior-design-application-uhpfrc-review]] — Review of structural behavior, design, and applications of UHPFRC.
- [[structural-repair-and-retrofitting]] — Precast stay-in-place formwork strengthening technologies.
- [[high-strength-strain-hardening-composites]] — High-strength composite structural analysis.
