---
title: "Multiple Cracking Behavior"
type: concept
source: "[[aveston-1973-theory-of-multiple-fracture]], [[wu-1992-snubbing-bundling-crack-spacing]], [[li-wu-1992-psh-conditions]]"
date: 2026-08-23
tags: [concept, multiple-cracking, crack-spacing, crack-width, ack-theory, ecc, shcc]
---

# Multiple Cracking Behavior

## Definition

The phenomenon in fiber-reinforced cementitious composites (ECC/SHCC) under tensile
loading in which fine cracks of tight, uniform spacing form continuously across the
member during the strain-hardening stage instead of localizing into a single crack.

## Mechanism and theory (ACK model and extensions)

1. **Aveston-Kelly-Blackwell (ACK) theory**:
   - Built on the multiple-fracture theory of continuous-fiber composites (1971, 1973).
   - After first cracking, load transfers from matrix to fiber; through the interfacial
     shear stress ($\tau_0$) the matrix tensile stress recovers with distance from the
     crack face (transfer length $x_t$).
   - A new crack forms where the recovered stress exceeds the strength of a nearby flaw.

2. **Crack spacing**:
   - Minimum crack spacing $x_{min} = x_t = \frac{V_m \sigma_{mu} d_f}{4 V_f \tau_0}$
   - Final saturated spacing $s$: $x_t \le s \le 2x_t$
   - In composites with random discontinuous fibers, the random orientation angles and
     flaw distributions make the saturation spacing probabilistically distributed.

3. **Crack width control**:
   - While multiple cracking proceeds, each individual crack opening is tightly capped
     at or below the steady-state crack opening displacement
     ($\delta_{ss} \le 100\ \mu\text{m}$).
   - Total imposed deformation is accommodated by an increase in the number (density)
     of cracks rather than by excessive widening of a single crack:
     $$\epsilon \approx N_{cracks} \times \frac{\delta}{L}$$

## Physical character and saturation

- **Saturated multiple cracking**: cracks have initiated at every flaw meeting the
  cracking-strength condition and no new cracks appear. Beyond this state the composite
  enters single-crack localization and failure at peak tensile stress.
- **Unsaturated multiple cracking**: insufficient fiber bridging stress leads to only a
  few cracks followed by premature failure.

## Related parameters

- $V_f, V_m$: fiber and matrix volume fractions
- $d_f, L_f$: fiber diameter and length (µm, mm)
- $\tau_0$: interfacial frictional shear strength (MPa)
- $s$: mean crack spacing (mm)
- $w$: mean crack width (µm)

## Related Notes

- [[aveston-1973-theory-of-multiple-fracture]] — classical origin of multiple-fracture
  theory (Aveston & Kelly 1973).
- [[wu-1992-snubbing-bundling-crack-spacing]] — snubbing and crack spacing model for
  discontinuous short-fiber composites.
- [[strain-hardening-mechanism]] — the strain-hardening mechanics that drive multiple cracking.
- [[pseudo-strain-hardening-criteria]] — PSH design conditions for achieving saturation.
- [[tosun-2014-flaw-size-fiber-distribution-pva-ecc]] — influence of flaw size
  distribution and fiber dispersion on the degree of multiple-cracking saturation.

- [[aveston-1973-theory-of-multiple-fracture-of]] — ACK multiple-fracture theory and
  crack-spacing analysis origin.

- [[huang-1995-steel-fiber-concrete-large-aggregate]] — Zhaoguo Pan origin paper
  (Dalian University of Technology): gradation optimization and flexural toughness of
  SFRC with 40 mm coarse aggregate.

- [[huang-2011-3d-numerical-simulation-frcc-cracking]] — South China University of
  Technology: 3D meso-scale Weibull softening-zone fracture model and numerical crack
  simulation for FRCC.

- [[huang-2021-seawater-sea-sand-ecc-crack-modeling]] — PolyU/HKUST/Michigan: Weibull
  crack model for 135 MPa ultra-high-strength, 7.2 % ultra-high-ductility seawater
  sea-sand SS-ECC.
