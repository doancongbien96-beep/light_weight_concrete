---
title: "Tensile Strain-Hardening Behavior of PVA-ECC (Li, Wang & Wu, 2001)"
type: source_note
source: "sources/1st PVA_li_ACImat_01.pdf"
citation: "Li, V.C., Wang, S., Wu, C. Tensile strain-hardening behavior of polyvinyl alcohol engineered cementitious composite (PVA-ECC). ACI Materials Journal 98(6) (2001) 483-492."
date: 2026-08-22
tags: [pva-ecc, interface-tailoring, oiling-agent, complementary-energy, pddA, crack-width, scan-ocr]
---

# Tensile Strain-Hardening Behavior of PVA-ECC

## Summary

The original paper that developed PVA-ECC under the performance-driven design approach (PDDA), using PVA fiber surface treatment (oil coating amounts of 0.3/0.5/0.8 wt %) and sand content (s/c 0.5~1.2) as design variables. At V_f 2.0 % it achieved ultimate strain exceeding 4 % and ultimate strength of 4.5 MPa, securing saturated multiple cracking with crack widths kept below 100 μm. It elucidated the fundamental cause of the behavioral difference by comparing complementary energy against PVA-FRC.

## Key Contributions

1. Demonstration of interface tailoring: the target parameters demanded by the micromechanics model (G_d < 2 J/m², τ = 1.0~1.7 MPa) were realized through oil coating in collaboration with the manufacturer (Kuraray REC fibers). Increased coating amount → reduced G_d·τ → increased J′_b.
2. FRC-vs-ECC difference explained by complementary energy (Table 4): RMU PVA-FRC has J′_b = 0.5 J/m² < J_tip (3.2~4.7 J/m²) and is therefore quasi-brittle, whereas PVA-ECC has J′_b = 9.6~16.5 J/m² >> J_tip and therefore strain-hardens. With the same mix proportions and similar fiber strengths (1620 vs 1660 MPa), the outcomes are exactly opposite — demonstrating that the interface determines everything.
3. Optimal combination of coating amount and sand content: the 0.3 % coating lacked margin and showed large scatter (strain 1.4~4.0 %); the 0.8 % coating at s/c = 1.0 delivered strain 5.2 % and strength 5.0 MPa. Higher coating allows higher sand content — 0.8 % is recommended from cost and shrinkage-control perspectives.
4. SEM fracture-surface analysis: protruded fiber length increases with coating amount (RMU < 0.2 mm vs about 2 mm at 0.8 % coating) — confirming suppression of fiber rupture.
5. Elucidation of the crack-width stabilization phenomenon: after rapid initial growth, widths stabilize before 1 % strain, with a stable width of 60~100 μm. Error-function fit δ = A·erf(Bε) (A=57, B=2.32). On the grounds that water permeability depends on the cube of crack width and chloride penetration exponentially, durability implications are drawn.

## Methods

PVA-REC (39 μm, 12 mm, 1620 MPa, E 42.8 GPa), V_f 2.0~2.5 %, w/c 0.45, fine sand 110 μm. Direct-tension coupon specimens 304.8×76.2×12.7 mm (MTS 25 kN, LVDT gauge length 180 mm); crack tracking with a video microscope at 200× magnification.

## Results

- First-crack strength 2.6~3.9 MPa; saturated multiple-crack spacing 2.5 mm (V_f 2.0)/1.8 mm (V_f 2.5).
- Mean crack opening under load 80~160 μm (less when elastic recovery is accounted for).

## Related Notes

- A case of implementing the theory of [[li-wu-1992-psh-conditions]]·[[li-wu-1992-psh-design-hpfrcc]] in a PVA system — the experimental pillar literature behind [[pseudo-strain-hardening-criteria]].
- A representative study applying the slip-hardening·chemical-bond models (Lin et al., Redon et al.) cited by the [[li-2023-ecc-micromechanics-critical-review]] review.
- Same fiber family as the REC 1.2 % oil-coated PVA used by [[sahmaran-2009-aggregate-type-size-ecc]].
- The interface measurement methodology (Redon et al.) of [[nematollahi-2017-one-part-pe-shgc-micromechanics]] traces its lineage to this paper's single-fiber pullout procedure.
- [[qiu-2016-fatigue-dependent-fiber-bridging-model]] — extends this paper's PVA interface (chemical bond G_d + slip hardening) to cyclic loading conditions; the fatigue version of the issue of oil coating altering interface properties.

## Remarks

- Secured via OCR from a scanned copy. Some Table 3 values may be distorted — cross-check against the original before precise citation.
