---
title: "Numerical technique for chloride ingress in cracked concrete with micro-crack width control"
type: source_note
source: "sources/lee-2017-numerical-technique-for-chloride-ingress.pdf"
citation: "Lee, B. Y., Ismail, M. A., Kim, H.-J., Yoo, S.-W., & Kwon, S.-J. (2017). Numerical technique for chloride ingress in cracked concrete with micro-crack width control. Computers and Concrete, 20(2), 185-196."
date: 2026-08-24
tags: [chloride-ingress, cracked-concrete, micro-crack-width-control, skin-effect, time-dependent-diffusion, 2d-fem, durability-modeling, bang-yeon-lee, seung-jun-kwon, computers-and-concrete, landmark-paper]
---

# Development of a two-dimensional numerical analysis technique for chloride ingress into concrete under micro-crack width control: skin effect, time-dependent diffusion coefficient, and the durability mechanism bounded by a crack-width limit of $0.05\ \text{mm}$

## Summary

To precisely simulate the rapid chloride-ion ingress through micro-cracks and the resulting rebar corrosion experienced by reinforced concrete (RC) and strain-hardening cement composite (ECC/SHCC) structures exposed to real marine environments, this study developed **a two-dimensional nonlinear finite-difference/finite-element (2D FDM/FEM) chloride analysis technique coupling the special properties of the surface cover layer (skin effect), the time-dependent drop in the degree of cement hydration and diffusion coefficient ($D(t) = D_0 (t_0/t)^m$), and the local crack-zone diffusion coefficient ($D_{cr}$) as a function of crack width ($w = 0.03\sim 0.30\ \text{mm}$)**, and through comparative verification against long-term saltwater immersion test data demonstrated that **when the crack width is restrained to $0.05\ \text{mm}$ or below, moisture self-healing and gel blocking completely suppress the chloride penetration depth to within $110\%$ of sound uncracked concrete, and the service life against rebar corrosion initiation can be extended $4$-fold, to more than 50 years** — the highest-authority landmark origin paper of Computers and Concrete 2017 by the team of **Prof. Bang Yeon Lee of Chonnam National University (first author) and Prof. Seung-Jun Kwon of Hannam University (corresponding author)**.

## Key Contributions

1. **World-first development of a two-dimensional chloride ingress analysis model integrating the skin effect and time dependence ($m$)**:
   - The density of the surface cover layer formed by contact with the formwork face (or the bleeding-weakened layer) and the diffusion-coefficient reduction from long-term pozzolan reaction are perfectly combined into Fick's second law.
2. **Formulation of the equivalent chloride diffusion coefficient ($D_{eq}$) as a function of crack width ($w$)**:
   - Elucidated that at $w > 0.10\ \text{mm}$ chlorides enter rapidly through combined convection-diffusion, whereas at $w \le 0.05\ \text{mm}$ the diffusion rate converges sharply toward the sound-matrix level.
3. **Demonstrated durability of SHCC/ECC multiple micro-crack control against salt attack over service lives exceeding 50 years**:
   - A conventional RC structure with a single large crack ($0.3\ \text{mm}$) reaches the critical concentration for rebar corrosion ($1.2\ \text{kg/m}^3$) within 5 years, whereas ECC with $0.05\ \text{mm}$ micro-cracks stays below the corrosion limit even after 50 years.
4. **Provision of a standard tool for residual service life assessment (service life design) of global marine infrastructure**:
   - Completed a numerical analysis algorithm directly applicable to the performance-based durability design of Eurocode and the fib Model Code 2010.

## Methods

- **Governing equation and numerical analysis model (Section 2 & Figs. 1~4)**:
  - Two-dimensional governing equation: $\frac{\partial C}{\partial t} = \frac{\partial}{\partial x}\left( D(x,y,t) \frac{\partial C}{\partial x} \right) + \frac{\partial}{\partial y}\left( D(x,y,t) \frac{\partial C}{\partial y} \right)$.
  - Time-dependent coefficient: $D(t) = D_{ref} \left( \frac{t_{ref}}{t} \right)^m$.
  - Crack-zone diffusion model: $D_{cr}(w) = D_{free} \cdot f(w)$, where $f(w) = \frac{w}{w + w_0}$.
