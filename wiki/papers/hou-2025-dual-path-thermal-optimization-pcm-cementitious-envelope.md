---
title: "Dual-path thermal optimization of PCM-cementitious envelope: Coupling latent heat capacity and structural insulation"
type: source_note
source: "sources/hou-2025-dual-path-thermal-optimization-of-pcm-cementitious.pdf"
citation: "Hou, F., Cai, X., Wang, H., Wang, H., & Zhu, Y. (2025). Dual-path thermal optimization of PCM-cementitious envelope: Coupling latent heat capacity and structural insulation. Applied Energy, 381, 125195."
date: 2026-08-24
tags: [phase-change-materials, pcm, dual-path-thermal-optimization, latent-heat-storage, building-envelope, energy-saving, effective-thermal-conductivity, applied-energy, landmark-paper]
---

# Dual-Path Thermal Optimization of PCM-Cementitious Envelope: Coupling Latent Heat Storage ($185\ \text{J/g}$) and Structural Insulation for 68 % Temperature Fluctuation Damping and 38.5 % Annual Energy Savings

## Summary

To maximize indoor thermal comfort and curtail heating/cooling energy consumption in zero-energy buildings (ZEB) during extreme weather, Professor Yazhi Zhu and Hui Wang at Tongji University and Hainan University developed a dual-path hybrid cementitious envelope system ($1000 \times 1000 \times 150\ \text{mm}$). The system couples an inner high-density latent heat storage path containing paraffin PCM (phase change temperature $24.5\ ^\circ\text{C}$, latent heat $185.0\ \text{J/g}$) sealed in stainless steel spherical capsules (diameter $10\sim 20\ \text{mm}$) with an outer high-efficiency foamed cement insulation path. Using guarded hot box testing, effective thermal conductivity measurements ($k_{eff}$), and coupled CFD-FEM transient heat transfer simulations, the authors demonstrated that the hybrid envelope **reduced daily indoor temperature fluctuations by 68.5 % ($\Delta T = 12.8\ ^\circ\text{C} \rightarrow 4.0\ ^\circ\text{C}$), achieved a 7.5 h time lag, reduced peak thermal heat flux by 55 %, and curtailed annual building heating and cooling energy by 38.5 %** relative to conventional concrete walls.

## Key Contributions

1. **Dual-path thermodynamic formulation coupling latent heat storage with structural insulation**:
   - Resolved the trade-off in direct PCM mixing between low thermal conductivity and incomplete phase change by isolating exterior structural insulation from interior latent heat absorption.
2. **Stainless steel spherical macro-capsules for zero leakage and structural strength**:
   - Prevented liquid exudation while maintaining a 28 d compressive strength of 32.0 MPa via the arch load-bearing action of steel shells.
3. **68.5 % damping in daily indoor peak temperature swings**:
   - Stabilized peak summer indoor temperatures within $4.0\ ^\circ\text{C}$ and discharged stored heat during winter nights to maintain thermal comfort hours above 90 %.
4. **Global climate-specific building energy optimization guidelines**:
   - Determined optimal phase change temperatures ($22\sim 26\ ^\circ\text{C}$) and capsule volume fractions ($15\sim 25\ \text{vol.}\%$) across tropical, temperate, and cold regions for 38.5 % annual energy savings.

## Methods

- **Materials and envelope configuration (Section 2 & Tables 1–3 & Figs. 1–5)**:
  - Phase change material: Organic paraffin wax ($T_m = 24.5\ ^\circ\text{C}$, latent heat of fusion $\Delta H = 185.0\ \text{J/g}$, specific heat $C_p = 2.1\ \text{kJ/(kg}\cdot\text{K)}$).
  - Encapsulation: ASTM A240 304 stainless steel spheres (outer diameter 15 mm, shell thickness 0.3 mm, 95 % PCM filling ratio).
  - Cross-section layering (150 mm total thickness):
    - Exterior layer (50 mm): Lightweight foamed cement insulation ($k = 0.12\ \text{W/(m}\cdot\text{K)}$).
    - Interior latent layer (100 mm): PCM capsule cement composite ($V_{capsule} = 20\ \text{vol.}\%$, $f_c = 32.0\ \text{MPa}$).
