---
title: "Tensile Deformation Characteristics of ECC Predicted with a Modified Fiber Bridging Curve"
type: source_note
source: "sources/Kim 등 - 2009 - Tensile Deformation Characteristics of ECC Predicted with a Modified Fiber Bridging Curve.pdf"
citation: "Kim, Y. Y., Lee, B. Y., & Kim, J. K. (2009). Tensile Deformation Characteristics of ECC Predicted with a Modified Fiber Bridging Curve. Journal of the Korea Concrete Institute, 21(5), 541-548."

date: 2026-08-24
tags: [ecc, fiber-bridging-curve, modified-micromechanics, plug-pullout, critical-fiber-spacing, image-processing, diana-fea, bang-yeon-lee, jkci, theory-foundation]
---

# Uniaxial Tensile Deformation Model for ECC Predicted with a Modified Fiber Bridging Curve Incorporating Critical Fiber Spacing ($s_{cr}$) for Plug Pull-out and Image Processing

## Summary

To overcome the long-standing analytical limitation where classical micromechanical bridging theory ($\sigma$-$\delta$ relations) overestimates uniaxial tensile strain capacity ($\varepsilon_{tu}$) and saturated crack spacing ($x_d$) by assuming perfect 3D uniform fiber dispersion and independent single-fiber pullout, Prof. Yun Yong Kim (Chungnam National University), Prof. Bang Yeon Lee (Chonnam National University), and Prof. Jin-Keun Kim (KAIST) developed a modified micromechanical framework. The authors utilized fluorescence microscopy and digital image processing (extracting individual fiber 3D inclination angle $\theta$ and center-to-center spacing $s$ from bounding-circle packing density $F_c$) combined with DIANA 3D nonlinear FE multi-fiber pullout simulations. The study identified a **critical fiber spacing ($s_{cr} = 0.045\sim 0.063\ \text{mm}$) for 'plug pull-out'**, wherein tight fiber clustering causes the intervening matrix block to tear out in shear. By excluding ineffective fibers ($\theta > 75^\circ$ and $s < s_{cr}$), the authors established a **Modified Fiber Bridging Curve** that accurately predicts uniaxial tensile stress-strain behavior. Fluorescence measurements revealed that the actual effective bridging fiber ratio accounts for only **$75.5\sim 86.2\%$** of the nominal volume fraction ($V_f = 2.0\ \text{vol.\%}$) across water-to-binder ratios (W/C = 0.60, 0.48 with and without slag). Incorporating the modified effective fiber volume fraction ($V_f^{eff}$) and crack spacing ($x_d$) reduced tensile strain prediction errors from over 40 % in classical models down to **within ±5 %**, accurately predicting tensile strain capacities ($2.4\sim 3.6\%$) and ultimate tensile strengths ($3.5\sim 5.7\ \text{MPa}$).

## Key Contributions

1. **First formulation of plug pull-out failure mode and critical fiber spacing ($s_{cr} = 0.045\sim 0.063\ \text{mm}$)**:
   - Demonstrated via 3D FEA that when inter-fiber spacing falls below $s_{cr}$ due to local clustering, individual frictional pullout is suppressed in favor of collective matrix shear tear-out.
2. **Automated extraction of individual fiber inclination ($\theta$) and packing density ($F_c$) via fluorescence image processing**:
   - Mapped 3D orientation angle distributions across thousands of fibers per section using $F_c = A_{ob}/A_{cc}$, quantifying fiber rupture losses for $\theta > 75^\circ$.
3. **Establishment of Modified Fiber Bridging Curve ($\sigma$-$\delta$) excluding ineffective fibers**:
   - Corrected the idealized 100 % efficiency assumption of classical micromechanics by applying the actual measured effective fiber fraction ($V_f^{eff} / V_f = 75.5\sim 86.2\%$).
4. **Substantial reduction of tensile strain prediction error from $40\% \rightarrow 5\%$**:
   - Integrated the modified bridging peak displacement ($\delta_{peak}$) with crack spacing ($x_d$) to achieve close agreement with experimental tensile stress-strain curves.

## Methods

