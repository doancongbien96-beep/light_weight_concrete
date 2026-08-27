---
title: "Effect of High Temperatures on Hot-Bonded SCC/ECC and SCC/UHPC Composite Systems (Baloch et al., 2023)"
type: source_note
source: "sources/Baloch 등 - 2023 - Effect of high temperatures on hot-bonded SCCECC and SCCUHPC composite systems.pdf"
citation: "Baloch, W.L., Siad, H., Lachemi, M., Sahmaran, M. Effect of high temperatures on hot-bonded SCC/ECC and SCC/UHPC composite systems. Construction and Building Materials 369 (2023) 130507. doi: 10.1016/j.conbuildmat.2023.130507"
date: 2026-08-22
tags: [ecc, uhpc, scc, composite-system, high-temperature, interfacial-bond, pva-fiber, steel-fiber]
---

# Flexural and bond behavior of hot-bonded SCC/ECC and SCC/UHPC composite systems after high-temperature exposure

## Summary

Four functionally graded composite systems were built by wet-on-wet (hot-joint) continuous
casting — an ECC or UHPFRC tension layer (each with PVA or steel fiber at 2 vol %) over an
SCC compression layer — then heated to 23–800 °C (side heating, 2.5 h soak at target,
air-cooled) for residual flexural performance and split-tension interlayer bond strength.
Key finding: the wet interface is not a structural weakness but delivers higher tensile bond
than monolithic SCC (+19.1–45.6 %); above 400 °C the fibers' thermal stability (PVA pyrolysis
versus steel survival) becomes the governing factor of residual performance. At 800 °C only
the steel-fiber UHPFRC system vanished by explosion while the PVA-UHPFRC system survived —
an inversion.

## Key Contributions

1. **Superiority of the wet interface demonstrated**: thanks to simultaneous hydration at
   fresh-to-fresh casting plus fibers crossing the interface, split-tension bond strength at
   ambient exceeded monolithic SCC by CS-EC-PV +19.1 %, CS-EC-SF +31.9 %, CS-UH-PV +34.7 %,
   CS-UH-SF +45.6 %. The concrete-to-concrete interface treated as a weakness in repair
   engineering is not the weakest plane in a hot joint.
2. **PVA pyrolysis creates a 400 °C brittleness transition**: PVA melts at 230 °C; above
   400 °C pyrolysis forms interfacial tunnels → PVA-based systems switch from ductile to
   brittle failure from 400 °C (no PVA fibers on fracture faces). Steel-fiber systems keep
   ductility to 600 °C.
3. **The CS-UH-SF spalling paradox**: steel-fiber UHPFRC leads all specimens up to 600 °C
   (P_MOR 6.43 kN @ 600 °C), but thermal explosion in the 690–700 °C window leaves no 800 °C
   data (the >650 °C spalling vulnerability of SF-UHPFRC alone [11] governs unchanged). The
   PVA-UHPFRC system instead survives 800 °C without spalling or delamination — molten PVA
   creates pore-pressure relief channels.
4. **Interfacial hydration differences quantified by SEM/EDS**: after 600 °C exposure the
   Si/Ca ratio across SCC/interface/UHPC layers was 0.63/0.78/0.96 versus 0.46/0.52/0.56 for
   SCC/interface/ECC. UHPFRC's low w/b secondary hydration (xonotlite/tobermorite-stable C-S-H)
   densifies and stiffens interfacial C-S-H — the microscopic basis of bond retention.
5. **Regression models for FEA/ANN inputs**: logistic-linear regressions of β_T coefficients
   on exposure temperature T for P_MOR, tensile bond, and mass loss (e.g., CS-EC-PV
   β_T,PMOR = 0.9035 − 0.001109T), R² = 91–98 % — early examples of high-temperature residual-
   performance models at composite-system scale.

## Methods

- **Mixes** (Table 2): ECC = OPC + GGBS/c 1.2 + silica sand 0.8, w/c 0.58, PVA or SF at
  2.0 vol % (fc 76.2/80.7 MPa, flexure 13.8/13.4 MPa). UHPFRC = HE cement + silica fume/c 0.2
  + GGBS/c 0.25 + silica sand 0.8 + quartz flour 0.35, w/c 0.21 (fc 112.2/138.6 MPa, flexure
  19.7/26.8 MPa). SCC = OPC 350 kg/m³, FA/c 0.43, w/c 0.48 (fc 44.2 MPa, flexure 8.5 MPa).
  Slump flow 670 mm (SCC), mortar flow ≥ 180 mm (ECC/UHPFRC).
- **Fibers** (Table 1): PVA 8 mm × 38 μm, E 42 GPa, 1620 MPa, melting point 230 °C. Steel
  fiber 13 mm × 0.2 mm, E 200 GPa, 2750 MPa.
