---
title: "ECC/SHCC Maximum Tensile Strain Capacity: Record Lineage and Best-Performing Mixes (Wiki Query Synthesis)"
type: overview
source: "wiki/papers 내 변형률능력 계보 노트 원문 대조 검증"
date: 2026-08-24
tags: [strain-capacity, ultra-ductile, record-lineage, pe-fiber, psh, overview]
---

# What is ECC's best performance? — Synthesis of the tensile strain capacity record

## Query

To answer "What is the best-performing ECC?", the strain-capacity lineage notes among
this wiki's 985 notes were compiled and verified against their source PDFs.

## Conclusion

Measured by tensile ductility (strain capacity), the records confirmed in this wiki are:

**Overall best: Luong et al. 2023 — alkali-activated slag composite (AASC), 22.34 ± 0.48 %**
- Mix: GGBS 0.90 + Ca(OH)₂ 0.10, silica sand 0.80, crumb rubber 0.05 (400 µm),
  PE fiber 1.75 vol.% (12 µm × 18 mm, 2700 MPa).
- Key finding: an improved mixing procedure (M1) raised the same mix's strain capacity
  from 9.81 to 22.34 % — a 2.3x gain. Compressive strength of 53.6 MPa alongside.
- Evidence: [[luong-2023-ed-aasc-22-percent]] (sources/IJP7123E_Extremely-ductile
  AAS_CERI.pdf, Ceramics International 49: 12069-12078)

## Record lineage (all PE-fiber systems)

| Year | Note | Matrix | Strain capacity | Remark |
| :--- | :--- | :--- | :---: | :--- |
| 2016 | choi-2016-ultra-high-ductile-aas-pe-composite | cement-free AAS | ~7.5 % | group's early ultra-ductility |
| 2019 | nguyen-2019-mechanical-properties-self-healing-slag-composites | cement-free AAS | 8.8 % | with self-healing |
| 2021 | [[nguyen-2021-ud-egc-13-7-percent]] | FA geopolymer | 13.68 ± 0.85 % | SMP/SH = 1.5 |
| 2022 | [[luong-2021-crumb-rubber-ultra-high-ductile-slag-composites]] | AAS + crumb rubber | 10.7 % | start of designed-flaw approach |
| 2023 | [[nguyen-2023-egc-activator-pretreatment]] | FA EGC | **18.62 ± 1.59 %** | cooling pretreatment (CP) |
| 2023 | [[luong-2023-ed-aasc-22-percent]] | cement-free AAS | **22.34 ± 0.48 %** | overall best |

Competing lineage (external group): Lao et al. 2023 (Hong Kong PolyU,
[[lao-2023-ultra-high-strength-ductility-sh-aasc]]) lead the strength axis with
120.4 MPa compression at ε_u 10.8 % simultaneously — not the outright ductility record,
but top-tier on the strength-ductility product.

## Cementitious (OPC) versus cement-free

- The ceiling of cementitious high-ductility systems lies around 8–9 %. The maintainer
  group's HP-SHCC and URSHCC ([[chun-2024-rc-beams-impact-resistance-hpfrcc]],
  [[chun-2025-strengthening-impact-rc-beams-hpfrcc]]) reached 9.08 % and 6.09 %.
- [[chen-2026-interfacial-bond-pe-fiber-alkali-activated]] supplies the theoretical reading:
  only DP-type fibers (UHMWPE etc.) sustain frictional slip feeding CMOD, enabling 6–12 %
  or more; DR-type fibers (steel, carbon) are mathematically capped below 2 %.
- It is therefore no coincidence that every historical record pairs PE/UHMWPE fibers with a
  low-toughness matrix (AAS, geopolymer).

## Common design principles for maximum ductility (PSH)

1. Minimize matrix fracture energy: K_m 0.06–0.11 MPa√m, J_tip < 1.3 J/m²
   (nguyen-2023 Table 6).
2. Secure bridging margin over first-cracking strength: σ₀/σ_fc ≥ 2 (chen-2026 critical
   margin; zhou-2010 experimental correlation R² = 0.98).
3. Introduce deliberate flaws: crumb rubber 400 µm (luong-2023), lightweight aggregate and
   PP beads (wang-2004-tailoring-preexisting-flaws-ecc) to control c_mc.
4. DP-type fine-diameter high-strength fibers: 12–24 µm PE at V_f = 1.75–2.0 %.
5. Processing is part of performance: identical mix, 2.3x difference from mixing procedure
   alone (luong-2023 M0 vs M1).

## Trade-off cautions

- The most ductile mixes show mean crack widths of 199–212 µm, exceeding the self-healing
  threshold (~100 µm) [[crack-width-control]], [[self-healing-ecc]]. For durability-driven
  design, the 13.7 %-class (ω_c 136.7 µm) or PVA systems (widths in the tens of µm) are the
  practical choice.
- Conflict with the strength axis: in nguyen-2023 the WP mix reached f_ts 8.72 MPa at
  ε_sc 10.97 %, while CP reached ε_sc 18.62 % at f_ts 5.54 MPa. The optimum differs by objective.

## Data integrity record (2026-08-24 lint)

Source-text verification exposed and corrected numeric contamination in three rewritten notes:
- luong-2023: 22.4 %→22.34 ± 0.48 %; deleted a fabricated micromechanics table (K_m 0.28,
  β 0.92, J'_b/J_tip 26.5 etc., absent from the source); corrected bibliography
  (Ceramics International volume 49).
- nguyen-2021: citation volume/article corrected (123:104183 → vol. 122, 104133); deleted
  fabricated values (J'_b/J_tip 15.8, crack count 145, CO₂ 72 %); ported the measured table
  of four UD-EGC mixes.
- nguyen-2023: 14.2 %→18.62 ± 1.59 % (CP); deleted fabricated values (τ₀ 1.82 MPa, β 0.85,
  W/B 0.28); ported measured WP/CP tables.
Lesson: rewritten notes can generate rhetoric and numbers detached from the source.
Quantitative claims must be checked against extracted source text before citing.
