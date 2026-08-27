---
title: "Development of a structural model with dynamic thermal conductivity for composite phase change materials: Numerical and experimental investigations"
type: source_note
source: "sources/hou-2025-development-of-a-structural-model.pdf"
citation: "Hou, F., Li, L., Cai, X., Wang, H., Gong, N., Zhu, Y., & Wang, H. (2025). Development of a structural model with dynamic thermal conductivity for composite phase change materials: Numerical and experimental investigations. Case Studies in Thermal Engineering, 72, 106348."
date: 2026-08-23
tags: [composite-phase-change-materials, cpcm, dynamic-thermal-conductivity, natural-convection, spherical-macrocapsules, spcm, hard-core-algorithm, building-thermal-regulation, theory-foundation]
---

# 3D Microstructure Thermal Model with Dynamic Thermal Conductivity Coupling Liquid Natural Convection for Spherical Macro-Encapsulated Phase Change Materials (SPCM)

## Summary

To overcome calculation errors in traditional static thermal conductivity models that neglect buoyancy-driven natural convection within melting liquid paraffin, a joint research team from Jiangsu Ocean University, Tongji University, and Hainan University developed a **3D heat transfer structural model with dynamic effective thermal conductivity ($k_{eff}(T)$)**. The model couples the 3D spatial distribution of spherical macrocapsules (SPCMs: outer diameter $15.63\ \text{mm}$, carbon steel shell thickness $0.445\ \text{mm}$, paraffin core) generated via a Hard-Core algorithm with a temperature-dependent natural convection enhancement factor ($Nu$). Validated against heating-cooling experiments on cement mortar cubes ($70.7\ \text{mm}$) and DSC thermal analysis, the dynamic model accelerated computational speeds 100-fold compared to direct Navier-Stokes solvers while tracking experimental temperature histories within **2.8 % relative error (RMSE $\le 0.42\ ^\circ\text{C}$)**. Incorporating 20 vol.% SPCM into cement panels dampened peak indoor temperature by **$5.8\ ^\circ\text{C}$** and introduced a **3.5 h time lag** under cyclic solar heating.

## Key Contributions

1. **Multi-scale model coupling liquid-state natural convection into dynamic effective thermal conductivity ($k_{eff}(T)$)**:
   - Converted buoyancy convection ($Nu > 1.0$) during solid-to-liquid transition into an equivalent dynamic thermal conductivity function, enabling rapid and accurate phase change simulation without direct Navier-Stokes solving.
2. **Hard-Core spatial repulsion algorithm for 3D random SPCM packing**:
   - Replicated the actual 3D spatial dispersion of spherical capsules inside cement cubes with 100 % fidelity using exclusion distances ($2R_s$) and clustering prevention thresholds ($l_{max} = 3\sim 10 R_s$).
3. **Quantification of thermal bridging and mechanical confinement by thin metal shells ($t_s = 0.445\ \text{mm}$)**:
   - Demonstrated that the steel shell bypassed the paraffin thermal conduction bottleneck while absorbing phase change expansion stresses to prevent matrix cracking.
4. **Thermal load reduction in building envelopes ($5.8\ ^\circ\text{C}$ damping, 3.5 h time lag)**:
   - Attenuated peak heat flux entering the building interior, providing design guidelines to reduce air-conditioning cooling energy by over 35 %.

## Methods

- **Dynamic effective thermal conductivity formulation (Section 4.1, Eqs. 3–7)**:
  1. Enhanced liquid paraffin thermal conductivity:
     $$k_l^* = Nu \cdot k_l$$
     - $Nu = C \cdot Ra^n$ ($Ra = \frac{g \beta (T - T_m) L^3}{\nu \alpha}$: Rayleigh number).
  2. Phase-transition dynamic thermal conductivity:
     $$k_{PCM}(T) = k_s + f_l(T) \cdot (k_l^* - k_s)$$
     - $f_l(T)$: Liquid fraction ($0.0 \sim 1.0$ derived from DSC enthalpy curve).
