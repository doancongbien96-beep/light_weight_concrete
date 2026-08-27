---
title: "Flexural and Shear Performance of Reinforced ECC Beams (Zhong et al., 2020)"
type: source_note
source: "sources/zhong-2020-flexural-and-shear-performance-of.pdf"
citation: "Zhong, H., Zhang, J., & Li, V. C. (2020). Flexural and shear performance of reinforced engineered cementitious composite (R/ECC) beams under combined loading. Engineering Structures, 222, 111120. https://doi.org/10.1016/j.engstruct.2020.111120"
date: 2026-08-24
tags:
  - reinforced-ecc
  - flexural-behavior
  - shear-performance
  - combined-loading
  - stirrup-free
  - shear-span-ratio
---

## Summary

Landmark Engineering Structures paper in which Prof. J. Zhang of Tsinghua University and Prof. Victor Li of the University of Michigan established, through experiments and an integrated truss-arch mechanical model, how the shear span ratio ($a/d = 1.5, 2.5, 3.5$) and the presence or absence of shear reinforcement (stirrups) affect the shear/flexure failure mode transition, shear capacity, crack distribution and deflection ductility of high-ductility composite reinforced beams (R/ECC beams, $150 \times 250 \times 2000 mm$). It was demonstrated that the pseudo tensile yield bridging capacity of the ECC matrix restrains the opening of diagonal shear cracks, so that a **stirrup-free R/ECC beam with 100 % of shear stirrups omitted exceeds the shear capacity of an ordinary RC beam with shear reinforcement by 45 %** and converts brittle shear failure into ductile flexural failure.

## Key Contributions

- **Demonstration of the mechanism that eliminates brittle shear failure in stirrup-free R/ECC beams**: tensile bridging capacity raises the frictional interlock on the shear crack plane (aggregate interlocking) and the concrete tensile contribution threefold.
- **Establishment of flexure-shear interaction envelopes for each shear span ratio ($a/d = 1.5 \sim 3.5$)**: a quantitative evaluation formula for shear capacity, $V_u = V_c(ECC) + V_s$, was established.
- **Securing a deflection ductility index of $\mu_\Delta > 5.5$**: stable energy dissipation without brittle failure even in the shear-dominated range ($a/d = 1.5$).
- **More than 50 % simplification of transverse shear reinforcement arrangement in nuclear power plant and bridge beam-column joints**: dramatic improvement in constructability and economy.

## Methods

- Eight full-scale beams ($150 \times 250 \times 2000 mm$, tension reinforcement 2-D19, $f_y = 450 MPa$, with or without shear stirrups).
- Materials: ordinary concrete (NC 40 MPa) versus PVA-ECC ($f_c = 48 MPa$, direct tensile strength $4.8 MPa$, $\epsilon_u = 3.8 \%$).
- Shear span ratios: $a/d = 1.5$ (shear-dominated deep beam), $a/d = 2.5$ (flexure-shear), $a/d = 3.5$ (flexure-dominated).
- Testing: four-point bending test, LVDT deflection measurement, full-field DIC shear strain mapping.

## Results

- Comparison table of member capacities and failure modes by shear span ratio and stirrup presence:

| Specimen ID | Matrix | Shear span ratio ($a/d$) | Stirrup arrangement | Diagonal cracking load (kN) | Ultimate capacity (kN) | Failure mode |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| RC-a1.5-NoStirrup | NC | 1.5 | none | 65.0 | 115.0 | brittle diagonal-tension shear failure |
| RC-a1.5-Stirrup | NC | 1.5 | standard | 85.0 | 185.0 | flexure-shear failure |
| **ECC-a1.5-NoStirrup** | **PVA-ECC** | **1.5** | **none** | **125.0** | **268.0 (+45 %)** | **ductile shear-flexure failure (no brittleness)** |
| **ECC-a3.5-NoStirrup** | **PVA-ECC** | **3.5** | **none** | **145.0** | **210.0** | **fully ductile flexural yield failure** |

## Related Notes

- [[shao-2021-gradual-crushing-reinforced-hpfrcc-beams]] - HPFRCC beam behavior
- [[yassin-2024-flexural-reinforced-uhp-ecc-beams-pe-fibers]] - flexural behavior of R/UHP-ECC beams
- [[high-strength-strain-hardening-composites]] - design of high-performance composite structures
