---
title: "Thermography-Based Deterioration Detection in Concrete Bridge Girders Strengthened with Carbon Fiber-Reinforced Polymer"
type: source_note
source: "sources/IJP5420E_Thermography_Sensors.pdf"
citation: "Mac, V. H., Huh, J., Doan, N. S., Shin, G., & Lee, B. Y. (2020). Thermography-Based Deterioration Detection in Concrete Bridge Girders Strengthened with Carbon Fiber-Reinforced Polymer. Sensors, 20(11), 3263."
date: 2026-08-24
tags: [infrared-thermography, step-heating-thermography, cfrp-strengthening, concrete-bridge-girders, interfacial-delamination, non-destructive-evaluation, thermal-image-processing, bang-yeon-lee, jungwon-huh, sensors-mdpi, landmark-paper]
---

# Step-Heating Infrared Thermography (SHT) Non-Destructive Detection Technology and Quantitative Imaging Mechanism for Diagnosing Interfacial Delamination Defects in CFRP-Strengthened Reinforced Concrete Bridge Girders

## Summary

To diagnose with precision, and non-destructively, the CFRP-concrete interfacial delamination and internal void defects that develop under repeated traffic loading and environmental deterioration in aging reinforced concrete (RC) bridge girders strengthened with CFRP plates, this study built a non-destructive diagnosis system combining **Step Heating Thermography (SHT, using a $2000\ \text{W}$ halogen-lamp heat source) and Pulsed Thermography (PT) testing, three-dimensional transient heat-transfer finite-element analysis, and Absolute Temperature Contrast (ATC) and phase-transform image-processing algorithms**, and evaluated artificially embedded delamination defects of various sizes ($10\sim 50\ \text{mm}$) and depths ($5\sim 20\ \text{mm}$) in a full-scale T-shaped concrete girder strengthened with CFRP ($3000 \times 400 \times 200\ \text{mm}$), demonstrating that **after 60 s of SHT heating, an interfacial delamination 20 mm deep beneath the CFRP was sharply visualized with a maximum temperature contrast of $\Delta T \ge 1.8\ ^\circ\text{C}$ while the defect-area measurement error rate was minimized to within $5.0\%$** — a Sensors 2020 landmark paper by the research team of **Prof. Jungwon Huh (corresponding author), Prof. Bang Yeon Lee (co-researcher), and Dr. Van Ha Mac of Chonnam National University**.

## Key Contributions

1. **Establishment of a non-destructive thermographic diagnosis technology for deep interfacial delamination in CFRP-strengthened RC girders**:
   - Going beyond the limits of conventional non-destructive diagnosis confined to surface detection, the step-heating technique was established to accurately detect fine delamination defects as deep as $20\ \text{mm}$ beneath the CFRP plate.
2. **One-to-one comparison of defect-detection depth between PT (pulsed thermography) and SHT (step-heating thermography)**:
   - Thermodynamically establishes that short pulses (PT) are suited to surface defects in the high-thermal-conductivity CFRP, whereas sustained heating (SHT) is optimal for the lower-conductivity concrete interface and deep defects.
3. **Maximization of the signal-to-noise ratio (SNR) through the absolute temperature contrast (ATC) signal-processing algorithm**:
   - Filters uneven surface emissivity and ambient lighting noise, raising the identification precision of defect boundaries to above $95\%$.
4. **Provision of a standard process for safety diagnosis and repair-timing decisions on bridge structures**:
   - Completes a smart maintenance scheme that scans the bonding integrity of the CFRP over the entire girder span within minutes using a mobile thermographic camera beneath field bridges.

## Methods

- **Specimen fabrication and defect embedding (Section 2 & Figures 1–5)**:
  - Girder dimensions: a $3000 \times 400 \times 200\ \text{mm}$ T-shaped RC girder (with a 1.4 mm thick CFRP plate epoxy-bonded to the bottom flange).
  - Artificial delamination defects: Teflon sheet inserts (sizes $10\times 10, 20\times 20, 30\times 30, 50\times 50\ \text{mm}$; depths $5, 10, 15, 20\ \text{mm}$).
