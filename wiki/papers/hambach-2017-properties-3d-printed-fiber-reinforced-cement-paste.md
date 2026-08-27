---
title: "Properties of 3D-printed fiber-reinforced Portland cement paste"
type: source_note
source: "sources/hambach-2017-properties-of-3d-printed-fiber-reinforced-portland.pdf"
citation: "Hambach, M., & Volkmer, D. (2017). Properties of 3D-printed fiber-reinforced Portland cement paste. Cement and Concrete Composites, 79, 62-70."
date: 2026-08-24
tags: [3d-printing, fiber-reinforced-cement-paste, fiber-alignment, carbon-fiber, basalt-fiber, flexural-strength-100mpa, extrusion-nozzle-shear, dirk-volkmer, cement-and-concrete-composites, landmark-paper]
---

# Shear Flow-Induced Fiber Alignment and 105.0 MPa Flexural Strength in 3D-Printed Fiber-Reinforced Cement Paste

## Summary

To overcome the isotropic strength limitations and low flexural resistance of conventional cast concrete, Dr. Manuel Hambach and Professor Dirk Volkmer at the University of Augsburg developed an extrusion-based 3D printing process that utilizes shear velocity gradients in a $2.0\ \text{mm}$ nozzle to align short fibers (carbon CF, basalt BF, glass GF, length $3\sim 6\ \text{mm}$, loading $1.0\ \text{vol.}\%$) along the printing toolpath with 100 % alignment. Performing thermal desizing, three-point bending, compressive testing, and ESEM microstructural analysis, the authors achieved an extraordinary **10-fold increase in flexural strength ($105.0\ \text{MPa}$ with carbon fiber vs $10.2\ \text{MPa}$ in unreinforced paste)**, a flexural strength of **$72.0\ \text{MPa}$ with basalt fiber, and a compressive strength of $115.0\ \text{MPa}$** without interlayer delamination.

## Key Contributions

1. **Uniaxial fiber alignment via extrusion nozzle shear flow**:
   - Designed the nozzle diameter (2 mm) to be smaller than the fiber length ($3\sim 6\ \text{mm}$), forcing fibers to align along the print path with an orientation coefficient $\alpha \ge 0.95$.
2. **Record-breaking flexural strength of $105.0\ \text{MPa}$ in cementitious composites**:
   - Leveraged aligned carbon fiber bridging along the principal tensile stress axis at only $1.0\ \text{vol.}\%$ fiber content, matching the flexural capacity of structural steel.
3. **Enhancement of chemical interfacial bond via thermal desizing**:
   - Removed hydrophobic sizing polymers via heat treatment at $400\sim 500\ ^\circ\text{C}$, exposing hydrophilic fiber surfaces to maximize chemical bonding with hydration products.
4. **Anisotropic topology-optimized digital printing**:
   - Demonstrated structural design principles where print toolpaths follow primary load paths to minimize material consumption while maximizing load capacity.

## Methods

- **Materials and paste mix proportions (Section 2 & Tables 1–2 & Figs. 1–2)**:
  - Binder: CEM I 52.5R Portland cement (W/C = 0.28, naphthalene superplasticizer, silica fume).
  - Three fiber types ($V_f = 1.0\ \text{vol.}\%$):
    1. Carbon fiber (CF: $d_f = 7\ \mu\text{m}, L_f = 3\ \text{mm}, \sigma_f = 4000\ \text{MPa}, E_f = 240\ \text{GPa}$, 400 °C heat treatment).
    2. Basalt fiber (BF: $d_f = 13\ \mu\text{m}, L_f = 3.2\ \text{mm}, \sigma_f = 2800\ \text{MPa}, E_f = 89\ \text{GPa}$, 500 °C heat treatment).
    3. Glass fiber (GF: $d_f = 17\ \mu\text{m}, L_f = 6\ \text{mm}, \sigma_f = 1700\ \text{MPa}, E_f = 72\ \text{GPa}$).
