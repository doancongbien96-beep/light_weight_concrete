---
title: "Particle Packing Models in High Performance Concrete and ECC"
type: concept
date: 2026-08-23
tags: [particle-packing, compressible-packing-model, cpm, modified-andreasen-andersen, packing-density, rheology, uhpc, concept]
source: internal
---


# Particle Packing Models in Cementitious Composites (CPM & Modified A&A)

## 1. Overview and theoretical background

The central physical principle for maximizing matrix flowability, compressive strength,
elastic modulus, and durability in HPC, UHPC, and ultra-ductile ECC/UHDCC is **particle
packing**. When cement, silica fume, slag, fly ash, limestone filler, and microsilica are
geometrically optimized to minimize inter-particle void volume, the excess water left
over after filling the voids (even at W/B 0.15–0.25) forms a lubricating water film on
particle surfaces (Water Film Thickness, WFT), achieving high flowability and a dense
hydration structure simultaneously.

## 2. Representative packing theory models

### (1) Modified Andreasen & Andersen continuous packing model
A statistical model optimizing the continuous particle size distribution:
$$P(d) = \frac{d^q - d_{min}^q}{d_{max}^q - d_{min}^q}$$
- $P(d)$: cumulative passing percentage below particle size $d$.
- $d_{max}, d_{min}$: largest and smallest sizes in the system ($0.1\ \mu\text{m} \sim 2.0\ \text{mm}$).
- $q$: distribution modulus.
  - $q = 0.22 \sim 0.25$: optimal for self-consolidating UHPC/ECC rich in fines
    (silica fume, filler).
  - $q = 0.30 \sim 0.37$: suited to ordinary structural high-strength concrete.

### (2) de Larrard's Compressible Packing Model (CPM)
A model quantifying geometric interactions between discrete particle fractions and
compaction energy:
- **Wall effect**: near the flat surface of large particles small particles cannot pack
  densely, raising porosity.
- **Loosening effect**: small particles wedged between large ones push contacts apart and
  loosen the skeleton.
- **Compaction index ($K$) and actual packing density ($\Phi$)**:
  $$K = \sum_{i=1}^n K_i = \sum_{i=1}^n \frac{\Phi_i / \Phi_i^*}{1 - \Phi_i / \Phi_i^*}$$
  As compaction energy tends to infinity ($K \rightarrow \infty$) the virtual packing
  density $\gamma$ is approached; actual $\Phi$ under vibration ($K \approx 7.0$) or
  self-weight ($K \approx 4.0$) is computed by implicit numerical solution.

## 3. Link to rheology and mechanics

- **Plastic viscosity and lubrication**:
  when relative solid concentration ($\Phi/\Phi_{max}$) is controlled below its critical
  value, paste plastic viscosity stabilizes exponentially, preventing fiber balling and
  guaranteeing uniform dispersion.
- **Maximum Paste Thickness (MPT)**:
  the thinner and more uniform the excess-paste film between aggregates, the more the rise
  of brittle-matrix fracture toughness ($K_m$) is suppressed — favorable for securing the
  PSH energy condition ($J'_b/J_{tip}$).

## 4. Key research papers and applications

- [[de-larrard-2002-hpc-mixture-proportioning]] — origin of CPM-based rheology-integrated
  80 MPa HPC mix design.
- [[choi-2017-uhpm-pe-fiber-tensile-cracking]] — 150 MPa UHPM mix from Modified A&A
  ($q=0.23$).
- [[choi-2020-high-strength-composite-impact-resistance]] — silica-fume/micro-filler
  densely packed matrix.
- [[chun-2024-rc-beams-impact-resistance-hpfrcc]] — impact-resistant HPFRCC design on a
  dense matrix.
- [[uhpc-vs-ecc-design-space]] — particle size packing comparison between HS and HD matrices.

- [[du-2023-silicon-carbide-fineness-cement-composites]] — silicon carbide fine-particle
  packed, highly thermally conductive cement composites.

- [[hannawi-2016-fibers-microstructure-mechanical-uhpfrc]] — fiber-type-dependent
  microstructural densification of UHPFRC with gas permeability and acoustic emission,
  origin paper.

- [[han-2016-concrete-spalling-influential-factors-fire]] — Prof. Dong-Yup Han (Gyeongsang
  National University): governing factors of ISO-834 explosive spalling, vapor pressure,
  and pore structure mechanisms, origin paper.

- [[denkov-1999-mechanisms-mixed-antifoams-oil-bridges]] — Rhodia/Sofia University:
  landmark mechanism paper on antifoam oil-bridge Laplace capillary foam rupture.
