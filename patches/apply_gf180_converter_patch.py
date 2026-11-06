path = r"C:\FOSSEE\eSim\src\kicadtoNgspice\Convert.py"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

target = """            # This has to be second i.e after deviceLine details
            # Adding .include line to Schematic Info at the start of line
            for item in list(set(includeLine)):
                schematicInfo.insert(0, item)

        return schematicInfo"""

patch = """            # This has to be second i.e after deviceLine details
            # Adding .include line to Schematic Info at the start of line
            for item in list(set(includeLine)):
                schematicInfo.insert(0, item)

        # Auto-detect GF180MCU components and ensure gf180mcu.lib is included
        has_gf180 = any(
            any(dev in line.lower() for dev in ['nfet_03v3', 'pfet_03v3', 'nfet_05v0', 'pfet_05v0', 'nfet_06v0', 'pfet_06v0', 'gf180'])
            for line in schematicInfo
        )
        if has_gf180:
            gf180_model_deck = "C:/FOSSEE/eSim/library/gf180_fd_pr/models/gf180mcu.lib"
            lib_line = f'.lib "{gf180_model_deck}" tt'
            if not any("gf180mcu.lib" in l for l in schematicInfo):
                schematicInfo.insert(0, lib_line)
                print("Convert.py: Automatically added GF180MCU model deck:", lib_line)

        return schematicInfo"""

if target in c:
    c = c.replace(target, patch)
    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Convert.py successfully patched!")
else:
    print("Target not found in Convert.py")
