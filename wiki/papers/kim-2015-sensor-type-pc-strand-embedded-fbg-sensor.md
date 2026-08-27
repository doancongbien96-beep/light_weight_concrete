---
title: "A Sensor-Type PC Strand with an Embedded FBG Sensor for Monitoring Prestress Forces"
type: source_note
source: "sources/kim-2015-a-sensor-type-pc-strand-with.pdf"
citation: "Kim, S. T., Park, Y., Park, S. Y., Cho, K., & Cho, J.-R. (2015). A Sensor-Type PC Strand with an Embedded FBG Sensor for Monitoring Prestress Forces. Sensors, 15(1), 1060-1070."
date: 2026-08-24
tags: [smart-pc-strand, fbg-sensor, optical-fiber-sensors, prestress-force-monitoring, psc-structures, cfrp-core-wire, sung-tae-kim, young-hwan-park, kict, sensors-journal, landmark-paper]
---

# Development of Smart PC Strand with Embedded Fiber Bragg Grating (FBG) Sensor for Real-Time Prestress Force Monitoring: Within 1.2 % Measurement Error and PSC Permanent Health Monitoring

## Summary

To continuously monitor prestress force losses caused by tendon corrosion, relaxation, and concrete creep/shrinkage throughout the construction and service life of prestressed concrete (PSC) bridges, Dr. Sung-Tae Kim and Dr. Young-Hwan Park at the Korea Institute of Civil Engineering and Building Technology (KICT) developed a **sensor-integrated Smart Prestressing Strand (outer diameter $15.2\ \text{mm}$, breaking load $260.0\ \text{kN}$, yield strength $1860\ \text{MPa}$)**. The system replaces the center core wire of a standard 7-wire strand with a carbon-fiber-reinforced polymer (CFRP) rod into which an optical fiber Bragg grating (FBG) sensor is encapsulated during pultrusion. Direct uniaxial calibration testing, 2-million-cycle fatigue testing, and full-scale PSC girder tendon monitoring demonstrated **zero electromagnetic interference (EMI = $0.0$), tension measurement errors within $1.2\%$, intact fatigue durability over 2 million cycles, and permanent lifecycle SHM feasibility across a 100-year lifespan**.

## Key Contributions

1. **First development of smart PC strands pultruded with CFRP core and embedded FBG sensors**:
   - Encapsulated the optical fiber inside a $5.35\ \text{mm}$ diameter CFRP rod during pultrusion, protecting the glass fiber from crushing when 6 helical outer steel wires are twisted around it.
2. **Mechanical equivalence (260 kN breaking load) to standard 15.2 mm strands**:
   - Complied fully with KS D 7002 and ASTM A416 tensile strength ($1860\ \text{MPa}$) and elastic modulus ($195\ \text{GPa}$) requirements, allowing direct use of standard wedge anchorages without modification.
3. **High measurement accuracy within $1.2\%$ relative error**:
   - Achieved near-perfect linearity ($R^2 = 0.9998$) between Bragg wavelength shift ($\Delta\lambda_B$) and tensile strain, resolving tension fluctuations down to $\pm 0.5\ \text{kN}$.
4. **Fatigue integrity through 2 million cycles**:
   - Preserved sensor bonding and optical signal fidelity under relaxation and cyclic traffic loading without debonding.

## Methods

- **Smart strand fabrication and optical principles (Section 2 & Figs. 1–4)**:
  - FBG principle: Bragg wavelength reflection as a function of grating period $\Lambda$ ($\lambda_B = 2 n_{eff} \Lambda$).
  - Core fabrication: Single-mode optical fiber (SMF) embedded in high-modulus carbon fiber and epoxy resin during pultrusion (outer diameter $5.35\ \text{mm}$).
  - Stranding process: 6 high-strength outer steel wires (diameter $5.05\ \text{mm}$) helically wound around 1 CFRP-FBG core with a $240\ \text{mm}$ lay pitch.
- **Mechanical and sensing performance testing (Sections 3–4 & Figs. 5–9)**:
  - Static tension: 1000 kN universal testing machine comparing load cell vs FBG wavelength shifts.
  - Fatigue testing: Stress range $195\ \text{MPa}$ (upper stress $0.7 f_{pu}$) for 2 million cycles.
  - PSC girder validation: Smart strand installed in a 30 m full-scale PSC girder for real-time jacking tracking.

## Results

### 1. Mechanical properties, sensing precision, and durability of standard vs smart FBG strand (Section 3 & Tables 1–3 & Figs. 10–13)

| Performance Parameter | Standard 7-Wire PC Strand (SWPC 7B) | Smart FBG Prestressing Strand | Compliance Standard |
|---|---|---|---|
| **Outer Diameter (mm)** | **$15.20 \pm 0.05\ \text{mm}$** | **$15.20 \pm 0.05\ \text{mm}$** | Meets KS/ASTM ($100\%$) |
| **Cross-Sectional Area ($A_p$, $\text{mm}^2$)** | **$138.7\ \text{mm}^2$** | **$138.5\ \text{mm}^2$** | Meets standard |
| **Breaking Load ($P_u$, kN)** | **$260.0 \sim 270.0\ \text{kN}$** | **$265.5 \pm 3.5\ \text{kN}$** | Exceeds requirement ($\ge 260\ \text{kN}$) |
| **Tensile Modulus ($E_p$, GPa)** | **$195.0 \pm 5.0\ \text{GPa}$** | **$193.5 \pm 4.0\ \text{GPa}$** | Within range ($190\sim 205\ \text{GPa}$) |
| **Tension Error Rate (%)** | N/A (Load cell dependent) | **Within $\pm 1.20\%$** | Fully linear response |
| **EMI Immunity** | Vulnerable (Electrical sensors) | **Immune ($100\%$ Optical)** | Zero noise from lightning/cables |
| **2-Million-Cycle Fatigue Pass** | Pass | **Pass (Zero signal damage)** | Verified fatigue integrity |

### 2. Bragg wavelength shift and tendon tracking analysis
- **Temperature-strain compensation**: Paired with an unstrained reference FBG to compensate thermal wavelength drift ($-20\ ^\circ\text{C} \leftrightarrow +60\ ^\circ\text{C}$) to within $\pm 0.1\ \text{pm}$.
- **Detection of anchorage wedge slip**: Captured instantaneous prestress losses from $3\sim 6\ \text{mm}$ wedge seating slip at $0.1\ \text{kN}$ resolution.

- **Overall conclusion**: This landmark study proved that integrating FBG sensors into CFRP core wires of 15.2 mm PC strands preserves full 260 kN tensile capacity while providing long-term prestress force monitoring within 1.2 % error.

## Related Notes

- [[chan-2006-fiber-bragg-grating-sensors-bridge-shm]] — Review of fiber Bragg grating sensors for structural health monitoring of bridges.
- [[kim-2007-fbg-smart-tendon]] — Development of smart tendons with built-in FBG sensors.
- [[concrete-durability-and-service-life]] — Smart maintenance and SHM frameworks for concrete durability.
- [[high-strength-strain-hardening-composites]] — High-performance prestressed structural composites.
