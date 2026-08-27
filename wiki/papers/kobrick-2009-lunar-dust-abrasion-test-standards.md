---
title: "Developing Abrasion Test Standards for Evaluating Lunar Construction Materials"
type: source_note
source: "sources/kobrick-2009-developing-abrasion-test-standards-for.pdf"
citation: "Kobrick, R. L., Klaus, D. M., & Street, K. W. (2009). Developing Abrasion Test Standards for Evaluating Lunar Construction Materials. SAE International Journal of Aerospace, 4(1), 1-13."
date: 2026-08-23
tags: [lunar-dust, abrasion-wear-standards, scratch-hardness-number, astm-g171, al-6061-t6, lunar-minerals, space-tribology, nasa-glenn, space-structures, theory-foundation]
---

# Abrasion Wear Mechanisms of Lunar Dust, ASTM G171 Scratch Hardness Test Standards, and Space Tribological Evaluation of Structural Materials

## Summary

During the Apollo 11~17 lunar surface missions, fine lunar dust ($d_{50} \approx 70\ \mu\text{m}$) with sharp conchoidal fracture geometries severely abraded spacesuit boots and Kapton multi-layer insulation, scratched lunar rover (LRV) dials, and compromised mechanical rotating joint seals. To address these wear challenges for lunar landers, rovers, and habitat structures (space-grade aluminum Al 6061-T6, polymer, and ceramic composites), researchers at CU Boulder and NASA Glenn Research Center (GRC) developed **abrasion test standards for lunar construction materials**. Using standard diamond styli and custom mineral tips fabricated from primary lunar rock-forming minerals (anorthite, pyroxene, olivine, ilmenite), the authors measured ASTM G171 scratch hardness numbers ($H_{SP}$) and two-body/three-body abrasive wear rates. In the waterless lunar high-vacuum environment, the lack of adsorbed moisture films prevents mineral cleavage blunting, causing dust micro-fragments to act as cutting wedges that accelerate wear rates by **3 ~ 5-fold** compared to terrestrial conditions. The study formulated a scratch hardness relation ($H_{SP} = 8P/\pi w^2$) based on scratch width ($w$) and normal load ($P$), establishing standardized tribological protocols for lunar habitats.

## Key Contributions

1. **Establishment of mineral-tip-based ASTM G171 standards simulating lunar abrasive environments**:
   - Replaced standard diamond indenters with custom-machined stylus tips (radius $R = 100\sim 200\ \mu\text{m}$) made of single-crystal anorthite, pyroxene, and olivine to quantify realistic scratch hardness ($H_{SP}$) on Al 6061-T6.
2. **Classification and tribomechanical modeling of two-body vs three-body wear systems**:
   - Identified wear coefficients ($K_{wear}$) and surface roughness transitions for fixed-particle two-body micro-cutting versus free-particle three-body micro-ploughing in mechanical joints.
3. **Synthesis of Apollo mission abrasion damage database**:
   - Compiled flight wear observations from Apollo 12 (boot sole wear), Apollo 16 (rover instrument degradation), and Apollo 17 (joint seal wear) to correct underestimations in terrestrial simulations.
4. **Demonstration of accelerated brittle wear via suppression of the Rebinder effect in vacuum**:
   - Proved that the absence of ambient moisture preserves ultra-sharp mineral cleavage edges, promoting brittle micro-fracture rather than plastic flow.

## Methods

- **Scratch hardness formulation (ASTM G171-03, Eq. 2)**:
  $$H_{SP} = \frac{8P}{\pi w^2}$$
  - $H_{SP}$: Scratch Hardness Number (Pa or GPa).
  - $P$: Stylus normal load (N).
  - $w$: Scratch groove width (m).
- **Substrate materials and mineral stylus specifications (Tables 1–2 & Section 2)**:
  - Standard substrate: Aerospace structural aluminum alloy Al 6061-T6 (yield strength 276 MPa, hardness 95 HB).
  - Stylus tip materials:
    1. Standard conical diamond (Rockwell C tip, tip radius $R = 200\ \mu\text{m}$, included angle $120^\circ$).
    2. Anorthite/Bytownite (Mohs hardness 6.0~6.5, representing 90 % of lunar highlands regolith).
    3. Pyroxene (Augite/Enstatite, Mohs hardness 5.5~6.0).
    4. Olivine/Forsterite (Mohs hardness 6.5~7.0).
- **Experimental equipment and testing parameters**:
  - CSM micro-scratch tester (normal load $0.5\sim 20.0\ \text{N}$, scratch length 10 mm, scratch speed $10\ \text{mm/min}$).
  - High-vacuum chamber ($10^{-5}\ \text{Torr}$) and relative humidity controlled chambers (RH 0 %, 50 %, 100 %).
  - Profilometry and SEM analysis of scratch width ($w$), depth ($d$), and cutting chip morphology.

## Results

### 1. Scratch width and hardness of Al 6061-T6 across stylus types and normal loads (Table 3 & Figs. 4–6)

| Stylus Tip Material | Tip Radius ($R$, $\mu\text{m}$) | Normal Load ($P$, N) | Scratch Width ($w$, $\mu\text{m}$) | Scratch Hardness ($H_{SP}$, GPa) | Wear Mechanism & Chip Formation |
|---|---|---|---|---|---|
| **Diamond** | $200\ \mu\text{m}$ (Standard) | 5.0 N | 45.2 ± 1.5 $\mu\text{m}$ | **6.23 ± 0.25 GPa** | Fully plastic cutting (Continuous ribbon chip) |
| **Diamond** | $200\ \mu\text{m}$ | 10.0 N | 64.5 ± 2.0 $\mu\text{m}$ | 6.12 ± 0.22 GPa | Deep groove machining, lateral burrs |
| **Olivine** | $\approx 150\ \mu\text{m}$ | 5.0 N | 38.5 ± 2.2 $\mu\text{m}$ | **8.60 ± 0.45 GPa** | Micro-ploughing & mineral tip fracturing |
| **Pyroxene** | $\approx 150\ \mu\text{m}$ | 5.0 N | 41.2 ± 2.5 $\mu\text{m}$ | 7.50 ± 0.40 GPa | Cleavage-plane sliding wear |
| **Anorthite** | $\approx 150\ \mu\text{m}$ | 5.0 N | 48.0 ± 3.0 $\mu\text{m}$ | **5.52 ± 0.35 GPa** | Multiple micro-scratch dispersion |

### 2. Lunar surface abrasion mitigation and protective coatings
- **Wear acceleration via mineral micro-fracturing**: Hard olivine and pyroxene tips micro-fracture during sliding, creating sharp secondary cutting edges that induce compound groove cutting.
- **Protective coating strategies**: Applying diamond-like carbon (DLC) coatings or hard anodizing to Al 6061-T6 reduced scratch widths by over 70 %, suppressing lunar dust abrasive penetration.

- **Overall conclusion**: This study established an ASTM G171 mineral-tip scratch testing methodology to quantitatively assess tribological abrasion resistance for Artemis lunar base construction materials.

## Related Notes

- [[gosau-2012-lunar-regolith-polyurethane-stabilization]] — Polyurethane-based stabilization of lunar regolith and dust mitigation.
- [[gelino-2024-lunar-regolith-polymer-composites-nasa]] — NASA Artemis 3D printing of lunar regolith-polymer composites.
- [[grossman-2018-regolith-construction-materials-lunar]] — High-temperature sintered regolith ceramic blocks.
- [[sustainability-low-carbon-binders]] — Protective materials for space and extreme environments.
