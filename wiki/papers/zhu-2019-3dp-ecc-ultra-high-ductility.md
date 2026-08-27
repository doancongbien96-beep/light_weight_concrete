---
title: "Development of 3D Printable ECC with Ultra-High Tensile Ductility for Digital Construction (Zhu et al., 2019)"
type: source_note
source: "sources/3D printable ECC UH.pdf"
citation: "Zhu, B., Pan, J., Nematollahi, B., Zhou, Z., Zhang, Y., Sanjayan, J. Development of 3D printable engineered cementitious composites with ultra-high tensile ductility for digital construction. Materials and Design 181 (2019) 108088. doi: 10.1016/j.matdes.2019.108088"
date: 2026-08-22
tags: [3d-printing, pe-ecc, ultra-high-ductility, thixotropy, buildability, fiber-alignment]
---

# Development of 3D printable ECC with ultra-high tensile ductility

## Summary

A paper developing a PE-ECC for extrusion-based 3DCP that achieved a tensile strain of up to 11.4 % (superior to casting). The goal was realizing a 'self-reinforced' structure rather than substituting steel fibers. Extrudability and buildability were secured through HPMC plus attapulgite nanoclay (ANC) thixotropic admixtures in a ternary binder of OPC + sulphoaluminate cement (SAC) + fly ash.

## Key Contributions

1. Ultra-high ductility achieved: with PE fibers of aspect ratio 500 (12 mm × 24 μm, 3 GPa, E = 116 GPa), a strain of 9.57 % at $V_f$ of 1.5 % and 11.43 % at 2 %. Far exceeding prior 3DP-ECC literature (PVA ~4 %, HDPE 3.2 %).
2. Finding that printing outperforms casting: at $V_f$ of 1.5~2 %, the tensile strength and strain of 3D printed ECC exceeded cast counterparts by 6~13 % and 12~14 % respectively. Two causes:
   - Optimized fiber orientation: effective fiber count per section parallel to the load direction was 4241/cm² for casting versus 6072/cm² for printing (SEM statistics). Extrusion aligns fibers with the stress direction.
   - Homogenized pore distribution: the pore size distribution of printed matrices is narrower, reducing scatter in the J′_b/J_tip margin → stable saturated multiple cracking.
3. Reversal in the low-fiber regime: at $V_f$ of 1.0 %, printing strain of 3.57 % fell below casting at 5.46 % — below the saturation multiple-cracking threshold, insufficient crack number governs over alignment benefit. The applicability limit of the orientation effect is stated explicitly.
4. Quantitative buildability indices proposed: dimensionless H (height loss ratio), W (width expansion), ϕ (diameter expansion) — from a 17-layer cylinder stacking test. M2 (thixotropy added) showed H 0.8 %, W 5.5 %, ϕ 0.7 %, overwhelmingly better than M1 (4.3/26.0/8.3 %).
5. Viscosity recovery rate (VRR) as a printability indicator: under protocol 1, M2 showed VRR of 83.1 % versus 61.2 % for M1. Static yield stress was also higher for M2, favoring stacking.

## Methods

Brookfield RST-SST vane viscometer (two protocols, Bingham down-curve fitting); gantry printer (auger extruder, nozzle 20 mm, travel 100 mm/s, extrusion 100 g/s, layer height 13 mm); JSCE dogbone (LVDT gauge 80 mm); GB/T 17671 flexure and compression; SEM + ImageJ pore statistics.

## Results

- Compressive strength 47.5~51.1 MPa (printing 2~12 % lower — interlayer voids); flexural strength 13.2~19.4 MPa (printing 4~9 % higher).
- Crack widths 69~82 μm (M2·M3); crack numbers 93~132 per 80 mm gauge.
- Pore size (67~68 μm) close to mean crack width — uniform flaw size contributes to equalized multiple cracking.

## Related Notes

- Same-group (Pan Jinlong, Southeast University) follow-up dynamic research lineage with [[pan-2023-dynamic-compressive-shpb-egc]].
- The logic of using pores as design factors lowering J_tip and σ_c parallels [[li-mo-2011-hes-ecc-repair]] polystyrene beads — an intentional initial-flaw strategy (directly linked to EPS-beads low-fiber EGC design).
- Reproduces in tension the orientation-strength relation of [[kang-2008-fiber-orientation-impacts-on-the]]: the difference between casting direction (random) and extrusion (aligned) appears directly as performance difference.
- A case where the rheology control frame of [[yang-2009-rheological-control-in-production-of]] extends to printing requirements (extrudability plus buildability).
