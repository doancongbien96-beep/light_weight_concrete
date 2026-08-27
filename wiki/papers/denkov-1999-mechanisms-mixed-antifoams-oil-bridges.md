---
title: "Mechanisms of Action of Mixed Solid-Liquid Antifoams. 2. Stability of Oil Bridges in Foam Films"
type: source_note
source: "sources/denkov-1999-mechanisms-of-action-of-mixed.pdf"
citation: "Denkov, N. D. (1999). Mechanisms of Action of Mixed Solid-Liquid Antifoams. 2. Stability of Oil Bridges in Foam Films. Langmuir, 15(25), 8530-8542."
date: 2026-08-24
tags: [antifoams, mixed-solid-liquid-antifoam, oil-bridges, foam-film-rupture, laplace-capillarity, neumann-triangle, three-phase-contact-angle, garrett-bridging-coefficient, langmuir, theory-foundation]
---

# Rupture Mechanisms of Foam Films by Mixed Solid-Liquid Antifoams (Silica-Silicone Oil): Capillary Instability of Oil Bridges and Laplace Interfacial Deformation Modeling

## Summary

To quantitatively elucidate the essential physicochemical mechanisms by which mixed antifoams (hydrophobic silica particles + silicone oil emulsion)—widely used to defoam and rupture excessively entrained harmful air bubbles in cement concrete chemical admixtures (superplasticizer SP) and aqueous surfactant solutions—destroy foam films, Professor Nikolai D. Denkov of Rhodia Chimie and Sofia University conducted this foundational interfacial chemistry study. Extending Garrett's classical bridging coefficient ($B$) theory by combining high-speed video microscopy of oil droplet penetration with a coupled three-dimensional integral analysis of the Laplace capillary pressure equilibrium equation ($\Delta P = \sigma(1/R_1 + 1/R_2)$) and Neumann vector triangle ($\vec{\sigma}_{AW} + \vec{\sigma}_{OW} + \vec{\sigma}_{OA} = 0$) accounting for surface deformations (nodoid, unduloid surfaces) of foam films, the author mathematically proved that oil bridges formed within foam films bifurcate into two distinct regimes depending on three-phase contact angles ($\theta_{OW}, \theta_{OA}$) and the ratio of bridge size to film thickness: (1) "mechanically unstable bridges" that spontaneously stretch within milliseconds ($\text{ms}$) to rupture the film, and (2) "metastable bridges" that maintain capillary equilibrium and persist for several seconds. Furthermore, a complete foam rupture phase diagram was established under the condition that the bridging coefficient $B = \sigma_{AW}^2 + \sigma_{OW}^2 - \sigma_{OA}^2 > 0$, where interfacial tension imbalances accelerate liquid drainage to destroy foam bubbles.

## Key Contributions

1. **Mathematical formalization of the bridging-stretching mechanism of oil bridges**:
   - Capillary unbalanced forces and stretching rates generated when an oil droplet pierces both surfaces of a foam film to form a bridge were derived via Laplace differential equations.
2. **Generalized bridge equilibrium analysis incorporating film surface curvatures (nodoid/unduloid)**:
   - Overcame Garrett's planar bridge assumption and rigorously analyzed the three-dimensional interfacial profile of real foam films using elliptic integrals.
3. **Derivation of critical contact angle ($\theta_{OW} < 90^\circ$) governing bridge instability and rupture**:
   - Established the thermodynamically unstable regime where oil bridges spontaneously expand through the interaction of oil-water interfacial tension ($\sigma_{OW}$) and air-water interfacial tension ($\sigma_{AW}$).
4. **Establishment of defoaming efficiency map as a function of droplet size to film thickness ratio ($R_{drop}/h$)**:
   - Provided quantitative guidelines for optimizing antifoam emulsion droplet sizes essential for controlling bubble diameters and pore structures in cement pastes.

## Methods

- **Thermodynamic and capillary geometric modeling (Sections 2–4)**:
  - Three interfaces: air-water (AW), oil-water (OW), and oil-air (OA).
  - Interfacial tension parameters: $\sigma_{AW}, \sigma_{OW}, \sigma_{OA}$.
  - System of Laplace capillary pressure equations:
    $$\frac{dz}{dr} = \pm \frac{r(C + \frac{\Delta P}{2\sigma} r^2)}{\sqrt{r^2 - [r(C + \frac{\Delta P}{2\sigma} r^2)]^2}}$$
  - Neumann vector equilibrium at the three-phase contact line:
    $$\cos\theta_{OW} = \frac{\sigma_{AW}^2 + \sigma_{OW}^2 - \sigma_{OA}^2}{2 \sigma_{AW} \sigma_{OW}} = \frac{B}{2\sigma_{AW}\sigma_{OW}} + 1$$
- **Numerical analysis procedure (Section 5)**:
  - Fourth-order Runge-Kutta numerical integration based on incomplete elliptic integrals $F(\varphi, q)$ and $E(\varphi, q)$.
  - Coupled iterative solver developed for bridge radius $r_C$, film radius $r_P$, and capillary pressure difference $\Delta P_{OW}$.

## Results

### 1. Thermodynamic parameters and stability classification of antifoam oil bridges (Tables 1–2 & Figs. 1–5)

| Bridge behavior type | Bridging coefficient ($B$) condition | Contact angle ($\theta_{OW}$) | Oil spreading coefficient ($S$) | Film deformation mode | Time required for rupture | Defoaming efficiency |
|---|---|---|---|---|---|---|
| **Mechanically unstable bridge** | **$B > 0$ (positive)** | **$\theta_{OW} < 90^\circ$** | **$S > 0$ (spontaneous spreading)** | **Nodoid stretching $\rightarrow$ neck thinning** | **$< 5\ \text{ms}$ (ultra-fast rupture)** | **Extremely high (ideal defoaming)** |
| **Metastable bridge** | $B < 0$ (negative) | $\theta_{OW} > 90^\circ$ | $S < 0$ (non-spreading) | Unduloid capillary equilibrium | Persists for seconds to tens of seconds | Incomplete defoaming |
| **Non-bridging droplet** | - | No contact formed | - | Spherical suspended droplet | No rupture | Ineffective |

### 2. Rupture kinetics and interfacial mechanism analysis
- **Spontaneous stretching of oil bridges**: When $B > 0$, the vector sum of the three interfacial tensions acts outward from the bridge waist, causing rapid thinning of the bridge neck and inducing capillary pinch-off within $3\sim 5\ \text{ms}$, completely collapsing the foam film.
- **Catalytic role of hydrophobic silica particles**: The presence of hydrophobic silica particles on oil droplet surfaces locally pierces the air-water interface, accelerating oil bridge formation by more than 100-fold.

- **Overall conclusion**: This work mathematically formalized foam film rupture mechanisms of mixed antifoams via three-dimensional Laplace capillary analysis and contact-angle thermodynamics, establishing the fundamental standard framework for modern colloid and concrete defoaming chemistry.

## Related Notes

- [[choi-2015-basalt-fiber-bonding-orientation-strength]] — Antifoams and interfacial tension control in cementitious composites.
- [[particle-packing-models]] — High-density packing frameworks for concrete via bubble defoaming.
- [[alkali-activated-materials]] — Bubble control and defoaming techniques in alkaline solutions.
- [[particle-packing-models]] — Elimination of entrapped macro-pores and durability enhancement via defoaming.
