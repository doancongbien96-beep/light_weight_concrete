---
title: "Interface Bond Properties"
type: concept
source: "[[lin-1999-interface-property-characterization]], [[li-2001-pva-ecc-strain-hardening]], [[ranade-2013-hshdc-micromechanics]]"
date: 2026-08-23
tags: [concept, interface-bond, single-fiber-pullout, chemical-bond, frictional-bond, snubbing, micromechanics]
---

# Interface Bond Properties (fiber-matrix interface)

## Definition

The family of physicochemical interface parameters governing the stress transfer
capacity and bonding mechanisms between a single fiber surface and the cement matrix in
fiber-reinforced composites.

## Core interface parameters and physical meaning

1. **Chemical bond debonding energy ($G_d$)**:
   - Energy required per unit interface area to separate (debond) the chemical bond
     between fiber and matrix (J/m²).
   - Hydrophilic PVA fibers can carry excessive $G_d$ through hydroxyl (-OH) bonding,
     causing premature rupture before pullout; oil coating (about 0.8–1.2 wt.%) tunes it
     to an appropriate level.
2. **Frictional shear strength ($\tau_0$)**:
   - Frictional shear stress acting as the fiber slides out of the matrix after
     debonding (MPa).
   - Too low: fibers slip out easily and maximum bridging stress ($\sigma_0$) falls.
     Too high: fiber rupture dominates and ductility degrades.
3. **Slip-hardening coefficient ($\beta$)**:
   - Dimensionless coefficient describing slip-hardening behavior in which frictional
     stress rises during pullout through abrasive particle packing and fiber surface damage.
4. **Snubbing coefficient ($f$)**:
   - Coefficient governing the exponential increase of pullout load when the fiber crosses
     the crack at an inclination angle ($\theta$), through the pulley effect:
     $$e^{f\theta}$$

## Single-fiber pullout curve ($P-\delta$) and bridging modeling

- Interface parameters ($G_d, \tau_0, \beta, f$) are measured by single-fiber pullout
  tests and inverse analysis.
- Integrating these micromechanical parameters yields the macroscopic crack-bridging
  constitutive curve $\sigma(\delta)$ of the composite.

## Related parameters

- $G_d$: chemical bond energy (J/m²)
- $\tau_0$: initial frictional shear strength (MPa)
- $\beta$: slip-hardening coefficient
- $f$: snubbing coefficient
- $d_f, L_f$: fiber diameter and embedded length (µm, mm)

## Related Notes

- [[lin-1999-interface-property-characterization]] — origin paper integrating the three
  interface parameters ($G_d, \tau_0, \beta$) with snubbing into one constitutive law.
- [[li-2001-pva-ecc-strain-hardening]] — interface tailoring via PVA oil coating and PSH
  achievement, origin paper.
- [[ranade-2013-hshdc-micromechanics]] — inclination-dependent interface hardening in
  high-strength matrices.
- [[fiber-bridging-constitutive-law]] — macroscopic bridging stress-opening models built
  on interface parameters.
- [[pseudo-strain-hardening-criteria]] — securing PSH margins through interface control.
