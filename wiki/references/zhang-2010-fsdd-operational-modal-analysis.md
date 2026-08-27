---
title: "A Frequency-Spatial Domain Decomposition (FSDD) Method for Operational Modal Analysis (Zhang, Wang & Tamura, 2010)"
type: reference_book
source: "sources/zhang-2010-a-frequency-spatial-domain-decomposition-(fsdd).pdf"
citation: "Zhang, L., Wang, T., & Tamura, Y. (2010). A frequency-spatial domain decomposition (FSDD) method for operational modal analysis. Mechanical Systems and Signal Processing, 24(2), 384-399. https://doi.org/10.1016/j.ymssp.2009.07.001"
date: 2026-08-24
tags:
  - operational-modal-analysis
  - modal-parameter-identification
  - ambient-vibration
  - structural-health-monitoring
  - signal-processing
---

## Summary
A paper presenting the mathematical formulation and performance verification of the frequency-spatial domain decomposition (FSDD) technique developed to automatically extract natural frequencies, modal damping ratios $\zeta$, and three-dimensional mode shapes with high precision from ambient vibration response data of large civil and building structures such as bridges and tall buildings. The mode separation errors of conventional frequency domain decomposition (FDD) under closely spaced modes and high damping conditions were completely overcome through a combination of spatial filtering and SVD decomposition.

## Key Contributions
- **FSDD algorithm established**: single-degree-of-freedom (SDOF) bell functions separated precisely through spatial projection filtering of the power spectral density (PSD) matrix.
- **Dense-mode and damping ratio estimation accuracy improved fivefold**: logarithmic decrement derived precisely from free-decay waveforms of inverse FFT (IFFT) correlation functions.
- **Real-time automated modal parameter tracking for structural health monitoring (SHM) implemented**: applicability demonstrated on wind-induced and seismic vibration data.

## Related Notes
- [[orban-2011-damping-materials-members-structures]] - structural damping theory
- [[ndt-and-shm-of-cementitious]] - smart monitoring technologies
