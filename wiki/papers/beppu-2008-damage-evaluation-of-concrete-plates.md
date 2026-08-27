---
title: "Damage Evaluation of Concrete Plates by High-Velocity Impact (Beppu et al., 2008)"
type: source_note
source: "sources/Beppu 등 - 2008 - Damage evaluation of concrete plates by high-velocity impact 1.pdf"
citation: "Beppu, M., Miwa, K., Itoh, M., Katayama, M., Ohno, T. Damage evaluation of concrete plates by high-velocity impact. International Journal of Impact Engineering 35(8) (2008) 1419–1426. doi: 10.1016/j.ijimpeng.2008.07.021"
date: 2026-08-22
tags: [impact, high-velocity, concrete, cratering, spalling, perforation, autodyn, strain-rate-effect]
---

# Local damage evaluation of concrete plates under high-velocity impact

## Summary

A paper that used a newly developed air-gun launch apparatus (12 m acceleration tube, 35 mm
inner diameter) to fire rigid mushroom-shaped projectiles (head diameter 25 mm, 50 g) at
50–1000 g masses and 100–500 m/s onto concrete plates 3–13 cm thick (fc 25 N/mm²), elucidating
the three local damage modes of cratering→spalling→perforation experimentally and numerically.
The fracture process was tracked at millisecond resolution with a high-speed camera and surface
strain gauges, and AUTODYN 2D axisymmetric analysis showed that only the combination of the
nonlinear Drucker–Prager yield criterion plus strain-rate effects (ε̇ = 10¹ s⁻¹) reproduced the
experiments.

## Key Contributions

1. **Experimental data on failure-mode boundaries**: for an 8 cm plate, impact velocity
   210 m/s → cratering (frontal crater diameter about 10 cm plus rear-face radial cracks),
   310 m/s → spalling (rear-face scab area > frontal crater), 415 m/s → perforation. Penetration
   depth is roughly proportional to impact velocity, and the modified NDRC equation [2] predicts
   the failure-mode boundaries well but overestimates penetration depth.
2. **Time-resolved observation of the damage process**: rear-face circular cracks formed at
   0.1–0.2 ms after impact, and concrete chunk scattering occurred at 5–15 ms (9 cm thickness,
   420 m/s). Internal cracks developed from the impact point through to the rear face. Frontal
   cratering finished crushing and pulverizing the surface concrete within 0.6 ms.
3. **Quantitative evidence of rear-face strain behavior**: the rear gauge reached a maximum
   compressive strain of 1100 με (at 0.14 ms) and then reversed into tension — instrumentation
   confirming that the compressive stress wave reflected off the free surface as tension,
   inducing spalling. The front gauge oscillated in the compressive regime (~250 με), and gauges
   near the impact point failed immediately.
4. **Numerical model sensitivity established**: exploring linear versus nonlinear
   Drucker–Prager criteria × ε̇ = 10⁻⁵~10² s⁻¹ showed that (i) reproducing penetration depth
   requires a nonlinear criterion with the same descending shape seen under high triaxial
   confinement, and (ii) higher strain rates localize damage (because the tensile strength
   increase ratio exceeds the compressive one); the combination of the nonlinear criterion +
   ε̇ = 10¹ s⁻¹ reproduced the experiments.
5. **Conceptual diagrams of the cratering/spalling mechanisms**: immediate post-impact plastic
   yielding of the loaded region → rapid expansion of the plastic zone (starting at
   t ≈ 1.13×10⁻³ ms); reflection of the compression wave off the free surface causing rear-face
   tensile failure (t ≈ 3.49×10⁻² ms); along the spalling path, additional diagonal cracks form
   and develop (t ≈ 5.36×10⁻² ms) before the scabbed fragment detaches at 2–3 m/s.

## Methods

- **Launch system**: air chamber + booster + compressor; 12 m/φ35 mm acceleration tube;
  velocity ranges per projectile mass 100 g: 250–500 m/s / 1000 g: 100–250 m/s; kinetic energy
  3–32 kJ. MC901 nylon sabot.
- **Tests**: 500 × 500 mm concrete plates (thickness 3–13 cm, fc 25 N/mm², E 25.5 kN/mm²,
  ν 0.15), impact velocities 200–500 m/s. Fracture process filmed with a high-speed video camera;
  strain gauges of 8 cm gauge length mounted on front and rear faces (at 50/150 mm from center,
  4 per face).
- **Numerical analysis**: AUTODYN, 2D axisymmetric, 4-node quadrilateral elements (12,800 plate
  elements @ 2.5 × 2.5 mm, 28 projectile elements). Linear equation of state; steel modeled as
  elastic (recovered projectiles confirmed undamaged); erosion criterion set at an effective
  strain of 2.5 (250 %). Validation target was the spalling case (8 cm thickness, 310 m/s).
  DIF: Fujikake et al. [3] for compression and Ross et al. [4] for tension adopted, with static
  strain rates of 1.2×10⁻⁵ and 1.0×10⁻⁷ s⁻¹ respectively.

## Results

- **Strength increase at assumed strain rates (Table 2)**:

| ε̇ (s⁻¹) | Compressive DIF | Tensile DIF | fc′d (MPa) | ft′d (MPa) |
|---|---|---|---|---|
| 10⁻⁵ (static) | 1.00 | 1.00 | 25.00 | 2.50 |
| 10⁻¹ | 1.26 | 1.70 | 31.50 | 4.25 |
| 10⁰ | 1.44 | 2.44 | 36.00 | 6.10 |
| 10¹ | 1.70 | 4.06 | 42.50 | 10.15 |
| 10² | 2.07 | 8.04 | 51.75 | 20.10 |

- Back-calculated strain rates from the actual fracture process (within 1 ms, strains
  100–2000 με) fall in the 10⁻¹~10² s⁻¹ order.
- The numerical analysis reproduced the failure mode and penetration depth of every test case
  (Fig. 19). Strain histories were reasonably reproduced for front gauge 2 and outer gauges 6·8
  in both profile and maximum, but rear gauges 5·7 differed substantially owing to mismatched
  crack locations between test and analysis (the limitation of point-wise strain comparison is
  stated explicitly).
- Follow-up tasks named: effects of projectile shape and stiffness, and 3D analysis.

## Related Notes

- [[pan-2023-dynamic-compressive-shpb-egc]] — SHPB-driven high-strain-rate compression of EGC
  (the materials end) and this paper's plate-level local damage (the structural end) sit at the
  two extremes of the dynamics spectrum; shared adoption of strain-rate effect (DIF) factors is
  the common discussion point.
- [[han-2022-egc-impact-cold-temperature]] — plain-concrete baseline data for ECC/EGC impact
  resistance research; the starting point for comparing how fiber bridging suppresses spalling
  and scattering.
- The contrast between empirical-formula design such as the modified NDRC and mechanism-based
  numerical analysis recurs as a framing in the impact-resistant design of UHPC/ECC
  ([[abbas-2016-uhpc-mechanical-performance-durability-sustainability]]).
