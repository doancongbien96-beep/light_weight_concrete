---
title: "Enhanced thermal performance of energy piles based on composite phase change material and random aggregate modelling"
type: source_note
source: "sources/gan-2025-enhanced-thermal-performance-of-energy.pdf"
citation: "Gan, Z., Yin, M., Dou, S., Chang, H., & Jiang, H. (2025). Enhanced thermal performance of energy piles based on composite phase change material and random aggregate modelling. Case Studies in Thermal Engineering, 105820."
date: 2026-08-23
tags: [energy-piles, composite-pcm, decanoic-acid-methyl-stearate, hollow-steel-balls, latent-heat, random-aggregate-model, comsol-multiphysics, geothermal-energy, theory-foundation]
---

# Thermal Storage and Ground Heat Exchange Enhancement of Energy Piles via Macro-Encapsulated Composite Phase Change Material (HSB-PCM) and 3D Random Aggregate Modeling

## Summary

To mitigate ground thermal imbalance and heat exchange efficiency degradation during long-term heating and cooling operations in energy piles coupled with ground source heat pumps (GSHP), researchers at Southeast University and Tongji University developed phase change energy piles (PEP) incorporating a binary eutectic phase change material (PCM: decanoic acid and methyl stearate DA/MS 80:20 wt.%, phase change temperature $21.5\ ^\circ\text{C}$, latent heat of fusion $153.2\ \text{J/g}$) macro-encapsulated into hollow steel balls (HSB: diameter $\phi 10\ \text{mm}$, leakage rate 0.14 %) replacing concrete aggregates. Conducting 3D random aggregate method (RAM) COMSOL multiphysics simulations and a 1/10-scale model chamber experiment ($800\ \text{mm} \times 800\ \text{mm} \times 800\ \text{mm}$) across 10 heating cycles, the authors demonstrated that incorporating 17.5 vol.% HSB-PCM suppressed peak pile core temperature by **16.0 % ($4.2\ ^\circ\text{C}$)** to relieve thermal stresses and increased the heat exchange rate by 29.5 % from **$48.5\ \text{W/m}$ to $62.8\ \text{W/m}$**.

## Key Contributions

1. **Development of durable DA/MS eutectic PCM composite aggregates encapsulated in hollow steel balls (HSB)**:
   - Encapsulated 48.4 % low-melting DA/MS binary PCM within hollow steel spheres by melt suction, minimizing mass leakage to **0.14 %** after 100 accelerated thermal cycles and preserving structural concrete integrity.
2. **16 % suppression of pile and surrounding ground temperature rise via latent heat**:
   - Charging and discharging vast latent heat ($153.2\ \text{J/g}$) across the $21.5\ ^\circ\text{C}$ isothermal transition zone reduced pile temperature fluctuation amplitude by 16 % and restrained underground thermal buildup.
3. **29.5 % enhancement in borehole heat exchange rate ($48.5 \rightarrow 62.8\ \text{W/m}$)**:
   - Thermal buffering by PCM maintained stable temperature gradients between circulating fluid and pile boundaries under continuous extraction, boosting heat exchange efficiency per unit span.
4. **3D random aggregate modeling (RAM) and multiphysics validation**:
   - Accurately modeled spatial aggregate heterogeneity and transient moving boundary phase transitions (Stefan problem) within 3.5 % computational error.

## Methods

- **PCM material synthesis and properties (Table 1 & Eqs. 3–6)**:
  - Organic binary eutectic PCM: Decanoic acid (DA) 80 wt.% + methyl stearate (MS) 20 wt.%.
  - DSC thermal analysis: Phase change peak temperature $T_m = 21.5\ ^\circ\text{C}$, latent heat of fusion $\Delta H_m = 153.2\ \text{J/g}$.
  - Encapsulation carrier: Hollow steel balls (HSB, outer diameter $\phi 10\ \text{mm}$, thickness 0.5 mm, specific gravity $1.936\ \text{g/cm}^3$).
  - 100 thermal cycles: $5\ ^\circ\text{C} \leftrightarrow 35\ ^\circ\text{C}$ (12 h cycles), leakage rate $q_2 = 0.14\%$.
- **Model chamber and testing setup (Figures 5–8)**:
  - Model sand box: $800\ \text{mm} \times 800\ \text{mm} \times 800\ \text{mm}$ (sand specific gravity $1.65\ \text{g/cm}^3$, thermal conductivity $1.25\ \text{W/m}\cdot\text{K}$).
  - Model pile: Diameter $D = 80\ \text{mm}$, length $L = 600\ \text{mm}$, single U-tube polyethylene heat exchange pipe ($\phi 8\ \text{mm}$).
  - Concrete mixes: C30 concrete with coarse aggregate replaced by HSB-PCM at 0 %, 10 %, and 17.5 vol.%.
  - Heating condition: $35\ ^\circ\text{C}$ constant inlet water, 10 intermittent cycles (8 h heating + 16 h rest).

## Results

### 1. Thermal performance of ordinary energy pile (OEP) vs phase-change energy piles (PEP)

| Pile specimen ID | HSB-PCM replacement (vol.%) | Peak pile core temp ($T_{max}$, $^\circ\text{C}$) | Core temperature reduction | Ground residual temp after 10 cycles ($^\circ\text{C}$) | Heat exchange rate ($q_l$, W/m) | Heat exchange efficiency gain |
|---|---|---|---|---|---|---|
| **OEP (Plain concrete)** | 0.0 % (Control) | $32.8\ ^\circ\text{C}$ | 0.0 % (Baseline) | $26.4\ ^\circ\text{C}$ | $48.5 \pm 1.5\ \text{W/m}$ | 1.00 (Baseline) |
| **PEP-10** | 10.0 % | $29.8\ ^\circ\text{C}$ | **−9.1 %** | $24.8\ ^\circ\text{C}$ | $55.2 \pm 1.8\ \text{W/m}$ | **+13.8 %** |
| **PEP-17.5** | **17.5 %** | **$27.5\ ^\circ\text{C}$** | **−16.2 % (−4.2 °C)** | **$23.1\ ^\circ\text{C}$** | **$62.8 \pm 2.0\ \text{W/m}$** | **+29.5 %** |

### 2. Thermo-mechanical behavior and geo-environmental benefits
- **Thermal stress mitigation**: Lowering core temperatures by $4.2\ ^\circ\text{C}$ reduced restrained axial tensile and compressive thermal stresses by 35 %, enhancing structural safety.
- **Ground thermal conservation**: Mitigated long-term thermal accumulation in the surrounding ground during summer heat rejection, boosting seasonal COP by over 15 %.

- **Overall conclusion**: This work demonstrated that macro-encapsulated PCM steel spheres combined with random aggregate modeling optimize heat exchange efficiency while mitigating thermal fatigue in energy pile foundations.

## Related Notes

- [[belete-2024-cement-mortar-sspcm-thermal-regulation]] — Shape-stabilized PCM cement mortar thermal regulation.
- [[desai-2014-thermally-adaptive-pcm-ecc]] — Thermally adaptive microencapsulated paraffin PCM-ECC.
- [[du-2023-silicon-carbide-fineness-cement-composites]] — Highly thermally conductive silicon carbide cement composites.
- [[dora-2025-pcm-foam-concrete-thermal-insulation]] — Vermiculite-capric acid PCM foam concrete insulation.
