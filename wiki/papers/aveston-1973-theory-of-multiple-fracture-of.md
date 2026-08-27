---
title: "Theory of Multiple Fracture of Fibrous Composites (Aveston & Kelly, 1973)"
type: source_note
source: "sources/aveston-1973-theory-of-multiple-fracture-of.pdf"
citation: "Aveston, J., & Kelly, A. (1973). Theory of multiple fracture of fibrous composites. Journal of Materials Science, 8(3), 352-362. https://doi.org/10.1007/BF00550155"
date: 2026-08-24
tags:
  - ack-theory
  - multiple-fracture
  - energy-balance
  - fiber-debonding
  - crack-spacing
  - theoretical-foundations
---

## Summary
A follow-up paper to the landmark ACK theory (Aveston-Cooper-Kelly Theory) by J. Aveston and A. Kelly of the UK National Physical Laboratory (NPL), which established, from an energy balance perspective, the multiple cracking and steady-state crack propagation phenomena that develop when a composite of brittle matrix reinforced with continuous or discontinuous fibers is subjected to uniaxial tensile loading. For both the case of a fully elastic-bonded fiber-matrix interface and the case of a frictional-slip debonded interface, the paper derives the critical crack initiation strain ($\epsilon_{mu}$), the steady-state cracking stress ($\sigma_{mc}$), the saturated crack spacing ($x$), and the nonlinear three-stage response of the composite stress-strain curve (elastic $\rightarrow$ multiple-cracking strain-hardening $\rightarrow$ fiber-dominated extension).

## Key Contributions
- **Completion of the governing energy-balance equation for ACK multiple cracking**: full reconciliation of the external work $\Delta W$, the decrease of matrix strain energy $\Delta U_m$, the increase of fiber strain energy $\Delta U_f$, the interfacial debonding/friction losses $U_d + U_s$, and the matrix surface fracture energy $\gamma_m$.
- **Formulation of the critical matrix cracking strain under frictional interface conditions**: derivation of $\epsilon_{mu} = \left[ \frac{12 \tau \gamma_m E_f V_f^2}{E_c E_m^2 r V_m} \right]^{1/3}$.
- **Establishment of the bounding envelope of the saturated crack spacing ($x$)**: $x' \le x \le 2x'$ ($x' = \frac{V_m \sigma_{mu} r}{2 V_f \tau}$).
- **Provision of the originating theory for the micromechanics of modern highly ductile composites (ECC/SHCC) (PSH criteria)**: established the prototype of Victor Li's steady-state cracking and $J$-integral theory.

## Methods
- Theoretical model: one-dimensional continuum mechanics energy balance $\Delta W = \Delta U_m + \Delta U_f + \Delta U_s + 2 V_m \gamma_m$.
- Interface states: (1) frictional slip interface (constant frictional stress $\tau$), (2) elastic shear interface (shear-lag parameter $\alpha$).
- Analysis variables: fiber volume fraction $V_f$, fiber radius $r$, fiber elastic modulus $E_f$, matrix elastic modulus $E_m$, matrix surface energy $\gamma_m$.

## Results
Comparison table of the principal governing mechanical equations by interface bonding condition according to ACK theory:

| Item | Frictional slip interface (Pure Friction $\tau$) | Elastic bond interface (Elastic Bonding $\tau_{el}$) |
| :--- | :--- | :--- |
| Critical cracking strain $\epsilon_{mu}$ | $\epsilon_{mu} = \left( \frac{12 \tau \gamma_m E_f V_f^2}{E_c E_m^2 r V_m} \right)^{1/3}$ | $\epsilon_{mu} = \left( \frac{2 \gamma_m \alpha E_f V_f}{E_c E_m V_m} \right)^{1/2}$ |
| Minimum transfer length $x'$ | $x' = \frac{V_m \sigma_{mu} r}{2 V_f \tau}$ | $x' = \frac{1}{\alpha} \ln\left(\frac{1}{1-\phi}\right)$ |
| Saturated mean crack spacing $x_{avg}$ | $x_{avg} = 1.337 x' = 1.337 \left(\frac{V_m \sigma_{mu} r}{2 V_f \tau}\right)$ | $x_{avg} = 1.337 x_{el}'$ |
| Condition for multiple fracture | $V_f > V_{f,crit} = \frac{\sigma_{mu}}{\sigma_{fu} + \sigma_{mu} - \sigma_m'}$ | $V_f > V_{f,crit}$ |
| Composite ultimate tensile strength $\sigma_{cu}$ | $\sigma_{cu} = V_f \sigma_{fu}$ | $\sigma_{cu} = V_f \sigma_{fu}$ |

## Related Notes
- [[pseudo-strain-hardening-criteria]] - PSH micromechanics strain-hardening criteria
- [[stang-1986-failure-composites-pullout-fracture]] - fundamentals of fiber pull-out fracture mechanics
- [[fiber-orientation-distribution]] - fiber orientation distribution theory
