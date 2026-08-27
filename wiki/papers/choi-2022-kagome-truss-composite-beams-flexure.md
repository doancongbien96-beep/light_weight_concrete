---
title: "Flexural behavior of composite beams of Kagome truss and fiber-reinforced cementitious composites"
type: source_note
source: "sources/choi-2022-flexural-behavior-of-composite-beams.pdf"
citation: "Choi, J.-I., Park, S.-E., Kim, Y. Y., & Lee, B. Y. (2022). Flexural behavior of composite beams of Kagome truss and fiber-reinforced cementitious composites. Construction and Building Materials, 361, 129653."
date: 2026-08-23
tags: [kagome-truss, cellular-metal, composite-beam, hd-frcc, hs-frcc, layered-section-analysis, flexural-ductility, user-group]
---

# Flexural behavior and nonlinear analysis of lightweight composite beams fusing Kagome periodic metal trusses with functional FRCC

## Summary

A study (corresponding author Bang Yeon Lee, Chonnam National University; with Se-Eun Park and
Yoon-Yong Kim of Chungnam National University) that fabricated three composite beams — wire-
woven Kagome truss cores, an ultralight porous periodic metal structure, geometrically fused
with two high-functionality FRCCs: ultra-ductile HD-FRCC (**6.33 %** tensile elongation) and
ultra-high-strength HS-FRCC (**156.8 MPa** compression) — as K-HD, K-HS, and K-HS-HD, then ran
third-point flexure tests plus nonlinear layered-section numerical analysis based on strain-
compatibility conditions. The hybrid beam K-HS-HD, placing 20 mm HS-FRCC in the compression zone
and 20 mm HD-FRCC in tension, raised maximum flexural load to **16.72 kN — 4.9x** the single-
layer beams (K-HD 3.40 kN, K-HS 3.72 kN) — and stiffness to **8.99 kN/mm, 20.4x**. The 3D Kagome
lattice embedded deeply into both cement layers formed powerful mechanical interlocking:
no interface shear delamination even beyond 75 mm deflection, producing the ideal ductile mode
of tensile-zone fine multiple cracking combined with truss yielding.

## Key Contributions

1. **Maximized flexural performance of the HS-top / HD-bottom hybrid layout (K-HS-HD)** proven:
   casting 157 MPa HS-FRCC in compression prevented extreme-fiber crushing while 6.33 % HD-FRCC
   in tension suppressed crack localization; capacity rose 4.9x (16.72 vs 3.40 kN) and stiffness
   20.4x (8.99 vs 0.44 kN/mm).
2. **Full composite action at the Kagome-FRCC interface demonstrated**: a 3D porous truss woven
   from stainless steel wire (STS 304, yield 620 MPa) continuously interlocks with the FRCC
   matrix — delamination of 0 % to ultimate load without shear studs or adhesives.
3. **Nonlinear layered-section model built and verified**: combining HD-FRCC hardening tension,
   HS-FRCC elastoplastic compression, and nonlinear Kagome truss axial laws predicted moment-
   curvature and load-deflection curves at high fidelity.

## Methods

- **Kagome truss spec**: STS 304 wire, diameter 1.2 mm, yield 620 MPa, tensile 745 MPa,
  E 193 GPa, density $7.9\ \text{g/cm}^3$. Truss: length 1400 mm, width 300 mm, depth 100 mm
  (periodic triangular/hexagonal cells).
- **FRCC mixes (Table 1)**:
  - **HD-FRCC**: AAS binder 1.0, W/B 0.30, silica sand 0.50, PE fiber 1.75 vol.% (12 µm,
    18 mm, 2700 MPa, E 88 GPa).
  - **HS-FRCC**: cement 0.8 + SF 0.2 (binder 1.0), W/B 0.19, filler 0.24, sand 0.88, expansive
    agent 0.075, steel fiber 1.50 vol.% (200 µm, 19.5 mm, 2500 MPa, E 200 GPa).
- **Composite beam configurations (Table 4)**:
  - **K-HD**: 30 mm HD-FRCC cast below the truss only.
  - **K-HS**: 30 mm HS-FRCC cast below the truss only.
  - **K-HS-HD**: 20 mm HS-FRCC above + 20 mm HD-FRCC below the truss.
- **Test setup**: clear span 1200 mm third-point loading (400 mm spacing), 200 kN actuator at
  1.0 mm/min; two LVDTs at midspan; precise measurement of soffit crack widths and counts.

## Results

### 1. FRCC material performance and cracking (Tables 2 & 3)

| Composite | Compression (MPa) | First cracking (MPa) | Max tension (MPa) | Strain capacity (%) | Cracks in gauge | Mean spacing (mm) | Mean width (µm) |
|---|---|---|---|---|---|---|---|
| **HD-FRCC** | 45.2 ± 0.38 | 4.80 ± 0.30 | 8.38 ± 0.29 | **6.33 ± 0.19 %** | **130.5 ± 1.8** | **0.61 mm** | 38.8 µm |
| **HS-FRCC** | **156.8 ± 4.22** | **10.78 ± 0.68** | **18.11 ± 1.13** | 0.49 ± 0.08 % | 12.5 ± 1.9 | 6.56 mm | 32.2 µm |

### 2. Composite beam bending results (Table 4)

| Beam | Layering | Stiffness at 50 % load (kN/mm) | Max load (kN) | Load ratio | Final failure mode |
|---|---|---|---|---|---|
| **K-HD** | bottom HD 30 mm | 0.44 | 3.40 kN | 1.00 (baseline) | top truss buckling + bottom multiple cracking |
| **K-HS** | bottom HS 30 mm | 1.29 | 3.72 kN | 1.09 | top buckling + bottom crack localization |
| **K-HS-HD** | **top HS 20 + bottom HD 20 mm** | **8.99 (20.4x)** | **16.72 (4.9x)** | **4.92** | **truss yielding + fully integrated ductile failure** |

### 3. Numerical model verification (Table 5)

### 3. Numerical model verification (Table 5)

| Beam | Stiffness at 50 % (kN/mm) [test / model] | Load at 30 mm (kN) [test / model] | Load at 70 mm (kN) [test / model] |
|---|---|---|---|
| **K-HD** | 0.44 / 0.50 | 2.92 / 3.12 | 3.29 / 3.49 |
| **K-HS** | 1.29 / 1.25 | 2.97 / 8.01 (early failure) | – / – |
| **K-HS-HD** | **8.99 / 13.07** | **16.03 / 18.65** | **16.15 / 23.55** |

- **Overall conclusion**: fusing an ultralight periodic Kagome truss with high-strength
  (compression) and high-ductility (tension) FRCCs minimizes self-weight while delivering
  amplified flexural capacity and ductile energy dissipation beyond ordinary RC structures.

## Related Notes

- [[ijp6321-kagome-truss-impact]] — high-velocity impact resistance of Kagome truss composite
  panels (Lee group).
- [[choi-2016-ultra-high-ductile-aas-pe-composite]] — origin of the ultra-ductile HD-FRCC matrix.
- [[choi-2017-uhpm-pe-fiber-tensile-cracking]] — origin of the 150 MPa HS-FRCC matrix.
- [[mai-2025-high-strength-steel-ecc-composite-beam-flexure]] — composite behavior of
  high-strength steel girders with ECC decks.
- [[uhpc-vs-ecc-design-space]] — complementary design space of ultra-high strength and ductility.
- [[multiple-cracking-behavior]] — saturated multiple cracking at 0.61 mm tensile-face spacing.
