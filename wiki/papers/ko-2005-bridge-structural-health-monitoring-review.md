---
title: "Technology developments in structural health monitoring of large-scale bridges"
type: source_note
source: "sources/ko-2005-technology-developments-in-structural-health.pdf"
citation: "Ko, J. M., & Ni, Y. Q. (2005). Technology developments in structural health monitoring of large-scale bridges. Engineering Structures, 27(12), 1715-1725."
date: 2026-08-24
tags: [structural-health-monitoring, large-scale-bridges, cable-stayed-bridges, suspension-bridges, fiber-optic-sensors, fbg-sensors, modal-identification, damage-detection, engineering-structures, landmark-review, theory-foundation]
---

# Structural Health Monitoring (SHM) System Architecture for Large-Scale Cable-Supported Bridges: Optical Fiber FBG Sensing, Distributed DAU Networks, Modal Damage Detection, and Lifecycle Assessment Review

## Summary

To ensure structural safety and enable early damage detection in large-scale cable-supported bridges (suspension and cable-stayed spans of $100\sim 2000\ \text{m}$, such as Tsing Ma, Sutong, Jiangyin, and Seohae Bridges) subjected to extreme natural hazards (typhoons, earthquakes) and traffic fatigue, Prof. J.M. Ko and Prof. Y.Q. Ni at the Hong Kong Polytechnic University (PolyU) synthesized technological developments over the past 20 years. This review systematically covers **SHM system design, embedded optical fiber Bragg grating (FBG) and Brillouin optical time-domain reflectometry (BOTDR) sensing, wireless smart sensor networks, optimal placement of PXI/SCXI-based distributed data acquisition units (DAU), modal-parameter-based damage detection algorithms (natural frequencies, mode shape curvatures, flexibility matrices), and lifecycle maintenance decision support**. By integrating statistical normalization to filter environmental variations (temperature gradients, traffic changes) with tendon-embedded FBG sensing, the authors established a modern structural health monitoring paradigm spanning from localized defect detection ($1.0\ \mu\varepsilon$ strain changes) to global dynamic property tracking.

## Key Contributions

1. **Standardization of the 6-layer SHM system architecture for large-scale bridges**:
   - Formulated a 6-stage integrated framework: sensor measurement $\rightarrow$ distributed DAU collection $\rightarrow$ optical data transmission $\rightarrow$ data pre-processing/mining $\rightarrow$ damage identification/health assessment $\rightarrow$ maintenance decision support.
2. **Framework for fiber optic FBG and Brillouin (BOTDR) sensing in stay and suspension cables**:
   - Demonstrated embedding FBG sensors into multi-kilometer main cables and stay cables for electromagnetic interference (EMI)-free permanent tension tracking.
3. **Optimal deployment of distributed data acquisition units (DAU) with PXI/SCXI optical networking**:
   - Deployed 7 or more decentralized DAU substations synchronized over FDDI optical networks to overcome cable signal attenuation across long bridge spans.
4. **Formulation of modal damage detection under environmental temperature/wind filtering**:
   - Established statistical regression (PCA/ANN) to filter daily temperature-induced frequency variations (up to 5 %), isolating true structural stiffness degradation.

## Methods

- **Global long-span bridge SHM database and sensor systems (Section 2 & Table 1)**:
  - Investigated 20 major cable-supported bridges in China and Hong Kong (e.g., Sutong Bridge span 1088 m, Tsing Ma Bridge span 1377 m, Jiangyin Bridge span 1385 m).
  - Sensor inventory:
    - Environmental loads: Anemometers (3D ultrasonic), temperature sensors (ambient and structural), seismometers.
    - Structural response: Accelerometers (servo and piezoelectric), displacement sensors (GPS and laser), tiltmeters, strain gauges (FBG and vibrating wire), cable tension sensors (EM sensors).
- **Modal damage detection formulations (Section 5)**:
  - Mode shape curvature damage index:
    $$\kappa_i = \frac{\phi_{i+1} - 2\phi_i + \phi_{i-1}}{h^2}$$
  - Change in flexibility matrix:
    $$[F] \approx \sum_{r=1}^{m} \frac{1}{\omega_r^2} \{\phi_r\} \{\phi_r\}^T, \quad [\Delta F] = [F_d] - [F_u]$$
  - Temperature-vibration correlation models using PCA and neural networks to remove thermal effects.

## Results

### 1. SHM sensor instrumentation and data acquisition architectures in landmark bridges (Tables 1–2 & Figs. 1–4)

| Bridge Name | Bridge Type | Main Span (m) | Sensor Types & Channels | Primary Monitored Parameters | DAU & Transmission Architecture |
|---|---|---|---|---|---|
| **Sutong Bridge** | Cable-stayed | **1088 m** | **18 types, 800+ channels** | **FBG cable tension, GPS tower displacement, wind vibration** | **7 distributed DAUs + PXI/SCXI FDDI optical network** |
| **Tsing Ma Bridge** | Suspension | 1377 m | 11 types, 600+ channels | Main cable tension, truss girder deflection, typhoon accelerations | 6 substations + real-time modal analysis |
| **Jiangyin Bridge** | Suspension | 1385 m | 9 types, 350+ channels | FBG girder strains, suspender fatigue | Centralized optical fiber interrogators |
| **Ting Kau Bridge** | 3-Tower Cable-stayed | 475 m × 2 | 8 types, 230+ channels | Central cable stabilization, pier tilting | High-speed synchronized DAU network |
| **Seohae Bridge** | Cable-stayed (Korea) | 470 m | 6 types, 180+ channels | Wind vibrations, cable tension variations | Distributed data acquisition system |

### 2. Sensing reliability and multi-scale damage identification mechanics
- **Long-term durability of optical fiber sensors**: Whereas electrical strain gauges exhibited > 50 % failure rates within 2~3 years from moisture ingress, FBG optical sensors maintained zero signal drift over 10+ years in aggressive marine environments.
- **Multi-scale damage synthesis**: Merged localized FBG strain tracking at fatigue hotspots with global accelerometer networks tracking overall structural flexibility changes ($[\Delta F]$).

- **Overall conclusion**: This review standardized structural health monitoring frameworks, optical fiber sensor deployment, distributed DAU networking, and modal damage detection for large-scale bridges globally.

## Related Notes

- [[kim-2012-fbg-smart-strand-prestressing-monitoring]] — Development of 7-wire smart strands with core-embedded FBG sensors.
- [[kim-2016-fbg-smart-strand-pretensioned-uhpc-deck]] — Prestress loss and wheel load fatigue monitoring in full-scale UHPC decks.
- [[structural-repair-and-retrofitting]] — Non-destructive structural diagnostics and repair/retrofitting frameworks.
- [[kang-2015-tunnel-lining-concrete-ultrasonic-strength-grade]] — Non-destructive safety assessment of infrastructure systems.
