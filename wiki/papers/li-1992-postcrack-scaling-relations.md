---
title: "Postcrack Scaling Relations for Fiber Reinforced Cementitious Composites (Li, 1992)"
type: source_note
source: "sources/Post-Crack Scaling Relations for Fiber-Reinfor.pdf"
citation: "Li, V.C. Postcrack scaling relations for fiber reinforced cementitious composites. Journal of Materials in Civil Engineering 4(1) (1992) 41-53. Paper No. 1174."
date: 2026-08-22
tags: [frcc, fiber-bridging, postcrack-strength, fracture-energy, snubbing, scaling-law, pullout, micromechanics, classic, scan-ocr]
---

# Postcrack Scaling Relations of FRC (Li 1992)

## Summary

This theory paper derives closed-form prepeak and postpeak stress-displacement (σ-δ) relations for the bridging mechanism of fiber reinforced cementitious composites (FRCC) reinforced with randomly oriented discontinuous flexible fibers, and establishes how postcrack strength and fracture energy scale with the micromechanics parameters (snubbing coefficient, fiber diameter/aspect ratio/volume fraction, interfacial bond strength). Experimental values for steel fiber (Visalvanich-Naaman data) and the polymer fiber Spectra PE (Wang et al. data) agree well with the scaling laws, making this one of the origin papers of the ECC bridging constitutive-law lineage. Scanned copy; full text secured via OCR.

## Key Contributions

1. Postcrack strength scaling law (Eq. 9): σ_pc = gτV_f(L_f/d_f)/2. A linear relationship with respect to the reinforcement index 2V_f(L_f/d_f), whose slope is the snubbing factor g. The special case g=1 matches Aveston et al. (1974). Steel fiber/mortar data are explained well with f≈1.0, and Spectra PE in normal- and high-strength mortar with f≈0.55.
2. Fracture energy scaling law (Eq. 11): G_c = gτV_f L_f²/12 — proportional to the square of fiber length. The debonding-zone energy (Eq. 12) is negligible at the δ* fraction level of postpeak pullout energy. Random orientation halves the fracture energy relative to aligned fibers (a factor of 2 when g=1; contrast with Cooper-Kelly).
3. Shape of the postpeak curve (Eq. 7): the (1-δ̃)² dependence σ(δ) ∝ g(1 - δ/(L_f/2))² is theoretically derived from integrating individual fiber slip contributions. Points out that Visalvanich-Naaman (1982)'s semi-empirical relation (Eq. 8) and Wecharatana-Shah (1983)'s empirical fitting arrived at the same (1-δ̃)² form, interpreting the empirical coefficient α explicitly as g/2.
4. Quantification of the snubbing effect: pullout-load amplification P(δ;φ) = P(δ)e^{fφ} for a fiber at inclination angle φ (Eq. 3, Morton-Groves proposal). The snubbing factor g goes from 1 to 2.32 as f goes from 0→1. Experimental values: nylon f≈0.7, polypropylene f≈0.9. gτ acts effectively as an 'effective bond strength' that multiplicatively amplifies both postcrack strength and fracture energy.
5. Optimal fiber length and trade-off (Eqs. 13-14): gt (=gτ) is a trade-off parameter between postcrack strength and optimal fracture energy — raising postcrack strength for PSH increases fiber rupture and reduces the optimal fracture energy. Furthermore, since postcrack strength scales inversely with fiber diameter d_f while optimal fracture energy scales proportionally with d_f, thin fibers favor PSH and thick fibers favor energy absorption.
6. Measurement caveat: in systems where first-cracking strength exceeds σ_pc (low-volume-fraction steel-fiber FRCC, etc.), the measured postcrack strength can be a lower bound of the true value (three-stage fracture scenario interpretation of Figs. 9-10).

## Methods

- Single-fiber pullout analysis: frictional bond τ held constant, elastic bonding neglected. Debonding (frictional slip activation) regime Eq. 1: P = πd_f τℓδ/δ_b (linear rise); after complete debonding, pullout regime Eq. 2: P = πd_f τ(1 - δ/ℓ) (linear drop). The linearization is justified in Appendix I together with the condition (ℓ/d_f)/(E_f/τ) << 1 (error below 1 %).
- Composite σ-δ curve (Eq. 4): integrates the contribution of only the fibers crossing the crack plane over the orientation distribution p(φ)=sinφ and the center-distance distribution p(z)=2/L_f (integration of the Li-Wang-Backer 1991 JMPS model). Prepeak/postpeak closed forms derived in Appendices II-III.
- Validation data: (i) Visalvanich-Naaman (1982) steel-fiber mortar, 5 series (V_f 0.5~1 %, L_f/d_f 42~83), ≥5 repeats per point; (ii) Wang et al. (1990) Spectra PE fiber (high-modulus PE), normal/high-strength mortar (V_f 0.6 %, L_f/d_f 168). Normalized τ values: steel/mortar 4 MPa, spectra/mortar 1 MPa.

## Results

- Postcrack strength vs reinforcement index plot (Fig. 4): steel fibers align on the f≈1.0 line, the Spectra series on the f≈0.55 line. Nylon direct-pullout limit data show a tendency toward larger f in high-strength mortar.
- Postpeak σ-δ curves (Figs. 5-6): the theoretical curve (Eq. 7) agrees well with the experimental mean curves for both steel and Spectra fibers.
- Normalized fracture energy — Fig. 7 (steel fiber, aspect-ratio axis) and Fig. 8 (log-log, slope 2 confirmed): verifies the G_c ∝ (L_f/d_f)² scaling.
- Stated limitations: fiber plastic bending, matrix spalling, and slip-dependent interfacial shear resistance not incorporated — nevertheless it captures the main physics and suffices for engineering design of FRCC tensile properties.

## Related Notes

- [[fiber-bridging-constitutive-law]] — the constitutive-law page into which this paper's closed-form σ(δ) is integrated
- [[pseudo-strain-hardening-criteria]] — σ_pc as the key input of the PSH strength criterion (σ_0 ≥ σ_c)
- [[li-wu-1992-psh-conditions]] — same-year PSH conditions theory (App Mech Rev); this paper is its material-parameter scaling companion
- [[morton-1976-effect-metal-wires-fracture-brittle-matrix-composites]] — experimental origin of the snubbing concept (source of this paper's Eq. 3)
- [[lin-1999-interface-property-characterization]] — follow-up theory extending to σ(δ) including the three interface parameters (G_d·τ_0·β)
- [[kanda-2006-saturated-psh-design-criteria-ecc]] — follow-up that develops this scaling law into a PSH performance-index design frame
- [[li-2023-ecc-micromechanics-critical-review]] — early node of the bridging-model lineage tracked by the review

## Remarks

- Scan-based OCR full text used. Some formula constants/subscripts may be misread (right-hand-side arrangement of Eqs. 7-8, etc.) — consult the original PDF for precise citation.
