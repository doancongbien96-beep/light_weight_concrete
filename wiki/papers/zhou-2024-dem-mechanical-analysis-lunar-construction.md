---
title: "DEM Mechanical Analysis of Lunar Construction and Regolith Structures (Zhou et al., 2024)"
type: source_note
source: "sources/zhou-2024-research-and-application-of-dem.pdf"
citation: "Zhou, Z., Zhang, Y., & Liu, J. (2024). Research and application of discrete element method (DEM) in lunar geotechnical engineering and regolith construction. Advances in Space Research, 73(5), 2450-2465. https://doi.org/10.1016/j.asr.2023.11.025"
date: 2026-08-24
tags:
  - lunar-construction
  - discrete-element-method
  - lunar-regolith-mechanics
  - isru
  - low-gravity
  - space-civil-engineering
---

## Summary
This 2024 research paper developed a three-dimensional discrete element method (DEM) space geotechnical engineering analysis framework that combines non-spherical particle cluster shapes with a van der Waals micro-adhesion model, in order to simulate computationally the excavation, transport, compaction, and sintering of lunar in-situ soil (regolith) and the bearing capacity and soil-structure interaction (SSI) of the regolith shielding wall placed over habitat domes under the extreme low-gravity (1/6 g) and ultra-high-vacuum environment of the lunar surface. Under 1/6 g low gravity, it numerically demonstrated the internal friction angle of regolith ($\phi = 42°$), the ultimate bearing capacity ($q_{ult}$), and the structural safety of a 3 m regolith-covered dome.

## Key Contributions
- **Establishment of a 3D DEM regolith particle model tailored to lunar low-gravity and vacuum environments**: implementation of irregular crushed shapes and micro-adhesion ($c = 0.5 \sim 2.5 kPa$).
- **Stability analysis of the 3 m regolith shielding layer above lunar habitat modules**: quantification of the earth pressure distribution under seismic vibration and of the arching effect.
- **Derivation of the optimal bucket shape for unmanned automatic excavation rovers**: a 40 % saving in excavation energy consumption compared with Earth gravity.
- **Establishment of engineering standards for lunar base infrastructure construction**: provision of foundational data for NASA and CNSA lunar base construction.

## Methods
- DEM analysis: the PFC3D discrete element solver with the contact Hertz-Mindlin contact model plus a micro-adhesion model.
- Environmental parameters: gravitational acceleration $g = 1.62 m/s^2$; particle size distribution taken from Apollo 11 soil samples ($d_{50} = 72 \mu m$).
- Experimental validation: comparison against triaxial compression test data of simulant soil inside a parabolic-flight microgravity chamber at 1/6 g.

## Results
- Analysis data on regolith ground mechanics and the structural stability of regolith covering under lunar low gravity:

| Analysis item | Earth environment (1 g) | Lunar environment (1/6 g) | Influence and characteristics of the space environment |
| :--- | :---: | :---: | :--- |
| Regolith unit weight | $18.5 kN/m^3$ | **$3.08 kN/m^3$** | Reduced bearing capacity from the 1/6 decrease in self-weight |
| Effective internal friction angle $\phi$ | 40.5° | **42.8°** | Increased frictional interlocking of clean vacuum-exposed surfaces |
| Ultimate bearing capacity of shallow foundations $q_{ult}$ | 450 kPa | **125 kPa** | A 72 % reduction in ground bearing capacity (countermeasures required) |
| Overburden pressure on top of the 3 m soil-cover dome | 55.5 kPa | **9.25 kPa** | Substantial relief of structural load (reduced dome self-weight) |

## Related Notes
- [[toklu-2000-lunar-base-civil-engineering]] - original source on civil engineering of lunar bases
- [[ruess-2006-structural-design-lunar-habitat]] - structural design of lunar habitat structures
- [[lunar-isru-materials]] - review of construction materials from space in-situ resources