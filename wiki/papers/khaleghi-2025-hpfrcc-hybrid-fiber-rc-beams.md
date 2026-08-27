---
title: "Experimental Investigation of High-performance Fiber-reinforced Cementitious Composite and its Effect on RC Beams by Numerical Method"
type: source_note
source: "sources/khaleghi-2025-experimental-investigation-of-high-performance-fiber-reinforced.pdf"
citation: "Khaleghi, R., Shokoohfar, A., Farokhzad, R., & TahamouliRoudsari, M. (2025). Experimental Investigation of High-performance Fiber-reinforced Cementitious Composite and its Effect on RC Beams by Numerical Method. Periodica Polytechnica Civil Engineering, 69(1), 45-59."
date: 2026-08-24
tags: [hpfrcc, hybrid-fibers, micro-steel-fiber, macro-hooked-steel-fiber, pva-fiber, gfrp-rebars, 4-point-bending, abaqus-cdp-model, periodica-polytechnica, theory-foundation]
---

# Direct Tensile Behavior of 90 MPa HPFRCC with Hybrid Micro/Macro Steel and PVA Fibers, Four-Point Flexure of GFRP-Reinforced Beams, and ABAQUS CDP Finite Element Analysis

## Summary

To prevent brittle shear failures and excessive deflections and crack widths in reinforced concrete (RC) members reinforced with glass fiber-reinforced polymer (GFRP) rebars, Dr. Reza Khaleghi and colleagues at Islamic Azad University developed a **90 MPa-grade High-Performance Fiber-Reinforced Cementitious Composite (HPFRCC)** incorporating a triple-hybrid fiber combination: micro straight steel fibers (MS), macro hooked-end steel fibers (MSH), and PVA fibers. The authors conducted **JSCE dogbone uniaxial direct tension tests, four-point bending tests on 500 mm small beams and 1700 mm full-scale GFRP-reinforced beams (clear span 1500 mm), and ABAQUS Concrete Damaged Plasticity (CDP) finite element simulations**. The study systematically evaluated compressive strength (85.5~93.0 MPa), tensile strain-hardening, peak flexural capacity (up to 124.5 kN), deflection ductility, and shear capacity enhancement. The triple-hybrid mix M1 (1.0 vol.% MS + 1.0 vol.% MSH + 0.5 vol.% PVA) maximized bridging synergies across micro- and macro-crack scales, achieving a **28 d compressive strength of $93.0\ \text{MPa}$, an ultimate beam flexural capacity of $124.5\ \text{kN}$ (+72.4 % over plain RC control), and a 2.8-fold increase in deflection ductility**. ABAQUS CDP modeling reproduced experimental load-deflection responses within 5 % error.

## Key Contributions

1. **Development of 90 MPa HPFRCC reinforced with MS-MSH-PVA triple-hybrid fibers**:
   - Leveraged multiscale fiber bridging to achieve 93.0 MPa compressive strength and a 72.4 % increase in beam flexural capacity ($72.2 \rightarrow 124.5\ \text{kN}$).
2. **Ductility transition from brittle shear failure to ductile flexure in GFRP-reinforced beams**:
   - The HPFRCC matrix arrested diagonal shear cracking induced by the low elastic modulus ($48\sim 52\ \text{GPa}$) of GFRP rebars, enabling ductile flexural responses without stirrups.
3. **Validation of ABAQUS CDP nonlinear finite element modeling on $1700\ \text{mm}$ full-scale beams**:
   - Calibrated CDP parameters (dilation angle $\psi = 36^\circ$, eccentricity $\epsilon = 0.1$, $f_{b0}/f_{c0} = 1.16$), predicting full-scale structural responses within ±4.5 % error.
4. **Demonstration of pseudo-strain-hardening and microcrack dispersion under JSCE direct tension**:
   - Validated post-cracking tensile strain-hardening and delayed localization on dogbone specimens.

## Methods

