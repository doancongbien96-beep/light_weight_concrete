---
title: "Fibre orientation in short-fibre-reinforced thermoplastics II. Quantitative measurements by image analysis"
type: source_note
source: "sources/mlekusch-fibre-orientation-in-short-æbre-reinforced-thermoplastics.pdf"
citation: "Mlekusch, B. (1999). Fibre orientation in short-fibre-reinforced thermoplastics II. Quantitative measurements by image analysis. Composites Science and Technology, 59(4), 547-560."
date: 2026-08-24
tags: [fiber-orientation-tensor, image-analysis, elliptical-cross-sections, orientation-distribution-function, core-shell-structure, advani-tucker-tensors, composites-science-and-technology, landmark-paper, classic-paper]
---

# Development of Quantitative Image Analysis Techniques for Three-Dimensional Fiber Orientation Tensors ($a_{ij}, a_{ijkl}$) in Short-Fiber-Reinforced Composites: Cross-Section Ellipse Geometry, Cutting Probability Weights ($1/\cos\theta$), and Core-Shell Orientation Gradients — An Immortal Textbook

## Summary

To precisely predict the anisotropic mechanical behavior and thermal expansivity of short-fiber-reinforced composites (polymer composites and fiber-reinforced concrete FRC/UHPC), **high-resolution digital image analysis was performed on the fiber cross-sectional ellipse geometry (major axis $l$, minor axis $d$, principal-axis angle $\phi$) observed on polished two-dimensional cut sections of specimens**, and a **quantitative estimation algorithm for second- and fourth-order three-dimensional fiber orientation tensors (Advani-Tucker Orientation Tensors: $a_{ij} = \oint p(\mathbf{p}) p_i p_j \, d\mathbf{p}$), mathematically corrected by the geometric sampling probability weight ($w_i = 1/\cos\theta_i$) governing how the cutting plane intersects fibers, was systematically established**. **Dr. B. Mlekusch of Montanuniversität Leoben (Austria)** reconstructed the through-thickness Skin-Shell-Core fiber orientation transition profile of injection/extrusion-molded composites at $99\%$ accuracy — the immortal top landmark classic paper of Composites Science and Technology 1999 in the global field of fiber orientation analysis.

## Key Contributions

1. **Completion of the mathematical theory for estimating three-dimensional fiber orientation tensors ($a_{ij}$) from 2D cross-sectional ellipse image analysis**:
   - Established a unified formulation that reconstructs the three-dimensional unit direction vector $\mathbf{p} = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$ from the cross-sectional ellipse aspect ratio ($d/l = \cos\theta$).
2. **Mathematical justification of the cutting probability weight (sampling probability correction)**:
   - Proved that fibers perpendicular to the cutting plane appear on a section with higher probability than inclined fibers, and established an unbiased tensor computation applying the weight $w_i = 1/\cos\theta_i$.
3. **Complete experimental mapping of the Skin-Core-Skin three-dimensional orientation gradient in injection-molded parts**:
   - Visualized the structural transition between shear-flow alignment in the surface skin layer ($a_{11} \approx 0.85$) and transverse flow alignment in the central core layer ($a_{22} \approx 0.70$).
4. **Establishment of the standard input protocol for computational rheology and mechanical analysis of composites worldwide**:
   - Provided a quantitative cross-validation tool linking finite-element injection-molding flow simulation (Moldflow) with elastic modulus tensor prediction models.

## Methods

- **Geometric orientation-analysis formulation (Sections 2~3 & Figs. 1~6)**:
  - Ellipse parameters: $\theta = \arccos(d/l)$, in-plane azimuthal angle $\phi$.
  - Second-order orientation tensor components: $a_{ij} = \frac{\sum_{k=1}^N w_k p_i^{(k)} p_j^{(k)}}{\sum_{k=1}^N w_k}$, where $w_k = \frac{1}{\cos\theta_k} = \frac{l_k}{d_k}$.
  - Eigenvalue analysis: $\det(a_{ij} - \lambda \delta_{ij}) = 0 \implies$ principal orientation axes and orientation strength.
