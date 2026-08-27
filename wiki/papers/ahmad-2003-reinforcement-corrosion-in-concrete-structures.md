---
title: "Reinforcement corrosion in concrete structures, its monitoring and service life prediction: A review"
type: source_note
source: "sources/ahmad-2003-reinforcement-corrosion-in-concrete-structures,.pdf"
citation: "Ahmad, S. (2003). Reinforcement corrosion in concrete structures, its monitoring and service life prediction: A review. Cement and Concrete Composites, 25(4-5), 459-479."
date: 2026-08-23
tags: [reinforcement-corrosion, electrochemical-monitoring, half-cell-potential, linear-polarization-resistance, tuutti-model, service-life-prediction, chloride-threshold, review]
---

# Reinforcement corrosion in concrete structures, non-destructive electrochemical monitoring, and residual service life prediction models: a comprehensive review

## Summary

This monumental comprehensive review by Prof. Shamsad Ahmad of King Fahd University of Petroleum and Minerals (KFUPM), Saudi Arabia, systematically consolidates the state of knowledge on reinforcement corrosion — the dominant durability deterioration phenomenon causing premature failure of reinforced concrete (RC) structures in marine environments and deicing-salt regions — covering the formation mechanism of the electrochemical corrosion cell, the thermodynamic electromotive force ($emf$) equilibrium of the anodic (oxidation) and cathodic (reduction) half-reactions, the factors governing corrosion (critical chloride concentration, carbonation-induced pH drop, oxygen and moisture diffusion, surface crack width), non-destructive electrochemical measurement techniques (half-cell potential, linear polarization resistance LPR, alternating-current impedance EIS, galvanic sensors), and numerical residual service life prediction models based on Tuutti's two-phase model (initiation period $t_i$ + propagation period $t_p$). The paper establishes theoretical and empirical service-life evaluation frameworks that quantitatively predict passive film breakdown driven by pore-solution pH reduction (12.5 $\rightarrow$ <9.0), rebar cross-sectional loss ($A_{st}$), bond stress reduction, and the onset of cover spalling defined by the critical crack width ($w_{cr} \ge 0.3\ \text{mm}$) produced by corrosion-product expansion pressure.

## Key Contributions

1. **Thermodynamic governing equations of the reinforcement corrosion electrochemical cell and electromotive force ($emf$)**:
   - **Anodic reaction (oxidation)**: $\text{Fe} \rightarrow \text{Fe}^{2+} + 2e^-$, $E_A = -0.44 + 0.0296 \log [\text{Fe}^{2+}]\ \text{(V)}$.
   - **Cathodic reaction (reduction)**: $\text{O}_2 + 2\text{H}_2\text{O} + 4e^- \rightarrow 4\text{OH}^-$, $E_C = 1.229 + 0.0148 \log [\text{O}_2] - 0.0591\ \text{pH}\ \text{(V)}$.
   - **Total corrosion emf ($e = E_C - E_A$)**:
     $$e = 1.669 + 0.0148 \log [\text{O}_2] - 0.0591\ \text{pH} - 0.0296 \log [\text{Fe}^{2+}]$$
   - Quantified how carbonation-induced pH decrease and increased dissolved oxygen concentration exponentially accelerate the corrosion driving potential ($e$) and the corrosion current ($I_{corr}$).
2. **Analysis of the precision and limitations of electrochemical non-destructive monitoring techniques**:
   - **Half-cell potential method (ASTM C876)**: assessment of corrosion probability (above 90 % active corrosion below $-350\ \text{mV CSE}$).
   - **Linear polarization resistance (LPR: Linear Polarization Resistance)**: quantitative real-time measurement of the instantaneous corrosion rate ($\mu\text{m/year}$) via the Stern–Geary relation ($I_{corr} = B / R_p$).
   - **Electrochemical impedance spectroscopy (EIS)**: frequency-domain separation and interpretation of solution resistance ($R_s$), polarization resistance ($R_p$), and double-layer capacitance ($C_{dl}$).
