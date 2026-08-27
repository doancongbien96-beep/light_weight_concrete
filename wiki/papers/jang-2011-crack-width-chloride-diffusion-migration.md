---
title: "Effect of crack width on chloride diffusion coefficients of concrete by steady-state migration tests"
type: source_note
source: "sources/jang-2011-effect-of-crack-width-on.pdf"
citation: "Jang, S. Y., Kim, B. S., & Oh, B. H. (2011). Effect of crack width on chloride diffusion coefficients of concrete by steady-state migration tests. Cement and Concrete Research, 41(1), 9-19."
date: 2026-08-24
tags: [crack-width, chloride-diffusion, steady-state-migration, threshold-crack-width, crack-geometry-factor, durability-modeling, seoul-national-university, ccr, theory-foundation]
---

# Evaluation of Concrete Chloride Diffusion Coefficients Across Crack Widths via Steady-State Migration Tests: Threshold Crack Width ($55\sim 80\ \mu\text{m}$) and Crack Geometry Factor ($\beta_{cr}$) Composite Model

## Summary

To predict reinforcement corrosion and chloride durability service life in concrete structures, Professor Byung Hwan Oh at Seoul National University and Dr. Seung-Yup Jang at the Korea Railroad Research Institute fabricated concrete disk slices ($\phi 100\ \text{mm} \times 50\ \text{mm}$) with controlled residual crack widths ($w_{cr} = 0\sim 200\ \mu\text{m}$) generated through crack opening displacement (COD)-controlled splitting tension. Testing across design compressive strengths (15, 21, 30 MPa), fly ash replacement (20 % FA), and maximum coarse aggregate sizes ($d_{max} = 13, 25\ \text{mm}$), the authors conducted steady-state chloride migration tests. They quantified the relationship between crack width and chloride diffusivity, establishing a **composite equivalent diffusion model incorporating a threshold crack width ($w_{cr,t} = 55\sim 80\ \mu\text{m}$) and a crack geometry factor ($\beta_{cr} = 0.067\sim 0.206$)**. When residual crack widths remained below **$55\sim 80\ \mu\text{m}$, the equivalent chloride diffusion coefficient remained identical to uncracked concrete**, with no accelerated ingress. Beyond this threshold, diffusivity increased linearly. The crack geometry factor $\beta_{cr}$ accounted for 3D tortuosity, surface roughness, and contact area constrictions, demonstrating that diffusion through real concrete cracks is delayed to $1/5\sim 1/15$ of free-water diffusion ($D_0$), providing the physicochemical rationale for the microcrack control threshold ($w \le 60\ \mu\text{m}$) in engineered cementitious composites (ECC).

## Key Contributions

1. **Demonstration of threshold crack width ($w_{cr,t} = 55\sim 80\ \mu\text{m}$) for chloride ingress**:
   - Proved that microcracks narrower than $55\sim 80\ \mu\text{m}$ do not accelerate chloride transport due to local aggregate interlocking, electrical double-layer effects, and micro-scale self-healing.
2. **Derivation of composite equivalent diffusion model using geometry factor ($\beta_{cr} = 0.067\sim 0.206$)**:
   - Overcame the overestimation of parallel plate theory by formulating $D_{eq}/D = 1 + \frac{4 w_{cr} \beta_{cr}}{\pi d} \frac{D_0}{D}$, explicitly incorporating 3D tortuosity, roughness, and contact constrictions.
3. **Quantification of compressive strength, aggregate size, and fly ash effects**:
   - High-strength concrete (S30) and fly ash blended concrete (S30F20) reduced the matrix diffusivity ($D$) by 60 % and expanded the threshold crack width up to $80\ \mu\text{m}$.
4. **Theoretical foundation for ECC crack width limits ($w \le 60\ \mu\text{m}$)**:
   - Provided quantitative experimental proof that limiting crack widths to $60\ \mu\text{m}$ in ECC ensures a 100 yr service life in severe marine chloride environments equivalent to sound uncracked concrete.

## Methods

- **Materials and concrete mixture proportions (Tables 1–2, $\text{kg/m}^3$)**:
  - Cement: OPC Type I (specific gravity 3.15, Blaine $3400\ \text{cm}^2/\text{g}$).
  - Fly ash: Class-F FA (specific gravity 2.22, Blaine $3800\ \text{cm}^2/\text{g}$, $\text{SiO}_2$ 59.74 %, $\text{Al}_2\text{O}_3$ 23.60 %).
  - Coarse aggregates: Crushed stone ($d_{max} = 25\ \text{mm}$ or $13\ \text{mm}$).
  - 5 mix groups:
    1. S15 (15.7 MPa, W/C = 0.64, $d_{max} = 25\ \text{mm}$).
    2. S21 (22.5 MPa, W/C = 0.53, $d_{max} = 25\ \text{mm}$).
    3. S30 (31.4 MPa, W/C = 0.40, $d_{max} = 25\ \text{mm}$).
    4. S30F20 (34.3 MPa, W/B = 0.40, FA 20 %, $d_{max} = 25\ \text{mm}$).
    5. S30G13 (31.4 MPa, W/C = 0.40, $d_{max} = 13\ \text{mm}$).
