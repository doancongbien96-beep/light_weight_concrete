---
title: "Experimental Study on the Structural Performance Degradation of Corrosion-Damaged Reinforced Concrete Beams"
type: source_note
source: "sources/jung-2019-experimental-study-on-the-structural.pdf"
citation: "Jung, J. S., Lee, B. Y., & Lee, K. S. (2019). Experimental Study on the Structural Performance Degradation of Corrosion-Damaged Reinforced Concrete Beams. Advances in Civil Engineering, 2019, 8493139."
date: 2026-08-24
tags: [rebar-corrosion, rc-beams, structural-performance-degradation, half-cell-potential, flexural-failure, shear-failure, seismic-capacity-reduction, bang-yeon-lee, hanyang-university, chonnam-national-university, theory-foundation]
---

# Quantitative Degradation Models for Flexural and Shear Capacities and Seismic Ductility Reduction Factor ($\eta$) in Corrosion-Damaged Reinforced Concrete (RC) Beams Based on Half-Cell Potential Differences ($\Delta V$)

## Summary

To accurately assess the residual seismic and structural safety of aging reinforced concrete (RC) buildings and bridges exposed to aggressive marine environments, Professor Bang Yeon Lee at Chonnam National University and Professor Kang Seok Lee at Hanyang University investigated the quantitative effects of rebar corrosion on RC beam capacity and ductility. The authors fabricated **16 full-scale RC beam specimens (8 flexure-critical and 8 shear-critical; cross-section $200\ \text{mm} \times 250\ \text{mm}$, clear span 1800 mm, total length 2200 mm)**, subjected them to accelerated corrosion using the impressed current technique, and mapped corrosion states across 24 surface nodes via half-cell potential measurements (ASTM C876). Through four-point bending tests, load-deflection responses, yield and ultimate strengths, ductility ratios, concrete spalling, and longitudinal rebar buckling were evaluated. As corrosion potential dropped from non-corroded conditions ($> -200\ \text{mV}$) to the >90 % corrosion probability regime ($-350\sim -550\ \text{mV}$), **the ultimate flexural capacity decreased by 28.5 % and displacement ductility plunged by 42.0 %**, while **shear capacity dropped by up to 35.2 % due to stirrup cross-sectional loss**, resulting in brittle failure. Based on these results, the authors formulated a non-destructive quantitative framework to estimate residual capacity reduction factors ($\eta$) directly from half-cell potential mapping.

## Key Contributions

1. **First 3D quantitative correlation between rebar corrosion, load capacity, and ductility**:
   - Established empirical regression models connecting half-cell potential differences to structural strength and ductility loss across 16 full-scale RC beams (8 flexure, 8 shear).
2. **Non-destructive structural assessment framework based on half-cell potential ($\Delta V$)**:
   - Proposed safety evaluation equations to predict residual flexural and shear capacities directly from 24-point ASTM C876 half-cell potential maps.
3. **Identification of premature stirrup corrosion causing brittle shear failure**:
   - Proved that thinner cover over stirrups leads to early cross-sectional loss, causing sudden shear failure without warning and up to 35.2 % capacity loss.
4. **Derivation of quantitative modification factors ($\eta$) for seismic evaluation codes (FEMA 274/310)**:
   - Replaced qualitative durability discount factors with experimentally calibrated strength-ductility degradation equations for seismic screening.

## Methods

- **Full-scale RC beam design and fabrication (Section 2 & Figs. 3–7)**:
  - Concrete: 28 d design compressive strength $f_{ck} = 24.0\ \text{MPa}$ (measured 26.5 MPa).
  - Reinforcement: Longitudinal rebar SD400 D16 ($f_y = 445\ \text{MPa}$), stirrups SD400 D10 ($f_y = 430\ \text{MPa}$).
  - 2 test series (16 beams total):
    - FB series (flexure-critical, 8 beams): FB-Non (control), FB-C1~C7 (accelerated corrosion for 5~35 d).
    - SB series (shear-critical, 8 beams): SB-Non (control), SB-C1~C7 (corrosion for 5~35 d, shear span-to-depth ratio $a/d = 2.85$).
