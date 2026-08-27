---
title: "매트릭스 연성이 강재 보강 ECC의 인장-stiffening 거동에 미치는 영향 (Fischer & Li, 2002)"
type: source_note
source: "sources/2002-influence-of-matrix-ductility-on.pdf"
citation: "Fischer, G., and Li, V. C. \"Influence of Matrix Ductility on Tension-Stiffening Behavior of Steel Reinforced Engineered Cementitious Composites (ECC).\" ACI Structural Journal, V. 99, No. 1 (2002), pp. 104-111."
date: 2026-08-22
tags: [tension-stiffening, reinforced-ecc, deformation-compatibility, multiple-cracking, bond, steel-reinforcement]
---

# Tension-Stiffening in Steel-Reinforced ECC (R/ECC): Role of Matrix Ductility

## Summary

This paper presents an experimental comparison of the tensile deformation behavior of steel-reinforced concrete (R/C), R/FRC, and R/ECC members under uniaxial tension. Replacing brittle concrete with strain-hardening multiple-cracking ECC allows the rebar and matrix to maintain deformation compatibility in both post-cracking and post-yielding regimes, simultaneously enhancing axial load capacity and ductility without composite degradation such as localized slip, excessive bond stresses, or longitudinal splitting. The central finding is that this performance enhancement stems not from increases in matrix strength or bond strength, but from a fundamental reduction in internal stress demands.

## Key Contributions

1. **Elimination of macroscopic rebar-matrix strain differentials via multiple cracking in R/ECC**: Upon crack formation, R/C suffered sudden load drops (>8 kN) and localized strain jumps (700 $\rightarrow$ 1400 µε), whereas R/ECC limited load drops to <1 kN and localized strain increases to 120~180 µε.
2. **Preservation of matrix contribution beyond rebar yielding**: In Type A specimens, the embedded rebar in R/ECC yielded only at 260 kN (vs 200 kN for bare steel), with ultimate failure occurring by necking and rupture of the protruding bare steel (310 kN). Conversely, R/C yielded concurrently with the bare bar (~200 kN) and failed prematurely by splitting and spalling.
3. **Saturated multiple microcracking in Type B specimens**: The ECC matrix developed ~40 transverse microcracks with an average spacing of 10 mm and crack widths of ~200 µm, avoiding tension-softening localization up to 4 % composite strain at a peak load of 175 kN. The matrix delayed rebar yielding, distributing yielding across 2000~2700 µε.
4. **Governing role of fiber bridging over bond properties**: Crack spacing in R/ECC is dictated by intrinsic ECC material properties (fiber bridging) rather than rebar-matrix interfacial bond characteristics, establishing a qualitative departure from R/C mechanics.

## Methods

- ECC matrix: PE fibers 1.5 vol%, cement, fine aggregate (mean size 0.3 mm), water, superplasticizer. Cracking strength 4.5 MPa @ 0.01 % strain, ultimate tensile strength 6.5 MPa @ ~4 % strain, compressive strength 80 MPa.
- Concrete: Coarse aggregate 10 mm, fc = 50 MPa. Tensile cracking strength 4 MPa @ 0.01 % assumed.
- Steel rebar: Yield strength 420 MPa @ ~0.2 % strain.
- Type A specimens: 175 × 175 × 500 mm with central notch ($a = 25$ mm) to fix initial crack location, D25 rebar ($\rho \approx$ 1.5 %). Internally strain-gaged split rebar (15 mm spacing near crack, 40 mm spacing elsewhere).
- Type B specimens: 120 × 120 × 500 mm, D19 rebar ($\rho \approx$ 1.8 %), strain gages along half length at 25 mm spacing to observe multiple cracking and post-yield behavior.
- Instrumentation: Dual LVDTs attached to rebar to measure member elongation under displacement control at 0.01 mm/s. Two concrete + two ECC specimens per type (8 specimens total), tested at 28~35 days.
- Classification framework: Naaman & Reinhardt (1995) HPFRCC definition (ultimate strength > cracking strength + multiple cracking) and pseudo-strain concepts.

## Results

| Parameter | R/C | R/ECC |
|---|---|---|
| First transverse crack load (Type A) | 112 kN | 104 kN |
| Elongation jump at cracking | 700 µε | 100 µε |
| Load drop at cracking | > 8 kN | < 1 kN |
| Embedded rebar yield load (Type A) | ~200 kN (same as bare bar) | 260 kN |
| Failure mode | Disintegration via splitting/spalling | Bare steel necking/fracture (310 kN) |
| Type B first crack / yield | 65 kN / ~100 kN | Pre-existing shrinkage cracks / embedded delayed yield after bare yield at 112 kN |
| Type B peak response | Premature termination (spalling) | 175 kN @ 4 % mean strain |

- Mechanistic interpretation: Prior to cracking, both matrices share load proportionally to stiffness. After cracking in R/C, load transfer occurs solely through interfacial bond, driving stress concentrations, slip, Goto cone cracking, and longitudinal splitting. In R/ECC, fiber bridging transfers crack-plane stresses back into the uncracked matrix, rendering macroscopic bond stresses unnecessary while activating only local bond required for crack opening.
- Energy absorption: Since both components (ECC matrix + steel rebar) exhibit strain hardening, deformation localization is prevented, significantly enhancing energy absorption across large inelastic deformation regimes for seismic applications.
- Conclusion: The superior performance of R/ECC derives not from increases in matrix tensile strength, confinement, or bond strength, but from the fundamental reduction of internal stress demands that require such resistance.

## Related Notes

- [[pseudo-strain-hardening-criteria]] — Micromechanical basis for HPFRCC classification and ECC multiple cracking (PSH).
- [[fiber-bridging-constitutive-law]] — Quantitative constitutive models for crack-plane stress transfer.
- [[fischer-2003-frp-reinforced-ecc-cyclic-flexure]] — Extension of deformation compatibility mechanisms to FRP reinforcement and cyclic flexure.
- [[li-2023-ecc-micromechanics-critical-review]] — Structural applications and rebar-composite interaction in ECC micromechanics.
