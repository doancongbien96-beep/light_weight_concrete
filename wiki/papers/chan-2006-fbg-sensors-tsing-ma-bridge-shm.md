---
title: "Fiber Bragg grating sensors for structural health monitoring of Tsing Ma bridge: Background and experimental observation (Chan et al., 2006)"
type: source_note
source: "sources/'chan-2006-fiber-bragg-grating-sensors-for.pdf'"
citation: "Chan, T.H.T., Yu, L., Tam, H.Y., Ni, Y.Q., Liu, S.Y., Chung, W.H., Cheng, L.K. Fiber Bragg grating sensors for structural health monitoring of Tsing Ma bridge: Background and experimental observation. Engineering Structures 28 (2006) 648-659. DOI 10.1016/j.engstruct.2005.09.018. Hong Kong Polytechnic Univ. + TNO TPD."
date: 2026-08-23
tags: [fbg, structural-health-monitoring, tsing-ma-bridge, suspension-bridge, dynamic-strain, wasrms]
---

# FBG Sensor Structural Health Monitoring of the Tsing Ma Bridge — Background and Field Experimental Observations

## Summary

Joint field demonstration (May 2003) by the Hong Kong Polytechnic University civil and photonics teams together with TNO (TPD). Forty FBG sensors in three arrays were installed on the hanger cables, rocker bearings, and truss girders of the Tsing Ma Bridge — the world's longest road-and-rail suspension bridge, main span 1377 m — dynamic strains under rail and road traffic were measured, and results were compared against the resistance strain gauges of WASHMS, the bridge's operating permanent monitoring system (about 800 sensors, 110 of them strain gauges). Train passages were clearly detected with the DEMINSYS high-speed interrogator (CCD-based, DC to 20 kHz simultaneously on all channels, detection limit below 1 pm), and the FBG results agreed closely with WASHMS, demonstrating FBG sensing as an alternative for dynamic strain monitoring of large bridges.

## Key Contributions

- Formalizing FBG principles for bridge application: Bragg wavelength λB = 2nΛ; strain sensitivity ~0.64 pm/με in the 800 nm band and ~1.15 pm/με at 1.55 μm; temperature sensitivity ~6.8 pm/°C and ~13 pm/°C. Equation (6) presents stress-free-FBG temperature compensation (separating thermal and mechanical effects).
- Comparison of multiplexing techniques: WDM (~40 gratings per fiber, accuracy 1 pm → 0.1 °C/1 με), TDM (10 pm → 1 °C/10 με, low SNR), FDM and SDM — wavelength encoding being insensitive to light-source intensity fluctuation and transmission-path loss stated explicitly as FBG's core advantage.
- Three-site installation package on a full-scale suspension bridge: Corning SMF28 fiber stripped of its acrylate coating and annealed, epoxy-bonded onto nitinol strips (6 × 110 mm; superelastic, corrosion-resistant, 8 % elongation without deformation), housed in IP65 ABS enclosures (120 × 80 × 60 mm) — functionally and physically compatible with the WASHMS resistance strain gauge housings.
- High-speed interrogation demonstrated with DEMINSYS: developed by TNO; 1530-1565 nm, channel spacing ~4 nm, readout up to ~20 kHz (sub-pm averaging per sample). Can capture frequency-event information beyond the ~20 Hz detection limit of WASHMS strain gauges.
- Field observation results: on the hanger cables, train passages (t = 307 s and 377 s, two trains in opposite directions) and a heavy vehicle (t = 195 s) were identified, with estimation of travel direction also possible. Rocker bearings and truss girders (21-sensor array, Chainage 23488) likewise yielded signals very similar to the resistance gauges despite installation-position differences.
- Signal quality quantified: FBG noise consists mainly of a 13 Hz component (bridge vibration picked up by DEMINSYS); a 10-point moving average narrows the band to ~2 kHz, and a 5000-point filter achieves sub-pm/με resolution.
- Synthesis of FBG advantages: remote monitoring, ease of installation, immunity to corrosion, reduced maintenance cost — a case extending from the first bridge field application of FBGs (embedded in Calgary concrete girders, 1995, Measures et al.) to full-scale large suspension bridge scale.

## Methods

- Target structure: Tsing Ma Bridge — upper deck carrying a dual three-lane high-speed road plus two rail tracks on the lower deck; longitudinal trusses at 26 m spacing with an orthotropic steel deck; Vierendeel cross frames at 4.5 m spacing (every fourth frame supporting suspenders). Opened on 1997-05-22.
- Installation: six hanger cables, the rocker bearings, and the support structures of the lower-deck Chainage 23488 section — 40 sensors in total (3 arrays, 21 on the truss girders). Dual bonding after local removal of anti-corrosion paint: cyanoacrylate (outside the housing footprint, instant fixing) + two-part waterproof epoxy (sensor side inside, rigid bond).
- Measurement: continuous 24 h operation (temperature + strain); ~20 h nighttime monitoring runs (sampling ~500 Hz); readout sampling at 0.106 ms for hangers, 2.1 ms for rockers, and 0.0528 ms for the truss. Stress-free FBGs co-installed for temperature compensation.
- Reference baseline: resistance strain gauges of WASHMS at adjacent locations logged simultaneously.

## Results

- Three train passages (320, 420, 560 s): FBG overshoot responses correspond exactly with the WASHMS gauge readings (Figure 11).
- Rocker bearing: despite strong sensor-position dependence arising from complex load paths, the 1 h histories of the two sensor types are highly similar, with clear train-passage detection.
- Truss girder: FBG (top) vs gauge (bottom) waveforms agree closely; sub-pm/με resolution confirmed after filtering.
- Conclusion: clear and accurate detection of the dynamic strain response, with advantages over resistance gauges in remote operation, corrosion immunity, and maintenance — detailed measurements and analysis promised in a follow-up paper ([31] Chan et al., submitted 2006).

## Related Notes

- [[kim-2007-fbg-smart-tendon]] — the user group's origin paper on FBG smart strands: develops the same bridge-cable sensing context into strand-embedded form
- [[kim-2010-fbg-strand-tension-monitoring]] — Yeosu field application of FBG smart strands (user group)
- [[kim-2017-enhanced-strain-measurement-range]] — FBG measurement-range extension lineage
- [[watkins-2003-smart-bridges]] — smart-bridge overview (three years before this paper)
- [[udd-1996-fiber-optic-smart-structures]] — fiber-optic smart structures textbook (the Udd-edited series containing Kersey's chapter [35])
- [[iten-2012-strain-sensing-cables]] · [[iten-2011-distributed-fiber-optic-sensing-dissertation]] — distributed fiber-optic strain sensing lineage
