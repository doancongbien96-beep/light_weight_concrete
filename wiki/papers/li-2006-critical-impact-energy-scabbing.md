---
title: "Critical impact energies for scabbing and perforation of concrete target (Li et al., 2006, Nuclear Engineering and Design)"
type: source_note
source: "sources/Li-2006-Critical impact energies for scabbing.pdf"
citation: "Li, Q.M., Reid, S.R., Ahmad-Zaidi, A.M. Critical impact energies for scabbing and perforation of concrete target. Nuclear Engineering and Design 236 (2006) 1140-1148. doi:10.1016/j.nucengdes.2005.10.017"
date: 2026-08-22
tags: [concrete-impact, scabbing, perforation, critical-impact-energy, ndrc-formula, empirical-formula, dimensional-analysis, ballistic-limit, protective-structures]
---

# Critical impact energies for scabbing and perforation of concrete targets

## Summary

A nuclear-facility protective structure paper (outside the user group) by the University of Manchester impact mechanics team of Q.M. Li and S.R. Reid. Using dimensionless-number analysis it organizes the influence of the relative target thickness H/d on the critical impact energies at which local damage of concrete targets (scabbing, perforation) initiates, and rationalizes the UMIST empirical formula (Reid-Wen 2001) embodied in the UK nuclear industry's R3 Impact Assessment Procedure via (1) dimensional analysis, (2) a formula derived from the NDRC family, (3) a semi-empirical route (NDRC + the Li-Chen 2003 penetration formula), and (4) an analytical route (the Li-Tong 2003 penetration-plugging model), cross-validating against the World Impact Data (Bainbridge 1988, a database of hundreds of experimental results). The conclusion is that the UMIST formula always yields the lower bound (safe side) and is therefore recommended for preliminary nuclear design without safety factors. sources/ holds two copies of the same paper (`Li-2006-Critical impact energies for scabbing.pdf`, `li-2006-critical-impact-energies-for-scabbing.pdf`), merged into a single note.

## Key Contributions

1. **Establishment of the dimensionless frame**: the scabbing limit hs and the perforation limit e were formalized as dimensionless relations of the form Ec/(d³fc) = G(M/(ρd³), H/d, ft/fc[, τf/fc]). Aggregate characteristic size and light-to-medium reinforcement (r = 0.3~1.5 % ewef) were excluded from the variables on the evidence that they have almost no effect on perforation or scabbing — showing that H/d is the governing parameter.
2. **Comparison of three families of empirical formulas on identical coordinates**: the UMIST formula (R3), the NDRC-derived formula, and the semi-empirical formula were all converted onto the critical impact energy Ec/(d³fc)-H/d plane to organize their relative rankings systematically by H/d interval (E = experiment, N = NDRC, S = semi-empirical, U = UMIST).
3. **Analytical expression for the perforation threshold energy**: a closed-form Ecp/(d³fc)-H/d relation (Eq. 28) was derived from Li-Tong 2003's two-stage model combining a penetration stage and a cone-plugging stage (k = 2, cone angle α = 60°) — fitting the experimental data better than the semi-empirical formula. Insensitivity to the cone angle confirmed (noted alongside Dancygier 1998's 70° and the mean crack angle of 59.2° from Li-Reid 2004 stress analysis).
4. **Safety-factor guidance**: the UMIST formula consistently gives the lowest prediction for both scabbing and perforation → no safety factor needed; recommended as optimal for preliminary impact design of nuclear facility concrete. The NDRC and semi-empirical formulas lie closer to experiment overall but may overestimate, so safety factors are required alongside them. In addition, a technique for extending ballistic-limit data from existing penetration test data via energy conservation (Eq. 29~30) is presented.

## Methods

- After deriving the governing dimensionless numbers of scabbing and perforation by dimensional analysis, the three classes of formulas were re-derived onto a common coordinate frame and compared with the 'just scabbing' and 'just/almost perforated' experimental values of the Bainbridge (1988) World Impact Data.
- UMIST formula validity range: projectile diameter d 22~600 mm, mass M 1~2622 kg, velocity V₀ ≤ 427 m/s, fc 19.9~78.5 MPa, reinforcement ratio r ≤ 4 % ewef, thickness H 50.8~640 mm (flat-nosed projectiles, N* = 0.72).
- Dynamic fragmentation stress σt(Pa) = 4.2fc + 135.0 MPa + [0.014fc + 0.45 MPa]·Vc(m/s); material dimensionless number S = 72.0·fc^-0.5 (fc in MPa); impact function I = MV₀²/(Sd³fc), N = M/(ρd³).

## Results

- Scabbing mechanism: caused by the impact compressive stress wave reflecting off the rear free surface and inducing tensile failure; occurs on a far shorter timescale than complete perforation or the global structural response.
- Scabbing comparison: around H/d ≈ 0.5 the UMIST formula lies closest to experiment; for 0.5 < H/d ≤ 3.0 the ranking is E > N > S > U; for H/d > 3.0 it is N > S > E > U — the UMIST formula gives the lowest value in every interval.
- Perforation comparison: roughly N > E > S > U throughout. There exist cases where the UMIST formula turns negative outside its valid lower bound (H/d ≥ 0.34).
- The analytical (plugging-model) formula fits experiment better than the semi-empirical one, and performs equally well on the extended ballistic-limit data. Caution is warranted near H/d = 4, where experimental scatter is large (small-mass/high-velocity vs large-mass/low-velocity cases mixed).
- Practical conclusion: the UMIST (R3) formula is a safe-side lower bound requiring no safety factor and is recommended for preliminary nuclear design; the NDRC and semi-empirical formulas require safety factors.

## Related Notes

- [[kim-2018-uhpfrc-hdfrc-projectile]] — the group's UHPFRC/HDFRC panel projectile-impact paper verifying penetration depth and scabbing limit thickness with the modified NDRC formula (FRC application of the NDRC-family formulas organized in this paper)
- [[kim-2015-shcc-impact-magazine]] — literature review of SHCC impact resistance (introductory note to the impact axis of fiber-reinforced materials)
- [[pan-2023-dynamic-compressive-shpb-egc]] — dynamic behavior axis connected through SHPB dynamic compression
