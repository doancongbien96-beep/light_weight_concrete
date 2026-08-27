---
title: "A novel 3D printing scheme for lunar construction with extremely low binder utilization"
type: source_note
source: "sources/geng-2025-a-novel-3d-printing-scheme.pdf"
citation: "Geng, Z., Wu, Z., Wang, X., Zhang, L., She, W., & Tan, M. J. (2025). A novel 3D printing scheme for lunar construction with extremely low binder utilization. Additive Manufacturing, 104230."
date: 2026-08-23
tags: [lunar-3d-printing, extremely-low-binder, roll-pressing, powder-extrusion, mortise-tenon-interlock, lunar-regolith-simulant, vacuum-dehydration, isru, theory-foundation]
---

# Novel 3D Printing Technology Integrating Roll-Pressing Compaction and Mortise-Tenon Joints for Low-Binder Lunar Regolith: 95 wt.% ISRU and Interlayer Shear Strengthening

## Summary

To overcome weak interlayer bonding, low compacted density, and excessive Earth-supplied binder dependency in 3D-printed lunar regolith structures, Professor Z. Geng and co-workers developed an integrated 3D printer printhead combining low-binder screw extrusion (< 5.0 wt.% binder, 95 wt.% lunar regolith simulant), dynamic roller compaction (38~78 N), and interlocking mortise-tenon profiled rollers under simulated lunar vacuum (10 Pa). Evaluating fine (LRS1: $d_{50} = 44\ \mu\text{m}$) and coarse (LRS2: $d_{50} = 122\ \mu\text{m}$) simulants, the authors demonstrated that applying 78 N roller compaction increased flexural strength (MOR) by **166 % (1.8 $\rightarrow$ 4.8 MPa)**, while profiled mortise-tenon rollers increased interlayer direct shear strength by **158 % (1.2 $\rightarrow$ 3.1 MPa)**, resolving cold-joint vulnerability in space additive manufacturing.

## Key Contributions

1. **Development of hybrid printhead integrating screw extrusion, roller compaction, and mortise-tenon joint profiling**:
   - Integrated dynamic compaction and mechanical interlocking directly onto extruded layers, overcoming low green strength in 95 wt.% regolith mixes with < 5.0 wt.% binder.
2. **166 % amplification in flexural strength via dynamic compaction**:
   - Applying 78 N compaction increased density from $1.52$ to $1.98\ \text{g/cm}^3$, eliminating internal inter-particle voids and raising MOR from 1.8 to 4.8 MPa.
3. **158 % increase in interlayer shear capacity via interlocking tenons**:
   - Profiled mortise-tenon joints formed geometric mechanical keys between adjacent layers, boosting direct shear strength to 3.1 MPa (1.2 MPa in control).
4. **Rapid flash-evaporation dewatering under lunar vacuum (10 Pa)**:
   - Moisture evaporated rapidly in vacuum, completing initial setting within 30 min and enabling continuous vertical layer accumulation without auxiliary heating.

## Methods

- **Raw materials and simulant properties (Figure 2 & Table 1)**:
  - Lunar regolith simulants (LRS):
    1. LRS1: Fine basaltic simulant (Apollo-17 type, $d_{50} = 44\ \mu\text{m}$, specific gravity 2.85).
    2. LRS2: Coarse simulant (Apollo-14 type, $d_{50} = 122\ \mu\text{m}$, specific gravity 2.78).
  - Binder: Low-carbon magnesia/silicate binder (< 5.0 wt.%, W/S = 0.08~0.12).
- **Printhead kinematic design (Figure 1)**:
  - Extrusion: Screw pitch 15.6 mm with three blade configurations (58 %, 73 %, 80 %, 87 %).
  - Roller compaction: Roller diameters $\phi 30\ \text{mm}, \phi 40\ \text{mm}$, and $\phi 50\ \text{mm}$, spring stiffness $K = 0.8\sim 1.6\ \text{N/mm}$ (applied loads 38 N, 55 N, 78 N).
  - Profiled tenon roller: Trapezoidal tenon profile (4 mm × 2.0 mm / 2 mm) machined along the roller circumference.
- **Testing program**:
  - Simulated lunar vacuum chamber: Pirani gauge 10 Pa, radiant heating at 44 °C.
  - Mechanical tests: Three-point bending (ASTM C1161 at 1.0 mm/min), direct interlayer shear testing.
  - Microstructure: SEM-EDS and 3D optical surface profilometry.

## Results

### 1. Physical and mechanical properties across compaction pressures and simulant types (Table 2 & Figures)

| Mixture & process condition | Roller diameter & load | Layer thickness (mm) | Bulk density ($\text{g/cm}^3$) | Flexural MOR (MPa) | Interlayer shear strength ($\tau_{inter}$, MPa) | Layer surface quality |
|---|---|---|---|---|---|---|
| **LRS1 - Uncompacted (Control)** | No roller (0 N) | 3.5 ± 0.3 mm | 1.52 ± 0.05 | 1.8 ± 0.2 MPa | 0.8 ± 0.1 MPa | Porous, high void volume |
| **LRS1 - Roller-38N** | $\phi 30\ \text{mm}$ (38 N) | 2.6 ± 0.2 mm | 1.78 ± 0.04 | 3.2 ± 0.3 MPa | 1.2 ± 0.1 MPa | Smooth surface |
| **LRS1 - Roller-78N** | $\phi 50\ \text{mm}$ (78 N) | 2.2 ± 0.1 mm (2.2 mm) | 1.98 ± 0.04 | **4.8 ± 0.4 MPa (+166 %)** | 1.5 ± 0.1 MPa | Dense, consolidated layer |
| **LRS2 - Roller-78N** | $\phi 50\ \text{mm}$ (78 N) | 2.4 ± 0.1 mm | 2.08 ± 0.05 | **4.2 ± 0.3 MPa** | 1.3 ± 0.1 MPa | Good aggregate interlocking |
| **LRS1 - Tenon-78N** | **$\phi 50\ \text{mm}$ Tenon (78 N)** | **2.2 ± 0.1 mm** | **1.96 ± 0.04** | **4.6 ± 0.3 MPa** | **3.1 ± 0.2 MPa (+158 %)** | **Interlocking tenon profile** |

### 2. Space engineering implications
- **Cold-joint mitigation**: Geometric tenons physically prevented sliding shear failure along print interfaces.
- **ISRU maximization**: Utilizing over 95 wt.% in-situ regolith reduces Earth launch logistics by over 90 % for lunar habitat construction.

- **Overall conclusion**: This work established the kinematics and material mechanics of hybrid 3D printing combining screw extrusion, dynamic roller compaction, and mortise-tenon joints for low-binder (< 5 %) high-ISRU (>95 %) lunar construction.

## Related Notes

- [[gelino-2024-lunar-regolith-polymer-composites-nasa]] — NASA Artemis lunar regolith polymer composite 3D printing.
- [[desai-1991-lunar-simulant-structural-materials]] — Sintered basalt ceramic composites from lunar regolith at 1100 °C.
- [[corrias-2012-lunar-isru-materials-shs-synthesis]] — Self-propagating high-temperature synthesis of lunar ISRU materials.
- [[sustainability-low-carbon-binders]] — Low-carbon and waterless binders for extreme environments.
