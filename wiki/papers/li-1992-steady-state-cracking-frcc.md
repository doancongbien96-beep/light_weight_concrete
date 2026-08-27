---
title: "Steady-State Cracking of Fiber-Reinforced Brittle-Matrix Composites (Li & Leung, 1992)"
type: source_note
source: "sources/li_JEM92_steady_state.pdf"
citation: "Li, V. C., & Leung, C. K. Y. (1992). Steady-state cracking of fiber-reinforced brittle-matrix composites. Journal of Engineering Mechanics, ASCE, 118(11), 2246-2264. https://doi.org/10.1061/(ASCE)0733-9399(1992)118:11(2246)"
date: 2026-08-24
tags:
  - steady-state-cracking
  - fracture-mechanics
  - fiber-bridging
  - engineered-cementitious-composites
  - j-integral
---

## Summary

The historic origin paper that formalized, via $J$-integral fracture mechanics theory, the interaction between crack-tip fracture energy and the stress-displacement history of bridging fibers in fiber-reinforced brittle-matrix composites, thereby mathematically establishing the opening and propagation conditions of the steady-state crack. It derived the conditions under which, once the crack-tip stress intensity factor reaches the critical fracture toughness ($K_m$) and the trailing fiber bridging zone reaches an equilibrium stress state, the crack propagates along a flat crack plane under no load increase, or a mild load increase, while maintaining a constant steady-state opening ($\delta_{ss}$). Extending the Marshall-Cox-Evans (MCE) continuous-fiber theory to short-fiber randomly dispersed composites completed the foundation of ECC micromechanics design theory.

## Key Contributions
- **Establishment of the steady-state crack energy equilibrium condition for short-fiber composites**:
  $$J_{tip} = \frac{K_m^2}{E_m} = \sigma_{ss} \delta_{ss} - \int_0^{\delta_{ss}} \sigma(\delta) d\delta$$
  The steady-state stress $\sigma_{ss}$ and steady-state crack width $\delta_{ss}$ are derived directly from the fiber bridging law $\sigma(\delta)$.
- **Analytical closed-form solution for the critical fiber volume fraction ($V_f^{crit}$)**:
  $$V_f^{crit} = \frac{12 K_m^2 E_m}{g \tau_0 E_f (L_f/d_f) \sigma_{fu}^2}$$
  A dimensionless design formula relating fiber diameter, length, strength, frictional bond, and matrix fracture toughness.
- **Boundary between brittle fracture and ductile strain-hardening established**: proving that when the condition $\sigma_{ss} \le \sigma_0$ (bridging peak stress) is satisfied, single-crack fracture is suppressed and multiple steady-state cracking is induced.

## Methods
- Nonlinear fracture mechanics and $J$-integral path analysis.
- Micromechanical modeling of orientation and pullout of three-dimensional random short fibers.
- Derivation of crack profile shape functions for cantilever and plate tension specimens.

## Results
- Under the condition $V_f > V_f^{crit}$, the crack tip maintains a constant $J_{tip}$ and propagates flat, and the composite as a whole does not fail but forms continuous multiple cracking.
- Mathematically demonstrated that lowering the matrix toughness ($K_m$) and optimizing the fiber frictional bond ($\tau_0$) and aspect ratio ($L_f/d_f$) can lower $V_f^{crit}$ to the $1.0 \sim 2.0 \%$ level.

## Related Notes
- [[li-1993-steady-state-multiple-cracking-frcc]] - comprehensive completion paper of the steady-state and multiple cracking theories
- [[pseudo-strain-hardening-criteria]] - PSH criterion index system based on steady-state crack energy
- [[fiber-bridging-constitutive-law]] - foundational theory of the fiber bridging constitutive equation
