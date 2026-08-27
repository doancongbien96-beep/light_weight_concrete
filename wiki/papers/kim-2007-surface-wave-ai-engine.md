---
title: "Simulation Parameters for Surface Wave Propagation on Concrete: (2) AI Engine and Estimation of Concrete Material Properties (Kim, Kwak, Shin & Lee, 2007)"
type: source_note
source: "sources/DJP0507N_콘크리트 표면파 전달.pdf"
citation: "김재홍, 곽효경, 신성우, 이방연. 콘크리트 표면파 전달의 시뮬레이션을 위한 매개변수 결정: (2) 인공 엔진 및 재료상수의 추정. 대한토목학회 논문집 27(6A) (2007) 869-879."
date: 2026-08-22
tags: [ndt, surface-wave, artificial-neural-network, genetic-algorithm, inverse-analysis, wavelet, korean-paper]
---

# Determination of Simulation Parameters for Concrete Surface Wave Propagation: AI Engine and Material Property Estimation

## Summary

This paper establishes an artificial intelligence engine to inversely identify concrete material properties from impact-generated surface acoustic waves (KAIST Prof. Hyo-Gyoung Kwak's group, collaborative research with Bang Yeon Lee). The NDE framework combines a FE database with ANN and genetic algorithms (GA) to estimate dynamic elastic modulus, damping, and compressive strength.

## Key Contributions

1. **FE+ANN hybrid inverse analysis framework**: Utilized a FE simulation database via Monte Carlo sampling (2,000 records × 16 attributes) as training data, avoiding experimental measurement noise.
2. **Principal Wavelet Component Analysis (PWCA)**: Applied continuous wavelet transforms (gaus1) to extract arrival time ($u_1$) and scale ($s_1$) of the primary energy peak, bypassing sensor ring-down issues.
3. **Statistical input parameter screening ($t$-test $p$-values)**: Identified significant correlations for output $V_1$ with 5 factors ($t_c$, $\rho$, $E$, $\eta_1$, $\eta_2$), $SA$ with ($t_c$, $E$, $\eta_2$), and $SB$ with ($t_c$, $\rho$, $E$, $\eta_2$). Confirmed low sensitivity for density $\rho$ and Poisson's ratio $\nu$.
4. **Quantification of inverse solvability limits**: Inversion succeeded for contact duration (99 % $R^2$), elastic modulus (95 % $R^2$), and stiffness damping (96 % $R^2$), whereas density (45 % $R^2$) and Poisson's ratio (34 % $R^2$) exhibited non-unique mapping requiring GA optimization.
5. **Verification of dynamic vs static modulus relations**: The inverted dynamic modulus matched empirical relations ($E_c = 0.83 E_d$, etc.). High repeatability was verified across low/medium/high strength concrete grades (L/M/H, $f_c$ = 19.9/32.0/53.0 MPa) tested in triplicate via pneumatic air-gun excitation.

## Methods

- Prisms ($40 \times 40 \times 15\ \text{cm}$, 40×40×15 cm) and 7 cylinders per grade.
- Instrumentation: 2-channel accelerometers (PCB 353B15, $l = d = 5\ \text{cm}$, 5 cm), air-shot gun impact source.
- Data processing: Continuous wavelet transform ($dt = 1\times 10^{-7}\ \text{s}$, dt=1e-7), Levenberg-Marquardt MLP (9/5/5 hidden nodes), 10-fold cross-validation, GA optimization.

## Results

- Surface wave velocity $V_1$: L = 2000~2024 m/s, M = ~2262-2283 m/s, H = 2451~2500 m/s.
- ANN-inverted modulus $E$: L = 26.6~28.6 GPa, M = ~32-33.6 GPa, H = 39.9~43.2 GPa (matching static values of 24.4/31.1/36.2 GPa).
- Initial waveform simulations showed complete agreement with experimental measurements.


## Related Notes

- [[lee-2008-database-mix-optimization-convex-hull]] — Contemporary ANN mixture optimization methodology by the same author (KCI).
- [[lee-kim-kim-2006-crack-pattern-recognition]] — Soft-computing applications in crack pattern recognition.
- [[kim-2007-fiber-dispersion-fluorescence]] — Image-processing and ANN techniques from the same research group.
- [[beppu-2008-damage-evaluation-of-concrete-plates]] — Impact excitation NDT for high-velocity projectile damage.
- [[bagheri-2019-ann-gp-boroaluminosilicate-geopolymer]] — Machine learning (ANN+GP) applications for concrete strength prediction.
