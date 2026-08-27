---
title: "Tailoring of Pre-existing Flaws in ECC Matrix for Saturated Strain Hardening (Wang & Li, 2004)"
type: source_note
source: "sources/WangFramcos5.pdf"
citation: "Wang, S., Li, V.C. Tailoring of pre-existing flaws in ECC matrix for saturated strain hardening. In Fracture Mechanics of Concrete Structures (FRAMCOS-5 학술대회 논문집), Li et al. eds, Ia-FraMCos, 2004, pp. 1005-1012. ISBN 0 87031 135 2."
date: 2026-08-23
tags: [ecc, artificial-flaw, multiple-cracking, psh, pva-ecc, flaw-size-distribution]
---

# Creating Saturated Multiple Cracking by Introducing Artificial Flaws

## Summary

The filename WangFramcos5 points to Wang (Shuxin Wang) plus the 5th FRAMCOS conference; the bibliographic record was confirmed from the paper's cover page. The paper proposes and validates a practical technique for achieving saturated multiple cracking by controlling the natural flaw size distribution of the matrix. Since the maximum fiber bridging stress σ0 sets the lower bound on activatable flaw sizes (the critical flaw size c_mc), deliberately inserting artificial flaws larger than this bound, using lightweight aggregates or plastic beads, recovers multiple cracking even in high-toughness matrices. Origin paper of the wiki's artificial-flaw design axis (PS beads, polystyrene bead lineage).

## Key Contributions

1. **Turning the critical flaw size concept into a design tool**: the crack strength of a brittle matrix is determined by the largest flaw in the cross-section, and σ0 imposes a lower bound so that only flaws larger than c_mc contribute to multiple cracking. Together with the J'b/Jtip>3 margin index (Kanda & Li 1998), this presents an alternative design axis that manipulates the flaw distribution directly instead of relying on low-toughness matrices; it is particularly effective for mixes forced into a high-strength, high-modulus, workable W/B regime.
2. **Dramatic effect of large artificial flaws**: Mix 2 (Norlite expanded shale lightweight aggregate 3.5 mm, 0.07 vol.%) raises strain capacity 0.38 %→2.48 % and cuts mean crack spacing 16.2 mm→2.4 mm. Mix 4 (Norlite 3.5 mm + PP beads, 4 × 2 mm ellipses, 0.07 vol.%) goes 1.86 %→3.79 % (improvement exceeding 100 %) and cuts crack spacing 4.8 mm→2.2 mm. Ultimate tensile strength is essentially unaffected; only first-cracking strength drops slightly (the introduced flaw size is comparable to the pre-existing largest void and therefore does not reach the steady-state cracking stress that lower-bounds crack strength).
3. **Decisiveness of size control (the Mix 5 counterexample)**: small Norlite at 1 mm (0.10 vol.%, replacing part of the sand) gives no improvement (1.89 %) despite the greater count; an artificial flaw activates only when its size rivals the natural maximum void. Introduced sizes were selected to match the largest void sizes observed on cracked cross-sections.
4. **Experimental characterization of the natural flaw system**: most large flaws are entrapped air voids, and the largest void on cracked cross-sections exceeds that of uncracked ones, with more voids larger than 1 mm as well (Mix 1: 2.5~5 mm averaging 3.4 mm; Mix 3: 1.7~4.2 mm averaging 2.8 mm). Matrix KIc is 0.67 for Mix 1 vs 0.61 MPa√m for Mix 3, so the lower first-cracking strength of Mix 3 despite its smaller voids is explained by the toughness difference.
5. **Consistency with crack-spacing theory**: the Wu & Li 1995 minimum crack-spacing formula (assuming f=0.7, τ0=3.5/2.7 MPa) gives x_d≈1.09 mm (Mix 2) and 1.02 mm (Mix 4); measured mean spacings sit near the theoretical upper bound of 2x_d, consistent with saturated multiple cracking.

## Methods

- Materials: PVA REC15 fibers (Kuraray) at 2 vol.%, length 12 mm, diameter 39 μm; Type I OPC, silica sand (mean 110 μm), Class C fly ash, high-range water reducer. Three artificial-flaw candidates — Norlite expanded shale lightweight aggregate (means of 1.0 mm and 3.5 mm, porous with low tensile strength) and PP plastic beads (elliptical, major/minor axes about 4 mm and 2 mm, behaving like embedded cracks owing to extremely weak interfacial bonding).
- Five mixes in two groups: Group 1 (Mix 1~2, FA 0.8, W/B 0.43); Group 2 (Mix 3~5, FA 1.2, W/B 0.53) — deliberate control mixes whose intentionally high matrix toughness (J'b/Jtip 0.44~1.24) suppresses multiple cracking, contrasted against the J'b/Jtip of 4.84~7.62 for saturated PVA-ECC by Li et al. 2002.
- Testing: coupons 304.8 × 76.2 × 12.7 mm, water curing 28 d, displacement-controlled direct uniaxial tension at 0.15 mm/min, two surface-mounted LVDTs (gauge about 180 mm), mean crack spacing measured after unloading. Control coupons were diamond-saw cut through cracked/uncracked cross-sections, and the large-void distribution was observed under a 200x optical microscope.

## Results

| Mix | Artificial flaw | First-cracking strength (MPa) | Ultimate strength (MPa) | Strain capacity (%) | Crack spacing (mm) |
|---|---|---|---|---|---|
| 1 (control) | None | 4.88 | 6.40 | 0.38 | 16.2 |
| 2 | Norlite 3.5 mm 0.07 vol.% | 4.75 | 6.82 | 2.48 | 2.4 |
| 3 (control) | None | 4.06 | 4.84 | 1.86 | 4.8 |
| 4 | Norlite 3.5 mm+PP beads 0.07 vol.% | 3.74 | 4.63 | 3.79 | 2.2 |
| 5 | Norlite 1 mm 0.10 vol.% | 3.80 | 4.90 | 1.89 | 4.9 |

- Crack patterns: the controls show wide spacing distributions reaching 2~50 mm together with crack-free face areas (unsaturated), while the artificial-flaw mixes show nearly saturated uniform distributions.
- Extraction was OCR-based, so the table figures were cross-checked against the body narrative (e.g., 0.38→2.48 %, 16.2→2.4 mm); room for comparison against the original remains for the table's full set of values.

## Related Notes

- [[pseudo-strain-hardening-criteria]] — origin axis of the J'b/Jtip margin index and the conditions for achieving PSH
- [[kanda-2006-saturated-psh-design-criteria-ecc]] — practical extension of the performance-index (J'b/Jtip>3) lineage cited by this paper
- [[fiber-bridging-constitutive-law]] — structural relation whereby the σ(δ) complementary energy J'b governs c_mc and the number of activated flaws
- [[li-wu-1992-psh-conditions]] — origin of the minimum crack-spacing and PSH-condition lineage
- [[wu-1992-snubbing-bundling-crack-spacing]] — crack-spacing theory axis including the snubbing coefficient f
- [[yu-2016-uhpc-artificial-flaw]] — user-group UHPC application follow-up of the artificial-flaw (PS bead) strategy
