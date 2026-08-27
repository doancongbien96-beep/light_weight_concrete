---
title: "Fiber Bragg grating sensors for structural health monitoring of bridges"
type: source_note
source: "sources/chan-2006-fiber-bragg-grating-sensors-for.pdf"
citation: "Chan, T. H. T., Yu, L., Tam, H. Y., Ni, Y. Q., Liu, S. Y., Chung, W. H., & Cheng, L. K. (2006). Fiber Bragg grating sensors for structural health monitoring of bridges. Structural Health Monitoring, 5(4), 381-407."
date: 2026-08-24
tags: [fiber-bragg-grating, fbg-sensors, structural-health-monitoring, bridge-monitoring, dynamic-strain-measurement, temperature-compensation, smart-structures, tommy-chan, landmark-paper, classic-paper]
---

# Fiber Bragg Grating (FBG) Sensor-Based Real-Time Structural Health Monitoring (SHM) of Long-Span Bridges: Dynamic Strain Measurement, Temperature Compensation, and Complete Immunity Mechanisms against Electromagnetic Interference (EMI)

## Summary

To overcome the electromagnetic interference (EMI) vulnerability of electrical strain gauges, their signal attenuation, and their short service life in harsh outdoor environments, and to monitor the long-term structural health of large infrastructure bridges in real time, the research team of Profs. Tommy H. T. Chan, Y. Q. Ni, and H. Y. Tam at The Hong Kong Polytechnic University (HKPolyU) developed a multichannel optical sensing system based on fiber Bragg gratings (FBG: Fiber Bragg Grating, modulation of the refractive-index grating spacing inside the fiber core, central wavelength $\lambda_B = 1550\ \text{nm}$) and embedded/bonded several hundred FBG sensors on two in-service Hong Kong bridges, the Tsing Ma Suspension Bridge and the Ting Kau Cable-Stayed Bridge, demonstrating for the first time in the world dynamic micro-strains of $\pm 500\ \mu\varepsilon$ under passing high-speed trains, temperature-coupled combined wavelength shifts ($\Delta\lambda_B$), complete immunity to electromagnetic noise ($0.0\ \text{dB}$), and stable high-rate dynamic sampling above $100\ \text{Hz}$: a landmark classic paper of the highest authority in Structural Health Monitoring (2006).

## Key Contributions

1. **World-first commercial-scale demonstration of FBG optical sensing monitoring on long-span sea-crossing bridges**:
   - FBG sensor networks installed on the steel trusses and concrete towers of Hong Kong's representative suspension bridge (Tsing Ma Bridge) and cable-stayed bridge (Ting Kau Bridge), establishing a standard for real-time condition diagnosis.
2. **Establishment of temperature-strain cross-interference separation and precision compensation (Temperature Compensation) technology**:
   - Stress-free dummy FBG sensors deployed in pairs completely cancel temperature-induced refractive-index drift, extracting only the pure mechanical dynamic strain at $1\ \mu\varepsilon$ resolution.
3. **Demonstration of complete immunity to lightning and high-voltage railway catenary electromagnetic interference (EMI)**:
   - Signals travel as light wavelengths through pure silica-glass optical fiber rather than electrical conductors, demonstrating that electromagnetically induced noise is blocked $100\%$.
4. **Realization of wavelength division multiplexing (WDM: Wavelength Division Multiplexing) over a single fiber**:
   - Dozens of FBG sensors with distinct reflection wavelengths connected in series along a single optical cable reduce wiring complexity and installation cost by $80\%$.

## Methods

- **FBG principle and sensing-system configuration (Section 2 & Figs. 1–3)**:
  - Bragg reflection condition: $\lambda_B = 2n_{eff}\Lambda$ ($n_{eff}$: effective core refractive index, $\Lambda$: grating period).
  - Wavelength-shift relation: $\Delta\lambda_B / \lambda_B = (1 - p_e)\Delta\varepsilon + (\alpha + \xi)\Delta T$ ($p_e = 0.22$: photoelastic coefficient, $\alpha$: thermal expansion coefficient, $\xi$: thermo-optic coefficient).
  - Instrumentation system: broadband ASE light source + high-speed wavelength-tunable filter interrogator (sampling rates $100\sim 500\ \text{Hz}$).
- **Field tests on actual bridges (Sections 3–5 & Figs. 4–12)**:
  - Target bridge: Tsing Ma Bridge, Hong Kong (main span $1377\ \text{m}$ rail-road double-deck suspension bridge).
  - Measured quantities: dynamic flexural strains of steel cross girders during Airport Express Line (AEL) train passages; typhoon wind-load response.

## Results

### 1. Field comparison of measurement performance, FBG sensors versus conventional electrical strain gauges (ESG), on Tsing Ma Bridge steel girders during high-speed train passages (Section 4 & Figs. 8–14)

| Measured quantity and characteristics | Conventional electrical resistance gauge (ESG) | FBG optical-fiber sensor system (FBG) | Performance gains and benefits |
|---|---|---|---|
| **Strain measurement resolution ($\mu\varepsilon$)** | **$\pm 5.0\ \mu\varepsilon$** | **$\pm 0.5 \sim 1.0\ \mu\varepsilon$** | **Five-fold precision improvement** |
| **Railway catenary electromagnetic interference (EMI noise)**| **Severe high-frequency noise ($\text{SNR} < 15\ \text{dB}$)**| **No noise ($\text{SNR} > 60\ \text{dB}$, complete immunity)**| **Perfect signal integrity** |
| **Long-term signal drift (Zero Drift)** | Zero point wanders with temperature/humidity | Absolute wavelength measurement eliminates drift entirely ($0.0$) | **Optimal for long-term monitoring** |
| **Sensor capacity per single cable** | One channel per cable (hundreds of wires) | **$16\sim 32$ multiplexed per optical fiber (WDM)**| **Wiring cost cut by $80\%$** |
| **Maximum dynamic strain under train passage** | $450 \pm 25\ \mu\varepsilon$ (noise superimposed) | **$448.5 \pm 2.0\ \mu\varepsilon$ (clean waveform)** | **Accurate fatigue stress-history acquisition** |

### 2. Interpretation of the optical wavelength-modulation and fatigue-damage diagnosis mechanism
- **Clarity of train-load response waveforms**: the four bogie load peaks produced as a high-speed train enters and passes are perfectly separated in the FBG wavelength spectrum, so accumulated bridge fatigue damage can be computed within $1\%$ error.
- **Long-term durability under marine wind exposure**: epoxy- and stainless-tube-encapsulated FBG sensors verified to operate for more than 10 years in a marine saline environment without sensitivity degradation.

- **Overall conclusion**: this paper is the highest-authority landmark classic of smart-infrastructure structural health monitoring (SHM), in which Prof. Tommy Chan's research team applied fiber-optic FBG sensors to full-scale long-span bridges and gave the first complete demonstration of high-precision dynamic strain measurement free of electromagnetic noise together with long-term condition assessment.

## Related Notes

- [[kim-2007-simulation-parameters-surface-wave-propagation-concrete-ann]] — original work on AI-based NDT via acoustic surface waves.
- [[monteiro-2017-self-sensing-piezoresistive-cement-carbon-black]] — original work on piezoresistive self-sensing concrete with carbon black.
- [[mac-2020-thermography-deterioration-detection-cfrp-bridge-girders]] — landmark infrared thermographic non-destructive detection.
- [[concrete-durability-and-service-life]] — smart maintenance and service-life prediction framework for structures.
