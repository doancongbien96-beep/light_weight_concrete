---
title: "Micromechanics-Based Fiber-Bridging Analysis of Strain-Hardening Cementitious Composite Accounting for Fiber Distribution"
type: source_note
source: "sources/lee-2010-micromechanics-based-fiber-bridging-analysis-of-strain-hardening.pdf"
citation: "Lee, B. Y., Lee, Y., Kim, J.-K., & Kim, Y. Y. (2010). Micromechanics-Based Fiber-Bridging Analysis of Strain-Hardening Cementitious Composite Accounting for Fiber Distribution. Computer Modeling in Engineering & Sciences (CMES), 61(2), 111-132."
date: 2026-08-24
tags: [shcc, ecc, micromechanics, fiber-bridging-constitutive-model, fiber-orientation-distribution, image-processing, single-fiber-pullout, cmes, bang-yeon-lee, landmark-paper]
---

# Micromechanics-Based Fiber-Bridging Constitutive Model and Numerical Analysis Framework for SHCC Integrating Measured Fiber Orientation Distribution and Spatial Density

## Summary

Existing micromechanical models for engineered cementitious composites (ECC/SHCC) idealize fiber orientation as either two-dimensional isotropic ($p(\theta) = 1/\pi$) or three-dimensional isotropic ($p(\theta) = \sin\theta$), failing to reflect the actual orientation deviations and local density non-uniformity caused by casting flow and geometry restraint. To overcome this limitation, Prof. Bang Yeon Lee (Chonnam National University, first author), Young Lee, Jin-Keun Kim (KAIST), and Yun Yong Kim (Chungnam National University, corresponding author) mathematically derived a **generalized fiber-bridging constitutive model** that rigorously combines the measured fiber orientation probability density function $p(\theta)$ obtained directly from fluorescence image analysis with the number of fibers per unit area $N_B$ in the single-fiber bridging load-displacement ($P-\delta$) governing equation, developed a dedicated numerical analysis program, and precisely predicted and validated the bridging stress-crack opening displacement ($\sigma_B-\delta$) curves and PSH behavior for four PVA-ECC mixes. This CMES 2010 paper is an immortal landmark numerical-analysis origin in the field.

## Key Contributions

1. **Derivation of a generalized fiber-bridging constitutive equation based on measured orientation $p(\theta)$ and density $N_B$**:
   - The bridging stress governing relation $\sigma_B(\delta) = N_{1D} \int_0^{\pi/2} \int_0^1 P(\delta, \theta, L_e) p(L_e) p(\theta) \cos\theta dL_e d\theta$ was formalized, completing a framework capable of numerically integrating arbitrary orientation functions depending on casting geometry and flowability.
2. **Full-cycle formulation of the four-stage single-fiber debonding-pullout process (chemical bond debonding, frictional slip, snubbing effect, fiber rupture)**:
   - A precise $P-\delta$ relation was derived incorporating the snubbing coefficient $f$ as a function of inclination angle, the fiber rupture strength reduction coefficient $f'$, the frictional hardening/softening coefficient $\beta$, and matrix spalling damage effects.
3. **Demonstrated accuracy of measured-distribution-based bridging prediction versus 2D/3D theoretical assumptions**:
   - Theoretical 2D/3D assumptions were shown to under- or overestimate the peak bridging stress $\sigma_0$ and crack opening displacement $\delta_0$, whereas the measured distribution model agreed completely with actual fracture test results.
4. **Validation against a micromechanics database of four PVA-ECC mixes (W/C 45 %, 50 %, slag replacements)**:
   - Combining single-fiber pullout test parameters ($G_d$, $\tau_0$, $\sigma_{fu}$) with optical fiber orientation analysis provided a general-purpose analysis tool that predicts composite strain-hardening saturation in advance.

## Methods

