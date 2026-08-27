---
title: "Dynamic Tensile Properties and Constitutive Modeling of HPFRCC (Zhou et al., 2021)"
type: source_note
source: "sources/zhou-2021-dynamic-tensile-properties-and-constitutive.pdf"
citation: "Zhou, Y., Chen, X., & Li, J. (2021). Dynamic tensile properties and constitutive modeling of high-performance fiber-reinforced cementitious composites. International Journal of Impact Engineering, 155, 103905. https://doi.org/10.1016/j.ijimpeng.2021.103905"
date: 2026-08-24
tags:
  - hpfrcc
  - dynamic-tensile-properties
  - strain-rate-effect
  - constitutive-model
  - pva-fiber
  - impact-energy
---

## Summary
A study by the research team of Professor Y. Zhou of Tongji University that elucidated, under high strain rate ($\dot{\epsilon} = 10^{-4} \sim 10^1 s^{-1}$) loading environments, the dynamic tensile strength increase, the transition of the strain-hardening envelope, and the fracture energy dissipation behavior of a ductile composite (PVA-HPFRCC, $f_c = 55 MPa$, quasi-static tensile strain capacity $4.0 \%$) by means of a split Hopkinson tensile bar (SHTB) and high-speed servo tensile testing, and established a dynamic visco-elastoplastic damage constitutive model. It was demonstrated that as the strain rate increased to $10^1 s^{-1}$, the direct tensile strength surged 2.2-fold from **5.1 MPa to 11.2 MPa** ($DIF_t = 2.20$) while maintaining a dynamic tensile strain capacity of **3.5 %**.

## Key Contributions
- **Establishment of a dynamic tensile damage constitutive model of HPFRCC under ultra-high strain rates ($10^{-4} \sim 10^1 s^{-1}$)**: formulation of a three-dimensional constitutive equation coupling the strain rate effect with interfacial frictional slip.
- **Analytical formulation of the tensile DIF envelope**: establishment of the precise model $DIF_t = 1.0 + 0.18 (\log_{10}(\dot{\epsilon}/\dot{\epsilon}_0))^{1.15}$ ($R^2 = 0.98$).
- **Attainment of a dynamic fracture energy density of $380 kJ/m^3$**: maximization of the capacity to absorb seismic and blast shock waves.
- **Verification of the rate dependence of multiple fine crack generation**: inertial confinement increased the number of cracks from 35 to 85 as the impact velocity increased.

## Methods
- Specimens: dogbone tensile specimens ($f_c = 55 MPa$, Kuraray PVA fiber $V_f = 2.0 \%$).
- Test equipment: 30 mm diameter high-strength titanium alloy SHTB tensile bar system and MTS high-speed actuator.
- Test rates: $\dot{\epsilon} = 10^{-4}, 10^{-2}, 1.0, 10^1 s^{-1}$.

## Results
- Direct tensile mechanical property data of the HPFRCC by strain rate:

| Strain rate $\dot{\epsilon}$ ($s^{-1}$) | First-cracking strength (MPa) | Ultimate direct tensile strength (MPa) | Dynamic increase factor $DIF_t$ | Ultimate tensile strain capacity (%) | Tensile fracture energy ($kJ/m^3$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $10^{-4} s^{-1}$ (quasi-static) | 3.65 | 5.10 | 1.00 (reference) | **4.20 %** | 185 |
| $10^{-2} s^{-1}$ | 4.85 | 6.80 | 1.33 | **4.05 %** | 240 |
| $1.0 s^{-1}$ | 6.50 | 9.20 | 1.80 | **3.80 %** | 310 |
| **$10^1 s^{-1}$ (high-speed impact)** | **7.85** | **11.20** | **2.20 (+120 %)** | **3.50 %** | **380 (+105 %)** |

## Related Notes
- [[zhang-2021-dynamic-tensile-ecc-intermediate-rates]] - dynamic tension of ECC at intermediate rates
- [[yu-2018-rate-dependent-tensile-uhp-ecc]] - high-rate tensile properties of UHP-ECC
- [[impact-and-blast-resistance-frcc]] - impact and blast resistant composite design theory
