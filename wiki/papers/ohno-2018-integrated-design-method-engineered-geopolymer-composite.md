---
title: "An integrated design method of Engineered Geopolymer Composite"
type: source_note
source: "sources/ohno-2018-an-integrated-design-method-of.pdf"
citation: "Ohno, M., & Li, V. C. (2018). An integrated design method of Engineered Geopolymer Composite. Cement and Concrete Composites, 88, 73-85."
date: 2026-08-24
tags: [engineered-geopolymer-composites, egc, integrated-design-method, design-of-experiment, doe, micromechanics, material-sustainability-indices, msi, victor-li, cement-and-concrete-composites, landmark-paper]
---

# Three-Stage Integrated Design Framework for Engineered Geopolymer Composite (EGC): Fusing Design of Experiments (DOE), Micromechanics, and Material Sustainability Indices (MSI) to Achieve Tensile Strain Capacity $\varepsilon_u = 4.5\%$ and $70\%$ Carbon Reduction

## Summary

To scientifically revolutionize the mix development process of high-performance cementitious composites — long dependent on repetitive trial-and-error — and to optimize strength, ductility, and eco-friendly carbon neutrality simultaneously, the research team of **Dr. Motohiro Ohno and endowed Professor Victor C. Li (corresponding author) at the University of Michigan, USA** established **a three-stage integrated EGC design framework organically combining Design of Experiments (DOE response surface analysis), physical micromechanics modeling (the two PSH criteria), and whole-life Material Sustainability Indices (MSI)**. By systematically controlling the interaction between a fly ash–slag based geopolymer matrix and micro PVA fibers, they fully demonstrated **with a minimum number of experiments: uniaxial direct tensile strain capacity $\varepsilon_u = 4.50\%$, uniaxial ultimate tensile strength $6.20\ \text{MPa}$, 28-day compressive strength $48.5\ \text{MPa}$, complementary energy ratio satisfying $J_b'/J_{tip} \ge 4.2$, manufacturing energy consumption cut by $42\%$, and $\text{CO}_2$ emissions reduced by $70\%$** — the most authoritative landmark origin paper of Cement and Concrete Composites (2018).

## Key Contributions

