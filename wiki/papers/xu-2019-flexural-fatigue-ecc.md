---
title: "Experimental Investigation on the Flexural Fatigue Behavior of ECC (Xu et al., 2019)"
type: source_note
source: "sources/xu-2019-experimental-investigation-on-the-flexural.pdf"
citation: "Xu, S., Hou, X., & Zhang, X. (2019). Experimental investigation on the flexural fatigue behavior of engineered cementitious composites. Construction and Building Materials, 220, 396-407. https://doi.org/10.1016/j.conbuildmat.2019.06.012"
date: 2026-08-24
tags:
  - engineered-cementitious-composites
  - flexural-fatigue
  - cyclic-loading
  - damage-evolution
  - weibull-distribution
  - s-n-relationship
---

## Summary
An original paper in which a team at Dalian University of Technology performed four-point flexural fatigue tests under fatigue stress ratios ($S = \sigma_{max}/f_r = 0.65, 0.70, 0.75, 0.80, 0.85, 0.90$, an R ratio of $R = 0.1$, sinusoidal loading at 5 Hz) to precisely evaluate the fatigue resistance of high-ductility composites (PVA-ECC) in repeated dynamic loading environments such as bridge decks, road pavements, and railway slabs, characterizing the increase in cyclic flexural deflection, dynamic elastic modulus degradation curves, evolution of the energy dissipation area, and an $S-N-P_f$ fatigue life prediction envelope based on the two-parameter Weibull statistical distribution. PVA-ECC dispersed deflection energy through a network of more than 30 fine cracks even under fatigue loading, demonstrating a non-failure limit (**Run-out**) of $2 \times 10^6$ cycles at $S = 0.70$.

## Key Contributions
- **Establishment of $S-N-P_f$ flexural fatigue life prediction envelopes based on the two-parameter Weibull distribution**: derivation of a fatigue limit stress ratio $S_e = 0.67$ at failure probability $P_f = 0.05$.
- **Demonstration of crack width restraint under repeated flexural fatigue loading**: individual crack widths were confirmed to remain below $45 \mu m$ even after $2 \times 10^6$ fatigue cycles.
- **Quantification of the three-stage fatigue damage evolution mechanism**: (stage 1) initial rapid stiffness loss (10 % of life), (stage 2) stable steady decay (75 % of life), (stage 3) rapid failure by fiber abrasion and rupture (15 % of life).
- **Presentation of flexural fatigue design guidelines for bridge decks and road pavements**: allowable flexural stress criteria provided.

## Methods
- Mix: PVA-ECC (Kuraray REC15, $V_f = 2.0 \%$, $f_c = 48.5 MPa$, static flexural modulus of rupture $f_r = 13.5 MPa$).
- Fatigue test: $100 \times 100 \times 400 mm$ prism beams; four-point flexural fatigue machine (span 300 mm, load-controlled $S = 0.65 \sim 0.90$, 5 Hz).
- Instrumentation: continuous recording of mid-span deflection with high-precision LVDTs, energy dissipation computed from dynamic hysteresis loops, SEM observation of fractured-fiber abrasion.

## Results
- Fatigue life and Weibull statistical analysis data by fatigue stress ratio:

| Fatigue stress ratio $S$ | Number of tests | Mean fatigue life $N_f$ (cycles) | Weibull shape parameter $m$ | Scale parameter $c$ | Fatigue failure mode |
| :---: | :---: | :---: | :---: | :---: | :--- |
| 0.90 | 5 | 2850 | 1.85 | 3200 | Localization failure after multiple cracking |
| 0.85 | 5 | 18500 | 2.10 | 20500 | Failure by progressive deflection increase |
| 0.80 | 5 | 68400 | 2.45 | 76000 | Typical three-stage damage failure |
| 0.75 | 5 | 485000 | 2.80 | 520000 | Distributed fine cracking over a wide area |
| **0.70** | **5** | **> 2,000,000 (Run-out)** | **-** | **-** | **Fatigue limit (no failure)** |

## Related Notes
- [[yu-2018-uhp-ecc-flexural-fatigue]] - flexural fatigue properties of UHP-ECC
- [[pseudo-strain-hardening-criteria]] - PSH micromechanics design theory
- [[crack-width-control]] - fine crack control under repeated loading
