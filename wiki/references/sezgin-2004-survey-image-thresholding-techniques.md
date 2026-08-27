---
title: "Survey over Image Thresholding Techniques and Quantitative Performance Evaluation (Sezgin & Sankur, 2004)"
type: reference_book
source: "sources/sankur-2004-survey-over-image-thresholding-techniques.pdf"
citation: "Sezgin, M., & Sankur, B. (2004). Survey over image thresholding techniques and quantitative performance evaluation. Journal of Electronic Imaging, 13(1), 146-165. https://doi.org/10.1117/1.1631315"
date: 2026-08-24
tags:
  - image-processing
  - thresholding-algorithms
  - binarization
  - crack-detection
  - quantitative-evaluation
---

## Summary
The most authoritative survey paper in the computer vision field: it classifies over 40 image binarization thresholding algorithms into six major categories (histogram-shape-based, clustering-based, entropy-based, object-attribute-based, spatial-statistics-based, and local adaptive), and comparatively evaluates them using quantitative performance measures (misclassification error, shape-preservation ratio) on nondestructive defect detection and character recognition images. It presents selection criteria for the binarization algorithms best suited to microcrack image segmentation of cementitious composites, fiber dispersion analysis, and porosity measurement (Otsu, Kittler-Illingworth, Sauvola, Niblack).

## Key Contributions
- **Systematization of 40 image binarization algorithms into six major categories**: mathematical formalization by segmentation theory and comparison of computational complexity.
- **Derivation of the optimal local adaptive algorithm under non-uniform illumination and noise**: demonstrated that the Sauvola and Wolf techniques are optimal for extracting concrete crack boundaries.
- **Establishment of five objective segmentation quality metrics**: definition of Misclassification Error (ME), Relative Foreground Area Error (RAE), and Modified Hausdorff Distance (MHD).

## Related Notes
- [[vincent-1993-morphological-grayscale-reconstruction]] - mathematical morphology image processing
- [[lee-2010-fluorescence-discriminating-fibers-hybrid-ecc]] - digital-image-based fiber dispersion analysis
