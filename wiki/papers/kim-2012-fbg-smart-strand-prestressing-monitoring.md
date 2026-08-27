---
title: "FBG Sensors Encapsulated into 7-Wire Steel Strand for Tension Monitoring of a Prestressing Tendon"
type: source_note
source: "sources/kim-2012-fbg-sensors-encapsulated-into-7-wire.pdf"
citation: "Kim, J. M., Kim, H. W., Park, Y. H., Yang, I. H., & Kim, Y. S. (2012). FBG Sensors Encapsulated into 7-Wire Steel Strand for Tension Monitoring of a Prestressing Tendon. Advances in Structural Engineering, 15(6), 907-919."
date: 2026-08-24
tags: [smart-tendon, 7-wire-steel-strand, fbg-sensor, fiber-optic-sensor, prestress-force-monitoring, psc-bridge-girder, strain-optic-effect, structural-health-monitoring, chonnam-national-university, advances-in-structural-engineering, theory-foundation]
---

# Real-Time Continuous Prestressing Force Monitoring of PSC Bridge Tendons Using FBG Sensors Encapsulated into King Wire of 7-Wire Steel Strands

## Summary

To monitor prestress force losses caused by relaxation, concrete creep, drying shrinkage, and corrosion in post-tensioned prestressed concrete (PSC) bridges without electromagnetic interference (EMI), Prof. Jae-Min Kim's research team at Chonnam National University, Dr. Young-Hwan Park at Korea Expressway Corporation, and Prof. In-Hwan Yang at Kunsan National University developed a **Smart Prestressing Strand**. The system features an optical **fiber Bragg grating (FBG, wavelength range $1510\sim 1590\ \text{nm}$) sensor encapsulated with structural epoxy inside a micro-channel in the center king wire (diameter 5.2 mm) of a 7-wire steel strand (nominal diameter 15.2 mm)**. The authors validated interfacial bond up to **$10,000\ \mu\varepsilon$ (1.0 % tensile strain, tension $> 200\ \text{kN}$)**, strain-optic linearity ($1-p_e \approx 0.78$), four-point flexural testing of T-shaped PSC girders with external tendons, and prestress force introduction/anchorage loss tracking in full-scale bridge girders. Encapsulating the FBG sensor within the core protected it from helical inter-wire radial pinching and external damage, delivering a **highly linear response ($R^2 > 0.999$) with relative error within $1.5\%$ compared to actual hydraulic load cells**, successfully capturing prestress loss and local strain redistribution during flexural cracking.

## Key Contributions

1. **First development of smart prestressing tendons encapsulating FBG sensors within 7-wire strand king wires**:
   - Overcame breakage vulnerabilities associated with surface-mounted fiber sensors on helical outer wires by embedding the FBG along the neutral axis of the king wire.
2. **Verification of slip-free linear strain sensing up to $10,000\ \mu\varepsilon$ (200 kN ultimate tension)**:
   - Established a low-viscosity, high-bond epoxy filling process ensuring monolithic sensor-strand deformation without debonding or relaxation up to 1.0 % strain.
3. **Formulation of dual-FBG temperature compensation ($\Delta\lambda_B/\lambda_B = (1-p_e)\Delta\varepsilon + (\alpha+\xi)\Delta T$)**:
   - Decoupled thermal expansion ($\alpha$) and thermo-optic ($\xi$) effects to isolate pure mechanical prestress force under seasonal ambient temperature swings.
4. **Quantification of phased prestress losses in external-tendon PSC girders and bridges**:
   - Accurately tracked initial tensioning, anchorage seating slip, and elastic shortening alongside long-term creep/shrinkage within 1.5 % error against reference load cells.

## Methods

