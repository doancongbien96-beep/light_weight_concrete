---
title: "Mixture-proportioning of high-performance concrete"
type: source_note
source: "sources/de-2002-mixture-proportioning-of-high-performance-concrete.pdf"
citation: "de Larrard, F., & Sedran, T. (2002). Mixture-proportioning of high-performance concrete. Cement and Concrete Research, 32(11), 1699-1704."
date: 2026-08-23
tags: [hpc, compressible-packing-model, cpm, mixture-proportioning, rheology, yield-stress, plastic-viscosity, maximum-paste-thickness, de-larrard, theory-foundation]
---

# Scientific Framework for Performance-Based Mixture Proportioning of High-Performance Concrete (HPC) Based on Compressible Packing Model (CPM) and Integrated Rheology-Mechanics Model

## Summary

Overcoming the limitations of conventional mixture proportioning reliant on empirical charts and trial-and-error, François de Larrard and Thierry Sedran of the Laboratoire Central des Ponts et Chaussées (LCPC) in France authored this classic foundational paper to quantitatively predict the flowability, strength, and durability of high-performance concrete (HPC) combining various binders (cement, silica fume, fly ash, limestone filler) and chemical admixtures. Taking the particle packing theory of the Compressible Packing Model (CPM) as the backbone, the authors integrated rheology (yield stress $\tau_0$, plastic viscosity $\mu$), hydration heat, compressive strength (Maximum Paste Thickness, MPT model), elastic modulus, autogenous shrinkage, and drying shrinkage into a single computational package (BÉTONLABPRO). By combining inter-particle interactions (wall effect and loosening effect) with the compaction energy index ($K$), the actual solid packing fraction ($\Phi$) was numerically solved. Under minimum unit cost constraints, the design of a special 80 MPa-class HPC for road pavements (slump 150 mm, plastic viscosity <350 Pa·s, total shrinkage $\ge 750 \times 10^{-6}$) was automatically optimized. In real trial batches, predictive agreement was verified with a 28-day compressive strength of **78.1 MPa**, slump of **160 mm**, and plastic viscosity of **120–250 Pa·s**.

## Key Contributions

1. **Formalization and numerical implementation of Compressible Packing Model (CPM)**:
   - Starting from intrinsic packing density ($\beta_i$) of monodisperse fractions, virtual packing density ($\gamma$) considering the wall effect and loosening effect was computed, establishing an $n$-equation system to back-calculate measurable actual packing density using compaction index $K$. Prediction accuracy within 1 % on absolute packing density.
2. **Introduction of filling diagram as a segregation resistance diagnostic tool**:
   - Visualized the relative filling ratio ($F_i/F_i^*$) distribution across particle size classes, identifying peak excessive values and grain size discontinuities (gaps) as segregation signs and guiding mixture adjustments.
3. **Physical modeling of fresh concrete rheology**:
   - Elucidated the mechanism that yield stress originates from inter-particle friction (friction coefficient increases with smaller particles; superplasticizer dosage reduces cement friction coefficient up to 5:1 ratio) and plastic viscosity originates from relative solid concentration ($\Phi/\gamma$). Slump model conversion achieved an average accuracy of 4–5 cm.
4. **Incorporation of Maximum Paste Thickness (MPT) concept into strength modeling**:
   - Combined the topological effect where smaller average distance between adjacent coarse aggregate particles (MPT) enhances strength with Féret's power law, constructing a universal strength model (average error 2–3 MPa) applicable to mixtures containing aggregates, pozzolans, and limestone fillers from 1 day to 1 year of age.
5. **Integrated deformation analysis via triple-sphere model**:
   - Divided the matrix centered around aggregate into an inner core (compressed paste) and outer layer (excess paste providing workability), analytically deriving elastic modulus, basic creep, drying creep, autogenous shrinkage, and drying shrinkage from hydrostatic stress analysis alone.

## Methods

- **CPM components**: (i) Packing density of monosize fractions, (ii) grain size distribution of mixture, (iii) compaction energy. Virtual packing density is computed by adding the wall effect (coarse particle interference) and loosening effect (fine particle interference) to residual packing density $\beta_i$ of dominant class $i$, while compaction index $K = \sum K_i$ uniquely determines actual packing density.
- **Rheology model**: Fresh concrete is treated as a Bingham material, defining yield stress and plastic viscosity from linear shear stress-strain rate relations. Plastic viscosity is a function of relative concentration, while yield stress is calculated by multiplying fractional compaction index by friction coefficient.
- **Strength model**: Cement concentration in paste is incorporated via Féret power law and modified by MPT effect from aggregate phase topology. Predicts strength from overall mixture composition rather than water-cement ratio alone.
- **Deformation model**: Hydrostatic pressure is applied to the triple-sphere (inner core-aggregate-outer layer) topology to analyze instantaneous and delayed deformations of concrete from phase deformations.
- **Validation**: Slump and elastic modulus models were validated using pure prediction mode (no fitting) on identical material series with superplasticizers.

## Results

- Special 80 MPa-class HPC design case for road pavements (Table 1):

| Parameter | Theoretical Mix | Actual Mix |
|---|---|---|
| Coarse aggregate 2/6 (kg/m³) | 935 | 912 |
| Fine aggregate 0/4 (kg/m³) | 623 | 608 |
| Cement (kg/m³) | 406 | 408 |
| Limestone filler (kg/m³) | 101 | 139 |
| Silica fume (kg/m³) | 40.6 | 39 |
| Superplasticizer (kg/m³) | 4.35 | 5.62 |
| Water (l/m³) | 185 | 190 |
| Compaction index K' | - | 6.9 |
| Slump (mm) | =150 target | 150 → 160 |
| Plastic viscosity (Pa·s) | <350 target | 120–250 (after 60 min) |
| 28-day compressive strength (MPa) | =80 target | 78.1 |
| 50% RH total shrinkage ($10^{-6}$) | ≥750 target | 750 |

- Slump model: Good agreement with experimental measurements in non-fitted predictions for superplasticizer series (Fig. 5).
- Thermal hydration model: Average accuracy of adiabatic temperature rise prediction approximately 2 °C.

## Related Notes

- [[collins-1999-shear-design-high-strength-concrete]] — AAS concrete mix and mechanical properties (Monash, Australia).
- [[sustainability-low-carbon-binders]] — Low-carbon binder mixture proportioning framework.
- [[creep-and-shrinkage-mechanisms]] — Concrete creep and shrinkage prediction model axis.
