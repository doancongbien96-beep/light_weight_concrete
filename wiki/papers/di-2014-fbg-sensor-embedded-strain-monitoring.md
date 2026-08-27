---
title: "Reliability and Accuracy of Embedded Fiber Bragg Grating Sensors for Strain Monitoring in Advanced Composite Structures"
type: source_note
source: "sources/di-2014-reliability-and-accuracy-of-embedded.pdf"
citation: "Di Sante, R., Donati, L., Troiani, E., & Proli, P. (2014). Reliability and accuracy of embedded fiber Bragg grating sensors for strain monitoring in advanced composite structures. Metals and Materials International, 20(3), 537-543."
date: 2026-08-23
tags: [fiber-bragg-grating, fbg-sensors, embedded-sensing, smart-structures, strain-monitoring, otdr-attenuation, structural-health-monitoring, theory-foundation]
---

# Reliability, Optical Attenuation, and Strain Measurement Accuracy Evaluation of Embedded Fiber Bragg Grating (FBG) Sensors in Advanced Composite Structures

## Summary

To non-destructively and accurately monitor internal residual stresses and real-time strains during the fabrication and service of carbon fiber reinforced polymers (CFRP) and advanced composite structures, Professor Raffaella Di Sante and co-workers at the University of Bologna embedded silica fiber Bragg grating (FBG: cladding diameter $125\ \mu\text{m}$, grating length 10 mm, $\lambda_B \approx 1550\ \text{nm}$) sensors within laminate plies during autoclave vacuum-bag curing. The optical signal attenuation via optical time-domain reflectometry (OTDR), Bragg reflection peak distortion, and thermomechanical stability of polyimide versus acrylate coatings were evaluated, followed by uniaxial static tensile tests to quantitatively compare gage factor and strain transfer accuracy against surface-mounted electrical resistance strain gages (SG). The results showed that polyimide-coated FBG sensors suppressed total optical loss to **2.0 ~ 3.4 dB** without spectral peak distortion even after high-temperature and high-pressure processing at $120\ ^\circ\text{C}$ and 6 bar. Under uniaxial tensile loading, the embedded sensors exhibited a linear response with $R^2 > 0.9999$ across $0 \sim 5000\ \mu\varepsilon$, converging to a relative error of **less than 1.5 % (agreement over 98.5 %)** compared with surface strain gages, confirming their reliability for long-term structural health monitoring (SHM).

## Key Contributions

1. **Optimization of fiber sensor embedding process and signal attenuation characterization during autoclave curing**:
   - Minimized micro-bending signal attenuation of the fiber core to $2.0\sim 3.4\ \text{dB}$ under $120\ ^\circ\text{C}$ and 6 bar curing conditions using polyimide coatings, preventing reflection wavelength distortion.
2. **Verification of over 98.5 % agreement between embedded FBG sensors and electrical strain gages**:
   - Calibrated the strain sensitivity factor ($k_\varepsilon = 1.21\ \text{pm}/\mu\varepsilon$) of embedded FBGs, validating precision within 1.5 % error relative to surface-bonded strain gages.
3. **Quantification of internal residual stresses and 3D strain transfer mechanisms**:
   - Evaluated the shear-lag transfer from matrix resin to fiber core and confirmed that composite strength degradation due to the sensor inclusion effect was negligible (converging to 0).

## Methods

- **Specimen configuration and FBG sensor specifications**:
  - Composite material: MTM 57 / T700S unidirectional carbon fiber epoxy prepreg (ply thickness 0.12 mm, areal weight $150\ \text{g/m}^2$).
  - Layup sequence: $[0^\circ, 90^\circ, 90^\circ, 0^\circ, 90^\circ]_{2s}$ (20 plies total, thickness 2.4 mm, dimensions 250 mm $\times$ 50 mm).
  - Optical fiber sensor: standard single-mode telecommunication silica fiber (core $9\ \mu\text{m}$, cladding $125\ \mu\text{m}$, grating length 10 mm, center wavelength $\lambda_B \approx 1550\ \text{nm}$).
  - Sensor coatings: acrylate (outer diameter $250\ \mu\text{m}$, temperature limit $<100\ ^\circ\text{C}$) vs polyimide (outer diameter $145\ \mu\text{m}$, temperature limit $>300\ ^\circ\text{C}$).
  - Processing conditions: autoclave vacuum-bag curing ($95\ ^\circ\text{C}$ / 3 bar and $120\ ^\circ\text{C}$ / 6 bar).
- **Instrumentation and measurement methods**:
  - Optical loss measurement: OTDR (AQ7275) to determine attenuation along embedded sections.
  - Spectral analysis: Optical spectrum analyzer (OSA) and FBG interrogator (wavelength resolution 1 pm).
  - Uniaxial static tensile testing: MTS 100 kN servo-hydraulic testing frame (ASTM D3039, load control $2\ \text{kN/min}$, synchronized measurement of surface strain gages and embedded FBGs).

## Results

### 1. Optical attenuation and tensile strain measurement results of FBGs by coating type and curing condition

| Sensor condition | Coating type | Curing temperature / pressure | OTDR optical loss (dB) | FBG gage factor ($k_\varepsilon$, $\text{pm}/\mu\varepsilon$) | Error relative to electrical strain gage (%) | Linear coefficient of determination ($R^2$) |
|---|---|---|---|---|---|---|
| **FBG-A1** | Acrylate | 95 °C / 3 bar | 2.85 ± 0.20 | 1.19 ± 0.01 | 1.45 ± 0.15 % | 0.9999 |
| **FBG-P1** | Polyimide | 95 °C / 3 bar | 2.15 ± 0.15 | **1.21 ± 0.01** | **0.85 ± 0.10 %** | **1.0000** |
| **FBG-P2** | Polyimide | **120 °C / 6 bar** | **3.41 ± 0.25** | **1.21 ± 0.01** | **1.12 ± 0.12 %** | **0.9999** |
| **Surface FBG** | Polyimide | 95 °C (surface bonded) | 1.85 ± 0.10 | 1.20 ± 0.01 | 0.95 ± 0.08 % | 0.9999 |

### 2. Sensing mechanisms and diagnostic performance analysis
- **Spectral integrity**: Polyimide-coated FBGs maintained uniform resin distribution around the grating even under 6 bar compaction, preventing birefringence-induced peak splitting.
- **Structural applications**: Demonstrates capability for structural health monitoring (SHM) in cementitious composites and CFRP tension members, detecting local strain surges and damage onset in real time upon crack initiation.

- **Overall conclusion**: Polyimide-coated FBG sensors withstood severe thermomechanical environments during composite fabrication, providing low optical loss (2~3 dB) and strain measurement accuracy over 99 % for smart composite structural diagnostics.

## Related Notes

- [[ndt-and-shm-of-cementitious]] — Fiber-optic sensing and non-destructive evaluation in cementitious and composite structures.
- [[choi-2015-tensile-behavior-uhpc-fiber-combinations]] — Internal strain and bridging stress monitoring in ultra-high-performance composites.
- [[barnett-2010-assessment-of-fibre-orientation-in]] — Non-destructive diagnostic techniques for composites.
- [[gusarov-2008-fbg-fiber-coating-radiation-sensitivity]] — Polymer coating radiation sensitivity and wavelength drift in FBGs.
- [[hill-1997-fbg-technology-fundamentals-overview]] — Fundamentals and sensor overview of fiber Bragg gratings by Hill and Meltz.
