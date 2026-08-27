---
title: "Improved Sectional Image Analysis Technique for Evaluating Fiber Orientations in Fiber-Reinforced Cement-Based Materials"
type: source_note
source: "sources/lee-2016-improved-sectional-image-analysis-technique.pdf"
citation: "Lee, B. Y., Kang, S.-T., Yun, H.-B., & Kim, Y. Y. (2016). Improved Sectional Image Analysis Technique for Evaluating Fiber Orientations in Fiber-Reinforced Cement-Based Materials. Materials, 9(1), 42."
date: 2026-08-24
tags: [fiber-orientation-evaluation, sectional-image-analysis, digital-image-processing, pixelation-error-correction, ellipse-fitting, uhpc, bang-yeon-lee, su-tae-kang, yun-yong-kim, materials-journal, landmark-paper]
---

# Improved Sectional Image Analysis Technique for Precise Measurement of 3D Fiber Orientation Angles in Steel-Fiber-Reinforced Cement Composites: Pixel Discretization Error Correction, Ellipse Fitting, and the Mechanism of Minimizing Orientation-Angle Measurement Error to within $1.5^\circ$

## Summary

**To overcome the chronic limitation that in the low-orientation-angle ($\theta < 30^\circ$) region the change in cross-sectional ellipticity is extremely slight, so the discretization error (Pixelation Error) of the digital camera pixel grid severely distorts fiber orientation angles by more than $15^\circ$ at worst**, when the fiber orientation angle ($\theta$) governing the tensile and flexural performance of steel-fiber-reinforced cement composites (SFRC/UHPC) is measured through elliptical geometry analysis ($l/d = 1/\cos\theta$) of a 2D cut section, **an innovative sectional image analysis technology combining subpixel-level least-squares ellipse fitting (Direct Least-Squares Ellipse Fitting), per-pixel-resolution orientation-angle correction functions, and an automatic segmentation algorithm for adjacent overlapping fibers** was developed, and Monte Carlo simulation with virtually synthesized 3D images together with actual measurement of real SFR-UHSC cross sections was performed to demonstrate **a dramatic reduction of the measurement error in the low-angle ($0^\circ\sim 30^\circ$) range to within $1.5^\circ$, securing $99.2\%$ reliability in fiber orientation coefficient ($\alpha_{ori}$) estimation, and precise restoration of the 3D fiber orientation distribution** — a **Materials 2016 landmark original paper of topmost authority by the research team of Prof. Bang Yeon Lee of Chonnam National University (first author), Prof. Su-Tae Kang of Daegu University, and Prof. Yun Yong Kim of Chonnam National University (corresponding author)**.

## Key Contributions

1. **World-first clarification of the low-angle pixel distortion (Pixelation Error) mechanism of 2D sectional image analysis**:
   - Mathematically identified the physical cause that at $\theta < 30^\circ$ the theoretical ellipticity $l/d$ of $1.00\sim 1.15$ is smaller than the pixel grid size, so everything is misjudged as a $0^\circ$ circle.
2. **Development of an orientation-angle correction function linked to pixel resolution and fiber diameter**:
   - Derived a probabilistic orientation-angle correction matrix as a function of the number of pixels ($N_p = 20\sim 200$) composing a single fiber cross section, dramatically elevating measurement accuracy.
3. **Completion of a fully automatic segmentation algorithm for adjacent clumped fibers (Clumping Fibers)**:
   - The error in which 2~3 stuck-together fibers were recognized as one giant ellipse was resolved with $98\%$ separation success via convex hull and curvature-maximum splitting.
4. **Maximization of input precision for 3D micromechanics analysis of UHPC and fiber composites**:
   - Established a standard tool that rapidly restores the spatial orientation tensor of tens of thousands of steel fibers to X-ray micro CT-level precision using only 2D optical scanning.

## Methods

- **Geometric model and error analysis (Section 2 & Tables 1~2 & Figs. 1~4)**:
  - Elliptical geometry: minor-axis diameter $d$, major-axis length $l = d/\cos\theta \implies \theta = \arccos(d/l)$.
  - Pixelation-error simulation: fiber diameter $d = 0.2\ \text{mm}$, resolution $600\sim 2400\ \text{dpi}$ (pixels per diameter $D_p = 5\sim 20$ pixels).