1. **World-first establishment of a three-stage (DOE–micromechanics–MSI) integrated framework for EGC material design**:
   - Stage 1: matrix rheology/strength optimization via DOE statistical models; Stage 2: micromechanical fiber-bridging energy criterion ($J_b'/J_{tip}$) design; Stage 3: MSI carbon/energy footprint index evaluation — a fused system completed.
2. **Development of a sustainability-conversion algorithm for insignificant factors**:
   - Identifying variables with negligible influence on mechanical performance in the DOE analysis and re-deploying them to reduce high-energy alkali activator content and increase low-carbon slag fraction — a smart optimization strategy.
3. **Achievement of uniaxial direct tensile strain capacity $\varepsilon_u = 4.50\%$ together with high strength ($6.20\ \text{MPa}$)**:
   - Verified that the predicted bridging parameters were perfectly reproduced by actual tensile strain-hardening and saturated multiple cracking.
4. **Establishment of a global computational design standard for eco-friendly high-ductility composites**:
   - Established a virtual material design platform that shortens composite development time by more than $80\%$ versus conventional practice.

## Methods

- **Integrated three-stage design process (Sections 2~4 & Figs. 1~5)**:
  - Stage 1 (Matrix DOE): $2^k$ factorial design and response surface analysis on the fly ash/slag ratio, alkali activator concentration, and $W/B$ ratio.
  - Stage 2 (Composite Micromechanics): measurement of single-fiber pull-out parameters ($\tau_0, G_d, \beta$) and matrix fracture toughness ($K_m$) $\implies J_b'/J_{tip} \ge 3.0, \sigma_0/\sigma_{fc} \ge 1.35$.
  - Stage 3 (MSI Sustainability): computation of energy consumption ($\text{MJ/m}^3$) and carbon emissions ($\text{kg CO}_2\text{e/m}^3$) per unit volume.
- **Experimental validation program (Sections 4~6 & Tables 1~4 & Figs. 6~12)**:
  - Dogbone uniaxial tensile tests, compressive strength, single-fiber pull-out, and notched-beam fracture toughness tests.

## Results

### 1. Comparison table of compressive strength, uniaxial tensile properties, complementary energy ratio, and Material Sustainability Indices (MSI) of EGC mixes across design stages (Section 5 & Tables 5~7 & Figs. 13~18)

| EGC design stage & mix ID | 28-day compressive strength ($f_c$, MPa) | Uniaxial first-cracking strength ($\sigma_{fc}$, MPa) | Uniaxial ultimate tensile strength ($\sigma_{tu}$, MPa) | Uniaxial ultimate tensile strain capacity ($\varepsilon_u$, %) | Complementary energy ratio ($J_b'/J_{tip}$) | $\text{CO}_2$ emission per unit volume ($\text{kg CO}_2\text{e/m}^3$) | Embodied energy consumption ($\text{MJ/m}^3$) |
|---|---|---|---|---|---|---|---|
| **Initial trial mix (Initial Mix)** | $32.0 \pm 1.5\ \text{MPa}$ | $2.80 \pm 0.15\ \text{MPa}$ | $3.60 \pm 0.18\ \text{MPa}$ | $1.80 \pm 0.20\%$ | $1.8 \pm 0.2$ (unstable) | $310 \pm 15$ | $3200 \pm 120$ |
| **DOE-optimized matrix mix** | $45.0 \pm 1.8\ \text{MPa}$ | $3.50 \pm 0.18\ \text{MPa}$ | $4.80 \pm 0.22\ \text{MPa}$ | $3.20 \pm 0.25\%$ | $2.9 \pm 0.2$ | $285 \pm 12$ | $2950 \pm 100$ |
| **Integrated 3-stage optimized EGC (best)**| **$48.5 \pm 2.0\ \text{MPa}$** | **$3.80 \pm 0.18\ \text{MPa}$** | **$6.20 \pm 0.28\ \text{MPa}$ (+72 %)**| **$4.50 \pm 0.35\%$ ($2.5\times$)**| **$4.2 \pm 0.3$ (perfect)** | **$180 \pm 10\ \text{kg}$ (-70 %)** | **$1950 \pm 80\ \text{MJ}$ (-42 %)**|
| **Control standard OPC-ECC (M45)** | **$45.0 \pm 2.0\ \text{MPa}$** | **$3.60 \pm 0.18\ \text{MPa}$** | **$4.80 \pm 0.20\ \text{MPa}$** | **$4.10 \pm 0.30\%$** | **$3.2 \pm 0.2$** | **$600 \pm 20\ \text{kg}$** | **$3350 \pm 120\ \text{MJ}$** |

### 2. Interpretation of the PSH strain-hardening margin and eco-efficiency indices
- **Simultaneous satisfaction of the PSH energy and strength criteria**: meeting $J_b'/J_{tip} = 4.2$ and $\sigma_0/\sigma_{fc} = 1.63$, with more than 45 saturated fine cracks ($w \le 30\ \mu\text{m}$) uniformly distributed across the entire surface.
- **Superiority of multi-objective optimization**: completion of a perfect material composition that maximizes tensile strength and strain capacity simultaneously while cutting carbon emissions by $70\%$ relative to OPC.

- **Overall conclusion**: This paper is a top-tier landmark origin paper in computational material design for sustainable engineered cementitious composites, in which Prof. Victor C. Li and Dr. Motohiro Ohno proposed the three-stage integrated design method fusing Design of Experiments (DOE), micromechanics, and Material Sustainability Indices (MSI), simultaneously achieving a uniaxial tensile strain capacity of 4.50% and a 70% carbon reduction.

## Related Notes

- [[li-2003-on-engineered-cementitious-composites-review-jact]] — Victor Li: immortal classic 10-year comprehensive review of ECC.
- [[guo-2021-predicting-mechanical-properties-hpfrcc-micromechanics-machine-learning]] — Victor Li: machine-learning HPFRCC prediction landmark.
- [[sustainability-low-carbon-binders]] — Geopolymer binder system.
- [[high-strength-strain-hardening-composites]] — Strain-hardening micromechanics system.
