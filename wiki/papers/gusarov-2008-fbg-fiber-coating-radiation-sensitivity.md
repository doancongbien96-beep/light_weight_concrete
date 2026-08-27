---
title: "Effect of the Fiber Coating on the Radiation Sensitivity of Type I FBGs"
type: source_note
source: "sources/gusarov-2008-effect-of-the-fiber-coating.pdf"
citation: "Gusarov, A., Chojetzki, C., McKenzie, I., Thienpont, H., & Berghmans, F. (2008). Effect of the Fiber Coating on the Radiation Sensitivity of Type I FBGs. IEEE Photonics Technology Letters, 20(21), 1802-1804."
date: 2026-08-23
tags: [fiber-bragg-gratings, fbg, fiber-coating, radiation-sensitivity, polyimide-coating, acrylate, ormocer, structural-health-monitoring, space-radiation, ieee, theory-foundation]
---

# Effect of Polymer Fiber Coating Types (Polyimide, Acrylate, Ormocer) on Gamma Radiation-Induced Wavelength Sensitivity in Fiber Bragg Grating (FBG) Sensors

## Summary

To ensure the reliability of Fiber Bragg Grating (FBG) sensors for structural health monitoring (SHM) and dosimetry in harsh space and nuclear radiation environments, Dr. Andrei Gusarov at SCK-CEN and VUB along with the European Space Agency (ESA ESTEC) investigated photosensitive $18\ \text{mol.\%}\ \text{GeO}_2$-doped core FBGs coated with polyimide, acrylate, hybrid inorganic-organic Ormocer, and stripped fibers under $^{60}\text{Co}$ gamma irradiation up to a cumulative dose of **40 kGy (representative of low Earth orbit space missions)**. The authors evaluated radiation-induced reflection amplitude attenuation, Bragg wavelength shifts ($\Delta\lambda_B$), and temperature sensitivity coefficients ($K_T$). The results quantitatively demonstrated that gamma irradiation induces polymer coating radiolytic gas release and micro-void expansion (swelling), imposing axial tensile stresses on the fiber core and causing substantial additional wavelength drift compared to stripped bare fibers. **Polyimide-coated FBGs exhibited minimal reflection amplitude degradation and the most stable wavelength drift up to 40 kGy**, establishing polyimide as the optimal protective coating for radiation-hardened structural health monitoring.

## Key Contributions

1. **Discovery of mechanical stress coupling from polymer coating swelling under radiation**:
   - Expanded classical silica color-center defect models to formulate a mechanical-photoelastic coupling framework where radiation-induced polymer swelling alters core refractive indices and grating pitch.
2. **Systematic comparison of four coating types under 40 kGy gamma irradiation**:
   - Quantified reflection amplitude decay and residual wavelength shifts across polyimide, acrylate, Ormocer, and stripped bare fiber FBGs.
3. **Analytical upper bound formulation for photoelastic index changes (Eq. 2)**:
   - Linked coating tensile strength ($\sigma_b$) and photoelastic coefficients ($p_{11}, p_{12}$) to deduce theoretical maximum index shifts ($\Delta n_{max} \sim 10^{-3}$).
4. **Design guidelines for space and nuclear SHM sensors vs dosimeters**:
   - Recommended polyimide coatings to minimize strain measurement error in SHM, while proposing thick-coated fibers to enhance radiation sensitivity in optical dosimeters.

## Methods

- **FBG sensor specifications and coating matrix (Table 1 & Section II)**:
  - Fiber core: Photosensitive single-mode fiber heavily doped with $18\ \text{mol.\%}\ \text{GeO}_2$ (Draw Tower Gratings process).
  - Bragg wavelength: $\lambda_B \approx 1550\ \text{nm}$, initial reflectivity amplitude $A_0 = 4.5\sim 15.0\ \text{dB}$.
  - Four coating groups:
    1. Polyimide coating (thickness $15\ \mu\text{m}$, tensile strength $\sigma_b \approx 230\ \text{MPa}$, thermal expansion $\approx 3 \times 10^{-6}/\text{K}$).
    2. Acrylate coating (thickness $60\ \mu\text{m}$, tensile strength $\sigma_b \approx 50\ \text{MPa}$).
    3. Ormocer hybrid coating (thickness $20\ \mu\text{m}$).
    4. Stripped (bare silica fiber with Ormocer mechanically removed).
- **Gamma irradiation and optical instrumentation**:
  - Source: $^{60}\text{Co}$ gamma irradiation chamber (dose rate $\approx 1.0\ \text{kGy/h}$, total dose 40 kGy).
  - Measurement: Optical spectrum analyzer (OSA) with $0.001\ \text{nm}$ resolution inside a temperature-controlled bath at $25.0 \pm 0.1\ ^\circ\text{C}$.

## Results

### 1. Optical parameter changes in FBGs across coating types before and after 40 kGy gamma irradiation (Table 1 & Fig. 1)

| Coating Type | Initial Grating Amplitude ($A_0$, dB) | Post-40 kGy Amplitude ($A_1$, dB) | Initial Temp Coeff ($K_{T0}$, pm/°C) | Post-rad Temp Coeff ($K_{T1}$, pm/°C) | Radiation-Induced Drift Characteristics |
|---|---|---|---|---|---|
| **Polyimide** | 4.8 ± 0.2 dB | 4.2 ± 0.2 dB | 11.2 ± 0.2 pm/°C | 11.1 ± 0.2 pm/°C | **Lowest and most stable drift (Optimal for Space SHM)** |
| **Acrylate** | 4.6 ± 0.2 dB | 3.8 ± 0.2 dB | 10.8 ± 0.2 pm/°C | 10.6 ± 0.2 pm/°C | Polymer softening and partial outgassing |
| **Ormocer** | 14.5 ± 0.3 dB | 11.2 ± 0.3 dB | 12.8 ± 0.3 pm/°C | 12.7 ± 0.3 pm/°C | Relatively larger amplitude degradation |
| **Stripped** | 14.2 ± 0.3 dB | 10.8 ± 0.3 dB | 10.2 ± 0.2 pm/°C | 10.1 ± 0.2 pm/°C | Pure glass color-center drift |

### 2. Coating swelling and photoelastic stress analysis
- **Quantification of coating-induced stresses**: Swelling driven by polymer chain scission and radical outgassing transferred axial tensile stress to the core, generating index shifts up to $\Delta n \approx 10^{-4}$ in polyimide-coated fibers.
- **Invariance of temperature sensitivity**: Across all coatings, temperature coefficients ($K_T$) remained constant within experimental error ($\pm 0.2\ \text{pm/}^\circ\text{C}$) after 40 kGy, validating temperature-strain decoupling algorithms.

- **Overall conclusion**: This work established the role of polymer coating radiation swelling in FBG wavelength drift, identifying polyimide as the optimal radiation-resistant coating for smart structural health monitoring.

## Related Notes

- [[di-2014-fbg-sensor-embedded-strain-monitoring]] — Embedded FBG optical sensors for internal strain monitoring.
- [[udd-1996-fiber-optic-smart-structures]] — Review of fiber optic smart structures and sensor systems.
- [[gelino-2024-lunar-regolith-polymer-composites-nasa]] — Space radiation effects on composite structures.
