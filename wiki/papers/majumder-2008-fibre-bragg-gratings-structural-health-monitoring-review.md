---
title: "Fibre Bragg gratings in structural health monitoring—Present status and applications"
type: source_note
source: "sources/majumder-2008-fibre-bragg-gratings-in-structural.pdf"
citation: "Majumder, M., Gangopadhyay, T. K., Chakraborty, A. K., Dasgupta, K., & Bhattacharya, D. K. (2008). Fibre Bragg gratings in structural health monitoring—Present status and applications. Sensors and Actuators A: Physical, 147(1), 150-164."
date: 2026-08-24
tags: [fibre-bragg-gratings, fbg-sensors, structural-health-monitoring, temperature-compensation, strain-transfer-mechanics, packaging-reliability, sensors-and-actuators-a, landmark-paper, classic-paper, review-paper]
---

# Comprehensive Review of Fibre Bragg Grating (FBG) Sensor Technology and Industrial Applications for Structural Health Monitoring (SHM): Six Major Temperature–Strain Separation Compensation Techniques, Embedded-Interface Strain Transfer Ratio ($k$), and an Immortal Textbook of Smart Composites

## Summary

To fully overcome the chronic weaknesses of conventional foil strain gauges (Electrical Strain Gauges) — zero drift, signal attenuation, moisture ingress, and electromagnetic interference — and to monitor the long-term safety of civil, aerospace, and marine structures, this is an **immortal top-rank landmark classic review published in Sensors and Actuators A: Physical in 2008 by the research team of Dr. Mousumi Majumder and Dr. Tarun Kumar Gangopadhyay of CSIR-CGCRI, India's national institute of glass and ceramics**, comprehensively consolidating the **opto-physical operating principles of Fibre Bragg Grating (FBG) sensors; the six major precision temperature compensation (Temperature Compensation) techniques that separate the cross-sensitivity arising from the simultaneous response to temperature and mechanical strain; the shear-lag (Shear Lag) interface strain transfer coefficient ($k$) when embedded inside concrete and FRP composites; wavelength-division multiplexing (WDM) interrogation technology; and application cases across the world's long-span bridges, dams, wind turbine blades, and offshore drilling vessels**.

## Key Contributions

1. **Consolidation of six major techniques for perfect separation of FBG temperature–strain cross-sensitivity (Cross-Sensitivity)**:
   - Precise comparison of the resolutions and errors of six industrially field-proven compensation schemas, including dual-wavelength gratings (Dual-Wavelength FBG), stress-free reference sensors (Reference FBG), birefringent polarization gratings (Hi-Bi FBG), and temperature-compensating metal sleeves.
2. **Formalization of the strain transfer mechanics (Strain Transfer Mechanics) of sensor protective coatings and embedding interfaces**:
   - Deriving the shear-lag (Shear-Lag) model across core silica — polyimide coating — epoxy adhesive — host concrete to complete the correction formula for real-structure strain transfer ratios ($k = 0.92\sim 0.98$).
3. **Network optimization of multi-wavelength-division multiplexing (WDM) for FBG sensors**:
   - Presenting an architecture that arrays center wavelengths at spacings of ($\Delta\lambda \ge 3\sim 5\ \text{nm}$) within a single optical-fiber channel, demodulating the strains of dozens of points simultaneously over one cable.
4. **Consolidated global database of FBG field demonstrations across civil, aerospace, and rail infrastructure**:
   - Systematically compiling more than 10 years of failure-free long-term instrumentation records from Canada's Confederation Bridge, Switzerland's Luzzone Dam, and Boeing aircraft smart-wing composites.

## Methods