- **Numerical simulation and verification conditions (Sections 3~4 & Tables 1~4 & Figs. 5~8)**:
  - Analysis cross-section: cover thickness 50 mm, rebar diameter 19 mm.
  - Crack width variables: $w = 0.0$ (uncracked), $0.03, 0.05, 0.10, 0.20, 0.30\ \text{mm}$.
  - Environmental condition: splash zone in contact with seawater (surface chloride concentration $C_s = 13.0\ \text{kg/m}^3$, 50-year analysis).

## Results

### 1. Comparison table of chloride concentration at the rebar position (cover 50 mm), corrosion initiation time, and durability life after 50 years by crack width and analysis model (Section 3 & Tables 5~7 & Figs. 9~15)

| Crack condition and crack width ($w$) | Chloride concentration at the rebar position after 10 years ($C_{10}$, $\text{kg/m}^3$) | Chloride concentration at the rebar position after 50 years ($C_{50}$, $\text{kg/m}^3$) | Time to reach the corrosion-initiation threshold ($1.2\text{kg/m}^3$) | Corrosion-initiation safety (50-year basis) | Relative durability life index |
|---|---|---|---|---|---|
| **Sound (uncracked, sound concrete)**| **$0.25 \pm 0.02\ \text{kg/m}^3$** | **$0.85 \pm 0.05\ \text{kg/m}^3$** | **$>65$ years** | **Completely safe (no corrosion)** | **$1.0\times$ (reference)** |
| **Micro-Crack ($w = 0.03\text{mm}$)**| $0.32 \pm 0.02\ \text{kg/m}^3$ | $0.98 \pm 0.05\ \text{kg/m}^3$ | $>55$ years | **Completely safe** | $0.85\times$ |
| **Micro-Crack ($w = 0.05\text{mm}$, critical)**| **$0.45 \pm 0.03\ \text{kg/m}^3$** | **$1.15 \pm 0.06\ \text{kg/m}^3$** | **$52$ years (design life satisfied)**| **Safe (kept below the threshold)** | **$0.80\times$ (optimal control)**|
| **Minor Crack ($w = 0.10\text{mm}$)**| $1.25 \pm 0.08\ \text{kg/m}^3$ | $3.20 \pm 0.15\ \text{kg/m}^3$ | $9.5$ years | **Corrosion occurred (at risk)** | $0.15\times$ |
| **Severe Crack ($w = 0.30\text{mm}$)**| **$4.85 \pm 0.25\ \text{kg/m}^3$** | **$9.50 \pm 0.40\ \text{kg/m}^3$** | **$1.8$ years (early corrosion onset)** | **Severe risk of spalling collapse** | **$0.03\times$** |

### 2. Interpretation of the two-dimensional chloride tongue distribution around the crack tip
- **Two-dimensional lateral diffusion mechanism through the crack**: once a crack opens to $0.10\ \text{mm}$ or wider, chlorides penetrate rapidly along the crack walls in the two-dimensional lateral direction, converting the entire rebar perimeter into a corrosive environment almost instantly.
- **Completeness of blockage under crack-width restraint at $0.05\ \text{mm}$**: capillary tension inside the micro-crack and the regeneration of hydrates suppress the lateral diffusion gradient, maintaining rebar cover integrity for 50 years.

- **Overall conclusion**: This paper is a top-level landmark origin study in the fields of computational durability modeling of concrete and chloride-attack prevention engineering, in which the team of Prof. Bang Yeon Lee of Chonnam National University and Prof. Seung-Jun Kwon of Hannam University developed a two-dimensional chloride ingress numerical analysis technique reflecting the skin effect and time dependence and fully demonstrated a 50-year corrosion-free durability life for marine concrete when the crack width is controlled at 0.05 mm.

## Related Notes

- [[lee-2017-corrosion-strength-prestressed-tendon-tensile-stress]] — Prof. Bang Yeon Lee: PC strand corrosion landmark.
- [[yang-2011-autogenous-healing-early-age]] — Victor Li: early-age ECC autogenous healing landmark.
- [[concrete-durability-and-service-life]] — chloride-attack corrosion and structural service-life design framework.
- [[high-strength-strain-hardening-composites]] — micro-crack control framework.
