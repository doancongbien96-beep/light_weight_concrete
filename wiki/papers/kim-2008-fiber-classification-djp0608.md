---
title: "Classification of PVA Fiber Dispersion in SHCC Cross-Sectional Images (Kim et al., 2008)"
type: source_note
source: "sources/DJP0608N_PVA-ECC단면 이미지의.pdf"
citation: "Kim, Y. Y., Lee, B. Y., Bang, J. W., & Kong, J. S. (2008). Classification of PVA fiber dispersion in SHCC cross-sectional images using digital image processing. Journal of the Korea Concrete Institute, 20(3), 365-372. https://doi.org/10.4334/JKCI.2008.20.3.365"
date: 2026-08-24
tags:
  - fiber-dispersion
  - digital-image-processing
  - pva-fiber
  - cross-sectional-image
  - automated-classification
  - spatial-point-pattern
---

# Classification of PVA Fiber Dispersion in SHCC Cross-Sectional Images

## Summary

To automatically and accurately quantify the spatial dispersion density and dispersion coefficient ($\alpha_{disp}$) of tens of thousands of fine PVA microfibers (diameter 39 µm) across cut sections of strain-hardening cementitious composites (PVA-SHCC), Prof. Yun Yong Kim, Prof. Bang Yeon Lee, Prof. Jin-Wook Bang, and Prof. Jung-Sik Kong developed and validated a digital image processing (DIP) framework combining adaptive binarization, watershed segmentation, and geometric shape filtering on UV fluorescence microscopy images of epoxy-impregnated polished sections. The algorithm automatically separated fibers from matrix voids and micro-defects with an accuracy exceeding $98 \%$, ensuring objectivity and rapidity in fiber dispersion evaluation.

## Key Contributions

- **DIP-based automated PVA fiber cross-sectional segmentation**: Formulated automated fluorescence intensity thresholding and multi-peak overlapping fiber separation filters.
- **Accurate calculation of fiber dispersion coefficient ($\alpha_{disp} = \exp[-\sqrt{(\sum(x_i - 1)^2)/k}]$)**: Divided cross-sections into $k$ grid cells to statistically quantify local density variations.
- **Suppression of void and microcrack false-positive rates below 2 %**: Applied geometric filtering based on area, circularity, and aspect ratio.
- **Verification of mixing sequence effects on fiber dispersion**: Demonstrated that slurry pre-mixing improves $\alpha_{disp}$ from 0.55 to 0.85 (+55 %) compared to dry batching.

## Methods

- Specimens: PVA-SHCC ($V_f = 2.0\%$, $W/B = 0.45$, silica sand).
- Specimen preparation: Vacuum drying, vacuum impregnation with fluorescent-dye-doped epoxy, and 6-stage diamond suspension polishing ($1\ \mu\text{m}$ roughness, $1 \mu m$).
- Image acquisition and processing: UV optical microscope ($100\times$ magnification, $100 \times$, high-resolution CCD camera) with custom MATLAB image processing routines.

## Results

- Identification accuracy and dispersion coefficient analysis across mixing methods:

| Mixing Method | Sequence | Fiber Count ($EA/\text{mm}^2$, $EA/mm^2$) | Manual Match (%) | Dispersion Coefficient $\alpha_{disp}$ | Tensile Strain Capacity (%) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| Method A | Dry powder + simultaneous fiber addition | 125 | 96.8 | 0.58 | 2.10 |
| Method B | Slurry mixing followed by fiber dispersion | 168 | 98.5 | **0.86** | **4.65** |
| Method C | Excessive over-mixing (fiber balling) | 98 | 94.2 | 0.42 | 1.15 (Premature rupture) |

## Related Notes

- [[lee-2010-fluorescence-discriminating-fibers-hybrid-ecc]] — Discrimination of hybrid fiber dispersion via fluorescence image analysis.
- [[fiber-orientation-distribution]] — Theoretical foundations of fiber orientation and spatial dispersion.
- [[pseudo-strain-hardening-criteria]] — Micromechanical criteria for pseudo-strain-hardening in composites.
