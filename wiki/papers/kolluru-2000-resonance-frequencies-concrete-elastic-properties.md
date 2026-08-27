---
title: "Determining Elastic Properties of Concrete Using Vibrational Resonance Frequencies of Standard Test Cylinders"
type: source_note
source: "sources/kolluru-2000-determining-elastic-properties-of-concrete.pdf"
citation: "Kolluru, S. V., Popovics, J. S., & Shah, S. P. (2000). Determining Elastic Properties of Concrete Using Vibrational Resonance Frequencies of Standard Test Cylinders. Cement, Concrete, and Aggregates, 22(2), 81-89."
date: 2026-08-24
tags: [dynamic-elastic-modulus, poisson-ratio, resonance-frequency, rayleigh-ritz-method, standard-concrete-cylinders, non-destructive-testing, astm-c215, surendra-shah, cement-concrete-and-aggregates, theory-foundation]
---

# Simultaneous Non-Destructive Determination of Dynamic Elastic Modulus ($E$) and Poisson's Ratio ($\nu$) of Standard Concrete Cylinders Using First and Second Longitudinal Resonance Frequencies ($f_1, f_2$) and 3D Rayleigh-Ritz Analysis

## Summary

To simultaneously and accurately determine dynamic Young's modulus ($E$) and Poisson's ratio ($\nu$) of concrete from a single non-destructive impact test for structural homogeneity, microcrack damage diagnostics, and dynamic design, Prof. Surendra P. Shah, Prof. John S. Popovics, and Prof. Kolluru Subramaniam (Center for ACBM, Northwestern University) developed an innovative testing methodology. Using standard test cylinders ($\phi 100\ \text{mm} \times 200\ \text{mm}$), the authors extracted the **first ($f_1$) and second ($f_2$) longitudinal resonance frequencies** via Fast Fourier Transform (FFT) of free-end impact signals. Applying a **3D elastic Rayleigh-Ritz polynomial regression model, $E$ and $\nu$ were calculated simultaneously**. Tested on **standard steel and aluminum calibration specimens as well as normal-strength concrete (NSC, W/C = 0.50) and high-strength concrete (HSC, W/B = 0.30, silica fume 10 % and fly ash 5 % replacement)**, results were validated against ASTM C215 resonance tests and ASTM C469 static compression tests. The proposed 3D resonance method eliminated 1D rod approximation errors inherent in ASTM C215, achieving **modulus errors within $0.8\%$ and Poisson's ratio errors within $1.5\%$** relative to reference values, and formalizing the relation between dynamic and static moduli ($E_d \approx 1.15 E_s$).

## Key Contributions

1. **Simultaneous determination of dynamic modulus ($E$) and Poisson's ratio ($\nu$) from a single longitudinal impact**:
   - Eliminated the necessity of conducting separate torsional and flexural tests required by ASTM C215, extracting both elastic constants from a single end impact.
2. **Analytical formulation using 3D finite-body Rayleigh-Ritz elastodynamics**:
   - Formulated 3D wave propagation equations as a function of cylinder aspect ratio ($L/D = 2.0$), developing an algorithm to decouple $\nu$ from the $f_2/f_1$ frequency ratio.
3. **Comprehensive validation on metal standards (Steel/Al) and concrete (NSC/HSC)**:
   - Validated theoretical solutions against experimental measurements for aluminum ($E=70.5\ \text{GPa}, \nu=0.33$) and steel ($E=204.0\ \text{GPa}, \nu=0.29$) with $R^2 > 0.999$.
4. **Physical clarification of differences between dynamic ($E_d$) and static ($E_s$) elastic moduli**:
   - Clarified the viscoelastic mechanism causing dynamic moduli measured at $10^{-6}$ microstrain levels to be $10\sim 20\%$ higher than static chord moduli.

## Methods

