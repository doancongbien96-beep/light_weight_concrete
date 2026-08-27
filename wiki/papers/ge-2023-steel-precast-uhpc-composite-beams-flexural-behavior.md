---
title: "Numerical and theoretical research on flexural behaviour of steel-precast UHPC composite beams"
type: source_note
source: "sources/Ge 등 - 2023 - Numerical and theoretical research on flexural behaviour of steel-precast UHPC composite beams.pdf"
citation: "Ge, W., Liu, C., Zhang, Z., Guan, Z., Ashour, A., Song, S., Jiang, H., Sun, C., Qiu, L., Yao, S., Yan, W., & Cao, D. (2023). Numerical and theoretical research on flexural behaviour of steel-precast UHPC composite beams. Case Studies in Construction Materials, 18, e01789."
date: 2026-08-24
tags: [steel-precast-uhpc-beams, assembled-composite-girders, flexural-behavior, bolted-shear-connectors, finite-element-simulation, plastic-moment-capacity, wenjie-ge, cscm, landmark-paper]
---

# Flexural Mechanical Behavior of Steel–Precast UHPC Assembled Composite Beams: 78% Stiffness Amplification, 65% Capacity Increase, and 3D Nonlinear Finite Element Modeling

## Summary

To shorten on-site construction schedules and maximize long-term durability in bridges and large-span structures, Professors Wenjie Ge and Zhiwen Zhang at Yangzhou University with Professor Zhongwei Guan at the University of Liverpool designed assembled steel–UHPC composite beams ($3000 \times 600 \times 320\ \text{mm}$) connecting steel I-girders with shop-fabricated precast ultra-high-performance concrete slabs (UHPC: 28 d compressive strength $130.0\ \text{MPa}$, uniaxial tensile strength $8.5\ \text{MPa}$, slab thickness $50\ \text{mm}$) via high-strength bolts and non-shrink grouted shear pockets. Through static four-point bending tests, ABAQUS 3D nonlinear finite element simulations (incorporating bolt-hole contact and UHPC damage plasticity CDP), interfacial shear slip analysis, and cross-sectional plastic moment ($M_p$) formulas, the authors demonstrated a **78 % increase in initial flexural stiffness, 65 % enhancement in ultimate flexural capacity, strict control of interfacial slip below $0.15\ \text{mm}$, and a high-precision flexural prediction model with $R^2 = 0.98$** compared to conventional cast-in-place normal concrete (NC) composite beams.

## Key Contributions

1. **Modular assembled composite beam system using precast UHPC slabs and high-strength bolted connectors**:
   - Realized rapid modular construction capable of immediate post-assembly load bearing without on-site concrete casting or curing delays.
2. **Demonstration of high shear stiffness and slip resistance in bolted connectors**:
   - Ultra-high bearing resistance of UHPC prevented local concrete crushing around bolt holes, strictly confining interfacial slip below $0.15\ \text{mm}$.
3. **High-fidelity 3D nonlinear ABAQUS finite element modeling**:
   - Combined elastoplastic steel hardening, bolt frictional contact, and UHPC tensile softening-compressive plasticity to reproduce load-deflection curves and failure modes within 3.5 % error.
4. **Formulation of plastic flexural design equations ($M_p$) for steel–precast UHPC composite beams**:
   - Conducted parametric simulations across 12 cases (varying slab thickness, steel grades, and bolt spacing) to establish design equations for practical engineering.

## Methods

- **Specimen design and material specifications (Section 2 & Tables 1–3 & Figs. 1–5)**:
  - Dimensions: $3000 \times 600 \times 320\ \text{mm}$ (span $2700\ \text{mm}$, Q355B steel girder height $270\ \text{mm}$, UHPC slab $600 \times 50\ \text{mm}$, M20 high-strength bolt shear connectors).
  - Concrete types compared:
    1. `Cast-in-situ NC`: Normal concrete cast in place ($f_c = 40.0\ \text{MPa}$, thickness 80 mm).
    2. `Precast UHPC`: Precast UHPC ($f_c = 130.0\ \text{MPa}$, thickness 50 mm, 2% straight steel fibers).
- **Testing program and FE simulation (Sections 2.3–4.5 & Figs. 6–14)**:
  - Four-point bending test under displacement control at 1.0 mm/min.
  - Instrumentation: LVDTs, strain gages, relative slip displacement transducers.
  - ABAQUS: C3D8R 8-node hexahedral elements, Concrete Damaged Plasticity (CDP) model.

## Results

### 1. Initial stiffness, ultimate load, deflection, and interfacial slip across composite beam configurations (Tables 4–6 & Figs. 15–20)

| Specimen ID | Slab material & thickness | Initial stiffness ($K_e$, kN/mm) | First cracking load ($P_{cr}$, kN) | Ultimate flexural load ($P_u$, kN) | Ultimate deflection ($\delta_u$, mm) | Max relative slip ($S_{max}$, mm) | Primary failure mode |
|---|---|---|---|---|---|---|---|
| **Steel-NC (Baseline)** | Cast-in-situ NC (80 mm) | **$12.5 \pm 0.6\ \text{kN/mm}$** | **$75.0 \pm 3.5\ \text{kN}$** | **$265.0 \pm 8.0\ \text{kN}$** | $28.0 \pm 1.2\ \text{mm}$ | **$0.75 \pm 0.05\ \text{mm}$** | Concrete crushing + steel yield |
| **Steel-Precast-UHPC** | **Precast UHPC (50 mm)** | **$22.2 \pm 0.8\ \text{kN/mm}$ (+78 %)** | **$145.0 \pm 6.0\ \text{kN}$ (+93 %)** | **$438.0 \pm 12.0\ \text{kN}$ (+65 %)** | **$42.5 \pm 1.8\ \text{mm}$ (+52 %)** | **$0.14 \pm 0.02\ \text{mm}$ (Minimal)** | **Full plastic yielding of steel** |

### 2. Cross-sectional stress redistribution and bolt shear transfer
- **Cross-sectional slimming and stiffness amplification**: Although the slab was 38 % thinner ($50\ \text{mm}$ vs 80 mm), the high elastic modulus ($48\ \text{GPa}$) and fiber bridging amplified flexural stiffness by 78 %.
- **Full composite action in grouted shear pockets**: High-strength non-shrink grouted shear pockets integrated with bolts transferred 100 % of interface shear without debonding.

- **Overall conclusion**: This work established the flexural mechanics, finite element modeling, and plastic moment design formulations for bolted modular steel–precast UHPC composite beams.

## Related Notes

- [[zhao-2023-steel-uhpc-composite-beams-negative-moment-behavior]] — Negative moment flexural behavior of steel-UHPC composite beams.
- [[tong-2025-steel-uhtcc-composite-decks-wet-joints-flexure]] — Flexural behavior of steel-UHTCC composite decks with wet joints.
- [[high-strength-strain-hardening-composites]] — Assembled composite structural systems.
- [[concrete-durability-and-service-life]] — Accelerated construction and structural durability.
