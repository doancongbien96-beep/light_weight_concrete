---
title: "Deterioration of Concrete Due to Reinforcement Steel Corrosion (Cabrera, 1996)"
type: source_note
source: "sources/cabrera-1996-deterioration-of-concrete-due-to.pdf"
citation: "Cabrera, J.G. Deterioration of concrete due to reinforcement steel corrosion. Cement and Concrete Composites 18 (1996) 47-59. doi: 10.1016/0958-9465(95)00043-7"
date: 2026-08-22
tags: [corrosion, deterioration, concrete-cracking, bond-strength, fly-ash, ccc]
---

# Deterioration of concrete due to reinforcement steel corrosion

## Summary

A classic corrosion-deterioration paper by Cabrera of CEMU, University of Leeds. Framed by
the problem that corrosion products generate internal pressure in the cover; once this
exceeds concrete tensile strength cracks form, degrading bond and effective steel section
until serviceability is lost. From accelerated-corrosion test data it built three regression
models: (a) corrosion rate back-calculated from crack width and cracking intensity,
(b) bond stress predicted from corrosion rate, and (c) serviceability loss predicted from
corrosion rate. Testing ran on OPC and PFA (30 % substitution) pozzolanic cement series
across three tracks — slab cracking characteristics, pullout bond strength, and beam
deflection. Headline results: cover thickness and degree of corrosion are inversely related,
but cracking intensity (total crack length basis) at equal corrosion grows with thicker
cover; PFA concrete's electrical resistance over 7x OPC's suppresses corrosion current to an
eighth or less, extending time-to-cracking about fivefold; bond strength first rises slightly
in early corrosion then collapses — at 12.6 % corrosion ultimate bond fell to 23.8 % of the
uncorroded value.

## Key Contributions

- **Corrosion-rate-from-crack-width inversion model**: with product density ρ=3.9 g/cm³
  (about twice the volume expansion of parent steel), measured mean and maximum widths agreed
  well with calculations below mass loss of 0.2 g/cm² — opening a practical route to estimate
  corrosion rate from visual crack observation alone.
- **Non-linear bond response established**: organized through the critical bond stress concept
  (lower of loaded-end slip 0.25 mm or free-end slip 0.051 mm); experiments confirmed peak-type
  behavior where products fill pores and raise confinement, raising bond initially before the sharp drop.
- **Anti-corrosion mechanism of PFA quantified**: simultaneous current-resistance measurement
  proved resistance growth as the direct cause of reduced corrosion. Reaching the same
  corrosion level took about 3x longer for PFA, and bond loss at equal corrosion was halved
  (PFA ~14 % vs OPC ~27 %).
- **Linear regression for serviceability loss**: deflection ratio Dr (corroded-beam deflection
  over uncorroded, at 0.6 × ultimate service load): Dr = 1.002 + 0.050C (r² = 0.960, OPC);
  Dr = 0.943 + 0.046C (r² = 0.936, PFA). At C = 9 % corrosion, deflection reaches 1.5x the
  uncorroded beam.

## Methods

- Mix: minimum-void design method at cement:sand:gravel = 1:2:3.35 (by weight), cement 325
  kg/m³, w/c 0.55. Admixed NaCl at Cl⁻ 2 % of binder. Rebar BS 4449 grade 460 high-bond bars;
  corners coated with 300 °C polymer insulation to isolate stirrup contact.
- Crack specimens: three rebars embedded 180 mm in 100×300×200 mm slabs (ends sealed; 160 mm
  effective exposure). Variables: bar diameter 12/16/20 mm (group A), OPC vs PFA (group B),
  transverse bars and cover 20/30 mm (group C).
- Pullout: 12 mm bar centered in a 150 mm cube at embedment 4φ ensuring bond-failure control.
- Beams: 125×160 mm section; Series I embedment 384 mm (BS 8110, flexure-controlled), Series II
  190 mm (bond-slip controlled); 100 mm recess under the load point for rebar strain and slip
  measurement.
- Exposure and acceleration: 20 °C 24 h mold cure then 35 °C / 45 % RH for 28 days; partial
  immersion in 5 % NaCl solution up to cover depth (tap-water controls). Rebar made anodic with
  a fluoride potentiostat at 3 V against SCE with stainless cathode. Corrosion mass by weight
  loss (pullout) and Faraday's law (beams). Crack width via Ultra Lomara 250b microscope;
  intensity as total surface crack length per area (300 cm²).

## Results

| Specimen | Variable | Mass loss (%) | Mass loss (g/cm²) | Cracking intensity (mm/cm²) |
|---|---|---|---|---|
| A-12 | diameter 12 mm | 17.73 | 0.463 | 0.93 |
| A-16 | diameter 16 mm | 12.80 | 0.393 | 0.95 |
| A-20 | diameter 20 mm | 6.76 | 0.345 | 1.02 |
| B-OPC | OPC, cover 20 mm | 19.21 | 0.480 | 0.74 |
| B-PFA | PFA, cover 20 mm | 3.55 | 0.045 | 0.20 |
| C-O | OPC, cover 30 mm | 13.48 | 0.320 | 0.99 |

- OPC corrosion current exceeded PFA's by 8x or more at all ages; PFA took on average 5x longer
  to first cracking. Only two PFA slabs cracked (42 and 46 days).
- Bond regressions: fbu = 23.478 − 1.313C (r² = 0.960, OPC); fbu = 26.133 − 1.341C (r² =
  0.909, PFA), fbu in MPa and C in %.
- Cracks always ran parallel to the rebar; first crack followed the shortest path (toward the
  cover), second cracks angled about 10° from the first — matching Ergatoudis et al.'s crack
  pattern models 1 and 2. With transverse bars present, cracking concentrated into single
  longitudinal cracks.
- Series I beams failed by rebar yield, Series II by free-end excessive slip — embedment length
  governs failure mode.

## Related Notes

- [[ahmad-2003-reinforcement-corrosion-in-concrete-structures]] : successor review covering the
  full corrosion mechanism
- [[castel-2000-mechanical-behaviour-of-corroded-reinforced]] : follow-up quantification of
  corroded RC member property degradation
- [[rodriguez-1997-corroded-reinforcement-capacity]] : residual capacity assessment of corroded
  reinforcement
- [[almusallam-1996-effect-of-reinforcement-corrosion-on]] : same-era experiments on corrosion
  effects on slab behavior
- [[el-maaddawy-2003-impressed-current-corrosion]] : follow-up application of the same
  impressed-current technique
- [[vidal-2007-corrosion-process-structural-performance-rc]] : lineage validating these
  accelerated results with natural-corrosion long-term data
- [[concrete-durability-and-service-life]] : concept page on the service-life prediction axis
  (Tuutti model succession)
