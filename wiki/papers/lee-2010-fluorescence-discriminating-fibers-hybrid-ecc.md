---
title: "Fluorescence Characteristic Analysis for Discriminating Fibers in Cementitious Composites"
type: source_note
source: "sources/lee-2010-fluorescence-characteristic-analysis-for-discriminating.pdf"
citation: "Lee, B. Y., Kim, T., & Kim, Y. Y. (2010). Fluorescence Characteristic Analysis for Discriminating Fibers in Cementitious Composites. Journal of Advanced Concrete Technology, 8(3), 337-344."
date: 2026-08-24
tags: [hybrid-ecc, fluorescence-spectroscopy, pva-fiber, pet-fiber, pe-fiber, multispectral-imaging, lda, fiber-discrimination, bang-yeon-lee, jact, landmark-paper]
---

# Fluorescence Characteristic Analysis and Multispectral-LDA Optimal Optical Filter Design for Discriminating Synthetic Fibers (PVA, PET, PE) in Hybrid ECC

## Summary

To non-destructively quantify the distinct 3D spatial dispersion and orientation characteristics of individual fiber types in hybrid fiber-reinforced cementitious composites (Hybrid ECC), Prof. Bang Yeon Lee (first author, Chonnam National University), Tae-Min Kim, and Prof. Yun Yong Kim (corresponding author) conducted a landmark study. The authors measured the **Fluorescence Excitation-Emission Matrices (EEM)** of 3 synthetic fiber types (PVA, PET, PE) and cement matrices using a Horiba FluoroMax-4 spectrofluorometer. Combining a **multispectral imaging model with Linear Discriminant Analysis (LDA)**, the authors established the world's first mathematical framework for designing optimal optical bandpass filters to maximize fiber discrimination resolution (Journal of Advanced Concrete Technology, 2010). While the cement matrix exhibited negligible fluorescence, PET ($\text{RFI} = 412$), PVA ($\text{RFI} = 100$), and PE ($\text{RFI} = 35$) fibers displayed distinct spectral peaks. Applying excitation/emission optical filters of Ex 400 nm / Em 460 nm for PVA-PE systems and Ex 350 nm / Em 390 nm for PVA-PET systems enabled $100\%$ automated identification and separation.

## Key Contributions

1. **Construction of 3D fluorescence spectroscopy EEM database for synthetic fibers (PVA/PET/PE) and cement matrices**:
   - Mapped relative fluorescence intensity (RFI) across excitation wavelengths of 250~500 nm and emission wavelengths of 300~650 nm.
2. **Algebraic design methodology for optimal optical filters based on multispectral models and LDA**:
   - Maximized Fisher's discriminant ratio $J = S_B/S_W$ (between-class to within-class variance) to analytically derive optimal filter transmission spectra $s(u), f(v)$.
3. **Automated 100 % discrimination algorithm in Hybrid ECC**:
   - Developed an image processing pipeline extracting centroid coordinates, cross-sectional areas, and orientation angles for PVA-PE and PVA-PET combinations from a single fluorescence image capture.
4. **Integration with hybrid bridging micromechanical models**:
   - Enabled isolated quantification of dispersion coefficients ($\alpha_f$) and fiber count densities ($F_n$) per fiber type, improving the accuracy of hybrid composite bridging stress-crack opening ($\sigma-\delta$) models.

## Methods

- **Materials and specimen preparation (Section 2.1)**:
  - PVA fiber: Kuraray REC15, diameter $39\ \mu\text{m}$, length 12 mm.
  - PET fiber: Diameter $14\ \mu\text{m}$, length 12 mm.
  - PE fiber: Diameter $12\ \mu\text{m}$, length 15 mm.
  - Cement matrix: W/C = 0.60, S/C = 0.80, Slag/C = 0.25, HPMC = 0.001 by weight.
- **Spectrofluorometric measurement (Section 2.2, Fig. 1)**:
  - Apparatus: Horiba FluoroMax-4 spectrofluorometer.
  - Excitation wavelengths: 250~500 nm (5 nm increments).
  - Emission detection: 300~650 nm (1 nm increments).
- **Mathematical model for optimal filter design (Sections 2.3–2.4)**:
  - Sensor intensity: $g_i = \int \int s(u) h_i(u,v) f(v) dudv$.
  - Optimization objective: Maximize Fisher discriminant $J = \frac{f^T B f}{f^T W f}$ via LDA eigenvalue decomposition.

## Results

### 1. Fluorescence spectroscopy characteristics and LDA optimal filter wavelengths (Tables 2–5, Figs. 2–4)

| Material / Hybrid Combination | Peak Excitation (Ex, nm) | Peak Emission (Em, nm) | Relative Fluorescence Intensity (RFI) | LDA Optimal Excitation Filter (nm) | LDA Optimal Emission Filter (nm) | Discrimination Accuracy |
|---|---|---|---|---|---|---|
| **Cement Matrix** | Broad / Weak | $400 \sim 500\ \text{nm}$ | **$< 5$ (Negligible)** | - | - | Complete background separation |
| **PVA Fiber** | **$380\ \text{nm}$** | **$460\ \text{nm}$** | **100 (Baseline)** | - | - | Distinct green fluorescence |
| **PET Fiber** | **$350\ \text{nm}$** | **$390\ \text{nm}$** | **412 (Peak intensity)** | - | - | Intense UV-blue fluorescence |
| **PE Fiber** | **$360\ \text{nm}$** | **$430\ \text{nm}$** | **35 (Low-medium)** | - | - | Blue fluorescence |
| **PVA - PE Hybrid** | $400\ \text{nm}$ | $460\ \text{nm}$ | $\Delta\text{RFI} = 65$ | **$400 \pm 10\ \text{nm}$** | **$460 \pm 15\ \text{nm}$** | **$100\%$ Discrimination** |
| **PVA - PET Hybrid** | $350\ \text{nm}$ | $390\ \text{nm}$ | $\Delta\text{RFI} = 312$ | **$350 \pm 10\ \text{nm}$** | **$390 \pm 10\ \text{nm}$** | **$100\%$ Discrimination** |
| **PET - PE Hybrid** | $350\ \text{nm}$ | $390\ \text{nm}$ | $\Delta\text{RFI} = 377$ | **$350 \pm 10\ \text{nm}$** | **$390 \pm 10\ \text{nm}$** | **$100\%$ Discrimination** |

### 2. Spectral analysis and discrimination mechanics
- **Molecular origin of fluorescence**: The conjugated benzene ring structure of PET emits intense fluorescence (RFI 412) under 350 nm excitation, whereas the acetalized structure of PVA emits at 380/460 nm.
- **LDA bandpass filter optimization**: Rather than simply taking peak wavelengths, LDA optimizes the spectral overlap integrals against background noise, driving false-recognition rates to zero.

- **Overall conclusion**: This landmark paper integrated fluorescence spectroscopy with LDA machine learning pattern recognition, establishing the first optical filter design methodology to achieve 100% automated discrimination of individual synthetic fiber types in hybrid fiber-reinforced cementitious composites.

## Related Notes

- [[kim-2007-slag-ecc-tensile-fiber-dispersion]] — Fluorescence microscopy for evaluating fiber dispersion in Slag-ECC.
- [[kang-2011-fiber-distribution-uhsc-flexural-strength]] — Prof. Bang Yeon Lee: Image analysis of steel fiber distribution in UHSC.
- [[felekoglu-2015-htpp-ecc-fiber-distribution-image-analysis]] — Image analysis for micro-fiber dispersion.
- [[strain-hardening-mechanism]] — ECC micromechanics and hybrid fiber bridging theories.
