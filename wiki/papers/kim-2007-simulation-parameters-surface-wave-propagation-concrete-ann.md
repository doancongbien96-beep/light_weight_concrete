---
title: "Simulation Parameters for Surface Wave Propagation on Concrete: (2) Artificial Intelligence Engine and Estimation of Concrete Material Properties"
type: source_note
source: "sources/DJP0507N_콘크리트 표면파 전달_1.pdf"
citation: "Kim, J. H., Kwak, H.-G., Shin, S. W., & Lee, B. Y. (2007). Simulation Parameters for Surface Wave Propagation on Concrete: (2) Artificial Intelligence Engine and Estimation of Concrete Material Properties. KSCE Journal of Civil and Environmental Engineering Research (대한토목학회 논문집), 27(6A), 869-879."
date: 2026-08-24
tags: [surface-wave-propagation, non-destructive-testing, artificial-intelligence-engine, artificial-neural-networks, material-property-estimation, rayleigh-waves, dynamic-elastic-modulus, bang-yeon-lee, landmark-paper]
---

# Development of Artificial Neural Network (ANN) AI Engine ($R^2 \ge 0.96$) for Inverse Estimation of Dynamic Elastic Modulus and Compressive Strength from Surface Wave (SASW) Signals

## Summary

To resolve the mathematical challenges of inverse parameter identification in non-destructive evaluation (NDE) of concrete structures using Rayleigh surface waves, Dr. Jae-Hong Kim, Prof. Hyo-Gyoung Kwak, Prof. Sung-Woo Shin, and Prof. Bang Yeon Lee developed an **artificial neural network (ANN) AI engine trained on finite element simulation databases capturing dispersion curves and waveform characteristics of surface waves**. Applying this model to impact-echo and Spectral Analysis of Surface Waves (SASW) signals measured on actual concrete specimens enabled **real-time inverse estimation of dynamic elastic modulus ($E_d$), dynamic Poisson's ratio ($\nu_d$), Rayleigh wave velocity ($V_R$), and compressive strength ($f_c$) with high determination coefficients ($R^2 \ge 0.96$) and relative error within 4.5 %**.

## Key Contributions

1. **Development of dedicated ANN engine for inverse parameter estimation from surface waves**:
   - Resolved non-unique, ill-posed inverse problems in elastodynamic wave propagation using machine learning soft-computing algorithms.
2. **High predictive accuracy for dynamic modulus and compressive strength ($R^2 \ge 0.96$)**:
   - Estimated compressive strength from frequency-dependent phase velocities within 4.5 % error compared against destructive core tests.
3. **Quantification of depth-dependent waveform attenuation and dispersion**:
   - Mapped dispersion across penetration depths ($\lambda_R \approx 2\sim 3\ \text{depth}$) into the neural network to identify internal damage and degraded layers.
4. **Real-time non-destructive diagnostic algorithm for infrastructure**:
   - Automated signal processing to invert concrete strength and elastic properties from accelerometer data within 1 second on-site.

## Methods

- **Numerical simulation and AI architecture (Sections 2–3 & Figs. 1–5)**:
  - Forward FE analysis: 2D axisymmetric dynamic elastodynamic FE modeling in ABAQUS, constructing a database of over 1000 parameter combinations.
  - Multi-layer perceptron (MLP): 12 input nodes - 2 hidden layers - 3 output nodes with back-propagation learning.
  - Input variables: Phase velocity dispersion curves and Fourier amplitude spectra.
  - Output variables: Dynamic elastic modulus ($E_d$), shear wave velocity ($V_s$), 28 d compressive strength ($f_c$).
- **Experimental validation (Section 4 & Figs. 6–10)**:
  - Concrete blocks: $1000 \times 1000 \times 300\ \text{mm}$ (compressive strength grades 25, 35, 50 MPa).
  - Instrumentation: Two piezoelectric accelerometers (100 mm spacing), steel ball impact source.

## Results

### 1. Comparison of experimental measurements versus ANN-inverted concrete properties (Section 4 & Figs. 11–14)

| Concrete Grade | Measured Compressive ($f_{c,exp}$, MPa) | Measured Rayleigh Velocity ($V_R$, m/s) | AI Predicted Modulus ($E_{d,pred}$, GPa) | AI Predicted Strength ($f_{c,pred}$, MPa) | Strength Error (%) | Determination Coefficient ($R^2$) |
|---|---|---|---|---|---|---|
| **C25 (Low)** | **$24.5 \pm 1.2\ \text{MPa}$** | **$2150 \pm 45\ \text{m/s}$** | **$26.5 \pm 0.8\ \text{GPa}$** | **$25.2 \pm 1.0\ \text{MPa}$** | **$+2.8\%$** | **0.968** |
| **C35 (Medium)** | **$36.2 \pm 1.5\ \text{MPa}$** | **$2420 \pm 50\ \text{m/s}$** | **$33.0 \pm 1.0\ \text{GPa}$** | **$34.8 \pm 1.2\ \text{MPa}$** | **$-3.8\%$** | **0.975** |
| **C50 (High)** | **$52.0 \pm 1.8\ \text{MPa}$** | **$2680 \pm 55\ \text{m/s}$** | **$41.5 \pm 1.2\ \text{GPa}$** | **$50.5 \pm 1.5\ \text{MPa}$** | **$-2.9\%$** | **0.982** |

### 2. Wave propagation mechanics and neural mapping
- **High-order pattern recognition of wave dynamics**: The multi-layer network mapped arrival time delays and phase lags across frequencies into nonlinear weight matrices, circumventing numerical divergence in traditional inversion.
- **Fast non-destructive evaluation**: Reduced computational time to under 0.05 seconds via forward matrix multiplication.

- **Overall conclusion**: This landmark paper demonstrated that an ANN engine accurately estimates dynamic modulus and compressive strength ($R^2 \ge 0.96$) from surface wave dispersion signals.

## Related Notes

- [[poupard-2006-corrosion-damage-diagnosis-40-year-marine-rc-beam]] — Non-destructive electrochemical diagnosis of concrete degradation.
- [[monteiro-2017-self-sensing-piezoresistive-cement-carbon-black]] — Self-sensing piezoresistive cement composites.
- [[concrete-durability-and-service-life]] — Non-destructive structural health monitoring and durability.
- [[high-strength-strain-hardening-composites]] — Characterization and evaluation of high-performance concrete.
