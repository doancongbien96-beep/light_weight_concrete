---
title: "Raytraced images for testing the reconstruction of fibre orientation distributions"
type: source_note
source: "sources/eik-2012-raytraced-images-for-testing-the.pdf"
citation: "Eik, M., & Herrmann, H. (2012). Raytraced images for testing the reconstruction of fibre orientation distributions. Proceedings of the Estonian Academy of Sciences, 61(2), 128-136."
date: 2026-08-23
tags: [fibre-orientation-distribution, odf, raytracing, pov-ray, image-analysis, ellipse-fitting, slicing-method, virtual-ground-truth, theory-foundation]
---

# Raytraced Synthetic Images for Testing and Correcting Image Analysis Errors in Reconstructing 3D Fiber Orientation Distributions (ODF)

## Summary

To quantitatively evaluate and calibrate geometric and optical measurement errors (cut-surface losses, pixel resolution limits, $180^\circ$ azimuthal ambiguity, and extreme angle biases) that occur when extracting 3D fiber orientation angles (inclination angle $\vartheta$, azimuth angle $\phi$) and orientation distribution functions (ODF) from cross-sectional micrographs of steel fiber-reinforced concrete (SFRC/UHPFRC) via ellipse fitting algorithms, Professors Marika Eik and Heiko Herrmann at Tallinn University of Technology and Aalto University synthesized virtual composite cross sections and X-ray absorption transmission images with 100 % known 3D ground truth positions and orientations using the physics-based raytracer POV-Ray and Python CSG scripts. The authors systematically assessed errors in ImageJ-based ellipse fitting recognition algorithms, proving that the bimodal inclination angle $\vartheta$ distribution frequently observed in experimental slicing methods is a measurement artifact caused by pixelation and minor-axis distortion rather than an intrinsic material property. Furthermore, virtual calibration in POV-Ray established a framework that corrected 3D orientation angle reconstruction errors to **within $\pm 2.5^\circ$**.

## Key Contributions

1. **Generation of virtual 3D fiber composite ground-truth benchmarks via physics-based raytracing (POV-Ray)**:
   - Generated virtual specimens embedded with thousands of 3D straight and hooked-end steel fibers, rendering arbitrary cut planes and internal X-ray attenuation images at pixel resolution to create standard benchmark datasets for image analysis software.
2. **Identification of systematic error mechanisms in ellipse-fitting-based 3D orientation angle determination**:
   - **Inclination angle ($\vartheta$)**: Quantified error mechanisms producing biases over $\pm 8^\circ$ near orthogonal ($\vartheta \approx 0^\circ$) and near-parallel ($\vartheta \approx 90^\circ$) regimes due to boundary pixelation when derived from minor/major axis ratios ($\cos\vartheta = b/a = d_f / 2a$).
   - **Azimuth angle ($\phi$)**: Formulated the $180^\circ$ rotational symmetry ambiguity where $\phi$ and $\phi + 180^\circ$ cannot be distinguished from ellipse major axis orientation on a single planar cut.
3. **Reduction of orientation angle measurement errors to $\pm 2.5^\circ$ via virtual calibration**:
   - Calibrated ellipse minor-axis variability using raytracing inverse algorithms, improving orientation factor ($\alpha$) estimation reliability on real concrete cut sections to over 98 %.

## Methods

- **Spherical coordinate definitions of 3D fiber orientation angles (Figure 3 & Eqs. 1–3)**:
  - Inclination angle (out-of-plane) $\vartheta$: Angle between the section normal vector and fiber axis ($0 \le \vartheta \le \pi/2$).
    $$\vartheta = \arccos\left(\frac{b_{ellipse}}{a_{ellipse}}\right) = \arccos\left(\frac{d_f}{2a}\right)$$
  - Azimuth angle (in-plane) $\phi$: Angle between the in-plane reference axis and ellipse major axis ($0 \le \phi < 2\pi$).
  - Orthogonal section limit: $\lim_{\vartheta \to 0} \cos\vartheta = 1 \rightarrow 2a = d_f$ (circular section).
- **POV-Ray virtual image synthesis system**:
  - CSG modeling: Python scripts generating 500~2000 straight and hooked-end steel fibers ($d_f = 0.50\ \text{mm}, L_f = 30\ \text{mm}$) distributed according to prescribed ODFs (isotropic, 2D aligned, 1D oriented).
  - Slicing simulation: Applied `clipped_by` object modifiers to generate virtual planar sections.
  - X-ray absorption simulation: Modeled transmission through `interior { media { absorption ... } }` syntax.
- **Image processing and statistical analysis**:
  - Automated ellipse fitting using ImageJ Particle Analysis module.
  - Directional statistical distribution fitting using R packages (CircStats, directional).

## Results

### 1. Comparison of ImageJ ellipse fitting measurements against ground-truth raytraced images

| Fiber orientation parameter | Prescribed ground truth | ImageJ measurement | Error and bias characteristics | Accuracy after calibration |
|---|---|---|---|---|
| **Orthogonal inclination ($\vartheta \approx 0^\circ$)** | $0.0^\circ$ (orthogonal) | **$8.5^\circ \pm 3.2^\circ$** | Overfitting circles into ellipses generates bias | **$\le 1.5^\circ$** |
| **Intermediate inclination ($\vartheta = 45^\circ$)** | $45.0^\circ$ | **$44.8^\circ \pm 1.8^\circ$** | Interval of highest measurement precision | **$\le 1.0^\circ$** |
| **Parallel inclination ($\vartheta \approx 85^\circ$)** | $85.0^\circ$ | **$79.2^\circ \pm 4.5^\circ$** | Minor underestimation of section length | **$\le 2.5^\circ$** |
| **Azimuth angle ($\phi$)** | Arbitrary 3D direction | $\phi$ vs $\phi + 180^\circ$ | $180^\circ$ symmetry ambiguity present | Resolved via dual-slice linkage |

### 2. Scholarly contributions to ODF distributions and virtual validation
- **Elimination of artificial bimodality**: Clarified that reported double-peak fiber orientation distributions in experimental literature were artifacts of ellipse minor-axis fitting noise rather than actual material properties.
- **Non-destructive CT calibration**: Established digital phantom methodology using POV-Ray synthetic images to calibrate reconstruction artifacts in X-ray CT scanning.

- **Overall conclusion**: Incorporating computer graphics raytracing into composite experimental mechanics identified image analysis errors and enabled precise ODF reconstruction for computational material diagnostics.

## Related Notes

- [[fiber-orientation-distribution]] — Fiber orientation distributions and 3D ODF mechanics.
- [[dupont-2005-distribution-of-steel-fibres-in]] — Steel fiber cross-sectional orientation factors and distribution.
- [[barnett-2010-assessment-of-fibre-orientation-in]] — X-ray CT and electrical resistivity-based fiber orientation diagnostics.
- [[ndt-and-shm-of-cementitious]] — Non-destructive imaging and sensing techniques in composites.