3. **Numerification of two-phase service life prediction based on the Tuutti model ($T = t_i + t_p$)**:
   - **Initiation period ($t_i$)**: Fick's second-law diffusion equation ($C(x, t) = C_s [1 - \text{erf}(x / 2\sqrt{D t})]$) yields the time at which the critical chloride concentration is reached ($C_{th} = 0.05\sim 0.1\ \%\ \text{by concrete wt.}$).
   - **Propagation period ($t_p$)**: elastic–plastic thick-walled cylinder theory models the period over which expansive corrosion products ($\text{Fe(OH)}_3$, $\text{Fe}_3\text{O}_4$, expanding 2 to 6 times in volume) induce cover tensile stress exceeding the concrete tensile strength ($f_t$), producing surface longitudinal cracking ($w = 0.3\ \text{mm}$) and cover spalling.

## Methods

- **Consolidation of corrosion-governing parameters and threshold criteria**:
  - Critical chloride ion concentration ($C_{th}$): 0.15 to 0.40 wt.% of total cement weight (water-soluble chlorides 0.06 to 0.15 wt.%).
  - Corrosion-rate classification criteria: $I_{corr} < 0.1\ \mu\text{A/cm}^2$ (negligible/passive), $0.1 \sim 0.5\ \mu\text{A/cm}^2$ (low to moderate), $0.5 \sim 1.0\ \mu\text{A/cm}^2$ (moderate to high), $> 1.0\ \mu\text{A/cm}^2$ (very high risk).
- **Service life prediction modeling techniques**:
  - Fickian diffusion models combined with environmental factors (Arrhenius temperature dependence, humidity, binder chloride binding capacities $\alpha, \beta$).
  - Bazant's and Weyers' numerical models of the limiting expansion pressure of corrosion products.

## Results

### 1. Comparison of non-destructive electrochemical corrosion diagnostic techniques

| Monitoring technique | Measured quantity | Evaluation result and output information | Advantages | Field application constraints |
|---|---|---|---|---|
| **Half-cell potential (HCP)** | Potential difference ($V$ vs CSE) | Probability of active corrosion (%) | Rapid; easy wide-area mapping | Cannot yield the actual corrosion rate ($\mu\text{m/yr}$); influenced by moisture content |
| **Linear polarization resistance (LPR)** | Polarization resistance ($R_p$, $\Omega$) | Instantaneous corrosion current density ($I_{corr}$) | Direct real-time corrosion rate output | Requires IR-drop correction and guard-ring control |
| **Electrochemical impedance (EIS)** | Impedance spectrum ($Z$) | Corrosion mechanism, film resistance | In-depth mechanism interpretation | Expensive equipment; excessively long field measurement time |
| **Galvanic current meter** | Galvanic current ($I_g$) | Dissimilar-metal and depth-wise corrosion currents | Continuous monitoring via permanent embedment | Limited to embedded sensor locations; localized data |

### 2. Structural implications of residual service life prediction models
- **Importance of crack width control**: once the surface crack width exceeds 0.1 mm, the chloride ion diffusion path shortens and the initiation period ($t_i$) shrinks by more than 80 %.
- **Shielding effect of ultra-high-ductility composites (SHCC)**: applying SHCC/ECC covers that restrict crack widths below 50 µm effectively blocks chloride penetration, extending $t_i$ practically indefinitely.

- **Overall conclusion**: reinforcement corrosion is a coupled physicochemical phenomenon of electrochemical potential equilibrium and mass transport through a porous medium, and securing a 100-year durable service life for structures is established to depend above all on low-permeability matrices combined with ECC-type covers that control fine cracks below 50 µm.

## Related Notes

- [[chen-2018-ultra-high-ductility-cement-composite-curving]] — original study on SHCC flexural repair of beams with 25 % corroded-reinforcement loss.
- [[crack-width-control]] — sub-50 µm fine crack width control criteria against chloride-induced corrosion.
- [[structural-repair-and-retrofitting]] — cross-section restoration and strengthening mechanisms for corroded legacy structures.
- [[choi-2017-carbonation-detection-image-processing]] — carbonation depth measurement (Lee group).
- [[sustainability-low-carbon-binders]] — chloride binding and corrosion resistance of low-carbon blended cements.
