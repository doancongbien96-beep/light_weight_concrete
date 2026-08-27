---
title: "Fiber Optic Smart Structures"
type: source_note
source: "sources/Udd-1996-Fiber optic smart structures.pdf"
citation: "Udd, E. (1996). Fiber optic smart structures. Proceedings of the IEEE, 84(1), 60-73."
date: 2026-08-23
tags: [fiber-optic-sensors, smart-structures, shm, fbg, fabry-perot, interferometry, distributed-sensing, eric-udd, invited-paper, theory-foundation]
---
# A Review of Sensing Mechanisms, Wavelength Multiplexing, and Structural Health Monitoring (SHM) of Fiber Optic Smart Structures

## Summary

An immortal IEEE invited landmark review by Dr. Eric Udd (Blue Road Research, USA) that comprehensively covers the theoretical operating principles and system architecture of **smart structure** technology based on **fiber optic sensors**, developed to self-diagnose internal strain, temperature, pressure, acoustic emission, and structural damage in real time over the life cycle of aerospace vehicles, smart materials, and civil infrastructure (bridges, dams, tunnels, nuclear containment buildings). Building on the physical advantages of optical fiber, namely complete immunity to electromagnetic interference (EMI), compact light weight, extreme durability, and direct embedment within materials (embedded sensing), the paper systematizes the governing equations of intensity-based, phase-interferometric (Fabry-Perot EFPI/IFPI, Sagnac, Mach-Zehnder), spectrally wavelength-modulated (fiber Bragg grating: FBG), and Brillouin/Raman distributed fiber optic sensing (distributed BOTDA/OTDR) technologies, and established the standard SHM paradigm that integrates thousands of sensors into a single optical fiber network through wavelength-division multiplexing (WDM) and time-division multiplexing (TDM).

## Key Contributions

1. **Physical theory systematization of the four major sensing mechanisms of fiber optic smart structures**:
   - **Intensity-based**: simple displacement/vibration detection using microbending of the optical fiber and numerical aperture (NA) alignment loss.
   - **Interferometric (Fabry-Perot, Sagnac, Mach-Zehnder)**: ultra-high-sensitivity dynamic strain measurement at the $\text{sub-}\mu\varepsilon$ level using the optical phase difference ($\Delta\phi = \frac{2\pi n}{\lambda} \Delta L$).
   - **Wavelength-modulated (spectrally based FBG)**: absolute strain and temperature measurement using the Bragg wavelength shift ($\Delta\lambda_B / \lambda_B = (1-p_e)\varepsilon + (\alpha_\Lambda + \xi)\Delta T$).
   - **Distributed sensing (BOTDR/BOTDA)**: uses the optical fiber itself as a continuous sensor to map one-dimensional strain/temperature profiles continuously over structures tens of kilometers long.
2. **Realization of three-dimensional distributed instrumentation networks inside smart structures through multiplexing**:
   - By fusing wavelength-division multiplexing (WDM), time-division multiplexing (TDM), and spatial-division multiplexing (SDM), several dozen to hundreds of FBG sensor nodes are connected in series along a single optical cable line, enabling precise position tracking of local cracks and damage.
3. **Demonstration of embedment reliability in composites and civil concrete and of interface transfer efficiency**:
   - Established packaging technology that secures perfect interface integrity, inducing no structural defects in the host material when embedded inside glass/carbon fiber composites and cement matrices, with strain transfer error below 1 %.

## Methods

- **Optical principles and configuration schemes by sensor type (Figures 1-12)**:
  - **FBG sensor (fiber Bragg grating)**:
    - Periodic modulation of the core refractive index ($\Lambda$); Bragg center wavelength $\lambda_B = 2 n_{eff} \Lambda$.
    - Strain sensitivity: approximately $1.2\ \text{pm}/\mu\varepsilon$ in the $1550\ \text{nm}$ band; temperature sensitivity approximately $10\ \text{pm}/^\circ\text{C}$.
  - **Fabry-Perot interferometer (extrinsic Fabry-Perot interferometer: EFPI)**:
    - Resonant etalon gap ($s$) between two cross-sections inside a capillary tube; phase change $\Delta\phi = \frac{4\pi}{\lambda}\Delta s$.
  - **Sagnac interferometer**:
    - Measures the non-reciprocal phase difference of counter-propagating light waves to detect high-frequency acoustic emission (AE) and impact locations.
  - **Distributed Brillouin scattering (Brillouin optical time domain analysis)**:
    - Distributed measurement exploiting the frequency shift ($\nu_B \approx 11\ \text{GHz}$) caused by inelastic scattering with acoustic phonons ($1\ \text{m}$ spatial resolution, $30\ \text{km}$ measurement distance).

## Results

### 1. Comparison of performance and application fields across fiber optic smart sensing system types

| Sensor type | Physical modulation scheme | Measured parameters | Spatial resolution / range | Multiplexing capacity (single channel) | Primary structural applications |
|---|---|---|---|---|---|
| **FBG (Bragg grating)** | Wavelength modulation (spectral $\lambda_B$) | Static/dynamic strain, temperature | Local point sensor ($1\sim 10\ \text{mm}$) | **50-100 nodes in series via WDM** | Bridge girders, wind turbine blades, aircraft |
| **EFPI (Fabry-Perot)** | Phase interference | Micro-displacement, high-temperature strain | Local point sensor ($1\sim 20\ \text{mm}$) | 5-10 via TDM | Reactor piping, ultra-high-temperature combustion chambers |
| **Sagnac / M-Z** | Optical path phase-difference interference | Acoustic emission (AE), vibration frequency | Distributed/integral line sensor | Single loop | Impact damage localization, intrusion detection |
| **BOTDA (Brillouin)** | Inelastic backscatter frequency | Continuous strain and temperature profiles | $0.5\sim 1.0\ \text{m}$ resolution / $50\ \text{km}$ | **Continuous distribution (tens of thousands of points)** | Dam embankment settlement, long tunnels, pipelines |

### 2. Interpretation of the self-diagnosis mechanism of smart composite materials
- **Electromagnetic interference immunity**: guarantees 100 % complete data reliability without signal distortion or noise even in thunderstorm, high-voltage transmission line, and electromagnetic pulse (EMP) environments.
- **Simultaneous separated measurement of multiple physical quantities**: establishes algorithms that completely separate and compensate thermal expansion due to temperature ($\Delta T$) from mechanical strain ($\varepsilon$) by arranging FBGs of two or more wavelength bands in series.

- **Overall conclusion**: this paper by Dr. Eric Udd is a monumental cornerstone work that went beyond a mere measuring instrument to establish worldwide, for the first time, the concept of the 'smart structure' in which the structure itself detects its own condition as if endowed with a nervous system, and led the engineering commercialization of fiber optic SHM technology.

## Related Notes

- [[di-2014-fbg-sensor-embedded-strain-monitoring]] — Original source on embedded FBG fiber optic sensors and strain monitoring in composites.
- [[ndt-and-shm-of-cementitious]] — Non-destructive diagnosis and smart sensing framework for cementitious composites.
- [[impact-and-blast-resistance-frcc]] — Dynamic impact and strain measurement using optical fiber sensors.
- [[crack-width-control]] — Fine crack diagnosis and monitoring via smart sensors.

- [[gusarov-2008-fbg-fiber-coating-radiation-sensitivity]] — Original source on radiation swelling of FBG polymer coatings and radiation tolerance.
