---
title: "Regolith stabilization and building materials for the lunar surface"
type: source_note
source: "sources/gosau-2012-regolith-stabilization-and-building-materials.pdf"
citation: "Gosau, J. M. (2012). Regolith stabilization and building materials for the lunar surface. In Earth and Space 2012 (pp. 243-249). Reston, VA: American Society of Civil Engineers (ASCE)."
date: 2026-08-23
tags: [lunar-regolith, polyurethane-resin, regolith-stabilization, automated-brick-builder, isru, low-outgassing, space-structures, asce, theory-foundation]
---

# Lunar Surface Regolith Stabilization, Structural Block Fabrication, and Automated Manufacturing Using Low-Outgassing Polyurethane Binders

## Summary

To prevent hazardous lunar dust dispersal (particle size $40\sim 80\ \mu\text{m}$) and construct landing pads, roads, and protective berms for lunar bases, Dr. Jan-Michael Gosau at Adherent Technologies Inc. (ATI) developed a lunar regolith stabilization process utilizing low-outgassing two-part polyurethane resin binders, reducing Earth-transported binder mass to **only 2~5 wt.%** (with **95~98 wt.%** in-situ regolith utilization). The author developed a PLC-controlled automated brick builder robot performing polyol pre-coating and dust-free compression molding within disposable polyethylene liner bags. Applying a two-step mixing protocol—pre-coating simulant (JSC-1A) with polyol before introducing isocyanate—reduced binder consumption by **75 % from >20 % down to 5 wt.%**, while hydraulic press-molded blocks achieved compressive strengths of **$25.4\sim 34.8\ \text{MPa}$**, establishing a foundational technology for unmanned lunar infrastructure construction.

## Key Contributions

1. **75 % reduction in Earth-supplied binder requirements (5 wt.% binder, 95 wt.% regolith)**:
   - Formulated a two-step mixing protocol that micro-coats polyol onto regolith grain surfaces prior to isocyanate injection, forming complete crosslinked polymer bridges with only 5 wt.% (5 %) binder.
2. **Formulation of low-outgassing resin for lunar vacuum**:
   - Selected multifunctional aromatic isocyanates and polymeric polyols satisfying NASA vacuum mass-loss standards (CVCM < 0.1 %) to eliminate volatile gas release in lunar vacuum.
3. **Demonstration of automated robotic brick builder with disposable liners**:
   - Fabricated a contamination-free automated unit using pneumatic actuators and PLC controls to meter, mix, compact, and eject blocks within thin polyethylene bags without requiring water cleaning.

## Methods

- **Materials and resin chemistry (Sections 2–3)**:
  - Lunar regolith simulant: JSC-1A (mean grain diameter $d_{50} = 45\ \mu\text{m}$, basaltic composition).
  - Two-part polyurethane system:
    1. Part A (Polyol): Multifunctional polyether/polyester polyol with wetting surfactants.
    2. Part B (Isocyanate): Low-volatility polymeric MDI aromatic polyisocyanate ($\text{NCO/OH}$ ratio = 1.05).
  - Binder mass fractions: 2 wt.%, 3.5 wt.%, 5.0 wt.%, and 10.0 wt.% relative to regolith.
- **Block fabrication and robotics (Figures 2–3)**:
  - Mixing protocol: Polyol-regolith pre-mixing followed by isocyanate addition and pneumatic mixing for 180 s.
  - Compaction press: 15 MPa hydraulic ram pressure ($100\ \text{mm} \times 100\ \text{mm} \times 50\ \text{mm}$ block dimensions).
  - Automated unit: AutomationDirect DirectLOGIC 205 PLC controlling 6 pneumatic actuators.
- **Testing program**:
  - Compressive strength: ASTM D695 at $1.0\ \text{mm/min}$.
  - Abrasion resistance: High-velocity lunar dust jet erosion.
  - Thermal vacuum testing: Degassing and residual strength testing in a $10^{-4}\ \text{Torr}$ vacuum chamber.

## Results

### 1. Mechanical performance of composite blocks across binder contents and mixing protocols (Table 1 & Results)

| Mixing protocol | Binder fraction (wt.%) | In-situ regolith (ISRU, wt.%) | Bulk density ($\text{g/cm}^3$) | Ambient compressive strength (MPa) | Post-vacuum compressive strength (MPa) | Failure & surface quality |
|---|---|---|---|---|---|---|
| **Direct one-step mixing (Conventional)** | 10.0 wt.% | 90.0 wt.% | 1.65 ± 0.05 | 12.5 ± 1.0 | 11.2 ± 0.9 | Resin agglomeration, porous |
| **Direct one-step mixing** | 20.0 wt.% | 80.0 wt.% | 1.82 ± 0.04 | 22.0 ± 1.5 | 20.5 ± 1.2 | Excessive binder consumption |
| **Two-step polyol pre-coating** | 2.0 wt.% | 98.0 wt.% | 1.72 ± 0.04 | 14.8 ± 0.8 | 13.9 ± 0.7 | 100 % dust suppression |
| **Two-step polyol pre-coating** | 3.5 wt.% | 96.5 wt.% | 1.88 ± 0.03 | 24.5 ± 1.2 | 23.2 ± 1.0 | Dense, homogeneous fracture |
| **Two-step polyol pre-coating** | **5.0 wt.%** | **95.0 wt.%** | **2.02 ± 0.03** | **34.8 ± 1.5** | **33.5 ± 1.4** | **Highest structural strength** |

### 2. Space engineering and operational feasibility
- **Waterless, zero-cleaning workflow**: Performing chemical polymerization inside disposable bag liners eliminates washing maintenance, enabling continuous automated block manufacturing in space vacuum.
- **Spray stabilization of regolith surfaces**: Spraying 2 wt.% low-viscosity resin penetrates and consolidates surface dust, suppressing lunar dust kicking under rover traffic.

- **Overall conclusion**: This work demonstrated that two-step polyol pre-coating reduces polyurethane binder requirements to 5 wt.%, producing 34.8 MPa structural lunar blocks in an automated robotic fabrication system.

## Related Notes

- [[gelino-2024-lunar-regolith-polymer-composites-nasa]] — NASA Artemis lunar regolith polymer composite 3D printing.
- [[geng-2025-novel-lunar-3d-printing-roll-pressing]] — Low-binder roller-compacted lunar regolith 3D printing.
- [[giwa-2023-planetary-construction-3d-printing]] — Review of planetary construction 3D printing and waterless binders.
- [[desai-1991-lunar-simulant-structural-materials]] — Sintered basalt ceramic composites from lunar regolith at 1100 °C.