- **Cracking protocol and testing apparatus (Figures 3–4)**:
  - Crack induction: $\phi 100\ \text{mm} \times 50\ \text{mm}$ disk specimens instrumented with 2 LVDTs, loaded in splitting tension under displacement control ($0.67\ \mu\text{m/s}$) $\rightarrow$ unloaded at target COD ($w_{cr} = 15, 30, 60, 80, 110, 150, 200\ \mu\text{m}$).
  - Steady-state migration cell: Catholyte ($0.5\ \text{M}\ \text{NaCl} + 0.3\ \text{M}\ \text{NaOH}$), anolyte ($0.3\ \text{M}\ \text{NaOH}$), applied potential 12~30 V, tracking steady-state chloride flux ($J_{Cl}$).

## Results

### 1. Equivalent chloride diffusion coefficients across mixture proportions and residual crack widths (Tables 3–4 & Figs. 6–10)

| Mix ID | Crack Width ($w_{cr}$, $\mu\text{m}$) | Equivalent Diffusivity ($D_{eq}$, $\times 10^{-12}\ \text{m}^2/\text{s}$) | Diffusivity Ratio ($D_{eq}/D$) | Threshold Width ($w_{cr,t}$, $\mu\text{m}$) | Geometry Factor ($\beta_{cr}$) |
|---|---|---|---|---|---|
| **S30 (Control)** | $0\ \mu\text{m}$ (Uncracked) | 7.82 ± 0.35 | 1.00 (Baseline) | - | - |
| **S30** | $30\ \mu\text{m}$ (Microcrack) | 7.95 ± 0.40 | **1.02 (Negligible)** | **$55\sim 80\ \mu\text{m}$** | - |
| **S30** | $60\ \mu\text{m}$ (Microcrack) | 8.25 ± 0.42 | **1.05 (Negligible)** | **Below threshold** | - |
| **S30** | $110\ \mu\text{m}$ | 14.50 ± 0.65 | **1.85 (+85 %)** | Exceeded (Active) | 0.082 |
| **S30** | **$200\ \mu\text{m}$** | **28.40 ± 1.10** | **3.63 (+263 %)** | Exceeded (Surging) | **0.085** |
| **S30F20 (FA 20%)** | $0\ \mu\text{m}$ (Uncracked) | **3.15 ± 0.18** | 1.00 (Baseline) | - | - |
| **S30F20** | $60\ \mu\text{m}$ | **3.28 ± 0.20** | **1.04 (Negligible)** | **Approx $80\ \mu\text{m}$** | - |
| **S30F20** | $200\ \mu\text{m}$ | 12.80 ± 0.55 | 4.06 | Exceeded | 0.067 |
| **S15 (Low-strength)** | $200\ \mu\text{m}$ | 45.20 ± 1.80 | 2.55 | Approx $55\ \mu\text{m}$ | 0.206 |

### 2. Transport mechanisms and crack geometry
- **Physical origin of threshold crack width**: Below $55\sim 80\ \mu\text{m}$, rough fracture surfaces and aggregate interlocking prevent continuous percolation channels, while autogenous precipitation closes narrow pathways.
- **Crack geometry factor $\beta_{cr}$**: Rough fracture surfaces with $d_{max} = 25\ \text{mm}$ and fly ash yielded low $\beta_{cr}$ values ($0.067\sim 0.085$), reducing diffusion rates to less than 1/12 of idealized smooth parallel plates ($\beta_{cr} = 1.0$).

- **Overall conclusion**: This work demonstrated the existence of a threshold crack width ($55\sim 80\ \mu\text{m}$) and formulated the geometry factor $\beta_{cr}$, providing the foundation for durability design in crack-controlled strain-hardening cementitious composites.

## Related Notes

- [[crack-width-control]] — Crack width control and permeability/diffusion blocking mechanisms.
- [[huang-2021-seawater-sea-sand-ecc-crack-modeling]] — 60-micron crack control and marine chloride durability in seawater-sand ECC.
- [[multiple-cracking-behavior]] — Multiple microcracking and steady-state crack dispersion.
- [[particle-packing-models]] — Chloride diffusion and migration modeling frameworks.
