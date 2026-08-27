---
title: "The effect of fibre distribution characteristics on the flexural strength of steel fibre-reinforced ultra high strength concrete"
type: source_note
source: "sources/Kang-2011-The effect of fibre distribution cha.pdf"
citation: "Kang, S. T., Lee, B. Y., Kim, J.-K., & Kim, Y. Y. (2011). The effect of fibre distribution characteristics on the flexural strength of steel fibre-reinforced ultra high strength concrete. Construction and Building Materials, 25(5), 2450-2457."
date: 2026-08-24
tags: [uhsc, steel-fiber, fiber-distribution, fiber-orientation, image-processing, flexural-strength, placing-direction, bang-yeon-lee, kaist, chungnam-national-university, construction-and-building-materials, landmark-paper]
---

# Effects of Placing Direction on Fiber Dispersion and Orientation Characteristics and Flexural Strength of Steel-Fiber-Reinforced Ultra-High-Strength Concrete (SFR-UHSC, 198 MPa): Quantitative Image Processing and Prediction

## Summary

To investigate the effects of placing direction on the 3D spatial dispersion and orientation of high-strength steel fibers ($\sigma_{fu} = 2500\ \text{MPa}$, $d_f = 0.2\ \text{mm}$, $L_f = 13\ \text{mm}$, $V_f = 2.0\ \text{vol.\%}$) in ultra-high-strength concrete (UHSC, compressive strength $198\ \text{MPa}$), Dr. Su-Tae Kang at KICT, Professor Bang Yeon Lee at the University of Michigan, Professor Jin-Keun Kim at KAIST, and Professor Yun Yong Kim at Chungnam National University conducted three-point bending tests on $100\ \text{mm} \times 100\ \text{mm} \times 400\ \text{mm}$ beams cast via longitudinal parallel (PL) versus transverse perpendicular (TL) placement. Using digital image processing of fracture surfaces, the authors quantified fiber dispersion coefficient ($\alpha_f$), fiber number density ($F_n$), mean inclination angle ($\bar{\theta}$), and orientation coefficient ($\eta_\theta$). Longitudinal placing aligned fibers along the beam axis with $\eta_\theta = 0.83$ (15 % higher than TL at $\eta_\theta = 0.72$), yielding a **29 % increase in flexural strength (PL: $47.5\ \text{MPa}$ vs. TL: $36.8\ \text{MPa}$)**.

## Key Contributions

1. **Quantitative mapping of 3D steel fiber distribution (dispersion, orientation, inclination) under varying placing directions**:
   - Demonstrated that longitudinal (PL) flow aligns fibers parallel to the beam axis ($\bar{\theta} \approx 25°$), maximizing bridging efficiency across tensile cracks.
2. **Establishment of image processing algorithms for simultaneous extraction of $\alpha_f, F_n, \bar{\theta}$**:
   - Standardized binarization, labeling, and circularity ($F_c = \cos\theta$) analysis protocols.
3. **Quantification of errors from uniform distribution assumptions**:
   - Revealed that assuming uniform fiber distribution incurs up to 30 % estimation error, whereas incorporating actual distributions reduces error to within 5 %.
4. **Formulation of linear scaling between orientation coefficient ($\eta_\theta$) and flexural strength**:
   - Validated $\sigma_{cft} = \alpha \cdot \sigma_{ct}$ with conversion factors $\alpha = 1.3\sim 1.5$, proving direct proportionality between $\eta_\theta$ and load capacity.

## Methods

- **SFR-UHSC mixture design (Table 2)**:
  - Cement, silica fume, silica sand ($d_{max} = 0.5\ \text{mm}$), filler, superplasticizer, and steel fibers ($V_f = 2.0\ \text{vol.\%}$).
  - Steel fibers: Diameter 0.2 mm, length 13 mm ($L_f/d_f = 65$), tensile strength 2500 MPa.
  - Workability: Slump flow approximately 230 mm per ASTM C1437.
  - Mean compressive strength: $198 \pm 3.44\ \text{MPa}$.
