---
title: "최소 볼록 집합을 이용한 데이터베이스 기반 콘크리트 최적배합"
type: source_note
source: "sources/DJP0708N_최소 볼록 집합을_1.pdf"
citation: "이방연, 김재홍, 김진근. (2008). 최소 볼록 집합을 이용한 데이터베이스 기반 콘크리트 최적배합. 콘크리트학회 논문집 (Journal of the Korea Concrete Institute), 20(5), 627-634."
date: 2026-08-24
tags: [concrete-mix-design, convex-hull, database-driven-design, optimization-algorithm, compressive-strength, slump-prediction, bang-yeon-lee, jin-keun-kim, kci, landmark-paper]
---

# Database-Driven Concrete Mix Optimization Using Convex Hull Algorithm: Feasible Domain Definition, $15\%$ Cost Reduction, and $4.5\%$ Property Prediction Error Validation

## Summary

To overcome high non-linearity between mixture proportions and concrete properties (slump, 28 d compressive strength) and resolve complex multi-objective optimization dilemmas (strength, workability, economy, sustainability), this study established a database-driven inverse proportioning system. Developed by Prof. Jin-Keun Kim, Dr. Jae-Hong Kim, and Dr. Bang Yeon Lee (KAIST / Chonnam National University), the system maps historical mixture data (over 400 experimental mixtures) into multi-dimensional space. By applying the **Minimum Convex Hull (QuickHull algorithm)** technique from computational geometry, it defines a mathematically rigorous feasible domain before optimizing multi-objective non-linear objective functions. Experimental validation across target strengths ($21\sim 60\ \text{MPa}$) and slumps ($80\sim 210\ \text{mm}$) confirmed **prediction errors within $4.5\%$, a $15\%$ cost reduction per unit volume by suppressing excessive cement, and highly reliable optimal proportions**.

## Key Contributions

1. **First establishment of computational convex hull theory for concrete mix proportioning**:
   - Eliminated dangerous extrapolation errors inherent in database learning models by constructing a Convex Hull bounding the dataset, restricting optimization strictly to reliable interpolation domains.
2. **Multi-objective optimization framework**:
   - Simultaneously satisfied 1) target compressive strength, 2) target slump, 3) minimization of unit water and cement contents (cost savings and crack mitigation), and 4) maximization of mineral admixture (FA/GGBS) replacement ratios within seconds.
3. **High-precision experimental validation ($\text{error} \le 4.5\%$)**:
   - Laboratory batch mixing verified that actual compressive strengths and slumps matched target values within an average error of $4.5\%$.
4. **$80\%$ reduction in trial batches and $15\%$ material cost savings**:
   - Established the foundations of digital smart concrete proportioning, drastically cutting repetitive trial-and-error mixing cycles at ready-mix batch plants.

## Methods

- **Database compilation and parameter definitions (Section 2, Tables 1–2)**:
  - Input parameters: 420 industrial ready-mix and laboratory trial batches (water-to-binder ratio W/B, sand percentage S/a, unit water W, unit cement C, mineral admixtures FA/GGBS, superplasticizer SP).
  - Output properties: Slump ($80\sim 210\ \text{mm}$), 28 d compressive strength ($21.0\sim 60.0\ \text{MPa}$).
- **Convex Hull optimization algorithm (Sections 2.2–2.4, Figs. 1–4)**:
  - Generation of $N$-dimensional convex polytopes via QuickHull.
  - Interpolation: Non-linear multi-variate regression and support vector machines (SVM).
  - Objective function: $\text{Min } J = w_1 \cdot \text{Cost} + w_2 (\Delta f_c)^2 + w_3 (\Delta \text{Slump})^2$.
- **Experimental verification trials (Section 3, Tables 3–5)**:
  - 3 design cases: normal strength/standard flow, high strength/high flow, ultra-high strength/low slump.
  - Slump cone test (KS F 2402), 28 d compressive strength (KS F 2405).

## Results

### 1. Comparison between Convex Hull optimized targets and actual laboratory batch properties (Section 3, Tables 4–6, Figs. 5–8)

| Design Case | Target Compressive Strength ($f_{c,target}$, MPa) | Target Slump ($\text{Slump}_{target}$, mm) | Optimal W/B (%) | Optimal Cement Content ($C$, $\text{kg/m}^3$) | Measured Compressive Strength ($f_{c,exp}$, MPa) | Measured Slump ($\text{Slump}_{exp}$, mm) | Prediction Error (%) |
|---|---|---|---|---|---|---|---|
| **Case 1 (Normal / Standard)** | **$27.0\ \text{MPa}$** | **$150\ \text{mm}$** | **$48.5\%$** | **$340\ \text{kg/m}^3$** | **$27.8 \pm 0.8\ \text{MPa}$** | **$155 \pm 5\ \text{mm}$** | **$3.1\%$ (High precision)** |
| **Case 2 (High strength / Flowable)** | **$45.0\ \text{MPa}$** | **$180\ \text{mm}$** | **$34.0\%$** | **$465\ \text{kg/m}^3$** | **$46.2 \pm 1.2\ \text{MPa}$** | **$185 \pm 5\ \text{mm}$** | **$2.7\%$ (Exact match)** |
| **Case 3 (Ultra-high strength)** | **$60.0\ \text{MPa}$** | **$120\ \text{mm}$** | **$27.5\%$** | **$540\ \text{kg/m}^3$** | **$58.5 \pm 1.5\ \text{MPa}$** | **$115 \pm 5\ \text{mm}$** | **$3.4\%$** |
| **Conventional Trial Mix (Control)** | $45.0\ \text{MPa}$ | $180\ \text{mm}$ | $36.0\%$ | $510\ \text{kg/m}^3$ | $44.5 \pm 2.0\ \text{MPa}$ | $170 \pm 15\ \text{mm}$ | $6.5\%$ (Excess cement) |

### 2. Polytope interpolation stability and cost analysis
- **Prevention of extrapolation failure**: Confining solutions within the convex hull prevents AI models from recommending unfeasible or physically irrational mix proportions.
- **$15\%$ cost reduction**: Optimized binder and superplasticizer dosages saved $45\ \text{kg}$ of cement per $\text{m}^3$ of concrete at equivalent strength.

- **Overall conclusion**: This landmark paper introduced the computational convex hull algorithm to concrete mix design, demonstrating that bounding the feasible interpolation domain enables target strength and workability predictions within 4.5% error.

## Related Notes

- [[kim-2007-simulation-parameters-surface-wave-propagation-concrete-ann]] — KAIST & Prof. Bang Yeon Lee: ANN inversion of concrete non-destructive parameters.
- [[sustainability-low-carbon-binders]] — Low-carbon eco-friendly concrete mix optimization frameworks.
- [[high-strength-strain-hardening-composites]] — High-performance concrete mix design framework.
- [[concrete-durability-and-service-life]] — Concrete quality control and durability assurance.
