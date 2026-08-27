---
title: "Flexural performance of composite beam with high-strength steel girder and ECC slab: A comprehensive parametric study"
type: source_note
source: "sources/construction-2025-flexural-performance-of-composite-beam.pdf"
citation: "Mai, A. D., Lee, C. K., & Nguyen, C. L. (2025). Flexural performance of composite beam with high-strength steel girder and ECC slab: A comprehensive parametric study. Research on Engineering Structures and Materials, 11(3), 1345-1367."
date: 2026-08-23
tags: [composite-beam, high-strength-steel, hss-s690, hss-s960, ecc-slab, strain-incompatibility, flexural-ductility, parametric-fe-analysis, theory-foundation]
---

# Flexural Performance, Strain Compatibility, and a 136-Model FE Parametric Study of Composite Beams Coupling High-Strength Steel (S690/S960) Girders with ECC Slabs

## Summary

To fundamentally overcome the critical strain incompatibility that arises when high-strength steel (HSS: High-Strength Steel S690, S960) girders with yield strengths at the 690~960 MPa level are combined with ordinary concrete (NC) slabs — where the concrete crushes prematurely at 0.25~0.30 % before the higher yield strain of the HSS (0.35~0.48 %) is reached, leaving the plastic flexural capacity unrealized — this latest leading structural research paper by the research team of the University of Danang (Vietnam) and UNSW Canberra (Australia) proposes an HSS-ECC composite beam system coupling a slab of strain-hardening cement composite (ECC: compressive strength 40~120 MPa, tensile strain capacity 2~5 %) with ultra-high ductility and high compressive deformation capacity, and performs precise three-dimensional nonlinear finite element (FE) parametric analysis of 136 models based on ABAQUS Solid C3D8R elements. The results show that the ECC slab stably accommodates plastic compressive strains of 0.6 % or more in the top compression zone without brittle fragmentation, thereby driving the S690 and S960 ultra-high-strength steel girders to reach full plastic yielding and mobilizing capacities above 100 % of the theoretical plastic flexural moment ($M_{FE}/M_{ps} = 1.02\sim 1.15$). The flexural ductility index ($R = \delta_u/\delta_y$) is also greatly improved to **3.5 ~ 5.5**, and it is demonstrated that even under partial shear connection ($\eta = 0.42\sim 0.82$) longitudinal splitting cracks around the studs and premature shear drop are completely prevented.

## Key Contributions

1. **Complete resolution of the strain incompatibility between HSS and concrete**:
   - Ordinary concrete fails by premature crushing before the S690/S960 steel yields because of its ultimate compressive strain ($\varepsilon_{cu} \approx 0.003$) limit, whereas ECC sustains compressive strains of 0.006 or greater through fiber confinement, exploiting 100 % of the HSS ultimate strength.
2. **Construction of a 136-model three-dimensional nonlinear FE parametric database of composite beams**:
   - Fully quantifies flexural behavior across a wide range of structural variables: steel grade (S690 vs S960), ECC compressive strength ($40\sim 120\ \text{MPa}$), slab width and thickness, web slenderness ($h_w/t_w$), degree of shear connection ($\eta = 0.42\sim 1.0$), presence or absence of profiled steel sheeting (PSS).
3. **Maximization of the flexural ductility index ($R$) and energy dissipation capacity**:
   - While HSS-NC beams show brittle failure with $R < 2.0$, HSS-ECC composite beams exhibit excellent flexural ductility of $R = 3.5\sim 5.5$, demonstrating their suitability as seismic-resistant composite structures.
4. **Securing design safety under partial shear connection**:
   - Even with an economical stud arrangement at a degree of shear connection $\eta = 0.5$, the tensile bridging stress of the ECC prevents shear fracture at the stud shank and guarantees continuous load redistribution.

## Methods