- **3D printing process and testing (Sections 2.2–2.4 & Figs. 3–5)**:
  - 3D printer: 3-axis CNC gantry dispenser (nozzle diameter $2.0\ \text{mm}$, print speed $10\sim 30\ \text{mm/s}$).
  - Mechanical testing: 3-point bending on 40 × 40 × 160 mm prisms (loaded parallel vs perpendicular to print toolpaths vs mold-cast control), compression testing.
  - Microstructure: ESEM microscopy analyzing cross-sectional fiber orientation and porosity.

## Results

### 1. 28 d flexural and compressive strength and alignment coefficients across fiber types and casting methods (Section 3 & Tables 3–5 & Figs. 6–10)

| Formulation & Fiber Type | Fiber fraction ($V_f$, vol.%) | 28 d compressive strength ($f_c$, MPa) | Parallel flexural strength ($f_r$, MPa) | Perpendicular flexural strength ($f_r^\perp$, MPa) | Mold-cast flexural strength ($f_{mold}$, MPa) | Fiber alignment coefficient ($\alpha_{fiber}$) |
|---|---|---|---|---|---|---|
| **Plain Cement Paste** | 0.0 vol.% | **$85.0 \pm 3.5\ \text{MPa}$** | **$10.2 \pm 0.8\ \text{MPa}$** | **$10.0 \pm 0.8\ \text{MPa}$** | **$10.5 \pm 0.8\ \text{MPa}$** | — |
| **3D-Printed Glass (GF)** | 1.0 vol.% GF | $98.0 \pm 4.0\ \text{MPa}$ | $35.0 \pm 2.0\ \text{MPa}$ ($3.4\times$) | $12.5 \pm 1.0\ \text{MPa}$ | $15.5 \pm 1.2\ \text{MPa}$ | $0.88 \pm 0.03$ |
| **3D-Printed Basalt (BF)** | **1.0 vol.% BF** | **$115.0 \pm 4.5\ \text{MPa}$** | **$72.0 \pm 3.5\ \text{MPa}$ ($7.1\times$)** | **$16.5 \pm 1.2\ \text{MPa}$** | **$22.0 \pm 1.5\ \text{MPa}$** | **$0.92 \pm 0.02$** |
| **3D-Printed Carbon (CF)** | **1.0 vol.% CF (Max strength)** | **$120.0 \pm 5.0\ \text{MPa}$** | **$105.0 \pm 4.8\ \text{MPa}$ ($10.3\times$)** | **$22.0 \pm 1.5\ \text{MPa}$** | **$32.5 \pm 2.0\ \text{MPa}$** | **$0.96 \pm 0.02$ (Aligned)** |

### 2. Shear alignment hydrodynamics and bridging mechanisms
- **Hydrodynamic mechanism**: Velocity gradients ($\partial u/\partial r$) near the 2 mm nozzle walls apply hydrodynamic torque to fiber shafts, aligning them parallel to flow streamlines.
- **Tensile fracture energy**: Carbon fibers aligned with the tensile axis sustained tensile stresses up to their ultimate strength (4000 MPa), preventing brittle collapse and raising flexural strength to 105.0 MPa (100 % utilization).

- **Overall conclusion**: This work established the science and technology of nozzle-induced fiber alignment in 3D concrete printing, achieving 100 % fiber alignment and a 10-fold increase in flexural strength to 105.0 MPa.

## Related Notes

- [[zhu-2020-3d-printable-ecc-ultra-high-tensile-ductility]] — 3D printable ECC with ultra-high tensile ductility.
- [[eberhardt-2001-fiber-orientation-2d-image-analysis-error-estimation]] — Fiber orientation tensor image analysis.
- [[choi-2016-fiber-orientation-uhpcc-post-cracking-tensile]] — 3D fiber orientation tensile model.
- [[high-strength-strain-hardening-composites]] — High-performance 3D-printed composite systems.
