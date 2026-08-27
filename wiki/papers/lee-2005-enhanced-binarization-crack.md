---
title: "Development of Image Processing for Concrete Surface Cracks by Employing Enhanced Binarization and Shape Analysis Technique (Lee, Kim & Kim, 2005)"
type: source_note
source: "sources/DJP0105N_개선된 이진화.pdf"
citation: "이방연, 김윤용, 김진근. 개선된 이진화 기법 및 형태 분석 기법을 이용한 콘크리트 표면 균열 영상처리 기법 개발. 한국콘크리트학회 논문집 17(3) (2005) 361-368."
date: 2026-08-22
tags: [image-processing, crack-detection, binarization, morphology, crack-width, korean-paper, scan-ocr]
---

# Development of Image Processing for Concrete Surface Cracks by Employing Enhanced Binarization and Shape Analysis Technique

## Summary

This paper presents an automated digital image processing algorithm to measure crack width, length, and orientation on concrete surfaces captured by digital cameras (KAIST Jin-Keun Kim research group, doctoral research of Prof. Bang Yeon Lee). The algorithm integrates 3 core stages: morphological shading correction, 2-stage enhanced binarization, and shape analysis. Implemented in MATLAB, the technique was validated for measurement accuracy against visual inspection and classical thresholding approaches.

## Key Contributions

1. **Morphological shading correction**: Eliminated uneven illumination using grayscale erosion/dilation/opening/closing operations with structuring elements, establishing a standard pre-processing pipeline for crack detection (Fig. 2).
2. **2-stage enhanced binarization**: Sequentially applied global (Otsu) and local thresholding, extracting microcracks missed in the initial phase and merging them; performance was enhanced by modifying the packing density criterion (Fig. 3–4).
3. **Crack width calculation algorithm**: Extracted crack skeletons via thinning and computed normal widths using a center-to-boundary minimum distance filter across a $40 \times 40$ pixel window (40×40, Figs. 6–8).
4. **Crack length and orientation tracking**: Employed connected-component labeling and coordinate tracking, determining orientation angles via $\tan^{-1}$ calculations (Eq. 2).
5. **Experimental calibration**: Verified using a digital camera with a NIKKOR AF-S 28~70 mm lens at a spatial resolution of 0.12 mm per pixel.

## Methods

Implemented in MATLAB. Processing workflow: Image acquisition → Shading correction → 1st-stage crack extraction (global + local + noise filtering) / 2nd-stage crack extraction (global + local) → 1st-stage crack subtraction and merging → Shape analysis (thinning / boundary tracing / labeling) → Calculation of width, length, and orientation.

## Related Notes

- [[kim-2008-fiber-classification-and-detection-technique]] — Subsequent work from the same research group using ANN for fluorescent fiber detection.
- [[lee-kim-kim-2006-crack-pattern-recognition]] — Neural network extension for concrete surface crack pattern recognition (DJP0205N).
- [[choi-2016-fiber-orientation-uhpcc-post-cracking-tensile]] — Image-analysis-based fiber orientation assessment.

## Remarks

- Scanned OCR document (Korean + English). Minor OCR artifacts exist in Korean body text; verify key values against original sources when citing.
