---
title: "Planetary Construction 3D Printing Using Lunar and Martian In Situ Materials"
type: source_note
source: "sources/giwa-2023-planetary-construction-3d-printing-using.pdf"
citation: "Giwa, I., Moore, D., Fiske, M., & Kazemian, A. (2023). Planetary Construction 3D Printing Using Lunar and Martian In Situ Materials. In Earth and Space 2022 (pp. 817-831). Reston, VA: American Society of Civil Engineers (ASCE)."
date: 2026-08-23
tags: [planetary-construction, 3d-printing-c3dp, lunar-regolith, martian-regolith, isru, sulfur-concrete, geopolymer, additive-manufacturing, asce, theory-foundation]
---

# Review of Waterless Binder Systems and Extreme-Environment Extrusion Mechanics for Lunar and Martian Planetary Construction 3D Printing (Planetary C3DP)

## Summary

To build landing pads, protective berms, habitat shelters, and radiation shielding structures for NASA's Artemis program and human Mars exploration while minimizing Earth-supplied payload and maximizing in-situ resource utilization (100 % ISRU), Professor Ali Kazemian at Louisiana State University and researchers at NASA Marshall Space Flight Center (MSFC) conducted a landmark state-of-the-art review on material systems, extrusion kinematics, and extreme environmental physics in Planetary Construction 3D Printing (Planetary C3DP). Addressing the severe constraints of waterless lunar and Martian environments (ultra-high vacuum $10^{-6}\ \text{Torr}$, reduced gravity $1/6\text{g} \sim 3/8\text{g}$, extreme temperatures $-180\ ^\circ\text{C} \sim 123\ ^\circ\text{C}$), the authors systematically evaluated the print rheology (extrudability, buildability, open time), interlayer bond strength, and durability of four primary binder systems: **thermally molten sulfur concrete ($130\sim 140\ ^\circ\text{C}$)**, **geopolymers/alkali-activated materials (AAM)**, **regolith-polymer composites (RPC)**, and **selective solar/microwave sintering**.

## Key Contributions

1. **Material classification of four major waterless/low-water 3D printing binder systems**:
   - **Sulfur concrete**: Rapid solidifying upon cooling from $135\ ^\circ\text{C}$ with 25~35 wt.% molten sulfur binder, developing **35 ~ 45 MPa compressive strength** within 1 h as a zero-water prime candidate.
   - **Geopolymers**: Hydrothermal alkali activation of clay/regolith achieving 20~30 MPa.
   - **Regolith-polymer composites (RPC)**: Thermoplastic melt extrusion yielding 40~55 MPa.
   - **Direct solar/microwave sintering**: Binder-free direct fusing at $1100\ ^\circ\text{C}$ yielding 2~5 MPa.
2. **Analysis of extreme planetary environmental effects on 3D printability**:
   - **Vacuum flash evaporation**: Rapid evaporation of free water induces poor cement hydration, confirming the necessity of waterless molten binders.
   - **Low gravity ($1/6\text{g}$)**: Lower hydrostatic self-weight pressure reduces bottom-layer deformation, enhancing vertical buildability 6-fold relative to Earth conditions.
3. **Autonomous robotic C3DP architectural framework**:
   - Formulated end-to-end autonomous robotic workflows encompassing excavation, crushing/grading, thermal mixing, robotic arm nozzle extrusion, and layer-by-layer thermal bonding.

## Methods

- **Planetary surface environmental parameters**:
  - **Moon**: Atmospheric pressure $\approx 10^{-10}\ \text{Pa}$ (high vacuum), gravity $1.62\ \text{m/s}^2$ ($1/6\text{g}$), temperature range $-180\ ^\circ\text{C} \sim 123\ ^\circ\text{C}$, regolith composed of $\text{SiO}_2, \text{Al}_2\text{O}_3, \text{FeO}, \text{CaO}$.
  - **Mars**: Atmospheric pressure $\approx 636\ \text{Pa}$ ($\text{CO}_2$ 95 %), gravity $3.71\ \text{m/s}^2$ ($3/8\text{g}$), temperature range $-114\ ^\circ\text{C} \sim 20\ ^\circ\text{C}$, regolith rich in $\text{SiO}_2, \text{Fe}_2\text{O}_3$, sulfates, and perchlorates.
- **Evaluated C3DP technologies and metrics (Tables 1–3)**:
  - Extrusion-based C3DP (continuous nozzle deposition).
  - Powder-bed 3D printing (D-Shape selective binder jetting).
  - Contour crafting.
  - Metrics: Compressive strength, flexural strength, plastic viscosity, up-mass ratio, water consumption, and energy requirements.

## Results

### 1. Comparison of major binder systems for planetary construction 3D printing (Comprehensive Synthesis)

| Binder system | Reaction & hardening mechanism | Water consumption (%) | Processing temperature | 28 d / ultimate compressive strength (MPa) | Earth up-mass dependency | Planetary suitability & limitations |
|---|---|---|---|---|---|---|
| **Sulfur concrete** | Molten sulfur phase change ($135\ ^\circ\text{C}$) | **0.0 % (Zero water)** | $120\sim 140\ ^\circ\text{C}$ | **35 ~ 45 MPa (1 h rapid)** | Very low (in-situ sulfur extraction) | **Optimal for Moon/Mars (thermal cycle crack caution)** |
| **Regolith-polymer (RPC)** | Thermoplastic melt bonding | **0.0 % (Zero water)** | $180\sim 220\ ^\circ\text{C}$ | **40 ~ 55 MPa** | $15\sim 20\ \text{wt.\%}$ up-mass | High toughness, good radiation shielding |
| **Geopolymer** | Alkali solution ($\text{NaOH/Na}_2\text{SiO}_3$) hydration | $10\sim 15\ \text{wt.\%}$ | $60\sim 80\ ^\circ\text{C}$ | 20 ~ 30 MPa | Activator shipment required | Requires sealed anti-evaporation curing chamber |
| **Solar direct sintering** | High-temperature regolith fusion | **0.0 %** | $1100\sim 1400\ ^\circ\text{C}$ | 2 ~ 5 MPa (Brittle fracture) | **0.0 % (100 % ISRU)** | Requires massive solar concentrators/power |

### 2. Planetary rheology and interface behavior
- **Rheological advantages of sulfur concrete**: Liquid sulfur ($\mu \approx 10\ \text{mPa}\cdot\text{s}$) enables low-pressure pumping of dense regolith slurries, solidifying rapidly below $119\ ^\circ\text{C}$ via $\beta$-monoclinic to $\alpha$-orthorhombic phase transition to support formwork-free vertical building.
- **Microgravity deposition mechanics**: Reduced gravitational acceleration prevents green slump deformation, maximizing continuous layer build height.

- **Overall conclusion**: This review established the technological roadmap, material selection matrices, and robotic processing parameters for planetary construction 3D printing in lunar and Martian environments.

## Related Notes

- [[gelino-2024-lunar-regolith-polymer-composites-nasa]] — NASA Artemis lunar regolith polymer composite 3D printing.
- [[geng-2025-novel-lunar-3d-printing-roll-pressing]] — Low-binder roller-compacted lunar regolith 3D printing.
- [[desai-1991-lunar-simulant-structural-materials]] — Sintered basalt ceramic composites from lunar regolith at 1100 °C.
- [[sustainability-low-carbon-binders]] — Low-carbon and waterless binders for extreme environments.
