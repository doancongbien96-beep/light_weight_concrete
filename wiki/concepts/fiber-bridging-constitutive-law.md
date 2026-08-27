---
title: "Fiber-Bridging Constitutive Law"
type: concept
source: "[[li-2023-ecc-micromechanics-critical-review]]"
date: 2026-08-22
tags: [concept, fiber-bridging, micromechanics, crack-bridging]
---

# Fiber-Bridging Constitutive Law

## Definition

The relationship σ_B(δ) between the stress carried per unit crack area by randomly
oriented discontinuous fibers spanning a crack and the crack opening displacement.
It is the key meso-scale constitutive law of ECC: it governs the crack propagation
mode and the pseudo strain-hardening potential, and it largely determines tensile
strength and crack width.

## Composition

σ_B(δ) is obtained (Eq. 8) by weighting the single-fiber pullout mechanics
P(δ, L_e, φ) over all fibers crossing the crack, using probability density
functions of fiber position (z) and inclination angle (φ). Module components:

- Aligned single-fiber pullout (debonding → slippage stages)
- Inclined-fiber pullout (inclination, snubbing effect)
- Random distributions of fiber position and orientation
- Additional mechanisms: two-way pullout, matrix micro-spalling, the Cook-Gordon
  effect, and fiber rupture

## Lineage

| Year | Development |
|---|---|
| 1992 | Li: closed-form solution for hydrophobic (friction-dominated) fibers |
| 1997 | Lin-Li: slip-hardening interfaces considered |
| 1998–1999 | apparent fiber strength; chemical bond introduced |
| 2008 | Yang et al.: numerical solution (extensible to new mechanisms) |
| 2015 | Huang et al.: closed-form solution for hydrophilic fibers (two-way pullout + rupture included) |

## Behavior differences by interface type

- Hydrophobic (PE): friction-dominated, slip-softening after the peak. Pullout load
  decreases with slip.
- Hydrophilic (PVA): chemical bond G_d + friction τ_0 + slip-hardening coefficient β.
  After complete debonding the load drops sharply, then rises again through the jamming
  effect of fibrillation on the fiber surface.

## Role

From the σ_B(δ) curve, the complementary energy J′_b (related to the area under the
curve) and the peak bridging stress σ_0 feed respectively into the energy and strength
criteria of [[pseudo-strain-hardening-criteria]]. The curve shape itself is the input to
steady-state crack analysis.

## Related Notes

- [[li-2023-ecc-micromechanics-critical-review]] — origin review
- [[pseudo-strain-hardening-criteria]] — design criteria this law feeds into
- [[qiu-2016-fatigue-dependent-fiber-bridging-model]] — first model adding a fatigue axis
  (N, σ_max) to the static σ_B(δ); predicts σ_0 and dissipated-energy degradation through
  interface hardening (γ_d, γ_s) and in-situ fiber strength reduction.
- [[chen-2025-damaged-rc-beams-strengthened-uhpc]] — structural-scale application:
  measured stress-concentration relief of steel-fiber bridging producing a dense
  microcrack distribution in the UHPC strengthening layer and a 3–5x increase in
  cracking load.
- [[morton-1976-effect-metal-wires-fracture-brittle-matrix-composites]] — experimental origin (1976) of inclined
  pullout load amplification (rope-over-drum snubbing model).
- [[park-2012-tensile-behavior-uhp-hfrc]] — direct tension on 16 UHP-HFRC series
  (200 MPa matrix + coarse fiber 1 % + fine fiber): coarse-fiber type governs the curve
  shape; T-fiber highest (18.6 MPa, 0.64 %).
- [[yang-2008-fiber-bridging-constitutive-law-of-ecc]] — source of the 2008 lineage
  entry: numerical σ(δ) solution integrating two-way pullout, micro-spalling, and
  Cook-Gordon, with experimental validation.

- [[ding-2019-optimal-interfacial-bond-fiber-rupture-hdcc]] — fiber-specific optimal
  interfacial shear strength and the theory of appropriate fiber-rupture compensating energy.
