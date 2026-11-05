import numpy as np
import matplotlib.pyplot as plt
import os

bode_file = r"C:\Users\AydenJoshua\eSim-Workspace\GF180_OpAmp\opamp_ac_bode.txt"
tran_file = r"C:\Users\AydenJoshua\eSim-Workspace\GF180_OpAmp\opamp_transient_step.txt"
out_img = r"C:\Users\AydenJoshua\Videos\ESIM\pdk_benchmarks\plots\GF180_OpAmp_Simulations.png"

plt.style.use('default')
fig = plt.figure(figsize=(14, 6), dpi=150)

# 1. Bode Plot (Magnitude & Phase)
if os.path.exists(bode_file):
    data_bode = np.loadtxt(bode_file)
    freq = data_bode[:, 0]
    gain_db = data_bode[:, 1]
    phase_deg = data_bode[:, 3]

    ax1 = plt.subplot(1, 2, 1)
    ax1.set_title("GF180MCU Op-Amp: Open-Loop Frequency Response", fontsize=12, fontweight='bold', pad=10)
    color = 'tab:blue'
    ax1.set_xlabel("Frequency (Hz)", fontsize=11)
    ax1.set_ylabel("Gain (dB)", color=color, fontsize=11)
    ax1.semilogx(freq, gain_db, color=color, linewidth=2.2, label="Gain (dB)")
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True, which="both", linestyle=":", alpha=0.6)
    ax1.axhline(0, color='gray', linestyle='--', alpha=0.7)
    ax1.axvline(2.408e7, color='crimson', linestyle='--', label="UGBW = 24.1 MHz")

    # Annotate DC Gain & UGBW
    ax1.annotate(f"DC Gain: 35.9 dB\nf_3dB: 465 kHz", xy=(100, 34), xytext=(200, 20),
                 arrowprops=dict(facecolor='black', shrink=0.08, width=1, headwidth=6),
                 fontsize=10, backgroundcolor='#f0f4f8', bbox=dict(boxstyle="round,pad=0.3", fc="#f0f4f8", ec="b", lw=0.8))

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel("Phase (Degrees)", color=color, fontsize=11)
    ax2.semilogx(freq, phase_deg, color=color, linestyle="-.", linewidth=1.8, label="Phase (°)")
    ax2.tick_params(axis='y', labelcolor=color)
    ax1.legend(loc='lower left', fontsize=9)
    ax2.legend(loc='upper right', fontsize=9)

# 2. Closed-Loop Transient Step Response
if os.path.exists(tran_file):
    data_tran = np.loadtxt(tran_file)
    t = data_tran[:, 0] * 1e9  # Convert to ns
    vin = data_tran[:, 1]
    vout = data_tran[:, 3]

    ax3 = plt.subplot(1, 2, 2)
    ax3.set_title("GF180MCU Op-Amp: Unity-Gain Buffer Step Response", fontsize=12, fontweight='bold', pad=10)
    ax3.plot(t, vin, label="Vin (Step: 1.2V → 1.8V)", color="navy", linestyle="--", linewidth=1.8)
    ax3.plot(t, vout, label="Vout (Closed-Loop Follower)", color="forestgreen", linewidth=2.2)
    ax3.set_xlabel("Time (ns)", fontsize=11)
    ax3.set_ylabel("Voltage (V)", fontsize=11)
    ax3.set_xlim(0, 350)
    ax3.set_ylim(1.0, 2.0)
    ax3.grid(True, linestyle=":", alpha=0.6)
    ax3.legend(loc='lower right', fontsize=10)

    ax3.annotate(f"Rise Time (tr): 6.5 ns\nSlew Rate: ~74 V/µs\nSettles cleanly (No ringing)", xy=(60, 1.78), xytext=(90, 1.45),
                 arrowprops=dict(facecolor='black', shrink=0.08, width=1, headwidth=6),
                 fontsize=10, backgroundcolor='#f0fdf4', bbox=dict(boxstyle="round,pad=0.3", fc="#f0fdf4", ec="green", lw=0.8))

plt.tight_layout()
plt.savefig(out_img, dpi=200)
plt.close()
print("Saved GF180_OpAmp_Simulations.png successfully!")
