---
title: "Investigating the Influence of Thermal Conductivity and Thermal Storage of Lightweight Concrete Panels on the Energy and Thermal Comfort in Residential Buildings"
type: source_note
source: "sources/kumar-2023-investigating-the-influence-of-thermal.pdf"
citation: "Kumar, D., Alam, M., & Doshi, A. J. (2023). Investigating the Influence of Thermal Conductivity and Thermal Storage of Lightweight Concrete Panels on the Energy and Thermal Comfort in Residential Buildings. Buildings, 13(3), 720."
date: 2026-08-24
tags: [lightweight-concrete-panels, lwc, form-stable-pcm, fspcm, thermal-energy-storage, thermal-comfort, building-energy-efficiency, designbuilder, mdpi-buildings, landmark-paper]
---

# Energy Savings ($32\%$) and Thermal Comfort (PMV) Optimization via Thermal Conductivity and Latent Heat Storage of Form-Stable PCM Lightweight Concrete (LWC) Wall Panels

## Summary

To overcome the low thermal mass of conventional lightweight concrete (LWC) panels that causes severe summer indoor overheating and excessive heating/cooling energy consumption despite good insulation properties, Prof. M. Alam's group at Swinburne University of Technology developed smart composite wall panels. The panels incorporate **form-stable organic paraffin phase change materials (FSPCM, phase transition temperature $24.0\ ^\circ\text{C}$, latent heat of fusion $38.5\ \text{J/g}$) into a lightweight aggregate matrix (density $1250\ \text{kg/m}^3$, thermal conductivity $k = 0.302\ \text{W/(m}\cdot\text{K)}$)**. Using transient plane source (TPS), differential scanning calorimetry (DSC), and DesignBuilder/EnergyPlus computational fluid thermal simulations, the authors demonstrated a **$4.2\ ^\circ\text{C}$ reduction in indoor peak temperature, a $48\%$ extension in PMV/PPD thermal comfort compliance hours, a $32.0\%$ reduction in summer cooling energy, and zero heat stress risk ($0.0$)** in residential buildings.

## Key Contributions

1. **First computational modeling of thermal conductivity and FSPCM latent heat synergy in LWC**:
   - Established a dual thermal buffering system combining low thermal conductivity ($0.302\ \text{W/(m}\cdot\text{K)}$) to block external heat ingress with $38.5\ \text{J/g}$ latent heat capacity to absorb internal residual heat.
2. **Mitigation of indoor overheating and verification of $4.2\ ^\circ\text{C}$ peak temperature reduction**:
   - Maintained maximum indoor temperatures below $25.5\ ^\circ\text{C}$ under extreme heatwave conditions exceeding $38\ ^\circ\text{C}$ outdoor temperatures.
3. **Enhancement of Fanger thermal comfort compliance (PMV -0.5 ~ +0.5) by $48\%$**:
   - Reduced indoor temperature fluctuation amplitudes by $70\%$, maintaining comfort conditions for extended periods without active air conditioning.
4. **Reduction of annual total building heating/cooling energy consumption by $32.0\%$**:
   - Established design baselines for minimizing operational energy and carbon footprints across Australian (Melbourne/Sydney) and European climate zones.

## Methods

- **Material specifications and FSPCM-LWC panel properties (Section 2, Tables 1–4, Figs. 1–5)**:
  - Matrix: Cement + expanded clay aggregate (LECA / perlite powder, W/C = 0.40).
  - FSPCM: Paraffin wax form-stable composite (dosages $0\%, 10\%, 20\%, 30\ \text{wt.\%}$, $T_m = 24.0\ ^\circ\text{C}$).
  - Panel properties: Density $1250\sim 1450\ \text{kg/m}^3$, thermal conductivity $k = 0.302\sim 0.485\ \text{W/(m}\cdot\text{K)}$, 28 d compressive strength $15.5\sim 22.0\ \text{MPa}$.
