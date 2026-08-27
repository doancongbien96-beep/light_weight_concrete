---
title: "Investigation of the Fiber Bridging Stress-Crack Opening Relationship of Fiber Reinforced Cementitious Composites (Yang & Fischer, 2005)"
type: source_note
source: "sources/yang-fischer-2005-bridging-stress-crack.pdf"
citation: "Yang, J., Fischer, G. Investigation of the fiber bridging stress-crack opening relationship of fiber reinforced cementitious composites. Proc. Int'l RILEM Workshop on HPFRCC in Structural Applications, Honolulu, Hawai'i (2005.5.23~26). University of Hawaii."
date: 2026-08-22
tags: [fiber-bridging, stress-crack-opening, simulation, multiple-cracking, strain-hardening, hpfrcc, rilem-workshop]
---

# Clarifying the fiber bridging stress-crack opening relationship of FRC

## Summary

A paper presented by Yang and Fischer of the University of Hawaii at the RILEM HPFRCC workshop (2005). It proposes a method for simulating the displacement-controlled uniaxial tensile behavior of ECC using experimentally obtained fiber bridging stress-crack opening curves σ_B(δ) as input. The approach reproduces multiple cracking during the strain-hardening stage and can predict multiple cracking characteristics such as crack width and spacing.

## Key Contributions

1. **σ_B(δ)-based multiple cracking simulation frame**: tri-linear approximations of the experimental bridging curve define upper and lower bounds, with four parameters (first-cracking strength σfc, peak bridging stress σpeak, peak opening displacement δ1, and bridging stiffness Kf) assumed to vary randomly within experimental ranges.
2. **Natural incorporation of material variables**: variability of matrix flaw size, fiber tensile strength, interface properties, and fiber orientation is embedded in parameter range setting — capturing variability from experimental data alone without a separate probabilistic model.
3. **Extensibility to structural members**: the simulation concept is suggested to be integrable into ECC structural member design procedures.

## Methods

- Upper and lower bounds of experimentally obtained σ_B(δ) curves approximated with a tri-linear model (Fig. 4a).
- Zhang & Stang's [10] flexural prediction model for steel FRC extended to ECC strain hardening.
- Random sampling of the four parameters → displacement-controlled uniaxial tension simulation → derivation of multiple cracking patterns.

## Results

- The simulation reproduced multiple cracking and strain-hardening behavior and yielded crack widths and spacings.
- Initial results promising — experimental validation to follow.

## Related Notes

- [[fiber-bridging-constitutive-law]] — σ_B(δ) theoretical framework
- [[yang-2008-fiber-bridging-constitutive-law-of-ecc]] — follow-up numerical model
- [[pseudo-strain-hardening-criteria]] — PSH conditions
- [[wu-1992-snubbing-bundling-crack-spacing]] — multiple crack spacing theory
- [[wang-2004-tailoring-preexisting-flaws-ecc]] — flaw tailoring design
