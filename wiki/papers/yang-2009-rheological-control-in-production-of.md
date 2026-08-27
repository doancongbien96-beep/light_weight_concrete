---
title: "Rheological Control in Production of Engineered Cementitious Composites (Yang et al., 2009)"
type: source_note
source: "sources/2009-rheological-control-in-production-of.pdf"
citation: "Yang, E.-H., Sahmaran, M., Yang, Y., Li, V.C. Rheological control in production of engineered cementitious composites. ACI Materials Journal 106(4) (2009) 357-366."
date: 2026-08-22
tags: [ecc, rheology, plastic-viscosity, fiber-dispersion, fly-ash, taguchi-method, workability]
---

# Rheological control in the production of ECC

## Summary

A study statistically clarifying fresh-state rheology control so that ECC properties optimized by micromechanics design can be reproduced in the field. Analyzing four factors — C/F (Class C/Class F fly ash ratio), w/b, HRWR/B, and VMA/B — through a Taguchi L9 orthogonal array, it was the first to present a systematic dataset showing that plastic viscosity is governed by w/b and relative yield stress by HRWR/B, and that viscosity (and Marsh cone flow time) correlates strongly and positively with tensile strain capacity and ultimate tensile strength.

## Key Contributions

1. **Governing factors separated per rheology parameter (ANOVA contribution rates)**: plastic viscosity — w/b 58.4 % (negative), HRWR/B 16.2 %, VMA/B 3.8 %, C/F pooled (not significant); relative yield stress — HRWR/B 44.1 %, VMA/B 25.8 %, C/F 16.7 %, w/b 13.4 %. A practical route presented for controlling the two parameters independently via different factors (w/b versus HRWR/B).
2. **Viscosity to hardened-property correlation**: plastic viscosity and Marsh cone flow time correlate strongly and positively with both tensile strain capacity and ultimate tensile strength (holding within each C/F group as well), while being uncorrelated with yield stress. The mechanism is high viscosity improving fiber dispersion and bridging efficiency.
3. **Substitutability of simple tests established**: mini slump flow ↔ relative yield stress (R² = 0.96); Marsh cone flow time ↔ plastic viscosity (R² = 0.86). Field quality control is possible without a rheometer.
4. **Hardened-property factor contributions**: tensile strain capacity — C/F 41.0 % (positive), w/b 29.0 % (negative), VMA/B 20.8 %; ultimate tensile strength — w/b 62.1 % (negative, very significant), C/F 26.3 % (positive, significant), HRWR/B 10.1 %, VMA/B pooled. High w/b is doubly disadvantageous: degraded interfacial frictional bond plus lower viscosity.
5. **Mix recommendations**: keep w/b at 0.25 ± 0.05; achieve high plastic viscosity with low yield stress by adjusting HRWR (VMA optional due to cost). HRWR and VMA trends reverse beyond saturation points (near HRWR > 0.51 % and VMA > 0.008 %). For local materials, optimize fresh state first, then redesign materials per micromechanics if properties still fall short.

## Methods

- Fixed design variables: S/B = 0.37, FA/PC = 2.8, PVA fibers 2 vol.% (length 8 mm, diameter 39 μm, strength 1600 MPa, density 1300 kg/m³, hydrophobic oil coating 1.2 mass %); fine aggregate max particle size 250 μm, mean 110 μm. Cement OPC; FA conforming to ASTM C618 Class C/F.
- Taguchi L9(3⁴): C/F = 0 / 0.25 / 0.50, w/b = 0.21 / 0.23 / 0.25, HRWR/B = 0.27~0.76 %, VMA/B = 0 / 0.008 / 0.016 % (nine mixes).
- Measurement: rotational viscometer (Bingham T = g + Nh linear regression; g = relative yield stress, h = plastic viscosity, using descending curves, silicone oil correction); mini slump cone (bottom 100 mm/top 70 mm/height 60 mm); Marsh cone (1700 mL, outlet 20 mm). Repeatability CV < 3 %.
- Hardened tests: compression φ75×150 mm; direct tension coupons 152.4×76.2×12.7 mm (0.005 mm/s, two external LVDTs over a ~50 mm gauge); 28 days. Curing: sealed bags 7 d (23 ± 2 °C) then air drying at 50 ± 5 % RH.

## Results

| Mix (lowest/highest examples) | Viscosity (Pa·s) | Yield stress g (N·mm) | Marsh cone (s) | Compression (MPa) | UTS (MPa) | Strain (%) |
|---|---|---|---|---|---|---|
| No.7 (C/F 0.50, w/b 0.21, HRWR 0.27, VMA 0.008) | 17.89 | 14.24 | 35.00 | 58.1 | 6.44 | 2.69 |
| No.2 (C/F 0, w/b 0.23, HRWR 0.51, VMA 0.008) | 3.05 | 0.61 | 12.56 | 51.5 | 4.10 | 1.38 |

- Ranges across nine mixes: viscosity 1.69~17.89 Pa·s, g 0.29~14.24 N·mm, Marsh cone 8.88~35.00 s, mortar mini-slump 129~418 mm, compression 50.1~58.1 MPa, UTS 4.07~6.44 MPa, strain 1.38~2.69 %. Bingham fits R² ≥ 99.3 %.
- Factor effects per performance requirement (Table 10 summary): to raise viscosity, lower w/b (−4) and HRWR/B (−3), raise VMA/B (+2); to lower yield stress, raise HRWR/B (+4) while noting direction reversal caution on raising w/b (−3).

## Related Notes

- (Link debt: kong-2003 not yet ingested — [[li-2023-ecc-micromechanics-critical-review]]) — direct predecessor of SCC-ECC rheology control (references 5-6 of this paper). Constitutive approaches such as electrostatic dispersion stabilization.
- [[sahmaran-2009-aggregate-type-size-ecc]] — co-author Şahmaran's FA/aggregate study; complements this paper's C/F results through FA effects on interfacial frictional bond and fiber dispersion.
- [[li-2023-ecc-micromechanics-critical-review]] — this paper occupies the processing step that realizes the 'complete fiber dispersion assumption' of micromechanics design in reality.
- [[pseudo-strain-hardening-criteria]] — achieving σ_0 ≥ σ_c is a function of interface bond (τ, G_d) and fiber dispersion; this paper underpins it through fresh-state control.