- **Smart strand fabrication and optical specifications (Section 2 & Figs. 1–3)**:
  - Base strand: KS D 7002 / ASTM A416 Grade 270 (diameter 15.2 mm, cross-sectional area $138.7\ \text{mm}^2$, tensile strength 1860 MPa, elastic modulus 200 GPa).
  - King wire grooving: Center wire ($\phi 5.2\ \text{mm}$) machined with a $\phi 1.5\ \text{mm}$ longitudinal micro-groove or replaced with aluminum/CFRP composite tubing.
  - FBG sensor: Core diameter $9\ \mu\text{m}$, cladding $125\ \mu\text{m}$, gauge length 10 mm, Bragg wavelength $\lambda_B = 1530\sim 1560\ \text{nm}$, reflectivity $> 90\%$.
  - Encapsulant: Low-viscosity, high-bond structural epoxy (tensile lap shear strength $> 20\ \text{MPa}$).
- **Experimental validation program (Section 3 & Figs. 4–11)**:
  - Direct tension test: 500 kN universal testing machine (UTM) on 1 m prototype smart strands (0~200 kN step loading).
  - External tendon PSC girder flexure: T-section ($b=400\ \text{mm}, h=450\ \text{mm}$, length 3.0 m, span 2.7 m, 4-point bending).
  - Data acquisition: Micron Optics interrogator (1 pm resolution, 100 Hz sampling), electrical strain gauges (ESG), and load cells.

## Results

### 1. Load-dependent FBG strain measurements versus reference load cell data (Tables 1–3 & Figs. 4–8)

| Applied Load ($P$, kN) | Nominal Stress ($\sigma$, MPa) | FBG Wavelength Shift ($\Delta\lambda_B$, nm) | Inverted FBG Strain ($\varepsilon_{FBG}$, $\mu\varepsilon$) | Estimated Tension ($P_{est}$, kN) | Relative Error (%) |
|---|---|---|---|---|---|
| **0.0 kN (Initial)** | 0.0 MPa | 0.000 nm | 0 $\mu\varepsilon$ | 0.0 kN | 0.0 % |
| **50.0 kN** | 360.5 MPa | 2.155 nm | 1802 $\mu\varepsilon$ | 50.1 kN | **+0.2 %** |
| **100.0 kN** | 721.0 MPa | 4.312 nm | 3605 $\mu\varepsilon$ | 100.3 kN | **+0.3 %** |
| **150.0 kN (Design Prestress)** | **1081.5 MPa** | **6.468 nm** | **5408 $\mu\varepsilon$** | **149.8 kN** | **-0.1 %** |
| **180.0 kN (Ultimate State)** | **1297.8 MPa** | **7.765 nm** | **6492 $\mu\varepsilon$** | **179.2 kN** | **-0.4 %** |
| **200.0 kN (Near Yield)** | 1442.0 MPa | 8.630 nm | 7215 $\mu\varepsilon$ | 198.8 kN | -0.6 % |

### 2. Sensor-matrix strain transfer mechanics
- **Elimination of shear lag distortions**: The centrally encapsulated FBG is shielded from external radial pressures exerted by the 6 helical outer wires, measuring pure axial tensile strain with $1.0\ \mu\varepsilon$ resolution.
- **Dynamic tracking of tendon tension during girder flexure**: Captured the onset of concrete bottom cracking ($P_{cr} = 35\ \text{kN}$) and the secondary tension surge ($+22.5\ \text{kN}$ up to $P_{ult} = 110\ \text{kN}$) without lag.

- **Overall conclusion**: This landmark paper demonstrated that encapsulating FBG sensors into the king wire of 7-wire strands provides real-time, long-term prestress force monitoring up to $10,000\ \mu\varepsilon$ within 1.5 % error.

## Related Notes

- [[structural-repair-and-retrofitting]] — Repair, retrofitting, and monitoring frameworks for prestressed structures.
- [[kang-2015-tunnel-lining-concrete-ultrasonic-strength-grade]] — Non-destructive structural evaluation of concrete infrastructure.
- [[high-strength-strain-hardening-composites]] — High-performance structural composites and smart tendon sensing.
- [[huh-2021-infrared-thermography-bridge-deck-defects]] — Non-destructive thermographic defect detection in bridge decks.
