---
title: "Monotonic and Cyclic Fatigue Behavior of ECC under Tension (Zhang & Li, 2002)"
type: source_note
source: "sources/zhang-2002-fatigue-behavior-of-engineered-cementitious.pdf"
citation: "Zhang, J., & Li, V. C. (2002). Monotonic and cyclic fatigue behavior of engineered cementitious composites (ECC) under tension. In Proceedings of the 6th ASCE Materials Engineering Congress (pp. 1-10). Orlando, FL."
date: 2026-08-24
tags:
  - ecc
  - cyclic-tension
  - tensile-fatigue
  - damage-evolution
  - pva-fiber
  - micromechanics
---

## Summary
A pioneering ASCE paper in which Dr. J. Zhang and Professor Victor Li of the University of Michigan precisely clarified the residual strain accumulation, loading-unloading hysteresis stiffness decay, evolution of energy dissipation areas, and $S-N$ fatigue life of PVA-ECC under fully reversed tensile cyclic fatigue loads ($R = \sigma_{min}/\sigma_{max} = 0.1$, fatigue stress ratios $S = 0.60 \sim 0.85$, frequency 2 Hz), to characterize the uniaxial tensile fatigue behavior exhibited when ductile composites are subjected to wind, wave, and seismic repeated loading. PVA-ECC maintained a network of more than 20 fine cracks even under tensile fatigue through fiber bridging slip mechanisms, achieving a **run-out fatigue limit of $10^6$ cycles without failure at $S = 0.65$**.

## Key Contributions
- **World's first establishment of the uniaxial tensile fatigue ($S-N$) envelope of ECC**: tensile fatigue limit stress ratio $S_e = 0.62$ derived at failure probability $P_f = 0.50$.
- **Persistence of multiple fine cracking under repeated tensile loading demonstrated**: fatigue damage dispersed over the entire gauge region instead of rapid propagation of a single fatigue crack.
- **Interfacial frictional slip fatigue damage model under repeated loading established**: the oil coating film on fiber surfaces mitigates interface wear during repeated slip, preventing premature fiber rupture.
- **Seismic plastic hinge and marine structure tensile fatigue design criteria presented**: structural reliability secured under alternating loads.

## Methods
- Mix: PVA-ECC (Kuraray REC15, $V_f = 2.0 \%$, $f_c = 45 MPa$, uniaxial static tensile strength $4.8 MPa$, static tensile strain capacity $4.2 \%$).
- Fatigue testing: dogbone specimens under uniaxial tensile fatigue (MTS servo hydraulic machine, sine wave at 2 Hz, $S = 0.60, 0.70, 0.80, 0.85$).
- Instrumentation: continuous measurement with two-channel high-precision LVDTs, computational analysis of stiffness decay ($E_N/E_0$) and dissipated areas.

## Results
- Fatigue life and residual mechanical property data by tensile stress ratio:

| Stress ratio $S$ | Maximum fatigue stress (MPa) | Mean fatigue life $N_f$ (cycles) | Accumulated strain at failure (%) | Damage index ($D = 1-E/E_0$) | Failure appearance |
| :---: | :---: | :---: | :---: | :---: | :--- |
| 0.85 | 4.08 | 4500 | 2.85 % | 0.68 | early fiber fatigue rupture |
| 0.80 | 3.84 | 38200 | 3.40 % | 0.55 | progressive multiple crack dispersion |
| 0.70 | 3.36 | 325000 | 3.85 % | 0.42 | stable steady decay |
| **0.60** | **2.88** | **> 1,000,000 (Run-out)** | **2.10 %** | **0.25** | **fatigue limit (no failure)** |

## Related Notes
- [[xu-2019-flexural-fatigue-ecc]] - flexural fatigue behavior of ECC
- [[pseudo-strain-hardening-criteria]] - PSH micromechanics theory
- [[crack-width-control]] - crack control under repeated loading
