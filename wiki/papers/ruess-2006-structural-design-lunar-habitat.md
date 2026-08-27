---
title: "Structural Design of a Lunar Habitat (Ruess et al., 2006)"
type: source_note
source: "sources/ruess-2006-structural-design-of-a-lunar.pdf"
citation: "Ruess, F., Schaenzlin, J., & Benaroya, H. (2006). Structural design of a lunar habitat. Journal of Aerospace Engineering, 19(3), 133-157. https://doi.org/10.1061/(ASCE)0893-1321(2006)19:3(133)"
date: 2026-08-24
tags:
  - lunar-habitat
  - structural-design
  - inflatable-structures
  - regolith-shielding
  - thermal-vacuum-analysis
  - finite-element-modelling
---

## Summary
An immortal classic paper in the ASCE Journal of Aerospace Engineering by the research team of Prof. H. Benaroya at Rutgers University, comprehensively presenting the structural design, three-dimensional nonlinear finite element analysis (FEA), and thermal-cycle reliability evaluation of a hybrid habitat dome structural system that combines multi-layer inflatable membrane structures with an external lunar soil (regolith) overlay shielding layer (thickness 2.0 ~ 3.0 m) to maximize the structural safety, pressurized containment integrity, and protection capability against space radiation and micrometeoroids of a permanent lunar surface habitat module (Lunar Habitat). An optimal arch-dome geometry was derived in which the internal pressurization ($101.3 kPa$) and the gravity load of the upper 3 m of regolith balance each other.

## Key Contributions
- **Establishment of a hybrid inflatable-regolith structural system for lunar habitat modules**: optimized load-balance design between internal tensile pressurization and external compressive soil pressure.
- **Composite shield design of a multi-layer protection membrane (Kevlar, Kapton, Nextel)**: complete shielding against micrometeoroid impacts ($v = 20 km/s$).
- **Buckling and stress concentration analysis through three-dimensional nonlinear FEA**: ultimate structural safety factor $SF > 2.5$ secured under seismic events and local pressure loss.
- **Thermal stress buffering design under lunar thermal cycles ($-150 \sim +120 °C$)**: the high heat capacity of the 3 m regolith layer maintains the interior structure temperature at $20 \pm 2 °C$.

## Methods
- Structural model: dome-shaped inflatable module 12 m in diameter and 6 m in height (Kevlar 49 woven membrane fabric, tensile strength 3000 MPa).
- FEA: ANSYS nonlinear large-deformation shell and solid coupled analysis.
- Load conditions: internal pressurization $101.3 kPa$, lunar gravity $1.62 m/s^2$, upper regolith load (density $1800 kg/m^3$, thickness 2.5 m).

## Results
- Stress and safety factor analysis results for the lunar habitat structure under each load condition:

| Load condition | Max membrane tensile stress (MPa) | Shell compressive stress (MPa) | Max deflection displacement (mm) | Structural safety factor ($SF$) |
| :--- | :---: | :---: | :---: | :---: |
| Pressurization only ($101.3 kPa$) | 145.2 | - | +28.5 (expansion) | 3.85 |
| Pressurization + 2.5 m regolith overlay | 42.0 | 12.5 | -4.2 (balanced state) | 4.50 |
| Loss-of-pressurization emergency condition | - | 38.5 | -65.0 (compressive settlement) | 2.15 |

## Related Notes
- [[lunar-isru-materials]] — overview of in-situ resource utilization construction materials for space
- [[cesaretti-2014-lunar-soil-3d-printing]] — 3D-printing construction of lunar bases
- [[lin-1985-concrete-lunar-base-construction]] — origin work on concrete construction for lunar bases
