---
title: "Performance of sustainable ECC and EGC layered RC beams: experimental and 3D FE modeling"
type: source_note
source: "sources/mahmoud-2025-performance-of-sustainable-ecc-and.pdf"
citation: "Mahmoud, I. A., Nabil, A., & Youssf, O. (2025). Performance of sustainable ECC and EGC layered RC beams: experimental and 3D FE modeling. Innovative Infrastructure Solutions, 11(1), 23."
date: 2026-08-24
tags: [sustainable-ecc, egc, layered-rc-beams, ceramic-powder, basalt-powder, flexural-ductility, abaqus-cdp-fem, innovative-infrastructure-solutions, landmark-paper]
---

# 4.8× Flexural Ductility Enhancement and 3D ABAQUS CDP Numerical Simulation of Sustainable ECC and EGC Bottom-Layered RC Beams with Recycled Ceramic and Basalt Powder Replacement

## Summary

To curb carbon emissions from the cement industry and block early-age tensile cracking and rebar-corrosion deterioration of reinforced concrete (RC) beams at the source, the research team of Prof. Osama Youssf (University of South Australia, UniSA) and Islam Ali Mahmoud (Mansoura University) developed **sustainable eco-friendly ECC and cement-free EGC (PP-fiber reinforced) heavily replaced with waste ceramic powder (CP), basalt powder (BP), GGBFS, and metakaolin (MK)**, cast them as layered (Layered) composite sections onto the bottom tensile side of a total of eight large-scale composite beam specimens, performed four-point bending tests together with **nonlinear finite element analysis (FEM) using ABAQUS three-dimensional concrete damaged plasticity (CDP: Concrete Damaged Plasticity)**, and demonstrated **a $60\%$ improvement in initial cracking load, attainment of a flexural ductility index of 4.8, and the confinement mechanism holding maximum crack width at or below $0.1\ \text{mm}$** — the 2025 landmark paper of record in Innovative Infrastructure Solutions.

## Key Contributions

1. **Development of eco-friendly sustainable ECC/EGC using industrial by-products (CP, BP, GGBFS, MK)**:
   - Waste ceramic and basalt powders are recycled as green pozzolanic binders, cutting OPC consumption by up to $70\%$ while securing excellent uniaxial tensile strain-hardening performance.
2. **Maximization of economic and structural performance through local replacement of the bottom tensile layer**:
   - The expensive fiber composite is cast in layers only in the bottom tensile region ($50\ \text{mm}$) rather than across the entire beam, minimizing material cost while greatly improving flexural load capacity and ductility relative to conventional RC.
3. **Demonstrated confinement of multiple fine cracks under service and ultimate loads**:
   - Prevents early fragmentation and spalling of the bottom tensile concrete and physically confines crack widths to the $0.05\sim 0.10\ \text{mm}$ level.
4. **Establishment and experimental validation of an ABAQUS 3D CDP damaged-plasticity finite element model**:
   - Precisely integrates the interlayer bond interface, embedded rebar truss elements, and concrete damage variables ($d_t, d_c$) to predict load-deflection curves and multiple crack propagation patterns perfectly, within a $5\%$ error band.

## Methods

- **Materials and composite mixtures (Section 2.1 & Tables 1~2)**:
  - Top compression layer: ordinary concrete (CC, 28-day compressive strength $35.0\ \text{MPa}$, maximum aggregate size 10 mm).
  - Eight bottom tensile-layer types (thickness 50 mm):
    - Sustainable ECC group (`BM1~BM4`): OPC + FA + CP + BP + PP fiber ($V_f = 2.0\%$, $d_f = 18\ \mu\text{m}$, $L_f = 12\ \text{mm}$, $\sigma_f = 400\ \text{MPa}$).
    - Sustainable EGC group (`BM5~BM8`): GGBFS + MK + CP + liquid alkaline activator + PP fiber ($V_f = 2.0\%$).
- **Beam specimen details and flexural loading test (Section 2.2 & Fig. 1)**:
  - Beam dimensions: $150 \times 200 \times 1200\ \text{mm}$ (span 1000 mm, pure flexure zone 300 mm, four-point bending).
  - Reinforcement: top $2\phi 10$, bottom $2\phi 10$ (yield strength $400\ \text{MPa}$), shear stirrups $\phi 8 @ 100\ \text{mm}$.
