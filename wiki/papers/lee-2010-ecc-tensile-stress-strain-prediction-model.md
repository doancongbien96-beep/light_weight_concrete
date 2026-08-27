---
title: "Prediction of ECC tensile stress-strain curves based on modified fiber bridging relations considering fiber distribution characteristics"
type: source_note
source: "sources/lee-2010-prediction-of-ecc-tensile-stress-strain.pdf"
citation: "Lee, B. Y., Kim, J.-K., & Kim, Y. Y. (2010). Prediction of ECC tensile stress-strain curves based on modified fiber bridging relations considering fiber distribution characteristics. Computers and Concrete, 7(5), 455-468."
date: 2026-08-24
tags: [ecc, tensile-stress-strain-prediction, fiber-bridging-relation, crack-spacing-model, pulley-force, fiber-dispersion-coefficient, computers-and-concrete, bang-yeon-lee, landmark-paper]
---

# Full-Range Numerical Prediction of ECC Uniaxial Tensile Stress-Strain Curves Incorporating Sectional Image Analysis and Inclined Fiber Pulley Force

## Summary

When simulating the direct uniaxial tensile behavior of Engineered Cementitious Composites (ECC), conventional models rely on idealized 2D/3D fiber orientation assumptions, causing significant overestimation of tensile strain capacity (errors exceeding $20\%$) due to neglected casting flow and dispersion non-uniformity. To overcome this limitation, Prof. Bang Yeon Lee (first author, Chonnam National University), Prof. Jin-Keun Kim (KAIST), and Prof. Yun Yong Kim (corresponding author, Chungnam National University) established a **modified fiber bridging constitutive relation ($\sigma_B-\delta$) incorporating the fiber dispersion coefficient ($\alpha_f$) and orientation distributions directly extracted from sectional fluorescence image analysis**. By coupling this with a **crack spacing ($x_d$) governing equation based on inclined fiber pulley reactions and frictional equilibrium**, the authors developed a numerical simulation framework capable of predicting the full-range stress-strain ($\sigma-\varepsilon$) response—from initial elasticity through multiple microcracking strain-hardening to peak strength and softening failure (Computers and Concrete, 2010).

## Key Contributions

1. **Derivation of a rigorous crack spacing ($x_d$) model incorporating inclined fiber pulley forces and orientation factor ($\phi_{ori}$)**:
   - Formulated the crack spacing governing equation $x_d = \frac{V_m f_{ct} d_f}{4 V_f \tau_0 \phi_{ori} (1 + \text{reaction factor})}$ by accounting for the normal pulley reaction forces exerted by inclined fibers on the matrix at crack faces.
2. **Mathematical integration of image-analysis-derived dispersion coefficient ($\alpha_f$) into multilinear tensile constitutive models**:
   - Directly integrated measured orientation probability density functions $p(\theta)$ and sectional fiber density $F_n$ into micromechanical bridging equations, seamlessly synthesizing the tensile stress-strain curve from the composite bridging stress-opening curve.
3. **Rigorous validation against uniaxial tensile experimental data for 4 PVA-ECC mixtures**:
   - While idealized 2D/3D assumptions overestimated tensile strain capacity by over $20\%$, the proposed model predicted experimental tensile strain capacity ($2.5\sim 4.2\%$) and strength within a $5\%$ error margin.
4. **Quantification of slag-induced fiber dispersion enhancement**:
   - Demonstrated numerically that slag-blended mixtures exhibit higher dispersion coefficients ($\alpha_f \approx 0.32$), maintaining peak bridging stress without degradation and ensuring stable saturated multiple cracking.

## Methods

