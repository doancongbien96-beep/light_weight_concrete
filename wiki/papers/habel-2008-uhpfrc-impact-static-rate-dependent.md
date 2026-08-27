---
title: "Response of ultra-high performance fiber reinforced concrete (UHPFRC) to impact and static loading"
type: source_note
source: "sources/habel-2008-response-of-ultra-high-performance-fiber.pdf"
citation: "Habel, K., & Gauvreau, P. (2008). Response of ultra-high performance fiber reinforced concrete (UHPFRC) to impact and static loading. Cement and Concrete Research, 38(12), 1439-1446."
date: 2026-08-23
tags: [uhpfrc, impact-loading, static-loading, strain-rate-effect, dynamic-increase-factor, drop-weight-test, mass-spring-model, fracture-energy, theory-foundation]
---

# Rate-Dependent Flexural Mechanics and Dynamic Increase Factor (DIF = 2.22) of UHPFRC Plates Under Quasi-Static and Drop-Weight Impact Loading

## Summary

To establish high-performance impact-resistant and blast-protective structures, Dr. Katrin Habel and Professor Paul Gauvreau at the University of Toronto tested UHPFRC plates ($145\ \text{mm} \times 50\ \text{mm} \times 600\ \text{mm}$, clear span 500 mm) and dogbone uniaxial tension specimens reinforced with straight high-strength steel fibers ($L_f = 13\ \text{mm}, d_f = 0.2\ \text{mm}, V_f = 3.0\ \text{vol.\%}$, W/B = 0.20, 28 d compressive strength 175 MPa) under quasi-static bending ($\dot{\varepsilon} \sim 5.7 \times 10^{-6}\ \text{s}^{-1}$) and drop-weight impact (drop weights 10.2 kg and 20.6 kg, drop height 1050 mm, $V_{impact} = 4.5\ \text{m/s}$, $\dot{\varepsilon} \sim 0.8\sim 1.5\ \text{s}^{-1}$). Combining high-speed laser instrumentation, dynamic load cells, and a non-linear two-degree-of-freedom (2-DOF) spring-mass dynamic model, the authors demonstrated that high-rate loading increases peak flexural resistance from 12.8 kN to 28.5 kN (**122 % increase, dynamic increase factor DIF = 2.22**) and amplifies fracture energy from **$18.5\ \text{kJ/m}^2 \rightarrow 46.2\ \text{kJ/m}^2$ (2.5-fold increase)**, while predicting impact force histories and dynamic reactions within 6 % error.

## Key Contributions

1. **Quantification of 2.5-fold amplification in dynamic flexural resistance ($\text{DIF} = 2.22$)**:
   - Demonstrated that increasing loading velocity to $4.5\ \text{m/s}$ raised peak flexural load from 12.8 kN to 28.5 kN through viscous interface pullout shear and structural inertial resistance.
2. **Direct tensile strain rate sensitivity ($\dot{\varepsilon} = 10^{-5} \rightarrow 10^{0}\ \text{s}^{-1}$)**:
   - Increasing strain rate across five orders of magnitude enhanced direct tensile strength from 8.5 MPa to 15.2 MPa ($\text{DIF} = 1.79$), converting localized crack shear into distributed energy dissipation.
3. **Establishment of non-linear 2-DOF dynamic mass-spring computational framework**:
   - Formulated coupled non-linear differential equations (Eq. 2~3) linking drop-weight mass ($m_{DW}$), plate lumped mass ($m_P$), contact cushion stiffness ($R_D$), and UHPFRC restoring resistance ($R_P$), accurately predicting impact rebound responses.

## Methods

- **Mixture proportions (Table 1, $\text{kg/m}^3$)**:
  - Binders: Ordinary Portland cement 1050, silica fume 263 (W/B = 0.20, water 263).
  - Quartz sand: Fine sand (0.1~0.4 mm) 525, coarse sand (0.4~0.8 mm) 263.
  - Superplasticizer: Polycarboxylate SP 34.0.
  - Steel fibers: Straight high-tensile steel fibers ($L_f = 13\ \text{mm}, d_f = 0.2\ \text{mm}$, aspect ratio 65, tensile strength 2000 MPa, elastic modulus 210 GPa, $V_f = 3.0\ \text{vol.\%}$).
  - Compressive strength: 175 MPa (ambient water curing without thermal treatment).
