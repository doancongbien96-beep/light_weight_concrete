---
title: "Fiber Optic Sensors in Structural Health Monitoring"
type: source_note
source: "sources/lópez-higuera-2011-fiber-optic-sensors-in-structural.pdf"
citation: "López-Higuera, J. M., Cobo, L. R., Incera, A. Q., & Cobo, A. (2011). Fiber Optic Sensors in Structural Health Monitoring. Journal of Lightwave Technology, 29(4), 587-608."
date: 2026-08-24
tags: [fiber-optic-sensors, structural-health-monitoring, shm, fbg-gratings, distributed-sensing, botda, ofdr, civil-infrastructure, wind-turbines, ieee-jlt, landmark-paper, classic-paper, review-paper]
---

# Definitive Comprehensive Review of Fiber Optic Sensor (FOS) Systems and Interrogation Techniques for Structural Health Monitoring (SHM): The Enduring Classic on the Principles, Multiplexing, and Infrastructure Applications of FBG, Interferometric, and Continuous Distributed (BOTDA/OFDR) Sensor Networks

## Summary

To fundamentally overcome the limits that conventional electrical sensors face under harsh outdoor environments—electromagnetic induction noise (EMI), lightning damage, long-distance signal attenuation, and the weight increase of extensive multi-cable wiring—and to monitor the life-cycle safety of large civil infrastructure (bridges, dams, tunnels), wind turbine blades, and aerospace composites in real time, this **enduring landmark classic review published in 2011 in the IEEE Journal of Lightwave Technology by the research team of José Miguel López-Higuera, Chair Professor at the University of Cantabria, Spain**, comprehensively codifies the **physical-optical operating principles of fiber optic sensor (Fiber Optic Sensors: FOS) technology encompassing fiber Bragg gratings (FBG), Fabry–Perot interferometers (FP), long-gauge sensors (SOFO), and ultra-long-range continuous distributed sensors (Brillouin BOTDA, Raman ROTDR, Rayleigh OFDR/$\phi$-OTDR), optical interrogator demodulation algorithms, wavelength/time-division multiplexing (WDM/TDM) architectures, concrete- and composite-embedding packaging reliability, and global landmark infrastructure demonstration cases**.

## Key Contributions

1. **Complete mathematical and physical unified classification of the four major global SHM fiber optic sensor (FOS) technology families**:
   - It systematically formalizes the spatial resolution, measurement dynamic bandwidth, and multiplexing limits of point sensors (FBG), quasi-distributed sensors (WDM FBG arrays), long-gauge integrated sensors (SOFO), and continuous distributed sensors (BOTDA/OFDR).
2. **Establishment of the FBG wavelength modulation and the complete separation mechanism of temperature–strain cross-sensitivity**:
   - For Bragg wavelength shifts ($\Delta\lambda_B/\lambda_B = C_{\varepsilon}\Delta\varepsilon + C_T\Delta T$), it establishes the standard demodulation circuitry that cancels temperature drift $100\%$ via a dummy FBG grating or a birefringent polarization grating.
3. **Demonstration of the $1\ \text{mm}\sim 100\ \text{km}$ scale coverage of distributed Brillouin/OFDR optical sensing**:
   - It presents an all-scale SHM paradigm spanning from $50\ \text{km}$ long-range strain monitoring of pipelines and tunnels (BOTDA) to $1\ \text{mm}$ ultrahigh-resolution crack tracking inside wind blades and aerospace composites (OFDR).
4. **Establishment of standard FOS monitoring guidelines for global mega-infrastructure (long-span bridges, dams, high-speed rail)**:
   - It completes a smart-structure autonomous nervous system (Nervous System) that aggregates the signals of thousands of sensor nodes into a single optical cable and operates without failure for more than 30 years in harsh environments.

## Methods