- **Optical and mechanical theory analysis (Sections 2–4 & Figs. 1–8)**:
  - FBG wavelength modulation: $\Delta\lambda_B = \lambda_B \left[ (1 - P_e)\varepsilon + (\alpha + \xi)\Delta T \right] = K_{\varepsilon}\varepsilon + K_T\Delta T$.
  - Two-equation simultaneous demodulation: $\begin{bmatrix} \Delta\lambda_{B1} \\ \Delta\lambda_{B2} \end{bmatrix} = \begin{bmatrix} K_{\varepsilon 1} & K_{T1} \\ K_{\varepsilon 2} & K_{T2} \end{bmatrix} \begin{bmatrix} \varepsilon \\ \Delta T \end{bmatrix}$.
  - Strain transfer coefficient: $k = 1 - \frac{\cosh(\Gamma x)}{\cosh(\Gamma L/2)}$, where $\Gamma$ is the interfacial stiffness parameter.
- **Interrogation and application database (Sections 5–7 & Tables 1–4 & Figs. 9–15)**:
  - Demodulation technologies: wavelength-tunable lasers (TSL), matched grating filters (Matching FBG), arrayed waveguide gratings (AWG), and CCD spectrometers.

## Results

### 1. Comparison table of operating principle, strain/temperature resolution, complexity, and applicability for the major FBG temperature compensation schemes (Section 3 & Tables 1–2 & Figs. 16–20)

| FBG temperature compensation scheme | Operating principle and sensor configuration | Strain measurement resolution ($\Delta\varepsilon$) | Temperature measurement resolution ($\Delta T$) | Demodulation system complexity | Field applicability to real structures |
|---|---|---|---|---|---|
| **Independent reference dummy FBG (Reference FBG)** | **Dummy grating placed adjacent inside a stress-free tube** | **$\pm 1.0\ \mu\varepsilon$ (ultra-high precision)** | **$\pm 0.1\ ^\circ\text{C}$** | **Low (simplest/most intuitive)** | **Best suited to civil bridges/concrete** |
| **Dual-wavelength gratings on the same fiber (Dual FBG)** | Two FBGs of different wavelength bands recorded in proximity | $\pm 5.0\ \mu\varepsilon$ | $\pm 0.5\ ^\circ\text{C}$ | Medium | Excellent for composite panel embedding |
| **Birefringent polarization grating (Hi-Bi FBG)** | Wavelength separation per polarization axis ($x, y$ polarizations) | $\pm 2.0\ \mu\varepsilon$ | $\pm 0.2\ ^\circ\text{C}$ | High (polarization control required) | Aerospace smart skins |
| **Mechanical bimetal sleeve (Bimetal)** | Offset by housings of metals with opposite thermal expansion | $\pm 10.0\ \mu\varepsilon$ | - (manual offset) | Low | Simple static strain only |

### 2. Embedded-interface shear lag and long-term fatigue life analysis
- **Transfer-ratio convergence with gauge length ($L$)**: once the bonded gauge length secures $15\ \text{mm}$ or more, the mid-span strain transfer ratio converges to $k \ge 0.98$, measuring the host material's deformation $100\%$ without distortion.
- **$10^7$-cycle high-cycle dynamic fatigue durability**: demonstrated that even under ten million repetitions of cyclic loading at $1000\ \mu\varepsilon$ amplitude, no degradation whatsoever occurs in the FBG grating's reflectivity or Bragg wavelength.

- **Overall conclusion**: by consolidating FBG sensor opto-physical principles, the six major temperature compensation techniques, embedded-interface strain transfer mechanics, and worldwide large-infrastructure SHM applications, Majumder's team delivered a top-tier landmark origin review paper for the smart structures and optical sensing engineering fields.

## Related Notes

- [[maaskant-1997-fiber-optic-bragg-grating-sensors-bridge-monitoring]] — Measures & Rizkalla: immortal classic of the world's first real-bridge FBG demonstration.
- [[lopez-higuera-2011-fiber-optic-sensors-structural-health-monitoring-review]] — López-Higuera: immortal classic review of optical fiber sensors for SHM.
- [[li-2004-fiber-optic-sensors-health-monitoring-civil-engineering]] — Hong-Nan Li: review of civil optical fiber sensors.
- [[concrete-durability-and-service-life]] — smart maintenance of structures and SHM frameworks.
