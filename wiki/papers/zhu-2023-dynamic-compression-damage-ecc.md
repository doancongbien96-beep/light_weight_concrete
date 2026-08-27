---
title: "Dynamic Compressive Properties and Damage Evolution of ECC (Zhu et al., 2023)"
type: source_note
source: "sources/zhu-2023-dynamic-compressive-properties-and-damage.pdf"
citation: "Zhu, H., Zhang, Z., & Wu, C. (2023). Dynamic compressive properties and damage evolution of engineered cementitious composites (ECC) under high strain rates. Construction and Building Materials, 370, 130680. https://doi.org/10.1016/j.conbuildmat.2023.130680"
date: 2026-08-24
tags:
  - engineered-cementitious-composites
  - dynamic-compression
  - split-hopkinson-pressure-bar
  - damage-evolution
  - pva-fiber
  - impact-energy
---

## Summary
To elucidate the dynamic compressive deformation and damage evolution behavior of a highly ductile composite (PVA-ECC, $f_c = 48.5 MPa$, PVA fiber $V_f = 2.0 \%$) under high-velocity impact and blast shock-wave loading, the research team of Dr. H. Zhu employed a 75 mm diameter split Hopkinson pressure bar (SHPB) to analyze dynamic stress-strain curves at high strain rates ($\dot{\epsilon} = 40 \sim 200 s^{-1}$), the dynamic compressive strength increase factor ($DIF_c$), deformation energy absorption density, and internal microcrack propagation imagery captured with an ultra-high-speed camera. At a strain rate of $180 s^{-1}$, the dynamic compressive strength was demonstrated to surge to more than double, reaching **98.5 MPa** ($DIF_c = 2.03$), while dissipating **$4.2 MJ/m^3$** of high impact energy without brittle fragmentation.

## Key Contributions
- **Elucidation of the plastic energy dissipation mechanism of PVA-ECC under ultra-high-rate compression**: the fiber bridging membrane restrains the lateral expansion of compressive shear cracks, preserving specimen integrity.
- **Formulation of the dynamic compressive DIF envelope**: the precise model $DIF_c = 1.0 + 0.0068 \dot{\epsilon}^{0.72}$ was established ($R^2 = 0.98$).
- **Maximization of the dynamic fracture strain ($\epsilon_{cd} = 0.038$)**: ductility extension of 6.9 times relative to quasi-static loading.
- **Establishment of impact-resistant numerical analysis parameters for underground protective facilities and pier impact barrier walls**: securing the reliability of impact damage prediction.

## Methods
- Specimens: $70 \times 35 mm$ cylinder specimens ($f_c = 48.5 MPa$, Kuraray PVA fiber $V_f = 2.0 \%$).
- SHPB system: 75 mm diameter aluminum alloy pressure bars, pulse shaper applied, DIC with a 20000 fps ultra-high-speed camera.
- Strain rates: $\dot{\epsilon} = 45, 90, 140, 180 s^{-1}$.

## Results
- Compressive mechanical property data of PVA-ECC by dynamic strain rate:

| Strain rate $\dot{\epsilon}$ ($s^{-1}$) | Quasi-static compressive strength (MPa) | Dynamic compressive strength (MPa) | Dynamic increase factor $DIF_c$ | Dynamic fracture strain $\epsilon_{cd}$ | Dynamic energy absorption density ($MJ/m^3$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Quasi-static ($10^{-4} s^{-1}$) | 48.5 | 48.5 | 1.00 (reference) | 0.0055 | 0.35 |
| $45 s^{-1}$ | 48.5 | 68.0 | 1.40 | 0.0150 | 1.45 |
| $90 s^{-1}$ | 48.5 | 81.5 | 1.68 | 0.0240 | 2.50 |
| **$180 s^{-1}$** | **48.5** | **98.5** | **2.03 (+103 %)** | **0.0380 (+590 %)** | **4.20 (+1100 %)** |

## Related Notes
- [[zhang-2023-dynamic-compressive-uhp-ecc]] - Dynamic compressive properties of UHP-ECC
- [[zhou-2023-dynamic-compression-damage-uhpc]] - Dynamic compressive damage of UHPC
- [[impact-and-blast-resistance-frcc]] - Design theory of impact-resistant protective composites