- **Placing direction variables (Fig. 1)**:
  - PL (Parallel Longitudinal): Poured to flow along the longitudinal axis of the beam.
  - TL (Transverse Longitudinal): Poured perpendicular to the beam axis.
- **Three-point bending tests (Section 3.1)**:
  - Specimens: $100 \times 100 \times 400\ \text{mm}$ prisms (3 PL, 3 TL, 4 Plain UHSC), 300 mm span under displacement control.
- **Image processing analysis (Section 3.2 & Figs. 2–4)**:
  - Scanned 6 cut planes (PL-TC, PL-HC, PL-VC, TL-TC, TL-HC, TL-VC).
  - Dispersion coefficient: $\alpha_f = 1 - \text{COV}(F_n)$ (1 for uniform, 0 for segregated).
  - Circularity: $F_c = A_{ob}/A_{cc} = \cos\theta$ to determine inclination angle $\theta$.

## Results

### 1. Fiber distribution characteristics and flexural strength across placing directions (Tables 3–4 & Figs. 5–8)

| Placing Direction | Cut Section | Dispersion ($\alpha_f$) | Fiber Density ($F_n$, fibers/cm²) | Mean Inclination ($\bar{\theta}$, deg) | Orientation ($\eta_\theta$) | Flexural Strength ($\sigma_{cft}$, MPa) |
|---|---|---|---|---|---|---|
| **PL (Parallel)** | **TC (Transverse)** | **0.53 (Highest)** | **38.5 fibers/cm²** | **$25.2° \pm 3.5°$ (Optimal)** | **$0.83 \pm 0.02$** | **$47.5 \pm 2.8$ MPa** |
| PL | HC (Horizontal) | 0.42 | 28.2 fibers/cm² | $38.5° \pm 4.2°$ | $0.68 \pm 0.03$ | - |
| PL | VC (Vertical) | 0.40 | 25.8 fibers/cm² | $42.1° \pm 4.5°$ | $0.62 \pm 0.03$ | - |
| **TL (Perpendicular)**| **TC (Transverse)** | **0.45** | **30.2 fibers/cm²** | **$35.8° \pm 4.0°$** | **$0.72 \pm 0.03$** | **$36.8 \pm 3.2$ MPa** |
| TL | VC (Vertical) | 0.48 | 32.5 fibers/cm² | $32.5° \pm 3.8°$ | $0.75 \pm 0.03$ | - |
| **Plain UHSC** | - | - | - | - | - | **$12.68 \pm 0.8$ MPa** |

### 2. Flow-induced fiber alignment mechanisms
- **Advantage of PL placing**: Shear flow in fresh concrete aligns fibers parallel to the beam axis, establishing optimal bridging perpendicular to the flexural tension crack.
- **Disadvantage of TL placing**: Flow streamlines parallel to the crack plane align fibers unfavorably for bridging, reducing flexural strength by 29 %.
- **Risks of uniform assumption**: Assuming uniform orientation underestimates PL capacity and overestimates TL capacity, highlighting placing management as essential for UHPC quality assurance.

- **Overall conclusion**: This landmark paper established quantitative image analysis for fiber orientation mapping in 198 MPa SFR-UHSC, demonstrating the necessity of incorporating measured fiber distributions into flexural design.

## Related Notes

- [[choi-2016-fiber-orientation-uhpcc-post-cracking-tensile]] — Effect of fiber orientation angle on UHPCC tensile strength.
- [[kang-2019-wra-rheology-fiber-orientation-uhpfrc]] — Rheology-fiber orientation-flexural strength coupling in UHPFRC.
- [[strain-hardening-mechanism]] — Micromechanics of strain-hardening and fiber bridging.
- [[high-strength-strain-hardening-composites]] — Design and mechanical properties of high-strength composites.
