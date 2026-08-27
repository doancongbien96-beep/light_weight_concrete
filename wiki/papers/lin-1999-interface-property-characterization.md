---
title: "On Interface Property Characterization and Performance of Fiber-Reinforced Cementitious Composites (Lin, Kanda & Li, 1999)"
type: source_note
source: "sources/On interface property characterization and per.pdf"
citation: "Lin, Z., Kanda, T., Li, V.C. On interface property characterization and performance of fiber-reinforced cementitious composites. Concrete Science and Engineering 1 (1999) 173-184. (RILEM)"
date: 2026-08-22
tags: [interface-characterization, single-fiber-pullout, chemical-bond, slip-hardening, snubbing, fiber-rupture, bridging-law, micromechanics, classic]
---

# Interface Property Characterization and Performance of Fiber-Reinforced Cementitious Composites

## Summary

A theory paper (Michigan ACE-MRL + Kajima Technical Research Institute) that quantitatively extracts the interface properties from single-fiber pullout tests — chemical bond energy Gd, frictional bond τ0, and the slip-hardening coefficient β — and, additionally integrating the snubbing effect and the fiber-strength reduction under inclined pullout (f′), derives a closed-form composite bridging stress–crack opening curve σ_B(δ). It systematized the influence of PVA fibers' strong chemical bonding on the critical length and the multiple-cracking condition (J′b>Jtip), thereby becoming the theoretical foundation for the subsequent interface-tailored design of ECC (development of REC15).

## Key Contributions

- Three-parameter pullout model: debonding is formalized as a mode-II tunneling crack (interfacial fracture toughness Gd), small-scale slip as constant friction τ0, and large-scale pullout as slip hardening β. From the maximum debond load equation P_a=πd_fτ₀L_e+½πd_f²√(G_d E_f), Gd and τ0 are calibrated directly.
- Duality formalization of inclined effects: the increase of the pullout load is governed by the snubbing coefficient f (P(φ)=P(0)e^{fφ}), while the reduction of the in-situ fiber strength is governed by f′ (σ_fu(φ)=σ_fu e^{-f'φ}) — the two exponents combine into a critical embedded length of the form L_c=2L_eg√(1-f²)-γ. For polymer fibers the ranges β=0.005~0.05, f=0.5~0.9, and PVA f′≈0.3 are reported.
- Quantification of the chemical-bond paradox: chemical bond↑ → early-age bridging stress and tensile strength↑, but complementary energy↓ and fracture energy↓ (accelerated fiber rupture). The strength–ductility trade-off is explained within a single model — the theoretical basis for PVA coating design.
- PVA-RMU vs RK case study: RMU (∅44 µm diameter, 6 mm length, Vf 1.5 %) has high strength, but its Gd=0.8 J/m² falls short of Jtip (~2 J/m²) → multiple cracking impossible. RK (∅40 µm, 12 mm, 2 %) satisfies the condition with Gd=3.4 J/m² → ductility secured. This proves that the choice of diameter and length changes the required interface property targets.

## Methods

- Single-fiber pullout: 1 N mini load cell, microfiber alignment technique, validated on PVA (∅14.8 µm). Three-stage interpretation: elastic elongation before debonding → debonding (the load drop point = evidence of chemical adhesion) → frictional pullout (a concave-upward rise = slip-hardening).
- Composite bridging law: closed form derived (Appendix B) by integrating over the orientation-angle and depth PDFs (p(φ)=sinφ, p(z)=2/L_f) together with treatment of the fiber-rupture domain (excluded below the critical embedded length curve). The Marshall–Cox J-integral reconfirms the steady-state cracking condition G_c≥J_tip.
- PVA composite: matrix of cement 1.0/sand 0.4/W 0.45, cured for 7 days in water + 1 day in air, dog-bone direct tension.

## Results

- Model fitting: the PVA-RMU pullout curves are reproduced with Gd=6.0 J/m², τ0=3.0 MPa, and β=0.05. Predictions of the maximum debond load across embedded lengths agree with the experiments.
- Non-regular sensitivity: an increase in chemical bond sharply raises the tensile strength of short fibers (governed by the initial debond stress), while the fracture energy decreases. An optimal fiber length exists (peak of the fracture energy).
- Complementary-energy map: the scatter of G_c is presented as a function of fiber length × relative chemical bond (γ/L_eg) — a practical tool for ECC mix design.

## Related Notes

- [[fiber-bridging-constitutive-law]] — the σ_B(δ) constitutive law that this paper derived in closed form
- [[kanda-1998-pva-interface-apparent-strength]] — preceding paper by the same group on interface properties and apparent strength
- [[li-wu-1992-psh-conditions]] — original source of the steady-state cracking condition (G_c≥J_tip)
- [[li-2003-ecc-review-jact]] — review applying this model to REC15 interface tailoring
- [[morton-1976-effect-metal-wires-fracture-brittle-matrix-composites]] — experimental original source of the snubbing effect
- [[nematollahi-2017-one-part-shgc-micromechanics]] — follow-up geopolymer application within the same framework (including the Km–τ0 correlation)
- [[ranade-2013-hshdc-micromechanics]] — extension of the three-parameter model to high-strength matrices with an added inclined-hardening mechanism
