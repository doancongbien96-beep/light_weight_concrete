---
title: "Evaluation of Fiber Bridging Law in ECC Considering Fiber Orientation Probability Distribution (Kang et al., 2009)"
type: source_note
source: "sources/DJP1109N_보강 섬유의 배향각에.pdf"
citation: "Kang, S. T., Lee, B. Y., Kim, J. K., & Kim, Y. Y. (2009). Evaluation of fiber bridging law in engineered cementitious composites considering fiber orientation probability distribution. Journal of the Korea Concrete Institute, 21(5), 629-637. https://doi.org/10.4334/JKCI.2009.21.5.629"
date: 2026-08-24
tags:
  - fiber-bridging-constitutive-law
  - fiber-orientation
  - probability-density-function
  - pva-ecc
  - micromechanics
  - crack-bridging-stress
---

# Evaluation of Fiber Bridging Law in ECC Considering Fiber Orientation Probability Distribution

## Summary

To accurately predict the crack bridging stress versus crack opening displacement relationship ($\sigma-\delta$ curve, Fiber Bridging Constitutive Law) across cracked planes in ductile cementitious composites (PVA-ECC), this theoretical paper by Professor Seung-Tae Kang, Professor Bang-Yeon Lee, Professor Jin-Keun Kim, and Professor Yun-Yong Kim derives a micromechanical constitutive model that integrates the 3D spatial fiber orientation probability density function ($p(\theta)$) and boundary wall effects, validated through polished cross-section image analysis and direct tension tests. The authors mathematically demonstrated that aligning fiber orientation parallel to the tensile axis increases the peak bridging stress $\sigma_0$ by up to 2.5-fold and substantially expands the complementary energy $J_b'$.

## Key Contributions

- **Closed-form integral solution of $\sigma-\delta$ incorporating fiber orientation PDF ($p(\theta) = \sin\theta / (1 - \cos\theta_{max})$)**: Resolved errors associated with assuming isotropic 3D random fiber distributions.
- **2D-to-3D orientation transition model based on boundary wall effects**: Formulated the effective orientation coefficient as a function of member thickness ($t$) and fiber length ($L_f$).
- **Quantification of PSH energy index ($J_b'/J_{tip}$) orientation dependency**: Increasing $\alpha_\theta$ from 0.5 to 0.85 enhanced pseudo-strain-hardening performance and stability by 3-fold.
- **Experimental validation against direct tension responses**: Achieved 95 % agreement between theoretical bridging predictions and experimental data over crack opening displacements of $0 \sim 2.0\ \text{mm}$ ($0 \sim 2.0 mm$).

## Methods

- **Theoretical formulation**: Formulated single fiber pullout bridging integrals incorporating snubbing friction coefficient $f$, matrix spalling/apparent strength reduction coefficient $f'$, chemical bond $G_d$, and frictional shear stress $\tau_0$.
- **Experimental validation**: PVA-ECC ($V_f = 2.0\%$, $W/B = 0.45$), direct tension dogbone tests, and optical microscopy measurement of fiber orientation angles on polished sections.

## Results

- Comparison of bridging parameters and tensile properties across fiber orientation conditions:

| Orientation Condition | Orientation Coefficient $\alpha_\theta$ | Peak Bridging Stress $\sigma_0$ (MPa) | Peak Opening $\delta_0$ (mm) | Complementary Energy $J_b'$ ($\text{J/m}^2$, $J/m^2$) | Tensile Strain Capacity (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 1D Fully Aligned ($0°$) | 1.00 | 7.85 | 0.85 | 45.2 | 6.50 |
| 2D In-plane Random (Thin plate) | 0.78 | 5.65 | 0.72 | 31.5 | 4.20 |
| 3D Spatial Random (Isotropic) | 0.50 | 3.85 | 0.55 | 18.2 | 2.10 |
| $90°$ Perpendicular Alignment | 0.20 | 1.45 | 0.25 | 4.5 | 0.45 (Softening) |

## Related Notes

- [[fiber-orientation-distribution]] — Theory of fiber orientation and dispersion in composites.
- [[kang-2008-fiber-orientation-djp0808]] — Effects of fiber orientation on SHCC mechanical properties.
- [[pseudo-strain-hardening-criteria]] — PSH micromechanical theory.
