---
title: "3D Printing Quality of Fiber-Reinforced Mortar Using Waste Cactus Powder Admixture (Kim et al., 2025)"
type: source_note
source: "sources/kim-2025-3d-printing-quality-of-fiber-reinforced.pdf"
citation: "Kim, E. B., Kim, M. W., Seo, D. W., & Lee, B. Y. (2025). 3D Printing Quality of Fiber-Reinforced Mortar Using Waste Cactus Powder Admixture. Journal of the Korea Concrete Institute, 37(2), 229-236."
date: 2026-08-24
tags: [3d-concrete-printing, waste-cactus-powder, bio-admixture, methyl-cellulose, nylon-fiber, buildability, extrudability, dimension-error, layer-accuracy, bang-yeon-lee, jkci, theory-foundation]
---

# Quantitative Evaluation of Extrusion Continuity, Dimensional Error, and Layering Accuracy ($a_{th} = 0.95$) in 3D Printing Mortars Using Eco-Friendly Waste Cactus Stem Powder (CS) Bio-Viscosity Modifier and Nylon Fibers

## Summary

To enhance the plastic viscosity and thixotropy of 3D printable cementitious composites while reducing the dosage of expensive synthetic viscosity modifying admixtures (methyl cellulose: MC) through recycling natural bio-resources, Prof. Bang Yeon Lee (corresponding author) and his research group at Chonnam National University utilized **waste cactus stem powder (CS, rich in gelatinous mucilage polysaccharides and lignin)** from Jeju Island as an eco-friendly bio-admixture. Incorporating nylon fibers ($V_f = 0.5\sim 1.5\ \text{vol.}\%$), the authors systematically evaluated **Brookfield rotational viscosity, flow table spread ($150\sim 190\ \text{mm}$ target range), extrusion continuity in gantry 3D printing (material extrusion ME, nozzle $\phi 10\ \text{mm}$), surface void count, dimensional error ($P_e$) of cylindrical specimens ($\phi 100\ \text{mm} \times 60\ \text{mm}$), and digital image binarization-based layering accuracy ($a_{th} = 1 - |\frac{x_{target}-\bar{x}}{x_{target}}|$)**. Results showed that the **M18-SP0.5 mixture**, combining 0.02 wt.% CS powder and 0.18 wt.% MC with 0.5 vol.% nylon fibers, achieved optimal plastic viscosity and workability ($168\ \text{mm}$ flow), delivering superior build quality with **dimensional error $P_e = 2.15\%$ (measured diameter 102.15 mm vs 100 mm target, height 59.8 mm vs 60 mm target) and layering accuracy $a_{th} = 0.948$ (out of 1.0)**. Conversely, increasing fiber volume fraction to 1.5 vol.% caused nozzle clogging ($\phi 10\ \text{mm}$) via fiber mechanical interlocking, delineating the critical fiber threshold.

## Key Contributions

1. **First development of eco-friendly bio-admixtures for 3D concrete printing using waste cactus stem powder (CS)**:
   - Utilized natural cactus polysaccharides to reduce synthetic MC usage by over 10 % while maintaining excellent buildability.
2. **Formulation of pixel-binarization-based 3D printing layering accuracy metric ($a_{th} = 0.948$)**:
   - Proposed a standardized evaluation protocol quantifying X-axis and Z-axis printing profile errors at $0.01$ index resolution.
3. **Identification of critical nylon fiber threshold ($V_f \le 1.0\ \text{vol.}\%$) for $\phi 10\ \text{mm}$ nozzle extrusion**:
   - Clarified the mechanical interlocking clogging mechanism when $V_f = 1.5\%$, defining the optimal balance between fiber reinforcement and extrusion continuity.
4. **Demonstration of high-precision hollow cylindrical 3D structures ($\phi 100\ \text{mm} \times 60\ \text{mm}$, 10 layers) with $2.15\%$ dimensional error**:
   - Achieved 10-layer vertical buildability without self-weight settlement or slump collapse.

## Methods

- **Materials and mixture proportions (Tables 1–5, mass ratios)**:
  - Binder: Type I Ordinary Portland Cement (OPC, Blaine fineness $3350\ \text{cm}^2/\text{g}$).
  - Fine aggregate: Silica sand No. 6 ($d_{50} = 220\ \mu\text{m}$, Sand/Binder = 1.0).
  - Bio-admixture: Dried and pulverized waste cactus stem powder (CS, $d \le 150\ \mu\text{m}$).
  - Synthetic modifier: Methyl cellulose (MC, viscosity 40,000 cPs).
  - Reinforcing fibers: Short nylon fibers (diameter $14\ \mu\text{m}$, length 6 mm, tensile strength 900 MPa, modulus 4.5 GPa, $V_f = 0.5, 1.0, 1.5\ \text{vol.}\%$).
  - Mixing water and admixture: W/B = 0.38, polycarboxylate ether superplasticizer (SP).
