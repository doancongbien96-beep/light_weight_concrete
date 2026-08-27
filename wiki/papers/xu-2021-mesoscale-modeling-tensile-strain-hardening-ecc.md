---
title: "Mesoscale Modeling of Tensile Strain-Hardening Behavior of ECC (Xu et al., 2021)"
type: source_note
source: "sources/xu-2021-mesoscale-modeling-of-tensile-strain-hardening.pdf"
citation: "Xu, M., Zhang, Y., & Li, V. C. (2021). Mesoscale modeling of tensile strain-hardening behavior of engineered cementitious composites (ECC). Cement and Concrete Research, 147, 106516. https://doi.org/10.1016/j.cemconres.2021.106516"
date: 2026-08-24
tags:
  - mesoscale-modeling
  - discrete-element-method
  - tensile-strain-hardening
  - fiber-bridging
  - multiple-cracking
---

## Summary
A pioneering study that directly simulated in three dimensions at the mesoscale the initiation and steady-state propagation of multiple fine cracks and the stress redistribution process by fiber bridging that occur in high-ductility composites (ECC) under uniaxial tensile loading, by combining the Lattice Discrete Particle Model (LDPM) with a Cohesive Zone Model. The random spatial distribution of aggregates/flaws inside the matrix and tens of thousands of short-fiber bridging mechanisms were individually incorporated into a discrete element network, reproducing the tensile stress-strain response, the crack spacing distribution, and the single-crack localization failure process with high accuracy.

## Key Contributions
- **Development of a 3D mesoscale discrete lattice-based numerical model of ECC tensile multiple cracking**: individual fiber pull-out bridging force ($\sigma-\delta$) integrated into lattice facets as nonlinear springs.
- **Dynamic simulation of the statistical flaw size distribution and the crack initiation sequence**: visualization of the process in which initial cracking starts at the largest flaw and then transitions sequentially to smaller flaws.
- **Secured reliability of macroscopic tensile strain capacity prediction**: agreement above 92 % was achieved with experimentally observed $3.0 \sim 6.0 \%$ tensile strain envelopes and measured crack counts.

## Methods
- LDPM framework based on three-dimensional Voronoi tessellation.
- Nonlinear fiber bridging constitutive subroutine and parallel computation analysis.

## Results
- Computationally demonstrated that the matrix fracture toughness $K_m$ and the spatial heterogeneity of the flaw distribution determine the multiple-cracking saturation limit.
- Established applicability as a virtual testing tool for ECC mix optimization.

## Related Notes
- [[pseudo-strain-hardening-criteria]] - Micromechanics theory of strain-hardening composites
- [[tosun-felekoglu-2014-flaw-size-tensile-strain-hardening-ecc]] - Flaw size distribution and strain-hardening behavior
