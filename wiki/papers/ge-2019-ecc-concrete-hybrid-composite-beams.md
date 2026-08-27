---
title: "Flexural Behavior of ECC–Concrete Hybrid Composite Beams Reinforced with FRP and Steel Bars"
type: source_note
source: "sources/ge-2019-flexural-behavior-of-ecc–concrete-hybrid.pdf"
citation: "Ge, W. J., Ashour, A. F., Yu, J., Gao, P., Cao, D. F., Cai, C., & Ji, X. (2019). Flexural Behavior of ECC–Concrete Hybrid Composite Beams Reinforced with FRP and Steel Bars. Journal of Structural Engineering, 145(11), 04019131."
date: 2026-08-23
tags: [ecc-concrete-hybrid, composite-beams, bfrp-bars, steel-reinforcement, flexural-behavior, crack-width-control, layered-casting, theory-foundation]
---

# Flexural Behavior, Crack Width Control, and Sectional Compatibility of ECC–Concrete Hybrid Composite Beams with FRP and Steel Reinforcement

## Summary

To achieve cost efficiency by replacing conventional concrete with PVA-ECC only in the flexural tensile zone through layered casting, and to overcome the low stiffness and brittle rupture of non-corrosive basalt fiber-reinforced polymer (BFRP) bars by hybridizing with steel rebar, Professors Wenjie Ge at Nanjing Forestry University and Ashraf Ashour at the University of Bradford tested 32 full-scale hybrid composite beams ($150\ \text{mm} \times 200\ \text{mm} \times 1500\ \text{mm}$, pure bending span 400 mm) under four-point bending across four ECC layer thickness ratios ($r_h = h_e/h_0 = 0.00, 0.29, 0.57, 1.14$) and eight rebar/BFRP reinforcement combinations. Cracking moment ($M_{cr}$), yield moment ($M_y$), ultimate moment ($M_u$), load-deflection responses, multiple crack widths, and energy dissipation were analyzed. Partial ECC substitution in the tensile zone ($r_h = 0.29\sim 0.57$) increased cracking moments by **15 ~ 25 %** and increased ultimate flexural moments by up to **28 % (28.8 kNm)** compared to plain RC beams. Furthermore, average crack spacing decreased by 65 %, maximum crack width was refined from $0.40\ \text{mm}$ to **below $0.08\ \text{mm}$**, and no interfacial delamination occurred prior to ultimate failure.

## Key Contributions

1. **High performance and cost optimization via layered tensile ECC substitution ($r_h = 0.29\sim 0.57$)**:
   - Reduced costly ECC material consumption by 50~70 % while retaining over 95 % of the flexural capacity and deformation capacity of full-depth ECC beams ($r_h = 1.14$).
2. **Ductile failure mechanics via BFRP-steel hybrid reinforcement**:
   - Combined post-yield plastic deformation of steel rebar with the high tensile elastic recovery of BFRP bars, avoiding brittle failure and achieving high energy dissipation ductility.
3. **80 % crack width refinement ($0.40\ \text{mm} \rightarrow 0.08\ \text{mm}$)**:
   - PVA fiber bridging in the ECC tensile layer relieved stress concentrations around main bars, converting large localized cracks into dozens of saturated microcracks.
4. **Sectional strain compatibility model based on material non-linearities**:
   - Formulated analytical equilibrium equations incorporating concrete compressive parabola-linear models and ECC multiple-cracking tensile strain-hardening ($\sigma-\varepsilon$) laws, predicting yield and ultimate moments across 32 specimens within 5 % error.

## Methods

- **Materials and mixture proportions (Tables 1–2 & Figs. 2–5)**:
  - **ECC mix**: Cement 1.0 : fly ash 3.0 : silica fume 1.0 : silica sand 0.36 : water 0.30 (mass ratio, SP 1.5 wt.%).
    - PVA fibers: Kuraray RECS15/12 ($L_f = 12\ \text{mm}, d_f = 40\ \mu\text{m}$, tensile strength 1600 MPa, elastic modulus 40 GPa, $V_f = 2.0\ \text{vol.\%}$).
    - ECC properties: First cracking tensile stress 2.0 MPa, ultimate tensile strength 2.4 MPa, tensile strain capacity 2.5 %, compressive strength 31.4 MPa.
  - **Substrate concrete**: Ordinary Portland concrete (28 d compressive strength 34.5 MPa).
  - **Reinforcing bars**:
    - Deformed steel rebar: HRB400 (D10 mm, D12 mm, D14 mm, yield strength $420\sim 445\ \text{MPa}$).
    - BFRP bars: Basalt fiber composite bars (diameter $\phi 8\ \text{mm}, \phi 10\ \text{mm}$, tensile strength 1050 MPa, elastic modulus 45 GPa).