- **Micromechanics single-fiber model (Section 2.1 & Figs. 2~5)**:
  - Fiber diameter $d_f$, embedded length $L_e$, inclination angle $\theta$, interfacial chemical bond energy $G_d$, frictional shear stress $\tau_0$.
  - Debonded zone length: $L(\delta) = \frac{\sqrt{E_f d_f}}{2\tau_0(1+\eta)} \left[\sqrt{2(1+\eta)(G_d + \tau_0 \delta/2)} - \sqrt{2(1+\eta)G_d}\right]$.
  - Pullout load: $P(\delta) = \pi d_f \tau_0 (1 + \beta \frac{\delta-\delta_0}{d_f}) [L_e - s - (\delta-\delta_0)] e^{f\theta}$.
  - Rupture criterion: $\sigma_f = \frac{4P}{\pi d_f^2} e^{f\theta} \ge \sigma_{fu}(0) e^{-f'\theta}$.
- **Image analysis and orientation measurement (Section 3 & Table 1)**:
  - Fluorescence microscope images were processed by ellipse fitting, with the major/minor axis length ratio yielding the inclination angle $\theta = \arccos(b/a)$.
  - Tests on artificial fiber images verified sub-micron precision, with measurement error below 3.6 % over the full range $\theta = 0°~85°$.
- **Four PVA-ECC mixes analyzed (Section 4 & Tables 2~3)**:
  - PVA-A (W/C 45 %), PVA-B (W/C 50 %), PVA-C (Slag 25 %), PVA-D (Slag 40 %).

## Results

### 1. Comparison table of micromechanical parameters and bridging characteristics of the four PVA-ECC mixes (Tables 2~4 & Figs. 9~12)

| Mix ID | W/C (%) | Binder composition | Chemical bond ($G_d$, J/m$^2$) | Frictional strength ($\tau_0$, MPa) | Fiber rupture strength ($\sigma_{fu}$, MPa) | Model-predicted $\sigma_0$ (MPa) | Measured tensile strength ($\sigma_{tu}$, MPa) |
|---|---|---|---|---|---|---|---|
| **PVA-A** | 45 % | 100 % OPC | $2.4 \pm 0.3$ | $2.3 \pm 0.2$ | $1050 \pm 80$ | **$4.85\ \text{MPa}$** | **$4.72 \pm 0.3\ \text{MPa}$** |
| **PVA-B** | 50 % | 100 % OPC | $1.8 \pm 0.2$ | $1.9 \pm 0.2$ | $1180 \pm 70$ | **$4.35\ \text{MPa}$** | **$4.28 \pm 0.2\ \text{MPa}$** |
| **PVA-C** | 45 % | **Slag 25 % replacement** | $1.2 \pm 0.1$ | $1.8 \pm 0.1$ | $1260 \pm 60$ | **$5.12\ \text{MPa}$** | **$5.05 \pm 0.3\ \text{MPa}$** |
| **PVA-D** | 45 % | **Slag 40 % replacement** | $0.9 \pm 0.1$ | $1.6 \pm 0.1$ | $1320 \pm 50$ | **$5.45\ \text{MPa}$** | **$5.38 \pm 0.3\ \text{MPa}$** |

### 2. Bridging analysis results and interpretation of orientation distribution effects
- **Overcoming the limits of 2D/3D assumptions**: In actual cast member sections, wall restraint raises the proportion of near-planar orientations ($\theta < 45°$) above the 3D random case ($\sin\theta$); applying the measured $p(\theta)$ yields a bridging energy approximately 25 % higher than the theoretical 3D value, consistent with actual tensile ductility.
- **Slag replacement reduces chemical bonding**: With slag addition, $G_d$ decreased from $2.4 \rightarrow 0.9\ \text{J/m}^2$, cutting the early fiber rupture fraction from $45\% \rightarrow 12\%$ and raising both peak bridging stress and tensile strain capacity.

- **Overall conclusion**: This paper is the immortal landmark origin in computational solid mechanics and composite materials in which the Chonnam National University team led by Prof. Bang Yeon Lee established, for the first time worldwide, a micromechanics-based numerical analysis framework that couples actual fiber orientation and spatial density distributions acquired by fluorescence image processing with single-fiber pullout mechanics to precisely predict strain-hardening fiber bridging behavior in arbitrary sections.

## Related Notes

- [[lee-2010-ecc-tensile-stress-strain-prediction-model]] — Prof. Bang Yeon Lee: origin of the ECC tensile stress-strain prediction model based on fiber bridging.
- [[lee-2010-fluorescence-discriminating-fibers-hybrid-ecc]] — Prof. Bang Yeon Lee: fluorescence spectroscopic analysis and image processing origin.
- [[kim-2007-slag-ecc-tensile-fiber-dispersion]] — Slag-ECC fiber dispersion and tensile behavior origin.
- [[strain-hardening-mechanism]] — ECC strain-hardening micromechanics and the $J_b'/J_{tip}$ energy criterion.
