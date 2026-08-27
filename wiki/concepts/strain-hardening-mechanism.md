---
title: "Strain-Hardening Mechanism"
type: concept
source: "[[li-wu-1992-psh-conditions]], [[li-2023-ecc-micromechanics-critical-review]]"
date: 2026-08-23
tags: [concept, strain-hardening, micromechanics, ecc, bridging-stress, constitutive-law]
---

# Strain-Hardening Mechanism

## Definition

Unlike the brittle or quasi-brittle behavior of ordinary concrete and ordinary fiber-
reinforced concrete (FRC), the behavior mechanism in which, under tensile loading,
stress keeps rising after first cracking instead of dropping, greatly extending
ductility and deformation capacity.

## Physical principle and conditions

For strain-hardening to develop, either the fiber bridging stress across the crack must
grow with crack opening (**slip-hardening**), or the maximum bridging stress
($\sigma_0$) must exceed the matrix first-cracking stress ($\sigma_{fc}$).

1. **Strength criterion**:
   $$\sigma_0 > \sigma_{fc}$$
   - Because the fiber bridging stress on the first-cracked section exceeds the matrix
     cracking strength, increasing load does not localize the existing crack into
     failure; new fine cracks initiate sequentially at other flaws.
2. **Energy criterion**:
   $$J'_b \ge J_{tip}$$
   - The complementary energy of fiber bridging ($J'_b = \sigma_0 \delta_0 -
     \int_0^{\delta_0} \sigma(\delta) d\delta$) must exceed the crack-tip fracture energy
     ($J_{tip} \approx K_m^2 / E_m$) for steady-state crack propagation to be maintained.

## Strain-hardening versus strain-softening

- **Strain-softening**: immediately after cracking, stress concentrates in one major
  crack and load capacity drops sharply to failure (ordinary FRC behavior).
- **Strain-har­dening (PSH)**: numerous fine cracks distribute across the whole member
  (multiple cracking), producing macroscopic yielding and tensile plastic deformation
  similar to metals (2–8 % strain).

## Related parameters

- $\sigma_0$: maximum fiber bridging stress (MPa)
- $\delta_0$: crack opening displacement at maximum bridging stress (µm)
- $\sigma_{fc}$ / $\sigma_c$: matrix cracking strength (MPa)
- $J'_b$: complementary energy (J/m²)
- $J_{tip}$: crack-tip fracture toughness energy (J/m²)

## Related Notes

- [[pseudo-strain-hardening-criteria]] — PSH design criteria and strength/energy margins.
- [[fiber-bridging-constitutive-law]] — derivation and modeling of the bridging law $\sigma(\delta)$.
- [[li-wu-1992-psh-conditions]] — first formal statement of the PSH theoretical conditions.
- [[li-2023-ecc-micromechanics-critical-review]] — comprehensive review of ECC
  micromechanics and strain-hardening design.
- [[kanda-2006-saturated-psh-design-criteria-ecc]] — practical saturated-PSH design
  criteria for rupture-dominated ECC.

- [[felekoglu-2014-htpp-ecc-flowability-mixing]] — HTPP-fiber ECC: viscous rheology and
  high-shear mixing achieving 3.9 % strain capacity.

- [[kong-2003-self-consolidating-pva-ecc-rheology]] — Victor Li group: MFS-HPMC
  compositional rheology control for self-consolidating PVA-ECC with 5 % tensile strain.

- [[kong-2003-electrosteric-dispersion-self-consolidating-ecc]] — Victor Li group:
  electrosteric dispersion stabilization for highly ductile self-consolidating PE-ECC,
  5.5 % strain capacity.

- [[kim-2009-modified-fiber-bridging-curve-ecc-tensile]] — Prof. Bang Yeon Lee
  (Chonnam National University): modified fiber-bridging curve combining plug pull-out
  critical spacing with image processing.

- [[lee-2010-micromechanics-fiber-bridging-distribution-model]] — Prof. Lee: generalized
  fiber-bridging model coupling measured fiber orientation distribution with spatial density.

- [[lee-2010-ecc-tensile-stress-strain-prediction-model]] — Prof. Lee: full-range ECC
  tensile stress-strain prediction from image-analyzed fiber distribution and pullout work.

- [[lee-2010-fluorescence-discriminating-fibers-hybrid-ecc]] — Prof. Lee: automatic
  identification of dissimilar fibers via fluorescence spectroscopy and multispectral LDA.

- [[li-1991-micromechanical-model-tension-softening-bridging]] — Victor Li: JMPS classic
  micromechanics model of tension softening/bridging toughening based on snubbing and
  slip-hardening interfaces.

- [[li-1995-matrix-design-for-pseudo-strain-hardening]] — Victor Li: upper bound on
  matrix fracture toughness for PSH composites (Jtip <= 0.010 kJ/m^2) and aggregate-volume
  design guidance.

- [[li-1994-shear-behavior-engineered-cementitious-composites]] — Victor Li: pure shear
  strain-hardening of ECC (shear ductility 4.0 %).

- [[li-1996-fiber-diameter-variation-composite-properties]] — Victor Li: micromechanics
  of bridging stress and fracture energy under fiber diameter variation.

- [[li-2002-interface-tailoring-pva-ecc-oiling-agent]] — Victor Li: interface tailoring
  of PVA-ECC by oiling surface treatment (tensile ductility 4.7 %), landmark paper.

- [[li-2012-tailoring-ecc-special-attributes-review]] — Victor Li: review framework for
  redesigning ECC toward special functionality.

- [[lin-1997-crack-bridging-slip-hardening-interfaces]] — Lin & Li: full-cycle fiber
  bridging model with slip-hardening interfaces and closed-form solutions, classic paper.

- [[li-1998-passive-smart-self-healing-ecc]] — Victor Li & Yoon-Mook Lim: passive smart
  self-healing ECC with embedded hollow fibers (PSS-ECC).

- [[lu-2018-recycled-pet-fiber-shcc-tensile-impact]] — Lu & Yu & Leung: recycled PET
  fiber SHCC under static tension and Charpy dynamic impact.

- [[maalej-1994-flexural-tensile-strength-ratio-in-ecc]] — Maalej & Victor Li: 5.0x
  amplification of the flexural/tensile strength ratio in ECC and the rising neutral axis
  mechanism, classic paper.

- [[maalej-2005-hybrid-fiber-ecc-dynamic-tensile-projectile-impact]] — Maalej & Quek:
  dynamic tension and high-velocity projectile resistance of hybrid-fiber ECC.

- [[ma-2019-emulsified-asphalt-high-damping-ecc]] — Ma & Qian & Victor Li:
  micromechanical design of high-damping EA-ECC with emulsified asphalt.

- [[marshall-1988-j-integral-steady-state-matrix-cracking]] — Marshall & Cox: immortal
  J-integral steady-state matrix cracking analysis governed by bridging complementary energy.

- [[mai-1979-asbestos-cement-strength-fracture-toughness]] — Yiu-Wing Mai: fracture
  toughness of short-fiber-reinforced cement composites and frictional energy dissipation
  in fiber pullout.

- [[felekoglu-2015-htpp-ecc-fiber-distribution-image-analysis]] — Felekoglu: BSE-SEM
  image analysis of fiber dispersion coefficient and control of multiple fine cracking in
  HTPP-ECC.

- [[lin-2023-hybrid-pe-pp-engineered-geopolymer-composite]] — Lin & Guo: tensile strain-
  hardening and crack-bridging constitutive model of PE-PP hybrid fiber EGC.