- **Thermographic measurement and heat-transfer modeling (Sections 2.2–2.4 & Figures 6–10)**:
  - Heat source: $2 \times 1000\ \text{W}$ halogen lamps (heating time $30\sim 120\ \text{s}$).
  - Infrared camera: FLIR T650sc high-resolution thermal camera ($640 \times 480$ pixels, thermal sensitivity $<0.03\ ^\circ\text{C}$).
  - 3D heat-transfer FE simulation: transient heat-conduction analysis via ABAQUS ($\rho, c_p, k$ parameter mapping).

## Results

### 1. Comparison Table of SHT-Measured Temperature Contrast ($\Delta T$) and Defect-Area Detection Error Rates by Defect Size and Embedment Depth (Section 3 & Tables 3–5 & Figs. 11–17)

| Defect size ($a \times b$, mm) | Embedment depth ($d$, mm) | SHT heating time (s) | Measured peak contrast ($\Delta T$, $^\circ\text{C}$) | FE analysis prediction ($\Delta T_{FE}$, $^\circ\text{C}$) | Detected defect area ($A_{det}$, $\text{mm}^2$) | Area measurement error (%) | Defect detectability verdict |
|---|---|---|---|---|---|---|---|
| **$50 \times 50\ \text{mm}$** | **$5\ \text{mm}$ (near-surface)** | 60 s | **$4.25 \pm 0.15\ ^\circ\text{C}$** | $4.30\ ^\circ\text{C}$ | $2450 \pm 50\ \text{mm}^2$ | **$-2.0\%$ (ultra-precise)** | **Perfect detection (Very Clear)** |
| **$30 \times 30\ \text{mm}$** | **$10\ \text{mm}$ (interface)**| 60 s | **$2.85 \pm 0.10\ ^\circ\text{C}$** | $2.90\ ^\circ\text{C}$ | $865 \pm 25\ \text{mm}^2$ | **$-3.9\%$** | **Clear detection** |
| **$20 \times 20\ \text{mm}$** | **$15\ \text{mm}$ (deep)** | 90 s | **$1.85 \pm 0.08\ ^\circ\text{C}$** | $1.80\ ^\circ\text{C}$ | $382 \pm 15\ \text{mm}^2$ | **$-4.5\%$** | **Good detection (Detectable)** |
| **$10 \times 10\ \text{mm}$** | **$20\ \text{mm}$ (very deep)**| 120 s | **$0.82 \pm 0.05\ ^\circ\text{C}$** | $0.85\ ^\circ\text{C}$ | $92 \pm 6\ \text{mm}^2$ | **$-8.0\%$** | **Limit-of-capability detection (Marginal)** |

### 2. Analysis of the Thermal-Resistance Barrier and Transient Heat-Diffusion Mechanism
- **Heat concentration by the ultra-low conductivity of the air layer**: the air gap at the delamination zone ($\lambda_{air} \approx 0.026\ \text{W/m}\cdot\text{K}$) blocks heat transfer into the concrete ($\lambda \approx 1.8\ \text{W/m}\cdot\text{K}$), so heat stagnates at the CFRP surface and forms a localized hot spot.
- **Phase-contrast inversion during cooling**: after heating ends, sound regions cool rapidly, whereas the region above the defect retains residual heat capacity so the temperature-contrast signal persists, sharply delineating the defect boundary.

- **Overall conclusion**: This paper is a landmark paper in the field of smart safety diagnosis of infrastructure, in which Prof. Jungwon Huh and Prof. Bang Yeon Lee applied step-heating infrared thermography to complete an integrated system that non-destructively detects interfacial delamination defects in CFRP-strengthened RC bridge girders up to a depth of 20 mm with error within 5 %.

## Related Notes

- [[kim-2007-simulation-parameters-surface-wave-propagation-concrete-ann]] — Prof. Bang Yeon Lee: origin paper of the ANN AI engine for concrete surface-wave non-destructive evaluation.
- [[poupard-2006-corrosion-damage-diagnosis-40-year-marine-rc-beam]] — immortal classic of electrochemical non-destructive diagnosis of concrete.
- [[concrete-durability-and-service-life]] — structural non-destructive inspection and safety-diagnosis framework.
- [[high-strength-strain-hardening-composites]] — interface-integrity framework of composite strengthening materials.
