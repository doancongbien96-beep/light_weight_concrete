---
title: "Steady-State and Multiple Cracking of Short Random Fiber Reinforced Brittle Matrix Composites (Li & Leung, 1993)"
type: source_note
source: "sources/jsce_paper93.pdf"
citation: "Li, V. C., & Leung, C. K. Y. (1993). Steady-state and multiple cracking of short random fiber reinforced brittle matrix composites. Journal of Materials in Civil Engineering (JSCE Proceedings), 1993(478), 23-32."
date: 2026-08-24
tags:
  - steady-state-cracking
  - multiple-cracking
  - micromechanics
  - engineered-cementitious-composites
  - fiber-bridging
---

## Summary

A monumental origin paper that established the theoretical fracture-mechanics and micromechanical criteria for multiple cracking and steady-state crack propagation in short random fiber reinforced brittle matrix composites. It formalized the stress magnification at a planar crack tip and the crack-opening restraint effect of the fiber bridging stress ($\sigma(\delta)$) within a $J$-integral energy equilibrium model. It mathematically derived the conditions $\sigma_0 > \sigma_{ss}$ and $J_b' > J_{tip}$ required for a crack to propagate flat (flat crack propagation) while maintaining a constant crack width ($\delta_{ss}$) rather than opening without limit at an arbitrary location, and provided the formula for the critical fiber volume fraction ($V_f^{crit}$), the core of ECC design.

## Key Contributions

- **Derivation of the steady-state crack opening energy equilibrium equation**:
  $$J_{tip} = \sigma_{ss} \delta_{ss} - \int_0^{\delta_{ss}} \sigma(\delta) d\delta = J_b'$$
  Formalizes that the energy demanded by the matrix crack-tip fracture toughness must be smaller than the complementary energy of the fiber bridging curve.
- **Linking the multiple cracking strength condition ($\sigma_{cu} > \sigma_{fc}$) with the steady-state condition**: establishes the condition that beyond the first cracking strength ($\sigma_{fc}$), bridging fibers do not rupture but carry additional load and redistribute stress into the adjacent matrix.
- **Introduction of the snubbing coefficient ($f$) for random 3D fiber orientation**: incorporates into the bridging constitutive law the snubbing friction amplification effect ($e^{f\theta}$) that arises when a fiber pulls out at an angle $\theta$ to the matrix crack plane.

## Methods

- Application of the fracture-mechanics Griffith crack model and the Barenblatt cohesive bridging zone model.
- Fiber pullout micromechanics model: frictional bond ($\tau_0$), fiber diameter ($d_f$), length ($L_f$), volume fraction ($V_f$), matrix elastic modulus ($E_m$).
- Derivation of analytical solutions for the steady-state stress $\sigma_{ss}$ and the steady-state crack width $\delta_{ss}$.

## Results

- When the fiber content exceeds the critical volume fraction $V_f^{crit}$, increasing tensile load produces numerous microcracks sequentially up to saturation instead of localization into a single dominant crack — pseudo strain-hardening is exhibited.
- Proved that with optimized frictional bond and a snubbing coefficient ($f \approx 0.5 \sim 0.8$), ultra-high tensile strain capacity at the level of $3 \sim 5 \%$ can be achieved with a small fiber content of $V_f = 2.0 \%$ or less.

## Related Notes

- [[pseudo-strain-hardening-criteria]] — PSH index design criteria for strain-hardening and multiple-cracking determination.
- [[fiber-bridging-constitutive-law]] — derivation and parametric analysis of the short-fiber bridging constitutive law.
- [[strain-hardening-mechanism]] — micromechanics of tensile strain-hardening in cementitious composites.
