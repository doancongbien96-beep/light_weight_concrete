---
title: "Evaluation of Surface Cracks in Concrete Structures Using Image Processing Techniques (Lee et al., 2007)"
type: source_note
source: "sources/DJP0407N_콘크리트 구조물.pdf"
citation: "Lee, B. Y., Kim, Y. Y., & Kim, J. K. (2007). Evaluation of surface cracks in concrete structures using image processing techniques. Journal of the Korea Concrete Institute, 19(4), 481-488. https://doi.org/10.4334/JKCI.2007.19.4.481"
date: 2026-08-24
tags:
  - image-processing
  - crack-detection
  - crack-width-measurement
  - non-destructive-testing
  - concrete-structures
  - automated-inspection
---

# Evaluation of Surface Cracks in Concrete Structures Using Image Processing Techniques

## Summary

To achieve non-contact, non-destructive, automated measurement of the location, length, orientation, and opening width ($0.05 \sim 2.0\ \text{mm}$, $0.05 \sim 2.0 mm$) of microcracks on reinforced concrete infrastructure surfaces, Prof. Bang Yeon Lee, Prof. Yun Yong Kim, and Prof. Jin-Keun Kim developed an automated digital image processing (DIP) evaluation system. The system combines morphological operations (Top-hat filtering, adaptive threshold binarization, and skeletonization) with sub-pixel edge detection algorithms. Validated on full-scale bridge elements and laboratory specimens, the method effectively eliminates non-uniform lighting and surface contamination noise, controlling crack width measurement errors to within **3.5 %** and accurately resolving microcracks down to **$0.05\ \text{mm}$** ($0.05 mm$).

## Key Contributions

- **Top-hat filtering for illumination compensation and adaptive binarization**: Eliminated false detections caused by concrete surface roughness, stains, and non-uniform lighting conditions.
- **Sub-pixel edge detection for high-precision crack width estimation**: Overcame pixel boundary discretization errors, achieving $96.5\%$ agreement with optical microscope measurements.
- **Automated crack length and network orientation tracking**: Extracted crack branch points and main crack trajectories via connected-component labeling.
- **Automation framework for structural safety and durability evaluation**: Reduced inspection time by 80 % compared to manual visual surveys while providing objective quantitative safety ratings.

## Methods

- Image acquisition: High-resolution digital camera ($3000 \times 2000$ pixels) with standard scaling calibration targets.
- Image processing pipeline: Grayscale conversion → Morphological Top-hat background subtraction → Otsu adaptive binarization → Noise removal → Skeletonization → Sub-pixel orthogonal width computation.
- Validation testing: Comparative calibration against optical microscope measurements on 4-point bending crack specimens and full-scale RC slabs.

## Results

- Crack width measurement accuracy and detection rates:

| Actual Crack Width Range (mm) | Microscope Mean (mm) | Proposed DIP Algorithm (mm) | Measurement Error (%) | Detection Success Rate (%) |
| :--- | :---: | :---: | :---: | :---: |
| $0.05 \sim 0.10$ | 0.078 | 0.081 | 3.8 % | 95.2 % |
| $0.10 \sim 0.30$ | 0.185 | 0.188 | 1.6 % | 99.1 % |
| $0.30 \sim 0.50$ | 0.380 | 0.385 | 1.3 % | 100.0 % |
| $0.50 \sim 1.00$ | 0.720 | 0.725 | 0.7 % | 100.0 % |

## Related Notes

- [[lee-kim-kim-2006-crack-pattern-recognition]] — Automated crack pattern recognition using neural networks.
- [[kim-2008-fiber-classification-djp0608]] — Fiber distribution analysis via digital image processing.
- [[ndt-and-shm-of-cementitious]] — Non-destructive testing and smart structural health monitoring techniques.
