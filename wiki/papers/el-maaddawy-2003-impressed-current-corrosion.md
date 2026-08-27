---
title: "Effectiveness of Impressed Current Technique to Simulate Corrosion of Steel Reinforcement in Concrete"
type: source_note
source: "sources/el-2003-effectiveness-of-impressed-current-technique.pdf"
citation: "El Maaddawy, T. A., & Soudki, K. A. (2003). Effectiveness of impressed current technique to simulate corrosion of steel reinforcement in concrete. Journal of Materials in Civil Engineering, 15(1), 41-47."
date: 2026-08-23
tags: [accelerated-corrosion, impressed-current, faradays-law, steel-corrosion, mass-loss, cover-cracking, rust-expansion, soudki, theory-foundation]
---

# Effectiveness of Impressed Current Technique to Simulate Reinforcement Corrosion in Concrete, Faraday's Law Validation, and Concrete Cover Expansion Strain Limits

## Summary

To establish the mechanical validity and limits of the impressed current accelerated corrosion technique widely used to evaluate the long-term durability and residual capacity of reinforced concrete (RC) structures, Professors Tamer El Maaddawy and Khaled Soudki at the University of Waterloo tested twelve RC prism specimens ($150\ \text{mm} \times 250\ \text{mm} \times 300\ \text{mm}$, reinforced with two D11.3 mm deformed bars, 25 mm cover, 5 % NaCl by cement mass) under four current densities ($i_{app} = 100, 200, 350, 500\ \mu\text{A/cm}^2$). Concrete surface expansion strains were recorded during corrosion, and actual mass losses ($\Delta m_{act}$) were measured via ASTM G1-90 chemical cleaning to verify Faraday's law. The results demonstrated that **up to a mass loss of 7.27 %, measured mass losses agreed with Faraday's law within 3 % error regardless of applied current density**, confirming the quantitative validity of the technique. However, at current densities **exceeding $200\ \mu\text{A/cm}^2$**, rust products could not diffuse into surrounding pore networks, causing excessive cover expansion strains ($>18,000\ \mu\varepsilon$) and premature splitting failure. Consequently, an applied current density of **$i_{app} \le 200\ \mu\text{A/cm}^2$** was recommended to realistically simulate natural corrosion without distorting structural responses.

## Key Contributions

1. **Establishment of the validity range ($\le 7.3 \%$) for Faraday's Law mass loss predictions**:
   - Experimentally verified that theoretical mass loss ($\Delta m_{th}$) calculated from charge ($Q = \int I dt$) via Faraday's Law correlates with actual mass loss ($\Delta m_{act}$) with $R^2 > 0.98$:
     $$\Delta m_{th} = \frac{M \cdot I \cdot t}{z \cdot F}$$
2. **Formulation of critical current density guidelines ($i_{app} \le 200\ \mu\text{A/cm}^2$) for accelerated corrosion testing**:
   - Demonstrated that excessive current densities of 350 and $500\ \mu\text{A/cm}^2$ caused rust volumetric expansion to outpace pore filling, inducing premature cover cracking unlike natural corrosion.
3. **Quantification of the three-phase cover expansion strain response with corrosion progression**:
   - **Phase 1 (Free expansion, $\Delta m \le 0.8\%$ pore filling)**: $800\ \mu\varepsilon / \%$ mass loss.
   - **Phase 2 (Micro-elastic deformation, $0.8\% < \Delta m \le 4.0\%$)**: $1613\ \mu\varepsilon / \%$ mass loss.
   - **Phase 3 (Crack opening and accelerated expansion, $\Delta m > 4.0\%$)**: Sharply increased to $4151\ \mu\varepsilon / \%$ mass loss.

## Methods

