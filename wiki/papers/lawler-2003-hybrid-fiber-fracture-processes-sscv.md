---
title: "Fracture processes of hybrid fiber-reinforced mortar"
type: source_note
source: "sources/lawler-2003-fracture-processes-of-hybrid-fiber-reinforced.pdf"
citation: "Lawler, J. S., Wilhelm, T., Zampini, D., & Shah, S. P. (2003). Fracture processes of hybrid fiber-reinforced mortar. Materials and Structures, RILEM, 36(257), 197-208."
date: 2026-08-24
tags: [hybrid-fiber, macro-steel-fiber, micro-steel-fiber, pva-fiber, fracture-process, sscv, computer-vision, crack-width-map, surendra-shah, northwestern-university, materials-and-structures, landmark-paper]
---

# Fracture Processes of Macro/Micro Steel and PVA Hybrid Fiber Reinforced Mortar: Multi-Scale Crack Control Synergy via Subregion Scanning Computer Vision (SSCV, $1\ \mu\text{m}$ Resolution)

## Summary

To overcome the scale-dependent limitations of single fiber reinforcement (where micro fibers delay crack initiation but lack large-displacement bridging, while macro fibers provide post-peak toughness but cannot arrest microcracks), Prof. Surendra P. Shah's group at Northwestern University investigated hybrid fiber reinforced mortar combining **hooked macro steel fibers ($d_f = 500\ \mu\text{m}$, $L_f = 30\ \text{mm}$), straight micro steel fibers ($d_f = 22\ \mu\text{m}$, $L_f = 6\ \text{mm}$), and PVA micro fibers ($d_f = 14\ \mu\text{m}$, $L_f = 12\ \text{mm}$)**. Using **Subregion Scanning Computer Vision (SSCV: tracking surface displacement fields across 56 subregions with $1\ \mu\text{m}$ resolution)** in notched 3-point bending (CMOD control) and direct tension tests, the authors elucidated the multi-scale synergy wherein **micro fibers arrest microcracks below $10\ \mu\text{m}$ while macro fibers bridge macrocracks, enhancing first cracking strength, peak load, and post-peak toughness**.

## Key Contributions

1. **Development of SSCV high-resolution surface displacement and crack width mapping ($1\ \mu\text{m}$ precision)**:
   - Utilized digital image correlation across 56 grid sub-images to continuously visualize and quantify the progression from sub-$10\ \mu\text{m}$ microcrack initiation to macrocrack localization.
2. **Demonstration of multi-scale fracture mitigation synergy between micro and macro fibers**:
   - Micro fibers (steel/PVA) delayed microcrack initiation below $10\ \mu\text{m}$ from matrix defects, elevating first crack strength, while macro steel fibers bridged main cracks exceeding $50\ \mu\text{m}$ to maximize residual toughness.
3. **Micro fiber enhancement of macro fiber anchorage matrix**:
   - Micro fibers suppressed local matrix microcracking and shear damage around the hooked ends of macro steel fibers, elevating their mechanical pullout efficiency.
4. **Distinction between PVA and micro steel fiber mechanics**:
   - PVA micro fibers maximized the number of distributed microcracks below $10\ \mu\text{m}$ via chemical bonding, whereas straight micro steel fibers provided superior strength enhancement due to their high elastic modulus ($210\ \text{GPa}$).

## Methods

- **Fiber specifications and mixture proportions (Tables 1–2)**:
  - **Macro steel fiber (s, 500/30)**: Hooked-end, $d_f = 500\ \mu\text{m}$, $L_f = 30\ \text{mm}$, $\sigma_{fu} = 1115\ \text{MPa}$, $E_f = 210\ \text{GPa}$, $V_f = 0.5\ \text{vol.\%}$.
  - **Micro steel fiber (S, 22/06)**: Straight, $d_f = 22\ \mu\text{m}$, $L_f = 6\ \text{mm}$, $\sigma_{fu} = 2100\ \text{MPa}$, $E_f = 210\ \text{GPa}$, $V_f = 1.5\ \text{vol.\%}$.
  - **PVA micro fiber (PVA, 14/12)**: Monofilament, $d_f = 14\ \mu\text{m}$, $L_f = 12\ \text{mm}$, $\sigma_{fu} = 1500\ \text{MPa}$, $E_f = 36\ \text{GPa}$, $V_f = 1.5\ \text{vol.\%}$.
  - Mix series: Plain unreinforced mortar, 0.5% s alone, 1.5% S alone, 1.5% PVA alone, Hybrid 1 (0.5% s + 1.5% S), Hybrid 2 (0.5% s + 1.5% PVA).
  - Matrix: Cement : sand : water = 1:2:0.5 by weight.
