---
title: "The Variation of Flow-Dependent Tensile Behavior in Radial Flow Dominant Placing of UHPFRCC (Kwon, Kang, Lee & Kim, 2012)"
type: source_note
source: "sources/Kwon-2012-The variation of flow-dependent tens.pdf"
citation: "Kwon, S.H., Kang, S.-T., Lee, B.Y., Kim, J.-K. The variation of flow-dependent tensile behavior in radial flow dominant placing of ultra high performance fiber reinforced cementitious composites (UHPFRCC). Construction and Building Materials 33 (2012) 109-121. doi: 10.1016/j.conbuildmat.2012.01.006"
date: 2026-08-22
tags: [uhpfrc, fiber-orientation, radial-flow, placement, tensile-behavior, jeffery-equation, fictitious-crack-model]
---

# Variation of Flow-Dependent Tensile Behavior in Radial Flow Placing of UHPFRCC

## Summary

This collaborative study by KAIST (Prof. Jin-Keun Kim, Prof. Su-Tae Kang, and Prof. Bang Yeon Lee) investigated the spatial variation in tensile and flexural behavior of a 1320×1320×100 mm UHPFRCC slab subjected to central free-fall radial flow placing. The authors cut 36 beam specimens from various locations to measure flexural tensile responses with flow distance, then developed a predictive framework combining a Jeffery-equation-based fiber rotation model, an orientation PDF-integrated bridging model, and a fictitious crack FEM model. Results proved that as flow distance increases, steel fibers align increasingly parallel to the circumferential flow front; consequently, mechanical performance degrades when the test axis is parallel to the flow direction and enhances when it is perpendicular.

## Key Contributions

- **Analytical framework for fiber orientation evolution in radial flow**: Inserted a 1D cylindrical radial velocity field ($V_r = Q/(2\pi r h)$, Vr=Q/(2πrh)) into Jeffery's equation to numerically track the evolution of fiber orientation angle $\theta$ probability density functions (PDF) across flow distances (110 steps at 5 mm intervals).
- **Structure-scale validation of bridging stress integration**: Integrated the directional PDF over the crack plane to compute fiber bridging stress $\sigma_B(\delta)$ (using the Lee et al. 2010 inclined pullout formulation) coupled with a bilinear matrix softening curve.
- **Experimental-analytical alignment**: In Series 2 (specimen axis perpendicular to radial flow), peak load and deflection-hardening increased with flow distance; in Series 1 and 3 (parallel), they decreased—an asymmetry accurately captured by the numerical model.
- **Practical design implications**: Quantified the hazards of directly extrapolating small-scale flexural test data to full-scale structures and provided an engineering basis for placement-guided fiber alignment strategies.

## Methods

- UHPFRCC mix proportions (mass ratios relative to cement): Cement 1.00, water 0.25, silica fume 0.25, fine aggregate 1.10, filler 0.30, superplasticizer 0.018, straight steel fibers (length 13 mm, diameter 0.2 mm) at 2 vol %.
- Casting: Free-fall from 200 mm height at slab center followed by radial free flow with surface leveling only. Cut into 36 beams ($100 \times 100 \times 440\ \text{mm}$, 100×100×440 mm) tested in 4-point bending over a 300 mm span using a 250 kN actuator under displacement control with LVDT deflection tracking.
- Modeling: Initial 3D random orientation $w(\theta,\phi) = 1/(4\pi)$ (w(h,φ)=1/4π), flow rate $Q = 0.001\ \text{m}^3/\text{s}$ (Q=0.001 m³/s), flow depth 50 mm. Single-crack interface element FEM combining matrix softening and fiber bridging.

## Results

- First crack deflection across all 36 beams fell within a narrow range of 0.06~0.08 mm regardless of location, whereas peak load varied significantly with spatial position.
- Series 1 (parallel): Peak load did not increase from center to edge; deflection-hardening vanished for $r \ge 275\ \text{mm}$ (r≥275 mm; beams 1-6 and 1-7 (1-6·1-7) showed immediate post-cracking load drops). Series 3 exhibited similar degradation.
- Series 2 (perpendicular): All beams displayed deflection-hardening, with maximum hardening increments in beams 2-7 through 2-10 (2-7~2-10); beams 2-11 and 2-12 (2-11~12, outer edge) showed slight reductions.
- Numerical PDF and load-deflection curves matched experimental trends, reproducing both hardening in beams 2-6/2-7 and softening in beams 1-6/1-7 and 3-6/3-7 (1-6/1-7·3-6/3-7).

## Related Notes

- [[kang-2008-fiber-orientation-djp0808]] — Previous study by the same research group on fiber orientation and flexural strength.
- [[kang-2011-fiber-distribution-uhsc-flexural-strength]] — Influence of steel fiber distribution characteristics on flexural strength (Reference 6).
- [[kim-2007-fiber-dispersion-fluorescence]] — Image-based quantitative evaluation of fiber dispersion.
- [[lee-2009-extruded-ecc-panel-fiber-distribution]] — Intentional extrusion alignment contrasted with flow-induced orientation.
- [[fiber-bridging-constitutive-law]] — Bridging stress framework incorporating orientation distribution functions.
- [[lai-2025-uhpfrc-nc-composite-beam-flexure]] — Structural applications of UHPFRC.
- [[afgc-2013-uhpfrc-recommendations]] — French UHPFRC design recommendations (orientation safety factor approach).
