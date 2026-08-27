---
title: "Fiber Orientation Distribution"
type: concept
source: "[[lu-2017-fiber-orientation-thickness]], [[kwon-2012-radial-flow-uhpfrcc-tensile]], [[kang-2008-fiber-orientation-impacts-on-the]]"
date: 2026-08-23
tags: [concept, fiber-orientation, orientation-factor, flow-induced-orientation, size-effect, micromechanics]
---

# Fiber Orientation Distribution

## Definition

The probabilistic statistical distribution of angles and directions along which
discontinuous short fibers arrange themselves in space within a composite. It is
determined by the composite's 1D, 2D (planar random), or 3D (spatial random) orientation
state and by the casting flow.

## Physical significance and effects

The more parallel fibers lie to the load direction, the greater the effective bridging
stress ($\sigma_0$) and energy absorption efficiency. Fibers perpendicular to the load
contribute almost nothing to tensile bridging.

1. **Orientation factor ($\eta_\theta$ / $\alpha_f$)**:
   - 1D aligned (load-parallel): $\eta_\theta = 1.0$
   - 2D random (thin plates, $t < L_f$): $\eta_\theta = \frac{2}{\pi} \approx 0.637$
   - 3D random (bulk members, $t \gg L_f$): $\eta_\theta = 0.500$
2. **Wall effect and thickness size effect**:
   - Near mold walls and thin-member boundaries fibers cannot penetrate the wall surface,
     forcing planar (2D) alignment.
   - The thinner the member, the higher the effective orientation factor rises — a
     geometric size effect that increases tensile strength and strain capacity.
3. **Flow-induced alignment**:
   - Fresh-paste rheology and casting direction (extrusion, pipe flow, radial flow) rotate
     and align fibers along the shear flow (per Jeffery's equation).

## Related parameters

- $\theta$: angle between fiber axis and crack-plane normal vector (rad, °)
- $p(\theta)$: fiber angular probability density function
- $\eta_\theta$: mean effective orientation factor ($\int \cos\theta \cdot p(\theta) d\theta$)
- $L_f, t$: fiber length and member thickness (mm)

## Related Notes

- [[lu-2017-fiber-orientation-thickness]] — thickness-dependent fiber orientation theory
  and size effect (HKUST).
- [[kwon-2012-radial-flow-uhpfrcc-tensile]] — orientation evolution in radial flow of
  UHPFRCC and flexural prediction.
- [[kang-2008-fiber-orientation-impacts-on-the]] — casting-direction dependence of
  orientation and impact resistance.
- [[barnett-2010-assessment-of-fibre-orientation-in]] — evaluation techniques and image
  analysis of fiber orientation.
- [[fiber-bridging-constitutive-law]] — base constitutive formulation integrating the
  orientation distribution into bridging curves.

- [[eik-2012-raytraced-images-fibre-orientation]] — POV-Ray raytracing-based ODF
  measurement-error correction for 3D fiber orientation.

- [[ferrara-2011-casting-flow-induced-fibre-orientation]] — flow-induced orientation in
  FR-SCC casting and flexural strain-hardening of 30 mm ultra-thin slabs.
