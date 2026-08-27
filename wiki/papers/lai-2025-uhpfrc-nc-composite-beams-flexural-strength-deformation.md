---
title: "Flexural strength and deformation behavior of UHPFRC-NC composite beams"
type: source_note
source: "sources/lai-2025-uhpfrc-nc-composite-beam-flexural-strength.pdf"
citation: "Lai, Y., Lee, M., Lai, Z., & Shao, X. (2025). Flexural strength and deformation behavior of UHPFRC-NC composite beams. Journal of Advanced Concrete Technology, 23, 64-78."
date: 2026-08-24
tags: [uhpfrc-nc-composite-beams, flexural-strength, deformation-behavior, strain-compatibility, neutral-axis-migration, xudong-shao, jact, landmark-paper]
---

# Flexural Strength and Deformation Behavior of UHPFRC ($135\ \text{MPa}$) - Normal Concrete (NC) Composite Beams: $60\%$ UHPFRC Reduction, $75\%$ Flexural Capacity Amplification, and Section Analysis Modeling

## Summary

To overcome high material costs in full-depth UHPFRC members while suppressing wide tensile cracking and low ductility in normal concrete (NC) beams, researchers at Hunan University led by Prof. Xudong Shao designed UHPFRC-NC hybrid composite beams ($2400 \times 150 \times 300\ \text{mm}$). The beams feature a thin bottom layer of ultra-high performance fiber-reinforced concrete (UHPFRC: 28 d compressive strength $135.0\ \text{MPa}$, straight steel fibers $V_f = 2.0\ \text{vol.\%}$, tensile strength $9.50\ \text{MPa}$) and an upper compression zone of normal concrete (NC: compressive strength $40.0\ \text{MPa}$). Static 4-point bending tests, neutral axis tracking, strain compatibility analyses, and nonlinear moment-curvature modeling demonstrated a **$110\%$ increase in flexural first-cracking load, a $75\%$ increase in ultimate flexural capacity ($118.5\ \text{kN} \rightarrow 208.0\ \text{kN}$), a $58\%$ reduction in material cost compared to full-depth UHPFRC beams, crack widths tightly restrained to $0.05\ \text{mm}$ under service loads, and complete composite action without interfacial delamination**.

## Key Contributions

1. **Section optimization theory for functionally graded UHPFRC-NC composite beams**:
   - Optimized bottom UHPFRC layer thickness ($h_u/h = 0.25\sim 0.40$), achieving $85\%$ of the flexural capacity of full-depth UHPFRC beams with minimal UHPFRC consumption.
2. **Neutral axis migration and ductile failure in compression-zone NC**:
   - Sustained tensile fiber bridging in the UHPFRC layer drove upward migration of the neutral axis, preventing premature brittle compressive crushing of the upper NC layer.
3. **Prevention of interfacial delamination via surface grooving and monolithic casting**:
   - Maintained interfacial relative slip below $0.02\ \text{mm}$, satisfying the Bernoulli-Euler plane-sections-remain-plane hypothesis up to ultimate load.
4. **Practical flexural design formulas for bridge and building applications**:
   - Formulated a sectional moment equation incorporating UHPFRC tensile softening-hardening bridging stresses ($\sigma_{bt}$), matching experimental capacities within $4.5\%$ error.

## Methods

- **Specimen design and mixture proportions (Section 2, Tables 1–3, Figs. 1–4)**:
  - Dimensions: $2400 \times 150 \times 300\ \text{mm}$ (span $2000\ \text{mm}$, pure bending region $600\ \text{mm}$).
  - Test series: `NC-Beam` (plain NC baseline), `Composite-U75` (75 mm bottom UHPFRC), `Composite-U100` (100 mm UHPFRC), `Composite-U150` (150 mm UHPFRC), `Full-UHPFRC` (full-depth UHPFRC).
  - Material properties: NC ($f_c = 40.0\ \text{MPa}$), UHPFRC ($f_c = 135.0\ \text{MPa}$, $2.0\ \text{vol.}\%$ micro steel fibers), longitudinal rebar HRB400 ($f_y = 435\ \text{MPa}$).
