# GF180MCU Open PDK Integration & Two-Stage CMOS Op-Amp for eSim 2.6

**FOSSEE eSim Autumn Fellowship 2026 — IIT Bombay**  
* **Intern:** Ayden Joshua M (3rd Year B.Tech ECE, Vellore Institute of Technology)  
* **Mentors:** Mr. Sumanto Kar, Sri. Varad Patil, Ms. Shanthi Priya K  
* **Task:** Integration with PDKs: IHP and GlobalFoundries (GF180MCU) Process Nodes (EE Tasks)  

---

## 1. Project Overview

This repository introduces the integration pipeline for the **GlobalFoundries GF180MCU (0.18µm / 180nm CMOS)** Open-Source Process Design Kit into **eSim 2.6** (developed by FOSSEE, IIT Bombay). 

Prior to this work, GF180MCU had 0% integration in eSim. This project establishes:
1. **KiCad 8/9 Symbol Library (`eSim_GF180.kicad_sym`):** Standard 4-pin MOSFET primitives (`nfet_03v3` and `pfet_03v3`) mapped to eSim spice netlister.
2. **BSIM3v3 Compact Model Deck (`gf180mcu.lib`):** Level 8 BSIM3v3 SPICE models avoiding the Verilog-A Windows compilation limitation in Ngspice.
3. **Reference Benchmark Circuit (Two-Stage CMOS Op-Amp):** A complete, fully connected analog IC design with active current-mirror loads and Miller frequency compensation.
4. **Simulation & Characterization Suite:** Open-loop frequency response (Bode plot) and closed-loop buffer transient step response analyzed using Ngspice.

---

## 2. Repository Structure

```
├── circuits/
│   └── GF180_OpAmp/                 # Complete eSim 2.6 Project
│       ├── GF180_OpAmp.kicad_sch    # Fully wired schematic file
│       ├── GF180_OpAmp.proj         # eSim project configuration
│       ├── GF180_OpAmp.cir          # AC frequency response netlist
│       ├── GF180_OpAmp_transient.cir# Closed-loop transient netlist
│       ├── gf180mcu.lib             # Bundled GF180MCU BSIM3v3 models
│       └── run_simulation_gui.bat   # 1-click interactive simulation runner
├── library/
│   ├── kicadLibrary/eSim-symbols/
│   │   └── eSim_GF180.kicad_sym     # KiCad 8/9 symbol definitions
│   └── gf180_fd_pr/models/
│       └── gf180mcu.lib             # Foundry SPICE model deck
├── plots/
│   ├── GF180_OpAmp_Schematic.png    # High-resolution schematic export
│   ├── GF180_OpAmp_Simulations.png  # Bode plot & transient step response
│   ├── gf180_inverter.png           # Digital inverter comparison plot
│   ├── sky130_inverter.png          # SkyWater 130nm reference plot
│   └── ihp_inverter.png             # IHP SG13 reference plot
├── presentation/
│   └── GF180_PDK_Integration_AydenJoshua.pptx  # 4-slide review presentation
└── README.md
```

---

## 3. Two-Stage CMOS Op-Amp Specifications & Performance

| Parameter | Measured Value | Unit |
| :--- | :--- | :--- |
| Supply Voltage ($V_{DD}$) | 3.3 | V |
| Input Common-Mode Range | 1.0 – 2.2 | V |
| DC Open-Loop Gain ($A_{v0}$) | 35.93 | dB ($\approx 63\times$) |
| 3-dB Bandwidth ($f_{3\text{dB}}$) | 465.4 | kHz |
| Unity-Gain Bandwidth (UGBW) | 24.08 | MHz |
| Phase Margin (PM) | > 65 | Degrees (Unconditionally Stable) |
| Slew Rate (SR) | $\approx$ 74 | V/µs |
| Transient Rise Time ($t_r$) | 6.49 | ns |

---

## 4. How to Use in eSim 2.6

1. **Install Symbols:** Copy `library/kicadLibrary/eSim-symbols/eSim_GF180.kicad_sym` into your eSim installation directory (`C:\FOSSEE\eSim\library\kicadLibrary\eSim-symbols\`).
2. **Register in `sym-lib-table`:** Append the following line to `sym-lib-table`:
   ```lisp
   (lib (name "eSim_GF180")(type "KiCad")(uri "${KICAD6_SYMBOL_DIR}/eSim_GF180.kicad_sym")(options "")(descr "GF180MCU Open PDK Symbols"))
   ```
3. **Open Project:** Launch eSim, open `circuits/GF180_OpAmp`, and run simulations directly in Ngspice.