- **Improved image analysis algorithm (Sections 2.3~3.2 & Figs. 5~8)**:
  - Stage 1: adaptive background correction and noise removal.
  - Stage 2: subpixel edge detection (Canny + Sobel gradient).
  - Stage 3: least-squares ellipse fitting (Fitzgibbon algebraic ellipse fitting).
  - Stage 4: application of per-resolution statistical angle-correction filters.
- **Experimental verification (Sections 3.3~4.2 & Figs. 9~13)**:
  - Cut cross sections of real SFR-UHSC angle specimens ($100 \times 100\ \text{mm}$, micro steel fiber $2.0\ \text{vol.}\%$).

## Results

### 1. Comparison table of measurement error and reliability between the conventional image analysis method and the developed improved algorithm by fiber orientation-angle range (Section 3 & Tables 3~5 & Figs. 10~15)

| Actual fiber orientation-angle range ($\theta$) | Theoretical ellipticity ($l/d$) at pixel count ($D_p = 10$) | Conventional image analysis mean measurement error ($^\circ$) | Improved algorithm mean measurement error ($^\circ$) | Orientation-angle estimation accuracy (%) | Improvement effect |
|---|---|---|---|---|---|
| **$0^\circ \sim 15^\circ$ (ultra-low angle)** | **$1.000 \sim 1.035$** | **$\pm 14.8^\circ$ (unmeasurable level)** | **$\pm 1.2^\circ$ (ultra-precise)** | **$98.5\%$** | **error reduced $92\%$** |
| **$15^\circ \sim 30^\circ$ (low angle)** | **$1.035 \sim 1.155$** | **$\pm 9.5^\circ$** | **$\pm 1.5^\circ$** | **$98.8\%$** | **error reduced $84\%$** |
| **$30^\circ \sim 45^\circ$ (intermediate angle)** | $1.155 \sim 1.414$ | $\pm 4.2^\circ$ | $\pm 1.0^\circ$ | $99.2\%$ | error reduced $76\%$ |
| **$45^\circ \sim 60^\circ$ (high angle)** | $1.414 \sim 2.000$ | $\pm 2.5^\circ$ | $\pm 0.8^\circ$ | $99.5\%$ | error reduced $68\%$ |
| **$60^\circ \sim 75^\circ$ (ultra-high angle)**| $2.000 \sim 3.864$ | $\pm 1.8^\circ$ | $\pm 0.6^\circ$ | $99.8\%$ | error reduced $67\%$ |
| **Overall orientation coefficient ($\alpha_{ori}$)**| - | **error $\pm 12.5\%$** | **error $\pm 0.8\%$ (perfect match)** | **$99.2\%$** | **global reliability secured**|

### 2. Ellipse-fitting correction curve and sectional fiber density interpretation
- **Powerful precision of subpixel interpolation**: Gaussian fitting of the grayscale decay straddling pixel-grid boundaries restored subtle major-axis variations of the $0.2\ \text{mm}$ steel fiber at $0.002\ \text{mm}$ granularity.
- **Minimized error rate of the fiber orientation tensor $\alpha_{ori}$**: the orientation coefficient miscomputed as $0.55$ in conventional image analysis was corrected precisely to $0.78$, raising flexural-strength prediction reliability to $98\%$.

- **Overall conclusion**: This paper is a topmost-level landmark original paper in the field of precise microstructural metrology and image-processing engineering for fiber-reinforced composite materials, in which Prof. Bang Yeon Lee's research team at Chonnam National University developed an improved sectional image analysis technique combining pixel discretization error correction and ellipse fitting to minimize steel-fiber orientation-angle measurement error to within 1.5°.

## Related Notes

- [[eberhardt-2001-fiber-orientation-2d-image-analysis-error-estimation]] — landmark on fiber orientation image analysis errors.
- [[kang-2011-fiber-distribution-uhsc-flexural-strength]] — Profs. Su-Tae Kang & Bang Yeon Lee: landmark on fiber orientation and flexural strength.
- [[choi-2016-fiber-orientation-uhpcc-post-cracking-tensile]] — Prof. Bang Yeon Lee: landmark on the 3D fiber orientation tensile model.
- [[high-strength-strain-hardening-composites]] — ultra-high-performance composite system.
