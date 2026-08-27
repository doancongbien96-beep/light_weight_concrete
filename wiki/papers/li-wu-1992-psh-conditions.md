---
title: "Conditions for Pseudo Strain-Hardening in Fiber Reinforced Brittle Matrix Composites (Li & Wu, 1992)"
type: source_note
source: "sources/1st PE_li_condition_for_PSH.pdf"
citation: "Li, V.C., Wu, H.-C. Conditions for pseudo strain-hardening in fiber reinforced brittle matrix composites. Applied Mechanics Reviews 45(8) (1992) 390-398."
date: 2026-08-22
tags: [psh, micromechanics, critical-fiber-volume, steady-state-cracking, fracture-mechanics, design-theory, scan-ocr]
---

# Conditions for Pseudo Strain-Hardening in Brittle Matrix Composites

## Summary

Theoretical paper deriving the conditions for the onset of pseudo strain-hardening (PSH) in continuous aligned (CA) and discontinuous random (DR) fiber composites within a unified fracture-mechanics framework. It recasts the conventional rule-of-mixtures-based Aveston critical fiber volume fraction concept in terms of matrix fracture energy, interfacial friction, and fiber factors, and validates the theory on a Spectra PE fiber/cement paste system. This is the origin document of ECC design theory.

## Key Contributions

1. Critical bridging toughness ratio: expresses the necessary condition for PSH as a bridging-toughness-to-crack-tip-toughness ratio of the form G_d/G_tip ≥ ~10 (CA) / ~3 (DR) (Eq. 14). This is the rigorous prototype of the energy criterion J′_b/J_tip ≥ 1 in [[pseudo-strain-hardening-criteria]], and a direct precursor of the Kanda-Li performance index concept.
2. Reformulation of the critical fiber volume fraction: Eq. 15 replaces the rule-of-mixtures expression (Aveston), making V_f,crit a function of matrix fracture toughness K_m, interfacial friction τ, and aspect ratio L_f/d_f. Low K_m, high aspect ratio, and high τ permit a low V_f,crit. DR systems require far higher V_f,crit than CA (Spectra example: CA 0.001 % vs DR 0.3 %; steel fiber example: CA 0.4 % vs DR 9 %).
3. Discovery of an auxiliary condition (Eq. 16): G_d does not increase monotonically with V_f (reduced crack opening lowers frictional work), so an additional condition must hold for a real solution to exist. For CA this is interpreted as a lower bound on fiber strength and an upper bound on interfacial bonding; for DR, as lower bounds on aspect ratio and bonding.
4. Transient crack size c_s and the sufficient condition: multiple cracking is guaranteed once the initial crack exceeds c_s. When K_m exceeds K_m^crit (0.188 for DR, 0.376 for CA), PSH is suppressed — predicting that PSH can be suppressed even at high V_f.
5. Design case validation: for Spectra PE fibers (d_f 38 μm, L_f 12.7 mm, E 120 GPa) in OPC paste (K_m 0.2 MPa√m), the theory predicts V_f,crit = 0.3 %, confirmed experimentally. The ultimate strain capacity of composites with V_f > V_f,crit was about 220 times that of subcritical composites.

## Methods

Fracture-mechanics analysis: stress intensity factor superposition (K_I + K_r = K_tip), an elliptical crack geometry assumption, and a generalized bridging stress–crack opening relation σ_b(δ) (Table 1 lists the constants for CA/DR, including the snubbing factor g). The quasi-steady-state cracking strength is evaluated as the first-cracking strength at the transient size (Eq. 19).

## Results

- First-cracking strength σ_fc depends on crack size while quasi-steady-state cracking strength σ_ss does not — their intersection defines c_s.
- The elliptical assumption overestimates σ_ss by about 20 % (relative to numerical analysis).
- Experiment: V_f 0.1 % failed brittly vs 1 % showing marked ductility plus multiple off-parallel cracks.

## Related Notes

- [[li-2023-ecc-micromechanics-critical-review]] — one of the starting points of the development lineage traced by that review (the 1992 PSH introduction entry in its Table 1).
- [[fiber-bridging-constitutive-law]] — origin of the generalized σ_b(δ) form and of the snubbing factor g.
- [[sahmaran-2009-aggregate-type-size-ecc]] — the design-theory foundation cited by subsequent experimental studies such as this one.
- [[cho-2012-basic-mixing-and-mechanical-tests]] — an application case interpreting the strain-performance difference between two binder-free HD-FRCC mixes through the strength/energy criteria (KCI 2012).

## Remarks

- Full text secured via OCR from a scanned copy. Some equations may be distorted (e.g., constant values) — cross-check against the original PDF when citing precisely.
- [[li-2003-ecc-review-jact]] — Li's invited review (2003) summarizing ten years of development of this theory.
- [[morton-1976-effect-metal-wires-fracture-brittle-matrix-composites]] — experimental origin of the snubbing (inclined pull-out friction) effect (1976).
