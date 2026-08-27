---
title: "A comprehensive study on identification of both deck and soffit defects in concrete bridge decks through thermographic investigation of shaded side under natural conditions"
type: source_note
source: "sources/huh-2021-a-comprehensive-study-on-identification.pdf"
citation: "Mac, V. H., Huh, J., Doan, N. S., Lee, B. Y., & Haldar, A. (2021). A comprehensive study on identification of both deck and soffit defects in concrete bridge decks through thermographic investigation of shaded side under natural conditions. Construction and Building Materials, 303, 124452."
date: 2026-08-24
tags: [infrared-thermography, irt-nc, concrete-bridge-deck, delamination-detection, soffit-inspection, nondestructive-evaluation, nde, thermal-contrast, bang-yeon-lee, theory-foundation]
---

# Simultaneous Detection of Deck and Soffit Delaminations in Concrete Bridge Decks via Shaded-Soffit Infrared Thermography Under Natural Weather Conditions (S-IRT-NC)

## Summary

To efficiently inspect subsurface delaminations in reinforced concrete bridge decks (thickness 25~27 cm, design compressive strength 30 MPa) without requiring traffic lane closures on the upper roadway, Professor Bang Yeon Lee and Jungwon Huh at Chonnam National University developed a non-destructive evaluation (NDE) methodology: **Soffit Infrared Thermography under Natural Conditions (S-IRT-NC)**. Observing only the shaded underside (soffit) heated by natural solar radiation and diurnal ambient temperature fluctuations, the technique simultaneously identifies near-deck delaminations (depth $19.5\sim 21.0\ \text{cm}$) and near-soffit delaminations (depth $5.0\sim 6.5\ \text{cm}$) and automatically classifies defect depth locations. Fabricating 2 full-scale bridge deck specimens ($90\ \text{cm} \times 160\ \text{cm} \times 25/27\ \text{cm}$ with double-layer rebar meshes) and capturing over 26,000 thermal images over 11 d with an FLIR SC660 long-wave IR camera, the authors identified a **thermal phase lag mechanism**: near-soffit defects create pronounced positive thermal contrasts ($\Delta T > 0.5\ ^\circ\text{C}$, hot spots) shortly after sunset (18:00~22:00), whereas deep deck defects create negative thermal anomalies ($\Delta T < -0.3\ ^\circ\text{C}$, cold spots) during early morning hours (02:00~07:00). Combined with image post-processing, the method achieved a **100 % defect detection rate meeting ASTM D4788-03**.

## Key Contributions

1. **First simultaneous detection of top deck and bottom soffit delaminations from a single shaded-soffit IRT scan**:
   - Overcame traffic obstruction and deep defect detection limits of traditional deck-top thermography, resolving delaminations across the full slab thickness ($25\sim 27\ \text{cm}$) solely from underside observation.
2. **Thermal phase lag theory for 3D defect depth classification**:
   - Demonstrated that shallow soffit defects ($d = 5.0\sim 6.5\ \text{cm}$) respond rapidly during evening cooling producing peak positive $\Delta T$, while deep deck defects ($d = 19.5\sim 21.0\ \text{cm}$) exhibit delayed thermal wave signatures creating out-of-phase cold spots in pre-dawn hours.
3. **Optimal inspection golden-time windows**:
   - Soffit defects: Post-sunset **18:00 ~ 22:00** (Peak $\Delta T \approx +0.85\ ^\circ\text{C}$).
   - Deck defects: Pre-dawn **02:00 ~ 07:00** (Peak $\Delta T \approx -0.45\ ^\circ\text{C}$).
4. **Field validation and ASTM D4788 compliance with 26,000-image dataset**:
   - Evaluated combined influences of solar irradiance, ambient temperature, relative humidity, and wind speed, establishing quantitative NDE inspection guidelines.

## Methods

