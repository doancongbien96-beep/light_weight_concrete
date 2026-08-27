---
title: "Gradual Crushing of Reinforced HPFRCC Beams under Flexure (Shao & Billington, 2021)"
type: source_note
source: "sources/shao-2021-gradual-crushing-of-steel-reinforced.pdf"
citation: "Shao, X., & Billington, S. L. (2021). Gradual crushing of steel-reinforced engineered cementitious composite beams under flexure. ASCE Journal of Structural Engineering, 147(4), 04021020. https://doi.org/10.1061/(ASCE)ST.1943-541X.0002958"
date: 2026-08-24
tags:
  - hpfrcc-beams
  - gradual-crushing
  - compressive-strain-capacity
  - flexural-ductility
  - high-reinforcement-ratio
  - seismic-design
---

## Summary
To fundamentally prevent the premature brittle compression crushing of the compression-zone concrete that arises when reinforced concrete (RC) flexural members are detailed with high-strength reinforcement or an over-reinforced ratio ($\rho_s > \rho_b$), the research team of Professor Sarah Billington at Stanford University employed a ductile fiber-reinforced cementitious composite (HPFRCC / ECC, uniaxial compressive strain capacity $\epsilon_{cu} > 0.015$) and elucidated, through precise experiments and section-integration analysis, the flexural behavior of full-scale R/HPFRCC beams, the gradual plastic crushing mechanism of the compression zone (Gradual Crushing), and the moment–curvature envelopes — a landmark paper in the ASCE Journal of Structural Engineering. It demonstrated that even under over-reinforced conditions the entire compression zone gradually absorbs plastic deformation without brittle failure, exhibiting a deflection ductility index $\mu_\Delta > 6.5$.

## Key Contributions
- **World-first elucidation of the gradual compressive crushing mechanism**: PVA fiber bridging restrained the unstable propagation of compression-shear cracks, gently controlling the softening slope in compression.
- **Complete elimination of brittle failure in over-reinforced beams ($\rho_s = 2.5 \sim 4.0 \%$)**: flexural ductility improved 3.5-fold over normal concrete even at high reinforcement ratios.
- **Establishment of a nonlinear compressive constitutive law for HPFRCC**: completed a section moment–curvature ($M-\phi$) design model reflecting an envelope compressive strain capacity $\epsilon_{cu} = 0.018$.
- **Realization of simplified transverse confinement reinforcement detailing in seismic plastic hinges and column–beam joints**: demonstrated the potential for a 50 % reduction in transverse reinforcement.

## Methods
- 8 large flexural specimens ($150 \times 250 \times 2400 mm$, span 2000 mm, tensile reinforcement ratios $\rho = 1.2 \%, 2.4 \%, 3.6 \%$).
- Materials: normal concrete (NC 45 MPa) versus PVA-HPFRCC ($f_c = 55 MPa$, tensile strain capacity $3.5 \%$, compressive failure strain $0.016$).
- Four-point bending tests, DIC full-field strain tensor mapping, and precision measurement with miniature strain gauges on the top compression zone.

## Results
- Comparative flexural performance and failure mode data by reinforcement ratio:

| Specimen ID | Matrix | Reinforcement ratio $\rho$ (%) | Yield load (kN) | Ultimate load (kN) | Deflection at failure (mm) | Displacement ductility index $\mu$ | Compression-zone failure aspect |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| NC-R1.2 | Normal concrete | 1.2 % | 82.5 | 115.4 | 32.5 | 3.25 | Ordinary flexural failure |
| NC-R3.6 | Normal concrete | 3.6 % (over-reinforced) | 165.0 | 178.2 | 18.5 | 1.45 (brittle) | Compressive concrete crushing/spalling |
| ECC-R1.2 | PVA-ECC | 1.2 % | 95.0 | 138.5 | 68.5 | 6.80 | Ultra-ductile multiple cracking |
| **ECC-R3.6** | **PVA-ECC** | **3.6 % (over-reinforced)** | **185.0** | **245.0** | **54.0** | **5.40** | **Gradual plastic crushing (no crushing/spalling)** |

## Related Notes
- [[yassin-2024-flexural-reinforced-uhp-ecc-beams-pe-fibers]] - flexural behavior of R/UHP-ECC beams
- [[high-strength-strain-hardening-composites]] - high-strength composite structural design
- [[pseudo-strain-hardening-criteria]] - PSH micromechanics theory
