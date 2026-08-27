---
title: "Theoretical Evaluation of Fiber Orientation and Tensile Behavior of ECC with Specimen Thickness (Lu et al., 2017)"
type: source_note
source: "sources/Theoretical evaluation of fiber ECC.pdf"
citation: "Lu, C., Leung, C. K. Y., & Li, V. C. (2017). Theoretical evaluation of fiber orientation and tensile behavior of engineered cementitious composites with specimen thickness. Construction and Building Materials, 150, 482-491. https://doi.org/10.1016/j.conbuildmat.2017.06.012"
date: 2026-08-24
tags:
  - fiber-orientation
  - specimen-thickness-effect
  - 2d-3d-transition
  - bridging-constitutive-law
  - pva-ecc
  - micromechanics
---

## Summary

This is the origin paper in which Professor Christopher Leung's team at Hong Kong University of Science and Technology elucidated, with a geometric probability model and experiments, the size effect that the relative ratio of member thickness ($t$) to fiber length ($L_f$) ($t/L_f = 0.5 \sim 5.0$) exerts on the transition of fiber orientation from 2D in-plane alignment to 3D spatial isotropy (2D-to-3D Orientation Transition), on the crack-plane fiber bridging constitutive law ($\sigma-\delta$), and on the uniaxial direct-tension strain-hardening envelope of PVA-ECC members. Thin members ($t/L_f \le 1.0$) develop a 2D alignment coefficient of $\alpha_\theta = 0.78$ owing to the mold wall effect, so that direct tensile strength is measured **55 %** higher and ultimate tensile strain capacity **75 %** higher than in thick members ($t/L_f \ge 3.0$, $\alpha_\theta = 0.50$); this thickness-dependence mechanism is formalized mathematically.

## Key Contributions

- **Formalization of the 3D fiber orientation probability density function $p(\theta, t)$ accounting for member thickness $t$**: boundary-layer analysis completed for the 3D isotropic core zone and the 2D constrained zone along the surface walls.
- **Establishment of closed-form integrals for the thickness-dependent bridging peak stress $\sigma_0(t)$ and complementary energy $J_b'(t)$**: a model of the size effect whereby ductility degrades as specimen thickness increases.
- **Proposal of a standard thickness guideline for tension test specimens**: a thickness correction factor ($K_{thick}$) formula presented for the safe design of full-scale structural members.
- **Precise verification against experimental data**: 95 % agreement confirmed with tensile test results of specimens 6, 13, 25, and 50 mm thick.

## Methods

- Mix: PVA-ECC (Kuraray REC15, $V_f = 2.0 \%$, $L_f = 12 mm$, $d_f = 39 \mu m$, $W/B = 0.45$, $FA/C = 1.2$).
- Specimen thickness variables: dogbone specimens of thickness $t = 6 mm$ ($t/L_f = 0.5$), $13 mm$ ($t/L_f = 1.08$), $25 mm$ ($t/L_f = 2.08$), $50 mm$ ($t/L_f = 4.17$).
- Tests: dogbone direct tension ($0.5 mm/min$, DIC full-field strain analysis) and elliptical analysis of polished cross sections under the microscope.

## Results

- Fiber orientation coefficient and tensile property data by specimen thickness:

| Specimen thickness $t$ (mm) | Thickness ratio $t/L_f$ | Effective orientation coefficient $\alpha_\theta$ | First cracking strength (MPa) | Ultimate tensile strength (MPa) | Ultimate tensile strain capacity (%) | Bridging complementary energy $J_b'$ ($J/m^2$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| 6 mm (thin plate) | 0.50 | **0.82** | 3.85 | **5.85** | **4.85** | **42.5** |
| 13 mm (standard) | 1.08 | **0.72** | 3.50 | **4.95** | **3.65** | **31.2** |
| 25 mm (intermediate) | 2.08 | **0.58** | 3.25 | **4.10** | **2.50** | **21.5** |
| 50 mm (block) | 4.17 | **0.51** | 3.10 | **3.75** | **1.85** | **15.8** |

## Related Notes

- [[fiber-orientation-distribution]] — theory of fiber orientation distribution
- [[kang-2009-fiber-bridging-pdf-ecc]] — fiber bridging probability distribution model
- [[pseudo-strain-hardening-criteria]] — PSH micromechanics theory
