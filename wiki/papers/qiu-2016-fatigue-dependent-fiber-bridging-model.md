---
title: "Micromechanics-based Fatigue Dependent Fiber-Bridging Constitutive Model (Qiu & Yang, 2016)"
type: source_note
source: "sources/A micromechanics-based fatigue briding.pdf"
citation: "Qiu, J., Yang, E.-H. A micromechanics-based fatigue dependent fiber-bridging constitutive model. Cement and Concrete Research 90 (2016) 117-126."
date: 2026-08-22
tags: [fatigue, fiber-bridging, micromechanics, single-fiber-pullout, pva-fiber, interface-hardening]
---

# Fatigue-Dependent Fiber-Bridging Constitutive Model (Micromechanics Model)

## Summary

The first analytical multiscale model that predicts fatigue-induced degradation of FRCC fiber bridging (the σ-δ curve). At the micro scale it employs post-fatigue single-fiber pullout (P-u curves), while at the macro scale it incorporates the statistics of fiber location and orientation and the fatigue-driven reduction of in-situ fiber strength to compute σ(δ, N, σ_max). The key finding is that the chemical bond G_d is fatigue-invariant, whereas the frictional bond τ_0 actually hardens (interface hardening) with cycle number and load level, and that this triggers premature fiber rupture, lowering the peak bridging stress σ_0 and the dissipated energy.

## Key Contributions

1. Paris-law-type formulation of fatigue-induced debonding: tunnel crack propagation Δa = N_d·C·(P_max - P_0)^M (C and M material constants; P_0 threshold). The threshold P_0 is determined analytically from G_d, E_f, and d_f.
2. Quantification of two aspects of fatigue interface hardening: both the debonding-stage hardening coefficient γ_d(N_d, P_max) and the slip-stage hardening coefficient γ_s(N_s, P_max) increase linearly with log N and as a power function of P_max. The causes are repeated-slip damage of the ductile fiber surface and a debris jamming effect.
3. Fatigue reduction formula for in-situ fiber strength: σ_fu(φ, N) = σ_fu(0, 1)·e^(-f'φ)·[1 - f''·log N]. Orientation factor f' = 0.33; fatigue coefficients f'' = 0.0649 (no oil)/0.0536 (oil coating).
4. Validation: reproduces post-fatigue P-u curves well — under non-debonded conditions (P_max 0.35 N, N up to 5×10⁵) measured Pa 0.513~0.592 N vs predicted 0.546~0.610 N, Pb measured 0.388~0.443 vs predicted 0.445~0.497; under fully debonded conditions (P_max ≥ 0.5 N) as well, the Pa error stayed within about 10 %.
5. Predicted evolution of σ(δ): the rising branch is strengthened by interface hardening, but the peak σ_0 decreases and the dissipated energy (area under the curve) shrinks — the degree of degradation depends on σ_max. Oil coating slightly lowers σ_0 but substantially restores descending-branch load capacity and energy dissipation, presenting an improvement strategy for fatigue resistance.
6. Extensibility: setting γ_d and γ_s negative extends applicability to systems whose interfaces soften under fatigue (steel fibers, etc.).

## Methods

The basic skeleton inserts fatigue terms into Lin-Li's fracture-mechanics-based single-fiber pullout model (G_d, τ_0, slip-hardening coefficient β). Debonding length a = min(a_0 + Δa(N_d), L_e); after translating the crack parallel to itself, the u-a'-σ relation is derived from stress equilibrium plus an energy criterion (Appendix A). The macro scale synthesizes snubbing P(φ) = P(0)e^(fφ) (f = 0.2, assumed fatigue-invariant), p(z) = 2/L_f, orientation probability densities (2D/3D distributions), and V_f 2 %. Inputs: PVA d_f 39 µm, E_f 22 GPa, E_m 20 GPa, G_d 2.68 J/m² (no oil)/1.77 J/m² (oil), τ_0 1.89/1.37 MPa, β 0.19/0.21. The validation data came from the same group's large-embedment-length (strength degradation) and short-embedment-length (interface degradation) single-fiber fatigue pullout experiments.

## Results

Post-fatigue bridging behavior predicted by the model: (1) σ_0 decreases monotonically with cycle number (accumulation of premature rupture), (2) rising-branch stiffness and stress rather increase owing to hardening, (3) a higher load level σ_max accelerates degradation, (4) at N = 10³ and σ_max = 4 MPa, the oil-coated system sustains load over a wider δ range than the uncoated system, with superior dissipated energy. It quantitatively reproduces the observation from the authors' preceding experiments (RELIM 2014, RILEM HPFRCC 2015) that interface hardening induces premature fiber rupture.

## Related Notes

- [[fiber-bridging-constitutive-law]] — the target curve this model extends. Positioned in the concept-page lineage as the first case adding a fatigue axis (N, σ_max) to the static σ_B(δ).
- [[li-wu-1992-psh-conditions]] — origin paper of the snubbing factor and the generalized σ_b(δ) form. This paper's f and f' definitions descend from that lineage.
- [[lee-2011-diverse-embedment-model]] — the steel-fiber counterpart of fiber-stress modeling reflecting orientation/embedment-length randomness. Shares the probabilistic averaging approach.
- [[li-2001-pva-ecc-strain-hardening]] — representative experiment of the PVA hydrophilic-interface (chemical bond + slip-hardening) system. The static version of the issue of oil coating altering interface properties.
