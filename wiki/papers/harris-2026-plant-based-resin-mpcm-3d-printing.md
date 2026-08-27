---
title: "A plant-based resin composite containing microencapsulated phase change material for thermal management"
type: source_note
source: "sources/harris-2026-a-plant-based-resin-composite-containing.pdf"
citation: "Harris, I., MacNeill, O., De Obaldia, E., & Yagoobi, J. (2026). A plant-based resin composite containing microencapsulated phase change material for thermal management. Thermal Science and Engineering Progress, 103210."
date: 2026-08-23
tags: [plant-based-resin, bio-composites, microencapsulated-pcm, mpcm-28, lcd-3d-printing, thermal-management, latent-heat-storage, finite-element-analysis, theory-foundation]
---

# LCD 3D Printing Fabrication and Thermal Management Behavior of Plant-Based Soybean Resin (PBR) Composites Containing Microencapsulated Phase Change Material (MPCM)

## Summary

To reduce carbon emissions and develop sustainable bio-based smart building envelopes and electronics thermal management solutions, Professor Jamal Yagoobi and co-workers at Worcester Polytechnic Institute (WPI) and Universidad Tecnológica de Panamá (UTP) developed a photocurable plant-based resin (PBR) derived from soybean oil reinforced with microencapsulated paraffin phase change material (MPCM-28, peak melting temperature $28.0\ ^\circ\text{C}$, latent heat of fusion $180.5\ \text{J/g}$) at 20 vol.%, 33 vol.%, and 50 vol.% loadings using commercial vat photopolymerization (LCD 3D printing). The authors evaluated tensile strength, bulk density, thermal conductivity ($k$), specific heat capacity ($c_p$), DSC/TGA thermal stability, and transient heat flux thermal regulation through finite element analysis (FEA) and experimental testing. The 50 vol.% MPCM formulation achieved uniform dispersion without impeding photopolymerization, providing a high latent heat storage capacity of **$65.8\ \text{J/g}$**. Incorporating 50 vol.% MPCM decreased thermal conductivity by **33.3 % ($0.21 \rightarrow 0.14\ \text{W/m}\cdot\text{K}$)**, increased effective specific heat by **55.2 % ($1.45 \rightarrow 2.25\ \text{J/g}\cdot\text{K}$)**, slowed the surface temperature rise rate by 48 % under thermal flux, and reduced peak temperature by **$4.8\ ^\circ\text{C}$**.

## Key Contributions

1. **Vat photopolymerization 3D printing of bio-resin with high MPCM loading (50 vol.%)**:
   - Replaced petroleum-based synthetic resins with soybean-oil-derived resins, optimizing UV (405 nm) exposure times ($3.5\sim 5.0\ \text{s}$) to overcome particle light scattering and print high-precision 3D thermal regulation structures.
2. **Concurrent enhancement of insulation and latent heat storage ($k = 0.14\ \text{W/m}\cdot\text{K}, \Delta H_m = 65.8\ \text{J/g}$)**:
   - Hollow microcapsule morphology reduced thermal conductivity by 33 % to block external heat penetration while absorbing substantial latent heat at $28\ ^\circ\text{C}$ to maintain isothermal stability.
3. **Thermo-mechanical characterization and non-linear FEA validation**:
   - Simulated moving phase change boundaries (Stefan problem) during heating-cooling cycles via 3D finite element analysis within 4.2 % relative error against experimental data.

## Methods

- **Materials and formulation design (Tables 1–2 & Figures 1–2)**:
  - Matrix: Anycubic Plant-based UV Resin (soybean-derived acrylate monomers/oligomers, density $1.08\ \text{g/cm}^3$).
  - PCM: Microencapsulated paraffin (MPCM-28, melamine-formaldehyde shell, average diameter $15\sim 20\ \mu\text{m}$, phase change temperature $28.0\ ^\circ\text{C}$, latent heat $180.5\ \text{J/g}$).
  - Mix matrix (4 formulations):
    1. PBR-0 (Pure plant-based resin control).
    2. PBR-MPCM20 (MPCM 20 vol.%, 17.5 wt.%).
    3. PBR-MPCM33 (MPCM 33 vol.%, 29.8 wt.%).
    4. PBR-MPCM50 (MPCM 50 vol.%, 46.2 wt.%).
