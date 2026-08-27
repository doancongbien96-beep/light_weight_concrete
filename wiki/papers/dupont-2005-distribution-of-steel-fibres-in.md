---
title: "Distribution of steel fibres in rectangular sections"
type: source_note
source: "sources/dupont-2005-distribution-of-steel-fibres-in.pdf"
citation: "Dupont, D., & Vandewalle, L. (2005). Distribution of steel fibres in rectangular sections. Cement and Concrete Composites, 27(3), 391-398."
date: 2026-08-23
tags: [steel-fibres, fibre-distribution, fibre-orientation-factor, wall-effect, boundary-conditions, rilem-beams, fibre-counting, theory-foundation]
---

# Wall Effects, Fiber Orientation Factor ($\alpha$), and Calculation of Effective Bridging Fibers in Rectangular Sections of Steel Fiber-Reinforced Concrete

## Summary

To predict the fiber bridging stress ($\sigma-\delta$) and flexural toughness ($f_{R,j}$) across cracked sections in steel fiber-reinforced concrete (SFRC) structural members (beams, slabs, columns), Professors David Dupont and Lucie Vandewalle at KU Leuven established a geometric probability model of the mechanism whereby the rotational freedom of fibers is restrained by mold wall effects. Dividing rectangular cross sections into three distinct domains (central bulk domain, single-wall boundary domain, and two-wall corner boundary domain), the authors analytically derived theoretical orientation factors ($\alpha_1, \alpha_2, \alpha_3$) for each zone. The formulation was verified by cut-section counting of actual steel fibers across 107 full-scale RILEM standard notched beam specimens. The results demonstrated that the unconstrained central bulk orientation factor is **$\alpha_1 = 0.50$** (fully 3D isotropic random), the single-wall boundary factor is **$\alpha_2 = 0.60$** (2D planar alignment), and the two-wall corner factor is **$\alpha_3 = 0.84$** (1D axial alignment). The total cross-sectional orientation factor ($\alpha_{tot}$) predicting total fiber counts ($N_f = \alpha_{tot} V_f A_c / A_f$) showed correlation with experimental measurements across 107 specimens with **$R^2 > 0.95$**.

## Key Contributions

1. **Analytical derivation of theoretical fiber orientation factors ($\alpha$) across boundary constraint zones**:
   - **Area 1 (3D unconstrained bulk zone)**: Fiber centers located more than $l_f/2$ from all walls $\rightarrow \alpha_1 = \int_0^{\pi/2} \cos\theta \sin\theta d\theta = \mathbf{0.50}$.
   - **Area 2 (Single-wall constraint zone)**: Fiber centers within $y < l_f/2$ of one wall $\rightarrow$ spherical truncation integration yields $\mathbf{\alpha_2 = 0.60}$.
   - **Area 3 (Two-wall corner constraint zone)**: Corner region with $y < l_f/2$ and $z < l_f/2$ $\rightarrow$ dual spherical cap integration yields $\mathbf{\alpha_3 = 0.84}$.
2. **Formulation of unified effective fiber count ($N_f$) equations for rectangular and notched sections**:
   - Developed an analytical equation calculating the total number of fibers crossing a section within 5 % error from cross-section dimensions ($b, h$), notch depth ($ND$), fiber length ($l_f$), fiber cross-sectional area ($A_f$), and volume fraction ($V_f$):
     $$N_f = \alpha_{tot} \frac{V_f}{A_f} A_c = \left( \frac{\alpha_1 A_1 + \alpha_2 A_2 + \alpha_3 A_3 + \cdots}{A_c} \right) \frac{V_f}{\pi d_f^2 / 4} A_c$$
3. **Large-scale experimental verification across 107 RILEM beam sections**:
   - Full section counting of straight and hooked-end steel fibers across 107 fracture surfaces confirmed linear correlation ($R^2 = 0.954$) between predictions and measurements, providing the basis for orientation factors in RILEM and fib Model Code recommendations.

## Methods

- **Cross-sectional partitioning and geometric orientation modeling**:
  - Dimensions: width $b$, height $h$, fiber length $l_f$, fiber diameter $d_f$.
  - Domain subdivision (Figures 1 & 5):
    - Area 1 (center): $(b - l_f) \times (h - l_f)$, $\alpha_1 = 0.50$.
    - Area 2 (top/bottom/side edges): $2(b - l_f)\frac{l_f}{2} + 2(h - l_f)\frac{l_f}{2}$, $\alpha_2 = 0.60$.
    - Area 3 (four corners): $4 \times (l_f/2)^2$, $\alpha_3 = 0.84$.
    - Notched specimen modification: Area 4 ($\alpha_4 = 0.53$) and Area 5 ($\alpha_5 = 0.72$) applied to the ligament area excluding the notch depth ($ND$).
- **Experimental verification program (KU Leuven)**:
  - 107 RILEM TC 162-TDF standard beam specimens ($150\ \text{mm} \times 150\ \text{mm} \times 600\ \text{mm}$, notch depth 25 mm).
  - Steel fiber types: Three types of hooked-end steel fibers ($l_f = 35\sim 60\ \text{mm}, d_f = 0.55\sim 0.90\ \text{mm}, V_f = 0.3\%\sim 1.0\%$).
  - Post-test high-resolution photography and digital image-based full fiber counting.

## Results

### 1. Theoretical orientation factors and boundary conditions across section zones

| Section zone | Boundary constraint condition | 3D fiber degrees of freedom | Theoretical orientation factor ($\alpha_i$) | Bridging efficiency evaluation |
|---|---|---|---|---|
| **Area 1 (Bulk center)** | Unconstrained (Bulk) | Full 3D spherical random rotation | **0.50** | Standard 3D isotropic baseline |
| **Area 2 (Single wall)** | 1-plane parallel constraint ($y < l_f/2$) | 2D planar hemispherical rotation | **0.60 (+20 %)** | Wall effect increases bridging fiber density |
| **Area 3 (Corner)** | 2-plane orthogonal constraint ($y, z < l_f/2$) | 1D axial alignment | **0.84 (+68 %)** | Highest bridging efficiency in corners |
| **Area 4 (Notch top)** | 1-plane notch cut boundary | Partial constraint | **0.53** | Orientation at outermost flexural tension fiber |
| **Area 5 (Notch corner)**| 2-plane notch + side wall boundary | Corner partial constraint | **0.72** | Bridging contribution at notch tip |

### 2. Verification on 107 RILEM specimens and size effect analysis
- **Member thickness effect**: In thinner sections ($h \approx l_f$), the proportional areas of Area 2 and Area 3 increase, shifting the overall orientation factor $\alpha_{tot}$ from 0.50 up to 0.65~0.75.
- **Experimental prediction accuracy**: The mean error between predicted and counted fiber totals across 107 beam sections was **2.8 %**.

- **Overall conclusion**: The orientation factor model by Dupont and Vandewalle quantified mold boundary alignment effects of steel fibers via analytical formulations, establishing a deterministic framework for designing the flexural and tensile capacity of fiber-reinforced concrete sections.

## Related Notes

- [[fiber-orientation-distribution]] — Fiber orientation distribution and 2D/3D bridging efficiency factor theories.
- [[barnett-2010-assessment-of-fibre-orientation-in]] — Flow-induced fiber orientation and cross-sectional bridging in UHPFRC.
- [[banthia-2007-toughness-enhancement-in-steel-fiber]] — Hybrid steel fiber reinforcement and flexural toughness evaluation.
- [[fiber-bridging-constitutive-law]] — Fiber bridging $\sigma-\delta$ constitutive modeling.
