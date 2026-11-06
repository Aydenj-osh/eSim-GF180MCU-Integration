# GF180MCU Open PDK Integration & Two-Stage CMOS Op-Amp for eSim 2.6

**FOSSEE eSim Autumn Fellowship 2026 — IIT Bombay**  
* **Intern:** Ayden Joshua M (3rd Year B.Tech ECE, Vellore Institute of Technology)  
* **Mentors:** Mr. Sumanto Kar, Sri. Varad Patil, Ms. Shanthi Priya K  
* **Task:** Integration with PDKs: IHP and GlobalFoundries (GF180MCU) Process Nodes (EE Tasks)  

---

## 1. Project Overview

This repository introduces the integration pipeline for the **GlobalFoundries GF180MCU (0.18µm / 180nm CMOS)** Open-Source Process Design Kit into **eSim 2.6** (developed by FOSSEE, IIT Bombay). 

Prior to this work, GF180MCU had 0% integration in eSim. This project establishes:
1. **KiCad Symbol Library (`eSim_GF180.kicad_sym`):** Standard 4-pin MOSFET primitives (`nfet_03v3`, `pfet_03v3`, plus complete set of 22 foundry devices) mapped to the eSim spice netlister.
2. **BSIM3v3 Compact Model Deck (`gf180mcu.lib`):** Level 8 BSIM3v3 SPICE models avoiding Verilog-A compilation dependencies in Windows Ngspice.
3. **Reference Benchmark Circuit (Two-Stage CMOS Op-Amp):** A complete, fully connected analog IC design with active current-mirror loads and Miller frequency compensation.
4. **Simulation & Characterization Suite:** Native Ngspice simulation waveforms for open-loop frequency response (Gain & Phase) and closed-loop buffer transient step response.

---

## 2. Repository Structure

```
├── circuits/
│   └── GF180_OpAmp/                 # Complete eSim 2.6 Project
│       ├── GF180_OpAmp.kicad_sch    # Fully wired schematic file
│       ├── GF180_OpAmp.proj         # eSim project configuration
│       ├── GF180_OpAmp.cir          # AC frequency response netlist
│       ├── gf180mcu.lib             # Bundled GF180MCU BSIM3v3 models
│       └── run_interactive_simulation.bat # 1-click interactive Ngspice runner
├── library/
│   ├── kicadLibrary/eSim-symbols/
│   │   └── eSim_GF180.kicad_sym     # KiCad 8/9 symbol definitions (22 devices)
│   └── gf180_fd_pr/models/
│       └── gf180mcu.lib             # Foundry SPICE model deck
├── plots/
│   ├── GF180_OpAmp_Schematic.png    # High-resolution schematic export
│   ├── gf180_opamp_ac_gain.png      # Ngspice Open-Loop AC Gain (dB)
│   ├── gf180_opamp_ac_phase.png     # Ngspice Phase Response (degrees)
│   ├── gf180_opamp_transient.png    # Ngspice Transient Step Response
│   ├── gf180_inverter_transient.png # Ngspice Inverter Transient Waveform
│   └── gf180_inverter_dc_vtc.png    # Ngspice DC Voltage Transfer Characteristic
└── GF180_PDK_Integration_AydenJoshua.pptx  # 4-slide evaluation presentation
```

---

## 3. Benchmark Circuit Specifications & Results

| Parameter | Measured Specification | Simulation Condition |
| :--- | :--- | :--- |
| **Open-Loop DC Gain ($A_{v0}$)** | **35.93 dB** (~63x amplification) | Differential AC sweep |
| **3-dB Cutoff Frequency ($f_{-3\text{dB}}$)** | **465.4 kHz** | Open-loop AC |
| **Unity Gain Bandwidth ($\text{UGBW}$)** | **24.08 MHz** | $C_{\text{load}} = 10\text{ pF}$ |
| **Phase Margin ($\text{PM}$)** | **$>65^\circ$** (Unconditionally stable) | Miller compensated ($R_z=1\text{k}\Omega, C_c=1.2\text{pF}$) |
| **Buffer Step Rise Time ($t_r$)** | **6.5 ns** | Unity-gain configuration ($1.2\text{V} \to 1.8\text{V}$) |
| **Slew Rate ($\text{SR}$)** | **~74 V/µs** | Large-signal transient step |

---

## 4. How to Run Interactive Simulation in eSim / Ngspice

1. Open `circuits/GF180_OpAmp/` in File Explorer.
2. Double-click `run_interactive_simulation.bat`.
3. Ngspice will launch and open the interactive graphical plot window directly on your screen.
