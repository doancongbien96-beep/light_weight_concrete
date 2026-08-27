---
title: "Ductility and Cracking Behavior of UHPC-RC Composite Beam under Bending Test Based on Acoustic Emission Parameters (Li, Gou, Tan, Hedayat, Sun & Guo, 2024)"
type: source_note
source: "sources/Li 등 - 2024 - Ductility and cracking behavior of UHPC-RC composite beam under bending test based on acoustic emiss.pdf"
citation: "Li, S., Gou, W., Tan, Z., Hedayat, M., Sun, W., Guo, P. Ductility and cracking behavior of UHPC-RC composite beam under bending test based on acoustic emission parameters. Structures 70 (2024) 107624. doi: 10.1016/j.istruc.2024.107624"
date: 2026-08-22
tags: [uhpc-rc-composite-beam, acoustic-emission, ductility-index, crack-classification, b-value, ndt, zhengzhou-group]
---

# Evaluation of Ductility and Cracking Behavior of UHPC-RC Composite Beams Based on Acoustic Emission (AE) Parameters

## Summary

Research from the Zhengzhou University group. UHPC-RC composite beams with a 50 mm UHPC layer on the tension side and control RC beams were tested under four-point bending while damage was monitored via AE (acoustic emission); crack classification was performed using novel ductility indices based on cumulative ring-down counts and energy (ARD·AED) together with RA-AF and b-value combined parameters. The UHPC composite beam increased cracking load by 2×, yield load by 18.8 %, and ultimate load by 20.2 %, but its displacement ductility index decreased by 7 %; ARD·AED matched the displacement-based indices within 2 % error.

## Key Contributions

- Proposal of AE cumulative ring-down count·energy-based ductility indices ARD=AER_u/AER_y, AED=AEE_u/AEE_y. RC beam 1.11/1.10 vs UHPC-RC 1.04/1.02, consistent in trend with the displacement ductility indices (error within 2 %) — ductility can be evaluated during monitoring rather than after failure.
- Classification of tensile vs shear cracks using the RA(rise time/amplitude)-AF(counts/duration) combined parameter: RC beams were shear-crack dominated (O-A stage 59 %→B-C stage 96 %), while UHPC-RC expanded the tensile-crack share in the initial and failure stages (UHPC-layer effect).
- Quantification of the micro→macro crack transition via the b-value (log₁₀N=a-b(A_dB/20), windows of 250 amplitudes): the micro→macro transition point was RC 14 % vs UHPC-RC 22 % (of ultimate load) — the UHPC layer prolongs the microcracking stage.
- Sandblasting treatment (average depth 2.5 mm) of the UHPC-RC interface confirmed no debonding up to failure.

## Methods

- Specimens: two types of 2000×150×250 mm beams, 3 tension rebars ϕ14-HRB400E (ratio 1.43 %), stirrups ϕ8@80. UHPC layer 50 mm (bottom). C30 compressive strength 33.8 MPa, UHPC 147.2 MPa (28 days), UHPC direct tension 6.82 MPa.
- Four-point loading (1000 kN jack), midspan deflection via 100 mm displacement transducers, strain gauges on tension rebars.
- AE: 4 RS-2A sensors (200 mm either side of span center), DS5-16B waveform analyzer, pre-amplification 40 dB, vaseline coupling.

## Results

- Load stages: cracking RC 19.5 kN vs composite 39 kN(+100 %), yield 149/177 kN(+18.8 %), ultimate 158/190 kN(+20.2 %). Displacement ductility μ_Δ fell from RC 1.30 → composite 1.21(-7 %).
- Three-stage AE division: silence (0~14 %/0~22 %), sharp surge then moderation (14~96 %/22~92 %), abrupt change (96~100 %/92~100 %). Cumulative ring-down counts·energy correspond to the mechanical three stages (microcracking·macrocracking·failure).
- b-value: RC fluctuated widely at the failure stage (mixed micro+macro cracks, severe damage), whereas UHPC-RC remained stable (UHPC layer suppresses internal crack formation).

## Related Notes

- [[lai-2025-uhpfrc-nc-composite-beam-flexure]] — UHPFRC-NC composite beam analysis/design axis (shared tension-side UHPFRC placement)
- [[ge-2023-steel-precast-uhpc-composite-beams-flexural-behavior]] — UHPC precast composite beams
- [[du-2025-steel-uhdcc-composite-bridge-deck-bending]] — Ultra-high ductility composite members
- [[kim-2017-enhanced-strain-measurement-range]] — User-group SHM instrumentation axis (FBG vs AE)
- [[lee-kim-kim-2006-crack-pattern-recognition]] — Image-based crack detection as the counterpart of AE-based crack classification
- [[chun-2024-rc-beams-impact-resistance-hpfrcc]] — Impact response of HPFRCC-applied RC members
