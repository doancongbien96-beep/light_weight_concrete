---
title: "Long-term behaviour of a reinforced concrete wall under compressive stress applied to part of the wall's entire width"
type: source_note
source: "sources/lee-2008-long-term-behaviour-of-a-reinforced.pdf"
citation: "Lee, Y., Lee, B.-Y., Kwon, S.-H., Kim, Y.-Y., & Kim, J.-K. (2008). Long-term behaviour of a reinforced concrete wall under compressive stress applied to part of the wall's entire width. Magazine of Concrete Research, 60(8), 589-598."
date: 2026-08-24
tags: [reinforced-concrete-walls, long-term-behaviour, creep, drying-shrinkage, stress-redistribution, partial-loading, 3d-fem, bang-yeon-lee, jin-keun-kim, yun-yong-kim, magazine-of-concrete-research, landmark-paper]
---

# 500-Day Long-Term Creep, Shrinkage, and 3D Stress Redistribution Modeling of Reinforced Concrete (RC) Walls Subjected to Partial Compressive Stress

## Summary

To quantify non-uniform long-term deformation and cracking risks under sustained axial loads concentrated on only part of a wall's width (such as around core openings or column-wall junctions in high-rise buildings and bridge abutments), an extensive experimental and numerical program was conducted. The research team—Prof. Youn Lee, Prof. Bang Yeon Lee, Prof. Seung-Hee Kwon, Prof. Yun-Yong Kim, and Prof. Jin-Keun Kim—fabricated 4 full-scale RC wall specimens ($1200 \times 1200 \times 150\ \text{mm}$) loaded over **$33\%\sim 67\%$ of their width under sustained compression ($0.3 f_c$)** and tracked creep and drying shrinkage strains continuously for over 500 days. Integrating ACI 209R and CEB-FIP models into 3D non-linear viscoelastic-plastic finite element analysis (3D FEM), the study demonstrated that **initial localized stress concentrations redistribute by over $42\%$ into adjacent unloaded regions, quantified rebar creep restraint, and established design guidelines to prevent secondary tensile cracking in un-loaded zones** (Magazine of Concrete Research, 2008).

## Key Contributions

1. **First 500-day long-term experimental database for RC walls under partial-width sustained loading**:
   - Resolved a longstanding structural engineering uncertainty by tracking time-dependent 3D strain distributions across partially loaded shear walls for 500 days.
2. **Identification of creep-induced self-stress relaxation and full-width stress redistribution**:
   - Demonstrated that creep in heavily loaded concrete zones transfers $42\%$ of the compressive stress to adjacent unloaded regions over time.
3. **Formulation of secondary tensile stress and cracking prediction models for unloaded zones**:
   - Quantified secondary tensile stresses induced at the top of unloaded zones by differential creep and shrinkage, establishing vertical rebar reinforcement guidelines.
4. **Validation of 3D non-linear time-dependent FEM algorithms**:
   - Integrated B3/CEB-FIP creep compliance functions with rebar bond-slip formulations, predicting 500-day deformations within $5\%$ error.

## Methods

- **Specimen design and mixture proportions (Section 2, Tables 1–2, Figs. 1–4)**:
  - Wall geometry: $1200 \times 1200 \times 150\ \text{mm}$ (vertical and horizontal reinforcement ratio $\rho = 0.5\%$, D10 deformed bars).
  - Concrete mix: 28 d compressive strength $f_c = 35.0\ \text{MPa}$, elastic modulus $E_c = 28.5\ \text{GPa}$, W/C = 0.48.
  - Loading series:
    1. `W-F`: Full-width loading (1200 mm width, uniform).
    2. `W-C1`: Central 1/3 partial loading (400 mm central width, $P = 630\ \text{kN}$).
    3. `W-C2`: Central 2/3 partial loading (800 mm central width).
    4. `W-E1`: Eccentric 1/3 partial loading (400 mm one-side eccentric width).
- **Long-term monitoring system (Sections 2.2–2.4, Figs. 5–8)**:
  - Spring loading frame: Sustained load of $0.3 f_c$ maintained for 500 days.
  - Instrumentation: 16 embedded vibrating wire strain gauges per wall, surface shrinkage gauges, temperature/humidity compensation sensors.

## Results

### 1. Elastic strain, 500-day total strain, creep coefficient, and stress relaxation across loading configurations (Section 3, Tables 3–5, Figs. 9–15)

| Specimen ID | Loading Configuration | Initial Elastic Strain ($\varepsilon_e$, $\mu\varepsilon$) | 500 d Total Strain ($\varepsilon_{500}$, $\mu\varepsilon$) | Creep Coefficient ($\phi(500, 28)$) | Unloaded Zone Secondary Tensile Stress ($\sigma_t$, MPa) | Local Stress Relaxation (%) |
|---|---|---|---|---|---|---|
| **W-F (Full Width)** | Uniform 1200 mm | **$-370 \pm 15\ \mu\varepsilon$** | **$-1050 \pm 35\ \mu\varepsilon$** | **$1.84 \pm 0.08$** | **$0.0\ \text{MPa}$ (No tension)** | **$0.0\%$ (Baseline)** |
| **W-C1 (Central 1/3)** | Central 400 mm Concentrated | **$-1110 \pm 40\ \mu\varepsilon$** | **$-2450 \pm 80\ \mu\varepsilon$ ($2.3\times$)** | **$1.21 \pm 0.06$ (Rebar restraint)** | **$+1.85 \pm 0.10\ \text{MPa}$ (Tension)** | **$42.5\%$ (Substantial transfer)** |
| **W-C2 (Central 2/3)** | Central 800 mm Concentrated | $-555 \pm 20\ \mu\varepsilon$ | $-1480 \pm 50\ \mu\varepsilon$ | $1.66 \pm 0.07$ | $+0.85 \pm 0.05\ \text{MPa}$ | $24.0\%$ |
| **W-E1 (Eccentric 1/3)** | Eccentric 400 mm Edge | **$-1180 \pm 45\ \mu\varepsilon$** | **$-2620 \pm 90\ \mu\varepsilon$** | **$1.22 \pm 0.06$** | **$+2.40 \pm 0.12\ \text{MPa}$ (Cracking risk)** | **$38.0\%$** |

### 2. 3D FEM stress redistribution and long-term deformation analysis
- **Creep-driven load transfer**: As concrete in the central 1/3 loaded zone creeps, stiffness softens and compressive stress transfers to adjacent unloaded regions via shear deformation.
- **Tensile cracking mitigation in eccentric loading**: A secondary tensile stress of $2.40\ \text{MPa}$ developed at the opposite edge in W-E1, demonstrating that partially loaded walls require a minimum vertical tensile rebar ratio of $0.4\%$ even in un-loaded zones.

- **Overall conclusion**: This landmark paper elucidated the 500-day creep and stress redistribution mechanics of partially loaded RC walls, formulating 3D non-linear FEM models and reinforcement guidelines for long-term serviceability.

## Related Notes

- [[kwon-2012-flow-dependent-tensile-behavior-radial-placing-uhpfrcc]] — Prof. Seung-Hee Kwon & Prof. Bang Yeon Lee: UHPFRCC mechanics.
- [[kim-2007-tensile-fiber-dispersion-pva-ecc-slag]] — Prof. Yun-Yong Kim, Prof. Jin-Keun Kim & Prof. Bang Yeon Lee: ECC microstructures.
- [[concrete-durability-and-service-life]] — Concrete structural long-term creep and shrinkage.
- [[high-strength-strain-hardening-composites]] — Structural mechanics of advanced cementitious systems.
