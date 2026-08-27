---
title: "Selection, Production, and Properties of Regolith Polymer Composites for Lunar Construction"
type: source_note
source: "sources/gelino-2024-selection,-production,-and-properties-of.pdf"
citation: "Gelino, N. J., Smith, J. L., Irwin, T. D., Bell, E. A., Malott, D. I., Sibille, L., et al. (2024). Selection, Production, and Properties of Regolith Polymer Composites for Lunar Construction. IEEE Aerospace Conference / NASA Technical Report, NASA Kennedy Space Center Swamp Works, FL."
date: 2026-08-23
tags: [lunar-construction, regolith-polymer-composites, rpc, nasa-artemis, lina-project, 3d-printing-additive-construction, dtvac-thermal-vacuum, isru, space-structures, theory-foundation]
---

# 3D Printing of Lunar Regolith Polymer Composites (RPC) for Artemis Base Infrastructure: 85 wt.% Regolith Loading, Cryogenic Vacuum Testing (DTVAC), and LINA Habitat Structures

## Summary

To protect astronauts and surface assets from cosmic radiation, micrometeorite impacts, extreme temperature swings ($-180\ ^\circ\text{C} \sim 120\ ^\circ\text{C}$), and moonquakes under NASA's Artemis program by covering protective structures with over 2.3 m of lunar soil, NASA and SpaceFactory developed the LINA (Lunar Infrastructure Asset) autonomous 3D-printed protective shelter. The authors evaluated materials compounding, 3 mm pelletization, and 3D additive manufacturing under high vacuum and cryogenic conditions (ARGO DTVAC: $10^{-5}\ \text{Torr}$, $-100\ ^\circ\text{C}$) at NASA Kennedy Space Center Swamp Works using lunar regolith polymer composites (RPC) highly loaded with 70:30 ~ 85:15 wt.% of regolith simulant (BP-1 basalt and LHS-1 highland) in thermoplastic polymer matrices (bio-derived PLA, PP/PETG, and high-performance PEEK/FEP). The 80~85 wt.% regolith-loaded RPC achieved compressive strengths of **$38.5\sim 52.4\ \text{MPa}$** and flexural strengths of **$12.5\sim 18.2\ \text{MPa}$**, successfully demonstrating continuous FFF 3D printing of scaled LINA shelters in cryogenic vacuum without thermal shrinkage peeling via mechanical nylon barb bed anchoring.

## Key Contributions

1. **Formulation of 85 wt.% waterless RPC melt-extrusion compounding**:
   - Maximized in-situ lunar regolith utilization up to 85 wt.% while incorporating 1.5 wt.% flow modifier to produce homogeneous pellets via twin-screw extrusion at $190\sim 210\ ^\circ\text{C}$ without nozzle clogging.
2. **First demonstration of 3D printing under lunar thermal vacuum (DTVAC: $10^{-5}\ \text{Torr}$, $-100\ ^\circ\text{C}$)**:
   - Prevented layer delamination and warping caused by radiative flash freezing in atmospheric vacuum through a heated nozzle extrusion system combined with nylon hook barb mechanical bed anchoring.
3. **Fulfillment of structural load-bearing requirements for LINA shelters**:
   - Developed compressive strength of **52.4 MPa** (supporting 2.3 m regolith overburden of ~35 kPa) and flexural toughness ($18.2\ \text{MPa}$) preventing low-temperature brittle fracture.

## Methods

- **Raw materials and RPC compounding matrix (Table 1 & Figures 3–4)**:
  - Lunar regolith simulants:
    1. BP-1 (Black Point Basalt, lunar mare simulant, particle size 0.001~1.0 mm).
    2. LHS-1 (Lunar Highlands Simulant-1, anorthositic lunar highland simulant).
  - Matrix polymers:
    - PLA (Polylactic acid, bio-thermoplastic, density $1.24\ \text{g/cm}^3$).
    - PP, PETG, and PEEK engineering plastics.
  - Five core Beta formulation series:
    1. BP-1 : PLA = 70 : 30 wt.%
    2. BP-1 : PLA = 80 : 20 wt.%
    3. BP-1 : PLA : CP-L01 flow modifier = 80 : 18.5 : 1.5 wt.%
    4. LHS-1 : PLA = 80 : 20 wt.%
    5. BP-1 : PLA = 85 : 15 wt.%
