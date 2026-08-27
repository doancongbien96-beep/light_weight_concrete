---
title: "A review of procedures for the analysis and design of concrete structures to resist missile impact effects"
type: source_note
source: "sources/kennedy-1976-a-review-of-procedures-for.pdf"
citation: "Kennedy, R. P. (1976). A review of procedures for the analysis and design of concrete structures to resist missile impact effects. Nuclear Engineering and Design, 37(2), 183-203."
date: 2026-08-24
tags: [missile-impact, concrete-containment, penetration-depth, scabbing-thickness, perforation-limit, modified-ndrc-formula, ace-formula, nuclear-engineering-design, structural-impact-dynamics, theory-foundation]
---

# Analysis and Design of Concrete Nuclear Containment Structures for Rigid Missile Impacts: Local Damage Mechanisms (Spalling, Penetration, Scabbing, Perforation) and Dynamic Response Review

## Summary

To ensure that concrete containment structures, nuclear fuel storage facilities, and protective barriers safely resist high-velocity external missiles (tornado-generated pipes, aircraft crash debris) and internal accidental missiles (turbine blade fragments, high-pressure pipe whips at velocities of $30\sim 450\ \text{m/s}$), this seminal review by Dr. R. P. Kennedy at Holmes & Narver synthesizes the state of the art in missile impact engineering. The paper quantifies the four primary local damage mechanisms in concrete targets—**front-face spalling, penetration depth ($x$), rear-face scabbing ($s$), and perforation ($e$)**. The author systematically compares empirical predictive formulas (Modified Petry, ACE, Modified NDRC, and BRL), establishes design thickness criteria against scabbing ($s/d = 2.12 + 1.36(x/d)$) and perforation ($e/d = 1.32 + 1.24(x/d)$), and details **single-degree-of-freedom (SDOF) elastoplastic energy balance procedures for overall structural dynamic response**, establishing the global benchmark for nuclear safety design.

## Key Contributions

1. **Standardized definition of 4 local damage modes in concrete missile impact**:
   - Delineated the physical progression from front spall crater formation, cylindrical penetration cavity growth, rear tensile wave reflection scabbing, to complete perforation.
2. **Standardization of the Modified NDRC formula for penetration depth ($x$)**:
   - Validated $x/d = 2\sqrt{G}$ (for $G \le 1.0$) and $x/d = 1 + G$ (for $G > 1.0$), capturing missile mass, nose shape factor ($N$), velocity ($V$), and concrete compressive strength ($f_c'$) within a 10 % error margin.
3. **Formulation of slab thickness design criteria for perforation ($e$) and scabbing ($s$) limits**:
   - Established $e/d = 1.32 + 1.24(x/d)$ and $s/d = 2.12 + 1.36(x/d)$ to set required structural barrier thicknesses.
4. **Establishment of SDOF elastoplastic energy balance dynamic analysis**:
   - Balanced kinetic missile energy against internal flexural strain energy ($U_{strain} = R_m (x_m - 0.5 x_e)$), enforcing ductility ratio limits ($\mu \le 10$).

## Methods

- **Impact parameters and governing relationships (Section 2 & Fig. 1)**:
  - Missile characteristics: Mass $M$, diameter $d$, nose shape factor $N$ (flat $N=0.72$, blunt/hemispherical $N=0.84$, sharp/ogive $N=1.0\sim 1.14$), impact velocity $V_0$ ($30\sim 450\ \text{m/s}$).
  - Target concrete: Compressive strength $f_c'$ (15~60 MPa), density $\rho$, thickness $t$.
  - Modified NDRC penetration parameter:
    $$G = 180 \times 10^{-6} \frac{N M V_0^{1.8}}{d^{2.8} \sqrt{f_c'}}$$
- **Thickness formulations for local damage prevention (Section 2.2)**:
  - Penetration depth: $x/d = 2\sqrt{G}$ ($G \le 1.0$), $x/d = 1 + G$ ($G > 1.0$).
  - Perforation limit: $e/d = 1.32 + 1.24(x/d)$ ($3 \le e/d \le 18$).
  - Scabbing limit: $s/d = 2.12 + 1.36(x/d)$ ($3 \le s/d \le 18$).
- **Overall dynamic response and energy balance (Section 3)**:
  - Forcing function: $F(t) = \frac{M V_0}{t_d} \left(1 - \frac{t}{t_d}\right)$ or Riera mass-deceleration force history.
  - Ductility ratio limit: $\mu = x_m / x_e \le 10.0$.

## Results

### 1. Comparison of empirical missile impact formulas for penetration, perforation, and scabbing (Tables 1–3 & Figs. 2–6)

| Formula Name | Developing Institution | Nose Factor ($N$) Included | Penetration Prediction ($x/d$) | Perforation Thickness ($e/d$) | Scabbing Thickness ($s/d$) | Evaluation & Reliability |
|---|---|---|---|---|---|---|
| **Modified NDRC** | **National Defense Research Comm.** | **Explicitly included ($0.72\sim 1.14$)** | **Most accurate (error < 8 %)** | **$1.32 + 1.24(x/d)$** | **$2.12 + 1.36(x/d)$** | **Global nuclear standard** |
| **ACE Formula** | US Army Corps of Engineers (1946) | Not included | Adequate at medium velocities | $1.32 + 1.24(x/d)$ | $2.12 + 1.36(x/d)$ | Conservative at low velocities |
| **Modified Petry** | US Navy / Civil (1910) | Not included | Underestimates low-velocity cases | $e = 2.0 x$ | $s = 2.2 x$ | Unconservative (deprecated) |
| **BRL Formula** | Ballistic Research Lab | Simplified density basis | Good for high-velocity ballistic | $e/d \approx 1.5 (x/d)$ | Not defined | Simplified military use |

### 2. Physical mechanics of stress wave reflection and scabbing
- **Stress wave reflection**: Compressive shockwaves ($\sigma_c$) reflect from the free rear surface as tensile waves ($\sigma_t$). When tensile reflections exceed the dynamic tensile strength of concrete, rear-face concrete fragments eject at high velocity (scabbing).
- **Rear scab steel plate reinforcement**: Anchoring a $6\sim 12\ \text{mm}$ steel plate to the rear face completely eliminates scabbing ejecta (100 %), reducing required barrier thickness from scabbing thickness ($s$) to perforation thickness ($e$) by approximately 30 %.

- **Overall conclusion**: This landmark review formulated the mechanics of penetration, spalling, scabbing, and perforation for rigid missile impacts on concrete, establishing the Modified NDRC formula and SDOF design as the enduring global standards for nuclear safety.

## Related Notes

- [[impact-and-blast-resistance-frcc]] — Impact and blast resistance mechanisms in fiber-reinforced composites.
- [[chun-2024-rc-beams-impact-resistance-hpfrcc]] — HPFRCC retrofitting of RC beams under impact loading.
- [[kang-2015-wire-woven-cellular-metals-review]] — Blast and impact energy absorption in wire-woven metal trusses.
- [[high-strength-strain-hardening-composites]] — High-performance composites for extreme impact resistance.