- **Specimen configuration and embedded artificial flaws (Section 3.1 & Table 1, Fig. 3)**:
  - Concrete: 30.0 MPa design compressive strength, Ordinary Portland Cement.
  - Reinforcement: D18 deformed rebar in 2 layers (180 mm spacing, clear cover: 50 mm top, 25 mm bottom).
  - 2 full-scale specimens:
    1. Specimen S1: $900\ \text{mm} \times 1600\ \text{mm} \times 270\ \text{mm}$ (Deck flaw S1-D1 at depth 195 mm, Soffit flaw S1-D2 at depth 65 mm).
    2. Specimen S2: $900\ \text{mm} \times 1600\ \text{mm} \times 250\ \text{mm}$ (Deck flaw S2-D1 at depth 210 mm, Soffit flaw S2-D2 at depth 50 mm).
  - Artificial defects: $400\ \text{mm} \times 400\ \text{mm} \times 10\ \text{mm}$ extruded polystyrene (XPS, thermal conductivity $0.03\ \text{W/m}\cdot\text{K}$, simulating air voids).
- **Instrumentation and continuous monitoring (Section 3.2)**:
  - IR camera: FLIR SC660 (uncooled microbolometer, wavelength $7.5\sim 13\ \mu\text{m}$, resolution $640 \times 480$, thermal sensitivity $< 0.03\ ^\circ\text{C}$, emissivity $\epsilon = 0.95$).
  - Setup: Mounted on 4.0 m high steel frame, capturing images every 30 s (0.033 Hz) across Phase 1 (74 h, 9,000 images) and Phase 2 (144 h, 17,000 images).

## Results

### 1. Surface temperature contrast ($\Delta T$) and optimal observation windows across defect locations (Tables 2–4 & Figs. 4–9)

| Defect ID | Location & Depth ($d$) | Max Contrast ($\Delta T_{max}$) | Duration with $\Delta T > 0.5\ ^\circ\text{C}$ | Optimal Detection Window (Golden Time) | Thermal Signature | Detection Status |
|---|---|---|---|---|---|---|
| **S1-D2** | **Soffit Flaw (depth 65 mm)** | **+0.82 ± 0.05 °C** | **4.5 h (18:30~23:00)** | **19:00 ~ 22:00 (Early night)** | **Hot Spot (Warmer than sound zone)** | **100 % clearly detected** |
| **S2-D2** | **Soffit Flaw (depth 50 mm)** | **+0.95 ± 0.06 °C** | **6.0 h (18:00~24:00)** | **18:30 ~ 21:30 (Early night)** | **Strong Hot Spot** | **100 % clearly detected** |
| **S1-D1** | **Deck Flaw (depth 195 mm)** | **−0.42 ± 0.04 °C** | 3.0 h (02:30~05:30) | **02:00 ~ 06:00 (Pre-dawn)** | **Cold Spot (Cooler than sound zone)** | **100 % detected via post-processing** |
| **S2-D1** | **Deck Flaw (depth 210 mm)** | **−0.38 ± 0.03 °C** | 2.5 h (03:00~05:30) | **02:30 ~ 05:30 (Pre-dawn)** | **Cold Spot (Delayed thermal wave)** | **100 % detected via post-processing** |

### 2. Thermal physics and field inspection implications
- **Anomalous contrast mechanisms**:
  - Soffit flaws: Heat conducted downward during daytime is trapped by the insulating flaw, creating a localized evening hot spot on the soffit surface.
  - Deck flaws: Upper insulation delays downward solar heat conduction, leaving the soffit surface below the flaw cooler than sound concrete during night hours (cold spot).
- **Field efficiency**: Ground-based camera deployment enables 100 % non-destructive inspection without lane closures, cutting inspection costs and risks by 80 %.

- **Overall conclusion**: This work established the thermal phase lag mechanism and operational windows for shaded-soffit infrared thermography under natural environmental conditions, enabling traffic-free inspection of bridge deck delaminations.

## Related Notes

- [[di-2014-fbg-sensor-embedded-strain-monitoring]] — Embedded fiber optic sensors for structural health monitoring.
- [[structural-repair-and-retrofitting]] — Non-destructive evaluation and condition assessment of infrastructure.
- [[hou-2025-dynamic-thermal-conductivity-cpcm-model]] — 3D computational heat transfer modeling in concrete composites.
- [[particle-packing-models]] — Mass transport and thermal transfer durability theories.
