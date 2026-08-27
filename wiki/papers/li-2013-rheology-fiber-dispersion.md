---
title: "Rheology, Fiber Dispersion, and Robust Properties of Engineered Cementitious Composites (Li & Li, 2013)"
type: source_note
source: "sources/Rheology, fiber dispersion.pdf"
citation: "Li, M., Li, V.C. Rheology, fiber dispersion, and robust properties of engineered cementitious composites. Materials and Structures 46(3) (2013) 405-420. doi: 10.1617/s11527-012-9909-z"
date: 2026-08-22
tags: [ecc, rheology, plastic-viscosity, marsh-cone, fiber-dispersion, fluorescence-imaging, vma, robustness, quality-control]
---

# Rheology, Fiber Dispersion, and Robustness of ECC (Li & Li 2013)

## Summary

The first paper to systematically establish the correlation between the plastic viscosity of fresh ECC mortar (before fiber addition) → the uniformity of PVA fiber dispersion → the tensile properties of the hardened composite (first author Mo Li, University of Houston; corresponding author V. C. Li). Starting from a measured case in which the tensile strain capacity swung from 0.6 to 3.4 % among ECC batches produced with identical mix proportions and the same mixer, it identifies the source of the variability as fiber-dispersion deviation created by fresh-state viscosity and proposes the Marsh cone flow time as a field quality-control index. It proposes an optimal flow-time window of 24~33 s and validated this with a white-ECC case study. Contrary to what the file name suggests, the publication year is RILEM Materials and Structures Vol. 46 (2013).

## Key Contributions

1. First quantitative establishment of the viscosity-fiber dispersion-composite performance correlation: low plastic viscosity causes insufficient mixing shear and hence fiber clumping; raising viscosity improves dispersion, but beyond a certain level large air-void entrapment reduces the effective net cross-section and the fiber amount in weak sections, so first-cracking strength and ultimate tensile strength rather decline — an inverted-U-shaped optimum exists.
2. Strong linear correlation between Marsh cone flow time ↔ plastic viscosity (R = 0.95): justifies field and laboratory viscosity management with a portable Marsh cone instead of a rotational viscometer.
3. Optimal fresh-state window: Marsh cone flow time of 24~33 s (VMA/cement of 0.02~0.03 % for this mix). Below 24 s both the fiber dispersion coefficient and the strain capacity drop sharply; above 33 s (at 39 s) the dispersion coefficient stays high but strength decreases due to air-void entrapment.
4. Strong positive correlation between the fiber dispersion coefficient α (Eqs. 5-6) and tensile strain capacity (Fig. 12a): a drop in α simultaneously causes reduced strain capacity and ultimate strength plus increased variability, and when α falls low enough a strain-hardening material transitions into a tension-softening material. The mechanism is: reduced bridging stress σ_0 in the weak section → increased critical flaw size c_mc → fewer activatable flaws.
5. Mix-invariance principle: the optimal VMA dosage differs from mix to mix, but the "optimal viscosity (flow time)" itself is a universal parameter as long as fiber type, content, and dimensions are unchanged — besides VMA addition, particle-size distribution adjustment, w/c adjustment, superplasticizer, etc. are all means of entering the target viscosity window.
6. WHITE-ECC case validation: no VMA at 12 s (α≈0.53, ε swinging 1.1~2.7 %) → VMA 0.05 % raising it to 28 s (α≈0.8, mean ε 2→3 % with reduced variability) → 0.1 % raising it to 38 s (ε improvement retained but slight drops in first-cracking and ultimate strength). Confirmed that mixes starting from lower viscosity require larger VMA doses.

## Methods

