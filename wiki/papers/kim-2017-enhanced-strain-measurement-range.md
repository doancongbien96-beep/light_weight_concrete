---
title: "Enhanced Strain Measurement Range of an FBG Sensor Embedded in Seven-Wire Steel Strands (Kim et al., 2017, Sensors)"
type: source_note
source: "sources/Kim-2017-Enhanced strain measurement range of.pdf"
citation: "Kim, J.-M., Kim, C.-M., Choi, S.-Y., Lee, B.Y. Enhanced strain measurement range of an FBG sensor embedded in seven-wire steel strands. Sensors 17(7) (2017) 1654. doi:10.3390/s17071654"
date: 2026-08-22
tags: [fbg, smart-strand, prestressing, structural-health-monitoring, polyimide]
---

# Enhanced Strain Measurement Range of an FBG Sensor Embedded in Seven-Wire Steel Strands

## Summary

In smart strand technology embedding FBG sensors into hollow king wires of 7-wire strands, conventional embedded sensors suffered from a narrow maximum strain measurement range (approx. 0.65 %) below the steel yield strain (approx. 1 %). This paper resolves this issue from both material and structural aspects (Prof. Bang Yeon Lee, corresponding author). By replacing acrylate recoating with polyimide and encasing the FBG sensor inside a protective polyimide tube bonded with epoxy, the authors achieved an average maximum measurement range of 1.73 % (+88 % over unjacketed sensors), with all specimens exceeding the steel yield strain and reaching up to 2.36 %.

## Key Contributions

1. **Identification of measurement range degradation mechanisms**: Determined that microcracking in the epoxy adhesive bonding the FBG sensor inside the king wire tube causes localized fiber shear stresses, sharply degrading failure strain. Embedding into strands reduced bare fiber failure strain by 86 % for OF-A (acrylate) and 81 % for OF-P (polyimide).
2. **Quantification of recoating material effects**: Polyimide-recoated fibers (tensile strength 102 MPa, modulus 4.28 GPa, density 1.48 g/cm³) achieved a failure strain of 0.79 % vs 0.45 % for acrylate (10.7 MPa, 47.4 MPa, 0.94 g/cm³)—a 75 % increase (a 2.3-fold increase is also noted in Section 3.1). When embedded in strands, OF-P achieved a 76 % higher failure strain than OF-A.
3. **Polyimide protective tube packaging**: Encapsulated the sensor in a polyimide tube (outer diameter 1.23 mm, inner diameter 1.13 mm, tensile strength 231 MPa, modulus 2.50 GPa at 23 °C) integrated with structural epoxy (viscosity 150 cPs, Shore D hardness 85, lap shear strength 14 MPa). This elevated the average strain range from 0.92 % (FBG-P-NP, unjacketed) to 1.73 % (FBG-P-PP, tubed, +88 %).
4. **Practicality for PSC structural health monitoring**: Extended reliable strain sensing beyond the design service strain (approx. 0.9 %, 90 % of yield) and steel yielding (approx. 1 %), enabling overload post-yield tracking.

## Methods

- FBG optical principles: Bragg reflection wavelength $\lambda_B = 2 n_{eff} \Lambda$, relative wavelength shift $\Delta\lambda / \lambda_B = (1 - P_e)\Delta\varepsilon + (\alpha + \xi)\Delta T$. Calibration constants from Ref. [23]: $P_e = 0.22$, $\alpha = 1.20\times 10^{-5}/^\circ\text{C}$, $\xi = 5.67\times 10^{-6}/^\circ\text{C}$.
- Smart strand architecture: King wire replaced by a seamless stainless steel tube (outer diameter 5.3 mm, inner diameter 1.9 mm) with 0.25 mm optical fiber secured via epoxy filling.
- Tensile testing: 1.4 m strand gauge length loaded to 210 kN at 20.0 kN/min load control. Bare fiber tension tested at 0.6 mm/min displacement control (6 specimens per material).
- Specimen groups: FBG-P-NP (normal, unjacketed) and FBG-P-PP (proposed, polyimide tube) with 7 specimens each.

## Results

| Configuration | Maximum Strain Measurement Range (Mean) |
|---|---|
| Bare optical fiber — acrylate recoating | 0.45 % |
| Bare optical fiber — polyimide recoating | 0.79 % |
| Strand-embedded FBG-P-NP (unjacketed) | 0.92 % (Below yield strain approx. 1 %) |
| Strand-embedded FBG-P-PP (polyimide tube) | 1.73 % (+88 % vs FBG-P-NP) |

- All FBG-P-PP specimens exceeded 1.0 % yield strain, reaching up to 2.36 %.
- Compared to the conventional embedded FBG measurement limit of approx. 0.65 % (6517.16 με), the proposed technique expanded the measurement range by 2.7-fold.

## Related Notes

- [[kim-2007-fbg-smart-tendon]] — Foundation technology measuring prestress tension via core-embedded FBG sensors (Ref. 21).
- [[iten-2012-strain-sensing-cables]] — Dual-layer cable packaging strategies for enhanced strain sensing range (Ref. 25).
- [[li-2024-uhpc-rc-beam-acoustic-emission]] — Comparative structural health monitoring combining acoustic emission and FBG strain sensing.
