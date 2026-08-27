---
title: "A novel method for the determination of polymeric micro-fiber distribution of cementitious composites exhibiting multiple cracking behavior under tensile loading"
type: source_note
source: "sources/felekoğlu-2015-a-novel-method-for-the.pdf"
citation: "Felekoğlu, B., Tosun-Felekoğlu, K., & Gödek, E. (2015). A novel method for the determination of polymeric micro-fiber distribution of cementitious composites exhibiting multiple cracking behavior under tensile loading. Materials & Design, 88, 1238-1247."
date: 2026-08-24
tags: [htpp-fiber, ecc, fiber-distribution, image-analysis, sem-bse, fiber-density-map, matrix-viscosity, strain-hardening, dokuz-eylul-university, materials-and-design, landmark-paper]
---

# SEM-Image Analysis Protocol for Evaluating Polymeric Micro-Fiber Distribution on Tensile Fracture Surfaces of HTPP-ECC and Matrix Viscosity Control Mechanisms

## Summary

In strain-hardening cementitious composites incorporating cost-effective high-tenacity polypropylene (HTPP: diameter $12\ \mu\text{m}$, length $12\ \text{mm}$, $V_f = 2.0\ \text{vol.\%}$) fibers, Professor Burak Felekoğlu and co-workers at Dokuz Eylül University developed an SEM-BSE image analysis protocol to quantify the 3D spatial distribution and generate 2D fiber density maps on tensile fracture surfaces. Comparing a low-viscosity matrix based on spherical fly ash (M24) against a high-viscosity matrix based on angular limestone powder (M37), the authors established the correlation between matrix rheological viscosity, fiber dispersion coefficient ($\alpha_f$), and saturated tensile strain-hardening behavior ($\varepsilon_u = 3.5\%$ vs $< 1.0\%$).

## Key Contributions

1. **Development of an SEM-BSE image analysis and fiber density mapping protocol for polymeric micro-fibers ($12\ \mu\text{m}$)**:
   - Utilized dark backscattered electron (BSE) contrast of hydrocarbon HTPP fibers combined with ImageJ algorithms to distinguish micro-fibers from matrix pore defects, generating 2D spatial fiber density maps across tensile failure sections.
2. **Quantification of the relationship between matrix rheology and fiber dispersion coefficient ($\alpha_f$)**:
   - The M24 matrix with lower plastic viscosity driven by spherical fly ash ball-bearing effects achieved a high dispersion coefficient ($\alpha_f = 0.72$), whereas the angular limestone powder M37 matrix suffered from high shear resistance, dropping $\alpha_f$ to 0.48 and causing fiber clumping.
3. **Verification of the impact of fiber dispersion on saturated multiple cracking and tensile ductility**:
   - Uniformly dispersed M24 achieved saturated propagation of $20\sim 26$ microcracks and tensile strain capacities of $3.2\sim 3.8\%$, whereas clumped M37 exhibited premature localization with $< 5$ cracks and $< 1.0\%$ strain capacity.
4. **Validation of ECC defect management design principles**:
   - Demonstrated that rather than eliminating initial flaws as in high-strength concrete, ECC relies on uniformly distributed micro-flaws that sequentially initiate multiple cracks under fiber bridging control.

## Methods

- **HTPP fiber properties**:
  - Material: High-tenacity polypropylene (HTPP), diameter $d_f = 12\ \mu\text{m}$, length $L_f = 12\ \text{mm}$ ($L_f/d_f = 1000$).
  - Tensile strength 850 MPa, elastic modulus 8.5 GPa, volume fraction $V_f = 2.0\ \text{vol.\%}$.
- **Matrix mix design comparison (Table 1)**:
  - **M24 (Low-viscosity mix)**: OPC 383, fly ash (FA) 843, silica sand 440, water 331 $\text{kg/m}^3$ (W/B = 0.27, W/C = 0.86), superplasticizer 3.3 $\text{kg/m}^3$.
  - **M37 (High-viscosity mix)**: OPC 837, limestone powder (LP) 1121, silica sand 628, water 310 $\text{kg/m}^3$ (W/B = 0.16, W/C = 0.37), superplasticizer 18.0 $\text{kg/m}^3$.
- **Rheological and mechanical testing (Sections 2.2–2.4)**:
  - Matrix viscosity: Marsh Cone efflux time and flow table testing (ASTM C230).
  - Uniaxial direct tension: JSCE dogbone specimens ($30 \times 13\ \text{mm}$ section, gage length 80 mm) at 0.5 mm/min.
- **SEM fracture surface image analysis (Section 2.3 & Figs. 2–4)**:
  - Polished tensile fracture surfaces under JEOL JSM-6060 SEM-BSE mode (150x magnification, grid tiling).
  - Fiber centroid extraction and dispersion coefficient calculation: $\alpha_f = 1 - \text{COV}(N_{fiber})$.

## Results

### 1. Fiber dispersion parameters and tensile performance of HTPP-ECC across matrices (Tables 2–3 & Figs. 5–8)

| Matrix mix ID | Powder system | Flow (mm) | Fiber dispersion coefficient ($\alpha_f$) | Mean fibers (per field) | Multiple crack count | Ultimate tensile strength ($\sigma_{tu}$, MPa) | Tensile strain capacity ($\varepsilon_u$, %) |
|---|---|---|---|---|---|---|---|
| **M24 (Low viscosity)** | **OPC + Fly ash** | **$165\ \text{mm}$** | **$0.72 \pm 0.04$ (Uniform)** | **$51 \pm 18$** | **$20 \sim 26$** | **$4.8 \pm 0.3\ \text{MPa}$** | **$3.5 \pm 0.3\%$ (Strain-hardening)** |
| **M37 (High viscosity)**| **OPC + Limestone powder** | **$162\ \text{mm}$** | **$0.48 \pm 0.08$ (Clumped)** | **$32 \pm 26$** | **$< 5$** | **$3.9 \pm 0.5\ \text{MPa}$** | **$< 1.0\%$ (Early localization)** |

### 2. Mechanisms linking matrix viscosity, fiber dispersion, and tensile ductility
- **Spherical fly ash lubrication mechanism**: In M24, spherical fly ash particles reduced slurry plastic viscosity, untangling fibers during mixing and creating a uniform bridging network.
- **Limestone powder viscosity rise and bridging deficiency**: In M37, angular particles increased shear resistance, creating fiber-depleted zones that localized into single cracks upon first cracking.

- **Overall conclusion**: This work established an SEM-image analysis protocol to quantify polymeric micro-fiber dispersion on tensile fracture surfaces, demonstrating that controlling matrix plastic viscosity is essential to achieving >3 % tensile strain hardening in low-cost HTPP-ECC.

## Related Notes

- [[kang-2011-fiber-distribution-uhsc-flexural-strength]] — Image processing-based fiber distribution and flexural prediction by Bang Yeon Lee group.
- [[kim-2007-slag-ecc-tensile-fiber-dispersion]] — Fluorescent microscope-based fiber dispersion evaluation in slag-ECC.
- [[strain-hardening-mechanism]] — ECC strain-hardening micromechanics and $J_b'/J_{tip}$ energy criteria.
- [[de-larrard-2002-hpc-mixture-proportioning]] — Concrete rheology and mixture optimization.
