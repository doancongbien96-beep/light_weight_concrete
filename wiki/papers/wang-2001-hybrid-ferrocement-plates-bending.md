---
title: "Bending Response of Hybrid Ferrocement Plates with Meshes and Fibers (Wang, Naaman & Li, 2001)"
type: source_note
source: "sources/bending_namman.pdf — 파일명은 제목 앞부분(BENDING)+2저자 성(Naaman) 오기 조합, 실제 1저자는 Shuxin Wang. 풀스캔 PDF로 OCR(kor 아닌 eng) 원전이라 수식·일부 표 판독값에 불확실성 있음"
citation: "Wang, S., Naaman, A.E., Li, V.C. Bending response of hybrid ferrocement plates with meshes and fibers. Proc. 7th Int. Symp. on Ferrocement and Thin Reinforced Cement Composites (FERRO-7), National University of Singapore, 2001. 6. 27-29, pp. 247-260."
date: 2026-08-23
tags: [ferrocement, hybrid-composite, expanded-steel-mesh, kevlar-frp-mesh, pe-fiber, pva-fiber, ecc-matrix, mor, michigan-group, ocr-source]
---

# Bending Response of Mesh+Fiber Hybrid Ferrocement Thin Plates

## Summary

An experimental study by the University of Michigan group (Naaman and Li) elucidating the four-point bending behavior of hybrid ferrocement thin plates combining meshes (expanded steel meshes ES1/ES2 and Kevlar FRP mesh) with short fibers (Spectra PE and PVA). Its thrust is that increasing the number of mesh layers is inefficient for MOR improvement, while the problem of early failure through cover delamination and outermost tensile-layer separation at high reinforcement ratios is solved by incorporating short fibers. Using a PE-ECC matrix gives a 64 % MOR increase with sharply reduced crack spacing, and the Kevlar mesh+ECC combination achieves an MOR equivalent to four steel mesh layers (6.73 % by volume) at about 1/6 the reinforcement amount while shrinking crack spacing to 1/5. Nonlinear analysis shows good agreement with the predicted MOR.

## Key Contributions

- Reinforcement strategy: at equal volume fraction, concentrating layers in the outermost positions (ES2, 2 layers) outperforms dispersed placement (ES1, 4 layers) in both MOR and stiffness — Series 3's MOR is nearly triple that of Series 1.
- Quantifying the ECC matrix effect: relative to plain mortar, the PE-ECC matrix (Series 4) yields MOR +64 % (39.9 vs 23.3 MPa), countless microcracks, and complete suppression of cover delamination. By contrast, the strain-softening PVA-FRC matrix (Series 6, Vf 2 %>1.5 %) improves only marginally — proof that matrix strain-hardening design, not fiber amount, governs.
- Redefining the fiber role in the over-reinforced regime: when compressive crushing failure dominates, the fibers' MOR contribution is limited (Series 5 vs 2), yet by raising matrix shear resistance they significantly delay interlayer separation of the outermost tensile layer and prevent cover delamination — a failure-mode-control rather than strength perspective.
- Kevlar FRP mesh (ECC matrix): similar behavior regardless of L/T orientation. After computing the balanced reinforcement ratio ρb=0.221 %, both series (0.36 %/0.215 %) were over-reinforced with compression failure preceding; because ECC compressive behavior is gradual, MOR>40 MPa was maintained even at large deflection (35 mm). The brittle interlayer-separation failure characteristic of FRP mesh converts to ductile failure with 1.5 % PE fibers.
- Crack control: primary crack spacing of 3~4 mm (matching the Kevlar transverse yarn spacing), with secondary microcracks between them closing upon load removal thanks to Kevlar elastic recovery. Series 7 (Kevlar+ECC) has a crack spacing about 1/5 that of four steel mesh layers (Vs=6.73 %).
- Toughness: versus the fiber-free Control, 2.0~2.1x at PVA 1 % and 3.9x at PE 1.5 % (No.8; No.7 unreadable due to OCR damage). Energy absorption up to +250 % per the abstract.
- Predictive models: steel mesh+PE-ECC reproduced by a closed-form equilibrium equation assuming uniform tensile-block stress (σt=5 MPa); the Kevlar combination reproduced by strain-compatibility nonlinear section analysis of the MOR and load-deflection curves (Table 5 errors within a few %).

## Methods

- Specimens: 304.8×76.2×12.7 mm thin plates, 24 total across 8 series, four-point bending (span 228.6 mm), MTS 810 (100 kN), external LVDTs, water curing at ages 12~14 days.
- Meshes: ES1 (opening 25.4 mm)/ES2 (12.7 mm), gage 20 expanded steel mesh, thickness 0.76 mm (yield strength ES1 307 MPa<ES2 410 MPa); Kevlar FRP mesh (10×6 bundle/in², 1500 denier, longitudinal leno weave, tensile strength 2800 MPa, effective modulus 124 GPa, elongation 2.8 %).
- Fibers: Spectra 900 PE (length 19 mm, diameter 38 μm, modulus 120 GPa, strength 2400 MPa) at 1.5 vol %; PVA1 (12 mm)/PVA2 (6 mm) (modulus 29 GPa, strength 900 MPa) at 1.0~2.0 vol %.
- Matrix: Mix1 cement:silica sand:water=1:1:0.36 (f'c 71 MPa); Mix2 1:0.5:0.28 (f'c 74 MPa) — Mix2+Spectra 1.5 % serves as the PE-ECC (εtu up to 6 %, σt 5 MPa).

## Results

- Experimental MOR (Table 5): No.1 23.3, No.2 42.6, No.3 63.4 (exceeding 60 MPa, Vs 6.73 %), No.4 39.9, No.8 (Kevlar T-direction) 41.2 MPa — agreeing with predictions (23.8/41.8/62.8/39.3/43.7 MPa) within small differences.
- Failure modes: No.1 flexural-tensile ductile failure; No.2 compressive crushing failure (over-reinforced); No.3 horizontal-shear-induced separation of the outermost tensile layer.
- Toughness index (area ratio up to 20 mm deflection): No.1 88.4, No.2 81.9, No.3 542, No.4 123, No.5 548, No.6 110 — numerically confirming that the fiber benefit is marginal at high reinforcement ratios (No.3 542 vs No.5 548).
- Because of the leno weave the Kevlar mesh's longitudinal effective stiffness is unknown → only the T direction was analyzed. Despite the Vs difference of 0.72 % vs 0.43 %, flexural stiffness is nearly identical (the longitudinal direction is denser, but the leno weave attenuates its effective stiffness).
- The fibers' strength contribution concentrates in the post-mesh-yield bridging regime — dependent on fiber-interface properties and on Vf.

## Related Notes

- [[pseudo-strain-hardening-criteria]] — theoretical basis for the ECC matrix performance of Series 4 and 7 (strain-hardening and multiple cracking)
- [[fiber-bridging-constitutive-law]] — analytical frame for the strength-gain regime governed by fiber bridging forces after mesh yielding
- [[yang-2008-fiber-bridging-constitutive-law-of-ecc]] — the experimental calibration paper for the σ(δ) law
- [[li-2023-ecc-micromechanics-critical-review]] — hub overview of co-author V.C. Li's ECC micromechanics design axis
