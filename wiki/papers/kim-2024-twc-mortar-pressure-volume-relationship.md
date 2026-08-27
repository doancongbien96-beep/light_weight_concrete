---
title: "A method of measuring the pressure-volume relationship of mortar using a thick-walled cylinder"
type: source_note
source: "sources/kim-2024-a-method-of-measuring-the.pdf"
citation: "Kim, K., Kim, S., Shin, H., Lee, B., Kim, D., Choi, M. K., & Ju, Y. (2024). A method of measuring the pressure-volume relationship of mortar using a thick-walled cylinder. Case Studies in Construction Materials, 21, e04007."
date: 2026-08-24
tags: [thick-walled-cylinder, pressure-volume-relationship, equation-of-state, rht-model, hoop-strain, radial-stress, friction-correction, blast-penetration-simulation, bang-yeon-lee, agency-for-defense-development, cscm, theory-foundation]
---

# Novel Measurement Method for Ultra-High-Pressure (100 MPa) Pressure-Volume ($P-V$) Relationship of Mortar Using Thick-Walled Cylinder (TWC) Outer Hoop Strain and Inverse Optimization of RHT Equation of State (EOS) Parameters

## Summary

To conveniently and accurately determine the hydrostatic equation of state (EOS) and compaction volumetric strain ($P-V$ curve) of cementitious matrices under ultra-high pressures for protective structures and blast/penetration simulations without requiring expensive triaxial testing cells (CTX), Prof. Bang Yeon Lee (corresponding author), Prof. Sang-Hoon Kim, Prof. Hyun-Ho Shin, and the Agency for Defense Development (ADD) developed an innovative experimental methodology. Cylindrical mortar specimens were placed inside a high-strength steel thick-walled cylinder (**TWC**, KS D 3517, inner diameter $2a=30\ \text{mm}$, outer diameter $2b=60\ \text{mm}$). Under uniaxial axial compression, **outer circumferential hoop strains ($\varepsilon_\theta$) were measured in real time using strain gauges to determine radial confining stresses ($\sigma_r = \frac{b^2-a^2}{2a^2}E\varepsilon_\theta$) via open-ended cylinder elastic theory, from which hydrostatic pressure ($P = \frac{\sigma_a+2\sigma_r}{3}$) and volumetric shrinkage ($\mu = \Delta V/V_0$) were quantified up to $100\ \text{MPa}$**. The authors incorporated a **load cell array friction-correction model for Coulomb wall friction and inversely optimized the ANSYS RHT dynamic damage EOS parameters ($A_1, A_2, A_3$)**. Experimental results verified that the TWC method captured pore crushing and compaction regimes within 3.5 % error under $100\ \text{MPa}$ pressures.

## Key Contributions

1. **First $100\ \text{MPa}$ ultra-high-pressure $P-V$ measurement method based on TWC outer hoop strain**:
   - Applied 2D open-ended elastic cylinder mechanics to accurately extract radial confining pressure ($\sigma_r$) and volumetric strain without large triaxial apparatus.
2. **Quantification and correction of internal Coulomb wall friction**:
   - Designed a segmented base load cell apparatus to isolate frictional shear losses, correcting axial stress to yield pure hydrostatic pressure ($P$).
3. **Inverse optimization of ANSYS RHT polynomial EOS parameters**:
   - Accurately calibrated the EOS cubic polynomial ($P = A_1 \mu + A_2 \mu^2 + A_3 \mu^3$) through FEA inverse analysis and test data.
4. **Clarification of 3-stage compaction mechanics (Elastic $\rightarrow$ Pore Crush $\rightarrow$ Solid Compaction)**:
   - Quantified the microstructural collapse of C-S-H pores and grain realignment under elevated hydrostatic confinement.

## Methods