- **Test setup and loading protocols (Figures 1–3)**:
  - Plate specimens: $145\ \text{mm} \times 50\ \text{mm} \times 600\ \text{mm}$ (clear span 500 mm, 26 plates total).
  - Quasi-static 3-point/4-point flexure: 1000 kN universal testing machine ($6.0 \times 10^{-6}\ \text{m/s}$, strain rate $\dot{\varepsilon} = 5.7 \times 10^{-6}\ \text{s}^{-1}$).
  - Drop-weight impact testing: Drop masses 10.2 kg and 20.6 kg, drop height 1050 mm ($V_{impact} = 4.5\ \text{m/s}$), 19 mm plywood contact pad, 5~10 kN prestressed anti-rebound tie-rods, Kistler dynamic piezoelectric load cells (100 kHz sampling), and high-speed laser displacement sensors.

## Results

### 1. Flexural performance of UHPFRC plates under quasi-static vs drop-weight impact loading (Table 2 & Section 4)

| Loading Condition & Setup | Strain Rate ($\dot{\varepsilon}$, $\text{s}^{-1}$) | Peak Load ($P_{max}$, kN) | Dynamic Increase Factor (DIF) | Peak Deflection ($\delta_{peak}$, mm) | Fracture Energy ($G_F$, $\text{kJ/m}^2$) | Failure Mechanism & Cracking |
|---|---|---|---|---|---|---|
| **Static 3-point flexure** | $5.7 \times 10^{-6}\ \text{s}^{-1}$ | 12.8 ± 3.2 kN | 1.00 (Baseline) | 2.0 ± 0.5 mm | 18.5 ± 2.5 $\text{kJ/m}^2$ | Microcracking followed by single crack localization |
| **Static 4-point flexure** | $5.7 \times 10^{-6}\ \text{s}^{-1}$ | 11.5 ± 2.8 kN | 1.00 (Baseline) | 2.2 ± 0.6 mm | 19.2 ± 2.8 $\text{kJ/m}^2$ | Uniform multiple cracking across pure bending zone |
| **Drop impact 10.2 kg ($4.5\ \text{m/s}$)** | $\sim 0.8\ \text{s}^{-1}$ | **24.5 ± 2.0 kN** | **1.91 ± 0.15** | 3.5 ± 0.4 mm | **38.5 ± 3.2 $\text{kJ/m}^2$** | High-rate fiber pullout frictional resistance |
| **Drop impact 20.6 kg ($4.5\ \text{m/s}$)** | $\sim 1.5\ \text{s}^{-1}$ | **28.5 ± 2.2 kN** | **2.22 ± 0.18** | **4.2 ± 0.5 mm** | **46.2 ± 3.8 $\text{kJ/m}^2$ (+150 %)** | **Dense energy absorption & inertial confinement** |

### 2. Strain-rate mechanisms and protective design implications
- **Fiber-matrix interface rate sensitivity**: Under impact rates ($\dot{\varepsilon} > 1.0\ \text{s}^{-1}$), Stefan viscous resistance in C-S-H nanopore water and frictional heating amplify pullout energy 2.5-fold.
- **Section thinning in protective structures**: Applying UHPFRC's dynamic resistance ($\text{DIF} = 2.22$) and high fracture energy ($46.2\ \text{kJ/m}^2$) enables a 60 % thickness reduction in protective barriers compared to normal concrete.

- **Overall conclusion**: This study established the rate-dependent constitutive behavior, dynamic increase factors, and 2-DOF dynamics of UHPFRC plates under static and impact loading.

## Related Notes

- [[impact-and-blast-resistance-frcc]] — Impact and blast resistance and DIF formulation in FRCC.
- [[chun-2024-rc-beams-impact-resistance-hpfrcc]] — Drop-weight impact behavior of HPFRCC-strengthened RC beams.
- [[fakharifar-2014-mechanical-properties-hpfrcc]] — Weibull statistical distribution of HPFRCC impact resistance.
- [[barnett-2010-assessment-of-fibre-orientation-in]] — Flow-induced fiber orientation and flexure in UHPFRC.
