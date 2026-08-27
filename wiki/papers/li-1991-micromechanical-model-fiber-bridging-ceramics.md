---
title: "A Micromechanical Model of Fiber Bridging in Tough Fibrous Ceramics (Li, Wang & Backer, 1991)"
type: source_note
source: "sources/li_JMPS91.pdf"
citation: "Li, V. C., Wang, Y., & Backer, S. (1991). A micromechanical model of fiber bridging in tough fibrous ceramics. Journal of the Mechanics and Physics of Solids, 39(5), 607-625. https://doi.org/10.1016/0022-5096(91)90043-N"
date: 2026-08-24
tags:
  - fiber-bridging
  - micromechanics
  - snubbing-effect
  - pullout-behavior
  - ceramic-matrix-composites
---

## Summary
A classic seminal paper that, in order to derive the crack-bridging stress-displacement relationship ($\sigma-\delta$ curve) of short-fiber randomly distributed brittle-matrix composites, was the first to mathematically model the matrix-corner friction amplification effect (Snubbing friction) according to the inclination angle $\theta$ of the fiber during pullout, together with the fiber rupture mechanism. Taking inspiration from the Euler-Eytelwein belt friction formula, the friction amplification effect arising when a fiber is embedded obliquely with respect to the crack plane was formalized as the snubbing coefficient $e^{f\theta}$, and the overall crack-bridging constitutive equation was derived by integrating the three-dimensional spatial probability density function of the fiber orientations.

## Key Contributions
- **Introduction and formulation of the snubbing friction coefficient ($f$)**: derived the pullout load amplification expression $P(\theta) = P(0) e^{f\theta}$ for a fiber with inclination angle $\theta$, enabling accurate prediction of the bridging stress of a three-dimensionally random distributed composite.
- **Formulation of the fiber rupture boundary condition ($\sigma_{max} \ge \sigma_{fu}$)**: derived an estimation formula for the critical angle ($\theta_{crit}$) of premature rupture caused by the combined action of the local bending stress at the matrix corner and the tensile pullout stress.
- **Completion of the analytical integral solution of the bridging curve for complete pullout versus partial rupture**: provides a closed-form expression of the two-stage (elastic debonding and frictional slip) bridging stress $\sigma(\delta)$ as a function of the magnitude of the crack opening displacement $\delta$.

## Methods
- Micromechanical shear-lag model and analysis of the inclined fiber pullout mechanism.
- Application of a three-dimensional random fiber orientation probability density function $p(\theta, \phi) = \frac{\sin\theta}{2\pi}$.
- Integration of the bridging stress constitutive equation:
  $$\sigma(\delta) = \frac{4 V_f}{\pi d_f^2} \int_0^{\pi/2} \int_0^{L_f/2} P(z, \theta, \delta) e^{f\theta} \sin\theta \cos\theta \, dz \, d\theta$$

## Results
- Owing to the snubbing effect ($f > 0$), an inclined pullout fiber develops a peak pullout resistance up to 2 ~ 3 times higher than that of a perpendicular pullout fiber, greatly increasing the macroscopic fracture toughness of the composite.
- It was mathematically demonstrated that when the fiber strength $\sigma_{fu}$ is insufficient, the snubbing effect instead induces premature rupture, so that optimal matching between the fiber aspect ratio ($L_f/d_f$) and the interfacial frictional bond ($\tau_0$) is essential.

## Related Notes
- [[fiber-bridging-constitutive-law]] - historical development and mathematical framework of the fiber bridging constitutive law
- [[li-1992-steady-state-cracking-frcc]] - steady-state cracking theory based on the bridging stress curve
- [[interface-bond-properties]] - measurement techniques for interfacial shear friction and the snubbing coefficient
