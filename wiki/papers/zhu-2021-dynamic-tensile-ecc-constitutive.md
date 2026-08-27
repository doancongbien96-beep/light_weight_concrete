---
title: "Dynamic Tensile Behavior and Constitutive Model of ECC (Zhu et al., 2021)"
type: source_note
source: "sources/zhu-2021-dynamic-tensile-behavior-and-constitutive.pdf"
citation: "Zhu, H., Zhang, Z., & Wu, C. (2021). Dynamic tensile behavior and constitutive model of engineered cementitious composites (ECC) under high strain rates. International Journal of Impact Engineering, 151, 103830. https://doi.org/10.1016/j.ijimpeng.2021.103830"
date: 2026-08-24
tags:
  - dynamic-tensile-behavior
  - high-strain-rates
  - split-hopkinson-bar
  - constitutive-model
  - pva-ecc
  - impact-resistance
---

## Summary
A study by Professor C. Wu's research team at the University of Western Australia, Australia that precisely measured through a split Hopkinson tension bar (SHTB) the dynamic tensile behavior of ductile composites (PVA-ECC, $f_c = 48 MPa$, tensile strain capacity $4.0 \%$) in high-speed impact and blast environments ($\dot{\epsilon} = 10^{-4} \sim 50 s^{-1}$) and established a micromechanics-based dynamic viscoplastic damage constitutive equation. As the strain rate increased to $40 s^{-1}$, the dynamic direct tensile strength surged by a factor of 2.46 from **5.2 MPa to 12.8 MPa** ($DIF_t = 2.46$) while a dynamic tensile strain capacity of **3.6 %** and fracture energy of **$420 kJ/m^3$** were exhibited.

## Key Contributions
- **Dynamic constitutive equation of PVA-ECC under ultra-high tensile strain rates ($50 s^{-1}$) established**: integrating rate-dependent interfacial friction slip and inertial confinement effects.
- **Tensile DIF envelope formulated**: $DIF_t = 1.0 + 0.22 (\log_{10}(\dot{\epsilon}/\dot{\epsilon}_0))^{1.20}$ ($R^2 = 0.98$).
- **Ultra-high energy dissipation stability demonstrated**: dynamic tensile fracture energy improved by a factor of 2.4 over quasi-static loading.
- **Interpretation parameters for blast-resistant protective structures completed**: LS-DYNA nonlinear analysis accuracy secured at 96 %.

## Methods
- Specimens: dogbone tension specimens ($f_c = 48 MPa$, Kuraray PVA fibers $V_f = 2.0 \%$).
- Test equipment: 25 mm diameter aluminum alloy SHTB tension bar, high-speed laser displacement meters, 10000 fps ultra-high-speed camera DIC.
- Strain rates: $\dot{\epsilon} = 10^{-4}, 1.0, 15, 40 s^{-1}$.

## Results
- Direct tensile mechanical data of PVA-ECC by strain rate:

| Strain rate $\dot{\epsilon}$ ($s^{-1}$) | First-crack strength (MPa) | Ultimate direct tensile strength (MPa) | Dynamic increase factor $DIF_t$ | Ultimate tensile strain capacity (%) | Dynamic fracture energy ($kJ/m^3$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $10^{-4} s^{-1}$ (quasi-static) | 3.50 | 5.20 | 1.00 (reference) | **4.20 %** | 175 |
| $1.0 s^{-1}$ | 5.80 | 8.50 | 1.63 | **3.95 %** | 285 |
| $15 s^{-1}$ | 7.50 | 10.80 | 2.08 | **3.80 %** | 360 |
| **$40 s^{-1}$ (ultra-high-speed impact)** | **9.20** | **12.80** | **2.46 (+146 %)** | **3.60 %** | **420 (+140 %)** |

## Related Notes
- [[zhou-2021-dynamic-tensile-constitutive-hpfrcc]] - HPFRCC dynamic tensile constitutive model
- [[zhang-2021-dynamic-tensile-ecc-intermediate-rates]] - intermediate-rate ECC dynamic tension
- [[impact-and-blast-resistance-frcc]] - design theory of impact-resistant protective composites