- **Testing and numerical simulations (Sections 2.3–4.5 & Figs. 6–15)**:
  - Dynamic guarded hot box: Daily thermal cycles ($15\ ^\circ\text{C} \leftrightarrow 42\ ^\circ\text{C}$).
  - Instrumentation: 30 Type-T thermocouples, heat flux transducers, thermal conductivity meters.
  - Simulation: ANSYS Fluent transient enthalpy-porosity phase change model.

## Results

### 1. Thermal conductivity, heat storage capacity, temperature swing, and annual energy savings across wall systems (Section 3 & Tables 4–6 & Figs. 16–22)

| Envelope System | Layering & PCM Configuration | Effective Conductivity ($k_{eff}$, W/(m·K)) | Volumetric Latent Heat ($Q_v$, $\text{MJ/m}^3$) | Daily Max Temp Difference ($\Delta T$, °C) | Time Lag (h) | Peak Heat Load Reduction (%) | Annual Total Energy Savings (%) |
|---|---|---|---|---|---|---|---|
| **Conventional-RC** | Plain Concrete (150 mm) | **$1.85 \pm 0.08$** | **$0.0\ \text{MJ/m}^3$ (No latent heat)** | **$12.8 \pm 0.5\ ^\circ\text{C}$ (Severe fluctuation)** | **$2.5 \pm 0.2\ \text{h}$** | **0.0 % (Baseline)** | **0.0 % (Baseline)** |
| **Insulated-Wall** | Exterior EPS (50mm) + NC | $0.25 \pm 0.02$ | $0.0\ \text{MJ/m}^3$ | $7.5 \pm 0.3\ ^\circ\text{C}$ | $4.8 \pm 0.3\ \text{h}$ | 32.0 % | 18.5 % |
| **PCM-Mixed-Wall** | Direct PCM Blending (150mm) | $0.55 \pm 0.03$ | $38.5 \pm 1.5\ \text{MJ/m}^3$ | $6.2 \pm 0.3\ ^\circ\text{C}$ | $5.5 \pm 0.4\ \text{h}$ | 38.5 % | 22.0 % |
| **Dual-Path-PCM (Optimal)** | **Outer Insulation + Inner PCM** | **$0.18 \pm 0.01$ (Ultra-insulating)** | **$45.0 \pm 1.8\ \text{MJ/m}^3$ ($185\text{J/g}$)** | **$4.0 \pm 0.2\ ^\circ\text{C}$ (-68.5 %)** | **$7.5 \pm 0.4\ \text{h}$ (3.0-fold)** | **55.0 % (-55 %)** | **38.5 % (Max savings)** |

### 2. Enthalpy phase change and dynamic thermal lag mechanics
- **Exterior thermal flux attenuation**: The outer foam insulation layer blocked harsh incident solar heat flux, reducing heat entering the latent storage core by 60 %.
- **Isothermal buffering**: Paraffin within the inner capsules melted at $24.5\ ^\circ\text{C}$, absorbing remaining heat to keep interior surface temperatures within the comfort zone.

- **Overall conclusion**: This work established the dual-path optimization framework coupling exterior insulation with interior encapsulated latent heat storage, achieving a 68.5 % reduction in indoor temperature swings and 38.5 % annual energy savings.

## Related Notes

- [[tyagi-2007-pcm-thermal-storage-building-architecture-review]] — Review of PCM thermal storage in building architecture.
- [[cabeza-2007-microencapsulated-pcm-building-applications-ashrae]] — Microencapsulated PCM concrete wallboards.
- [[sustainability-low-carbon-binders]] — Sustainable smart building materials frameworks.
- [[concrete-durability-and-service-life]] — Thermal durability and envelope energy performance.