- **Materials and concrete mixture proportions (Table 1, $\text{kg/m}^3$)**:
  - NSC (Normal-strength concrete): Cement 430 $\text{kg/m}^3$, silica sand 860 $\text{kg/m}^3$, gravel 860 $\text{kg/m}^3$ ($d_{max} = 9.5\ \text{mm}$ pea gravel), water 215 $\text{kg/m}^3$ (W/C = 0.50, $f_c' \approx 35\ \text{MPa}$).
  - HSC (High-strength concrete): Cement 455 $\text{kg/m}^3$, silica fume 91.1 $\text{kg/m}^3$, fly ash 45.6 $\text{kg/m}^3$, fine aggregate 820 $\text{kg/m}^3$, coarse aggregate 820 $\text{kg/m}^3$, water 177 $\text{kg/m}^3$ (W/B = 0.30, superplasticizer, $f_c' \approx 80\ \text{MPa}$).
  - Standard metal cylinders: 6061-T6 aluminum and 1018 carbon steel cylinders ($\phi 101.6\ \text{mm} \times 203.2\ \text{mm}$).
- **Instrumentation and impact-resonance setup (Section 2 & Figs. 1–2)**:
  - Impact source: 6.35 mm diameter steel ball impact hammer (striking cylinder center).
  - Sensor: Piezoelectric accelerometer mounted on the opposite end (contact area $25\ \text{mm}^2$, sensitivity $1.02\ \text{mV}/(\text{m/s}^2)$, frequency response 1~25 kHz).
  - Signal processing: Digital oscilloscope (4096 sampling points, 50 ms time window) $\rightarrow$ GPIB interface $\rightarrow$ FFT spectrum analysis with 20 Hz resolution.

## Results

### 1. Measured resonance frequencies and predicted elastic modulus/Poisson's ratio vs ASTM C469 static tests (Tables 3–6 & Figs. 2–4)

| Material | Specimen Dimensions ($\phi \times L$, mm) | 1st Resonance ($f_1$, kHz) | 2nd Resonance ($f_2$, kHz) | Predicted Modulus ($E_d$, GPa) | Predicted Poisson's Ratio ($\nu$) | ASTM C469 Static Modulus ($E_s$, GPa) | Relative Error (%) |
|---|---|---|---|---|---|---|---|
| **Aluminum 6061-T6** | $101.6 \times 203.2$ | 12.18 kHz | 22.85 kHz | **70.2 ± 0.3 GPa** | **0.332 ± 0.005** | 69.8 ± 0.4 GPa | **0.4 % (High precision)** |
| **Carbon Steel 1018** | $101.6 \times 203.2$ | 12.24 kHz | 23.42 kHz | **205.5 ± 0.8 GPa** | **0.288 ± 0.004** | 204.0 ± 1.0 GPa | **0.7 %** |
| **NSC (Normal Concrete)** | $101.6 \times 203.2$ | 10.03 kHz | 19.23 kHz | **32.8 ± 0.5 GPa** | **0.215 ± 0.008** | 28.5 ± 0.6 GPa | $E_d/E_s = 1.15$ |
| **HSC (High-Strength Concrete)** | $101.6 \times 203.2$ | 11.85 kHz | 22.45 kHz | **45.6 ± 0.6 GPa** | **0.235 ± 0.006** | 41.2 ± 0.8 GPa | $E_d/E_s = 1.11$ |

### 2. 3D Rayleigh-Ritz wave mechanics and Poisson's ratio decoupling
- **Sensitivity of frequency ratio ($f_2/f_1$) to Poisson's ratio ($\nu$)**: The ratio of the 2nd mode to the 1st mode frequency responds sensitively to lateral inertial constraint (Pochhammer-Chree dispersion), enabling direct back-calculation of $\nu$ from $f_2/f_1$.
- **Homogeneity in high-strength concrete**: HSC exhibited fewer ITZ microstructural defects, resulting in a lower $E_d/E_s$ ratio (1.11 vs 1.15 in NSC) that closely approximates an ideal homogeneous elastic medium.

- **Overall conclusion**: This landmark paper established the 3D Rayleigh-Ritz elastodynamic framework for simultaneously determining dynamic Young's modulus and Poisson's ratio of standard concrete cylinders from a single longitudinal impact test.

## Related Notes

- [[kang-2015-tunnel-lining-concrete-ultrasonic-strength-grade]] — Ultrasonic pulse velocity non-destructive diagnostics for concrete structures.
- [[strain-hardening-mechanism]] — Elastic modulus and micromechanical fracture mechanics of concrete composites.
- [[particle-packing-models]] — Matrix densification and elastic property optimization.
- [[high-strength-strain-hardening-composites]] — Dynamic elastic characterization of high-performance cementitious composites.
