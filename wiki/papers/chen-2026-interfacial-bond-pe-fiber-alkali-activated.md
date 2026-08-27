---
title: "To achieve high tensile strain capacity in cementitious composites"
type: source_note
source: "sources/chen-2026-to-achieve-high-tensile-strain.pdf"
citation: "Chen, J., Basang, Z., Wang, R., Dai, N., Jiang, F., Wang, F., Xiao, J., Yu, K., & Yu, J. (2026). To achieve high tensile strain capacity in cementitious composites. Composites Part B: Engineering, 112000."
date: 2026-08-23
tags: [tensile-strain-capacity, ultra-high-ductility, debonding-and-pullout, debonding-and-rupture, fiber-bridging, statistical-dispersion, kequan-yu, theory-foundation]
---

# Micromechanical conditions and statistical-mechanics analysis for achieving ultra-high tensile strain capacities above 6 % in cementitious composites

## Summary

To identify the physical and statistical mechanisms behind why most fiber-reinforced cement composites (FRC/ECC) plateau at tensile strains of 2~4 % while only a handful of mixes exhibit ultra-high tensile strain capacity above 6 %, this recent landmark theory paper from the Tongji University team of Kequan Yu and Jiangtao Yu consolidates the interfacial bond-pullout mechanics of 11 representative commercial monofilament fibers (steel, carbon, glass, aramid, PBO, PVA, PP, UHMWPE, etc.), from the single-fiber scale up to a statistical-mechanics model of multiple cracking. The authors mathematically dichotomize fiber behavior into a frictional pullout-dominated regime (DP: Debonding & Pullout) and a fiber-rupture-dominated regime (DR: Debonding & Rupture), proving that DR fibers are confined to their own elasto-plastic elongation within the effective debonding length $L_f$, so strains beyond 2 % are mathematically unattainable. In contrast, DP fibers such as UHMWPE supply crack opening (CMOD) through frictional slip displacement across the entire embedded length, and the increase in bridging-count density per unit area ($N_f \propto 1/d_f^2$) enabled by fine fiber diameters ($d_f \le 20\ \mu\text{m}$) dramatically lowers the coefficient of variation (COV) of the bridging force across the crack plane, which quantitatively unlocks the **6~12 %** extreme strain-hardening strain capacity.

## Key Contributions

1. **Two-regime classification of single-fiber failure mechanics (DP vs DR) and mathematical proof of the tensile strain ceiling**:
   - **DP type (Debonding & Pullout: UHMWPE, PP)**: without fiber rupture, frictional pullout slip along the entire embedded length $L_f$ supplies the crack opening displacement (CMOD) $\rightarrow$ saturated multiple cracking can deliver **6~12 %** ultra-high strain capacity.
   - **DR type (Debonding & Rupture: Steel, Carbon, Glass, Aramid, PBO)**: strong interfacial adhesion causes fiber rupture $\rightarrow$ only the intrinsic elongation within the effective debonding segment ($L_f = R_u^f d_f / 4\tau$) contributes, strictly capping the theoretical strain capacity below **2.0 %**.
   - **Hybrid type (PVA)**: strong chemical bonding produces partial rupture + partial pullout $\rightarrow$ typically 2.0~4.5 % strain capacity.
2. **Mathematical correlation established between fiber diameter ($d_f$) and the statistical dispersion of multi-crack bridging forces**:
   - At equal volume fraction ($V_f = 2.0\ \%$), reducing the fiber diameter $40\ \mu\text{m} \rightarrow 15\ \mu\text{m}$ increases the number of bridging fibers per unit area $N_f$ by 7.1-fold.
   - The spatial coefficient of variation (COV) of the bridging force falls sharply in proportion to $1/\sqrt{N_f}$, blocking premature localized failure of weak sections at the source and inducing 100 % saturated multiple cracking.
3. **Quantitative critical margins of the two PSH criteria for realizing ultra-high ductility (>6 %)**:
   - Strength criterion: $\sigma_0/\sigma_{fc} \ge 2.0$ (peak bridging stress / first-cracking strength).
   - Energy criterion: $J'_b/J_{tip} \ge 3.0\sim 5.0$ (complementary bridging energy / matrix fracture energy).

## Methods

