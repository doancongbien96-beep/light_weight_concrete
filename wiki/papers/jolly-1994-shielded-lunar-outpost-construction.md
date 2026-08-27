---
title: "Design and Construction of Shielded Lunar Outpost"
type: source_note
source: "sources/jolly-1994-design-and-construction-of-shielded.pdf"
citation: "Jolly, S. D., Happel, J., & Sture, S. (1994). Design and Construction of Shielded Lunar Outpost. Journal of Aerospace Engineering, 7(4), 417-434."
date: 2026-08-24
tags: [lunar-outpost, radiation-shielding, lunar-soil-mechanics, regolith-excavation, lunar-scraper-vehicle, tied-arch-superstructure, nasa-flo, asce-jae, colorado-boulder, theory-foundation]
---

# Regolith Shielding Structures (Tied-Arch, Trench, and Wall) and Autonomous Lunar Scraper Vehicle (LSV) Construction Simulation for Long-Duration Lunar Outposts (NASA FLO)

## Summary

In support of NASA's First Lunar Outpost (FLO) mission for human crews staying 6 months or longer, protection against galactic cosmic rays (GCR), solar proton events (SPE), hypervelocity micrometeoroids, and extreme thermal cycles requires $1.0\sim 4.0\ \text{m}$ of lunar regolith cover. Professor Stein Sture and co-workers at the University of Colorado at Boulder evaluated **four shielding structural typologies—Option 1 (lightweight Tied-Arch roof), Option 2 (In-Trench burial), Option 3 (freestanding Retaining Wall), and Option 4 (natural slope Berm/Mound)**. Considering the cutting mechanics of dense sub-surface regolith ($\rho \approx 2.0\ \text{g/cm}^3$ at depths of 20 cm or greater), the authors modeled an autonomous **Lunar Scraper-Tractor Vehicle (LSV: total mass 1300 kg, bucket capacity $0.25\ \text{m}^3$, cutting depth 1.4 cm, powered by $\text{Ni-H}_2$ batteries)** to simulate earthmoving volumes ($500\sim 3500\ \text{m}^3$), travel distances, construction energy (MJ), and completion hours. Among the four configurations, **the lightweight Tied-Arch roof reduced total excavation volume by over 40 % to $1200\ \text{m}^3$ and completed construction in 120 h (850 LSV cycles, 3200 MJ)**, establishing mechanical design benchmarks for space earthmoving equipment operating under reduced gravity traction limits.

## Key Contributions

1. **Comparative analysis of 4 regolith shielding structural concepts (Tied-Arch vs Trench vs Wall vs Mound)**:
   - Demonstrated that the Tied-Arch superstructure avoids the massive earthwork volume surges caused by regolith angle of repose limits ($\phi = 35^\circ\sim 40^\circ$), reducing earthmoving by over 40 %.
2. **Design and rating of lightweight remote lunar scraper vehicle (LSV 1300 kg)**:
   - Formulated a shallow $1.4\ \text{cm}$ cutting depth and $0.305\ \text{m/s}$ speed to prevent wheel slip and overturning under 1/6 gravity.
3. **Quantification of constructability across regolith shielding depths ($1.0\ \text{m}$ vs $4.0\ \text{m}$)**:
   - Established radiation risk versus energy expenditure trade-off curves comparing 1.0 m cover ($750\ \text{m}^3$, 80 h) with 4.0 m full shielding ($2800\ \text{m}^3$, 280 h).
4. **Soil mechanics modeling of lunar regolith excavation and tractive resistance**:
   - Integrated depth-dependent shear strength ($c = 0.1\sim 1.0\ \text{kPa}, \phi = 35^\circ\sim 48^\circ$) and wheel-soil traction models to accurately compute hauling and loading power.

## Methods

- **Shielding structural configurations (Section: Structural Concepts & Figs. 1–2)**:
  - Option 1 (Tied-Arch): Lightweight aluminum tied-arch truss roof + sandwich plate distributing regolith loads to perimeter footings.
  - Option 2 (In-Trench): Excavating a trench, placing habitat modules, and backfilling to grade level.
  - Option 3 (Retaining Wall): Erecting perimeter retaining wall panels and backfilling regolith.
  - Option 4 (Mound/Berm): Building a natural sloped regolith mound over surface modules at a $35^\circ$ angle of repose.
- **LSV vehicle parameters and simulation inputs (Fig. 2)**:
  - Total vehicle mass: 1300 kg (tare mass 925 kg + payload 375 kg, volume $0.25\ \text{m}^3$).
  - Mobility and scraping: Travel speed $0.305\ \text{m/s}$ (1.1 km/h), scraping cut depth 1.4 cm, loading cycle duration 59 s.
  - Power: $275\ \text{kg}$ $\text{Ni-H}_2$ rechargeable battery pack (12 h operating shift).

## Results

### 1. Earthmoving volumes, construction time, and energy consumption across shielding options (Tables 1–3 & Figs. 2–4)

| Shielding Option | Cover Depth (m) | Excavation Volume ($\text{m}^3$) | LSV Operating Cycles | Travel Distance (km) | Construction Time (Hours) | Energy Consumption (MJ) | Constructability Rating |
|---|---|---|---|---|---|---|---|
| **Option 1 (Tied-Arch)** | **1.0 m** | **680 ± 25** | **450 cycles** | **95 km** | **68 h (Lowest)** | **1850 MJ (Lowest)** | **Superior (Optimal)** |
| **Option 1 (Tied-Arch)** | **4.0 m** | **1850 ± 50** | **1230 cycles** | **260 km** | **185 h** | **5100 MJ** | **High efficiency** |
| **Option 2 (In-Trench)** | 1.0 m | 1150 ± 40 | 760 cycles | 165 km | 115 h | 3200 MJ | Moderate |
| **Option 2 (In-Trench)** | 4.0 m | 3200 ± 80 | 2130 cycles | 450 km | 320 h | 8800 MJ | Difficult excavation |
| **Option 3 (Retaining Wall)** | 1.0 m | 850 ± 30 | 560 cycles | 120 km | 85 h | 2400 MJ | Panel erection needed |
| **Option 4 (Mound/Berm)** | 4.0 m | **3650 ± 100 (Max)** | **2430 cycles** | **520 km** | **370 h (Longest)** | **10200 MJ (Max)** | **Poor (Volume surge)** |

### 2. Earthmoving mechanics and construction engineering
- **Inefficiency of unconfined berms**: Angle of repose constraints in Option 4 broadened the footprint to over 25 m width, doubling earthmoving ($3650\ \text{m}^3$ vs $1850\ \text{m}^3$) and extending construction time to 370 h.
- **Structural advantages of Tied-Arch**: Option 1 transferred soil dead load directly to peripheral ground footings, shielding the habitat modules from surcharge loads while minimizing earthwork volume.

- **Overall conclusion**: This work established quantitative construction simulations for lunar radiation shielding, proving the superiority of Tied-Arch superstructures and defining equipment operating envelopes for autonomous lunar earthmoving vehicles.

## Related Notes

- [[jablonski-2008-technical-requirements-lunar-structures]] — Technical requirements and building codes for lunar habitats.
- [[benaroya-2008-lunar-base-engineering-framework]] — Structural engineering framework for lunar bases.
- [[benaroya-2002-engineering-design-construction-lunar-bases]] — ASCE landmark on lunar base engineering, design, and construction.
- [[dyke-2024-standards-lunar-isru-materials]] — Testing standards for lunar ISRU materials and landing pads.
