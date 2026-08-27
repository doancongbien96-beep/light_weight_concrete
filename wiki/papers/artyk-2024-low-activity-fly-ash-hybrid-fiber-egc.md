---
title: "EGC with Low-Activity Fly Ash and Hybrid Fibers: Experiment + Micromechanical Design (Artyk et al., 2024)"
type: source_note
source: "sources/1-s2.0-S0950061824009012-main.pdf"
citation: "Artyk, Z., Kuan, Y., Ogwumeh, C.M., Shon, C.-S., Zhang, D., Kim, J. Development of engineered geopolymer composite with low-activity fly ash and hybrid fibers: Experiment and micromechanical modeling. Construction and Building Materials 422 (2024) 135760."
date: 2026-08-22
tags: [egc, low-activity-fly-ash, hybrid-fiber, pva, pp, steel-fiber, micromechanics, thermal-conductivity, retrofit]
---

# Low-activity fly ash EGC with hybrid fibers: experiment and micromechanics-based design

## Summary

This study develops EGC from sub-standard low-activity fly ash (locally sourced in
Kazakhstan; 47 % passing the No. 325 sieve; strength activity index <75 %) blended 1:1 with
GGBFS, evaluating PVA/PP/steel hybrid fiber effects at a total of 2 vol %. The target is a
lightweight, thermally insulating, ductile composite for unreinforced masonry repair.
Calibrating micromechanical model parameters from single-crack tension tests, it delivers
hybrid design charts.

## Key Contributions

1. Strain-hardening achieved even with low-activity fly ash: an appropriate fiber combination
   simultaneously meets compression above 20 MPa, tensile strain beyond 2 %, and thermal
   conductivity under 0.25 W/mK.
2. Hybrid fiber effects: the PVA+PP pair is synergistic — highest compressive strength
   (25 MPa, over PVA-only 20.8 MPa). PVA alone reaches 2.1 MPa tensile strength at 2.72 %
   strain; 1.5 % PVA + 0.5 % PP matches this (2.1 MPa, 2.68 %) — a 25 % PVA saving. PP or
   steel fiber alone are brittle (PSH_S < 1.0).
3. Reassessment of PSH indices: the energy criterion PSH_E ≥ 2.7 lacks discriminating power in
   low-activity fly ash EGC (low K_m means no ductility even at PSH_E > 5); the strength
   criterion PSH_S ≥ 1.3 is the effective indicator. Linear index-capacity correlations are
   provided (R2 = 0.85/0.88).
4. Calibrated micromechanics parameters (Table 7): PVA G_d=0.73 J/m2, τ_0=1.05 MPa, β=0.58;
   PP τ_0=0.24 MPa; steel τ_0=2.1 MPa, β=0.75 — interface data for low-activity fly ash
   geopolymers against ECC literature ranges.
5. Validated superposition model for hybrids: volume-fraction-weighted superposition of
   single-fiber calibrated parameters predicts hybrid σ_B(δ); pre-peak response agrees well.
6. Design chart: minimum PVA content needed for a target capacity of 1.5 % — 0.84 % with PP,
   1.04 % with steel fiber, 0.95 % with both.

## Methods

Mix: FA:GGBFS 0.5:0.5; activator/binder 0.35 (Na2SiO3/NaOH 2.5, 12 M); W/B 0.38; S/B 0.36;
SP 1 %. Ambient sealed 24 h then air-cured. Tests: flow table, drying shrinkage (ASTM C490),
compression (cylinders), direct tension (dog-bone, 100 mm gauge), single-crack tension,
three-point flexure (for K_m), thermal conductivity. Parameter calibration via Dakota
Gauss-Newton (quoFEM).

## Results

- Density 1600–1700 kg/m3 (lightweight-concrete limit 1850).
- Drying shrinkage: matrix ~3 % at 35 days (the no-aggregate problem), reduced to 0.8 % with
  PVA. PP and steel fibers help little (~2 %).
- The matrix shows 7→28-day compressive strength regression (shrinkage cracking); fiber
  inclusion prevents it.
- Thermal conductivity ~0.2 W/mK across mixes — markedly below ordinary concrete's 1.36–2.0.
- Steel fiber alone (35 mm) disperses poorly due to length, lowest compression at 9.8 MPa.

## Related Notes

- A case of applying [[li-2023-ecc-micromechanics-critical-review]]'s backward-tailoring
  procedure to low-activity fly ash EGC. It reconfirms PSH_S ≥ 1.3 effectiveness and its
  caveat on PSH_E matrix dependence adds evidence to [[pseudo-strain-hardening-criteria]].
- The approach of cutting PVA oil-coating cost through hybridization pairs with the cost-
  carbon assessment in [[shumuye-2024-nanoparticles-egc-review]] for practicality analysis.
- [[lee-2008-database-mix-optimization-convex-hull]] — a different axis from backward
  tailoring: finding mixes via database plus optimization.
- Global quantitative grounds on FA supply and quality limits:
  [[scrivener-2016-unep-eco-efficient-cements]] §8 (~900 Mt/year, one third utilized).

- [[cho-2012-basic-mixing-and-mechanical-tests]] — early domestic demonstration of cement-free
  ductile composites (GGBS+PVA, KCI 2012): starting point of the low-activity/cement-free
  binder lineage.
