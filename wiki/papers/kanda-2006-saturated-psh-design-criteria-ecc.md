---
title: "Practical Design Criteria for Saturated Pseudo Strain Hardening Behavior in ECC"
type: source_note
source: "sources/Kanda-2006-Practical design criteria for satur.pdf"
citation: "Kanda, T. & Li, V. C. (2006). Practical Design Criteria for Saturated Pseudo Strain Hardening Behavior in ECC. Journal of Advanced Concrete Technology, 4(1), 59-72."
date: 2026-08-24
tags: [ecc, pseudo-strain-hardening, psh-saturation, performance-index, design-criteria, complementary-energy, first-cracking-strength, crack-spacing, micromechanics, victor-li, tetsushi-kanda, jact, landmark-paper]
---

# Practical Design Criteria for Saturated Pseudo-Strain-Hardening (PSH) in Fiber-Rupturing ECC: Concurrent Satisfaction of Energy Index ($J_b'/J_{tip} > 2.7$) and Stress Index ($\sigma_{peak}/\sigma_{fc} > 1.3$)

## Summary

To establish quantitative material design criteria ensuring that engineered cementitious composites (ECC) achieve fully saturated pseudo-strain-hardening (Saturated PSH)—where crack spacing converges to the theoretical saturation spacing $x_d$—Dr. Tetsushi Kanda at Kajima Corporation and Professor Victor C. Li at the University of Michigan evaluated five ECC formulations containing fiber-rupturing PVA and PE fibers ($V_f = 1.5\sim 2.0\%$, $d_f = 14\sim 40\ \mu\text{m}$, W/C $= 27\sim 42\%$). The authors formulated two micromechanics-based performance indices: (1) **Energy Performance Index $J_b'/J_{tip}$** (fiber bridging complementary energy to matrix crack tip toughness ratio) and (2) **Stress Performance Index $\sigma_{peak}/(\sigma_{fc})_i$** (peak bridging stress to initial matrix cracking strength ratio). Correlating these indices with experimental PSH saturation ratios ($x_d^{test}/x_d$), the study proved that **simultaneous satisfaction of $J_b'/J_{tip} > 2.7$ and $\sigma_{peak}/(\sigma_{fc})_i > 1.3$ serves as the practical design criterion for saturated PSH**. While PE-ECC ($V_f = 2.0\%$, $d_f = 38\ \mu\text{m}$) achieved $J_b'/J_{tip} = 17.9$ and $\sigma_{peak}/(\sigma_{fc})_i = 4.0$ with fully saturated PSH (tensile strain > 4 %), PVA $14\ \mu\text{m}$ ECC (W/C = 27 %) fell short ($J_b'/J_{tip} = 2.1$, $\sigma_{peak}/(\sigma_{fc})_i = 1.2$), accurately explaining its unsaturated PSH response.

## Key Contributions

1. **First quantitative formulation of 2 performance indices for saturated PSH**:
   - **Energy criterion**: $J_b'/J_{tip} > 2.7$ (complementary energy at least 2.7 times matrix tip toughness).
   - **Stress criterion**: $\sigma_{peak}/(\sigma_{fc})_i > 1.3$ (peak bridging stress at least 1.3 times first cracking strength).
   - Proved experimentally that concurrent satisfaction of both criteria is necessary and sufficient for saturated PSH.
2. **Formulation of initial cracking strength ($\sigma_{fc}$) dependence on flaw size ($c_m$)**:
   - Derived closed-form solutions for matrix cracking from penny-shaped flaws combining Griffith-Irwin mechanics and bridging shielding ($K_B$), incorporating a 0.8 flaw reduction factor.
3. **Correlation between PSH saturation index ($x_d^{test}/x_d$) and tensile strain capacity**:
   - Demonstrated that achieving $x_d^{test}/x_d \ge 1.5$ reliably secures tensile strain capacity > 4 %, below which ductility drops sharply.