- Materials: OPC Type I (Blaine 3300 cm²/g), Class F fly ash (10~20 μm), F-110 silica sand (mean 110 μm), REC15 PVA fiber at 2 % by volume (nominal strength 1620 MPa, apparent strength 1092 MPa, diameter 39 μm, length 12 mm, oil coating 1.2 wt%), polycarboxylate high-range water reducer. VMA (V-MAR V) dosages of 0/0.01/0.015/0.02/0.025/0.03/0.04 % — seven mixes (identical mix proportions otherwise).
- Mixing: 12 L Hobart mixer; solid ingredients 100 rpm 1 min → water + air-entrainer 150 rpm 3 min (mortar complete) → viscosity measurement → fiber added to a separate batch 150 rpm 3 min → self-consolidating casting (no vibration).
- Fresh state: Viskomat-NT rotational viscometer (Bingham T = g + Nh, with relative viscosity h converted to Pa·s via calibration liquid), Marsh cone (time from opening of the bottom orifice until light transmission), mini-slump (top 70 mm/bottom 100 mm/height 60 mm, averaged over two diagonal directions).
- Hardened tension: plate specimens of 228.6 × 76.2 × 12.7 mm, cured 24 h before demolding → 7 d moist + 21 d air, tested at 28 d age. 25 kN MTS under displacement control 0.0025 mm/s, LVDT gauge length 101.6 mm, five specimens per mix.
- Fiber dispersion quantification: 5 mm-thick slices cut from the final fracture (weakest section), photographed unpolished with a fluorescence microscope (TE300 Nikon, mercury lamp + UV filter + CCD Hamamatsu ORCA-ER); 105 frames (21×5) stitched into a full cross-section image (2300×4186 px), fibers counted on a 59×21 grid unit basis, and α = exp[-w(x)] computed from the coefficient-of-variation function w(x) (=1 when uniform).

## Results

| Mix | Marsh cone (s) | α range | ε_pc (%) |
|---|---|---|---|
| VMA 0 | 9 | 0.29~0.50 | 0.03~0.44 |
| VMA 0.01 % | 12 | 0.49~0.57 | 0.32~1.19 |
| VMA 0.015 % | 17 | 0.55~0.66 | 0.75~1.97 |
| VMA 0.02 % | 24 | 0.73~0.84 | 2.87~3.50 |
| VMA 0.025 % | 30 | 0.72~0.89 | 2.68~3.35 |
| VMA 0.03 % | 33 | 0.67~0.84 | 2.71~3.25 |
| VMA 0.04 % | 39 | 0.77~0.88 | 2.83~3.33 |

- Of the VMA 0 mix, only one of five specimens showed modest hardening (ε 0.44 %); the rest were tension-softening.
- Tensile strength increases over the VMA/C 0~0.02 % range with reduced variability, and decreases over the 0.025~0.04 % range (cause: large air-void entrapment, confirmed by microscope observation) — ε_pc plateaus after 0.02 %.
- Mini-slump diameter decreases upon fiber addition but responds hardly at all to VMA dosage — suggesting that viscosity alone can be selectively controlled without sacrificing deformability.
- Application limits stated explicitly: the optimal window of 24~33 s is limited to the REC15 PVA 2 vol% + force-based mixer condition, and a higher optimal viscosity is expected for gravity-type truck mixers, etc. (future work).

## Related Notes

- [[yang-2009-rheological-control-in-production-of]] — the preceding ACI MJ study cited as ref. 32 of this paper; this paper developed its DOE-based fresh-state control into the viscosity-dispersion-performance correlation framework.
- [[kim-2007-fiber-dispersion-fluorescence]] — user-group implementation of the fluorescence-image-based quantitative fiber dispersion evaluation method (the same problem as this paper's α quantification).
- [[lee-2009-extruded-ecc-panel-fiber-distribution]] — user-group study on how the forming process governs fiber distribution.
- [[choi-2015-rheological-mechanical-fr-aac]] — follow-up extending the viscosity-ductility correlation to AAS systems.
- [[pseudo-strain-hardening-criteria]] — the physical link governing whether fiber-dispersion deviation satisfies σ_0 ≥ σ_c.
- [[li-2003-ecc-review-jact]] — overview of the framework linking micromechanics design and processing control.
- [[li-2023-ecc-micromechanics-critical-review]] — review context addressing the conditions for realizing the "perfect fiber dispersion assumption".