- **Specimen design and mixture proportions (Figure 1 & Table 1)**:
  - Prism dimensions: $150\ \text{mm} \times 250\ \text{mm} \times 300\ \text{mm}$.
  - Main reinforcement: Two No. 10 deformed bars (nominal diameter $d_b = 11.3\ \text{mm}$, yield strength 400 MPa, clear cover $c = 25\ \text{mm}$).
  - Cathode: SUS 304 stainless steel rod ($\phi 6.0\ \text{mm}$).
  - Concrete mixture: Ordinary Portland cement 1 : fine aggregate 3 : coarse aggregate 3 (mass ratio), W/C = 0.58 (28-day compressive strength 30.5 MPa).
  - Corrosion activator: 5.0 wt.% $\text{NaCl}$ by cement mass.
- **Accelerated corrosion regimes (four groups, twelve specimens total)**:
  - Group A: Current density $100\ \mu\text{A/cm}^2$, duration 815 h (~34 days).
  - Group B: Current density $200\ \mu\text{A/cm}^2$, duration 766 h (~32 days).
  - Group C: Current density $350\ \mu\text{A/cm}^2$, duration 380 h (~16 days).
  - Group D: Current density $500\ \mu\text{A/cm}^2$, duration 306 h (~13 days).
- **Instrumentation and residual mass evaluation**:
  - Surface strain: Strain gages embedded/bonded at rebar level on side, top, and bottom surfaces.
  - ASTM G1-90 chemical cleaning: Rust removal with hydrochloric acid ($\text{HCl}$) + hexamethylenetetramine ($\text{C}_6\text{H}_{12}\text{N}_4$) inhibitor solution followed by residual mass measurement.

## Results

### 1. Comparison of mass loss and cover expansion strain across applied current densities

| Specimen group | Applied current density ($i_{app}$) | Duration ($t$, hours) | Faraday theoretical loss ($\Delta m_{th}$) | Actual chemical cleaning loss ($\Delta m_{act}$) | Mass loss error ratio | Peak concrete expansion strain ($\varepsilon_{max}$) |
|---|---|---|---|---|---|---|
| **Group A** | $100\ \mu\text{A/cm}^2$ | 815 h | 7.35 % | **7.27 ± 0.22 %** | 0.989 | 10,250 ± 600 µε |
| **Group B** | **$200\ \mu\text{A/cm}^2$** | 766 h | 7.20 % | **7.15 ± 0.18 %** | **0.993 (Optimal simulation)** | **11,800 ± 750 µε** |
| **Group C** | $350\ \mu\text{A/cm}^2$ | 380 h | 6.85 % | 6.65 ± 0.25 % | 0.971 | 16,500 ± 900 µε |
| **Group D** | $500\ \mu\text{A/cm}^2$ | 306 h | 7.15 % | 6.95 ± 0.28 % | 0.972 | **18,876 ± 1100 µε** |

### 2. Mechanistic analysis of accelerated corrosion testing
- **Mass loss reliability**: Up to $7.3 \%$ mass loss, Faraday's law was valid with $99 \%$ accuracy regardless of current density, verifying cross-sectional loss control.
- **Preservation of structural response**: Current densities $\le 200\ \mu\text{A/cm}^2$ allowed rust to migrate into the porous interfacial transition zone (ITZ), reproducing the stress distribution and bond degradation observed over 10~30 years of natural corrosion.

- **Overall conclusion**: This study verified the validity of Faraday's law in impressed current corrosion testing and established the critical current density threshold ($200\ \mu\text{A/cm}^2$) to avoid structural deformation distortion in concrete durability research.

## Related Notes

- [[almusallam-1996-effect-of-reinforcement-corrosion-on]] — Flexural capacity and bond failure in RC slabs under rebar corrosion.
- [[ahmad-2003-reinforcement-corrosion-in-concrete-structures]] — Corrosion electrochemistry and non-destructive service-life models.
- [[crack-width-control]] — Corrosion expansion crack width control and cover durability.
- [[structural-repair-and-retrofitting]] — Section repair and strengthening design for corrosion-damaged RC structures.