- **Governing principles and mathematical framework of optical sensing (Sections 2~5 & Figs. 1~12)**:
  - 1. FBG gratings: $\lambda_B = 2 n_{eff} \Lambda$, strain sensitivity $1.2\ \text{pm}/\mu\varepsilon$, temperature sensitivity $10\ \text{pm}/^\circ\text{C}$.
  - 2. Fabry–Perot interference: phase difference $\phi = \frac{4\pi n L}{\lambda}$, measuring changes in the resonant cavity length.
  - 3. BOTDA distributed sensing: Brillouin frequency $\nu_B = \frac{2 n v_a}{\lambda}$, strain sensitivity $0.05\ \text{MHz}/\mu\varepsilon$, temperature sensitivity $1.0\ \text{MHz}/^\circ\text{C}$.
  - 4. OFDR high-resolution sensing: optical frequency-domain reflectometry (spatial resolution $<1.0\ \text{mm}$).
- **Industry-specific application database (Sections 6~8 & Tables 1~4 & Figs. 13~24)**:
  - Civil bridges/tunnels, wind power blades, aerospace composite airframes, offshore gas pipelines.

## Results

### 1. Comparison table of sensing mechanisms, spatial resolution, measurement distance, multiplexing capacity, and SHM application domains by major fiber optic sensor technology (Section 5 & Tables 1~3 & Figs. 25~30)

| Optical sensor technology class | Physical sensing operating principle | Measured physical quantities | Spatial Resolution | Maximum Measurement Range | Multiplexing Capacity (per channel) | Optimal SHM Application Targets |
|---|---|---|---|---|---|---|
| **FBG (point/quasi-distributed sensor)** | **Bragg reflected wavelength shift ($\Delta\lambda_B$)**| **Strain, temperature, vibration acceleration** | **Local point ($1\sim 10\ \text{mm}$)** | **$10\sim 20\ \text{km}$** | **$30\sim 100$ points (WDM/TDM)**| **Bridge girders, cables, dampers** |
| **EFPI (interferometric sensor)** | Fabry–Perot phase interference | Fine strain, pressure, acoustics | Super-local point ($1\sim 5\ \text{mm}$) | $<2\ \text{km}$ | $1\sim 4$ points | High-temperature/ultraprecision local stress |
| **SOFO (long-gauge sensor)**| Low-coherence Michelson interferometer | Long-base integrated strain, deflection | Long base ($0.2\sim 10\ \text{m}$ gauge)| $<5\ \text{km}$ | $10\sim 30$ points | Integrated strain of concrete cracking |
| **BOTDA (continuous distributed sensor)**| **Stimulated Brillouin scattering frequency** | **Continuous strain and temperature profiles**| **$0.5\sim 2.0\ \text{m}$ (wide area)** | **$>50\ \text{km}$ (ultra-long-range)** | **Continuous distribution (tens of thousands of points)** | **Tunnels, pipelines, embankments** |
| **OFDR (ultrahigh-resolution distributed)**| **Rayleigh scattering optical frequency interference**| **Micro strain and cracks** | **$<1.0\ \text{mm}$ (ultrahigh resolution)**| **$<100\ \text{m}$** | **Hundreds of thousands of points (dense)** | **Wind blades, aerospace fuselages** |

### 2. Sensor packaging and long-term harsh-environment reliability analysis
- **Complete immunity to electromagnetic fields and lightning (EMI Immunity)**: no induced electromotive force is generated at all even under high-voltage railway catenaries or in lightning-hazard zones, preventing electronic equipment damage and signal distortion $100\%$.
- **Smart-structure composite integration**: optical fibers $125\ \mu\text{m}$ in diameter are embedded without defects during carbon-fiber composite (CFRP) laminate molding, monitoring residual stresses during manufacturing and interlaminar delamination during service in real time.

- **Overall conclusion**: This paper is an enduringly authoritative, textbook-level standard landmark classic review in which Professor López-Higuera's research team codified the principles of FBG, interferometric, and ultra-long-range distributed fiber optic sensors, their interrogation techniques, and their SHM applications to global large-scale infrastructure, establishing the definitive standard of the smart structures and optical sensing engineering fields.

## Related Notes

- [[li-2004-fiber-optic-sensors-health-monitoring-civil-engineering]] — Hong-Nan Li & Gang-Bing Song: the enduring classic of civil fiber optic sensing.
- [[chan-2006-fiber-bragg-grating-sensors-bridge-shm]] — FBG bridge SHM landmark.
- [[kim-2015-sensor-type-pc-strand-embedded-fbg-sensor]] — KICT FBG smart PC strand landmark.
- [[concrete-durability-and-service-life]] — Smart SHM maintenance framework.
