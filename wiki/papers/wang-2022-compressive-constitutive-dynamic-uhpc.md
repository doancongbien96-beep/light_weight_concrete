---
title: "Compressive Behavior and Constitutive Model of UHPC under Dynamic Loading (Wang et al., 2022)"
type: source_note
source: "sources/wang-2022-compressive-behavior-and-constitutive-model.pdf"
citation: "Wang, Y., Zhang, Z., & Chen, Y. (2022). Compressive behavior and constitutive model of ultra-high performance concrete (UHPC) under dynamic loading. International Journal of Impact Engineering, 164, 104198. https://doi.org/10.1016/j.ijimpeng.2022.104198"
date: 2026-08-24
tags:
  - uhpc
  - dynamic-compression
  - strain-rate-effect
  - split-hopkinson-pressure-bar
  - constitutive-model
---

## Summary
This study evaluated the dynamic uniaxial compressive behavior of ultra-high performance concrete (UHPC, static compressive strength $150 MPa$) under impact and blast loading using a split Hopkinson pressure bar (SHPB) over the strain rate band $\dot{\epsilon} = 30 \sim 250 s^{-1}$. The dynamic increase factor (DIF), peak strain increase, energy absorption density, and crushed fragment size distribution accompanying increasing strain rate were analyzed in detail by laser diffraction particle size analysis. A nonlinear dynamic compressive constitutive model combining strain-rate hardening with continuum damage mechanics was established, and a user subroutine (VUMAT) deployable in finite element analysis programs was developed.

## Key Contributions
- **Establishment of a DIF empirical relation and mechanics model for UHPC under ultra-high-speed compression**: modeling of the regime $DIF = (\dot{\epsilon}/\dot{\epsilon}_0)^{0.045}$ ($\dot{\epsilon} \le 80 s^{-1}$) together with the exponentially surging regime.
- **Quantification of the dynamic fragmentation confinement effect of the steel fiber volume fraction ($V_f = 1.5 \sim 3.0 \%$)**: demonstrated that a higher fiber content suppresses the scattering of fragments after high-speed impact and prevents pulverization of the crushed material into sand-size powder.
- **Completion of a rate-dependent damage plasticity constitutive model**: achieved prediction error within 5 % for stress-strain curves across the entire static and dynamic range.

## Methods
- **Mix proportion**: $W/B = 0.16$, silica fume 25 %, straight high-strength steel fibers ($V_f = 2.0 \%$, diameter 0.2 mm, length 13 mm, strength 2600 MPa).
- **Test equipment**: 75 mm diameter steel SHPB apparatus, semiconductor strain gauges, and high-speed video recording.

## Results
- Dynamic compressive strength: static $152 MPa \rightarrow \dot{\epsilon} = 220 s^{-1}$ reaching $245 MPa$ ($DIF = 1.61$).
- The impact fracture energy absorption density increased 3.8-fold relative to the static case, demonstrating maximized blast resistance and penetration resistance performance.

## Related Notes
- [[ke-2023-dynamic-compressive-behavior-uhpc]] — comparison of the dynamic compressive behavior of UHPC
- [[impact-and-blast-resistance-frcc]] — impact resistance analysis of high-strength fiber composites
