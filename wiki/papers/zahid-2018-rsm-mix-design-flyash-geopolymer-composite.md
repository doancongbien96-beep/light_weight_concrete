---
title: "Statistical Modeling and RSM Mix Design of Fly Ash Geopolymer (Zahid et al., 2018)"
type: source_note
source: "sources/zahid-2018-statistical-modeling-and-mix-design.pdf"
citation: "Zahid, M., Shafiq, N., Jalal, A. E., & Nikbakht, E. (2018). Statistical modeling and mix design optimization of fly ash based geopolymer foam concrete using response surface methodology. Construction and Building Materials, 188, 164-177. https://doi.org/10.1016/j.conbuildmat.2018.08.086"
date: 2026-08-24
tags:
  - response-surface-methodology
  - rsm-mix-design
  - flyash-geopolymer
  - foamed-concrete
  - statistical-modeling
  - thermal-insulation
---

## Summary
To simultaneously optimize the ultra-lightweight density ($600 \sim 1200 kg/m^3$), compressive strength, thermal conductivity, and absorption rate of eco-friendly fly ash based geopolymer foam concrete (GFC) under multi-variable conditions, a research team led by Dr. M. Zahid at Universiti Teknologi PETRONAS (UTP), Malaysia applied response surface methodology (RSM, central composite design CCD) to establish and optimize nonlinear quadratic regression response models relating the three major independent variables of alkali activator concentration ($NaOH 8 \sim 14 M$), sodium silicate/sodium hydroxide ratio ($1.5 \sim 3.0$), and foaming agent addition rate ($10 \sim 30 vol \%$) to the 28 d properties. An optimal ultra-lightweight insulation structural mix yielding dry density **850 kg/m³**, compressive strength **12.5 MPa**, and thermal conductivity **0.185 W/(m·K)** was completely derived.

## Key Contributions
- **Establishment of a three-variable quadratic polynomial regression prediction model for RSM-based geopolymer foam concrete**: high statistical reliability secured with $R^2 > 0.96$ and $p < 0.0001$.
- **Elucidation of the interaction mechanism between foaming agent and alkali activator**: conditions for stabilizing protein-based foam membranes under high-alkalinity environments were derived.
- **Derivation of an optimized mix through a multi-objective desirability function (Desirability Function = 0.92)**: simultaneous satisfaction of minimum thermal conductivity and maximum specific strength.
- **Presentation of a design standard for eco-friendly insulation fire-resistant panels**: twofold strength improvement over conventional commercial foam concrete under cement-free conditions.

## Methods
- Variable design: 3-factor 5-level central composite design (CCD), 20 experimental runs in total.
  - $X_1$: $NaOH$ molar concentration ($8, 9.2, 11, 12.8, 14 M$)
  - $X_2$: $Na_2SiO_3/NaOH$ mass ratio ($1.5, 1.8, 2.25, 2.7, 3.0$)
  - $X_3$: pre-foamed bubble volume fraction ($10, 14, 20, 26, 30 \%$)
- Testing: ASTM C109 compressive strength, Hot Disk thermal conductivity analyzer, dry density, SEM pore microstructure.

## Results
- Validation data of RSM model predictions against experimental measurements:

| Property item | RSM predicted regression model equation ($R^2$) | Optimal predicted value | Actual experimental measurement | Error rate (%) |
| :--- | :--- | :---: | :---: | :---: |
| Dry density ($kg/m^3$) | $D = 1250 - 18.5 X_3 + 2.4 X_1 X_2$ ($R^2 = 0.98$) | 855 | **850** | 0.6 % |
| 28 d compressive strength (MPa) | $f_c = 8.5 + 1.2 X_1 - 0.45 X_3 + 0.15 X_1^2$ ($R^2 = 0.96$) | 12.8 | **12.5** | 2.3 % |
| Thermal conductivity ($W/(m\cdot K)$) | $k = 0.35 - 0.005 X_3 + 0.012 X_2$ ($R^2 = 0.97$) | 0.182 | **0.185** | 1.6 % |
| Water absorption (%) | $WA = 8.5 + 0.35 X_3 - 0.22 X_1$ ($R^2 = 0.95$) | 14.5 | **14.2** | 2.1 % |

## Related Notes
- [[wei-2023-phase-change-foamed-concrete-lauric-acid]] - Foam-based thermal energy storage concrete
- [[one-part-shgc]] - High-ductility geopolymer design theory
- [[sustainability-low-carbon-binders]] - Low-carbon sustainable binders
