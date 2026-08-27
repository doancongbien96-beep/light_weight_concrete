---
title: "Microstructure-guided computational model for predicting effective thermal conductivity of cementitious composites filled with phase change particles"
type: source_note
source: "sources/hou-2022-microstructure-guided-computational-model-for-predicting.pdf"
citation: "Hou, F., Zhao, X., Wang, H., & Dong, Q. (2022). Microstructure-guided computational model for predicting effective thermal conductivity of cementitious composites filled with phase change particles. Case Studies in Thermal Engineering, 38, 102339."
date: 2026-08-23
tags: [phase-change-materials, hollow-steel-balls, pcm-hsb, thermal-conductivity-enhancement, finite-element-modeling, effective-medium-theory, energy-storage, hainan-university, theory-foundation]
---

# Microstructure-Based Finite Element Thermal Modeling and 25.8 % Thermal Conductivity Enhancement in Concrete Containing Hollow Steel Ball Encapsulated Paraffin PCM

## Summary

To overcome low thermal conductivity ($0.2\ \text{W/m}\cdot\text{K}$) and mechanical degradation in cementitious composites incorporating organic paraffin phase change materials (PCM), Professor Huizhong Wang and co-workers at Hainan University developed a macro-encapsulation approach enclosing paraffin PCM (melting point $28.0\ ^\circ\text{C}$, latent heat $145.0\ \text{J/g}$) inside high-conductivity hollow carbon steel balls (HSBs: outer diameter $25\ \text{mm}$, shell thickness $1.5\ \text{mm}$, paraffin filling ratio 83.87 vol.%). Replacing mortar matrix with PCM-HSB particles at 0 vol.%, 5.09 vol.%, 10.18 vol.%, and 15.28 vol.%, the authors evaluated effective thermal conductivity (CTC) using transient plane source (Hot Disk TPS) and established a 3D microstructure-based finite element (FE) model alongside effective medium theories (Maxwell, Hamilton-Crosser, Hasselman-Johnson). The high-conductivity steel shell ($k_{steel} = 45.0\ \text{W/m}\cdot\text{K}$) established 3D thermal bridging, **increasing effective thermal conductivity by 25.84 % ($1.180 \rightarrow 1.485\ \text{W/m}\cdot\text{K}$)** at 15.28 vol.% PCM-HSB loading while retaining a 28 d compressive strength of **46.5 MPa** (only a 12.7 % reduction from 53.2 MPa in control mortar).

## Key Contributions

1. **Reversal of PCM thermal degradation via hollow steel ball (HSB) macro-encapsulation**:
   - Encapsulating low-conductivity paraffin ($0.2\ \text{W/m}\cdot\text{K}$) in a 1.5 mm steel shell ($45.0\ \text{W/m}\cdot\text{K}$) raised effective particle thermal conductivity to $3.2\ \text{W/m}\cdot\text{K}$, increasing composite conductivity by 25.84 % over unreinforced mortar.
2. **Microstructure-based 3-phase (Matrix-Shell-Core) finite element heat transfer modeling**:
   - Formulated 3D random particle distribution RVE models, achieving close agreement with experimental data within ±3.5 % relative error.
3. **Simultaneous high latent heat storage ($15.2\ \text{J/g}$) and 46.5 MPa compressive strength**:
   - Prevented the >50 % compressive strength losses common in polymer microcapsule PCMs by utilizing the arch shell bearing capacity of steel spheres.
4. **Hasselman-Johnson effective medium formulation with interfacial thermal resistance ($R_k$)**:
   - Quantified parametric sensitivities of shell-to-radius ratio ($t_s/R_s$) and interfacial contact resistance on overall thermal transport.

## Methods