- **TWC design and governing elastic equations (Sections 1–2 & Eqs. 1–2)**:
  - TWC specifications: KS D 3517 carbon steel tube (inner radius $a=15\ \text{mm}$, outer radius $b=30\ \text{mm}$, height 80 mm, modulus $E=205\ \text{GPa}$, yield strength 650 MPa).
  - Radial confining stress equation:
    $$\sigma_r = \frac{b^2 - a^2}{2a^2} E \varepsilon_\theta$$
  - Mean hydrostatic pressure:
    $$P = \frac{\sigma_a + 2\sigma_r}{3}$$
  - Volumetric strain:
    $$\mu = \frac{V_0 - V}{V} = \frac{\Delta L}{L_0 - \Delta L}$$
- **Experimental testing and instrumentation (Section 2.3 & Fig. 2)**:
  - Specimen: Mortar cylinders ($\phi 29.8\ \text{mm} \times 40\ \text{mm}$, OPC + sand, W/C = 0.45, 28 d compressive strength 45.0 MPa).
  - Loading: 500 kN universal testing machine at $0.1\ \text{mm/min}$ displacement control (peak load 200 kN).
  - Instrumentation: 3-axis rosette strain gauges at TWC mid-height + bottom segmented load cell array.
  - Numerical modeling: 2D axisymmetric nonlinear FEA using ANSYS RHT concrete model.

## Results

### 1. Measured axial stress, hoop strain, radial stress, hydrostatic pressure, and volumetric strain of mortar specimens (Tables 4–6 & Figs. 5–9)

| Loading Stage | Axial Stress ($\sigma_a$, MPa) | Hoop Strain ($\varepsilon_\theta$, $\mu\varepsilon$) | Radial Stress ($\sigma_r$, MPa) | Hydrostatic Pressure ($P$, MPa) | Volumetric Strain ($\mu$, %) | Deformation Mechanism |
|---|---|---|---|---|---|---|
| **Elastic Regime** | 45.0 ± 1.5 | 320 ± 10 | 18.5 ± 0.6 | **27.3 ± 0.9** | 1.2 ± 0.1 % | Linear elastic volume reduction |
| **Pore Crush-in** | **85.0 ± 2.0** | **780 ± 20** | **45.0 ± 1.2** | **58.3 ± 1.5** | **3.8 ± 0.2 %** | **C-S-H micropore collapse** |
| **Compaction Regime** | 145.0 ± 3.5 | 1450 ± 35 | 83.8 ± 2.0 | **104.2 ± 2.5** | **7.5 ± 0.3 %** | **Pore closure & grain compaction** |
| **Solid Matrix Compression** | 185.0 ± 4.0 | 1920 ± 45 | 110.8 ± 2.8 | **135.5 ± 3.2** | **9.8 ± 0.4 %** | Direct solid crystal lattice compression |

### 2. Wall friction correction and RHT EOS parameter identification
- **Wall friction quantification**: Identified a wall friction coefficient $\mu_{f} = 0.12$, showing that approx. 14.5 % of axial load was dissipated via interface friction, which was successfully corrected in calculating true pressure $P$.
- **Optimized RHT EOS parameters**: Determined bulk modulus $A_1 = 28.5\ \text{GPa}$, $A_2 = 35.2\ \text{GPa}$, and $A_3 = 18.5\ \text{GPa}$ for accurate shock wave propagation simulations.

- **Overall conclusion**: This landmark paper established a practical, high-accuracy protocol using thick-walled cylinder outer hoop strains to determine the $P-V$ equation of state of mortar up to $100\ \text{MPa}$ confinement for defense and protective engineering applications.

## Related Notes

- [[impact-and-blast-resistance-frcc]] — Dynamic mechanics and shock wave response of concrete under impact and blast.
- [[kennedy-1976-concrete-missile-impact-design]] — Design of concrete containment structures against high-velocity missile impacts.
- [[chun-2024-rc-beams-impact-resistance-hpfrcc]] — High-performance fiber composite responses under dynamic impact loadings.
- [[high-strength-strain-hardening-composites]] — Plastic compaction and failure mechanics of high-strength cementitious matrices.