- **Testing apparatus and optical measurement (Section 2, Figs. 1–4)**:
  - Flexural tests: RILEM TC 89-FMT notched beams ($100 \times 100 \times 400\ \text{mm}$, notch depth $33\ \text{mm}$) loaded under closed-loop CMOD control at $0.15\ \text{mm/min}$.
  - Direct tension: $75 \times 150 \times 12.7\ \text{mm}$ coupon plates under displacement control.
  - SSCV system: High-resolution CCD camera on an automated $x-y$ motor stage scanning 56 surface regions for digital image correlation (DIC) displacement field computation.

## Results

### 1. Flexural fracture parameters and crack control across fiber combinations (Table 3, Figs. 5–10)

| Mix Series | Fiber Combination | Total Volume ($V_f$, %) | 1st Crack Strength ($\sigma_{fc}$, MPa) | Modulus of Rupture (MOR, MPa) | Post-Peak Toughness (N$\cdot$m) | Microcrack Behavior ($\le 10\ \mu\text{m}$) |
|---|---|---|---|---|---|---|
| **Plain (Control)** | None | 0.0 % | $3.8 \pm 0.2$ | $3.8 \pm 0.2$ | $0.15 \pm 0.02$ | Single brittle crack rapid propagation |
| **0.5% s (Macro)** | 500/30 Steel | 0.5 % | $3.9 \pm 0.2$ | $4.2 \pm 0.3$ | $4.20 \pm 0.35$ | Single crack localization, residual bridging |
| **1.5% S (Micro)** | 22/06 Micro Steel | 1.5 % | $5.2 \pm 0.3$ | $6.8 \pm 0.4$ | $2.80 \pm 0.25$ | Microcrack multi-dispersion, steep post-peak drop |
| **1.5% PVA (Micro)** | 14/12 PVA | 1.5 % | **$5.8 \pm 0.3$** | $7.2 \pm 0.4$ | $3.50 \pm 0.30$ | **Highest multiple microcrack density** |
| **Hybrid 1** | **0.5% s + 1.5% S** | **2.0 %** | **$5.4 \pm 0.3$** | **$8.6 \pm 0.5$ (Highest)** | **$8.90 \pm 0.55$ (Synergy)** | **Simultaneous strength and toughness gain** |
| **Hybrid 2** | **0.5% s + 1.5% PVA** | **2.0 %** | **$6.1 \pm 0.4$ (Highest)** | **$9.1 \pm 0.5$ (Highest)** | **$9.80 \pm 0.60$ (Highest)** | **Microcrack dispersion + macrocrack bridging** |

### 2. Multi-scale hybrid fracture mechanisms
- **Micro-cracking phase**: Micro fibers shield the tips of microcracks ($< 10\ \mu\text{m}$), increasing first cracking strength by over $50\%$.
- **Macro-cracking and pullout phase**: When the main crack width exceeds $50\ \mu\text{m}$, macro hooked-end steel fibers engage to dissipate pullout energy, achieving a quantitative synergy where total hybrid fracture energy exceeds the sum of individual fiber contributions by more than 1.5 times.

- **Overall conclusion**: This landmark paper by Prof. Surendra P. Shah's group utilized high-resolution SSCV computer vision to visually quantify multi-scale crack control synergies between micro and macro fibers, establishing fundamental design principles for hybrid fiber reinforced concrete.

## Related Notes

- [[strain-hardening-mechanism]] — Micromechanics and fiber bridging theories for ECC/FRC.
- [[kang-2011-fiber-distribution-uhsc-flexural-strength]] — Prof. Bang Yeon Lee: Image analysis of steel fiber distribution.
- [[felekoglu-2015-htpp-ecc-fiber-distribution-image-analysis]] — Image analysis of micro-fiber dispersion in HTPP-ECC.
- [[high-strength-strain-hardening-composites]] — High-performance hybrid fiber reinforced composites.
