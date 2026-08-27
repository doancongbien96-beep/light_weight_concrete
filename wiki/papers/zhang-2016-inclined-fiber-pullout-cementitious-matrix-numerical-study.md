---
title: "Inclined Fiber Pullout from a Cementitious Matrix: A Numerical Study"
type: source_note
source: "sources/materials-09-00800.pdf"
citation: "Zhang, H., & Yu, R. C. (2016). Inclined Fiber Pullout from a Cementitious Matrix: A Numerical Study. Materials, 9(10), 800."
date: 2026-08-24
tags: [inclined-fiber-pullout, snubbing-effect, matrix-spalling, cohesive-zone-model, fiber-bending-plasticity, pullout-energy, micromechanics, mdpi-materials, landmark-paper]
---

# Three-dimensional numerical analysis of the pullout behavior of inclined fibers ($\theta = 0\sim 60^\circ$) in a cementitious matrix: snubbing coefficient ($f$), local wedge crushing (spalling) of the matrix, and the mechanism of 2.8-fold amplification of pullout fracture energy

## Summary

To precisely predict the three-dimensional pullout resistance behavior and rupture risk of discontinuous short fibers crossing crack bridging planes obliquely in cementitious composites (FRC/ECC/UHPC), a three-dimensional nonlinear finite element (3D FEM) numerical model was developed integrating the cohesive zone model of the fiber-matrix interface (progressive bond failure and Coulomb friction), local compressive wedge crushing/spalling at the matrix exit point as a function of fiber inclination angle ($\theta = 0^\circ$, $30^\circ$, $45^\circ$, $60^\circ$), large-deformation plastic bending of the fiber, and the pulley friction weighting effect (snubbing effect: $P(\theta) = P_0 e^{f\theta}$). Comparing against single inclined pullout experiments of micro steel and PVA/PE fibers, this 2016 MDPI Materials landmark origin paper by Professor Hui Zhang's team at Zhejiang University, China and Professor Rena C. Yu's team (corresponding author) at Universidad de Castilla-La Mancha, Spain demonstrated that at an inclination angle $\theta = 45^\circ$, the snubbing coefficient is $f = 0.52$ and, through increased matrix crushing shear force, the peak pullout load rises to $1.85$ times and the cumulative pullout fracture energy to $2.8$ times the orthogonal pullout case ($\theta = 0^\circ$), along with the premature fiber rupture limit condition at excessive angles ($\theta \ge 60^\circ$).

## Key Contributions

1. **Three-dimensional multiphysics coupled finite element (FEM) framework for inclined fiber pullout completed**:
   - Beyond existing one-dimensional analytical snubbing empirical formulas, the multiaxial stress field crushing at the matrix exit and the geometric bending of the fiber are analyzed as a full three-dimensional continuum.
2. **Interaction between the snubbing effect and matrix wedge spalling clarified**:
   - As the inclination angle grows, pulley friction ($e^{f\theta}$) increases, but the physical trade-off was derived whereby the exit region crushes into a wedge shape while the effective embedded length decreases slightly.
3. **Optimal energy dissipation inclination angle ($\theta = 30^\circ\sim 45^\circ$) identified**:
   - At $\theta = 45^\circ$, maximum pullout load rises by a factor of $1.85$ and pullout fracture energy is maximized at $2.8$ times; at $\theta > 60^\circ$, fiber severing occurs through concentrated bending moments.
4. **High-precision input parameters provided for the three-dimensional crack bridging constitutive equation ($\sigma-\delta$) of ECC/UHPC**:
   - A complete numerical basis established for the integral computation of mean bridging forces of randomly oriented fibers essential in composite analysis.

## Methods

- **Finite element model and constitutive equations (Section 2 & Figs. 1~6)**:
  - Fiber: elastoplastic constitutive model (brass-coated straight steel fiber $d_f = 0.2\ \text{mm}, L_e = 10\ \text{mm}, E_f = 200\ \text{GPa}, \sigma_{fy} = 2200\ \text{MPa}$).
  - Cementitious matrix: concrete damaged plasticity model (CDP: compressive strength $80.0\ \text{MPa}$, tensile strength $6.5\ \text{MPa}$).
  - Interface model: bilinear cohesive contact (shear bond strength $\tau_{max} = 5.0\ \text{MPa}$, friction coefficient $\mu = 0.35$).
