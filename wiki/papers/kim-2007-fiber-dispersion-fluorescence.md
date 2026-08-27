---
title: "Quantitative Evaluation of Fiber Dispersion of Fiber-Reinforced Cement Composites Using an Image Processing Technique (Kim, Lee, Kim & Kim, 2007)"
type: source_note
source: "sources/DJP0307N_이미지 프로세싱.pdf"
citation: "김윤용, 이방연, 김정수, 김진근. 영상처리기법을 이용한 섬유보강 시멘트 복합재의 섬유 분산성 정량 평가. 한국비파괴검사학회지 27(2) (2007) 148-156."
date: 2026-08-22
tags: [fiber-dispersion, image-processing, fluorescence, watershed-algorithm, pva-ecc, korean-paper, scan-ocr]
---

# Quantitative Evaluation of Fiber Dispersion in Fiber-Reinforced Cement Composites Using Image Processing

## Summary

This paper by Prof. Jin-Keun Kim's group at KAIST captures fluorescent-dyed (GFP-like agent) PVA fibers using a fluorescence microscope and CCD camera, quantitatively assessing cross-sectional fiber distribution through an improved algorithm based on discriminant analysis and watershed segmentation. This work serves as the foundational predecessor to [[kim-2008-fiber-classification-and-detection-technique]].

## Key Contributions

1. **Establishment of fluorescence imaging pipeline**: Overcame low optical contrast between PVA fibers and cement matrices by observing fibers as green fluorescent dots under confocal fluorescence microscopy (Olympus BX51 + CCD).
2. **Four-class geometric shape classification (Figs. 6–7)**: Classified detected fiber objects into Type 1 (circular cross-section / perpendicular cut) through Type 4 (inclined cut) using packing density and perimeter-to-area histograms, extracting spatial orientation data.
3. **Application of watershed segmentation (Beucher method)**: Separated multi-peak clustered fiber blobs (Fig. 8) into discrete fiber entities (Fig. 9), enabling accurate fiber counting even in densely packed sections.
4. **Integration of statistical dispersion metrics**: Applied statistical processing to spatial coordinates to derive quantitative fiber dispersion indices.

## Methods

- Prepared PVA-ECC specimens ($13 \times 36 \times 20\ \text{mm}$, 13×36×20 mm), polished cross-sections, and captured fluorescence images.
- Processing workflow: RGB $\rightarrow$ grayscale $\rightarrow$ Otsu binarization $\rightarrow$ noise filtering $\rightarrow$ packing density filtering $\rightarrow$ watershed segmentation.

## Results

- Successfully automated the recognition and segmentation of overlapping PVA fibers in cementitious cross-sections.
- Validated that the combination of discriminant thresholding and watershed segmentation delivers robust, objective fiber dispersion metrics across varying mix proportions.

## Related Notes

- [[kim-2008-fiber-classification-and-detection-technique]] — Extended this framework to 5-type ANN classification (JKCI 2008).
- [[lee-2005-enhanced-binarization-crack]] — Shares preprocessing algorithms including Otsu and 2-stage binarization.
- [[choi-2016-fiber-orientation-uhpcc-post-cracking-tensile]] — Addresses fiber orientation and distribution quantification in steel-fiber UHPCC.
- [[zhu-2019-3dp-ecc-ultra-high-ductility]] — SEM fiber count verification of alignment in 3D-printed ECC.
- [[lee-2009-extruded-ecc-panel-fiber-distribution]] — Follow-up application to extruded ECC panels by the same research group.
- [[kim-2007-slag-ecc-tensile-fiber-dispersion]] — Application of this dispersion assessment methodology to GGBS-ECC material design.
