---
title: "A Review of Developments and Challenges for UHPC in Structural Engineering: Behavior, Analysis, and Design"
type: source_note
source: "sources/hung-2021-a-review-of-developments-and.pdf"
citation: "Hung, C. C., El-Tawil, S., & Chao, S. H. (2021). A Review of Developments and Challenges for UHPC in Structural Engineering: Behavior, Analysis, and Design. Journal of Structural Engineering, 147(9), 03121001."
date: 2026-08-24
tags: [uhpc, uhpfrc, structural-engineering, r-uhpc-beams-columns, development-length, shear-strength, seismic-retrofitting, asce-jse, state-of-the-art-review, theory-foundation]
---

# Mechanical Behavior, Non-Linear Analysis, Design Provisions, and Engineering Challenges of Reinforced Ultra-High-Performance Concrete (R/UHPC) Structural Members: A Comprehensive Review

## Summary

With ultra-high-performance concrete (UHPC)—featuring compressive strengths exceeding 150 MPa, direct tensile strengths over 8 MPa, and exceptional tensile strain-hardening/crack control—increasingly utilized for lightweighting, seismic resilience, and extreme service-life extension, direct application of conventional concrete codes (ACI 318, AASHTO) to R/UHPC (rebar-reinforced UHPC) members introduces structural inefficiencies and brittle failure risks. To resolve these challenges, a collaborative team from National Cheng Kung University, the University of Michigan, and the University of Texas at Arlington synthesized the state of the art in structural behavior and failure mechanisms across **flexural beams, columns, beam-column joints, shear walls, bridge deck splices, impact/blast barriers, and retrofitting systems**, providing a comprehensive comparative analysis of international design provisions (ACI 239R/AASHTO, French NF P 18-470, Swiss SIA 2052, Japanese JSCE). Due to the high bond strength of UHPC ($\tau_b \ge 10.0\ \text{MPa}$), rebar development and lap splice lengths can be reduced to **$8\sim 10 d_b$** (over 70 % shorter than the $30\sim 40 d_b$ required in conventional concrete) to develop rebar yield strength. Furthermore, the review outlines next-generation limit state design philosophies integrating ultimate compressive strain limits ($\varepsilon_{cu} = 0.015$, 5-fold higher than normal concrete) and tensile bridging contributions to shear capacity ($V_c$).

## Key Contributions

1. **Systematic synthesis of R/UHPC structural member behavior and failure mechanisms**:
   - Clarified mechanics governing flexural members (delayed neutral axis shift via tensile hardening), compression columns (3-fold increase in ductility index), and beam-column joints (50 % reduction in transverse shear rebar).
2. **Standardization of shortened rebar development and splice lengths ($8\sim 10 d_b$)**:
   - Validated that embedment lengths of $8\sim 10 d_b$ with clear covers of $3 d_b$ guarantee full yielding (>420 MPa) across 25~35 mm large-diameter deformed bars.
3. **Formulation of shear resistance models incorporating UHPC fiber bridging**:
   - Integrated fiber bridging tensile stress ($\sigma_{tu}$) into concrete shear contributions ($V_c$), establishing stirrup-free high-shear design formulations.
4. **Comprehensive benchmarking of international UHPC design codes (ACI, AASHTO, NF P 18-470, SIA 2052, JSCE)**:
   - Systematically compared tensile softening/hardening constitutive models, safety factors, and creep/shrinkage design parameters across international standards.

## Methods

- **Structural systems and member topologies analyzed (Sections 2–8)**:
  - Flexural members: Simple beams, continuous beams, and prestressed girders ($1\sim 4\ \text{vol.\%}$ fibers; straight, hooked, and twisted geometries).
  - Compression/beam-column members: R/UHPC columns, hollow-core columns, concrete-filled steel tubes (CFT).
  - Connections: Precast bridge deck loop joints, shear pockets, seismic beam-column connections.
  - Extreme loading: Dynamic resistance under vehicular impact, high-velocity projectile penetration, and blast detonations.
- **International code comparison framework (Section 9)**:
  - ACI 239R (USA), AASHTO Guide Specifications for UHPC (USA), NF P 18-470 (France), SIA 2052 (Switzerland), JSCE Recommendations (Japan).

## Results

### 1. Comparative analysis of international UHPC structural design provisions (Tables 1–3 & Figs. 1–6)

| Design Standard / Agency | Compressive Strength ($f_c'$, MPa) | Ultimate Compressive Strain ($\varepsilon_{cu}$) | Tensile Constitutive Model | Shear Design Approach | Rebar Development / Splice Length |
|---|---|---|---|---|---|
| **USA ACI 239R / AASHTO** | $\ge 120\ \text{MPa}$ | $0.0035 \sim 0.015$ | Bilinear or ignored tension | $V_n = V_{cf} + V_s$ (fiber bridging included) | **$8\sim 10 d_b$** (Ultra-short) |
| **France NF P 18-470** | $\ge 130\ \text{MPa}$ | $0.004 \sim 0.010$ | Trilinear (Hardening/softening with orientation $K$) | $V_{Rd} = V_{Rd,c} + V_{Rd,f} + V_{Rd,s}$ | **$10\sim 12 d_b$** |
| **Switzerland SIA 2052** | $\ge 150\ \text{MPa}$ | $0.005 \sim 0.012$ | Bilinear hardening followed by plastic flow | Direct integration of bridging stress | **$8\sim 10 d_b$** |
| **Japan JSCE** | $\ge 150\ \text{MPa}$ | $0.0035 \sim 0.008$ | Uniaxial fracture energy ($G_F$) model | $V_y = V_{cd} + V_{sd} + V_{fd}$ | **$10\sim 15 d_b$** |

### 2. Structural performance and engineering challenges
- **Rebar bond capacity**: Increasing steel fiber volume fractions from $1\% \rightarrow 2\% \rightarrow 4\%$ increased ultimate bond strength by 29 % and 53 %, exceeding 10 MPa.
- **Ductility in ultra-high-strength matrices**: At fiber dosages $\ge 2.0\ \text{vol.\%}$, R/UHPC column axial ductility indices increased by 200~300 % over standard RC, achieving displacement ductility factors > 4.0.

- **Overall conclusion**: This review provides a comprehensive synthesis of experimental findings, analytical modeling, and international design provisions for reinforced UHPC structures.

## Related Notes

- [[high-strength-strain-hardening-composites]] — Material mechanics of UHPC and high-strength composites.
- [[structural-repair-and-retrofitting]] — Structural rehabilitation and joint engineering with UHPC.
- [[choi-2016-fiber-orientation-uhpcc-post-cracking-tensile]] — Fiber orientation and tensile constitutive models in UHPCC.
- [[esfahani-2020-hpfrcc-substitution-gfrp-rc-beams]] — Structural behavior of HPFRCC composite beams.
