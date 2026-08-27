---
title: "Fatigue Behavior of ECC under Cyclic Compression (Zolfagharnasab et al., 2022)"
type: source_note
source: "sources/zolfagharnasab-2022-fatigue-behavior-of-engineered-cementitious.pdf"
citation: "Zolfagharnasab, A., Ranjbar, N., & Zhang, Y. (2022). Fatigue behavior of engineered cementitious composites (ECC) under cyclic compression. Construction and Building Materials, 325, 126750. https://doi.org/10.1016/j.conbuildmat.2022.126750"
date: 2026-08-24
tags:
  - engineered-cementitious-composites
  - compressive-fatigue
  - cyclic-compression
  - damage-accumulation
  - pva-fiber
  - acoustic-emission
---

## Summary
To extend the fatigue life of structural members subjected to high-cycle repeated compressive loading, such as wind turbine foundations, offshore jacket platforms, and bridge piers, this study elucidated the residual plastic strain accumulation, elastic modulus degradation history, acoustic emission (AE) micro-damage evolution, and $S-N$ fatigue life envelope of a high-ductility composite (PVA-ECC, $f_c = 55 MPa$, PVA fiber $V_f = 2.0 \%$) under uniaxial compressive fatigue (cyclic compression, stress ratios $S_{max} = 0.65 \sim 0.85$, $S_{min} = 0.10$, frequency 4 Hz). PVA-ECC recorded a run-out limit of $2 \times 10^6$ cycles without failure even under the high compressive fatigue load of $S = 0.70$, demonstrating a fatigue life extended **15 times** over normal high-strength concrete.

## Key Contributions
- **Completion of a PVA-ECC compressive fatigue ($S-N-P_f$) life prediction model**: derivation of a fatigue limit stress ratio $S_e = 0.68$ at a failure probability of 5 %.
- **Quantification of the mechanism by which fiber bridging restrains the lateral expansion of compressive shear cracks**: AE signal analysis demonstrated delayed coalescence of microcracks into macroscopic cracks.
- **Establishment of three-stage fatigue damage evolution kinetics**: stage 1 initial stiffness degradation $\rightarrow$ stage 2 stable steady creep $\rightarrow$ stage 3 transition to rapid failure.
- **Proposal of fatigue design criteria for offshore wind power support structures**: a 40 % increase in the fatigue failure safety factor.

## Methods
- Specimens: $100 \times 200 mm$ cylinder specimens ($f_c = 55 MPa$, Kuraray REC15 PVA fiber $V_f = 2.0 \%$).
- Fatigue testing: MTS servo-hydraulic testing machine (4 Hz sine wave, $S_{max} = 0.65, 0.70, 0.75, 0.80, 0.85$, $S_{min} = 0.10$).
- Instrumentation: continuous LVDT measurement of axial and lateral strains, real-time elastic wave detection with 8-channel AE sensors.

## Results
- PVA-ECC life and accumulated strain data by compressive fatigue stress ratio:

| Fatigue stress ratio $S_{max}$ | Maximum fatigue stress (MPa) | Mean fatigue life $N_f$ (cycles) | Accumulated strain at failure ($\times 10^{-3}$) | Fatigue damage ($1-E/E_0$) | Failure mode |
| :---: | :---: | :---: | :---: | :---: | :--- |
| 0.85 | 46.75 | 12500 | 5.85 | 0.68 | Multiple shear fragmentation |
| 0.80 | 44.00 | 85000 | 5.20 | 0.55 | Shear band failure |
| 0.75 | 41.25 | 620000 | 4.65 | 0.42 | Gradual expansive failure |
| **0.70** | **38.50** | **> 2,000,000 (Run-out)** | **3.20** | **0.25** | **Fatigue limit (no failure)** |
| **0.65** | **35.75** | **> 2,000,000 (Run-out)** | **2.60** | **0.18** | **Fatigue limit (no failure)** |

## Related Notes
- [[zhang-2002-fatigue-behavior-ecc-cyclic-tension]] - ECC tensile fatigue behavior
- [[xu-2019-flexural-fatigue-ecc]] - ECC flexural fatigue properties
- [[high-strength-strain-hardening-composites]] - high-performance composite structural design
