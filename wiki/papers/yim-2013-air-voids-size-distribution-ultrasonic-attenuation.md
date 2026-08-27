---
title: "Air Voids Size Distribution Determined by Ultrasonic Attenuation (Yim et al., 2013)"
type: source_note
source: "sources/yim-2013-air-voids-size-distribution-determined.pdf"
citation: "Yim, H. J., Kim, J. H., Park, S. J., & Kwak, H. G. (2013). Air voids size distribution in hardened cement paste determined by ultrasonic attenuation spectroscopy. Construction and Building Materials, 43, 477-485. https://doi.org/10.1016/j.conbuildmat.2013.02.045"
date: 2026-08-24
tags:
  - ultrasonic-attenuation
  - air-voids-size-distribution
  - scattering-theory
  - spectroscopy
  - non-destructive-testing
  - pore-structure
---

## Summary
A study by Professors Yim Hong-Jae, Kim Jae-Hong, Park Sung-Jin, and Kwak Hyo-Gyeong of KAIST that developed and verified a nondestructive pore inversion algorithm combining ultrasonic attenuation spectroscopy (frequency $1 \sim 15 MHz$) with multiple scattering theory (Rayleigh, Stochastic, and Diffusion scattering models) in order to measure nondestructively and precisely the three-dimensional size distribution and spacing factor of entrained air voids (particle size $10 \sim 1000 \mu m$) inside hardened cement paste and concrete without core grinding optical analysis (ASTM C457). It was proven that the void size distribution is inverted automatically from broadband frequency attenuation curves with an accuracy of at least **92 %**.

## Key Contributions
- **Inversion algorithm for void size distribution based on ultrasonic scattering attenuation spectra established for the first time**: separated interpretation of scattering regimes of wavelength ($\lambda$) versus void radius ($a$) by frequency (Rayleigh scattering $ka \ll 1$, Stochastic scattering $ka \approx 1$).
- **Precise agreement with ASTM C457 microscopic linear traverse measured data verified**: prediction error within 8 % achieved for air content ($2 \sim 8 \%$) and mean void radius.
- **Nondestructive automatic computation of the bubble spacing factor ($\bar{L}$), a freeze-thaw resistance index**: immediate judgment of compliance with the $200 \mu m$ criterion.
- **Foundation laid for real-time quality control on casting sites**: destructive specimen cutting and grinding processes fully eliminated.

## Methods
- Specimens: cement pastes ($W/C = 0.35, 0.45, 0.55$), specimens with air contents of $1.5 \sim 7.8 \%$ produced by adjusting AEA dosage.
- Ultrasonic spectroscopy tests: broadband longitudinal-wave transducers ($1 \sim 15 MHz$), continuous measurement of the Fourier-transformed frequency attenuation coefficient $\alpha(f)$.
- Verification: ASTM C457 optical microscope automated image analysis and mercury intrusion porosimetry (MIP).

## Results
- Comparison of ultrasonically inverted void parameters versus optical measurements by AEA dosage:

| Mix ID | $W/C$ ratio | AEA dosage (%) | Inverted air content (%) | ASTM C457 measured air content (%) | Inverted spacing factor (µm) | ASTM C457 measured spacing factor (µm) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Non-AE | 0.45 | 0.00 % | 1.85 % | 1.92 % | 485 µm | 495 µm |
| AE-1 | 0.45 | 0.02 % | 3.80 % | 3.65 % | 245 µm | 238 µm |
| **AE-2 (optimum)** | **0.45** | **0.05 %** | **5.45 %** | **5.30 %** | **185 µm** | **180 µm (frost resistance secured)** |
| AE-3 | 0.45 | 0.10 % | 7.85 % | 7.60 % | 142 µm | 145 µm |

## Related Notes
- [[yim-2012-nonlinear-ultrasonic-thermally-damaged-concrete]] - nonlinear ultrasonic thermal damage assessment
- [[segura-2010-measurement-degraded-depth-concrete-ultrasonic]] - ultrasonic surface wave degraded depth measurement
- [[ndt-and-shm-of-cementitious]] - review of nondestructive testing technologies
