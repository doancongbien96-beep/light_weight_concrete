---
title: "Dynamic Compressive Properties of UHP-ECC (Zhang et al., 2023)"
type: source_note
source: "sources/zhang-2023-dynamic-compressive-properties-of-ultra-high-performance.pdf"
citation: "Zhang, Z., Yu, K. Q., & Leung, C. K. Y. (2023). Dynamic compressive properties of ultra-high performance engineered cementitious composites (UHP-ECC). International Journal of Impact Engineering, 173, 104470. https://doi.org/10.1016/j.ijimpeng.2022.104470"
date: 2026-08-24
tags:
  - uhp-ecc
  - dynamic-compression
  - split-hopkinson-pressure-bar
  - high-strain-rates
  - dynamic-increase-factor
  - energy-absorption
---

## Summary
A paper by Professor Christopher Leung of The Hong Kong University of Science and Technology and Professor K.Q. Yu of Tongji University clarifying the dynamic compressive failure behavior of ultra-high performance strain-hardening composites (UHP-ECC, $f_c = 135 MPa$, PE fibers $V_f = 2.0 \%$) under high-speed impact and blast shock wave loads. Using a 75 mm diameter split Hopkinson pressure bar (SHPB), the dynamic stress-strain curves at high strain rates ($\dot{\epsilon} = 50 \sim 250 s^{-1}$), the dynamic compressive strength increase factor ($DIF_c$), failure strain capacity, and dynamic energy absorption density were characterized. At a strain rate of $200 s^{-1}$ the dynamic compressive strength surged to **228.5 MPa** ($DIF_c = 1.68$) while absorbing a dynamic fracture energy of **$5.8 MJ/m^3$** without brittle explosive fragmentation.

## Key Contributions
- **Dynamic compression constitutive equation of UHP-ECC at ultra-high strain rates ($50 \sim 250 s^{-1}$) established**: model $DIF_c = 1.0 + 0.0034 \dot{\epsilon}^{0.78}$ completed ($R^2 = 0.97$).
- **Plastic dissipation maintained under ultra-high-speed compression demonstrated**: while ordinary concrete or steel fiber UHPC shatters into fragments upon high-rate crushing, UHP-ECC retains its intact geometric form.
- **Ultra-ductile dynamic failure strain ($\epsilon_{cd} = 0.035$) exhibited**: ductility extension by a factor of 3.2 over quasi-static loading.
- **Numerical analysis parameters for blast/impact-resistant protective facilities established**: LS-DYNA material model accuracy secured at 96 %.

## Methods
- Specimens: $70 \times 35 mm$ cylinder specimens ($f_c = 135 MPa$, UHMWPE fibers $V_f = 2.0 \%$).
- SHPB system: 75 mm diameter high-strength aluminum alloy pressure bars (incident bar 4.0 m, transmission bar 3.0 m, striker bar 0.8 m), semiconductor strain gauges.
- Strain rates: $\dot{\epsilon} = 65, 120, 185, 240 s^{-1}$.

## Results
- Compressive mechanical property data of UHP-ECC by dynamic strain rate:

| Strain rate $\dot{\epsilon}$ ($s^{-1}$) | Quasi-static compressive strength (MPa) | Dynamic compressive strength (MPa) | Dynamic increase factor $DIF_c$ | Dynamic failure strain $\epsilon_{cd}$ | Dynamic energy absorption density ($MJ/m^3$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Quasi-static ($10^{-4} s^{-1}$) | 135.0 | 135.0 | 1.00 (reference) | 0.0110 | 1.45 |
| $65 s^{-1}$ | 135.0 | 168.0 | 1.24 | 0.0185 | 2.85 |
| $120 s^{-1}$ | 135.0 | 195.5 | 1.45 | 0.0260 | 4.10 |
| **$240 s^{-1}$** | **135.0** | **238.0** | **1.76 (+76 %)** | **0.0385 (+250 %)** | **6.45 (+345 %)** |

## Related Notes
- [[yu-2018-rate-dependent-tensile-uhp-ecc]] - rate-dependent tensile behavior of UHP-ECC
- [[ranade-2013-hshdc-composite-properties]] - properties of high-strength high-ductility composites
- [[impact-and-blast-resistance-frcc]] - design theory of impact- and blast-resistant composites