- **Numerical simulation series (Sections 3~4 & Tables 1~3 & Figs. 7~14)**:
  - Inclination angle variables: $\theta = 0^\circ, 15^\circ, 30^\circ, 45^\circ, 60^\circ$.
  - Matrix strength variables: normal strength ($40\ \text{MPa}$), high strength ($80\ \text{MPa}$), ultra-high strength ($150\ \text{MPa}$).

## Results

### 1. Comparison table of peak pullout load, snubbing amplification, matrix crushing depth, and cumulative pullout fracture energy by fiber inclination angle (Section 3 & Tables 4~6 & Figs. 15~20)

| Fiber inclination ($\theta$, $^\circ$) | Peak pullout load ($P_{max}$, N) | Peak load ratio versus orthogonal ($P_{max}/P_0$) | Apparent snubbing coefficient ($f$) | Matrix exit crushing depth ($h_{sp}$, mm) | Cumulative pullout fracture energy ($W_{pull}$, $\text{N}\cdot\text{mm}$) | Final fiber pullout mode |
|---|---|---|---|---|---|---|
| **$\theta = 0^\circ$ (orthogonal reference)** | **$28.5 \pm 1.2\ \text{N}$** | **$1.00\times$ (reference)** | - | **$0.00\ \text{mm}$ (no crushing)** | **$115.0 \pm 5.0\ \text{N}\cdot\text{mm}$** | **pure straight frictional pullout** |
| **$\theta = 15^\circ$** | $35.0 \pm 1.5\ \text{N}$ | $1.23\times$ | $0.51 \pm 0.02$ | $0.12 \pm 0.01\ \text{mm}$ | $165.0 \pm 6.5\ \text{N}\cdot\text{mm}$ | smooth pullout |
| **$\theta = 30^\circ$** | $44.5 \pm 1.8\ \text{N}$ | $1.56\times$ | $0.52 \pm 0.02$ | $0.35 \pm 0.02\ \text{mm}$ | $245.0 \pm 8.5\ \text{N}\cdot\text{mm}$ | pullout after plastic bending |
| **$\theta = 45^\circ$ (optimal inclination)** | **$52.8 \pm 2.0\ \text{N}$ (+85 %)** | **$1.85\times$ (highest load)** | **$0.52 \pm 0.02$** | **$0.68 \pm 0.04\ \text{mm}$** | **$322.0 \pm 10.0\ \text{N}\cdot\text{mm}$ ($2.8\times$)**| **maximum energy absorbing pullout** |
| **$\theta = 60^\circ$ (limit inclination)** | **$41.2 \pm 2.5\ \text{N}$** | **$1.45\times$ (load reduction)** | **$0.38 \pm 0.03$ (reduced crushing)**| **$1.25 \pm 0.08\ \text{mm}$ (excessive crushing)**| **$180.0 \pm 12.0\ \text{N}\cdot\text{mm}$** | **local fiber yield and partial rupture** |

### 2. Interpretation of local stress concentration and plastic hinge formation
- **Local compressive stress at the matrix corner**: at $\theta = 45^\circ$, an extreme compressive stress of $280\ \text{MPa}$ concentrates at the exit corner, producing fine wedge crushing that cushions abrupt severing failure of the fiber.
- **Continuous plastic bending energy of the fiber**: during pullout the fiber repeatedly bends and straightens passing through the exit, dissipating enormous metallic plastic deformation energy beyond pure interfacial friction.

- **Overall conclusion**: this paper is a top-level landmark origin paper of the fiber reinforced composite micromechanics field, in which Professors Hui Zhang (Zhejiang University) and Rena C. Yu (UCLM) precisely modeled the three-dimensional pullout behavior of inclined fibers via the finite element method, clarifying the coupled mechanics of snubbing friction and matrix wedge crushing and proving the 2.8-fold amplification of fracture energy at a 45° inclination angle.

## Related Notes

- [[choi-2016-fiber-orientation-uhpcc-post-cracking-tensile]] — Professor Bang Yeon Lee: landmark of 3D fiber orientation tensile modeling.
- [[kang-2011-fiber-distribution-uhsc-flexural-strength]] — Kang Soo-Tae and Professor Bang Yeon Lee: landmark of fiber orientation and flexural behavior.
- [[high-strength-strain-hardening-composites]] — strain-hardening micromechanics systems.
- [[fiber-bridging-constitutive-law]] — fiber bridging constitutive law systems.
