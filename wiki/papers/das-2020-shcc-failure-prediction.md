---
title: "A fundamental method for prediction of failure of SHCC without prior information (Das & Leung, 2020)"
type: source_note
source: "sources/CKY leung_a fundamental prediction of failure of SHCC.pdf"
citation: "Das, A.K., Leung, C.K.Y. A fundamental method for prediction of failure of strain hardening cementitious composites without prior information. Cement and Concrete Composites 114 (2020) 103745."
date: 2026-08-22
tags: [failure-prediction, finite-time-singularity, acoustic-emission, power-spectral-entropy, shcc, structural-health-monitoring, monte-carlo]
---

# Predicting the Failure Timing of SHCC Without Prior Information (Finite-Time Singularity Based)

## Summary

The first methodology for predicting the remaining service life (MRSL = EFT − COC) of SHCC structures from sensor data alone, with no laboratory data or mix information. Starting from damage mechanics σ = E(1−D)ε it derives the finite-time singularity ε ∝ [1/(t_c − t)]^m, shows that this is identical in form to Voight's empirical law (d²D/dε² = K·(dD/dε)^m, the equation long used to forecast volcanic eruptions and slope failures), then changes basis to measurable parameters and obtains the failure time by extrapolating the inverse-rate straight line. Using the power spectral entropy (PSE) of AE waveforms as the parameter, deviation of predicted failure time under normal conditions is typically below 5 %, and robustness under uncertainty, partial data, and nonlinear variable-amplitude loading was demonstrated through Monte Carlo simulation.

## Key Contributions

1. **Justifying application of the finite-time singularity → Voight empirical law to SHCC**: starting from representative-volume-element (RVE) damage mechanics, shows that the power law (1−D) ∝ (ε(t_c) − ε)^m reproduces the shape of tangent-stiffness degradation curves from Li's micromechanics numerical model and from actual tensile tests beyond the initial regime, and derives d²D/dε² = K(dD/dε)^m by double differentiation. All three failure paths (concave for m < 2, linear for m = 2, convex for m > 2) converge to a decreasing inverse rate.
2. **Parameter substitution and prediction equation**: integrating up to the condition that the inverse rate → 0 just before failure yields ε(t_c) = ε + (dD/dε)^(1−m)/(K(m−1)); substituting a field-measurable quantity P positively correlated with damage gives t_c = t + (dP/dt)^(1−m)/(K(m−1)). As P it selects PSE (the power spectral entropy of the AE signal, −Σ S log₂S over S_xx), which is independent of thresholding and filtering choices and insensitive to SNR.
3. **Training-data density control idea**: since the initial regime, in which the model does not hold, contaminates training, proposes practical strategies that lower early data density naturally — reducing the interrogation frequency of active sensors on engineering grounds, or using passive detection such as AE whose early event density is inherently low.
4. **Probabilistic frame**: models the intrinsic stochasticity of the cracking process as P = p(γ) and produces a failure-time distribution by Monte Carlo. Where a deterministic decision value is needed, mean minus standard deviation is used as a conservative estimate (e.g. mean 2.17 × 10³ s − σ 4.02 × 10² s = 1.77 × 10³ s).
5. **Objectifying DIC-based failure determination**: points out the ambiguity of visual reading of stress-strain curves (small stress jumps persist even after localization), and defines crack area CA together with TCA, which weights CA by the strain excess, as ground truth (a surge in TCA = failure; Eq. 14–15, threshold near the mortar tensile limit of ~0.01 %).
6. **Nonlinear loading extension to an R-SHCC beam**: in variable-amplitude non-periodic four-point flexural fatigue of a steel-reinforced SHCC beam (length 1 m, span 900 mm / loading point 300 mm), an InvPSE-based prediction reproduced well the material failure (localization; member capacity maintained by stress redistribution to the reinforcing bar) at ~5500 s; even when the load curve is nonlinear, the methodology remains valid as long as damage accumulates with time.
7. **Theoretical extension to creep**: the SHCC tensile creep rate ε̇_n = k·σ_n^p (a power law confirmed against literature data referenced to 0.3/0.5/0.7× tensile strength) takes a positive-feedback form and can therefore be combined with this methodology, suggesting coverage of long-term sustained-load situations.

## Methods

Tensile coupons 350 × 25 × 8 mm in two mixes: Mix-1 (FA 0.8 : cement CEM I 42.5 0.18 : silica fume 0.02 : silica sand max 0.16 mm 0.2 : water 0.22 : SP 0.003 by weight, with PVA Kuraray K-II REC15 at 1.5/2/2.5 vol %), Mix-2 (FA 0.65 : binder (PC+FA) 0.35 : rock fines max 2.36 mm 0.3 : water 0.3 : SP 0.004, PVA 2 %). Water curing for more than 28 days. Lloyd-Ametek EZ50 (50 kN) under displacement control at 0.1 mm/min, LVDT with 150 mm gauge length, two AE sensors (±4 cm from the specimen center), DIC (open-source Ncorr, Canon EOS D6 II automatic capture at 30 s intervals). The inverse rate of PSE is computed over equal windows of 10 s, fitted with m = 2 (the typical value for geomaterials), and the point where the inverse-rate curve meets the X axis is defined as the predicted failure time. Verification metric NE = |predicted − actual|/total test duration.

## Results

- **Normal conditions**: mean NE by test-duration cluster — ≤500 s: 0.103, 500–1000 s: 0.041, 1000–1500 s: 0.034, 1500–2000 s: 0.037, 2000–2500 s: 0.023, ≥2500 s: 0.029. That is, typically <5 % error with no dependence on total failure time (generalizes across a wide range of strain capacities below and above 3 %). The degradation of the shortest test cluster stems from too few training points plus the sensitivity of NE at short durations.
- **Probabilistic stability**: in the worst case that adds uncertainty U (twice the experimental level) on top of observations, the mode's NE stayed < 0.05 for all three of normal/lognormal/uniform distributions. Lognormal showed the largest variance because of its many extreme events.
- **Partial data** (Case A monitoring only the beginning / Case B monitoring after damage detection / Case C fixed sliding window): probability within ±0.1 NE averaged ~0.86, with most of each distribution inside ±0.1 NE. Case A under-predicts from departure out of the initial regime (concave up at m = 2) and Case B over-predicts from departure out of the final regime (convex down at m = 2) — the influence of the distorted regimes dilutes as the window grows.
- **R-SHCC beam**: under variable-amplitude non-periodic loading the predicted distribution matches the TCA surge (~5500 s). Even though individual InvPSE points fluctuate with amplitude changes, a sufficiently large time window averages them out.

## Related Notes

- [[pseudo-strain-hardening-criteria]] — the definition of 'failure' (termination of multiple cracking and crack localization) ties directly to exhaustion of PSH; the context in which PSE was developed by the same author's earlier work as an operational regime identifier distinguishing the saturated multiple-cracking phase from the localization phase.
- [[li-wu-1992-psh-conditions]] — origin reference for the SHCC micromechanics design basis cited at the outset (Li-Leung 1992 multiple-cracking theory); the paper's micromechanics simulation benchmark is also a Li-lineage model.
- [[qiu-2016-fatigue-dependent-fiber-bridging-model]] — treats bridging-capacity degradation under repeated loading via micromechanics, while this paper addresses the resulting behavioral degradation through sensor time series: a complementary pair.
- [[monteiro-2017-carbon-black-traffic-sensor]] — the same sensing-for-infrastructure axis, reading structural state through a cementitious self-sensing parameter (PSE vs electrical resistance).
