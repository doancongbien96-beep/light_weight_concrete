---
title: "Analytical Model for Tensile Behavior of Fiber-Reinforced Concrete (Lim, Paramasivam & Lee, 1987)"
type: source_note
source: "sources/lim-1987-analytical-model-for-tensile-behavior-of-frp.pdf"
citation: "Lim, T. Y., Paramasivam, P., & Lee, S. L. (1987). Analytical model for tensile behavior of steel-fiber-reinforced concrete. ACI Materials Journal, 84(4), 286-298."
date: 2026-08-24
tags:
  - steel-fiber-reinforced-concrete
  - tensile-constitutive-model
  - fiber-pullout
  - post-cracking-behavior
  - analytical-modeling
---

## Summary

A classic paper presenting an early micromechanical analytical model for predicting the uniaxial tensile behavior of steel fiber reinforced concrete (SFRC) and its post-cracking tensile strain-softening stress–displacement curve. By combining the single steel fiber's matrix pull-out load–slip relation with probabilistic distributions of spatially random fiber orientation (two-dimensional and three-dimensional), it establishes an analytical integration technique that quantitatively computes the initial cracking strength, the peak bridging stress, and the tensile softening slope. The flexural plastic-hinge deformation energy of straight and hooked-end steel fibers is incorporated into the model, verifying close agreement with experimental results.

## Key Contributions

- **Analytical integration model established for the steel fiber pull-out mechanism**: presents an analytical solution for the total bridging stress by combining the single-fiber pull-out characteristics ($P-s$) with probability density functions of the orientation angle $\theta$ and embedded length $z$.
- **Modeling of the mechanical anchorage effect of hooked-end steel fibers**: quantifies the additional energy dissipation ($W_{hook}$) due to plastic deformation of the hook bend, beyond the frictional bond of straight fibers.
- **Establishment of the SFRC tensile strain-softening constitutive equation**: provides a uniaxial tensile stress–crack opening displacement ($\sigma-w$) relation directly usable as input to nonlinear finite-element fracture analysis.

## Methods

- Assumption of three-dimensional homogeneous random orientation and numerical integration of planar crack bridging.
- Validation against steel fiber pull-out test data: diameters 0.4 ~ 0.8 mm, lengths 25 ~ 50 mm, $V_f = 0.5 \sim 2.0 \%$.
- Theory–experiment comparison validated against direct tensile test data.

## Results

- Established that the post-cracking residual tensile strength and fracture energy ($G_F$) increase in linear proportion to the steel fiber volume fraction ($V_f$) and aspect ratio ($L_f/d_f$).
- Ordinary steel fibers at $V_f < 2.0 \%$ exhibit gradual tensile strain-softening instead of strain-hardening, providing the basis for subsequent high-ductility fiber design aimed at preventing crack localization.

## Related Notes

- [[fiber-bridging-constitutive-law]] — development lineage of the fiber bridging constitutive equation
- [[uhpc-vs-ecc-design-space]] — comparison of the tensile strain-softening behavior of steel-fiber UHPC with the strain-hardening behavior of ECC
