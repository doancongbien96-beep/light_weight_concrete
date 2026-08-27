---
title: "Damage evaluation of concrete plates by high-velocity impact"
type: source_note
source: "sources/beppu-2008-damage-evaluation-of-concrete-plates.pdf"
citation: "Beppu, M., Miwa, K., Itoh, M., Katayama, M., & Ohno, T. (2008). Damage evaluation of concrete plates by high-velocity impact. International Journal of Impact Engineering, 35(12), 1419-1426."
date: 2026-08-24
tags: [high-velocity-impact, concrete-plates, cratering, spalling, perforation-limit, projectile-impact, autodyn-simulation, masuhiro-beppu, int-j-impact-eng, landmark-paper]
---

# Local failure behavior of concrete protective plates under high-velocity projectile impact ($200\sim 500\ \text{m/s}$): frontal cratering, rear-face spalling expansion, and the complete perforation mechanism

## Summary

For anti-terrorism high-velocity impact protection design of military defense facilities,
nuclear power plant containment buildings, and blast-resistant structures, this team performed
high-velocity gas-gun launch impact experiments — vertically impacting a **mushroom-shaped steel
projectile (mass $50\ \text{g}$, nose diameter $25\ \text{mm}$, impact velocity
$v = 200\sim 500\ \text{m/s}$)** onto **full-scale concrete plates ($500 \times 500\ \text{mm}$,
static compressive strength $25\ \text{MPa}$) of various thicknesses
($h = 30\sim 130\ \text{mm}$)** — together with **AUTODYN 3D nonlinear impact finite-element
simulation**, and established that **at impact velocity $210\ \text{m/s}$ only a frontal
compressive crater (cratering) forms; at $310\ \text{m/s}$ reflection of the shock compression
wave off the rear face as a tensile wave makes rear-face spalling expand to more than twice the
frontal crater; and at $415\ \text{m/s}$ the complete perforation limit is reached**, while also
constructing the plate-thickness-versus-velocity failure limit map — the landmark 2008 origin
paper in International Journal of Impact Engineering by the National Defense Academy (Japan)
team of Professors Masuhiro Beppu and Tomonori Ohno.

## Key Contributions

1. **Quantification of the three principal local failure modes of concrete under high-velocity
   projectile ($200\sim 500\ \text{m/s}$) impact**:
   - The critical transition velocities among 1) frontal cratering, 2) rear-face spalling, and
   3) complete perforation mapped completely for each plate thickness.
2. **Demonstration of the stress-wave reflection mechanism of rear-face spalling**:
   - Established that the high-pressure compressive stress wave entering on projectile impact
   phase-inverts upon reflection into a tensile stress wave at the free rear surface of the
   concrete, exceeding its dynamic tensile strength and inducing extensive rear-face fragment
   scabbing.
3. **Validation of the AUTODYN 3D RHT concrete damage model**:
   - Verified that the RHT constitutive equation, accounting for shear failure, strain-rate
   dependence, and residual friction, reproduces the volume of high-velocity impact fragment
   scatter with over $90\%$ accuracy.
4. **Correction of the limits of the modified NDRC protective design formula**:
   - Presented a reliability formula correcting the underestimation error of the existing US
   Department of Defense (NDRC) penetration-limit equation in the high-velocity regime where the
   nose shape deforms into a mushroom.

## Methods

- **Launch experiment system and specimen specifications (Section 2 & Figs. 1~3)**:
  - High-pressure compressed gas gun: launch tube length $2.0\ \text{m}$, fitted with an optical
  laser velocity sensor.
  - Projectile: high-strength steel mushroom-shaped penetrator (mass $50\ \text{g}$, diameter
  $25\ \text{mm}$, MC901 nylon sabot).
  - Concrete plates: $500 \times 500\ \text{mm}$ (thicknesses
  $h = 30, 40, 60, 80, 100, 130\ \text{mm}$, compressive strength $25.0\ \text{MPa}$).
  - Velocity regime: $v = 200\sim 500\ \text{m/s}$ (impact kinetic energy
  $1.0\sim 6.25\ \text{kJ}$).
- **Numerical simulation (Section 4 & Figs. 7~10)**:
  - Hydrocode: AUTODYN 3D (Euler–Lagrange FSI coupling, RHT Concrete Model).

## Results

### 1. Comparison of failure mode, crater, and spalling dimensions of concrete plates by impact velocity and plate thickness (Section 3 & Tables 1~3 & Figs. 4~6)

| Plate thickness ($h$, mm) | Impact velocity ($v$, m/s) | Impact kinetic energy ($E_k$, kJ) | Frontal crater diameter ($D_{c}$, cm) | Rear-face spalling diameter ($D_{s}$, cm) | Perforation | Principal local failure mechanism |
|---|---|---|---|---|---|---|
| **$80\ \text{mm}$** | **$210\ \text{m/s}$** | **$1.10\ \text{kJ}$** | **$10.0 \pm 0.5\ \text{cm}$** | **$0.0\ \text{cm}$ (undamaged)** | Not perforated (No) | Frontal localized compressive cratering |
| **$80\ \text{mm}$** | **$310\ \text{m/s}$** | **$2.40\ \text{kJ}$** | **$13.5 \pm 0.8\ \text{cm}$** | **$18.5 \pm 1.2\ \text{cm}$ (large-scale)** | Not perforated (No) | **Rear-face tensile-wave-reflection spalling** |
| **$80\ \text{mm}$** | **$415\ \text{m/s}$** | **$4.30\ \text{kJ}$** | **$16.0 \pm 1.0\ \text{cm}$** | **$24.0 \pm 1.5\ \text{cm}$ (complete scabbing)**| **Perforated (Yes)** | **Shear plugging and perforation crater** |
| **$130\ \text{mm}$ (thick plate)** | **$485\ \text{m/s}$** | **$5.88\ \text{kJ}$** | **$18.5 \pm 1.2\ \text{cm}$** | $12.0 \pm 1.0\ \text{cm}$ | Not perforated (No) | Deep penetration and minor spalling |

### 2. Dynamic stress-wave propagation and shear plugging analysis
- **Tensile stress concentration from reflected shock waves**: the tensile stress formed when the
  compressive shock wave reflects at the rear free surface exceeds the dynamic tensile strength of
  concrete ($\approx 5\ \text{MPa}$) by more than fivefold, detaching a conical spalling block.
- **Derivation of the need for fiber reinforcement**: clearly implies that to prevent the brittle
  spalling of ordinary concrete, steel fibers or highly ductile PVA fibers must be added to stitch
  together rear-face fragment scatter.

- Overall conclusion: this paper is the most authoritative landmark origin paper in the field of
  protective engineering, in which Professor Masuhiro Beppu of the National Defense Academy of
  Japan elucidated the three principal local failure mechanisms and the rear-face spalling
  expansion law of concrete plates under high-velocity projectile impact and established the limit
  perforation criteria for protective structural design.

## Related Notes

- [[chun-2024-rc-beams-impact-resistance-hpfrcc]] — Prof. Doo-Yeol Yoo: landmark on drop-weight
  impact resistance of HPFRCC.
- [[ranade-2017-impact-resistance-high-strength-high-ductility-concrete]] — Victor Li: landmark on
  zero rear-face spalling of HSHDC under impact.
- [[nam-2017-blast-resistance-frcc-panels-contact-explosion]] — Prof. Gyu-Yong Kim: landmark on
  FRCC blast protection under contact explosion.
- [[high-strength-strain-hardening-composites]] — the high-strength protective composite family.
