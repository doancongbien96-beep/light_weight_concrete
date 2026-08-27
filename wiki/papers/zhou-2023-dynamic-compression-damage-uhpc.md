---
title: "Dynamic Compressive Behavior and Damage Constitutive Model of UHPC (Zhou et al., 2023)"
type: source_note
source: "sources/zhou-2023-dynamic-compressive-behavior-and-damage.pdf"
citation: "Zhou, X., Zhang, S., & Chen, Y. (2023). Dynamic compressive behavior and damage constitutive model of ultra-high performance concrete (UHPC). International Journal of Impact Engineering, 178, 104610. https://doi.org/10.1016/j.ijimpeng.2023.104610"
date: 2026-08-24
tags:
  - uhpc
  - dynamic-compression
  - split-hopkinson-pressure-bar
  - damage-constitutive-model
  - steel-fiber
  - impact-energy
---

## Summary
To clarify the dynamic compressive failure mechanism of ultra-high performance concrete (UHPC, $f_c = 150 MPa$, hooked/straight steel fibers $V_f = 2.0 \sim 3.0 \%$) under explosion and hypervelocity projectile impact loading, this study employed a large-diameter 100 mm split Hopkinson pressure bar (SHPB) to determine experimentally the dynamic compressive stress-strain curves at high strain rates ($\dot{\epsilon} = 30 \sim 200 s^{-1}$), the dynamic compressive strength increase factor ($DIF_c$), the deformation energy absorption capacity, and the fragment size distribution of failure (Weibull distribution), and established a viscoelastic-plastic dynamic damage constitutive model. At a strain rate of $180 s^{-1}$, the dynamic compressive strength reached **265.0 MPa** ($DIF_c = 1.77$) and a dynamic energy absorption density of **$8.2 MJ/m^3$** was achieved.

## Key Contributions
- **Completion of a nonlinear viscoelastic-plastic damage constitutive equation dedicated to UHPC under hypervelocity compression**: establishment of a model combining strain rate sensitivity with a steel fiber bridging damage variable.
- **Establishment of a precise calculation formula for the dynamic compressive DIF**: $DIF_c = 1.0 + 0.0042 \dot{\epsilon}^{0.75}$ ($R^2 = 0.98$).
- **Weibull statistical modeling of the fragment size distribution after fragmentation**: the average fragment diameter increased by more than five times with increasing steel fiber content, suppressing fragmentation-type spalling.
- **Establishment of computational simulation parameters for blast- and impact-resistant design of protective facilities**: verification of the accuracy of the LS-DYNA MAT_159 model.

## Methods
- Specimens: $100 \times 50 mm$ cylindrical specimens ($f_c = 150 MPa$, steel fiber $V_f = 2.0, 2.5, 3.0 \%$).
- SHPB system: high-strength steel pressure bars of 100 mm diameter (incident bar 6.0 m, transmitted bar 4.0 m), with a pulse shaper applied.
- Test rates: $\dot{\epsilon} = 35, 75, 125, 180 s^{-1}$.

## Results
- Dynamic compressive mechanical property data of UHPC by strain rate:

| Strain rate $\dot{\epsilon}$ ($s^{-1}$) | Quasi-static compressive strength (MPa) | Dynamic compressive strength (MPa) | Dynamic increase factor $DIF_c$ | Dynamic failure strain $\epsilon_{cd}$ | Dynamic energy absorption density ($MJ/m^3$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Quasi-static ($10^{-4} s^{-1}$) | 150.0 | 150.0 | 1.00 (baseline) | 0.0045 | 0.85 |
| $35 s^{-1}$ | 150.0 | 185.0 | 1.23 | 0.0085 | 2.10 |
| $75 s^{-1}$ | 150.0 | 215.0 | 1.43 | 0.0125 | 4.25 |
| $125 s^{-1}$ | 150.0 | 242.0 | 1.61 | 0.0165 | 6.10 |
| **$180 s^{-1}$** | **150.0** | **265.0** | **1.77 (+77 %)** | **0.0210 (+366 %)** | **8.20 (+865 %)** |

## Related Notes
- [[zhang-2023-dynamic-compressive-uhp-ecc]] - dynamic compressive properties of UHP-ECC
- [[impact-and-blast-resistance-frcc]] - design theory of impact-resistant protective composites
- [[high-strength-strain-hardening-composites]] - mechanics of ultra-high-strength composites