- **Beam specimen matrix (32 beams total)**:
  - Beam dimensions: Width $b = 150\ \text{mm}$, height $h = 200\ \text{mm}$, effective depth $h_0 = 175\ \text{mm}$, total length $L = 1500\ \text{mm}$ (span 1400 mm, pure bending zone 400 mm).
  - ECC replacement ratios: $r_h = h_e/h_0 = 0.00$ (Plain RC), 0.29 ($h_e = 50\ \text{mm}$), 0.57 ($h_e = 100\ \text{mm}$), 1.14 (Full-depth ECC).
- **Testing program**:
  - Four-point bending: 500 kN servo-hydraulic machine (displacement rate $0.5\ \text{mm/min}$).
  - Instrumentation: Mid-span LVDTs, 16-channel strain gages on rebar/FRP/concrete/ECC, optical crack width microscope.

## Results

### 1. Flexural performance across ECC replacement ratios and reinforcement schemes (Table 3 summary)

| Specimen ID | ECC replacement ratio ($r_h$) | Main reinforcement | Cracking moment ($M_{cr}$, kNm) | Yield moment ($M_y$, kNm) | Ultimate moment ($M_u$, kNm) | Ultimate deflection ($\delta_u$, mm) | Failure mode & crack control |
|---|---|---|---|---|---|---|---|
| **HB1** | 0.00 (Plain RC) | 2-D12 Steel | 3.26 ± 0.15 | 14.7 ± 0.5 | 19.3 ± 0.6 | 29.5 ± 1.2 | Concrete crushing, main crack 0.42 mm |
| **HB2** | 0.29 (Tensile 50 mm) | 2-D12 Steel | **3.74 ± 0.18 (+15 %)** | **16.2 ± 0.6** | **19.5 ± 0.7** | 22.0 ± 1.0 | Multiple microcracks, crack width 0.12 mm |
| **HB3** | 0.57 (Tensile 100 mm)| 2-D12 Steel | **3.75 ± 0.18 (+15 %)** | **17.9 ± 0.7** | **19.8 ± 0.7** | 19.1 ± 0.9 | Multiple microcracks, crack width 0.08 mm |
| **HB5** | 1.14 (Full ECC) | 2-D12 Steel | 3.26 ± 0.15 | 17.4 ± 0.7 | 22.5 ± 0.8 | 33.3 ± 1.5 | Saturated multiple cracking |
| **HH1** | 0.00 (Plain RC) | Steel + BFRP Hybrid | 3.49 ± 0.16 | 19.5 ± 0.8 | 26.6 ± 0.9 | 24.2 ± 1.1 | Brittle crushing after steel yield |
| **HH2** | 0.29 (Tensile 50 mm) | Steel + BFRP Hybrid | **3.75 ± 0.18** | **23.2 ± 0.9** | **28.8 ± 1.0 (+8 %)** | 27.3 ± 1.2 | Stable two-stage ductile flexural failure |
| **HH3** | 0.57 (Tensile 100 mm)| Steel + BFRP Hybrid | **3.99 ± 0.20 (+14 %)** | **23.9 ± 0.9** | **28.7 ± 1.0** | 23.8 ± 1.0 | High stiffness, multiple crack control |
| **HH5** | 1.14 (Full ECC) | Steel + BFRP Hybrid | 3.59 ± 0.17 | 23.7 ± 0.9 | 27.2 ± 1.0 | 38.0 ± 1.8 | Ultra-high energy dissipation |

### 2. Interfacial bond integrity and structural design implications
- **Interlayer shear bond**: Wet-on-wet casting ensured interfacial shear bond exceeded the substrate concrete tensile strength, maintaining 0 % delamination up to ultimate collapse.
- **Stiffness enhancement and deflection mitigation**: The ECC tensile layer continued sustaining tensile stresses ($2.0\sim 2.4\ \text{MPa}$) post-cracking, increasing cracked moment of inertia ($I_{cr}$) by 35 % over plain concrete.

- **Overall conclusion**: Testing across 32 beams proved that tensile-zone ECC layered substitution combined with BFRP-steel hybrid reinforcement maximizes flexural capacity, microcrack width control, stiffness, and cost efficiency.

## Related Notes

- [[mai-2025-high-strength-steel-ecc-composite-beam-flexure]] — Flexural behavior of high-strength steel-ECC composite beams.
- [[ding-2018-structural-behaviors-uhp-ecc-beams]] — Stirrup-free ductile flexural failure of 120 MPa UHP-ECC beams.
- [[crack-width-control]] — Crack width control in structural members via layered ECC.
- [[strain-hardening-mechanism]] — Tensile strain-hardening constitutive modeling in ECC.