- **Flexural testing protocol (Sections 2.3–2.5, Figs. 5–8)**:
  - 4-point bending under displacement control (0.5 mm/min).
  - Instrumentation: 5 LVDTs for midspan deflections, 8 concrete strain gauges along height, optical microscope for crack widths.

## Results

### 1. First cracking load, ultimate capacity, ductility ratio, crack width, and cost efficiency across configurations (Section 3, Tables 4–6, Figs. 9–15)

| Specimen ID | Bottom UHPFRC Depth ($h_u$, mm) | 1st Crack Load ($P_{cr}$, kN) | Ultimate Load ($P_u$, kN) | Ultimate Deflection ($\delta_u$, mm) | Ductility Index ($\mu$) | Service Crack Width ($W_s$, mm) | Material Cost Reduction (%) |
|---|---|---|---|---|---|---|---|
| **NC-Beam (Control)** | 0 mm (Pure NC) | **$28.5 \pm 1.2\ \text{kN}$** | **$118.5 \pm 4.0\ \text{kN}$** | $18.5 \pm 0.8\ \text{mm}$ | **$2.45 \pm 0.15$ (Low ductility)** | **$0.25 \pm 0.02\ \text{mm}$** | - |
| **Composite-U75** | 75 mm ($0.25h$) | $48.0 \pm 2.0\ \text{kN}$ | $175.0 \pm 5.5\ \text{kN}$ (+48 %) | $28.0 \pm 1.2\ \text{mm}$ | $3.80 \pm 0.20$ | $0.07 \pm 0.01\ \text{mm}$ | **$68.0\%$ savings** |
| **Composite-U100 (Optimal)** | **100 mm ($0.33h$)** | **$60.0 \pm 2.5\ \text{kN}$ (+110 %)** | **$208.0 \pm 6.5\ \text{kN}$ (+75 %)** | **$35.5 \pm 1.5\ \text{mm}$ (+92 %)** | **$4.65 \pm 0.22$ ($1.9\times$)** | **$<0.05\ \text{mm}$ (Ultra-tight)** | **$58.0\%$ savings (Optimal ROI)** |
| **Composite-U150** | 150 mm ($0.50h$) | $68.5 \pm 2.8\ \text{kN}$ | $225.0 \pm 7.0\ \text{kN}$ (+90 %) | $38.0 \pm 1.5\ \text{mm}$ | $4.85 \pm 0.25$ | $<0.05\ \text{mm}$ | $42.0\%$ savings |
| **Full-UHPFRC** | 300 mm ($1.0h$) | **$75.0 \pm 3.0\ \text{kN}$** | **$245.0 \pm 8.0\ \text{kN}$** | $42.0 \pm 1.8\ \text{mm}$ | $5.10 \pm 0.25$ | $<0.03\ \text{mm}$ | 0.0% (Highest cost) |

### 2. Stress redistribution and neutral axis migration mechanics
- **Tensile strain-hardening contribution**: Following rebar yield, the bottom 100 mm UHPFRC layer sustained tensile stresses, maximizing the internal moment arm.
- **Tight crack width ($0.05\ \text{mm}$) confinement**: Crack widths remained tightly constrained, providing durability against chloride attack in marine and freeze-thaw environments.

- **Overall conclusion**: This landmark study demonstrated that optimal bottom placement of UHPFRC in composite beams reduces material costs by 58% while increasing flexural capacity by 75% and constraining crack widths to 0.05 mm.

## Related Notes

- [[cai-2025-nc-uhpc-composite-beams-flexural-behavior]] — Embedded UHPC composite beam flexural behavior.
- [[ge-2023-steel-precast-uhpc-composite-beams-flexural-behavior]] — Precast steel-UHPC composite beam flexure.
- [[high-strength-strain-hardening-composites]] — High-performance composite structures.
- [[concrete-durability-and-service-life]] — Structural durability and crack width criteria.