- **3D printing apparatus and testing protocols (Sections 2.2–2.3 & Figs. 1–3)**:
  - 3D printer: Gantry material extrusion printer (build volume $500\ \text{mm} \times 500\ \text{mm} \times 500\ \text{mm}$, screw nozzle $\phi 10\ \text{mm}$, printing speed $25\ \text{mm/s}$).
  - Test structure: Hollow cylinder (outer diameter 100 mm, height 60 mm, 10 layers, 6.0 mm layer height).
  - Rheology: Brookfield DV-II viscometer (Spindle HB-6, 100 rpm) and KS F 2476 flow test (25 drops in 15 s).
  - Quality metrics: Dimensional error $P_e = (\frac{m_p}{m_m}-1)\times 100$, layering accuracy $a_{th} = 1 - |\frac{x_{target}-\bar{x}}{x_{target}}|$, surface void count across $120^\circ$ quadrant.

## Results

### 1. Rheological properties, 3D printing extrudability, dimensional error, and layering accuracy (Tables 7–9 & Figs. 4–9)

| Mix ID | MC / CS Ratio (wt.%) | Nylon Fiber ($V_f$, %) | Viscosity ($\text{Pa}\cdot\text{s}$) | Flow (mm) | Extrusion Continuity | Dimensional Error ($P_e$, %) | Layering Accuracy ($a_{th}$) | Surface Void Count |
|---|---|---|---|---|---|---|---|---|
| **M0 (No modifier)** | 0.00 / 0.00 | 0.5 % | 12.5 ± 0.5 | 225 ± 5 | Discontinuous (Slump collapse) | +12.5 ± 1.2 % | 0.725 ± 0.02 | 45 ± 4 (Excessive) |
| **M20 (MC only)** | 0.20 / 0.00 | 0.5 % | 28.5 ± 1.0 | 155 ± 4 | Continuous extrusion | +3.80 ± 0.4 % | 0.912 ± 0.01 | 18 ± 2 |
| **M18-SP0.5 (Optimal)** | **0.18 / 0.02** | **0.5 %** | **26.4 ± 0.8** | **168 ± 4 (Optimal)** | **Complete continuous build** | **+2.15 ± 0.3 % (Lowest)** | **0.948 ± 0.01 (Highest)** | **12 ± 2 (Minimum)** |
| **M18-SP1.0** | 0.18 / 0.02 | 1.0 % | 31.2 ± 1.2 | 164 ± 4 | Continuous build | +2.85 ± 0.3 % | 0.935 ± 0.01 | 15 ± 2 |
| **M18-SP1.5** | 0.18 / 0.02 | 1.5 % | 42.5 ± 1.5 | 159 ± 4 | **No extrusion (Nozzle clogging)** | Unmeasurable | Unmeasurable | Unmeasurable |

### 2. Bio-polysaccharide thickening mechanisms and fiber hydrodynamics
- **Viscoelastic network formation via waste cactus powder**: Natural gelatin and lignin in CS bind free water and bridge cement particles to induce shear thinning behavior, ensuring low viscosity during nozzle extrusion while rapidly recovering static yield stress upon deposition.
- **Fiber volume fraction fluid mechanics**: For $V_f = 0.5\sim 1.0\%$, nylon fibers align along the extrusion streamline, providing crack resistance; at $1.5\%$, fiber bridging at the nozzle constriction causes steep pressure buildup and blockage.

- **Overall conclusion**: This landmark paper demonstrated that eco-friendly waste cactus stem powder (CS) successfully substitutes synthetic viscosity agents in 3D concrete printing, achieving minimal dimensional error (2.15 %) and superior layering accuracy ($a_{th}=0.948$).

## Related Notes

- [[hyun-2025-3d-printable-aas-shcc-recycled-selvage-fiber]] — 3D printable cementless alkali-activated composites reinforced with recycled fibers.
- [[khoshnevis-2017-isru-robotic-construction-lunar-mars]] — Contour Crafting automated 3D printing construction for lunar and Martian infrastructure.
- [[choi-2015-rheological-mechanical-fr-aac]] — Rheological and extrusion flow control in autoclaved aerated composites.
- [[sustainability-low-carbon-binders]] — Eco-friendly bio-admixtures and sustainable building material systems.