- **Specimens and tests**: 50 × 76 × 355 mm prisms (bottom ECC/UHPFRC 38 mm + top SCC 38 mm,
  cast continuously without surface treatment or compaction), 90 units + 30 monolithic SCC →
  four-point flexure (ASTM C1609, 0.05 mm/min). Cut cuboids 50 × 76 × 76 mm, 120 units →
  split-tension bond (ASTM C496, 0.1 MPa/s). Electric-furnace side heating to
  200/400/600/800 °C + 2.5 h hold + air cooling (furnace curve compared against ISO 834 and
  ASTM E119). Mass loss, surface color-change and crack observation, SEM/EDS (interface of
  200 °C and 600 °C specimens).

## Results

- **Flexural peak load P_MOR (kN)**:

| Temperature | SCC | CS-EC-PV | CS-EC-SF | CS-UH-PV | CS-UH-SF |
|---|---|---|---|---|---|
| 23 °C | 5.24 | 8.10 (+54.6 %) | 8.34 (+59.1 %) | 12.10 (+130.7 %) | 12.53 (+139.1 %) |
| 200 °C | 3.92 | 4.69 | 5.89 | 9.48 | 11.25 |
| 400 °C | 2.43 | 3.10 | 4.43 | 5.03 | 10.81 |
| 600 °C | 1.07 | 1.83 | 2.00 | 0.80 | 6.43 |
| 800 °C | 0.31 | 0.70 | 1.15 | 0.34 | –*(spalled) |

- Ambient Δ_MOR: CS-EC-PV +128.1 %, CS-EC-SF +85.4 %, CS-UH-PV +56.2 %, CS-UH-SF +50.6 %;
  initial stiffness +59.1–215.6 %; proportional-limit energy absorption 10.4/9.3/24.1/23.4x
  SCC (5.8–16.1x at ultimate). P_LOP < P_MOR in every specimen — deflection hardening.
- **Bond strength reduction**: at 400 °C EC-PV −28.3 %, EC-SF −21.7 %, UH-PV −18.6 %,
  UH-SF −6.9 % (monolithic SCC beyond −35 %). Retention at 600 °C: EC-PV 40 %, EC-SF 52 %,
  UH-PV 28 % (anomalous collapse from PVA pyrolysis plus interface cracking; P_LOP 0.46 kN),
  UH-SF 50 %. At 800 °C monolithic SCC −88.7 % (calcareous aggregate decarbonation), CS
  systems generally over −75 %.
- **Failure modes**: below 400 °C all CS specimens ductile (flexural cracks starting at the
  soffit with fine cracking). From 400 °C PVA systems failed brittle without warning while
  steel-fiber systems kept ductility with gentle softening. Interface delamination or
  horizontal slip occurred nowhere up to 800 °C except the exploded CS-UH-SF specimens.
- **SEM**: at 200 °C the interfacial transition zone carries constituents of both mixes
  (fibers + coarse aggregate particles) undamaged. At 600 °C PVA systems show tunnels crossing
  the interface (melted-PVA traces) with propagated cracks, worst in CS-EC-PV. Even so, no
  complete debonding beyond 600 °C.

## Related Notes

- [[lv-2025-high-temperature-ternary-egc-pe]] — temperature-spectrum comparison of PE's thermal
  weakness (~150 °C) versus PVA (230 °C melt, 400 °C pyrolysis); EGC matrices are more heat
  resistant, so 800 °C no-spalling is their common conclusion.
- [[abbas-2016-uhpc-mechanical-performance-durability-sustainability]] — origin of the dense-UHPC
  vapor-pressure spalling vulnerability and PP/PVA melting-fiber mitigation logic; directly
  connected to the CS-UH-SF explosion and CS-UH-PV survival results here.
- [[cheng-2024-ceramsite-lw-egc-high-temp]] — high-temperature residual performance of ceramsite
  LWA EGC; lightweight route contrasted with this paper's functional layering route.
- [[sahmaran-2009-aggregate-type-size-ecc]] · Sahmaran et al. 2011 (JMCE 23, high-temperature ECC
  residual performance, references [2][43]) — co-author Şahmaran group's ECC thermal lineage.
- [[li-mo-2011-hes-ecc-repair]] · [[kumar-2022-egc-repair-sand-binder-ratio]] — cases extending
  the bonding topic of ECC/EGC overlay repair to fresh-to-fresh new casting.
- [[pseudo-strain-hardening-criteria]] — deflection hardening judgment of the CS prisms
  (P_LOP < P_MOR) is the flexural version of the PSH criterion.
