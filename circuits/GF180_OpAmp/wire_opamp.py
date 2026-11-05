import uuid

def uid():
    return str(uuid.uuid4())

# Coordinates of components on schematic
# M3 (PMOS load 1): (90, 60)
# M4 (PMOS load 2): (130, 60)
# M1 (NMOS diff in-): (90, 100)
# M2 (NMOS diff in+): (130, 100)
# M5 (NMOS tail): (110, 135)
# M6 (PMOS CS driver): (175, 60)
# M7 (NMOS sink load): (175, 110)
# M8 (NMOS diode bias): (45, 110)
# Rbias (Resistor): (45, 60)
# Rz (Resistor, rot=90): (145, 80)
# Cc (Capacitor, rot=90): (158, 80)
# Cload (Capacitor): (195, 95)

# Pins calculations:
# PFET (x, y): S=(x+2.54, y-7.62), D=(x+2.54, y+7.62), G=(x-5.08, y), B=(x+5.08, y-3.81)
# NFET (x, y): D=(x+2.54, y-7.62), S=(x+2.54, y+7.62), G=(x-5.08, y), B=(x+5.08, y+3.81)

wires = []
junctions = []

def add_wire(x1, y1, x2, y2):
    wires.append(f'  (wire (pts (xy {x1} {y1}) (xy {x2} {y2})) (stroke (width 0) (type default)))')

def add_junction(x, y):
    junctions.append(f'  (junction (at {x} {y}) (diameter 0.9144) (color 0 0 0 0))')

# 1. VDD Rail at Y=35
add_wire(30, 35, 185, 35) # Main horizontal VDD bus

# VDD drops to sources of PMOS and Rbias
# Rbias top (45, 56.19)
add_wire(45, 35, 45, 56.19)
add_junction(45, 35)

# M3 Source (92.54, 52.38) & Bulk (95.08, 56.19)
add_wire(92.54, 35, 92.54, 52.38)
add_junction(92.54, 35)
add_wire(95.08, 56.19, 95.08, 45)
add_wire(95.08, 45, 92.54, 45)
add_junction(92.54, 45)

# M4 Source (132.54, 35) to (132.54, 52.38) & Bulk
add_wire(132.54, 35, 132.54, 52.38)
add_junction(132.54, 35)
add_wire(135.08, 56.19, 135.08, 45)
add_wire(135.08, 45, 132.54, 45)
add_junction(132.54, 45)

# M6 Source (177.54, 35) to (177.54, 52.38) & Bulk
add_wire(177.54, 35, 177.54, 52.38)
add_junction(177.54, 35)
add_wire(180.08, 56.19, 180.08, 45)
add_wire(180.08, 45, 177.54, 45)
add_junction(177.54, 45)

# 2. Bias Network
# Rbias bottom (45, 63.81) to M8 Drain (47.54, 102.38)
add_wire(45, 63.81, 47.54, 63.81)
add_wire(47.54, 63.81, 47.54, 102.38)

# M8 Diode Connection: Drain (47.54, 102.38) to Gate (39.92, 110)
add_wire(47.54, 95, 35, 95)
add_wire(35, 95, 35, 110)
add_wire(35, 110, 39.92, 110)
add_junction(47.54, 95)

# Bias Bus (Vbias) from M8 Gate (35, 110) to M5 Gate (104.92, 135) and M7 Gate (169.92, 110)
add_wire(35, 110, 35, 125)
add_wire(35, 125, 104.92, 125)
add_wire(104.92, 125, 104.92, 135) # to M5 Gate
add_junction(35, 110)

add_wire(104.92, 125, 169.92, 125) # to M7 Gate
add_wire(169.92, 125, 169.92, 110)
add_junction(104.92, 125)

# M8 Source (47.54, 117.62) & Bulk (50.08, 113.81) to GND at Y=155
add_wire(47.54, 117.62, 47.54, 155)
add_wire(50.08, 113.81, 50.08, 120)
add_wire(50.08, 120, 47.54, 120)
add_junction(47.54, 120)

# 3. Differential Pair Connections
# M3 Drain (92.54, 67.62) to M1 Drain (92.54, 92.38)
add_wire(92.54, 67.62, 92.54, 92.38)

# M3 Gate (84.92, 60) tied to M3 Drain (92.54, 75) - Diode Active Load
add_wire(84.92, 60, 84.92, 75)
add_wire(84.92, 75, 92.54, 75)
add_junction(92.54, 75)