- **Micromechanics parameter database analysis of 11 fiber types (Table 2)**:
  - Fiber types: Microsteel, Hooked steel, Carbon, Basalt, Glass, POM, Aramid, PBO, PVA, PP, UHMWPE.
  - Parameters: nominal diameter ($d_f$), tensile strength ($R_u^f$), elastic modulus ($E_f$), rupture strain ($\varepsilon_u^f$), interfacial shear strength ($\tau$), effective debonding length ($L_f$).
- **Statistical-mechanics numerical simulation model of multiple cracking**:
  - Bi-linear and slip-softening single-fiber pullout constitutive relations.
  - Gaussian/Weibull probability distribution functions incorporating fiber embedment length, snubbing effect, and diameter deviation.
  - Monte Carlo integration of multi-section bridging forces and analysis of the composite tensile stress-strain response.

## Results

### 1. Comparison of micromechanics parameters and tensile strain ceilings by fiber type (Table 2)

| Fiber type | Diameter ($d_f$, µm) | Tensile strength (MPa) | Elastic modulus (GPa) | Rupture strain (%) | Interfacial strength ($\tau$, MPa) | Failure mode | Measured/ceiling composite tensile strain |
|---|---|---|---|---|---|---|---|
| **Microsteel** | 200 | 2500 | 200 | 2.5 % | 4.0 | DR | 0.3 ~ 0.8 % |
| **Carbon** | 7 | 4000 | 230 | 1.7 % | 2.5 | DR | 0.1 ~ 0.5 % |
| **Basalt** | 13 | 2500 | 85 | 2.8 % | 1.8 | DR | 0.2 ~ 0.6 % |
| **Aramid** | 12 | 3400 | 73 | 4.6 % | 3.8 | DR | 0.8 ~ 1.6 % |
| **PBO** | 13 | 5800 | 180 | 3.5 % | 4.4 | DR | 1.0 ~ 1.8 % |
| **PVA (REC15)** | 40 | 1600 | 40 | 6.0 % | 2.5 | Hybrid | 2.0 ~ 4.5 % |
| **PP** | 20 | 600 | 6 | 15.0 % | 1.0 | DP | 2.0 ~ 5.0 % |
| **UHMWPE** | **15 ~ 25** | **2800 ~ 3200** | **88 ~ 120** | **3.0 %** | **1.5 ~ 2.5** | **DP** | **6.0 ~ 12.0 % (ultra-high ductility achieved)** |

### 2. Correlation between bridging fiber diameter and statistical multiple-cracking saturation
- $40\ \mu\text{m}$ diameter PVA fiber: at $V_f = 2\ \%$, about 1,600 fibers/$cm^2$ per section with a bridging-force COV of about 8~12 %; premature rupture localization sets in at 3~4 % strain.
- $16\ \mu\text{m}$ diameter PE fiber: at $V_f = 2\ \%$, about **10,000 fibers/$cm^2$** per section with the bridging-force COV collapsing to **below 3 %** $\rightarrow$ induces more than 80 saturation-limit multiple cracks and achieves 7~10 % ultra-high strain capacity.

- **Overall conclusion**: Establishes mathematically and micromechanically that attaining extreme tensile strains above 6 % requires (1) selecting a high-strength fiber governed entirely by frictional slip with no interfacial rupture (UHMWPE), (2) securing high bridging-count density through fine-diameter design at 20 µm or below, and (3) a PSH strength margin of $\sigma_0/\sigma_{fc} \ge 2.0$.

## Related Notes

- [[pseudo-strain-hardening-criteria]] — original sources of the PSH steady-state cracking and energy criteria (Victor Li).
- [[choi-2016-ultra-high-ductile-aas-pe-composite]] — demonstration of a 7.50 % ultra-ductile AAS-PE composite (Bang Yeon Lee group).
- [[choi-2020-high-ductility-high-strength-pe-composite]] — demonstration of a 7.90 % ultra-ductile 80 MPa UHDCC (Bang Yeon Lee group).
- [[strain-hardening-mechanism]] — micromechanics theory framework of the PSH strength and energy criteria.
- [[multiple-cracking-behavior]] — summation of crack opening (CMOD) and the saturated multiple-cracking mechanism.
