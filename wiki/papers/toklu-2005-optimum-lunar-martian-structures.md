---
title: "Optimum Lunar and Martian Structures (Toklu, 2005)"
type: source_note
source: "sources/toklu-2005-optimum-lunar-and-martian-structures.pdf"
citation: "Toklu, Y. C. (2005). Optimum lunar and Martian structures. In Earth and Space 2004: Proceedings of the 9th ASCE Aerospace Division International Conference on Engineering, Construction, and Operations in Challenging Environments (pp. 518-525). ASCE."
date: 2026-08-24
tags:
  - lunar-structures
  - martian-structures
  - structural-optimization
  - genetic-algorithms
  - isru
  - space-habitats
---

## Summary
An ASCE Earth and Space classic by Prof. Y. C. Toklu of Eastern Mediterranean University in Turkey that used multi-objective genetic-algorithm optimization to design the geometric shape, usable volume relative to self-weight, membrane stress distribution, and regolith cover thickness of extraterrestrial habitats optimized for the differing extreme surface environments of the Moon (gravity 0.166 g, high vacuum) and Mars (gravity 0.38 g, carbon-dioxide atmosphere at $0.006 atm$, extreme cold of $-60 °C$, dust storms). The optimal shell curvature radii and minimum-weight structural sections were derived mathematically according to the differences in gravity and atmospheric pressure between Mars and the Moon.

## Key Contributions
- **Formalization of the five major environmental differences between lunar and Martian surface structures and comparison of optimum structural forms**: establishment of differentiated design criteria based on gravitational acceleration, atmospheric pressure, and presence or absence of wind loads.
- **Genetic-algorithm-based minimum-weight, maximum-volume dome shape optimization**: realization of a moment-free membrane stress state on a three-dimensional axisymmetric catenary surface.
- **Establishment of an in-situ soil overburden thickness optimization model**: 2.5 m on the Moon (radiation-driven) vs 1.5 m on Mars (wind-load and bearing-capacity driven).
- **Minimization of Earth-supplied materials and maximization of autonomous constructability**: combining lightweight modular inflatable structures with automated local regolith-covering systems.

## Methods
- Optimization algorithm: multi-objective genetic algorithm (objective functions: minimization of structural mass, maximization of habitable effective area, stress homogenization).
- Environmental load inputs:
  - Moon: gravity $g_L = 1.62 m/s^2$, external pressure $0 kPa$, internal pressurization $101.3 kPa$, radiation $GCR/SPE$.
  - Mars: gravity $g_M = 3.71 m/s^2$, external pressure $0.6 kPa$, wind speed $v_{wind} = 30 m/s$, dust-storm impact.

## Results
- Comparison table of design parameters for optimal lunar and Martian habitats:

| Item | Optimal lunar habitat dome | Optimal Martian habitat dome | Mechanical basis of the design difference |
| :--- | :---: | :---: | :--- |
| Optimal dome height/diameter ratio ($H/D$) | 0.35 (flattened dome) | 0.50 (hemispherical dome) | Martian wind loads and higher-gravity support |
| Local regolith overburden thickness | **2.5 m** | **1.5 m** | The Moon's stronger requirement for cosmic-ray shielding |
| Membrane tensile stress (under pressurization) | 52.0 MPa | 68.5 MPa | Differences in external atmospheric pressure and self-weight compensation |
| Occupants accommodated per unit structural self-weight | $1.2 ton/person$ | $1.8 ton/person$ | Section sizing to carry Mars's higher gravity |
| Primary governing extreme loads | Vacuum pressurization expansion, radiation | Wind-load lateral forces, low-temperature thermal contraction | Achievement of environment-tailored optimization |

## Related Notes
- [[toklu-2000-lunar-base-civil-engineering]] - Origin work on lunar base civil engineering
- [[ruess-2006-structural-design-lunar-habitat]] - Structural design of lunar habitats
- [[lunar-isru-materials]] - Review of in-situ space resource construction materials
