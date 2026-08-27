---
title: "Editorial for special issue on digital concrete / rheology and processing (Flatt, Roussel & Sanjayan, 2018)"
type: source_note
source: "sources/flatt-2018-editorial-for-special-issue-on.pdf"
citation: "Flatt, R. J., Roussel, N., & Sanjayan, J. G. (2018). Editorial for special issue on digital concrete / rheology and processing. Cement and Concrete Research, 112, 1-4. https://doi.org/10.1016/j.cemconres.2018.06.002"
date: 2026-08-24
tags:
  - 3d-printing-concrete
  - digital-concrete
  - rheology
  - thixotropy
  - yield-stress-evolution
---

# Editorial for Special Issue on Digital Concrete: Rheology and Processing (Flatt, Roussel & Sanjayan, 2018)

## Summary

Serving as the editorial introduction to the Cement and Concrete Research special issue on digital fabrication, this foundational paper synthesizes the physicochemical and rheological frameworks underpinning 3D concrete printing (3DCP). It quantifies the inherent trade-offs among pumpability, extrudability, buildability, and interlayer bond strength in formwork-free additive construction. The authors establish thixotropy control and the static yield stress evolution rate ($A_{thix}$) during the dormant period of cement hydration as central research benchmarks for digital concrete science.

## Key Contributions

- **Systematization of four core process requirements in digital concrete**: Formulated the rheological interactions among pumpability (low flow resistance), extrudability (nozzle shape retention), buildability (structural yield strength to resist self-weight and vertical printing loads), and interlayer bonding (mitigation of cold joints).
- **Mathematical framework for buildability and thixotropic structuration**: Formulated critical thresholds for the static yield stress growth rate $A_{thix} = \partial \tau_0 / \partial t$ to prevent lower-layer collapse during vertical layer accumulation.
- **Technology roadmap for accelerated hydration and active processing**: Outlined strategies for balancing workability and rapid setting through inline chemical acceleration (set-on-demand) injected immediately prior to extrusion.

## Methods

- Scholarly review and synthesis of rheological constitutive equations for cementitious suspensions.
- Viscoelastic and plastic yield models: Application of Bingham ($\tau = \tau_0 + \mu_p \dot{\gamma}$) and Herschel-Bulkley formulations.
- Maximum buildable height derived from the thixotropic structuration parameter $A_{thix}$ (in Pa/s or Pa/min):
  $$\tau_{0}(t) = \tau_{0,0} + A_{thix} t$$
  $$h_{max} = \frac{2 \tau_0(t)}{\rho g}$$

## Results

- Successful digital fabrication requires materials that maintain low viscosity and shear stress during extrusion, followed immediately by rapid thixotropic recovery of static yield stress ($\tau_{0,static}$) upon deposition.
- Identified interlayer delay time ($t_{gap}$) as a primary challenge, where surface desiccation and hydration discontinuities can reduce tensile and shear bond strengths by up to 50 %, introducing mechanical anisotropy into 3D-printed structures.

## Related Notes

- [[3d-printable-ecc]] — Buildability and fiber orientation mechanisms in 3D-printable strain-hardening composites.
- [[particle-packing-models]] — Particle packing optimization for printable pastes and mortars.
- [[zhu-2019-3dp-ecc-ultra-high-ductility]] — Rheological and mechanical behavior of ultra-high-ductility 3D-printable ECC.
