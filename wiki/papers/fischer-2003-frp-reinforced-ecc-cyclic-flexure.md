---
title: "FRP 보강 ECC 휴 부재의 변형 거동 — 반복가력 조건 (Fischer & Li, 2003)"
type: source_note
source: "sources/2003-deformation-behavior-of-fiber-reinforced-polymer.pdf"
citation: "Fischer, G., and Li, V. C. \"Deformation Behavior of Fiber-Reinforced Polymer Reinforced Engineered Cementitious Composite (ECC) Flexural Members under Reversed Cyclic Loading Conditions.\" ACI Structural Journal, V. 100, No. 1 (2003), pp. 25-35."
date: 2026-08-22
tags: [frp-reinforcement, reinforced-ecc, reversed-cyclic-loading, bond, residual-deflection, moment-curvature]
---

# Cyclic Flexural Deformation Behavior of FRP-Reinforced ECC Members

## Summary

This paper experimentally verified the structural benefits of combining non-yielding high-strength FRP reinforcement (aramid Technora rods) with ductile strain-hardening ECC matrices under reversed cyclic flexural loading. Brittle concrete flexural members reinforced with FRP suffer from localized opening of few wide cracks, bond splitting, spalling, and sudden rupture of FRP bars at low drift levels. In contrast, R/ECC flexural members develop distributed multiple microcracks that eliminate interfacial shear stress concentrations, achieving stable hysteretic behavior up to 12~13 % drift with crack widths maintained below 200 µm without requiring shear stirrups.

## Key Contributions

1. **Verification of deformation compatibility in structural members**: Saturated multiple cracking in ECC (crack spacing 0.5~5 mm, crack widths < 200 µm) prevented FRP stress concentrations, bond splitting, and cover spalling. The control R/C specimen (S-1) developed bond splitting cracks at 5 % drift, cover spalling at 6 % drift, and lost stiffness before partial FRP rupture at 7 % drift (9 kN); R/ECC (S-2) experienced no bond splitting, undergoing rotational sliding until FRP rupture at 12 % drift (13 kN).
2. **Demonstration of bond independence**: Specimen S-3 without stirrups and sand-coated specimen S-4 exhibited virtually identical crack spacing (15 mm) and flexural responses. Increasing bond strength via sand coating yielded no performance gain, instead concentrating cracks near the base and promoting earlier sliding planes (S-4 reached 12.5 kN). Provided adequate development length exists, R/ECC cyclic behavior is essentially independent of interfacial bond strength.
3. **Elimination of shear stirrups**: In S-2, all FRP bar ruptures occurred at stirrup intersections due to localized pinching and puncture damage. Because ECC provides continuous intrinsic lateral confinement that prevents bar buckling and ensures ductile compressive behavior, transverse shear stirrups are unneeded when shear demands are satisfied. Unreinforced specimen S-3 achieved optimal capacity (14.3 kN), matching the theoretical prediction of 14.2 kN.
4. **Analytical sectional model**: Derived load-deflection envelopes from nonlinear moment-curvature relations incorporating matrix nonlinear compressive behavior (Hognestad parabola + linear softening), calculating cracked sectional stiffness $EI_{cr}$ as a function of load:
   $$\Delta(L) = \frac{F \cdot l_{cr}^2}{EI_{cr}} \left(\frac{L}{2} - \frac{l_{cr}}{6}\right) + \frac{F \cdot (L - l_{cr})}{EI_{cr}} \left(L - \frac{l_{cr}}{2}\right) + \frac{F \cdot (L - l_{cr})^3}{3 EI_g}$$

## Methods

- Materials: Aramid FRP Technora Rods (Teijin, deformed ribbed) with E = 54 GPa, tensile strength 1800 MPa, tensile strain capacity 3.8 % (compression assumed ~10 % of tension). ECC: PE fibers 1.5 vol%, maximum aggregate size 0.25 mm, first cracking 4.5 MPa @ 0.01 %, ultimate tensile strength 6.0 MPa @ ~3.8 %, fc = 80 MPa @ 0.5 %. Concrete: coarse aggregate 10 mm, fc = 50 MPa @ 0.2 %.
- Specimens: 4 cantilever specimens (100 × 100 mm cross section, height 500 mm). Symmetrical longitudinal reinforcement with 4 Ø6 mm FRP bars (reinforcement ratio 1.13 %). S-1: R/C + stirrups, S-2: R/ECC + stirrups (Ø3 mm @ 25/75 mm, transverse reinforcement ratio 0.57/0.19 %), S-3: R/ECC without stirrups, S-4: R/ECC without stirrups + sand coating. Designed to ensure matrix compressive failure precedes FRP tensile rupture under ultimate compressive strain limits (concrete 0.003, ECC 0.006).
- Loading: 100 kN actuator under displacement control with stepped cyclic drift increments starting from 0.5 %. Surface optical dot image tracking (1520 × 960 px, error ~0.5 mm) capturing deflection profiles and curvature distributions.

## Results

| Specimen | Matrix | Transverse rebar | Coating | Drift / shear force at failure | Observations |
|---|---|---|---|---|---|
| **S-1** | R/C | Present | — | 7 % / 9.0 kN | Crack spacing ~100 mm, width 2 mm, bond splitting & spalling |
| **S-2** | R/ECC | Present | — | 12 % / 13 kN | Crack spacing 40 $\rightarrow$ 20 mm, width 0.2 mm, rotational sliding |
| **S-3** | R/ECC | None | — | **13 % / 14.3 kN** | Uniform crack spacing 15 mm, matches predicted 14.2 kN |
| **S-4** | R/ECC | None | Sand | 13 % / 12.5 kN | Base crack concentration $\rightarrow$ premature sliding plane |

- Curvatures: Distributed smoothly along member height without base localization. Peak curvature at 7 % drift reached 0.00040 1/mm for S-1 (exceeding theoretical 0.00031) and 0.00072 1/mm for S-2 (exceeding predicted 0.00044), indicating in-situ matrix strain capacities exceeded design assumptions.
- Residual deflection ratios: Maintained minimum values of ~0.2 upon crack saturation (at 3 % drift for S-1 and 6 % drift for S-2). S-2 retained a ratio of ~0.2 up to 10 % drift, whereas S-1 increased sharply after 5 % drift due to bond splitting and crushing.
- Model performance: The analytical formulation matched cyclic reload envelopes accurately, with S-3 showing agreement across the entire range.
- Energy dissipation: While ECC exhibited high tensile ductility, total energy dissipation in FRP-ECC members remained moderate compared to steel-reinforced systems because elastic FRP bars recover strain elastically, making crack formation the primary dissipation mechanism.

## Related Notes

- [[fischer-2002-matrix-ductility-tension-stiffening]] — Precursor study establishing deformation compatibility and reduced bond stress demands in uniaxial tension.
- [[gangarao-2007-frp-rc-design-textbook]] — Reference textbook on FRP-reinforced concrete design.
- [[pseudo-strain-hardening-criteria]] — Micromechanical criteria governing ECC multiple cracking (PSH).
- [[bakis-2002-frp-composites-construction-state-of-the-art]] — State of the art on FRP internal reinforcement design.
