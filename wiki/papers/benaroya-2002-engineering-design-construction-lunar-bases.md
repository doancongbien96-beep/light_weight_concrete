---
title: "Engineering, Design and Construction of Lunar Bases"
type: source_note
source: "sources/benaroya-2002-engineering,-design-and-construction-of.pdf"
citation: "Benaroya, H., Bernold, L., & Chua, K. M. (2002). Engineering, Design and Construction of Lunar Bases. Journal of Aerospace Engineering, 15(2), 33-45."
date: 2026-08-24
tags: [lunar-bases, space-structures, structural-mechanics, inflatable-structures, regolith-shielding, robotic-construction, hyperbolic-soil-model, asce-jae, rutgers-university, theory-foundation]
---

# Structural engineering, design, and construction framework of lunar bases: structural typology, regolith geomechanics, radiation shielding, and robotic automated construction

## Summary

To establish the core civil and structural engineering tasks of permanent human settlement
on the Moon and forward outposts for deep-space exploration, Prof. Haym Benaroya's team at
Rutgers University consolidated decades of lunar-base construction research and systematically
framed **structural typology (rigid modules, inflatable membranes, trusses, lava-tube
underground bases, regolith concrete, sintered arches), a nonlinear hyperbolic soil-foundation
mechanics model for lunar regolith, minimum $2.5\sim 3.0\ \text{m}$ shielding-layer design,
and remote autonomous robotic construction** under the Moon's extreme environment —
**ultra-high vacuum ($10^{-12}\ \text{Torr}$), severe thermal cycling over the 28-day cycle
($-180\ ^\circ\text{C} \sim +120\ ^\circ\text{C}$), lethal space radiation (GCR/SPE),
hypervelocity micrometeorites ($10\sim 70\ \text{km/s}$), and one-sixth gravity
($1.62\ \text{m/s}^2$)**. The team clarified the equilibrium mechanism between tensile stress
from internal pressurization ($1.0\ \text{atm} \approx 101.3\ \text{kPa}$) and external
regolith load, and demonstrated via nonlinear FEA that foundation bearing capacity degrades
below the terrestrial level in low gravity as confining stress drops — an essential guide for
space architectural and civil structural design.

## Key Contributions

1. **Classification map of six core lunar-base structural types completed**: merits,
   drawbacks, and technology readiness levels fully established for rigid modules, inflatable
   dual-membrane structures, space trusses, natural lava tubes, and in-situ sintered regolith arches.
2. **Nonlinear hyperbolic soil model for lunar regolith**: developed a computational framework
   predicting settlement of large optical-telescope foundations and base pads using the
   nonlinear $\sigma$-$\varepsilon$ relation.
3. **Optimal regolith overburden ($2.5\sim 3.0\ \text{m}$) quantified for radiation and
   thermal shielding**: design equation for a cover keeping annual human dose below
   $5\ \text{rem}$ while damping the external $-180\sim +120\ ^\circ\text{C}$ swing to a
   constant interior $+20\ ^\circ\text{C}$.
4. **Robotic autonomous excavation-construction systems minimizing astronaut EVA**: process
   chart for surface module placement, regolith backfilling, and remote interlocking-block assembly.

## Methods

- **Lunar environmental loads and boundary conditions (Section 2 & Table 1)**:
  - Pressure differential: internal pressurization $P_{in} = 101.3\ \text{kPa}$ (1.0 atm)
    versus near-zero external vacuum (tension-dominated).
  - Thermal load: repeated expansion/contraction of $\Delta T = 300\ ^\circ\text{C}$ over the
    28-day solar day.
  - Gravity: $g_{moon} = 1.62\ \text{m/s}^2$ ($1/6 g$).
  - Radiation: galactic cosmic rays (GCR) and solar particle events (SPE).
- **Per-type mechanics and ground design (Sections 3–6)**:
  - Inflatables: Kevlar/Mylar composite fiber membranes + structural foam fill + external
    torus supports.
  - Soil-foundation mechanics: Duncan-Chang nonlinear hyperbolic constitutive FEA (initial
    modulus $E_i = K P_a (\sigma_3/P_a)^n$).
  - Shielding thickness: optimization of regolith layer depth by mass stopping-power computation.

## Results

### 1. Comparison table of mechanics, pros/cons, and shielding requirements by structure type (Tables 1~3 & Appendix)

| Type | Principal material | Earth-mass efficiency | Ease of assembly | Pressurization support | Required shield depth | Strengths / limits |
|---|---|---|---|---|---|---|
| **Rigid cylinder modules** | Al-Li alloy / composites | low (fixed volume) | very easy (direct landing) | circumferential ring tension | **$2.5\sim 3.0\ \text{m}$ regolith** | proven tech / launch volume limits |
| **Inflatable membrane** | Kevlar/Mylar multi-layer | **excellent (vacuum packing)** | **good (auto-deployment)** | **membrane tension** | **$2.5\sim 3.0\ \text{m}$ (external torus)** | large volumes / puncture vulnerability |
| **Truss space frame** | CFRP | good | medium (robotic assembly) | nodal axial force transfer | attached regolith panels | high stiffness / needs extra membrane for sealing |
| **Underground lava-tube base** | natural basalt rock ceiling | **best (no skin transport)** | difficult (vertical access) | natural rock arch compression | **natural shielding complete ($>10\ \text{m}$)** | perfect radiation/meteorite shield / exploration difficulty |
| **ISRU sintered regolith arch** | 100 % sintered regolith | best (100 % local material) | long robotic build time | arch compressive thrust line | self-shielding ($0.5\sim 1.0\ \text{m}$) | minimal transport cost / high-energy lasers required |

### 2. Structural mechanics and shielding engineering interpretation
- **Self-cancellation of pressurization versus overburden**: the upward pressure from
  $101.3\ \text{kPa}$ internal air far exceeds the weight of a $2.5\ \text{m}$ overburden
  ($\gamma_{moon} h \approx 1.5\ \text{g/cm}^3 \times 1.62\ \text{m/s}^2 \times 2.5\ \text{m}
  \approx 6.1\ \text{kPa}$), so the structure always sits in pure tension — cable ties and
  foundation anchors are mandatory.
- **The low-gravity bearing paradox**: at $1/6 g$, structure self-weight also falls to $1/6$,
  but ultimate bearing capacity ($q_{ult} = c N_c + q N_q + 0.5 \gamma B N_\gamma$) collapses
  even faster through reduced confining stress, requiring larger footing areas than on Earth.

- **Overall conclusion**: this immortal classic is the first comprehensive engineering
  consolidation of lunar-base structural mechanics, inflatables, regolith geomechanics,
  radiation shielding, and robotic construction.

## Related Notes

- [[dyke-2024-standards-lunar-isru-materials]] — test standards for lunar ISRU structural
  materials and landing-pad design.
- [[he-2025-lunar-base-insitu-functional-materials]] — Chang'e-5 regolith basalt fiber and ISRU
  composites origin paper.
- [[high-strength-strain-hardening-composites]] — extreme-environment high-strength structural
  composite framework.
- [[particle-packing-models]] — lunar regolith particle packing and geomechanics models.