# Mirror to M4 Gate (124.92, 60)
add_wire(84.92, 75, 84.92, 70)
add_wire(84.92, 70, 124.92, 70)
add_wire(124.92, 70, 124.92, 60)
add_junction(84.92, 75)

# M4 Drain (132.54, 67.62) to M2 Drain (132.54, 92.38) [Node n2]
add_wire(132.54, 67.62, 132.54, 92.38)

# M1 Source (92.54, 107.62) and M2 Source (132.54, 107.62) to Tail Node (112.54, 115)
add_wire(92.54, 107.62, 92.54, 115)
add_wire(92.54, 115, 112.54, 115)
add_wire(132.54, 107.62, 132.54, 115)
add_wire(132.54, 115, 112.54, 115)
add_wire(112.54, 115, 112.54, 127.38) # To M5 Drain (112.54, 127.38)
add_junction(112.54, 115)

# M1 Bulk (95.08, 103.81) to Source & M2 Bulk (135.08, 103.81) to Source
add_wire(95.08, 103.81, 95.08, 110)
add_wire(95.08, 110, 92.54, 110)
add_junction(92.54, 110)

add_wire(135.08, 103.81, 135.08, 110)
add_wire(135.08, 110, 132.54, 110)
add_junction(132.54, 110)

# M5 Source (112.54, 142.62) & Bulk to GND at Y=155
add_wire(112.54, 142.62, 112.54, 155)
add_wire(115.08, 138.81, 115.08, 145)
add_wire(115.08, 145, 112.54, 145)
add_junction(112.54, 145)

# Differential Inputs:
# M1 Gate (84.92, 100) to Vin- port
add_wire(84.92, 100, 75, 100)

# M2 Gate (124.92, 100) to Vin+ port
add_wire(124.92, 100, 140, 100)

# 4. First Stage Output (Node n2) to Second Stage Gate & Miller Compensation
# Node n2 is at (132.54, 80)
# Connect to M6 Gate (169.92, 60)
add_wire(132.54, 80, 141.19, 80) # To Rz left pin (141.19, 80)
add_junction(132.54, 80)

add_wire(132.54, 80, 132.54, 85)
add_wire(132.54, 85, 165, 85)
add_wire(165, 85, 165, 60)
add_wire(165, 60, 169.92, 60) # To M6 Gate

# Rz right pin (148.81, 80) to Cc left pin (154.19, 80)
add_wire(148.81, 80, 154.19, 80)

# Cc right pin (161.81, 80) to Vout node (177.54, 80)
add_wire(161.81, 80, 177.54, 80)
add_junction(177.54, 80)

# Second Stage Output Node: M6 Drain (177.54, 67.62) to M7 Drain (177.54, 102.38)
add_wire(177.54, 67.62, 177.54, 102.38)

# Vout line extends to Cload top pin (195, 91.19) and Vout output port
add_wire(177.54, 80, 195, 80)
add_wire(195, 80, 195, 91.19)
add_wire(195, 80, 205, 80) # Vout output terminal

# Cload bottom pin (195, 98.81) to GND at Y=155
add_wire(195, 98.81, 195, 155)

# M7 Source (177.54, 117.62) & Bulk to GND at Y=155
add_wire(177.54, 117.62, 177.54, 155)
add_wire(180.08, 113.81, 180.08, 120)
add_wire(180.08, 120, 177.54, 120)
add_junction(177.54, 120)

# 5. GND Bus at Y=155
add_wire(30, 155, 200, 155)
add_junction(47.54, 155)
add_junction(112.54, 155)
add_junction(177.54, 155)
add_junction(195, 155)

print(f"Generated {len(wires)} wires and {len(junctions)} junctions.")

# Read template symbols
import build_valid_sch
M1_id = uid()
M2_id = uid()
M3_id = uid()
M4_id = uid()
M5_id = uid()
M6_id = uid()
M7_id = uid()
M8_id = uid()
Rbias_id = uid()
Rz_id = uid()
Cc_id = uid()
Cload_id = uid()

