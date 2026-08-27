---
title: "Interface Property and Apparent Strength of High-Strength Hydrophilic Fiber in Cement Matrix (Kanda & Li, 1998)"
type: source_note
source: "sources/Interface Property and Apparent Strength of a.pdf"
citation: "Kanda, T., Li, V.C. Interface property and apparent strength of high-strength hydrophilic fiber in cement matrix. Journal of Materials in Civil Engineering 10(1) (1998) 5-13."
date: 2026-08-22
tags: [pva-fiber, fiber-matrix-interface, chemical-bond, frictional-bond, apparent-fiber-strength, single-fiber-pullout, micromechanics]
---

# Interface Property and Apparent Strength of High-Strength Hydrophilic Fiber in Cement Matrix

## Summary

This foundational paper quantifies the chemical bond and frictional bond strengths of PVA fibers (14 μm and 40 μm) through single fiber pullout tests, and quantifies the degradation of apparent fiber strength via embedded pull-to-rupture tests in cement matrices. While hydrophilic high-strength fibers exhibit unexpectedly high interfacial bond strength, their effective in-situ strength decreases markedly as the fiber inclination angle relative to the crack plane increases, explaining why composite performance does not scale directly with intrinsic fiber strength. This work provides the foundational experimental data for PVA interface parameters ($\tau_0, \tau_f, f'$) in ECC micromechanical design.

## Key Contributions

1. **First quantitative characterization of PVA fiber interfacial properties**: Chemical debonding strength $\tau_0 \approx 29\text{--}37\ \text{MPa}$, frictional bond strength $\tau_f \approx 2.2\text{--}4.4\ \text{MPa}$. These values are significantly higher than those of hydrophobic fibers (PE 1.02 MPa, nylon 0.16 MPa, Li et al. 1990) due to hydrogen bonding from PVA hydroxyl (-OH) groups.
2. **Independence of $\tau_0$ and sensitivity of $\tau_f$ to matrix W/C**: $\tau_0$ remained stable regardless of matrix W/C (27/42/62 %) and fiber diameter/surface treatment, whereas $\tau_f$ decreased with increasing W/C. Interpreted via Coulomb friction: lower matrix elastic modulus at high W/C reduced residual normal stresses, and higher ITZ porosity reduced contact area, lowering $\tau_f$.
3. **Quantification of apparent fiber strength reduction**: Fixed-end intrinsic strength of approximately 1,900 MPa dropped to ~1,700 MPa under 0° embedded pullout (due to surface abrasion during debonding slip), and degraded further to ~1,000 MPa at an inclination angle of 75° (a 40 % reduction from 0° to 75°). Proposed an apparent strength reduction coefficient $f' \approx 0.3/\text{rad}$ in the form $\sigma_{fu}(\phi) = \sigma'_u \exp(-f'\phi)$ (Eq. 3).
4. **Critical embedment length formulation ($l_{e,crit}$)**: Showed that combining fiber snubbing ($f$) with apparent strength reduction ($f'$) further reduces $l_{e,crit}$ (Eq. 4), establishing the theoretical foundation for microfiber pullout test design (limiting embedment length to produce pullout rather than rupture).
5. **Three strength degradation mechanisms**: Discussed (i) slip abrasion during debonding, (ii) localized matrix spalling at high inclination angles (>60°), and (iii) flexural tensile stress concentration at the exit point (estimated at ~650 MPa at 75°), suggesting synergistic rather than additive interactions.

## Methods

- **Single fiber pullout testing**: Katz-Li (1996) microfiber testing procedure with embedment lengths of 0.3–1.2 mm (representative 0.5 mm), free length of 1 mm, 1 N mini load cell, and real-time optical microscopy (50x magnification). Specimens mounted on aluminum plates via superglue at 4 corners to minimize boundary constraints.
- **Analytical inversion**: Inverted $\tau_0$ and $\tau_f$ from peak load $P_a$ and post-debond load $P_b$ using the Leung-Li (1991) strength-controlled debonding model (Eqs. 1–2). Assumed effective radius R* = 2.5 mm, $V_m = 1$, and calculated matrix modulus $E_m$ using Hirsch's (1962) model. First peak displacement corrected for system compliance (0.385 mm/N) from fixed-end tests to ensure reliable $P_a/P_b$ discrimination (Appendix I).
- **Materials**: 2 types of PVA fibers—14 μm (density 1.3 kg/L, tensile strength 2,254 MPa, E_f 60 GPa, elongation 5 %) and 40 μm (tensile strength 1,250 MPa, E_f 22 GPa, elongation 5.7 %). 3 matrix pastes—W/C 27 % (silica fume 0.8 + superplasticizer 0.27), W/C 42 %, and W/C 62 % (with thickeners).
- **Two series of apparent strength tests**: (a) Embedded pull-to-rupture with ~5 mm embedment length to induce rupture at angles of 0/15/30/45/60/75° (14 μm + W/C 27 %); (b) Fixed-end tests with dual glued ends (similar to ASTM D 2101) to isolate boundary effects.

## Results

| Parameter | Value |
|---|---|
| Chemical bond $\tau_0$ | 29–37 MPa (stable across W/C and fiber types) |
| Frictional bond $\tau_f$ | 2.2–4.4 MPa (decreased with higher W/C, lower for 40 μm) |
| Fixed-end strength | ≈ 1,900 MPa |
| Embedded 0° apparent strength | ≈ 1,700 MPa |
| 75° apparent strength | ≈ 1,000 MPa (~40 % reduction from 0°) |
| Strength reduction factor $f'$ | ≈ 0.3 /rad (curve fitting) |

- Observed slip-hardening (secondary load peak after initial drop) during pullout, attributed to surface abrasion matching plasma-treated PE behavior (Li et al. 1996).
- Rupture cross-sections at 45° showed failure occurring inside the original matrix (mean slip-out 43 μm) with calculated debond length L_d ≈ 0.9 mm << 5 mm, confirming rupture during ongoing debonding.
- Model validation (Appendix II): Reconstructed $P_a\text{--}l_e$ curves closely matched experimental trends (theoretical debond length 554 μm vs measured 539 μm; peak displacement 18 μm vs corrected measurement 13 μm).
- The authors noted that τ₀ ≈ 30–40 MPa (30–40 MPa) exceeds paste shear strength and represents a phenomenological parameter, but applies directly to composite crack bridging without scale effects.

## Related Notes

- [[kanda-2006-saturated-psh-design-criteria-ecc]] — Follow-up extending interface and apparent strength data into PSH performance index design.
- [[li-wu-1992-psh-conditions]] — Original PSH theory; this paper provides experimental parameters ($\tau_0, \tau_f, f, f'$) for PVA systems.
- [[pseudo-strain-hardening-criteria]] — Experimental origin of micromechanical input parameters.
- [[fiber-bridging-constitutive-law]] — Origin of the $f'$ concept in fiber-rupture-inclusive $\sigma_B(\delta)$ relations.
- [[li-2023-ecc-micromechanics-critical-review]] — Historical review of interfacial characterization lineage.
- [[qiu-2016-fatigue-dependent-fiber-bridging-model]] — Fatigue bridging model using PVA interface inputs ($\tau_0$, slip-hardening coefficients).
- [[li-2001-pva-ecc-strain-hardening]] — Representative demonstration of PVA-ECC.
- [[park-2012-tensile-behavior-uhp-hfrc]] — UHP-HFRC (200 MPa matrix + 1 % macro-fibers + micro-fibers) direct tension across 16 series with T-fiber peak (18.6 MPa, 0.64 %).
- [[lin-1999-interface-property-characterization]] — Extension of the 3-parameter interface model into closed-form $\sigma(\delta)$ relationships.
