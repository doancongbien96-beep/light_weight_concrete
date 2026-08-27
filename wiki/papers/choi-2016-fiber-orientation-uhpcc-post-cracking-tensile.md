---
title: "Predicting Post-Cracking Tensile Behavior of UHPCC by Fiber Orientation (Choi et al., 2016)"
type: source_note
source: "sources/Choi 등 - 2016 - Improvement in Predicting the Post-Cracking Tensile Behavior of Ultra-High Performance Cementitious.pdf"
citation: "Choi, J. I., Koh, K. T., Ryu, G. S., & Lee, B. Y. (2016). Improvement in predicting the post-cracking tensile behavior of ultra-high performance cementitious composites by considering fiber orientation. Materials, 9(10), 829. https://doi.org/10.3390/ma9100829"
date: 2026-08-24
tags:
  - uhpcc
  - fiber-orientation-coefficient
  - post-cracking-tensile
  - steel-fiber
  - micromechanical-model
  - image-processing
---

## Summary
This 2016 Materials paper by the joint team of the Korea Institute of Civil Engineering and Building Technology and Chonnam National University (Dr. Jeong-il Choi and Prof. Bang Yeon Lee) precisely characterized the fiber orientation distribution and post-cracking direct tensile behavior of UHPCC (micro straight steel fibers at $V_f$ = 2.0 vol %, diameter 0.2 mm, hybrid of 16.3 mm and 19.5 mm lengths) according to the casting method (Method A: central casting with random orientation vs Method B: longitudinally flow-induced alignment), using cross-sectional digital image processing and a single-fiber pull-out bridging analytical model. Under flow-aligned casting (Method B), the effective fiber count per unit area (= 0.468 EA/mm²) and the orientation coefficients ($\eta_\theta$ = 0.531, $\alpha_f$ = 0.715) doubled compared with random casting Method A (= 0.227 EA/mm², $\eta_\theta$ = 0.447, $\alpha_f$ = 0.645), demonstrating that the ultimate tensile strength increased dramatically **by 1.97× (96.6 %), from 7.59 MPa to 14.92 MPa**.

## Key Contributions
- **Quantification of the three-dimensional fiber orientation distribution in UHPCC by casting method (Method A vs Method B)**: precise detection of the fiber counts (910 vs 1872) and orientation-angle distributions through cross-sectional optical scanning image processing.
- **Clarification of the effect of fiber orientation on first-cracking strength and ultimate tensile strength**: first-cracking strength increased slightly, from 6.68 MPa to 7.55 MPa, whereas the ultimate tensile strength surged twofold, from 7.59 MPa to 14.92 MPa.
- **Completion of the parameter set of the Lee et al. single-fiber pull-out bridging model**: applying $E_m$ = 45 GPa, $E_f$ = 200 GPa, $\tau_{max}$ = 6.8 MPa, f = 1.6, κ = 1.8.
- **Establishment of tensile design guidance for full-scale UHPCC structures considering member geometry and casting flow**: standardization of construction practice to minimize the scatter in tensile performance caused by casting directionality.

## Methods
- UHPCC unit mix (kg/m³): cement 771, silica fume 193, silica sand 848, filler (> 98 % $SiO_2$, 4 µm) 231, high-range water reducer (WRA) 46.3, water 160 ($W/B$ = 0.20), steel fiber 156 ($V_f$ = 2.0 vol %).
- Steel fiber specification: diameter 0.2 mm, length 16.3 mm (1.0 %) + length 19.5 mm (1.0 %), tensile strength 2500 MPa, density 7.5 g/cm³.
- Casting methods:
  - **Method A**: central casting of the specimen (inducing random three-dimensional orientation)
  - **Method B**: end casting of the specimen (inducing one-dimensional flow alignment along the specimen length)
- Tests: dogbone-type direct tensile test (0.2 mm/min, CMOD clip gauge) and high-resolution digital image analysis of cut cross-sections.

## Results
- Comparative data from UHPCC direct tensile tests and cross-sectional fiber image analysis by casting method (Table 2, Table 3, Table 4, Table 6):

| Measurement item | Method A (central random casting) | Method B (flow-aligned casting) | Performance change (B vs A) |
| :--- | :---: | :---: | :---: |
| **First cracking strength (MPa)** | 6.68 ± 1.07 | **7.55 ± 1.48** | +13.0 % |
| **CMOD at first cracking (mm)** | 0.007 ± 0.001 | 0.007 ± 0.001 | Identical |
| **Ultimate tensile strength (MPa)** | **7.59 ± 0.217** | **14.92 ± 0.297** | **+96.6 % (1.97×)** |
| **CMOD at ultimate (mm)** | 0.157 ± 0.130 | **0.369 ± 0.247** | **+135.0 % (2.35×)** |
| **Total detected fiber count** | 910 ± 84 | **1872 ± 48** | **+105.7 % (2.06×)** |
| **Fiber count per unit area (EA/mm²)** | 0.227 ± 0.021 | **0.468 ± 0.040** | **+106.2 % (2.06×)** |
| **Fiber orientation coefficient $\eta_\theta$** | 0.447 | **0.531** | +18.8 % |
| **Orientation coefficient $\alpha_f$** | 0.645 | **0.715** | +10.9 % |

## Related Notes
- [[choi-2015-tensile-behavior-uhpc-fiber-combinations]] — Tensile behavior of UHPC by fiber combination
- [[fiber-orientation-distribution]] — Theory of fiber orientation distribution
- [[zerbino-2012-fiber-orientation-self-compacting-frc]] — Fiber orientation in self-compacting FRC