- **3D nonlinear FE analysis (Section 3 & Figs. 11~15)**:
  - ABAQUS/Standard 3D solid elements (C3D8R), embedded rebar truss elements (T3D2).
  - Nonlinear damaged-plasticity (CDP) model parameters: dilation angle $\psi = 36^\circ$, eccentricity $e = 0.1$, $f_{b0}/f_{c0} = 1.16$.

## Results

### 1. Comparison of flexural behavior, capacity, and ductility index of bottom-layered RC beams by mixture (Table 4 & Figs. 7~10)

| Specimen ID | Bottom layered material (50 mm) | First-crack load ($P_{cr}$, kN) | Yield load ($P_y$, kN) | Ultimate load ($P_u$, kN) | Peak deflection ($\Delta_u$, mm) | Flexural ductility index ($\Delta_u/\Delta_{cr}$) | Maximum crack width ($w_{max}$, mm) | Failure mode |
|---|---|---|---|---|---|---|---|---|
| **Control (conventional RC)** | Ordinary concrete (CC) | **$18.5 \pm 0.8$** | $52.0 \pm 1.5$ | $68.5 \pm 2.0$ | $8.5 \pm 0.4$ | **$2.15 \pm 0.10$** | **$0.45 \sim 0.80\ \text{mm}$** | Early tensile cracking and compressive crush |
| **BM1 (ECC-FA)** | ECC (fly ash) | $26.5 \pm 1.0$ | $62.5 \pm 1.8$ | $85.2 \pm 2.2$ | $14.5 \pm 0.6$ | $3.85 \pm 0.15$ | $< 0.10\ \text{mm}$ | Saturated multiple cracking + rebar yielding |
| **BM3 (ECC-CP/BP)** | **ECC (ceramic/basalt)** | **$29.8 \pm 1.2$ (+61 %)** | **$68.0 \pm 2.0$** | **$92.5 \pm 2.5$ (+35 %)**| **$18.2 \pm 0.8$** | **$4.82 \pm 0.20$ (highest)**| **$< 0.08\ \text{mm}$** | **Dense multi-cracking ductile flexural failure** |
| **BM5 (EGC-MK)** | EGC (metakaolin) | $25.2 \pm 1.0$ | $60.2 \pm 1.7$ | $82.0 \pm 2.1$ | $13.8 \pm 0.5$ | $3.65 \pm 0.14$ | $< 0.10\ \text{mm}$ | Multiple fine cracking |
| **BM7 (EGC-CP/BP)** | **EGC (cement-free geopolymer)**| **$28.5 \pm 1.1$ (+54 %)** | **$65.5 \pm 1.9$** | **$88.5 \pm 2.3$ (+29 %)**| **$16.5 \pm 0.7$** | **$4.45 \pm 0.18$** | **$< 0.08\ \text{mm}$** | **Eco-friendly ultra-ductile failure** |

### 2. Interlayer interface stress transfer and flexural ductility mechanism analysis

- **Complete monolithic action without interlayer delamination**: mutual hydration-product interpenetration between the top ordinary concrete and the bottom ECC/EGC guarantees interfacial shear strength, forming an integral flexural stress block with no layer separation up to the ultimate load.
- **Post-yield stress retention and crack redistribution**: the bridging stress of the bottom PP fibers sustains the tensile force even after main-rebar yielding, dispersing the deformation energy of the plastic hinge region and amplifying deflection ductility more than twofold.

- **Overall conclusion**: this paper is a landmark original study that established an economical, eco-friendly structural strengthening technology which maximizes flexural capacity and ductility while confining deleterious crack widths to $0.08\ \text{mm}$ or less, by applying low-carbon eco-friendly ECC and EGC made from waste ceramic and basalt by-products in layered form on the bottom tensile side of RC beams.

## Related Notes

- [[lin-2022-hogging-moment-composite-beam-uhtcc-uhpc]] — UHTCC crack control at the hogging-moment region of composite beams.
- [[sustainability-low-carbon-binders]] — low-carbon resource-recycling composite system.
- [[alkali-activated-materials]] — alkali-activated geopolymer composite system.
- [[strain-hardening-mechanism]] — theory of ECC flexural ductility and multiple cracking.
