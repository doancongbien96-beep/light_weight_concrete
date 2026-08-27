---
title: "Studies on repair and strengthening methods of damaged reinforced concrete columns"
type: source_note
source: "sources/fukuyama-2000-studies-on-repair-and-strengthening.pdf"
citation: "Fukuyama, K., Higashibata, Y., & Miyauchi, Y. (2000). Studies on repair and strengthening methods of damaged reinforced concrete columns. Cement and Concrete Composites, 22(1), 17-28."
date: 2026-08-23
tags: [seismic-retrofit, damaged-rc-columns, cf-sheets, cfrp-plates, steel-jacketing, cyclic-shear, ductility-enhancement, kobe-earthquake, takenaka, theory-foundation]
---

# Shear Capacity Restoration and Ductility Enhancement of Earthquake-Damaged RC Columns via Carbon Fiber Sheet (CFRP) and Steel Jacketing

## Summary

To rapidly restore and enhance the seismic safety of reinforced concrete (RC) columns sustaining severe shear failure and rebar buckling during the 1995 Hyogoken-Nanbu (Kobe) earthquake without removing crushed concrete or buckled longitudinal bars, researchers at Takenaka Corporation applied **carbon fiber sheets (2 plies of CF sheets: $300\ \text{g/m}^2/\text{layer}$)**, **preformed CFRP plates**, **steel plate jacketing (thickness $t = 2.3\ \text{mm}$)**, **RC section enlargement jackets**, and non-shrink high-flow mortar grouting to eight 1/2-scale column specimens ($350\ \text{mm} \times 350\ \text{mm} \times 900\ \text{mm}$, shear span-to-depth ratio $M/QD = 1.29$). Under constant axial load ($\sigma_0 = 3.0\ \text{MPa}$) and cyclic lateral shear reversals, the retrofitted columns achieved peak shear strengths of **$285\sim 340\ \text{kN}$ (34 ~ 60 % higher than the undamaged baseline of 213 kN)** and increased ultimate drift capacity from **$R = 4.1 \times 10^{-3}\ \text{rad}$ to $15\sim 20 \times 10^{-3}\ \text{rad}$ (over 4-fold increase)**, transforming brittle shear failure into ductile flexural yielding.

## Key Contributions

1. **Demonstration of >100 % seismic restoration in severely damaged RC columns**:
   - Proved that even in columns with crushed core concrete and buckled longitudinal bars, full shear capacity and initial stiffness can be restored without demolishing crushed zones by combining non-shrink mortar pressure grouting with external carbon fiber wrapping.
2. **Transition from brittle shear failure to high-ductility flexural response ($R \ge 1.5 \%$)**:
   - Lateral carbon fiber confinement restrained diagonal shear crack opening, suppressing brittle shear splitting and establishing stable spindle-shaped hysteresis loops up to drift angles of $R = 15/1000\sim 20/1000\ \text{rad}$.
3. **Establishment of modified Arakawa shear strength equation for retrofitted columns**:
   - Formulated ultimate shear strength prediction models incorporating carbon fiber tensile strength ($f_{cf}$), effective strain ($\varepsilon_{cfe} = 0.007$), and jacket thickness:
     $$V_{su} = \left[ \frac{0.053 p_t^{0.23} (F_c + 18)}{M/(Q d) + 0.12} + 0.85 \sqrt{p_w \sigma_{wy} + p_{cf} \sigma_{cf}} + 0.1 \sigma_0 \right] b j$$

## Methods

- **Column specimens and retrofit matrix (Table 2 & Figure 4)**:
  - Column geometry: Section $350\ \text{mm} \times 350\ \text{mm}$, height $H = 900\ \text{mm}$ ($M/QD = 1.29$).
  - Existing reinforcement (C1): Main bars 4-D16 ($p_t = 0.65\%$, yield strength 372 MPa), ties 2-D6 @ 100 mm ($p_w = 0.18\%$, yield strength 354 MPa).
  - Concrete compressive strength: $F_c = 23.5\ \text{MPa}$.
  - Specimen series:
    - C1: Undamaged control baseline.
    - C2: Damaged + RC enlargement jacket ($450\times 450\ \text{mm}$, welded wire mesh + high-flow concrete).
    - C3: Damaged + steel plate jacket ($450\times 450\ \text{mm}$, 2.3 mm steel plate + high-flow concrete).
    - C4: Retained crushed concrete + recasting with high-flow concrete ($350\times 350\ \text{mm}$).
    - C5: Retained crushed concrete + non-shrink mortar grouting ($350\times 350\ \text{mm}$).
    - C6: Undamaged column + steel jacket ($350\times 350\ \text{mm}$, 2.3 mm plate).
    - C7: Undamaged column + **2-ply CF sheet wrapping ($300\ \text{g/m}^2/\text{layer}$, modulus 230 GPa)**.
    - C29: Damaged column + **preformed CFRP plate jacket + non-shrink mortar grouting**.
