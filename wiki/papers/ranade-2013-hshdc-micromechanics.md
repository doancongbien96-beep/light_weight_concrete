---
title: "Micromechanics of High-Strength, High-Ductility Concrete (Ranade, Li, Stults, Rushing, Roth & Heard, 2013)"
type: source_note
source: "sources/Micromechanics of High-Strength, High-Ductilit.pdf"
citation: "Ranade, R., Li, V.C., Stults, M.D., Rushing, T.S., Roth, J., Heard, W.F. Micromechanics of high-strength, high-ductility concrete. ACI Materials Journal 110(4) (2013) 375-384."
date: 2026-08-22
tags: [hshdc, pe-fiber, inclined-pullout, inclination-hardening, snubbing, micromechanics, psh-index, high-strength-matrix]
---

# Micromechanics of HSHDC

## Summary

This paper establishes the micromechanical design basis of high-strength high-ductility concrete (HSHDC), which simultaneously possesses a compressive strength of 166 MPa and a tensile strain capacity of 3.4 % (Michigan ACE-MRL + US Army Engineer Research and Development Center ERDC). From 50 single-fiber pullout tests on UHMWPE fiber, it discovered a new 'inclination-angle-dependent hardening' mechanism that existing SHCC models cannot explain, and carried through a modified pullout model → scale-link model → σ-δ curve computation → multiple-cracking condition verification that incorporates it. The core discovery is the phenomenon whereby the high-strength matrix bites into the fiber (pencil-tip abrasion) and thereby raises the pullout load instead of lowering it.

## Key Contributions

- Quantification of PE-HSHDC interface properties: frictional bond τ0 = 1.52 MPa (2~3× that of medium-strength matrices), chemical bond Gd ≈ 0 J/m² (hydrophobic PE), slip-hardening β = 0.003 (two orders of magnitude below PVA-SHCC — the pullout tunnel stays smooth thanks to ultra-fine particle packing), snubbing coefficient f = 0.59.
- Discovery and formalization of the new 'inclination-dependent hardening' mechanism: as the inclination angle increases, the matrix wedge tip becomes sharper and grips the fiber laterally, and as slip proceeds the fiber cross-section abrades like a pencil tip, jamming at the exit → linear rise of the pullout load. Quantified by the parameter m = 386 N/(m-rad) and demonstrated with SEM micrographs. The exact opposite of microspalling in SHCC (the matrix breaks away and softens).
- Scale-link verification: computing the σ-δ curve with the fluorescence-microscope orientation distribution (mixed 2D+3D, w = 0.73) as input agrees with single-crack tests on notched specimens (mean bridging capacity 13.8 MPa). The modified model (13.0 MPa) outperforms the existing SHCC model (12.0 MPa).
- Demonstration that the multiple-cracking conditions are satisfied: strength criterion min(σ0)/σ_ci(fc) = 11.0/8.4 = 1.3 > 1.2; energy criterion J′b/Jtip = 682/25 = 27 >> 3. Proves micromechanically that ductility can be retained even in a high-strength matrix (Km = 1.1 MPa√m).

## Methods

- Mix: H-cement 907 kg/m³, silica fume 353, ground quartz powder 251, silica sand 635, W/C 0.15, HRWRA, PE fiber (UHMWPE, ∅28 µm, length 12.7 mm, strength 3000 MPa, nominal modulus 100 GPa / effective 30 GPa) at 2 vol %. Curing: 7 days in water + 5 days in water at 90 °C + 3 days in air at 90 °C.
- Single-fiber pullout: 50 specimens (aligned 30 + inclined 14°~45° 20), 5 N load cell, free-length elastic elongation correction. Single-crack test: six 305×76×12.7 mm notched specimens, two LVDTs.
- Km from an ASTM E399 notched beam; orientation distribution by fluorescence microscopy (method of Lee et al. 2009).

## Results

- τ0 derivation: from the slope 0.134 of the linear regression of P_peak against L_e, τ0 = 1.52 MPa; the y-intercept is nearly zero, so Gd ≈ 0. Mean β = 0.003.
- Snubbing: fitting ln[P_peak(φ)/P_peak(0)] = fφ yields f = 0.59.
- Inclination-hardening parameter m = 386 N/(m-rad): derived from the pattern in which the observed-model difference scales linearly with (u-u₀).
- Even under assumed theoretical 2D/3D distributions, min(σ0) = 9.4~10.2 MPa and J′b = 468~581 J/m², satisfying both conditions.

## Related Notes

- [[ranade-2012-hshdc-poster]] — materials-overview poster companion to this paper
- [[lee-2015-pe-cementless-composite-tensile]] — user-group follow-up that cites Ranade et al.'s HSHDC (comparison target in this paper)
- [[morton-1976-effect-metal-wires-fracture-brittle-matrix-composites]] — experimental origin of the snubbing concept
- [[lin-1999-interface-property-characterization]] — origin of the three-parameter pullout model (extended by this paper)
- [[kanda-2006-saturated-psh-design-criteria-ecc]] — PSH performance index framework
- [[fiber-bridging-constitutive-law]] — the scale-link σ(δ) model
- [[pseudo-strain-hardening-criteria]] — strength and energy conditions
- [[wu-2023-pe-fiber-dosage-length-egc]] — the PE fiber design axis
