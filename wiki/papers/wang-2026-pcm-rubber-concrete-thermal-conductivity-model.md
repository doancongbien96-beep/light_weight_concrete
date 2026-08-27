---
title: "Multicomponent Optimization and Thermal Conductivity Model of PCM Rubber Concrete (Wang et al., 2026)"
type: source_note
source: "sources/wang-2026-multicomponent-optimization-design-and-thermal.pdf"
citation: "Wang, Y., Mia, M. S., Kim, H. K., & Lee, B. Y. (2026). Multicomponent optimization design and thermal conductivity model of PCM-rubber composite concrete for building energy conservation. Cement and Concrete Composites, 166, 105980."
date: 2026-08-24
tags:
  - pcm-rubber-concrete
  - thermal-conductivity-model
  - multi-objective-optimization
  - microencapsulated-pcm
  - energy-conservation
  - building-insulation
---

## Summary
A 2026 latest study by Professor Bang Yeon Lee's research team at Chonnam National University that establishes a multiphase predictive model for the effective thermal conductivity of composite thermal-energy-storage concrete (PCM-RuC) hybridly incorporating waste-tire rubber powder (10 ~ 30 vol %) and microencapsulated phase change material (MPCM, 10 ~ 30 vol %) as a multicomponent system, and designs genetic-algorithm-based multi-objective optimal mixes to simultaneously optimize building-envelope insulation (low thermal conductivity), thermal storage (high latent heat capacity), and impact-absorbing ductility. A modified Maxwell-Eucken three-phase thermal conduction model was established, reducing the composite's thermal conductivity by 60 % to $0.35 W/(m\cdot K)$ while achieving an effective latent heat of **35.0 J/g** and a compressive strength of 28.5 MPa.

## Key Contributions
- **Theoretical model for the effective thermal conductivity ($k_{eff}$) of the rubber-MPCM three-phase porous composite completed**: a closed-form predictive equation combining the low thermal conductivity of rubber with the latent heat storage effect of MPCM ($R^2 = 0.98$).
- **Dual energy-saving synergy of insulation and thermal storage clarified**: indoor peak temperature mitigated by $4.8 °C$ and building heating/cooling energy reduced by 45 %.
- **Strength-thermal-property balance point derived through multi-objective optimization (NSGA-II)**: structural exterior wall panel criteria satisfied at rubber 15 vol % + MPCM 20 vol %.
- **Fusion of waste-tire upcycling and zero-energy construction**: substantial reduction in life-cycle carbon emissions.

## Methods
- Matrix: OPC ($W/C = 0.38$), rubber powder ($d = 1.0 mm$), paraffin MPCM ($T_m = 26 °C$, $\Delta H = 150 J/g$).
- Thermal and mechanical testing: Hot Disk TPS thermal conductivity, DSC latent heat, 28 d compressive strength, continuous temperature measurement in a full-scale insulated-wall simulation chamber.

## Results
- Thermophysical and mechanical property measurement table for the PCM-rubber composite concretes:

| Mix ID | Rubber fraction (vol %) | MPCM fraction (vol %) | 28 d compressive strength (MPa) | Thermal conductivity ($W/(m\cdot K)$) | Effective latent heat $\Delta H$ ($J/g$) | Chamber peak temperature reduction ($°C$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Control | 0 % | 0 % | 52.5 | 0.88 | 0.0 | reference |
| RuC-20 | 20 % | 0 % | 36.0 | 0.52 | 0.0 | $-1.5 °C$ |
| MPCM-20 | 0 % | 20 % | 38.5 | 0.58 | 28.5 | $-3.2 °C$ |
| **PCM-RuC-Opt** | **15 %** | **20 %** | **28.5** | **0.35** | **35.0** | **$-4.8 °C$** |

## Related Notes
- [[mia-2026-thermal-properties-cement-embedded-mpcm]] - MPCM cement thermophysical properties
- [[tang-2025-pcm-concrete-energy-storage]] - PCM concrete thermal energy storage technology review
- [[bompa-2017-experimental-constitutive-modelling-rubberised-concrete]] - rubberised concrete mechanics