- **LCD 3D printing and specimen fabrication**:
  - Printer: Anycubic Photon Mono X 6K (405 nm UV wavelength, layer thickness $50\ \mu\text{m}$, exposure time 4.5 s).
  - Specimens: Cylindrical blocks ($\phi 30\ \text{mm} \times 15\ \text{mm}$) for thermal properties, ASTM D638 Type IV tensile dogbones, and flat plates ($100\ \text{mm} \times 100\ \text{mm} \times 5\ \text{mm}$) for thermal management tests.
- **Testing methods**:
  - Thermal properties: Thermtest MP-V (transient plane source TPS measuring thermal conductivity and thermal diffusivity).
  - Thermal analysis: DSC (Netzsch 214 Polyma, $5\ ^\circ\text{C/min}$), TGA (Q50, $25\sim 600\ ^\circ\text{C}$ under $\text{N}_2$).
  - Tensile testing: Instron 5969 universal testing machine (50 kN load cell, crosshead speed $5\ \text{mm/min}$).
  - Transient thermal testing: 100 W flexible silicone heater, 4-channel Type-K thermocouples, and FLIR infrared camera.

## Results

### 1. Physical, mechanical, and thermal properties of bio-composites across MPCM contents (Tables 3–5 & Figs. 3–7)

| Mix ID | MPCM content (vol.%) | Bulk density ($\text{g/cm}^3$) | Tensile strength ($\sigma_t$, MPa) | Elongation at break ($\varepsilon_f$, %) | Thermal conductivity ($k$, W/mK) | Specific heat capacity ($c_p$, J/gK) | Latent heat of fusion ($\Delta H_m$, J/g) |
|---|---|---|---|---|---|---|---|
| **PBR-0 (Control)** | 0.0 % (Control) | 1.08 ± 0.01 | 32.5 ± 1.5 | 8.5 ± 0.5 % | 0.21 ± 0.01 | 1.45 ± 0.05 | 0.0 J/g (No latent heat) |
| **PBR-MPCM20** | 20.0 vol.% | 1.02 ± 0.01 | 22.4 ± 1.2 | 6.2 ± 0.4 % | 0.18 ± 0.01 | 1.72 ± 0.06 | 28.5 ± 1.2 J/g |
| **PBR-MPCM33** | 33.0 vol.% | 0.98 ± 0.01 | 15.8 ± 1.0 | 4.8 ± 0.3 % | 0.16 ± 0.01 | 1.95 ± 0.07 | 45.2 ± 1.8 J/g |
| **PBR-MPCM50** | **50.0 vol.%** | **0.92 ± 0.01** | **10.5 ± 0.8** | **3.2 ± 0.2 %** | **0.14 ± 0.01 (−33 %)** | **2.25 ± 0.08 (+55 %)** | **65.8 ± 2.2 J/g** |

### 2. Thermal management and sustainability analysis
- **Thermal buffering mechanism**: Under a $1000\ \text{W/m}^2$ heat flux, the MPCM50 panel established an isothermal plateau across $27\sim 30\ ^\circ\text{C}$ for 12 min, maintaining back-face temperatures $4.8\ ^\circ\text{C}$ lower than unreinforced controls.
- **Environmental benefits**: Substituting petroleum-based polymers with soybean-derived bio-resins reduced the material carbon footprint by 45 %.

- **Overall conclusion**: This study developed 3D-printable plant-based resin composites combining lightweight density (0.92 g/cm³), low thermal conductivity (0.14 W/mK), and high latent heat storage (65.8 J/g) for smart bio-based thermal management.

## Related Notes

- [[gu-2022-halloysite-pcm-cement-panel-thermal]] — Halloysite-PEG phase change cement panels for thermal regulation.
- [[desai-2014-thermally-adaptive-pcm-ecc]] — Microencapsulated paraffin PCM incorporated thermally adaptive ECC.
- [[sustainability-low-carbon-binders]] — Sustainable bio-based and low-carbon composite materials frameworks.
- [[gencel-2022-attapulgite-pcm-foam-concrete]] — Nanoclay eutectic PCM thermal foam concrete.
