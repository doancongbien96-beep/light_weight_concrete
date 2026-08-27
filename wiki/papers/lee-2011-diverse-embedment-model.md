---
title: "Diverse Embedment Model for Steel Fiber-Reinforced Concrete in Tension: Model Development (Lee, Cho & Vecchio, 2011)"
type: source_note
source: "sources/2011-diverse-embedment-model-for-steel.pdf"
citation: "Lee, S.-C., Cho, J.-Y., Vecchio, F.J. Diverse embedment model for steel fiber-reinforced concrete in tension: Model development. ACI Materials Journal 108(5) (2011) 516-525."
date: 2026-08-22
tags: [sfrc, pullout-model, fiber-orientation, embedment-length, end-hooked-fiber, tension-model]
---

# Development of the Diverse Embedment Model (DEM) for Tensile Analysis of Steel Fiber-Reinforced Concrete

## Summary

The Diverse Embedment Model (DEM), a tensile stress analysis model accounting for both the random embedment length and orientation angle distributions of steel fibers, was developed. The two-sided embedded pullout behavior of a single fiber was separated into frictional bonding plus mechanical anchorage (end-hooked), and the restraint effect of finite member dimensions on the orientation distribution was also incorporated. The model supplements limitations of the Variable Engagement Model (VEM): its uniform bond stress assumption and single-sided slip assumption.

## Key Contributions

1. Formulation of two-sided embedded pullout: equilibrium equations for the short-side and long-side slips were derived from the compatibility condition that crack width equals the sum of slips on both sides (Eqs. 2~3). At maximum fiber stress, the crack width changes from s_f to 2s_f depending on embedment ratio (VEM always assumes s_f fixed).
2. Inclination angle effect: snub head slip increases with cos²θ (Eq. 7), and the critical crack width is w_pq = s_f[1+4(l_a/l_f)²]/cos²θ. A simplification holding frictional strength constant was adopted (including reconciliation of conflicting literature findings by Banthia-Trottier versus Ouyang et al.).
3. Mechanical anchorage model for end-hooked fibers: anchorage strength was idealized as parabolic before snub-head engagement and linear afterward, vanishing when slip exceeds the hook length (Eq. 14). It is treated as an independent parallel contribution to the friction mechanism.
4. Generalization of the orientation coefficient α_f: local orientation coefficients were derived for both 2D (member thickness restraint truncating θ_l~θ_u) and 3D (thickness + width restraint), embedding member size effects probabilistically.
5. Verification of the rigid body translation assumption: numerical solutions of the two-stage pullout analysis (Runge-Kutta) confirmed that elastic fiber deformation is negligible compared to slip.

## Methods

Governing equation (shear-lag type differential equation) + bilinear bond-slip law (Nammur-Naaman); effective concrete diameter 15d_f (CEB-FIP MC90). Orientation effects were idealized using single-fiber pullout test data (including Banthia-Trottier crimped fibers). Validation is reported in the companion paper (Lee et al. 2011, ACI MJ 108(5):526-535).

## Results

- The fiber stress-crack width relationship can be approximated as bilinear.
- The crack-width-based fiber stress expressions (Eqs. 8~10) determine rupture: fracture occurs when the maximum experienced stress exceeds the fiber tensile strength.

## Related Notes

- [[kang-2008-fiber-orientation-impacts-on-the]] — Experimental counterpart showing orientation effects on measured strength (+61 % in flexure). DEM provides its prediction frame.
- Contrasted with the snubbing/orientation discussion in [[li-wu-1992-psh-design-hpfrcc]]: DEM addresses steel fibers (mechanical anchorage), while PSH theory centers on polymer fibers (friction + slip-hardening).
- [[fiber-bridging-constitutive-law]] — The steel-fiber version of statistical synthesis of σ_B(δ).
- [[qiu-2016-fatigue-dependent-fiber-bridging-model]] — Extends the same stochastic averaging (embedment length and orientation distributions) to fatigue degradation conditions; shares the single-fiber pullout → bridging synthesis structure.