- **Finite element modeling technique (ABAQUS, Fig. 1)**:
  - Steel girder, ECC slab, shear studs, high-strength bolts: three-dimensional 8-node reduced-integration solid elements (C3D8R).
  - Profiled steel sheeting (PSS): 4-node shell elements (S4R); reinforcement mesh: 2-node truss elements (T3D2).
  - Material nonlinear constitutive laws: steel (bilinear elasto-plasticity with isotropic hardening), ECC (compression damaged plasticity and uniaxial tensile strain-hardening model of Meng et al.).
  - Contact conditions: surface-to-surface frictional contact at the steel-ECC interface, Tie constraint at the stud shank, Embedded constraint for the reinforcement mesh.
- **Parametric analysis groups (136 models)**:
  - **Group 1 (108 models)**: S690 (54) and S960 (54) steel girders, ECC strengths (40, 60, 80, 100, 120 MPa), slab geometry variables.
  - **Group 2 (28 models)**: web thickness ($t_w = 6, 8, 10\ \text{mm}$), flange width ($b_f$), stud spacing ($s_{stud} = 80\sim 200\ \text{mm}$, $\eta = 0.42\sim 1.0$), solid slab vs PSS deck.
- **Evaluation metrics**:
  - Yield moment ($M_y$), ultimate moment ($M_u$), plastic moment ratio ($M_{FE}/M_{ps}$), flexural stiffness ($EI_0$), flexural ductility index ($R = \delta_u/\delta_y$).

## Results

### 1. Flexural performance of composite beams by steel grade and ECC strength (summary of Tables 3 & 4)

| Steel grade | ECC compressive strength ($f'_c$, MPa) | Degree of shear connection ($\eta$) | Flexural capacity ratio ($M_{FE}/M_{ps}$) | Initial flexural stiffness ($EI_0$, $\text{kN}\cdot\text{m}^2$) | Flexural ductility index ($R = \delta_u/\delta_y$) | Failure mode |
|---|---|---|---|---|---|---|
| **S690** | 40 MPa | 0.52 | **1.04** | 18,200 | 4.85 | Steel flange yielding + ECC compressive plastification |
| **S690** | 80 MPa | 0.68 | **1.12** | 21,500 | 4.20 | Fully plastic flexural yielding |
| **S690** | 120 MPa | 0.82 | **1.18** | 23,800 | 3.65 | High-strength flexural capacity mobilized |
| **S960** | 40 MPa | 0.42 | **1.01** | 18,500 | 5.20 | Successful attainment of 100 % plastic moment |
| **S960** | 80 MPa | 0.58 | **1.08** | 21,900 | 4.10 | Stable plastic flexural failure |
| **S960** | 120 MPa | 0.72 | **1.14** | 24,100 | 3.50 | Highest flexural capacity achieved |

### 2. Analysis of the influence of key structural variables

- **Plastic moment attainment ratio**: all 136 models recorded $M_{FE}/M_{ps} \ge 1.01$, verifying that with an ECC slab the plastic sectional capacity is fully mobilized at 100 % regardless of the steel grade (S690/S960).
- **Web thickness and slenderness**: increasing the web thickness from 6 mm to 10 mm raises the flexural stiffness by 11 %, but the plastic neutral axis (PNA) descends and the ductility index $R$ decreases by 14 %.
- **Slab form**: the difference in flexural capacity between solid ECC slabs and slabs cast on PSS deckplates is less than 2 %, so they behave very similarly and the construction-friendly deckplate method remains applicable.

- **Overall conclusion**: this paper demonstrates that combining high-strength steel (S690/S960) with ECC slabs is an ideal composite structural system that blocks premature concrete crushing at the source and draws out 100 % of the latent capacity of the high-strength steel, providing a key breakthrough for dead-load reduction and seismic-performance enhancement in super-tall buildings and long-span bridges.

## Related Notes

- [[chen-2024-ecc-layered-functionally-graded-impact]] — review of steel-concrete composite bridge decks.
- [[choi-2022-kagome-truss-composite-beams-flexure]] — flexural behavior of metal-truss/FRCC composite beams.
- [[chen-2018-ultra-high-ductility-cement-composite-curving]] — high-strength SHCC strengthening composite sections.
- [[uhpc-vs-ecc-design-space]] — design space of UHPC (ultra-high strength) vs ECC (ultra-high ductility) for composite structures.
- [[strain-hardening-mechanism]] — tensile strain-hardening and compressive ductility mechanisms of ECC.