4. **Numerical calculation methodology for fiber-rupture-inclusive complementary energy ($J_b'$)**:
   - Extended the Li and Leung (1992) penny-shaped crack bridging formulation to five ECC mixtures, rigorously matching theoretical predictions with experiments.

## Methods

- **Five ECC mixtures (Tables 1–3)**:
  - **PVA-14 (W/C 42 %)**: 14 $\mu\text{m}$ PVA fiber, $V_f = 1.5\%$, $L_f = 12\ \text{mm}$, $\sigma_{fu} = 1690\ \text{MPa}$, $E_f = 42.8\ \text{GPa}$, W/C = 0.42.
  - **PVA-14 (W/C 27 %)**: 14 $\mu\text{m}$ PVA fiber, $V_f = 1.5\%$, $L_f = 12\ \text{mm}$, W/C = 0.27 (high-strength matrix).
  - **PVA-40 (W/C 42 %)**: 40 $\mu\text{m}$ PVA fiber, $V_f = 1.5\%$, $L_f = 12\ \text{mm}$, $\sigma_{fu} = 1092\ \text{MPa}$, $E_f = 25\ \text{GPa}$, W/C = 0.42.
  - **PVA-40 (W/C 27 %)**: 40 $\mu\text{m}$ PVA fiber, $V_f = 1.5\%$, W/C = 0.27.
  - **PE-38**: 38 $\mu\text{m}$ high-strength PE fiber, $V_f = 2.0\%$, $L_f = 12\ \text{mm}$, $\sigma_{fu} = 2610\ \text{MPa}$, $E_f = 120\ \text{GPa}$.
- **Micromechanical parameters (Table 3)**:
  - Interfacial properties ($G_d, \tau_0, f, \xi$) derived from single fiber pullout tests and literature.
- **Testing program (Section 4 & Figs. 1–4)**:
  - Direct tension: Dumbbell specimens ($30\ \text{mm} \times 12\ \text{mm}$ cross section, 100 mm gauge length, 0.2 mm/min).
  - Matrix toughness ($K_m$): SENB three-point notched beam testing per RILEM.
  - Single fiber pullout: Inverting $\tau_0, G_d$ interface parameters.

## Results

### 1. Performance indices and PSH saturation across five ECC mixtures (Tables 4–5 & Figs. 10–14)

| ECC Mixture Type | Fiber Type / Diameter | W/C (%) | $J_b'/J_{tip}$ | $\sigma_{peak}/(\sigma_{fc})_i$ | PSH Saturation ($x_d^{test}/x_d$) | Tensile Strain Capacity ($\varepsilon_u$, %) | PSH State |
|---|---|---|---|---|---|---|---|
| **PE-38** | **PE / 38 $\mu$m** | **45 %** | **17.9 (Highest)** | **4.0 (Highest)** | **$\ge 1.5$ (Saturated)** | **> 4.0 % (Saturated)** | **Fully saturated PSH** |
| **PVA-14 (W/C 42 %)** | PVA / 14 $\mu$m | 42 % | **5.0** | **1.8** | $\ge 1.5$ | 2.5~3.5 % | **Saturated** |
| **PVA-40 (W/C 42 %)** | PVA / 40 $\mu$m | 42 % | **4.5** | **1.6** | 1.2~1.5 | 1.5~2.5 % | **Sub-saturated** |
| **PVA-40 (W/C 27 %)** | PVA / 40 $\mu$m | 27 % | **3.2** | **1.4** | 1.0~1.2 | 0.8~1.5 % | **Marginal PSH** |
| **PVA-14 (W/C 27 %)** | PVA / 14 $\mu$m | 27 % | **2.1 (Sub-critical)** | **1.2 (Sub-critical)** | **< 1.0 (Unsaturated)** | **< 0.5 %** | **Unsaturated PSH** |

### 2. Physical interpretation of saturated PSH criteria
- **Energy criterion ($J_b'/J_{tip} > 2.7$)**: Serves as the necessary condition for steady-state flat cracking, ensuring that fiber bridging energy dissipated across crack faces significantly exceeds matrix fracture energy.
- **Stress criterion ($\sigma_{peak}/(\sigma_{fc})_i > 1.3$)**: Ensures that bridging capacity surpasses the cracking strength of internal flaws (up to size $c_m$) with a 0.8 safety factor to sustain sequential crack initiation until complete saturation.
- **Influence of W/C ratio**: Higher W/C lowers matrix strength, reducing $\sigma_{fc}$ and raising the stress index, but also alters interfacial bonding ($G_d, \tau_0$), requiring micromechanical balancing.

- **Overall conclusion**: This seminal work formulated and experimentally validated the concurrent criteria of $J_b'/J_{tip} > 2.7$ and $\sigma_{peak}/(\sigma_{fc})_i > 1.3$ for achieving saturated PSH in ECC.

## Related Notes

- [[strain-hardening-mechanism]] — Core theory of ECC strain-hardening micromechanics and energy/strength criteria.
- [[fiber-bridging-constitutive-law]] — Bridging stress-crack opening constitutive law and complementary energy ($J_b'$).
- [[kim-2009-modified-fiber-bridging-curve-ecc-tensile]] — Modified fiber bridging curves and matrix micromechanical design.
- [[high-strength-strain-hardening-composites]] — Design principles for high-strength strain-hardening composites (UHPC/UHP-ECC).