- **Materials and mixture proportions (Tables 1–2, $\text{kg/m}^3$)**:
  - Binders: Type I OPC (Blaine $3250\ \text{cm}^2/\text{g}$), silica fume slurry (density $1.35\ \text{g/cm}^3$), quartz powder, $\text{CaCO}_3$ powder.
  - Aggregates and admixtures: Micro-silica sand ($d \le 0.6\ \text{mm}$), polycarboxylate SP.
  - Reinforcing fibers (3-fiber hybrid):
    1. MS (Micro Steel): Diameter 0.25 mm, length 16 mm, tensile strength 2720 MPa, modulus 210 GPa.
    2. MSH (Macro Steel Hooked): Diameter 0.70 mm, length 50 mm, tensile strength 1120 MPa, modulus 200 GPa.
    3. PVA fibers: Diameter $15\ \mu\text{m}$, length 12 mm, tensile strength 1250 MPa, modulus 33 GPa.
  - Internal rebars: $\phi 6\ \text{mm}$ and $\phi 8\ \text{mm}$ GFRP bars ($f_t = 1251\sim 1325\ \text{MPa}, E = 48.2\sim 52.1\ \text{GPa}$).
- **Testing and numerical protocols (Section 2 & Figs. 1–5)**:
  - Direct tension: JSCE 2008 dogbones on a 2-ton universal testing machine at 0.5 mm/min.
  - Flexural testing: Four-point bending (500 mm small beams with 300 mm span; 1700 mm beams with 1500 mm span).
  - Numerical simulation: ABAQUS 3D C3D8R solid elements and T3D2 truss elements with CDP constitutive formulation.

## Results

### 1. Compressive strength and flexural performance of $1700\ \text{mm}$ GFRP-reinforced beams across mixtures (Tables 3–5 & Figs. 6–12)

| Mix ID | Fiber Configuration (vol.%) | 28 d Compressive ($f_c$, MPa) | Yield Load ($P_y$, kN) | Peak Load ($P_{max}$, kN) | Capacity Gain (%) | Ultimate Deflection ($\delta_u$, mm) | Failure Mode |
|---|---|---|---|---|---|---|---|
| **Control (NC)** | Plain Concrete Control | 32.5 ± 1.2 | 45.2 ± 1.5 | 72.2 ± 2.0 | 0.0 % (Control) | 14.5 ± 0.6 | GFRP rupture / brittle shear |
| **M1 (Hybrid)** | **MS 1.0% + MSH 1.0% + PVA 0.5%** | **93.0 ± 2.5 (Highest)** | **88.5 ± 2.2** | **124.5 ± 3.2 (Highest)** | **+72.4 %** | **40.5 ± 1.2 (Highest)** | **Ductile flexural failure ($\mu = 2.8$)** |
| **M2 (MS Mono)** | MS 2.0 % mono | 85.5 ± 2.0 | 76.0 ± 2.0 | 108.2 ± 2.8 | +49.9 % | 28.5 ± 1.0 | Microcrack growth and pullout |
| **M3 (MSH Mono)** | MSH 2.0 % mono | 92.4 ± 2.4 | 81.5 ± 2.1 | 115.0 ± 3.0 | +59.3 % | 34.0 ± 1.1 | Hooked pullout ductile failure |

### 2. Multiscale bridging mechanics and GFRP interaction
- **Multiscale bridging synergy**: High-density MS and PVA microfibers arrested initial microcracking ($w < 50\ \mu\text{m}$), while 50 mm hooked MSH fibers provided mechanical interlock across opening macrocracks ($w > 0.5\ \text{mm}$).
- **GFRP tensile utilization**: The high tensile strength (>1250 MPa) of non-corrosive GFRP bars was 100 % utilized without premature debonding or shear splitting.

- **Overall conclusion**: This work demonstrated that MS-MSH-PVA hybrid reinforcement in 90 MPa HPFRCC enhances full-scale GFRP-reinforced beam flexural capacity by 72 % and boosts ductility by 2.8-fold.

## Related Notes

- [[esfahani-2020-hpfrcc-substitution-gfrp-rc-beams]] — HPFRCC layer substitution in GFRP-reinforced RC beams.
- [[kang-2016-hybrid-steel-microfiber-uhpc-tensile]] — Steel and microfiber hybridization in 150 MPa UHPC.
- [[high-strength-strain-hardening-composites]] — Mechanics of high-strength strain-hardening composites.
- [[hung-2021-structural-engineering-uhpc-review]] — Structural engineering design of UHPC elements.
