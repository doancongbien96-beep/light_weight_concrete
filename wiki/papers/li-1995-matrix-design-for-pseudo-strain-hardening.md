---
title: "Matrix design for pseudo-strain-hardening fibre reinforced cementitious composites"
type: source_note
source: "sources/li-1995-matrix-design-for-pseudo-strain-hardening-fibre.pdf"
citation: "Li, V. C., Mishra, D. K., & Wu, H.-C. (1995). Matrix design for pseudo-strain-hardening fibre reinforced cementitious composites. Materials and Structures, 28(10), 586-595."
date: 2026-08-24
tags: [pseudo-strain-hardening, psh, matrix-design, fracture-toughness, jtip, sand-cement-ratio, spectra-pe-fiber, victor-li, materials-and-structures, landmark-paper]
---

# Matrix Design Principles for Micromechanics-Based Strain-Hardening (PSH) Cement Composites: Fracture Toughness Upper Bound ($J_{tip} \le 0.010\ \text{kJ/m}^2$) and Sand/Cement Ratio (S/C) Optimal Control Guidance

## Summary

To reliably achieve pseudo strain-hardening (PSH) and multiple fine cracking under practical mix conditions of short fiber content $V_f \le 2.0\ \text{vol.}\%$, this work moved beyond the existing focus on fiber and interfacial variables to theoretically formalize **the quantitative influence of matrix fracture toughness ($K_m$, $J_{tip}$), elastic modulus ($E_m$), tensile strength ($f_{ct}$), and sand content ratio (Sand/Cement ratio) on composite tensile ductility**. Through fracture toughness measurement of seven matrices via compact tension (CT) testing and uniaxial direct tension testing of Spectra PE fiber composites, the joint research team of **University of Michigan endowed professor Victor C. Li, Dhanada K. Mishra, and Hwai-Chung Wu** demonstrated **the $J_{tip} \le 0.010\ \text{kJ/m}^2$ upper bound and the attainment of tensile strains of $5.6\sim 6.5\%$** — an immortal top landmark origin paper of Materials and Structures (RILEM), 1995.

## Key Contributions

1. **First establishment of a critical upper bound on matrix fracture toughness ($J_{tip}$, $\le 0.010\ \text{kJ/m}^2$) for achieving PSH**:
   - Quantitatively presented the matrix toughness upper bound required to satisfy the steady-state crack propagation energy criterion that the crack-tip fracture toughness $J_{tip} = K_m^2 / E_m$ must remain below the fiber bridging complementary energy $J_b'$ ($J_b' / J_{tip} > 1$).
2. **Clarified the trade-off mechanism by which aggregate content (S/C ratio) and maximum aggregate size affect composite ductility**:
   - Demonstrated that increasing the sand content ratio raises matrix elastic modulus ($E_m$) and strength, but crack-tip toughness ($K_m$) surges from $0.31 \rightarrow 0.71\ \text{MPa}\sqrt{\text{m}}$, undermining strain hardening.
3. **Presented three matrix design guidelines for PSH cement composites**:
   - ① Design to reduce $J_{tip}$ (exclusion of coarse aggregate and use of fine silica sand).
   - ② Secure a margin between matrix tensile strength ($f_{ct}$) and the peak bridging stress ($\sigma_0$) ($\sigma_0 > f_{ct}$).
   - ③ Secure an appropriate initial defect size ($c_0$) distribution.
4. **Achieved direct tensile strains of $5.6\sim 6.5\%$ in Spectra PE fiber composites**:
   - Realized ultra-high ductility above 5 % at practical fiber content ($V_f = 2.0\%$) using a theoretically optimized low-toughness mortar matrix.

## Methods

- **Micromechanics PSH governing equations (Section 2 & Figs. 1~2)**:
  - Crack-tip energy: $J_{tip} \approx \frac{K_m^2}{E_m}$.
  - Bridging complementary energy: $J_b' = \sigma_0 \delta_0 - \int_0^{\delta_0} \sigma(\delta) d\delta$.
  - Energy condition: $J_{tip} < J_b' = \frac{1}{24} g V_f \tau_0 \frac{L_f^2}{d_f}$.
  - Strength condition: $f_{ct} \le \sigma_0 = \frac{1}{6} g V_f \tau_0 \frac{L_f}{d_f}$.
- **Matrix fracture toughness measurement tests (Section 3 & Fig. 3)**:
  - Specimen geometry: compact tension (CT) specimens ($127 \times 152 \times 12.7\ \text{mm}$, per ASTM E399).
  - Seven matrix mixes: W/C = 0.32 ~ 0.45, S/C = 0.0 ~ 2.0.
