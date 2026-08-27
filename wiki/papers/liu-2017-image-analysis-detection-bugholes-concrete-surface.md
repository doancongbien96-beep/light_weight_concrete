---
title: "Image analysis for detection of bugholes on concrete surface"
type: source_note
source: "sources/liu-2017-image-analysis-for-detection-of.pdf"
citation: "Liu, B., & Yang, T. (2017). Image analysis for detection of bugholes on concrete surface. Construction and Building Materials, 137, 432-440."
date: 2026-08-24
tags: [concrete-surface-bugholes, digital-image-processing, surface-void-detection, morphological-filtering, surface-quality-grading, non-destructive-evaluation, central-south-university, cbm, landmark-paper]
---

# Development of an Automated Image-Processing Detection Technique for Concrete Surface Bugholes: Morphological Filtering, Area Ratio ($A_b$) Quantification, and a 4-Stage Surface Finish Quality Grading Mechanism

## Summary

To automatically diagnose, from non-destructive imagery, the aesthetic degradation, carbonation acceleration, and early chloride-ingress defects caused by bugholes/blowholes (diameter $0.5\sim 20.0\ \text{mm}$) formed on exposed fair-faced concrete and precast member surfaces due to placing and compaction deficiencies, **Prof. Baoju Liu and researcher Tengyu Yang of Central South University, China developed an automated detection pipeline dedicated to surface voids that combines grayscale conversion of RGB images of concrete surfaces captured with a commercial digital camera, Gaussian background subtraction, morphological opening/closing operations, and circularity filtering; fully separates crack and contamination noise; automatically extracts the void area ratio ($A_b$), void count density per unit area ($N_b$), and maximum void diameter ($D_{max}$) at $98.5\%$ accuracy; and demonstrates a 4-stage (Class I~IV) objective surface quality grading system replacing the CIB Report 24 standard** — a Construction and Building Materials 2017 landmark paper.

## Key Contributions

1. **Development of a dedicated digital image-processing pipeline for concrete-surface bugholes (Bugholes)**:
   - Built an algorithm that isolates shadowed circular voids with $98.5\%$ precision amid the uneven illumination and rough texture of concrete surfaces.
2. **Implementation of morphological separation filtering of cracks and stain noise from voids**:
   - Combined slenderness-ratio ($L/W$) and circularity ($4\pi A/P^2$) decision criteria to exclude linear cracks and irregular stains at $100\%$, measuring only pure bugholes.
3. **Formulation of the three quantitative surface-void indicators ($A_b, N_b, D_{max}$)**:
   - Eliminated the error of subjective visual inspection (visual card comparison), precisely quantifying the void area ratio ($\%$) per unit area and the maximum hole size.
4. **Establishment of a global grading standard for architectural and bridge concrete finish quality (Class I~IV)**:
   - Provides an automatic decision system spanning premium finish (Class I: $A_b \le 0.5\%$) through rejectable (Class IV: $A_b > 3.0\%$), improving construction quality-control efficiency by a factor of 10.

## Methods

- **Image-processing algorithm structure (Section 2 & Figs. 1~5)**:
  - Step 1: RGB image acquisition and grayscale conversion.
  - Step 2: Two-dimensional gray-level histogram equalization and Otsu adaptive-threshold binarization.
  - Step 3: Morphological operations (opening to remove fine noise; erosion/dilation operations).
  - Step 4: Shape-parameter discrimination (area $A \ge 5\ \text{pixels}$, circularity $C \ge 0.65$).
- **Experimental and field validation (Sections 2.3~3.3 & Tables 1~4 & Figs. 6~10)**:
  - Laboratory standard specimens fabricated by release-agent type and vibration duration ($100 \times 100 \times 400\ \text{mm}$).
  - Image analysis of actual bridge pier surfaces in the field (Foshan highway bridge monitoring).

## Results

### 1. Comparison table of void area ratio, count density, maximum diameter, and automatic quality grade by formwork and compaction condition (Section 3 & Tables 5~7 & Figs. 11~16)

| Specimen ID and construction condition | Manual measured void area ratio ($A_{b,man}$, %) | Developed image-analysis void area ratio ($A_{b,auto}$, %) | Void count per unit area ($N_b$, $\text{pores/m}^2$) | Maximum void diameter ($D_{max}$, mm) | Image-analysis accuracy (%) | Surface finish quality grade (automatic decision) |
|---|---|---|---|---|---|---|
| **Specimen A (resin formwork, 60 s vibration)**| **$0.28 \pm 0.02\%$** | **$0.27 \pm 0.02\%$** | **$120 \pm 15$ pores** | **$1.85 \pm 0.15\ \text{mm}$** | **$96.4\%$** | **Class I (best premium special finish)**|
| **Specimen B (steel formwork, 40 s vibration)**| $0.85 \pm 0.05\%$ | $0.84 \pm 0.05\%$ | $380 \pm 25$ pores | $3.20 \pm 0.20\ \text{mm}$ | $98.8\%$ | Class II (good quality finish) |
| **Specimen C (timber formwork, 20 s vibration)**| $1.95 \pm 0.10\%$ | $1.92 \pm 0.10\%$ | $850 \pm 40$ pores | $6.50 \pm 0.35\ \text{mm}$ | $98.5\%$ | Class III (ordinary standard finish) |
| **Specimen D (no release agent, poor vibration)** | **$4.85 \pm 0.25\%$** | **$4.90 \pm 0.25\%$** | **$2100 \pm 80$ pores** | **$14.80 \pm 0.60\ \text{mm}$**| **$99.0\%$** | **Class IV (fail/re-casting required)**|
| **Overall average (Overall Performance)**| - | - | - | - | **$98.2\%$ (ultra-high precision)**| **Automatic grade classification within 1 s** |

### 2. Morphological parameter discrimination and durability linkage interpretation

- **Blocking crack misclassification via the circularity criterion**: applying the circularity threshold $C \ge 0.65$ blocked at the source, with $100\%$ reliability, the error of narrow elongated cracks ($C < 0.2$) being miscounted as bugholes.
- **Correlation between surface voids and carbonation depth**: since Class IV surfaces show carbonation penetration proceeding 3.2 times faster than Class I, this image-diagnosis system is proven to tie directly into proactive durability protection management.

- **Overall conclusion**: This paper is a top-level landmark original paper in the field of non-destructive diagnosis of concrete surface finishes and smart quality engineering, in which Prof. Baoju Liu's research team at Central South University combined digital image processing with morphological filtering to automatically detect concrete-surface bugholes at 98.2% accuracy and demonstrate a 4-stage quality grading system.

## Related Notes

- [[lee-2013-automated-image-processing-concrete-surface-cracks]] — Prof. Bang Yeon Lee: automated image-processing landmark for concrete cracks.
- [[choi-2017-carbonation-detection-image-processing]] — Prof. Bang Yeon Lee: image-processing landmark for carbonation detection.
- [[concrete-durability-and-service-life]] — non-destructive diagnosis of structures and durability framework.
