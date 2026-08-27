---
title: "Thermography-Based Deterioration Detection in Concrete Bridge Girders Strengthened with CFRP (Mac, Huh, Doan, Shin & Lee, 2020)"
type: source_note
source: "sources/Mac-2020-Thermography-Based Deterioration Dete.pdf"
citation: "Mac, V. H., Huh, J., Doan, N. S., Shin, G., Lee, B. Y. Thermography-based deterioration detection in concrete bridge girders strengthened with carbon fiber-reinforced polymer. Sensors 20(11) (2020) 3263. doi: 10.3390/s20113263"
date: 2026-08-22
tags: [thermography, step-heating-thermography, cfrp-strengthening, delamination, ndt, thermal-diffusivity, snr, chonnam-group]
---

# Step-Heating Thermographic Detection and Quantification of Internal Delamination in CFRP-Strengthened Concrete Girders

## Summary

A study by the Chonnam National University group (corresponding author Huh; Prof. Bang Yeon Lee co-author and advisor). Deep concrete delamination — more neglected than CFRP-layer damage — in concrete girders strengthened with CFRP sheets was quantitatively detected using step-heating thermography (SHT). Using specimens embedding eight artificial delaminations at depths of 1–8 cm, the study established the detection limits, the effect of heating time, and the effect of CFRP bonding, and proposed the previously nonexistent empirical thermal diffusivity αe = 1.0153 cm²/min for CSC (CFRP-strengthened concrete), achieving a delamination depth-prediction RMSE of 0.4–0.7 cm.

## Key Contributions

- Quantified detection limit: within heating durations of 40 min or less, SHT can detect delaminations to a depth of 7 cm (the deepest case, 8 cm, showed a maximum ΔT of 0.033 °C — NETD-level — but went undetected with a negative SNR of −0.653 dB). Minimum required heating times per depth are specified — back-face delaminations (depth ≤4 cm) were all detected from 10 min onward, 5 cm from 15 min, 6 cm from 20 min, and 7 cm from 25 min.
- Established that CFRP sheets actually raise delamination contrast (absolute contrast): under identical conditions the maximum ΔT of the BD3 delamination was 0.51 °C in CWC (unstrengthened) vs 0.73 °C in CSC (CFRP-strengthened) (SNR 6.02 vs 8.66 dB). The cause is increased heat absorption owing to the high emissivity of the CFRP surface (0.97 vs concrete 0.95) — demonstrating empirically that CFRP does not interfere with thermographic detection.
- Proposal of an empirical thermal diffusivity for CSC girders: from the relation between observation time OBT and depth, OBT = 0.9849×Z² (R² = 0.981), giving αe = 1/0.9849 = 1.0153 cm²/min — a value between Maldague's literature values (CFRP about 3.7, concrete about 0.53 cm²/min), explained by the effective-medium concept. Intended for field depth prediction.
- Post-processing algorithm comparison (TSR + PPT + ABC): for short heating (5 min), PPT phase data prevails (BD2 SNR 4.98→9.74 dB); for long heating (10–15 min), TSR prevails. Combining the two methods' results was never worse than ABC alone in any case, so a multi-algorithm combination is recommended.

## Methods

- Specimens: eight 10×10×1 cm polystyrene artificial delaminations (thermal conductivity k=0.027 W/m°C, similar to air's 0.024) embedded in plate-type concrete specimens with a design compressive strength of 30 MPa. Positioned at depths of 1–4 cm from the front face (the FD series at 5–8 cm) and 5–8 cm from the back face (the BD series at 1–4 cm). Each column held one pair of identical-spec delaminations in the CSC region and the CWC region for direct comparison of the CFRP effect.
- CFRP sheet: one ply of unidirectional sheet (thickness 0.167 mm), applied in a six-step sequence of epoxy primer — putty — sheet bonding — finish coating.
- Heating and measurement: four halogen lamps (500 W × 4, total 2000 W) placed 1.2 m from the test surface. Back-face heating at 3/5/10/15/20 min and front-face heating in seven segments over 5–40 min, among 36 cases total. Images recorded with a long-wave infrared camera FLIR SC660 (thermal sensitivity 0.03 °C) at 0.5 Hz (every 2 s), covering the entire heating and cooling periods.
- Analysis metrics: absolute contrast Cab = T_de − T_nde (defect ROI vs surrounding ROI), SNR = 20 log10(|S−N|/σ_noise). Detection criterion: ΔT ≥ NETD 0.03 °C AND SNR > 0 dB. Depth predicted via Z² = αe×OBT (OBT measured from cooling onset to the ΔT peak).

## Results

- Contrast–depth–heating-time relationship: at equal heating time, shallower defects show higher contrast (with 10 min of heating, BD2-CF 0.86 °C vs BD3-CF 0.52 °C), and maximum ΔT increases with longer heating (FD4-CF: 0.02/0.05/0.07 °C at 10/20/30 min).
- Depth prediction accuracy: across all-case average predictions, the deviation of the ideal-line contrast slope was about 2 %. RMSE was 0.650/0.545 cm for 15/20 min heating, 0.69/0.68/0.42 cm for 3/5/10 min (back-face defects only), and 0.63/0.64/0.50 cm for 25/30/40 min (front-face defects only) — accuracy improves with longer heating.
- Post-processing SNR comparison (back-face heating): for BD2-CF at 5 min, ABC gave 4.98 → PPT phase 9.74 dB (+95 %), with TSR first derivative at 9.49 dB. For BD3-CF at 5 min, TSR on log data raised 1.90→4.61 dB (+143 %). Conversely, applying PPT at 10 min dropped BD3-CF to 3.46 dB, below ABC (5.08 dB) — algorithm effects are defect- and condition-dependent.
- Author contributions: analysis by V.H.M.; Huh and Lee (the user's professor) participated in validation and supervision. Supported by the Ministry of Oceans and Fisheries port technology development program (20180323) and the Ministry of Land, Infrastructure and Transport research program (19RDRP-B076564-06).

## Related Notes

- [[lee-kim-kim-2006-crack-pattern-recognition]] — user group's image-based crack detection axis (visible-light imaging vs infrared imaging)
- [[lee-2005-enhanced-binarization-crack]] — binarization preprocessing on the NDT/image diagnostics axis
- [[kim-2007-surface-wave-ai-engine]] — surface-wave NDT (elastic waves vs thermal waves)
- [[kim-2007-fbg-smart-tendon]] — user group's FBG optical-fiber instrumentation axis
- [[li-2024-uhpc-rc-beam-acoustic-emission]] — AE-based damage monitoring (counterpart pairing active-heating thermography with passive sensors)