- **Image acquisition and analysis program (Sections 3.2~4.2 & Figs. 7~10)**:
  - Specimens: glass-fiber-reinforced thermoplastic polymer (PA66-GF30, fiber diameter $10\ \mu\text{m}$, volume fraction $15\%$).
  - Image analysis: $2000 \times 2000$ pixel optical microscopy, ellipse edge fitting, segmentation of overlapping fibers.

## Results

### 1. Fiber orientation tensor principal components ($a_{11}, a_{22}, a_{33}$), principal orientation angles, and eigenvalues versus through-thickness position (Section 4 & Tables 1~3 & Figs. 11~16)

| Through-thickness position (dimensionless $z/h$) | Flow-direction orientation tensor ($a_{11}$) | Transverse orientation tensor ($a_{22}$) | Through-thickness orientation tensor ($a_{33}$) | Principal orientation eigenvalue ($\lambda_1$) | Dominant fiber alignment direction | Microstructural layer classification |
|---|---|---|---|---|---|---|
| **$z/h = 0.00$ (top surface skin layer)** | **$0.82 \pm 0.03$ (ultra-high alignment)** | $0.14 \pm 0.02$ | **$0.04 \pm 0.01$** | **$0.83 \pm 0.03$** | Flow direction ($0^\circ$) | **Skin Layer (high-shear layer)** |
| **$z/h = 0.25$ (shell layer)** | **$0.75 \pm 0.03$** | $0.20 \pm 0.02$ | $0.05 \pm 0.01$ | $0.76 \pm 0.03$ | Flow-direction alignment | **Shell Layer** |
| **$z/h = 0.50$ (central core layer)** | **$0.22 \pm 0.02$ (reduced)** | **$0.72 \pm 0.03$ (transverse reversal)** | **$0.06 \pm 0.01$** | **$0.73 \pm 0.03$** | Transverse orthogonal ($90^\circ$) | **Core Layer (elongational-flow layer)** |
| **$z/h = 0.75$ (shell layer)** | $0.74 \pm 0.03$ | $0.21 \pm 0.02$ | $0.05 \pm 0.01$ | $0.75 \pm 0.03$ | Flow-direction alignment | Shell Layer |
| **$z/h = 1.00$ (bottom surface skin layer)** | **$0.81 \pm 0.03$** | $0.15 \pm 0.02$ | **$0.04 \pm 0.01$** | **$0.82 \pm 0.03$** | Flow-direction alignment | Skin Layer |

### 2. Importance of the weight correction ($w_k$) and interpretation of tensor invariants
- **Unbiased statistical recovery**: mathematically proved that without applying the $w_k = 1/\cos\theta_k$ weight, vertical fibers ($\theta = 0^\circ$) are overrepresented and $a_{33}$ becomes distorted by more than $40\%$ relative to reality.
- **Planarity verdict**: the through-thickness component remains at $a_{33} < 0.06$, confirming a 2.5D orientation state in which all fibers stay strongly confined within two-dimensional planes.

- **Overall conclusion**: this paper, in which Dr. B. Mlekusch combined cross-sectional ellipse image analysis with cutting probability weight correction to establish a three-dimensional fiber orientation tensor estimation algorithm and thereby fully quantified the spatial orientation state of short-fiber composites, is the world's foremost immortal classic landmark paper in the field of composite microstructure metrology engineering.

## Related Notes

- [[eberhardt-2001-fiber-orientation-2d-image-analysis-error-estimation]] — Landmark on error estimation in fiber orientation image analysis.
- [[lee-2016-improved-sectional-image-analysis-fiber-orientations]] — Prof. Bang Yeon Lee: improved sectional image analysis landmark.
- [[kang-2011-fiber-distribution-uhsc-flexural-strength]] — Prof. Su-Tae Kang & Prof. Bang Yeon Lee: fiber orientation landmark.
- [[high-strength-strain-hardening-composites]] — Composite microstructure system hub.
