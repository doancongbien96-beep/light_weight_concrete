---
title: "Fiber-Bridging Constitutive Law of Engineered Cementitious Composites (Yang, Wang, Yang & Li, 2008)"
type: source_note
source: "sources/Yang-2008-Fiber-bridging constitutive law of e.pdf"
citation: "Yang, E.-H., Wang, S., Yang, Y., Li, V.C. Fiber-Bridging Constitutive Law of Engineered Cementitious Composites. Journal of Advanced Concrete Technology 6(1), 181-193, 2008."
date: 2026-08-23
tags: [ecc, fiber-bridging, constitutive-law, micromechanics, sigma-delta-curve, crack-width-control]
---

# Analytical model and experimental verification of the ECC fiber bridging constitutive law σ(δ)

## Summary

A paper that analytically predicts the fiber bridging constitutive law σ(δ) of ECC starting from material constituent parameters and verifies it through notched coupon tension tests. Building on the simplified model of Lin et al. (1999), three new fiber/matrix interaction mechanisms — two-way debonding/pullout, matrix micro-spalling, and the Cook-Gordon effect — were added, raising prediction accuracy of crack opening displacement in particular. The 2008 entry in the lineage table of the [[fiber-bridging-constitutive-law]] concept page is precisely this paper.

## Key Contributions

1. **Two-way pullout modeling**: on slip-hardening interfaces (PVA), the pullout load keeps rising even after complete debonding of the short embedded side, so the long embedded side joins subsequent debonding and pullout. Allocating the slip contributions of both fiber sides δL+δS=δ by load equilibrium (Eqs. 8~16), this is the principal mechanism resolving underprediction of crack opening.
2. **Semi-empirical expression for matrix micro-spalling**: the spall size s produced by local failure at the fiber exit point was proposed to be proportional to external load and inversely proportional to matrix tensile strength and fiber diameter (Eq. 17, spalling coefficient k=500 calibrated). Predicted spalling of 0~28 μm matches the observed maximum of 30 μm. Spalling reduces the effective orientation angle, delaying fiber rupture and raising peak bridging stress.
3. **Incorporation of the Cook-Gordon effect into σ(δ)**: premature interface debonding caused by normal stress ahead of the crack tip lengthens the free fiber segment α, creating additional opening δcg=4αP/(π d_f²E_f). For hydrophilic PVA with α=2d_f (78 μm) the effect is small, but for hydrophobic PE and PP families it is expected to be large.
4. **Experimental verification protocol**: single-crack conditions were created by lowering fiber volume fractions to 0.5 and 0.1 vol.%, and coupons with deep side notches (6 mm) plus shallow surface notches (2 mm) were pulled in deformation control to measure σ(δ) curves directly — the model reproduces average behavior well.
5. **Weakest-plane governing logic**: the gap between the predicted 2 vol.% peak of 6.7 MPa at 130 μm and the composite tensile measurement (about 5 MPa at a mean 60 μm) is explained by ±25 % scatter in effective fiber content across crack planes. At a stress level of 5 MPa the opening range spans 37~133 μm with a mean of 62 μm, matching the observed 60 μm — providing a micromechanics interpretation of the crack width self-control mechanism.

## Methods

- Materials: PVA-ECC M45 (field-standard mix) — cement 571, fly ash 685, silica sand (mean 110 μm) 456, water 332 kg/m³, polycarboxylate high-range water reducer 6.8 kg/m³, PVA fibers (12 mm, 39 μm, tensile strength 1600 MPa, density 1300 kg/m³, oil coating 1.2 wt %) 26 kg/m³ (2 vol %). Modified mixes of 0.5 and 0.1 vol.% were used for σ(δ) measurement.
- Testing: coupons 90 × 76 × 13 mm with diamond-saw notches; servo-hydraulic deformation control at 0.0001 mm/s (quasi-static); two 5 mm gauge extensometers extracting crack opening displacement by removing deformation up to just before cracking. Air curing for 28 d (50±5 % RH, 23±2 °C).
- Microparameter determination: interface τ0·Gd·β from single-fiber pullout tests (Redon et al. 2001); apparent fiber strength σfu=1060 MPa and strength reduction factor f'=0.33 from single-fiber in-situ strength tests (Kanda & Li 1998); snubbing coefficient f=0.2 as the lower bound of Wu's 2001 range (0.2~0.8, reflecting the 1.2 % oil coating); Em=20 GPa from initial tensile slope; σm=5 MPa back-calculated from wedge splitting tests; Cook-Gordon parameter α=78 μm adopting Bentur's proposed lower bound of 2d_f.
- Integration: probability density function averaging over fiber position z and orientation φ (Eqs. 21~25). Because coupon thickness (13 mm) is comparable to fiber length, a 2D random orientation p(φ)=2/π was assumed (3D would be p(φ)=sin φ).

## Results

- Model input parameters: d_f=39 μm, L_f=12 mm, E_f=22 GPa, σfu=1060 MPa, f=0.2, f'=0.33, α=78 μm, Em=20 GPa, σm=5 MPa, k=500.
- Fiber-volume dependence of interface properties (bond degrades as air content loosens the microstructure):

| Matrix | τ0 (MPa) | Gd (J/m²) | β |
|---|---|---|---|
| 0.1 vol.% PVA | 1.91 | 1.24 | 0.63 |
| 0.5 vol.% PVA | 1.58 | 1.13 | 0.60 |
| 2 vol.% PVA | 1.31 | 1.08 | 0.58 |

- Mechanism decomposition (Vf=2 vol.% prediction): 1-way (Lin et al. 1999) 6.2 MPa @93 μm → +two-way 6.3 MPa @130 μm → +micro-spalling 6.7 MPa @131 μm → +Cook-Gordon 6.7 MPa @133 μm. Two-way pullout carries the opening-displacement accuracy, micro-spalling the peak stress, while Cook-Gordon is negligible for PVA.
- Verification: within the experimental σ(δ) scatter at Vf=0.1 and 0.5 vol.% (peak stress scatters widely between specimens while the corresponding opening stays nearly constant — more fibers raise stress, but higher mean spring stiffness binds the opening), the model curve agrees well with average behavior.

## Related Notes

- [[fiber-bridging-constitutive-law]] — concept page of the σ(δ) constitutive law this paper established (lineage 2008 entry)
- [[pseudo-strain-hardening-criteria]] — relation entering as a multiplier into the J'tip ≤ J'b energy criterion and σc<σ0 strength criterion
- [[lin-1999-interface-property-characterization]] — origin of the 1-way simplified model and interface parameters (Gd·τ0·β) that this work improved upon
- [[wu-1992-snubbing-bundling-crack-spacing]] — origin lineage of the snubbing coefficient f and crack spacing theory axis
- [[kanda-2006-saturated-psh-design-criteria-ecc]] — practical extension of PSH performance indices such as J'b/Jtip
- [[lu-2017-fiber-orientation-thickness]] — extends this paper's 2D/3D orientation distribution assumption to the member thickness perspective
- [[qiu-2016-fatigue-dependent-fiber-bridging-model]] — successor bridging model adding fatigue degradation to static σ(δ)
