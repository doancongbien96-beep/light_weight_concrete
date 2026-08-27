---
title: "Theory of Multiple Fracture of Fibrous Composites (Aveston & Kelly, 1973)"
type: source_note
source: "sources/'aveston-1973-theory-of-multiple-fracture-of.pdf'"
citation: "Aveston, J., Kelly, A. Theory of multiple fracture of fibrous composites. Journal of Materials Science 8 (1973) 352-362. National Physical Laboratory, Teddington, UK. Received 4 July 1972, accepted 5 September 1972."
date: 2026-08-23
tags: [ack-theory, multiple-cracking, crack-spacing, shear-lag, debonding, energetics, random-fiber-orientation, brittle-matrix, classic]
---

# Theory of Multiple Fracture in Fibrous Composites

## Summary

A theoretical follow-up (National Physical Laboratory) that removes the two limitations of the original Aveston-Cooper-Kelly (ACK) 1971 conference paper. First, in place of the existing theory's fully debonded (friction-only) interface assumption, it formalizes the bonded case, in which elastic interfacial continuity persists even after matrix cracking, using shear-lag analysis. Second, it goes beyond the parallel-aligned-fiber assumption to derive the crack spacing for thin flexible fibers randomly oriented in two and three dimensions. The crack-spacing formula derived here (x′ = σmu·Vm·r/(2τ′)) and the energy-based logic for the increase in reference-crack strain are the direct ancestors of SHCC/ECC multiple-cracking theory.

## Key Contributions

- Closed-form solution for the bonded case: interfacial shear stress decays as τ = (√φ/2)Δσ₀·exp(-√φ·y), with φ built from matrix shear stiffness Gm and a geometric term ln(R/r). The crack spacing l = σmu·Vm·r/(2τmax) takes the same form as x′ of the debonded case with τ′ replaced by τmax.
- Stress-strain curve prediction: in the bonded case a gently rising hardening curve emerges naturally without additional assumptions such as scatter in matrix strength (which the debonded case required). After first cracking, unloading returns to the origin if bond is maintained, while a frictional interface leaves permanent residual deformation.
- Debonding criterion (Eq. 15): elastic interfacial continuity is maintained only when Ef/Ec exceeds the term 4n²·Vf²·r² (n = τu/σmu). For cement with n = 1 the critical Vf would be carbon 0.36, steel 0.38, glass 0.50, outside practical ranges, so some debonding is inevitable in real FRC; n = 2 and n = 4 lower these values to 0.09 and 0.02 respectively.
- Partial debonding analysis: the minimum crack spacing L = l′ + l equals x′ or reaches at least 85 % of it under most practical conditions, demonstrating that the simple debonded theory suffices; correction is needed only when interfacial shear strength τu far exceeds σmu.
- Energetics (Section 8): the reference-crack formation condition takes the form Ec·εmu² ≥ (shear-lag term) + 4γm·Vm/r, so the effective matrix fracture strain εmud increases as r decreases. For an elastic interface to give a larger strain increment than a debonded one, τ′ < σmu/3 and τu ≥ σmu must hold (Eqs. 26-27).
- Random orientation correction: the number of fibers bridging a unit crack area is 2/π of the parallel case for two-dimensional randomness and 1/2 for three-dimensional randomness. Crack spacing increases relative to the parallel-case x′ to (π/2)x′ in two dimensions and 2x′ in three dimensions — thanks to the pulley action of flexible fibers, the orientation penalty is smaller than one might expect.

## Methods

- Modified shear-lag analysis: fiber-matrix relative displacement modeled with hexagonal packing geometry (R = r[π/(2√3 Vf)]^(1/2)); closed-form derivation in Appendix 1.
- Unified derivation of crack spacing for the three interfacial states (debonded, bonded, partially debonded) from the fundamental load-transfer relation dF/dy = -(2Vf/r)τ.
- Energetic verification: reference-crack strain derived from the equality condition applied work = increase in composite elastic strain energy + matrix fracture surface work (Appendix 1).
- Random orientation handled via directional-probability integration in Appendix 2 (N sinθ distribution in 2D, N cosθ distribution in 3D) together with the pulley reaction assumption of flexible fibers.
- Example calculations: Portland cement + 1 vol % steel fiber (Ef = 2×10⁵ MPa), comparison of critical Vf for glass, steel, and carbon fibers.

## Results

- Crack-spacing dependence: in the debonded case the crack spacing lies between x′ and 2x′ (close to the mean value x′); in the bonded case between l and 2l. During crack progression the additional strain is constant regardless of the number of cracks in both cases.
- At practical cement-composite Vf (<5 %), debonding is unavoidable, so frictional-interface theory suffices for practical crack-spacing prediction; even under partial debonding the minimum crack spacing remains at least 85 % of x′.
- Orientation effects are far smaller than the values suggested by extensions of Cox's elastic solution or by Allen and Laws's efficiency factors; for strength and toughness purposes, two-dimensional random placement is nearly equivalent to complete parallel alignment.
- The theory's self-stated limitations: neglect of normal and tangential stresses at the fiber surface and omission of Poisson effects are stated explicitly; comparison with numerical solutions (broken-fiber problem) confirms that shear-lag analysis fits well at distances beyond about 0.4 fiber radii.

## Related Notes

- [[li-wu-1992-psh-conditions]] — original source reconstructing ACK theory as ECC PSH design criteria
- [[wu-1992-snubbing-bundling-crack-spacing]] — direct successor extending it with the snubbing index and bundle effective bond
- [[morton-1976-effect-metal-wires-fracture-brittle-matrix-composites]] — experimental origin of the snubbing phenomenon
- [[lin-1999-interface-property-characterization]] — unified closed-form σ(δ) law for snubbing and interfacial parameters
- [[kanda-1998-pva-interface-apparent-strength]] — quantitative application of this theory's load-transfer concept to PVA fibers
- [[kanda-2006-saturated-psh-design-criteria-ecc]] — practical design criteria developed into PSH performance indices
- [[pseudo-strain-hardening-criteria]] — concept page on the conditions for multiple cracking
- [[fiber-bridging-constitutive-law]] — concept page on the fiber bridging constitutive law
- [[li-2023-ecc-micromechanics-critical-review]] — review hub overseeing this theory axis