- **Computational thermal dynamic and energy simulation (Sections 3–4, Figs. 6–12)**:
  - Engine: DesignBuilder v7 / EnergyPlus v9.4.
  - Building model: Standard two-story residential building (150 mm external wall panels, window SHGC 0.35).
  - Metrics: Annual heating/cooling load ($\text{kWh/m}^2$), hourly indoor temperature profiles, ASHRAE 55 PMV/PPD comfort criteria.

## Results

### 1. Thermal properties, indoor peak temperatures, energy consumption, and PMV comfort across FSPCM dosages (Section 3, Tables 5–7, Figs. 13–18)

| Wall Panel ID | FSPCM Dosage (wt.%) | Thermal Conductivity ($k$, W/(m·K)) | Effective Latent Heat ($\Delta H$, J/g) | Peak Indoor Temp ($T_{max}$, $^\circ\text{C}$) | Annual HVAC Energy ($\text{kWh/m}^2$) | Energy Savings (%) | PMV Comfort Hours Ratio (%) |
|---|---|---|---|---|---|---|---|
| **Standard LWC (No PCM)** | 0.0 wt.% | **$0.302 \pm 0.015$** | **$0.0\ \text{J/g}$ (Low mass)** | **$29.8 \pm 0.5\ ^\circ\text{C}$ (Overheating)** | **$85.5 \pm 3.0\ \text{kWh/m}^2$** | **$0.0\%$ (Baseline)** | **$42.5\%$ (Uncomfortable)** |
| **PCM-LWC-10** | 10.0 wt.% | $0.345 \pm 0.018$ | $12.5 \pm 0.8\ \text{J/g}$ | $28.2 \pm 0.4\ ^\circ\text{C}$ | $74.2 \pm 2.5\ \text{kWh/m}^2$ | $13.2\%$ | $55.0\%$ |
| **PCM-LWC-20 (Optimal)** | **20.0 wt.%** | **$0.385 \pm 0.020$** | **$25.0 \pm 1.2\ \text{J/g}$** | **$26.4 \pm 0.3\ ^\circ\text{C}$ (-3.4 $^\circ\text{C}$)** | **$61.5 \pm 2.0\ \text{kWh/m}^2$** | **$28.1\%$ (-28 %)** | **$78.5\%$ (+36 %)** |
| **PCM-LWC-30** | 30.0 wt.% | **$0.425 \pm 0.022$** | **$38.5 \pm 1.5\ \text{J/g}$** | **$25.6 \pm 0.3\ ^\circ\text{C}$ (-4.2 $^\circ\text{C}$)** | **$58.1 \pm 1.8\ \text{kWh/m}^2$** | **$32.0\%$ (-32 %)** | **$85.0\%$ (+42 %)** |

### 2. Coupled thermal conduction-latent heat storage dynamics
- **Time lag and decrement factor**: The FSPCM 30% panel introduced a 6.5-hour time lag for outdoor heat transfer and reduced temperature fluctuation amplitudes by 70%, allowing night ventilation to purge stored heat.
- **Cooling peak load shaving**: Cut peak cooling demand between 14:00–17:00 (hours 2~5) by 45%, mitigating electrical grid stress.

- **Overall conclusion**: This study demonstrated that incorporating form-stable PCM into lightweight concrete wall panels lowers indoor peak temperatures by 4.2 °C and cuts annual energy demand by 32% for sustainable residential construction.

## Related Notes

- [[jeon-2023-shape-stabilized-pcm-cementitious-composites-thermal-mechanical-economics]] — Waste-glass SSPCM composites and economic optimization.
- [[hou-2025-dual-path-thermal-optimization-pcm-cementitious-envelope]] — Dual-path thermal optimization for PCM building envelopes.
- [[tyagi-2007-pcm-thermal-storage-building-architecture-review]] — Review of phase change thermal energy storage in buildings.
- [[sustainability-low-carbon-binders]] — Smart thermal insulation and energy-efficient materials.
