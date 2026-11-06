#!/bin/bash
# ==============================================================================
# eSim GF180MCU PDK Integration - Automated Ubuntu Installer
# Author: Ayden Joshua M (FOSSEE eSim Autumn Fellowship 2026, IIT Bombay)
# ==============================================================================

set -e

echo "=== Installing GF180MCU PDK Integration for eSim on Ubuntu ==="

# 1. Detect eSim root directory
ESIM_ROOT=""
for dir in "/usr/share/local/eSim" "/usr/local/eSim" "$HOME/eSim" "$HOME/.eSim"; do
    if [ -d "$dir" ]; then
        ESIM_ROOT="$dir"
        break
    fi
done

if [ -z "$ESIM_ROOT" ]; then
    echo "Warning: Standard eSim directory not found. Defaulting to /usr/share/local/eSim"
    ESIM_ROOT="/usr/share/local/eSim"
fi

echo "Using eSim Root: $ESIM_ROOT"

# 2. Install KiCad Symbols
SYM_DEST="$ESIM_ROOT/library/kicadLibrary/eSim-symbols"
echo "Copying eSim_GF180.kicad_sym -> $SYM_DEST"
sudo mkdir -p "$SYM_DEST"
sudo cp library/kicadLibrary/eSim-symbols/eSim_GF180.kicad_sym "$SYM_DEST/"

# 3. Install SPICE Models
MODELS_DEST="$ESIM_ROOT/library/gf180_fd_pr/models"
echo "Copying gf180mcu.lib -> $MODELS_DEST"
sudo mkdir -p "$MODELS_DEST"
sudo cp library/gf180_fd_pr/models/gf180mcu.lib "$MODELS_DEST/"

# 4. Update KiCad sym-lib-table in user config
ENTRY="(lib (name \"eSim_GF180\")(type \"KiCad\")(uri \"$SYM_DEST/eSim_GF180.kicad_sym\")(options \"\")(descr \"GF180MCU Open PDK Component Library\"))"

for kicad_ver in "9.0" "8.0" "7.0"; do
    TABLE="$HOME/.config/kicad/$kicad_ver/sym-lib-table"
    if [ -f "$TABLE" ]; then
        if grep -q "eSim_GF180" "$TABLE"; then
            echo "sym-lib-table ($kicad_ver) already has eSim_GF180 registered."
        else
            echo "Adding eSim_GF180 to KiCad $kicad_ver sym-lib-table..."
            # Insert before the last closing parenthesis
            sed -i '$ s/)/  '"$ENTRY"'\n)/' "$TABLE"
        fi
    fi
done

# 5. Update eSim Template sym-lib-table
TEMPLATE_TABLE="$ESIM_ROOT/library/kicadLibrary/template/sym-lib-table"
if [ -f "$TEMPLATE_TABLE" ]; then
    if grep -q "eSim_GF180" "$TEMPLATE_TABLE"; then
        echo "eSim template sym-lib-table already registered."
    else
        echo "Adding eSim_GF180 to eSim template sym-lib-table..."
        sudo sed -i '$ s/)/  '"$ENTRY"'\n)/' "$TEMPLATE_TABLE"
    fi
fi

# 6. Patch Convert.py if available
CONVERT_PY="$ESIM_ROOT/src/kicadtoNgspice/Convert.py"
if [ -f "$CONVERT_PY" ]; then
    if grep -q "gf180mcu.lib" "$CONVERT_PY"; then
        echo "Convert.py is already patched for GF180MCU."
    else
        echo "Applying GF180MCU auto-detection patch to Convert.py..."
        python3 patches/apply_gf180_converter_patch.py || true
    fi
fi

echo "=============================================================="
echo " GF180MCU PDK Integration completed successfully on Ubuntu!"
echo " Launch eSim and open circuits/GF180_OpAmp to simulate."
echo "=============================================================="