- **Materials and SPCM specifications (Section 2 & Figs. 3–6)**:
  - Mortar matrix: P·O 42.5 cement, W/C = 0.40, S/C = 2.0.
  - SPCM capsule: Hollow steel sphere ($R_s = 7.816\ \text{mm}$, outer diameter $15.63\ \text{mm}$, shell thickness $t_s = 0.445\ \text{mm}$, steel density $7850\ \text{kg/m}^3$, thermal conductivity $45\ \text{W/m}\cdot\text{K}$).
  - Paraffin core: Melting point $28.0\ ^\circ\text{C}$, latent heat $145.0\ \text{J/g}$, solid density $880\ \text{kg/m}^3$.
  - Specimen: $70.7\ \text{mm} \times 70.7\ \text{mm} \times 70.7\ \text{mm}$ cubes with central Type-K thermocouples.
- **Testing and computation**:
  - Environmental chamber thermal cycling ($10\ ^\circ\text{C} \leftrightarrow 50\ ^\circ\text{C}$ at $0.5\ ^\circ\text{C/min}$).
  - DSC analysis: TA Instruments Q20 ($5\ ^\circ\text{C/min}$, -10~60 °C).
  - Finite element computation: COMSOL Multiphysics non-linear transient heat transfer module.

## Results

### 1. Experimental heating-cooling performance vs dynamic model simulation across SPCM loadings (Tables 1–3 & Figs. 7–12)

| Specimen Group | SPCM Fraction ($f_P$, vol.%) | Experimental Peak Time ($t_{peak}$, h) | Experimental Peak Temp ($T_{max}$, °C) | Dynamic Model Error (RMSE) | Peak Time Lag ($\Delta t$) | Peak Temperature Damping ($\Delta T$) |
|---|---|---|---|---|---|---|
| **Control (Pure Mortar)** | 0.0 % (Control) | 2.10 ± 0.05 h | 44.5 ± 0.3 °C | 0.25 °C | 0.0 h (Baseline) | 0.0 °C (Baseline) |
| **CPCM-1 (5% SPCM)** | 5.20 vol.% | 2.85 ± 0.08 h | 42.2 ± 0.3 °C | 0.32 °C | +0.75 h | −2.3 °C |
| **CPCM-2 (10% SPCM)** | 10.50 vol.% | 3.90 ± 0.10 h | 40.5 ± 0.4 °C | 0.38 °C | +1.80 h | −4.0 °C |
| **CPCM-3 (20% SPCM)** | **20.80 vol.%** | **5.60 ± 0.12 h** | **38.7 ± 0.4 °C** | **0.42 °C (within 2.8 %)** | **+3.50 h (Lag)** | **−5.8 °C (Damping)** |

### 2. Physical heat transfer mechanisms and model accuracy
- **Necessity of natural convection coupling**: Static conduction models underestimated heat transfer in liquid paraffin, over-predicting phase change completion times by 22 %; the proposed dynamic model achieved >98 % agreement with experimental curves.
- **Multiscale synergy**: Mesoscale capsule heat exchange combined with macroscopic panel thermal storage to maximize building load attenuation.

- **Overall conclusion**: This study developed a predictive 3D structural model incorporating liquid natural convection and dynamic thermal conductivity for macro-encapsulated phase change concrete composites.

## Related Notes

- [[hou-2022-microstructure-model-pcm-steel-ball-concrete]] — Microstructure effective thermal conductivity model of PCM hollow steel balls.
- [[gan-2025-pcm-energy-piles-thermal-performance]] — Thermal performance of PCM hollow steel ball energy piles.
- [[hao-2022-3d-printed-concrete-recycled-aggregate-pcm]] — Recycled aggregate PCM 3D printed concrete thermal conductivity.
- [[sustainability-low-carbon-binders]] — Low-carbon energy storage construction materials.
