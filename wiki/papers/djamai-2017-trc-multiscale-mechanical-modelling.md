---
title: "Textile reinforced concrete multiscale mechanical modelling: Application to TRC sandwich panels"
type: source_note
source: "sources/djamai-2017-textile-reinforced-concrete-multiscale-mechanical.pdf"
citation: "Djamai, Z. I., Bahrar, M., Salvatore, F., Si Larbi, A., & El Mankibi, M. (2017). Textile reinforced concrete multiscale mechanical modelling: Application to TRC sandwich panels. Finite Elements in Analysis and Design, 135, 22-35."
date: 2026-08-23
tags: [textile-reinforced-concrete, trc, multiscale-modelling, cohesive-friction-law, bond-slip, sandwich-panels, finite-element-method, theory-foundation]
---

# Cohesive-Friction Multiscale Mechanical Modeling of Textile Reinforced Concrete (TRC) and Flexural Failure Analysis of Sandwich Panels

## Summary

To predict the coupled failure mechanisms (matrix multiple cracking, yarn-matrix interfacial cohesive debonding, Coulomb frictional pullout, and yarn rupture) of textile reinforced concrete (TRC)—incorporating carbon and alkali-resistant glass fiber grids within fine cementitious matrices—and lightweight insulating sandwich panels clad with TRC facings, Professor Amir Si Larbi and co-workers at the Université de Lyon / ENISE established a three-stage multiscale finite element (FE) computational framework linking micro-scale (single yarn pullout), meso-scale (TRC coupon uniaxial tension), and macro-scale (TRC-insulation sandwich panel four-point bending). The study developed a three-stage cohesive-friction bond-slip constitutive law rigorously separating cohesive damage from matrix drying shrinkage-induced Coulomb friction ($\tau_f = 1.3\ \text{MPa}$) and implemented an inverse analysis technique to identify interfacial parameters directly from tensile load-CMOD curves, capturing nonlinear flexural load-deflection responses and multiple shear cracking patterns within 5 % error.

## Key Contributions

1. **Establishment of a three-phase interfacial bond-slip law separating cohesion and Coulomb friction**:
   - **Phase I (Elastic contact)**: Linear stress transfer driven by initial interfacial shear stiffness $K_0$ ($\tau = K_0 \delta$).
   - **Phase II (Cohesive damage)**: Softening response governed by damage variable $D$ upon reaching cohesive strength $\tau_{max}$ ($\tau = (1-D)K_0 \delta$).
   - **Phase III (Pure frictional sliding)**: Constant residual frictional shear resistance governed by matrix shrinkage pressure ($P = E \varepsilon_{shrink}$) and friction coefficient ($\mu$) after complete debonding ($D=1$) ($\tau_f = \mu P = 1.3\ \text{MPa}$).
2. **Establishment of an inverse identification method for interfacial parameters based on tensile fracture**:
   - Accurately back-calculated Mode II cohesive fracture energy ($G_{IIc} = 0.45\ \text{N/mm}$) and peak bond strength ($\tau_{max} = 3.2\ \text{MPa}$) from the pullout branch of TRC direct tension tests.
3. **Computational structural validation on TRC insulated sandwich panels**:
   - Applied the multiscale framework to four-point bending tests of sandwich panels composed of an expanded polystyrene (EPS) core and two 10 mm-thick carbon TRC facings, predicting multiple tensile cracking in facings and shear deformation in the core.

## Methods

- **Material properties and TRC configurations (Tables 1 & 2)**:
  - Matrix: Self-consolidating high-flow fine mortar (CEM I 52.5, W/B = 0.35, micro-silica sand $d_{max} = 1.0\ \text{mm}$, 28-day compressive strength 55 MPa, elastic modulus 28 GPa, tensile strength 4.2 MPa).
  - Reinforcing textile: 2D orthogonal carbon fiber grid (grid spacing $10\ \text{mm} \times 10\ \text{mm}$, yarn cross-sectional area $0.45\ \text{mm}^2$, tensile strength 1800 MPa, elastic modulus 230 GPa).
  - Core material: Expanded polystyrene (EPS) insulation (thickness 80 mm, density $25\ \text{kg/m}^3$, elastic modulus 5.2 MPa, shear modulus 2.1 MPa).
- **Multiscale finite element modeling framework (ABAQUS Implicit)**:
  - Micro/meso model: Cement matrix (3D solid C3D8R, Concrete Damaged Plasticity) + fiber yarn (truss T3D2 or solid) + interface (cohesive surface contact with Coulomb friction, Eqs. 1–2).
  - Shrinkage pressure simulation: Equivalent shrinkage strain ($\varepsilon_{shrink}$) applied to the matrix to induce confining pressure ($P$) onto yarn surfaces.
- **Experimental validation program**:
  - Double-sided yarn pull-out tests.
  - TRC coupon uniaxial tension tests ($500\ \text{mm} \times 60\ \text{mm} \times 10\ \text{mm}$, displacement control at $0.5\ \text{mm/min}$, DIC CMOD measurement).
  - TRC sandwich panel four-point bending tests ($1200\ \text{mm} \times 300\ \text{mm} \times 100\ \text{mm}$, clear span 1000 mm).

## Results

### 1. Interfacial properties identified from single-yarn and TRC tension inverse analysis

| Interface model parameter | Symbol and units | Calibrated and inverse-identified value | Physical significance and effect |
|---|---|---|---|
| **Initial shear bond stiffness** | $K_0$ ($\text{MPa/mm}$) | **125.0 ± 5.0** | Chemical adhesion and initial elastic shear resistance |
| **Peak cohesive shear strength** | $\tau_{max}$ (MPa) | **3.20 ± 0.15** | Critical threshold for interfacial micro-debonding |
| **Mode II cohesive fracture energy** | $G_{IIc}$ (N/mm) | **0.45 ± 0.03** | Energy dissipated during complete cohesive debonding |
| **Shrinkage-induced confining pressure** | $P$ (MPa) | **4.33 ± 0.20** | Clamping stress from autogenous and drying shrinkage |
| **Coulomb friction coefficient** | $\mu$ (-) | **0.30 ± 0.02** | Sliding friction coefficient after debonding |
| **Final residual frictional shear stress** | $\tau_f$ (MPa) | **1.30 ± 0.08** | $\tau_f = \mu P$, post-debonding sustained capacity |

### 2. Sandwich panel four-point bending simulations versus experimental validation
- **Load-deflection curve agreement**: Predicted the entire structural response within **4.2 % error**, including initial elastic stage, multiple microcracking propagation in facings ($P = 4.5\sim 7.2\ \text{kN}$), EPS core shear yielding, and peak capacity ($P_{max} = 9.8\ \text{kN}$, deflection 22.5 mm).
- **Crack pattern reproduction**: Numerically captured regular multiple microcracks matching the 10 mm grid spacing in the bottom tension facing and delayed compressive crushing in the top facing.

- **Overall conclusion**: The multiscale cohesive-friction model provides a computational framework connecting micro-scale yarn pullout mechanisms to the structural flexural design of large-scale TRC sandwich panels.

## Related Notes

- [[fiber-bridging-constitutive-law]] — Fiber-matrix interfacial bond-slip ($\tau-\delta$) constitutive laws.
- [[strain-hardening-mechanism]] — Multiple cracking and strain-hardening analysis in fiber composites.
- [[ding-2019-optimal-interfacial-bond-fiber-rupture-hdcc]] — Optimal interfacial bond strength and fiber rupture mechanics theory.
- [[structural-repair-and-retrofitting]] — Thin-section repair and retrofitting structural analysis using TRC.