- **Accelerated corrosion and half-cell potential logging (Sections 2.2–3.1)**:
  - Impressed current: $0.5\ \text{A}$ constant DC in 3.0 % $\text{NaCl}$ solution.
  - Potential mapping: Proceq CANIN+ analyzer ($\text{Cu/CuSO}_4$ reference electrode, ASTM C876, 24 nodes).
- **Structural testing and instrumentation (Section 2.3)**:
  - Loading: 1000 kN hydraulic actuator four-point bending (1800 mm span, 600 mm pure bending zone).
  - Measurements: Midspan displacement LVDT, rebar strain gauges, crack widths, and spalling tracking.

## Results

### 1. Flexural and shear capacity and ductility reduction across half-cell potential levels (Tables 1–4 & Figs. 10–15)

| Specimen ID | Failure Mode | Half-Cell Potential (mV CSE) | Yield Load ($P_y$, kN) | Ultimate Load ($P_{max}$, kN) | Capacity Loss (%) | Ultimate Disp. ($\delta_u$, mm) | Ductility Index ($\mu = \delta_u/\delta_y$) |
|---|---|---|---|---|---|---|---|
| **FB-Non (Control)** | Flexure | −125 mV (Non-corroded) | 92.5 ± 2.0 | **118.5 ± 2.5** | 0.0 % (Baseline) | **38.5 ± 1.2** | **4.85 (Ductile)** |
| **FB-C2 (Mild)** | Flexure | −285 mV (Uncertain) | 88.0 ± 1.8 | 112.0 ± 2.2 | −5.48 % | 35.2 ± 1.0 | 4.40 |
| **FB-C4 (Moderate)** | Flexure | −415 mV (Corroded) | 78.5 ± 1.6 | 98.2 ± 2.0 | −17.13 % | 28.5 ± 0.9 | 3.65 |
| **FB-C7 (Severe)** | **Flexure** | **−545 mV (Severe)** | **65.0 ± 1.5** | **84.7 ± 1.8** | **−28.52 %** | **22.3 ± 0.8** | **2.81 (−42.0 %)** |
| **SB-Non (Control)** | Shear | −130 mV (Non-corroded) | — | **162.0 ± 3.5** | 0.0 % (Baseline) | 12.5 ± 0.5 | 1.85 (Brittle) |
| **SB-C3 (Moderate)** | Shear | −385 mV (Corroded) | — | 132.5 ± 2.8 | −18.21 % | 9.8 ± 0.4 | 1.45 |
| **SB-C7 (Severe)** | **Shear** | **−560 mV (Severe)** | — | **105.0 ± 2.2** | **−35.19 %** | **6.5 ± 0.3** | **1.10 (Extremely brittle)** |

### 2. Corrosion mechanics and seismic safety
- **Corrosion expansion pressure and spalling**: 2~6-fold volume expansion of rust products caused longitudinal splitting cracks in concrete cover, leading to premature spalling and reduced effective compression zones.
- **Longitudinal rebar buckling and ductility plunge**: Rebar cross-section loss and bond degradation precipitated post-yield softening, reducing flexural displacement ductility by 42 % and elevating seismic collapse risk.

- **Overall conclusion**: This study established quantitative models correlating half-cell potential measurements with flexural, shear, and seismic ductility degradation in corrosion-damaged RC beams.

## Related Notes

- [[hyun-2020-flexural-behavior-concrete-ecc-composite-beams]] — Seismic performance of ECC plastic hinge composite beams.
- [[structural-repair-and-retrofitting]] — Repair and retrofitting mechanisms for deteriorated concrete structures.
- [[jang-2011-crack-width-chloride-diffusion-migration]] — Concrete microcracking and chloride transport mechanisms.
- [[kaish-2018-ferrocement-composites-column-strengthening]] — Column structural strengthening and confinement.