- **Materials and mixture proportions (Tables 1–2, mass ratios)**:
  - Binders: Type I Portland cement (OPC) + GGBS (Blaine $4300\ \text{cm}^2/\text{g}$).
  - Fine aggregates: Micro-silica sand ($d_{50} = 110\ \mu\text{m}$, S/B = 0.36).
  - Reinforcing fibers: Kuraray oil-coated PVA fibers ($L_f = 12\ \text{mm}, d_f = 40\ \mu\text{m}$, tensile strength 1600 MPa, modulus 40 GPa, $V_f = 2.0\ \text{vol.\%}$).
  - Four mixture series:
    1. W/C = 60 % (w/o slag, pure cement).
    2. W/C = 60 % (w/ slag 20 %, effective W/B = 48 %).
    3. W/C = 48 % (w/o slag, low W/C cement).
    4. W/C = 48 % (w/ slag 20 %, effective W/B = 38 %).
- **Image processing and numerical simulation systems (Figures 1–6 & 8–10)**:
  - Fluorescence analysis: Vacuum epoxy impregnation of cut sections $\rightarrow$ RGB imaging $\rightarrow$ binarization $\rightarrow$ packing density $F_c = \frac{4}{\pi} \frac{d}{l}$ calculation $\rightarrow$ inclination angle $\theta = \arccos(\frac{4}{\pi} F_c)$ and centroid spacing $s$ measurements.
  - 3D FE pullout analysis: DIANA 9.2 nonlinear solver (multi-fiber embedment $l_e = 3.0\ \text{mm}$ to determine critical spacing $s_{cr}$).
  - Direct tension testing: Dogbone specimens ($330\ \text{mm} \times 60\ \text{mm} \times 13\ \text{mm}$, 0.2 mm/min displacement control, 80 mm gauge length).

## Results

### 1. Effective fiber ratios, plug pull-out critical spacing, and uniaxial tensile responses across mixtures (Tables 1–4 & Figs. 7–11)

| Mix ID | W/B Ratio & Binders | Plug Critical Spacing ($s_{cr}$, mm) | $\theta > 75^\circ$ Excluded (%) | $s < s_{cr}$ Excluded (%) | **Effective Fiber Ratio ($V_f^{eff}/V_f$)** | Measured Tensile Strength ($\sigma_{peak}$, MPa) | Measured Strain Capacity ($\varepsilon_{tu}$, %) | Modified Model Predicted ($\varepsilon_{pred}$, %) |
|---|---|---|---|---|---|---|---|---|
| **W/C 60% (w/o slag)** | 0.60 (Pure cement) | **0.063 mm** | 2.8 % | 16.5 % | **80.7 %** | 3.5 ± 0.4 MPa | **2.4 ± 0.3 %** | **2.35 % (Error 2 %)** |
| **W/C 60% (w/ slag)** | 0.48 (Slag blend) | **0.052 mm** | 0.9 % | 12.9 % | **86.2 % (Highest)** | 4.8 ± 0.15 MPa | **3.6 ± 0.2 %** | **3.52 % (Error 2 %)** |
| **W/C 48% (w/o slag)** | 0.48 (Pure cement) | **0.048 mm** | 2.9 % | 21.6 % | **75.5 %** | 4.8 ± 0.35 MPa | **0.73 ± 0.2 %** | **0.78 % (Error 7 %)** |
| **W/C 48% (w/ slag)** | 0.38 (Slag blend) | **0.045 mm** | 1.9 % | 18.3 % | **79.8 %** | 5.7 ± 0.3 MPa | **0.98 ± 0.3 %** | **0.95 % (Error 3 %)** |

### 2. Modified micromechanics and tensile deformation mechanisms
- **Maximizing effective fiber fraction via slag**: The W/C 60% (w/ slag) mix minimized fiber clustering through the ball-bearing effect of slag particles ($s < s_{cr}$ fraction at 12.9 %), securing an effective fiber ratio of 86.2 % and achieving the highest tensile strain capacity of **$3.6\ \%$** ($3.6 \%$).
- **Physical origin of classical model error**: Classical models neglected plug pull-out in fiber clusters, overpredicting bridging stress and ductility by over 40 %; applying $V_f^{eff}$ restores rigorous agreement.

- **Overall conclusion**: This landmark paper established a modified fiber bridging model integrating critical spacing for plug pull-out with image processing, raising the predictive accuracy of ECC tensile strain capacity to within ±5 %.

## Related Notes

- [[hyun-2018-limestone-powder-hdcc-micromechanics]] — Micromechanical fiber pullout and fracture toughness characterization.
- [[choi-2016-fiber-orientation-uhpcc-post-cracking-tensile]] — Fiber orientation and tensile modeling in ultra-high-performance composites.
- [[strain-hardening-mechanism]] — Pseudo-strain-hardening micromechanics and fiber bridging curves ($\sigma$-$\delta$).
- [[multiple-cracking-behavior]] — Saturated multiple microcrack spacing ($x_d$) and crack width control.
