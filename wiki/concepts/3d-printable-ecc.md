---
title: "3D Printable ECC"
type: concept
source: "[[li-2023-ecc-micromechanics-critical-review]], [[lu-2017-fiber-orientation-thickness]]"
date: 2026-08-23
tags: [concept, 3d-printing, additive-manufacturing, printability, buildability, fiber-alignment, anisotropy, rheology]
---

# 3D Printable ECC (strain-hardening composites for additive manufacturing)

## Definition

Construction material for additive manufacturing that combines 3D concrete printing
(3DCP) — layer-by-layer extrusion through a nozzle without formwork — with the highly
ductile strain-hardening (ECC/SHCC) mechanism.

## Key requirements and physical trade-offs

1. **Fresh rheology**:
   - **Extrudability**: low yield stress and shear-thinning behavior for smooth,
     clog-free flow through the nozzle.
   - **Buildability**: rapid recovery of static yield stress and thixotropy so freshly
     extruded layers carry their self-weight and the load of layers above.
2. **Fiber alignment and mechanical anisotropy**:
   - The intense shear field in narrow-nozzle extrusion aligns the discontinuous short
     fibers **highly parallel to the printing direction**.
   - **Longitudinal (print-line direction)**: orientation factor
     $\eta_\theta \approx 0.9$ or above, maximizing direct tensile strength (>8 MPa)
     and tensile strain capacity (4–8 %), far exceeding mold-cast ECC.
   - **Transverse and interlayer directions**: fiber bridging is absent across layers,
     creating relatively weak cold-joint interfaces; interface interlocking design is
     therefore critical to overcome anisotropy.

## Mix and printing parameters

- Binders: high-volume fly ash (HVFA), silica fume, viscosity-modifying admixture (VMA),
  thixotropy-enhancing agents (nanoclay).
- Fibers: high-modulus PE fibers, PVA fibers (length 6–12 mm).
- Printing variables: nozzle diameter/shape, extrusion rate, travel speed, layer interval time.

## Related Notes

- [[lu-2017-fiber-orientation-thickness]] — theory of fiber orientation factors in
  extrusion and thin members.
- [[fiber-orientation-distribution]] — flow-induced orientation and anisotropy
  constitutive modeling.
- [[strain-hardening-mechanism]] — conditions for tensile strain-hardening in printed members.
- [[qian-2010-self-healing-ecc-nanoclay]] — nanoclay-modified composite for rheology control.