sch_full = f"""(kicad_sch (version 20211123) (generator eeschema)

  (uuid {uid()})

  (paper "A4")

  (title_block
    (title "Two-Stage CMOS Operational Amplifier in GF180MCU PDK")
    (date "2026-11-05")
    (rev "1.0")
    (company "FOSSEE eSim Fellowship - IIT Bombay")
    (comment 1 "Designed by Ayden Joshua M (VIT)")
    (comment 2 "GlobalFoundries 180nm Open PDK (3.3V CMOS)")
  )

  (lib_symbols
    (symbol "eSim_GF180:nfet_03v3" (pin_names (offset 0.254)) (in_bom yes) (on_board yes)
      (property "Reference" "M" (id 0) (at 2.54 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Value" "nfet_03v3" (id 1) (at 2.54 0 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Footprint" "" (id 2) (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "GF180MCU 3.3V NMOS" (id 3) (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "nfet_03v3_0_1"
        (polyline (pts (xy 0.254 -2.54) (xy -2.032 -2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.254 0) (xy -2.032 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.254 2.54) (xy -2.032 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -2.032 -3.302) (xy -2.032 3.302)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -2.794 -3.302) (xy -2.794 3.302)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0.254 -2.54) (xy 0.254 -3.81) (xy 2.54 -3.81)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.254 2.54) (xy 0.254 3.81) (xy 2.54 3.81) (xy 2.54 5.08)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.254 0) (xy 2.54 0) (xy 2.54 -5.08)) (stroke (width 0) (type default)) (fill (type none)))
        (circle (center 1.27 0) (radius 3.302) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "nfet_03v3_1_1"
        (pin passive line (at -5.08 0 0) (length 2.286) (name "G" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 7.62 270) (length 2.54) (name "D" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 -7.62 90) (length 2.54) (name "S" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 5.08 -3.81 180) (length 2.54) (name "B" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "eSim_GF180:pfet_03v3" (pin_names (offset 0.254)) (in_bom yes) (on_board yes)
      (property "Reference" "M" (id 0) (at 2.54 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Value" "pfet_03v3" (id 1) (at 2.54 0 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Footprint" "" (id 2) (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "GF180MCU 3.3V PMOS" (id 3) (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "pfet_03v3_0_1"
        (polyline (pts (xy 0.254 -2.54) (xy -2.032 -2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.254 0) (xy -2.032 0)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.254 2.54) (xy -2.032 2.54)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy -2.032 -3.302) (xy -2.032 3.302)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy -2.794 -3.302) (xy -2.794 3.302)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 0.254 2.54) (xy 0.254 3.81) (xy 2.54 3.81)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.254 -2.54) (xy 0.254 -3.81) (xy 2.54 -3.81) (xy 2.54 -5.08)) (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 0.254 0) (xy 2.54 0) (xy 2.54 5.08)) (stroke (width 0) (type default)) (fill (type none)))
        (circle (center -3.556 0) (radius 0.508) (stroke (width 0) (type default)) (fill (type none)))
        (circle (center 1.27 0) (radius 3.302) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "pfet_03v3_1_1"
        (pin passive line (at -5.08 0 0) (length 1.27) (name "G" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 -7.62 90) (length 2.54) (name "D" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 2.54 7.62 270) (length 2.54) (name "S" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 5.08 3.81 180) (length 2.54) (name "B" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "eSim_Devices:resistor" (pin_numbers hide) (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "R" (id 0) (at 2.032 0 90) (effects (font (size 1.27 1.27))))
      (property "Value" "resistor" (id 1) (at 0 0 90) (effects (font (size 1.27 1.27))))
      (symbol "resistor_0_1"
        (polyline (pts (xy 0 -2.54) (xy -0.889 -1.905) (xy 0.889 -1.27) (xy -0.889 -0.635) (xy 0.889 0) (xy -0.889 0.635) (xy 0.889 1.27) (xy -0.889 1.905) (xy 0 2.54)) (stroke (width 0.254) (type default)) (fill (type none)))
      )
      (symbol "resistor_1_1"
        (pin passive line (at 0 3.81 270) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "eSim_Devices:capacitor" (pin_numbers hide) (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "C" (id 0) (at 2.54 0 0) (effects (font (size 1.27 1.27))))
      (property "Value" "capacitor" (id 1) (at 2.54 -2.54 0) (effects (font (size 1.27 1.27))))
      (symbol "capacitor_0_1"
        (polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
        (polyline (pts (xy -2.032 0.762) (xy 2.032 0.762)) (stroke (width 0.508) (type default)) (fill (type none)))
      )
      (symbol "capacitor_1_1"
        (pin passive line (at 0 3.81 270) (length 3.048) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 3.048) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )
  )

  <!-- Components -->
  (symbol (lib_id "eSim_GF180:nfet_03v3") (at 90 100 0) (unit 1)
    (in_bom yes) (on_board yes)
    (uuid {M1_id})
    (property "Reference" "M1" (id 0) (at 84 92 0))
    (property "Value" "nfet_03v3" (id 1) (at 84 95 0))
    (property "Model" "W=10u L=0.5u" (id 4) (at 84 98 0))
    (pin "1" (uuid {uid()}))
    (pin "2" (uuid {uid()}))
    (pin "3" (uuid {uid()}))
    (pin "4" (uuid {uid()}))
  )

  (symbol (lib_id "eSim_GF180:nfet_03v3") (at 130 100 0) (unit 1)
    (in_bom yes) (on_board yes)
    (uuid {M2_id})
    (property "Reference" "M2" (id 0) (at 138 92 0))
    (property "Value" "nfet_03v3" (id 1) (at 138 95 0))
    (property "Model" "W=10u L=0.5u" (id 4) (at 138 98 0))
    (pin "1" (uuid {uid()}))
    (pin "2" (uuid {uid()}))
    (pin "3" (uuid {uid()}))
    (pin "4" (uuid {uid()}))
  )

  (symbol (lib_id "eSim_GF180:pfet_03v3") (at 90 60 0) (unit 1)
    (in_bom yes) (on_board yes)
    (uuid {M3_id})
    (property "Reference" "M3" (id 0) (at 84 52 0))
    (property "Value" "pfet_03v3" (id 1) (at 84 55 0))
    (property "Model" "W=20u L=0.5u" (id 4) (at 84 58 0))
    (pin "1" (uuid {uid()}))
    (pin "2" (uuid {uid()}))
    (pin "3" (uuid {uid()}))
    (pin "4" (uuid {uid()}))
  )

  (symbol (lib_id "eSim_GF180:pfet_03v3") (at 130 60 0) (unit 1)
    (in_bom yes) (on_board yes)
    (uuid {M4_id})
    (property "Reference" "M4" (id 0) (at 138 52 0))
    (property "Value" "pfet_03v3" (id 1) (at 138 55 0))
    (property "Model" "W=20u L=0.5u" (id 4) (at 138 58 0))
    (pin "1" (uuid {uid()}))
    (pin "2" (uuid {uid()}))
    (pin "3" (uuid {uid()}))
    (pin "4" (uuid {uid()}))
  )

  (symbol (lib_id "eSim_GF180:nfet_03v3") (at 110 135 0) (unit 1)
    (in_bom yes) (on_board yes)
    (uuid {M5_id})
    (property "Reference" "M5" (id 0) (at 118 127 0))
    (property "Value" "nfet_03v3" (id 1) (at 118 130 0))
    (property "Model" "W=20u L=0.5u" (id 4) (at 118 133 0))
    (pin "1" (uuid {uid()}))
    (pin "2" (uuid {uid()}))
    (pin "3" (uuid {uid()}))
    (pin "4" (uuid {uid()}))
  )

  (symbol (lib_id "eSim_GF180:pfet_03v3") (at 175 60 0) (unit 1)
    (in_bom yes) (on_board yes)
    (uuid {M6_id})
    (property "Reference" "M6" (id 0) (at 183 52 0))
    (property "Value" "pfet_03v3" (id 1) (at 183 55 0))
    (property "Model" "W=40u L=0.5u" (id 4) (at 183 58 0))
    (pin "1" (uuid {uid()}))
    (pin "2" (uuid {uid()}))
    (pin "3" (uuid {uid()}))
    (pin "4" (uuid {uid()}))
  )

  (symbol (lib_id "eSim_GF180:nfet_03v3") (at 175 110 0) (unit 1)
    (in_bom yes) (on_board yes)
    (uuid {M7_id})
    (property "Reference" "M7" (id 0) (at 183 102 0))
    (property "Value" "nfet_03v3" (id 1) (at 183 105 0))
    (property "Model" "W=40u L=0.5u" (id 4) (at 183 108 0))
    (pin "1" (uuid {uid()}))
    (pin "2" (uuid {uid()}))
    (pin "3" (uuid {uid()}))
    (pin "4" (uuid {uid()}))
  )

  (symbol (lib_id "eSim_GF180:nfet_03v3") (at 45 110 0) (unit 1)
    (in_bom yes) (on_board yes)
    (uuid {M8_id})
    (property "Reference" "M8" (id 0) (at 53 102 0))
    (property "Value" "nfet_03v3" (id 1) (at 53 105 0))
    (property "Model" "W=10u L=0.5u" (id 4) (at 53 108 0))
    (pin "1" (uuid {uid()}))
    (pin "2" (uuid {uid()}))
    (pin "3" (uuid {uid()}))
    (pin "4" (uuid {uid()}))
  )

  (symbol (lib_id "eSim_Devices:resistor") (at 45 60 0) (unit 1)
    (in_bom yes) (on_board yes)
    (uuid {Rbias_id})
    (property "Reference" "Rbias" (id 0) (at 51 60 90))
    (property "Value" "40k" (id 1) (at 45 60 90))
    (pin "1" (uuid {uid()}))
    (pin "2" (uuid {uid()}))
  )

  (symbol (lib_id "eSim_Devices:resistor") (at 145 80 90) (unit 1)
    (in_bom yes) (on_board yes)
    (uuid {Rz_id})
    (property "Reference" "Rz" (id 0) (at 145 74 0))
    (property "Value" "1k" (id 1) (at 145 77 0))
    (pin "1" (uuid {uid()}))
    (pin "2" (uuid {uid()}))
  )

  (symbol (lib_id "eSim_Devices:capacitor") (at 158 80 90) (unit 1)
    (in_bom yes) (on_board yes)
    (uuid {Cc_id})
    (property "Reference" "Cc" (id 0) (at 158 74 0))
    (property "Value" "1.2p" (id 1) (at 158 77 0))
    (pin "1" (uuid {uid()}))
    (pin "2" (uuid {uid()}))
  )

  (symbol (lib_id "eSim_Devices:capacitor") (at 195 95 0) (unit 1)
    (in_bom yes) (on_board yes)
    (uuid {Cload_id})
    (property "Reference" "Cload" (id 0) (at 201 95 0))
    (property "Value" "10p" (id 1) (at 201 98 0))
    (pin "1" (uuid {uid()}))
    (pin "2" (uuid {uid()}))
  )

  <!-- Wires -->
  {chr(10).join(wires)}

  <!-- Junctions -->
  {chr(10).join(junctions)}

  <!-- Annotations & Labels -->
  (text "VDD = 3.3V" (at 30 31 0) (effects (font (size 2.5 2.5) (bold yes))))
  (text "GND (0V)" (at 30 160 0) (effects (font (size 2.5 2.5) (bold yes))))
  (text "Vin-" (at 72 100 0) (effects (font (size 2.0 2.0) (bold yes))))
  (text "Vin+" (at 143 100 0) (effects (font (size 2.0 2.0) (bold yes))))
  (text "Vout" (at 208 80 0) (effects (font (size 2.5 2.5) (bold yes))))
  (text "Bias Generator" (at 45 48 0) (effects (font (size 1.8 1.8))))
  (text "Differential Input Stage" (at 110 48 0) (effects (font (size 1.8 1.8))))
  (text "Output Stage" (at 175 48 0) (effects (font (size 1.8 1.8))))
  (text "Miller Comp (Rz + Cc)" (at 151 72 0) (effects (font (size 1.4 1.4))))

  (sheet_instances
    (path "/" (page "1"))
  )

  (symbol_instances
    (path "/{M1_id}" (reference "M1") (unit 1) (value "nfet_03v3") (footprint ""))
    (path "/{M2_id}" (reference "M2") (unit 1) (value "nfet_03v3") (footprint ""))
    (path "/{M3_id}" (reference "M3") (unit 1) (value "pfet_03v3") (footprint ""))
    (path "/{M4_id}" (reference "M4") (unit 1) (value "pfet_03v3") (footprint ""))
    (path "/{M5_id}" (reference "M5") (unit 1) (value "nfet_03v3") (footprint ""))
    (path "/{M6_id}" (reference "M6") (unit 1) (value "pfet_03v3") (footprint ""))
    (path "/{M7_id}" (reference "M7") (unit 1) (value "nfet_03v3") (footprint ""))
    (path "/{M8_id}" (reference "M8") (unit 1) (value "nfet_03v3") (footprint ""))
    (path "/{Rbias_id}" (reference "Rbias") (unit 1) (value "40k") (footprint ""))
    (path "/{Rz_id}" (reference "Rz") (unit 1) (value "1k") (footprint ""))
    (path "/{Cc_id}" (reference "Cc") (unit 1) (value "1.2p") (footprint ""))
    (path "/{Cload_id}" (reference "Cload") (unit 1) (value "10p") (footprint ""))
  )
)
"""

sch_path = r"C:\Users\AydenJoshua\eSim-Workspace\GF180_OpAmp\GF180_OpAmp.kicad_sch"
with open(sch_path, "w", encoding="utf-8") as f:
    f.write(sch_full)

print("Saved fully wired schematic!")