- **Materials and PCM-HSB fabrication (Table 1–2 & Section 2)**:
  - Matrix: P·O 42.5 cement, standard quartz sand (S/C = 2.0, W/C = 0.40).
  - Hollow steel balls (HSBs): Carbon steel shells ($R_s = 12.5\ \text{mm}$, thickness $t_s = 1.5\ \text{mm}$, density $7.85\ \text{g/cm}^3$, thermal conductivity $45.0\ \text{W/m}\cdot\text{K}$).
  - Phase change material: Organic paraffin (melting point $28.0\ ^\circ\text{C}$, latent heat $145.0\ \text{J/g}$, density $0.88\ \text{g/cm}^3$, thermal conductivity $0.21\ \text{W/m}\cdot\text{K}$).
  - Infill process: Vacuum liquid paraffin injection via a $\phi 5\ \text{mm}$ drill hole followed by sealed plug closure (actual filling ratio $\tilde{\xi}_{PCM} \approx 81.5\%$).
- **Mix matrix (4 configurations)**:
  - M0 (Control): PCM-HSB 0.0 vol.%.
  - M1: PCM-HSB 5.09 vol.% (1 ball per cube).
  - M2: PCM-HSB 10.18 vol.% (2 balls per cube).
  - M3: PCM-HSB 15.28 vol.% (3 balls per cube).
- **Testing program**:
  - Thermal conductivity: Hot Disk TPS 2500S (15 mm Kapton sensor, 1.2 W power, 40 s duration, error within ±3 %).
  - Compressive strength: $70.7\ \text{mm} \times 70.7\ \text{mm} \times 70.7\ \text{mm}$ cubes (28 d curing, 300 kN frame).
  - Computation: ABAQUS 3D non-linear steady-state thermal conduction module.

## Results

### 1. Thermal conductivity and mechanical properties across PCM-HSB volume fractions (Tables 3–5 & Figs. 4–9)

| Mix ID | PCM-HSB Loading (vol.%) | Measured Conductivity ($k_{eff}$, W/mK) | FE Computed Conductivity ($k_{num}$, W/mK) | Thermal Conductivity Gain (%) | 28 d Compressive Strength ($f_{cc}$, MPa) | Strength Loss (%) | Latent Heat Capacity ($\text{J/g}$) |
|---|---|---|---|---|---|---|---|
| **M0 (Control)** | 0.0 % (Control) | 1.180 ± 0.025 | 1.180 | 0.0 % (Control) | 53.2 ± 2.0 | 0.0 % (Control) | 0.0 J/g |
| **M1 (1-HSB)** | 5.09 vol.% | 1.272 ± 0.028 | 1.265 | **+7.80 %** | 50.8 ± 1.8 | −4.5 % | 4.8 ± 0.2 J/g |
| **M2 (2-HSB)** | 10.18 vol.% | 1.375 ± 0.030 | 1.368 | **+16.53 %** | 48.5 ± 1.6 | −8.8 % | 9.8 ± 0.4 J/g |
| **M3 (3-HSB)** | **15.28 vol.%** | **1.485 ± 0.032** | **1.478** | **+25.84 %** | **46.5 ± 1.5** | **−12.7 % (Minor)** | **15.2 ± 0.5 J/g** |

### 2. Thermal conduction and failure mechanisms
- **Heat flux concentration**: The 45 W/mK steel shell absorbs heat flux from the surrounding matrix, channeling thermal energy into the core and across adjacent matrix zones.
- **Failure mode**: High modulus steel spheres force compressive failure cracks to deviate along sphere contours, preventing explosive crushing.

- **Overall conclusion**: This work established a predictive 3D microstructure finite element framework and demonstrated that hollow steel ball encapsulation enhances concrete thermal conductivity by 25.8 % while retaining structural strength for thermal energy storage.

## Related Notes

- [[gan-2025-pcm-energy-piles-thermal-performance]] — PCM hollow steel ball energy pile heat exchange with 29.5 % enhancement.
- [[hao-2022-3d-printed-concrete-recycled-aggregate-pcm]] — Recycled aggregate PCM 3D printed concrete thermal behavior.
- [[sustainability-low-carbon-binders]] — Low-carbon thermal energy storage building materials.
- [[gencel-2022-slag-capric-acid-thermal-mortar]] — Blast furnace slag capric acid thermal energy storage mortar.