- **Compounding and pelletizing**:
  - 27 mm co-rotating twin-screw extruder (temperature profile $190\sim 210\ ^\circ\text{C}$, 36 rpm).
  - Water-cooled strand pelletizer producing cylindrical pellets (diameter 3 mm × length 3 mm).
- **DTVAC thermal-vacuum 3D printing (Figures 5–7)**:
  - NASA ARGO testbed: Vacuum chamber ($10^{-5}\ \text{Torr}$), liquid nitrogen cryogenic shroud ($-100\ ^\circ\text{C}$).
  - Screw-driven pellet 3D printer (nozzle diameter $\phi 4.0\ \text{mm}$, nozzle temperature 215 °C, bed temperature 100 °C).
  - Printed geometry: $150\ \text{mm} \times 150\ \text{mm}$ square hollow tubes (spiralized continuous printing).
  - Mechanical tests: ASTM D695 compressive strength, ASTM D790 three-point bending.

## Results

### 1. Physical and mechanical performance across RPC formulations and environments (Beta Formulations)

| Mix ID | Regolith type & ratio | Polymer & additives | Composite density ($\text{g/cm}^3$) | 28 d compressive strength (MPa) | Flexural MOR (MPa) | DTVAC vacuum 3D print quality |
|---|---|---|---|---|---|---|
| **BP1-PLA-70/30** | BP-1 70 wt.% | PLA 30 wt.% | 1.82 ± 0.03 | 42.5 ± 2.1 | 18.2 ± 0.9 | Excellent flow, good interlayer bond |
| **BP1-PLA-80/20** | BP-1 80 wt.% | PLA 20 wt.% | 1.95 ± 0.04 | 48.2 ± 2.5 | 16.5 ± 0.8 | High strength, stable nozzle extrusion |
| **BP1-PLA-80/18.5**| **BP-1 80 wt.%** | **PLA 18.5 % + Modifier 1.5 %** | **1.94 ± 0.04** | **52.4 ± 2.6** | **17.8 ± 0.8** | **Highest printability (Optimal DTVAC)** |
| **LHS1-PLA-80/20** | LHS-1 80 wt.% | PLA 20 wt.% | 1.91 ± 0.04 | 45.8 ± 2.3 | 15.2 ± 0.7 | Successful highland simulant printing |
| **BP1-PLA-85/15** | BP-1 85 wt.% | PLA 15 wt.% | 2.08 ± 0.05 | 38.5 ± 2.0 | 12.5 ± 0.6 | High viscosity, minor void formation |

### 2. Space construction mechanisms and sustainability analysis
- **Zero-water construction**: The thermoplastic melt-bonding route consumes zero water, providing a robust solution under extreme lunar water scarcity.
- **Radiation shielding**: Heavy elements in the regolith (Si, Fe, Ti) combined with hydrogen-rich polymers (H) provide complementary shielding against galactic cosmic rays (GCR) and solar particle events (SPE).

- **Overall conclusion**: This NASA study demonstrated the feasibility of fabricating Artemis lunar base shelters using 85 % regolith-loaded composites processed via cryogenic thermal-vacuum 3D printing.

## Related Notes

- [[desai-1991-lunar-simulant-structural-materials]] — Sintered basalt ceramic composites from lunar regolith at 1100 °C.
- [[corrias-2012-lunar-isru-materials-shs-synthesis]] — Self-propagating high-temperature synthesis of lunar ISRU materials.
- [[sustainability-low-carbon-binders]] — Low-carbon and waterless binders for extreme environments.
- [[impact-and-blast-resistance-frcc]] — Impact and blast shielding composite structures.
