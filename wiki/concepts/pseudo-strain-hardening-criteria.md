---
title: "Pseudo Strain-Hardening Criteria (PSH)"
type: concept
source: "[[li-2023-ecc-micromechanics-critical-review]]"
date: 2026-08-22
tags: [concept, strain-hardening, micromechanics, design-criteria]
---

# Pseudo Strain-Hardening Criteria (PSH)

## Definition

The micromechanical necessary conditions for a composite to exhibit strain-hardening
rather than strain-softening under tension. Both criteria must hold simultaneously.

- Energy criterion: J′_b ≥ J_tip — the complementary energy of fiber bridging must
  exceed the crack-tip toughness so the crack propagates in a steady-state mode.
  Physically, the net energy supplied by external work must exceed the crack-tip energy
  required for unlimited crack extension.
- Strength criterion: σ_0 ≥ σ_c — the maximum bridging stress must reach the matrix
  cracking strength so cracking initiates at multiple flaw sites instead of localizing
  at a single defect.

## Interpretation

The energy criterion determines the crack propagation mode; the strength criterion
determines the multiplicity of crack initiation. Even when both are satisfied, multiple
cracks form sequentially, and the first crack is generally not the final failure crack.
This follows from microstructural heterogeneity (fiber diameter scatter, flaw size and
distribution, curing variability).

## Design margin indices

Margins are applied as safety factors to account for heterogeneity. Experimentally
grounded values:

| System | J′_b/J_tip | σ_0/σ_c | Source |
|---|---|---|---|
| PE-ECC | > 3 | > 1.2 | Kanda-Li 1998 experiments |
| PVA-ECC (some mixes) | - | ≈ 1.45 | Kanda 1998 |

The margin index must be determined experimentally for each mix. As a probabilistic
alternative, Li-Yang 2018 treat the parameters as random variables, define limit-state
surfaces G(x)=J′_b−J_tip=0 and F(x)=σ_0−σ_c=0, and evaluate hardening potential via
the failure probability P_f.

## Validity of the indices: matrix dependence (accumulated evidence in this wiki)

- **σ_0/σ_fc ≥ 1.2–1.3 is a robust discriminator**: in both Nematollahi 2017
  (lightweight EGC, [[nematollahi-2017-lightweight-aggregate-egc]]) and Artyk 2024
  ([[artyk-2024-low-activity-fly-ash-hybrid-fiber-egc]]), mixes exceeding this range
  achieved saturated multiple cracking with strain capacity ≥ 1.5 %.
- **The discriminating power of J′_b/J_tip ≥ 2.7 depends on the matrix**: in matrices
  with low K_m such as low-activity fly ash, ductility may be absent even when
  J′_b/J_tip > 5 (Artyk 2024). In one-part SHGC (Nematollahi 2017), by contrast, the
  difference in the energy index explained the difference in strain capacity exactly.
- **Relative comparison of the indices is more useful than absolute thresholds**:
  within a single matrix, comparisons across curing conditions or fiber types show the
  ranking of PSH indices matches the measured ranking of strain capacity (Nematollahi
  2017 one-part SHGC).
- **Parameter interpretation**: aggregate shape (spherical → lower K_m), alkalinity
  (higher → higher J_tip; [[han-2022-egc-impact-cold-temperature]],
  [[feng-2024-chloride-egc-mix-parameters]]), and FA content (lower G_d, higher τ,
  lower J_tip; [[sahmaran-2009-aggregate-type-size-ecc]]) shift the balance between σ_c
  and σ_0 along paths repeatedly confirmed across this wiki.

## Related Notes

- [[li-2023-ecc-micromechanics-critical-review]] — origin review
- [[fiber-bridging-constitutive-law]] — curve from which J′_b and σ_0 are defined
- [[nematollahi-2017-one-part-pe-shgc-micromechanics]] — standard procedure for computing
  the indices and interface data
- [[cho-2012-basic-mixing-and-mechanical-tests]] — measured case applying the PSH index
  frame unchanged to a cement-free (alkali-activated slag) matrix: strength index
  improved under the B2 activator → tensile strain capacity +16.7 %.
- [[park-2012-tensile-behavior-uhp-hfrc]] — direct tension on 16 UHP-HFRC series
  (200 MPa matrix + coarse fiber 1 % + fine fiber): coarse-fiber type governs the curve
  shape; T-fiber highest (18.6 MPa, 0.64 %).
- [[zhou-2010-limestone-slag-ecc]] - M1–M6 experiments showing strong linear correlation
  between the sigma_pc - sigma_cc margin and strain capacity (R^2 = 0.98); representative
  empirical data for the margin criteria.
