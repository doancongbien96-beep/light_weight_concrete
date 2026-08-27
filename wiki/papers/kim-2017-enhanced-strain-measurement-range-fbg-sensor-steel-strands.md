---
title: "Enhanced Strain Measurement Range of an FBG Sensor Embedded in Seven-Wire Steel Strands"
type: source_note
source: "sources/kim-2017-enhanced-strain-measurement-range-of.pdf"
citation: "Kim, J.-M., Kim, C.-M., Choi, S.-Y., & Lee, B. Y. (2017). Enhanced Strain Measurement Range of an FBG Sensor Embedded in Seven-Wire Steel Strands. Sensors, 17(7), 1654."
date: 2026-08-24
tags: [fbg-sensor, optical-fiber-sensors, smart-pc-strand, strain-measurement-range-enhancement, large-strain-monitoring, prestressed-concrete, bang-yeon-lee, jae-min-kim, sensors-journal, landmark-paper]
---

# Large Strain ($\varepsilon \ge 3.0\% = 30,000\ \mu\varepsilon$) Measurement Range Extension for Optical Fiber FBG Sensors Embedded in 7-Wire Steel Strands: Slip Buffer Mechanism for Ultimate Rupture Monitoring

## Summary

Standard silica optical fiber Bragg grating (FBG) sensors have an intrinsic rupture strain limit ($\approx 1.0\% = 10,000\ \mu\varepsilon$). Consequently, they break prematurely during the yielding and plastic deformation stages ($\varepsilon > 2.0\sim 3.5\%$) of prestressed concrete (PSC) steel strands, leaving pre-collapse structural behaviors unmonitored. To overcome this limitation, Prof. Jae-Min Kim and Prof. Bang Yeon Lee (corresponding author) at Chonnam National University developed a **large-strain smart PC strand incorporating a controlled slip buffer mechanism (strain reduction factor $\kappa = 0.35$)** inside a hollow king wire rather than bonding the optical fiber entirely with rigid epoxy. Uniaxial tensile rupture testing ($260\ \text{kN}$ ultimate load), cyclic tendon tensioning, and strain transfer calibration demonstrated that this packaging mechanism prevents premature fiber rupture while maintaining linear measurement precision (correlation coefficient $R^2 \ge 0.999$) well into the plastic rupture regime beyond $3.0\%$ ($30,000\ \mu\varepsilon$).

## Key Contributions

1. **3-fold expansion of FBG strain measurement capacity ($1.0\% \rightarrow 3.0\%$)**:
   - Developed an encapsulation mechanism enabling real-time monitoring of strand plastic elongation up to $30,000\ \mu\varepsilon$ without glass fiber failure.
2. **Formulation of slip buffer and strain transfer coefficient ($\kappa = 0.35$)**:
   - Established a proportional transfer equation ($\varepsilon_{FBG} = \kappa \cdot \varepsilon_s$) relating strand strain ($\varepsilon_s$) to actual optical fiber strain ($\varepsilon_{FBG}$) within $1.5\%$ error.
3. **Real-time sensing of seismic and ultimate pre-collapse plastic deformation in PSC structures**:
   - Retained tracking of residual prestress force and plastic hinge rotation under extreme overload conditions where conventional sensors fail.
4. **Complete protection against friction during strand anchorage and tensioning**:
   - The hollow steel king wire provided 100 % isolation from severe localized shear forces exerted by wedge grips.

## Methods

- **Large-strain FBG sensor structural design (Section 2 & Figs. 1–4)**:
  - Hollow king wire: Specially machined steel tubing (outer diameter $5.35\ \text{mm}$, inner diameter $2.0\ \text{mm}$).
  - Sensor embedment: FBG gauge length $10\ \text{mm}$, dual-end epoxy anchorage spacing $L_g = 150\ \text{mm}$, intermediate slip-buffering sleeve.
  - Bragg wavelength formulation:
    $$\Delta\lambda_B / \lambda_B = (1 - P_e) \cdot \kappa \cdot \Delta\varepsilon_s + (\alpha + \xi) \Delta T$$
- **Tensile testing and strain calibration (Sections 3–4 & Figs. 5–9)**:
  - Direct tensile rupture testing on a 1000 kN universal testing machine ($0\sim 30,000\ \mu\varepsilon$).
  - Simultaneous multi-channel validation using electrical strain gauges (ESG), optical LVDTs, and load cells.

## Results

### 1. Strain measurement range, linearity, and rupture performance across sensor configurations (Section 3 & Tables 1–3 & Figs. 10–14)

| Sensor System Configuration | Maximum Measurement Strain ($\varepsilon_{max}$, $\mu\varepsilon$) | Linearity Correlation ($R^2$) | Strand Yield ($14,000\mu\varepsilon$) Tracked | Strand Rupture ($30,000\mu\varepsilon$) Tracked | Sensor Integrity at Ultimate |
|---|---|---|---|---|---|
| **Surface-Mounted FBG** | **$8,500 \pm 500\ \mu\varepsilon$ ($0.85\%$)** | $0.9980$ | No (Premature break) | No (Fractured) | Broken near $9,000\mu\varepsilon$ |
| **Direct-Embedded FBG (Fully bonded)** | $11,000 \pm 800\ \mu\varepsilon$ ($1.10\%$) | $0.9985$ | Incomplete (Near break) | No (Fractured) | Broken near $11,500\mu\varepsilon$ |
| **Slip-Buffered FBG (Optimal)** | **$>32,000\ \mu\varepsilon$ ($>3.20\%$, $3\times$)** | **$0.9995$ (Fully linear)** | **Yes (100 % verified)** | **Yes (100 % real-time)** | **Intact through full strand rupture** |

### 2. Strain transfer mechanics and pre-collapse warning
- **Accurate tracking of post-yield plastic deformation**: As the strand deformed beyond elasticity to its $1860\ \text{MPa}$ ultimate strength, the slip buffer distributed stress concentrations, keeping fiber strains below $10,000\ \mu\varepsilon$.
- **Real-time early warning capabilities**: Provides quantitative reserve safety margins prior to cable rupture or girder plastic collapse.

- **Overall conclusion**: This landmark paper demonstrated that integrating a slip buffer mechanism extends FBG strain measurement capacity to 30,000 με (over 3.0%), enabling real-time structural monitoring up to full strand rupture.

## Related Notes

- [[kim-2015-sensor-type-pc-strand-embedded-fbg-sensor]] — Development of smart PC strands with embedded FBG sensors.
- [[chan-2006-fiber-bragg-grating-sensors-bridge-shm]] — Classic review of fiber optic Bragg grating sensors for bridge SHM.
- [[concrete-durability-and-service-life]] — Smart maintenance and structural health monitoring frameworks.
- [[high-strength-strain-hardening-composites]] — Prestressed structural composite engineering.