- **Composite tension tests (Section 3.3)**:
  - Fiber: Spectra PE ($V_f = 2.0\ \text{vol.}\%$, diameter $38\ \mu\text{m}$, length 12.7 mm, tensile strength 2.6 GPa, elastic modulus 117 GPa).
  - Dogbone-shaped plate specimens ($152 \times 76.2 \times 12.7\ \text{mm}$), displacement-controlled tension.

## Results

### 1. Quantitative comparison table of fracture toughness per matrix mix and uniaxial direct tension performance of composites (Tables 1~3 & Figs. 4~11)

| Mix ID | W/C | S/C (aggregate ratio) | Compressive strength ($f_c$, MPa) | Matrix toughness ($K_m$, $\text{MPa}\sqrt{\text{m}}$) | Crack-tip toughness ($J_{tip}$, $\text{kJ/m}^2$) | Composite tensile strength ($\sigma_{tu}$, MPa) | Composite tensile strain ($\varepsilon_u$, %) | Failure mode |
|---|---|---|---|---|---|---|---|---|
| **MR#1 (paste)** | 0.45 | 0.0 | 45.0 MPa | **$0.33\ \text{MPa}\sqrt{\text{m}}$** | **$0.0047\ \text{kJ/m}^2$** | - | - | Low-toughness matrix |
| **MR#2 (mortar)** | 0.45 | 0.5 | 61.3 MPa | **$0.31\ \text{MPa}\sqrt{\text{m}}$** | **$0.0048\ \text{kJ/m}^2$** | - | - | Optimal matrix |
| **MR#4 (high aggregate)** | 0.45 | 1.5 | 82.5 MPa | **$0.57\ \text{MPa}\sqrt{\text{m}}$** | **$0.0108\ \text{kJ/m}^2$ (over limit)** | - | - | High-toughness risk |
| **MR#6 (excess aggregate)** | 0.45 | 2.0 | 90.6 MPa | **$0.71\ \text{MPa}\sqrt{\text{m}}$** | **$0.0168\ \text{kJ/m}^2$ (dangerous)** | - | - | PSH impossible |
| **Mix I (paste ECC)**| 0.32 | 0.0 | 65.6 MPa | 0.35 | 0.0051 | **$4.8 \pm 0.3\ \text{MPa}$** | **$5.6 \pm 0.4\%$** | **Saturated multiple cracking** |
| **Mix IIIa (mortar ECC)**| 0.35 | **0.5 (optimal)**| **$55.8 \pm 2.0$** | **0.38** | **$0.0055\ \text{kJ/m}^2$** | **$4.6 \pm 0.2\ \text{MPa}$** | **$6.5 \pm 0.5\%$ (highest)**| **Fully saturated PSH** |

### 2. Analysis of matrix fracture toughness and the PSH energy margin
- **The dilemma between aggregate addition and crack-tip toughness**: adding aggregates induces crack deflection and aggregate bridging in the matrix, increasing $K_m$ by more than a factor of two. Once $K_m$ exceeds $0.6\ \text{MPa}\sqrt{\text{m}}$, $J_{tip} > J_b'$ holds and the crack runs brittlely before the fibers can even develop their bridging stress.
- **The optimal region of S/C = 0.5~1.0**: using fine silica sand within the range S/C $\le 1.0$ suppresses $J_{tip}$ to $\le 0.006\ \text{kJ/m}^2$, securing a sufficient energy margin of $J_b'/J_{tip} > 2.0$ and realizing ultra-high ductility reaching $6.5\%$.

- **Overall conclusion**: This paper is the top immortal landmark origin paper of the materials engineering and fracture mechanics fields, in which professor Victor C. Li identified for the first time that the key governing the ductile strain-hardening of ECC lies not only in the fibers themselves but in the fracture toughness of the matrix ($J_{tip} \le 0.010\ \text{kJ/m}^2$), and presented quantitative design guidelines for aggregate proportioning.

## Related Notes

- [[li-1991-micromechanical-model-tension-softening-bridging]] — Victor Li: origin paper of the fiber bridging tension-softening micromechanics model.
- [[kanda-2006-saturated-psh-design-criteria-ecc]] — Kanda & Li: landmark on saturated PSH design criteria.
- [[strain-hardening-mechanism]] — micromechanics of ECC strain-hardening and the $J_b'/J_{tip}$ energy criterion.
- [[lee-2010-micromechanics-fiber-bridging-distribution-model]] — Prof. Bang Yeon Lee: origin paper of the orientation-coupled fiber bridging constitutive model.
