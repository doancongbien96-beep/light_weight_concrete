---
title: "A J-integral method for calculating steady-state matrix cracking stresses in composites"
type: source_note
source: "sources/marshall-1988-a-j-integral-method-for-calculating.pdf"
citation: "Marshall, D. B., & Cox, B. N. (1988). A J-integral method for calculating steady-state matrix cracking stresses in composites. Mechanics of Materials, 7(2), 127-133."
date: 2026-08-24
tags: [j-integral, steady-state-cracking, fiber-bridging, complementary-energy, matrix-fracture-toughness, micromechanics, ack-theory, landmark-paper]
---

# Establishment of the J-integral (J-Integral) energy-equilibrium analytical solution for computing the steady-state crack propagation stress ($\sigma_{ss}$) and bridging complementary energy ($J_b'$) of fiber-bridged composites

## Summary

To derive the critical matrix cracking stress ($\sigma_{ss}$) at which a crack tip extends in the steady state (steady-state) while maintaining a constant opening displacement without any further load increase in brittle-matrix composites (ceramic/cementitious) reinforced with short and continuous fibers, this immortal landmark origin paper by Dr. D.B. Marshall and Dr. B.N. Cox of Rockwell International Science Center, published in Mechanics of Materials in 1988, established for the first time in the world the **J-integral closed-contour energy-conservation path analysis method** connecting the crack tip and the far-field boundary, and rigorously derived the correlation $J_{tip} = \sigma_{ss} \delta_0 - \int_0^{\delta_0} \sigma_B(\delta) d\delta$ between the bridging stress-opening displacement curve ($\sigma_B-\delta$) of the bridging ligament and the matrix fracture toughness ($J_{tip} = K_m^2/E_m$), thereby completing the mathematical foundation of the pseudo strain-hardening (PSH) energy criterion ($J_b'/J_{tip} \ge 1.0$) of modern ECC.

## Key Contributions

1. **First derivation of the J-integral energy governing equation for steady-state matrix cracking**:
   - Without analyzing the complex stress concentrations along the crack trajectory, the difference between the far-field stress work and the deformation energy of the bridging ligament is rigorously formalized through the J-integral, completing the formula for the critical stress $\sigma_{ss}$.
2. **Establishment of the bridging complementary energy (complementary energy, $J_b'$) concept**:
   - Proved the fracture-mechanical law that when $J_b' = \sigma_{ss} \delta_0 - \int_0^{\delta_0} \sigma_B(\delta) d\delta$ reaches equilibrium with the matrix fracture toughness $J_{tip}$, the crack propagates indefinitely in the steady state.
3. **Secured universal extensibility to residual stress and nonlinear interfacial bridging behavior**:
   - Fully integrated into a single analytical solution the influence on $\sigma_{ss}$ of internal residual tensile/compressive stresses in the matrix caused by thermal expansion coefficient mismatch or hydration shrinkage.
4. **Proved mathematical consistency with the ACK (Aveston-Cooper-Kelly) and Budiansky-Hutchinson-Evans models**:
   - Under the frictional interface condition ($\tau = \text{const}$), proved that the J-integral analytical solution of Marshall-Cox coincides exactly with the results of the earlier complex energy-balance integrations.

## Methods

- **J-integral closed-contour path analysis (Section 2 & Fig. 2)**:
  - J-integral conservation law over the closed contour $\Gamma = \Gamma_0 + \Gamma_B + \Gamma_\infty$ surrounding the crack tip:
    $\oint_\Gamma \left( W dy - T_i \frac{\partial u_i}{\partial x} ds \right) = 0$
  - Far-field boundary ($\Gamma_\infty$) contribution: $J_\infty = \sigma_{ss} \delta_0$.
  - Crack-face bridging zone ($\Gamma_B$) contribution: $J_B = -\int_0^{\delta_0} \sigma_B(\delta) d\delta$.
  - Crack tip ($\Gamma_0$) contribution: $J_{tip} = \frac{K_m^2 (1-\nu^2)}{E_m}$.
- **Derivation of the energy-conservation governing equation**:
  $J_{tip} = \sigma_{ss} \delta_0 - \int_0^{\delta_0} \sigma_B(\delta) d\delta \equiv J_b'(\delta_0)$

## Results

### 1. Comparison of the Marshall-Cox J-integral model with classical composite cracking theories (Sections 2~4)

| Fracture mechanics model | Developer and year | Applicable crack mode | Governing equation for the critical matrix cracking stress ($\sigma_{ss}$ or $\sigma_{mc}$) | Representation of bridging interface behavior |
|---|---|---|---|---|
| **ACK Theory** | Aveston et al. (1971) | One-dimensional continuous fiber | $\sigma_{mc} = \left[ \frac{12 \tau \gamma_m E_f V_f^2 E_c^2}{(1-V_f) E_m^2 r} \right]^{1/3}$ | Limited to constant friction ($\tau_0$) |
| **BHE Model** | Budiansky et al. (1986) | Three-dimensional continuous fiber | $\sigma_{ss} = 2 \left( \frac{V_f^2 E_f E_c^2 \tau K_m^2}{r E_m} \right)^{1/3}$ | Complex energy integration for continuous fibers |
| **Marshall-Cox (proposed)** | **Marshall & Cox (1988)** | **Universal for short/continuous fibers** | **$J_{tip} = \sigma_{ss} \delta_0 - \int_0^{\delta_0} \sigma_B(\delta) d\delta$** | **Any arbitrary nonlinear $\sigma_B(\delta)$ fully applicable** |

### 2. Connection between bridging complementary energy and the ECC strain-hardening saturation mechanism

- **Physical meaning of steady-state crack propagation**: once the crack tip opening displacement reaches $\delta_0$, the tip stress intensity factor $K_{tip}$ becomes pinned at the matrix fracture toughness $K_{m}$, so the crack propagates indefinitely in parallel even without further load increase.
- **Development toward the multiple microcracking regime**: if the crack bridging complementary energy $J_b'$ exceeds the matrix crack-tip toughness $J_{tip}$ ($J_b' \ge J_{tip}$), the material does not fail abruptly; new microcracks continue to form at other flaw locations, delivering enormous pseudo strain-hardening (PSH) strain capacity.

- **Overall conclusion**: This paper, in which Marshall and Cox harnessed the closed-contour path independence of the J-integral to complete the steady-state crack propagation stress of fiber-bridged composites and the bridging complementary energy equilibrium in the most elegant and simple analytical form, is an immortal supreme classic origin paper of modern composite fracture mechanics and ECC micromechanics-based design.

## Related Notes

- [[li-1991-micromechanical-model-tension-softening-bridging]] — Victor Li: origin of the fiber-bridging tension-softening and PSH micromechanics model.
- [[li-1995-matrix-design-for-pseudo-strain-hardening]] — Victor Li: origin of the PSH composite matrix design guideline.
- [[lin-1997-crack-bridging-slip-hardening-interfaces]] — Lin & Li: origin of the slip-hardening interface crack-bridging analytical solution.
- [[strain-hardening-mechanism]] — theoretical framework of ECC strain-hardening micromechanics.