- **Crack spacing and tensile strain constitutive formulations (Section 2, Figs. 1–2)**:
  - Crack spacing bounds: $x' \le x \le 2x'$ (where minimum crack spacing $x'$ corresponds to matrix tensile strength $f_{ct}$).
  - Total tensile strain: $\varepsilon = \frac{\sigma}{E_c} + \frac{\delta(\sigma)}{x_d}$ (where $\delta(\sigma)$ is the inverse function of the bridging stress-crack opening curve).
- **Sectional image processing and fiber tracking (Section 3, Fig. 4)**:
  - Fluorescence microscopy images $\rightarrow$ adaptive binarization and boundary ellipse fitting $\rightarrow$ measurement of centroid coordinates, aspect ratios, and inclination angles $\theta = \arccos(b/a)$.
  - Dispersion coefficient: $\alpha_f = 1 - \text{COV}(N_{fiber})$.
- **4 PVA-ECC validation mixtures (Section 5, Tables 2–5)**:
  - `wc60wos`: W/C = 0.60, 0 % slag.
  - `wc60ws`: W/C = 0.60, 25 % slag replacement.
  - `wc48wos`: W/C = 0.48, 0 % slag.
  - `wc48ws`: W/C = 0.48, 25 % slag replacement.
  - PVA fibers: Kuraray REC15 ($V_f = 2.0\ \text{vol.}\%$, $d_f = 39\ \mu\text{m}$, $L_f = 12\ \text{mm}$).

## Results

### 1. Fiber distribution parameters and model predictions vs experimental tensile response across 4 PVA-ECC mixtures (Tables 5–7, Figs. 6–9)

| Mix ID | W/C (%) | Slag Replacement | Dispersion Coeff. ($\alpha_f$) | Fiber Density ($F_n$, fibers/mm$^2$) | Exp. Tensile Strength ($\sigma_{tu}$, MPa) | Predicted Tensile Strength (MPa) | Exp. Tensile Strain ($\varepsilon_u$, %) | Predicted Strain (%) | 2D Assumption Predicted Strain (%) |
|---|---|---|---|---|---|---|---|---|---|
| **wc60wos** | 60 % | 0 % (Plain) | 0.311 | $8.95 \pm 0.39$ | $3.58 \pm 0.2$ | **$3.65\ \text{MPa}$** | $2.55 \pm 0.3\%$ | **$2.62\%$** | $3.15\%$ (+24 % overestimation) |
| **wc60ws** | 60 % | **25 % slag** | **0.321** | $9.94 \pm 0.29$ | $3.82 \pm 0.2$ | **$3.90\ \text{MPa}$** | $3.25 \pm 0.3\%$ | **$3.30\%$** | $3.85\%$ (+18 % overestimation) |
| **wc48wos** | 48 % | 0 % (Plain) | 0.315 | $10.6 \pm 0.97$ | $4.25 \pm 0.3$ | **$4.32\ \text{MPa}$** | $3.45 \pm 0.4\%$ | **$3.50\%$** | $4.15\%$ (+20 % overestimation) |
| **wc48ws** | 48 % | **25 % slag** | **0.317** | **$11.8 \pm 0.65$** | **$4.85 \pm 0.3$** | **$4.92\ \text{MPa}$** | **$4.18 \pm 0.4\%$** | **$4.25\%$** | **$5.02\%$ (+20 % overestimation)** |

### 2. Numerical simulation and crack spacing mechanics
- **Influence of inclined fiber pulley force**: Pulley reaction forces exerted at matrix corners accelerate load transfer into the adjacent matrix, reducing crack spacing $x_d$ by approximately $15\%$ relative to pure frictional assumptions and enhancing crack density.
- **Necessity of image-analysis-based prediction**: Idealized 2D random assumptions overestimate fiber bridging stiffness and inflate predicted strain capacity by approximately $20\%$, confirming that incorporating measured fiber distributions is essential for reliable structural design.

- **Overall conclusion**: This landmark paper integrated actual fiber orientation image analysis with inclined fiber pulley mechanics to establish a numerical simulation framework predicting full-range direct uniaxial tensile stress-strain curves of ECC within 5% error.

## Related Notes

- [[lee-2010-micromechanics-fiber-bridging-distribution-model]] — Prof. Bang Yeon Lee: Fiber bridging constitutive model based on measured orientation.
- [[lee-2010-fluorescence-discriminating-fibers-hybrid-ecc]] — Prof. Bang Yeon Lee: Fluorescence image analysis and optical filter design.
- [[kim-2007-slag-ecc-tensile-fiber-dispersion]] — Fiber dispersion and tensile behavior in slag-blended ECC.
- [[kanda-2006-saturated-psh-design-criteria-ecc]] — Saturated PSH design criteria for ECC.
