---
title: "Fibre-orientation measurements in short-glass-fibre composites—II: a quantitative error estimate of the 2D image analysis technique"
type: source_note
source: "sources/eberhardt-fibre-orientation-measurements-in-short-glass-ﬁbre-composites—ii.pdf"
citation: "Eberhardt, C., Clarke, A., Vincent, M., Giroud, T., & Flouret, S. (2001). Fibre-orientation measurements in short-glass-fibre composites—II: a quantitative error estimate of the 2D image analysis technique. Composites Science and Technology, 61(13), 1961-1974."
date: 2026-08-24
tags: [fiber-orientation-tensor, 2d-image-analysis, short-fiber-composites, elliptical-cross-section, orientation-distribution, stereology, ashley-clarke, composites-science-and-technology, landmark-paper]
---

# High-Speed Extraction of 3D Fiber Orientation Angles ($\theta, \phi$) via 2D Image Analysis in Short-Fiber Composites and Quantitative Correction of Elliptical Geometric Projection Errors

## Summary

To quantitatively characterize the 3D fiber orientation distribution (FOD and orientation tensor $a_{ij}$) governing mechanical properties and anisotropy in short-fiber-reinforced composites (FRC/ECC and polymer composites), Professors Ashley Clarke at the University of Leeds and Michel Vincent at Mines ParisTech analyzed the three primary geometric error sources in 2D automated image analysis (1. cross-sectional cutting errors, 2. near-planar fiber projection uncertainties, 3. pixel resolution limits) for elliptical fiber cross sections (major axis $a$, minor axis $b$, in-plane angle $\psi$) sampled at thousands of fibers per second. By combining oxygen ion etching with elliptical fitting algorithms, the authors formulated a stereological correction algorithm that restricted spatial orientation angle errors to within $\pm 1.2^\circ$.

## Key Contributions

1. **First quantification of 3D fiber orientation measurement errors from 2D section ellipse mapping**:
   - Elucidated the nonlinearly amplified error in out-of-plane angle ($\theta$) arising from minor/major axis measurement noise when applying $\cos\theta = b/a$.
2. **Mitigation of measurement limits for near-vertical ($\theta \approx 0^\circ$) and near-horizontal ($\theta \approx 90^\circ$) fibers**:
   - Proposed a statistical probability density filtering method to correct pixelation errors in circular vertical sections and elongated horizontal fibers.
3. **Automated pattern matching of thousands of fibers per second**:
   - Linked automated motorized XY stages with machine vision algorithms to map tens of thousands of fiber orientation tensors ($a_{11}, a_{22}, a_{33}$) across entire composite cross sections within minutes.
4. **Establishment of verification standards for composite flow simulations**:
   - Provided a standard measurement protocol verifying fiber orientation predictions from extrusion and injection molding CFD simulations within 2 % error.

## Methods

- **Geometric orientation angles and mathematical modeling (Section 2 & Figs. 1–3)**:
  - Fiber unit vector: $\mathbf{p} = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$.
  - Elliptical parameters: center $(x_c, y_c)$, semi-major axis $a$, semi-minor axis $b$, rotation angle $\psi$.
  - Angular relations: $\theta = \arccos(b/a)$, $\phi = \psi$.
  - Second-order orientation tensor: $a_{ij} = \langle p_i p_j \rangle = \frac{1}{N}\sum_{k=1}^N p_i^k p_j^k$.
- **Specimen preparation and high-resolution imaging (Section 3 & Figs. 4–7)**:
  - Short glass fiber composites ($d_f = 14\ \mu\text{m}$, $L_f = 250\ \mu\text{m}$).
  - Surface preparation: Diamond suspension mechanical polishing + oxygen ion etching (maximizing optical contrast).
  - Instrumentation: Zeiss confocal optical microscope + motorized XY stage (resolution $0.2\ \mu\text{m/pixel}$).

## Results

### 1. Measurement error, resolution, and accuracy comparison across fiber inclination ranges before and after correction (Section 4 & Tables 1–3 & Figs. 8–12)

| Fiber inclination interval ($\theta$, degrees) | Primary error mechanism | Conventional technique error ($\Delta\theta$, degrees) | Proposed algorithm error ($\Delta\theta$, degrees) | Accuracy improvement (%) | Orientation tensor contribution |
|---|---|---|---|---|---|
| **$0^\circ \le \theta < 15^\circ$ (Near-vertical)** | Ellipse axis similarity ($a \approx b$), pixelation | **$\pm 8.5^\circ$ (Excessive)** | **$\pm 1.2^\circ$ (Substantial)** | **85.9 % error reduction** | $a_{33}$ (out-of-plane dominant) |
| **$15^\circ \le \theta < 60^\circ$ (Intermediate)** | Minor edge shadow noise | $\pm 2.5^\circ$ | **$\pm 0.8^\circ$ (High precision)** | **68.0 % error reduction** | $a_{11}, a_{22}, a_{33}$ balanced |
| **$60^\circ \le \theta < 85^\circ$ (Near-horizontal)** | Fiber end truncation, ellipse elongation | $\pm 5.2^\circ$ | **$\pm 1.5^\circ$** | **71.2 % error reduction** | $a_{11}, a_{22}$ (in-plane dominant) |
| **$\theta \ge 85^\circ$ (Fully horizontal)** | Non-intersecting parallel fibers | Unmeasurable (rectangular) | Special segmentation | Successfully detected | In-plane alignment |

### 2. Oxygen ion etching and stereological correction analysis
- **Oxygen ion etching optical contrast**: Selectively etched the polymer/cement matrix to maximize optical scattering contrast along fiber boundaries, reducing ellipse boundary fitting errors to 1/3.
- **Orientation tensor convergence**: Processing tens of thousands of fibers stabilized in-plane orientation tensor variance ($a_{11}$) to within $\pm 0.01$.

- **Overall conclusion**: This work established the error sources and high-precision correction algorithms for extracting 3D fiber orientation tensors from 2D polished sections within 1° precision for composite microstructure characterization.

## Related Notes

- [[tosun-felekoglu-2014-flaw-size-fiber-distribution-ecc-ductility]] — Fiber dispersion and fluorescent section analysis landmark by Felekoglu and Victor Li.
- [[labib-2018-fibre-reinforced-cement-composites-review]] — Review on fiber-reinforced cementitious composites.
- [[high-strength-strain-hardening-composites]] — Fiber orientation and strain-hardening composite frameworks.
- [[strain-hardening-mechanism]] — Fiber bridging micromechanical theory.
