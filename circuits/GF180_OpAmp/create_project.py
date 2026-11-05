import uuid

def uid():
    return str(uuid.uuid4())

sch_text = f"""(kicad_sch (version 20211123) (generator eeschema)

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

  <!-- Transistors Instances -->
  (symbol (lib_id "eSim_GF180:nfet_03v3") (at 90 100 0) (unit 1)
    (uuid {uid()})
    (property "Reference" "M1" (id 0) (at 92.54 97.46 0))
    (property "Value" "nfet_03v3" (id 1) (at 92.54 100 0))
    (property "Model" "W=10u L=0.5u" (id 4) (at 92.54 102.54 0))
  )

  (symbol (lib_id "eSim_GF180:nfet_03v3") (at 130 100 0) (unit 1)
    (uuid {uid()})
    (property "Reference" "M2" (id 0) (at 132.54 97.46 0))
    (property "Value" "nfet_03v3" (id 1) (at 132.54 100 0))
    (property "Model" "W=10u L=0.5u" (id 4) (at 132.54 102.54 0))
  )

  (symbol (lib_id "eSim_GF180:pfet_03v3") (at 90 60 0) (unit 1)
    (uuid {uid()})
    (property "Reference" "M3" (id 0) (at 92.54 57.46 0))
    (property "Value" "pfet_03v3" (id 1) (at 92.54 60 0))
    (property "Model" "W=20u L=0.5u" (id 4) (at 92.54 62.54 0))
  )

  (symbol (lib_id "eSim_GF180:pfet_03v3") (at 130 60 0) (unit 1)
    (uuid {uid()})
    (property "Reference" "M4" (id 0) (at 132.54 57.46 0))
    (property "Value" "pfet_03v3" (id 1) (at 132.54 60 0))
    (property "Model" "W=20u L=0.5u" (id 4) (at 132.54 62.54 0))
  )

  (symbol (lib_id "eSim_GF180:nfet_03v3") (at 110 130 0) (unit 1)
    (uuid {uid()})
    (property "Reference" "M5" (id 0) (at 112.54 127.46 0))
    (property "Value" "nfet_03v3" (id 1) (at 112.54 130 0))
    (property "Model" "W=20u L=0.5u" (id 4) (at 112.54 132.54 0))
  )

  (symbol (lib_id "eSim_GF180:pfet_03v3") (at 175 60 0) (unit 1)
    (uuid {uid()})
    (property "Reference" "M6" (id 0) (at 177.54 57.46 0))
    (property "Value" "pfet_03v3" (id 1) (at 177.54 60 0))
    (property "Model" "W=40u L=0.5u" (id 4) (at 177.54 62.54 0))
  )

  (symbol (lib_id "eSim_GF180:nfet_03v3") (at 175 110 0) (unit 1)
    (uuid {uid()})
    (property "Reference" "M7" (id 0) (at 177.54 107.46 0))
    (property "Value" "nfet_03v3" (id 1) (at 177.54 110 0))
    (property "Model" "W=40u L=0.5u" (id 4) (at 177.54 112.54 0))
  )

  (symbol (lib_id "eSim_GF180:nfet_03v3") (at 50 110 0) (unit 1)
    (uuid {uid()})
    (property "Reference" "M8" (id 0) (at 52.54 107.46 0))
    (property "Value" "nfet_03v3" (id 1) (at 52.54 110 0))
    (property "Model" "W=10u L=0.5u" (id 4) (at 52.54 112.54 0))
  )

  <!-- Passives -->
  (symbol (lib_id "eSim_Devices:resistor") (at 50 60 0) (unit 1)
    (uuid {uid()})
    (property "Reference" "Rbias" (id 0) (at 52.032 60 90))
    (property "Value" "40k" (id 1) (at 50 60 90))
  )

  (symbol (lib_id "eSim_Devices:capacitor") (at 155 75 90) (unit 1)
    (uuid {uid()})
    (property "Reference" "Cc" (id 0) (at 155 72.46 0))
    (property "Value" "1.2p" (id 1) (at 155 77.54 0))
  )

  (symbol (lib_id "eSim_Devices:resistor") (at 145 75 90) (unit 1)
    (uuid {uid()})
    (property "Reference" "Rz" (id 0) (at 145 72.46 0))
    (property "Value" "1k" (id 1) (at 145 77.54 0))
  )

  (symbol (lib_id "eSim_Devices:capacitor") (at 195 90 0) (unit 1)
    (uuid {uid()})
    (property "Reference" "Cload" (id 0) (at 197.54 90 0))
    (property "Value" "10p" (id 1) (at 197.54 92.54 0))
  )

  <!-- Connections / Wires -->
  (wire (pts (xy 50 56.19) (xy 50 40)) (stroke (width 0) (type default)))
  (wire (pts (xy 50 40) (xy 92.54 40)) (stroke (width 0) (type default)))
  (wire (pts (xy 92.54 40) (xy 92.54 52.38)) (stroke (width 0) (type default)))
  (wire (pts (xy 92.54 40) (xy 132.54 40)) (stroke (width 0) (type default)))
  (wire (pts (xy 132.54 40) (xy 132.54 52.38)) (stroke (width 0) (type default)))
  (wire (pts (xy 132.54 40) (xy 177.54 40)) (stroke (width 0) (type default)))
  (wire (pts (xy 177.54 40) (xy 177.54 52.38)) (stroke (width 0) (type default)))

  (text "VDD = 3.3V" (at 50 36 0) (effects (font (size 2.0 2.0))))
  (text "Vin-" (at 75 100 0) (effects (font (size 1.5 1.5))))
  (text "Vin+" (at 145 100 0) (effects (font (size 1.5 1.5))))
  (text "Vout" (at 185 85 0) (effects (font (size 2.0 2.0))))
  (text "Differential Input Stage" (at 100 80 0) (effects (font (size 1.5 1.5))))
  (text "Second Stage (Output)" (at 175 80 0) (effects (font (size 1.5 1.5))))
  (text "Bias Gen" (at 45 80 0) (effects (font (size 1.5 1.5))))
)
"""

with open(r"C:\Users\AydenJoshua\eSim-Workspace\GF180_OpAmp\GF180_OpAmp.kicad_sch", "w", encoding="utf-8") as f:
    f.write(sch_text)

with open(r"C:\Users\AydenJoshua\eSim-Workspace\GF180_OpAmp\GF180_OpAmp.proj", "w", encoding="utf-8") as f:
    f.write("schematicFile GF180_OpAmp.kicad_sch\n")

print("Created GF180_OpAmp.kicad_sch and GF180_OpAmp.proj successfully!")