- **Loading and instrumentation (Figure 7)**:
  - Constant axial load: $N = 368\ \text{kN}$ ($\sigma_0 = N/BD = 3.0\ \text{MPa}$).
  - Cyclic lateral shear: Reversed cyclic displacement control ($R = \pm 1/1000, 2.5/1000, 5/1000, 10/1000, 15/1000, 20/1000\ \text{rad}$).

## Results

### 1. Cyclic shear performance of RC columns across repair and retrofitting schemes (Table 5 & Figures 9–12)

| Specimen ID | Damage state & retrofit scheme | Peak shear strength ($Q_{max}$, kN) | Strength ratio ($Q/Q_{C1}$) | Drift at peak load ($R_{max}$, rad) | Ultimate drift ($R_u$, rad) | Failure mode & hysteresis |
|---|---|---|---|---|---|---|
| **C1 (Control)** | Undamaged baseline | 213 kN | 1.00 (Baseline) | $4.1 \times 10^{-3}$ | $5.0 \times 10^{-3}$ | Brittle shear splitting |
| **C2 (RC jacket)** | Crushed concrete + RC jacket | **385 kN** | **1.81 (+81 %)** | $9.0 \times 10^{-3}$ | $15.0 \times 10^{-3}$ | Mesh fracture + flexural-shear |
| **C3 (Steel jacket)**| Buckled rebar + 2.3 mm steel jacket | **420 kN** | **1.97 (+97 %)** | $15.0 \times 10^{-3}$ | **$20.0 \times 10^{-3}$** | Corner plate buckling + ductile |
| **C4 (Recast)** | Crushed retained + recast | 225 kN | 1.06 (+6 %) | $4.5 \times 10^{-3}$ | $6.0 \times 10^{-3}$ | 100 % restoration of original strength |
| **C5 (Grout)** | Crushed retained + non-shrink grout | 260 kN | 1.22 (+22 %) | $5.0 \times 10^{-3}$ | $8.0 \times 10^{-3}$ | Strength increase from high-strength grout |
| **C6 (Direct steel)**| Undamaged + 2.3 mm steel jacket | 340 kN | 1.60 (+60 %) | $10.0 \times 10^{-3}$ | **$20.0 \times 10^{-3}$** | Flexural plastic hinge formation |
| **C7 (CF sheet)** | **Undamaged + 2-ply CF sheets** | **335 kN** | **1.57 (+57 %)** | **$10.0 \times 10^{-3}$** | **$18.0 \times 10^{-3}$** | **CFRP-confined ductile flexure** |
| **C29 (CFRP plate)**| **Damaged + CFRP plate jacket** | **310 kN** | **1.46 (+46 %)** | **$10.0 \times 10^{-3}$** | **$17.0 \times 10^{-3}$** | **Ductile flexural restoration** |

### 2. Practical seismic retrofit implications
- **Elimination of demolition requirements**: Grouting without removing buckled bars or crushed concrete shortened construction schedules by 70 % while exceeding undamaged performance.
- **Advantages of CFRP systems**: Lightweight composite jackets added negligible self-weight and permitted rapid manual installation in confined spaces without welding or heavy machinery.

- **Overall conclusion**: This work established the seismic repair and retrofitting efficacy of CFRP composites and steel jacketing on severely damaged RC columns, demonstrating full shear capacity restoration and substantial ductility enhancement.

## Related Notes

- [[structural-repair-and-retrofitting]] — Seismic retrofitting and section restoration frameworks for RC structures.
- [[abegaz-2013-advanced-frp-frcm-column-confinement]] — Triaxial confinement and sectional geometry effects in FRP/FRCM columns.
- [[foti-2016-polymer-pet-cfrp-concrete-reinforcement]] — Flexural behavior of CFRP and polymer-reinforced concrete.
- [[impact-and-blast-resistance-frcc]] — Dynamic impact and seismic energy dissipation mechanisms.
