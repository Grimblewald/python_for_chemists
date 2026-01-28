#!/usr/bin/env python3
"""
Generate figures for Chapter 12 (Practical Projects)
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
from scipy.optimize import curve_fit

# Set random seed for reproducibility
np.random.seed(42)

# Output directory
OUTPUT_DIR = "chap12"

# Common figure settings for book
plt.rcParams.update({
    "figure.figsize": (5, 3.5),
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
    "figure.dpi": 150,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.1,
})


def save_fig(name):
    """Save figure to PDF."""
    plt.savefig(f"{OUTPUT_DIR}/{name}.pdf")
    plt.close()
    print(f"  Saved {name}.pdf")


print("Generating Chapter 12 figures...")

# ============================================================================
# Figure 1: Calibration curve
# ============================================================================

# Simulated calibration data
concentrations = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
# Multiple replicates per concentration
absorbances = {
    0.0: [0.02, 0.01, 0.03],
    0.1: [0.15, 0.14, 0.16],
    0.2: [0.28, 0.30, 0.27],
    0.3: [0.43, 0.41, 0.44],
    0.4: [0.56, 0.58, 0.55],
    0.5: [0.71, 0.69, 0.72],
}

# Calculate means and standard errors
means = np.array([np.mean(absorbances[c]) for c in concentrations])
sems = np.array([np.std(absorbances[c]) / np.sqrt(len(absorbances[c]))
                 for c in concentrations])

# Linear regression
result = linregress(concentrations, means)
slope = result.slope
intercept = result.intercept
r_squared = result.rvalue**2

fig, ax = plt.subplots(figsize=(6, 4))

# Plot data with error bars
ax.errorbar(concentrations, means, yerr=sems, fmt="ko",
            capsize=5, label="Standards", markersize=6)

# Plot regression line
x_line = np.linspace(0, concentrations.max() * 1.1, 100)
y_line = slope * x_line + intercept
ax.plot(x_line, y_line, "r-", label=f"Fit: $R^2$ = {r_squared:.4f}")

ax.set_xlabel("Concentration (M)")
ax.set_ylabel("Absorbance (AU)")
ax.set_title("Calibration Curve")
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
save_fig("calibration_curve")


# ============================================================================
# Figure 2: Kinetics analysis (2x2 diagnostic plots)
# ============================================================================

# Simulated kinetics data (first-order decay)
time = np.array([0, 5, 10, 15, 20, 25, 30, 40, 50, 60])
# True first-order decay with some noise
k_true = 0.05
C0_true = 1.0
concentration = C0_true * np.exp(-k_true * time) + np.random.randn(len(time)) * 0.02

# Define models
def first_order(t, C0, k):
    return C0 * np.exp(-k * t)

def second_order(t, C0, k):
    return C0 / (1 + k * C0 * t)

# Fit both models
popt1, _ = curve_fit(first_order, time, concentration, p0=[1.0, 0.05])
popt2, _ = curve_fit(second_order, time, concentration, p0=[1.0, 0.05])

y_fit1 = first_order(time, *popt1)
y_fit2 = second_order(time, *popt2)

# Calculate R² for both
ss_tot = np.sum((concentration - np.mean(concentration))**2)
r2_1 = 1 - np.sum((concentration - y_fit1)**2) / ss_tot
r2_2 = 1 - np.sum((concentration - y_fit2)**2) / ss_tot

# Create 2x2 figure
fig, axes = plt.subplots(2, 2, figsize=(8, 6))

# Panel 1: Raw data with fits
ax1 = axes[0, 0]
ax1.plot(time, concentration, "ko", label="Data", markersize=6)
ax1.plot(time, y_fit1, "b-", label=f"1st order ($R^2$={r2_1:.3f})", linewidth=2)
ax1.plot(time, y_fit2, "r--", label=f"2nd order ($R^2$={r2_2:.3f})", linewidth=2)
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Concentration (M)")
ax1.legend(fontsize=8)
ax1.set_title("Model Comparison")

# Panel 2: First-order linearization (ln C vs t)
ax2 = axes[0, 1]
ax2.plot(time, np.log(concentration), "ko", markersize=6)
# Add trend line
slope_ln, intercept_ln, _, _, _ = linregress(time, np.log(concentration))
ax2.plot(time, slope_ln * time + intercept_ln, "b-", linewidth=2)
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("ln(C)")
ax2.set_title("First-Order Test")

# Panel 3: Second-order linearization (1/C vs t)
ax3 = axes[1, 0]
ax3.plot(time, 1/concentration, "ko", markersize=6)
# Add trend line
slope_inv, intercept_inv, _, _, _ = linregress(time, 1/concentration)
ax3.plot(time, slope_inv * time + intercept_inv, "r-", linewidth=2)
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("1/C ($M^{-1}$)")
ax3.set_title("Second-Order Test")

# Panel 4: Residuals for best fit
ax4 = axes[1, 1]
best_fit = y_fit1 if r2_1 > r2_2 else y_fit2
residuals = concentration - best_fit
ax4.plot(time, residuals, "ko", markersize=6)
ax4.axhline(y=0, color="gray", linestyle="--", alpha=0.7)
ax4.set_xlabel("Time (s)")
ax4.set_ylabel("Residual")
ax4.set_title("Residuals (Best Fit)")

plt.tight_layout()
save_fig("kinetics_analysis")


# ============================================================================
# Figure 3: Batch processing example (spectrum)
# ============================================================================

# Simulated spectrum
wavelength = np.linspace(400, 700, 200)
# Gaussian peaks + noise
spectrum = (0.8 * np.exp(-((wavelength - 480)**2) / 500) +
            0.5 * np.exp(-((wavelength - 550)**2) / 800) +
            np.random.randn(200) * 0.02)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(wavelength, spectrum, "b-", linewidth=1.5)
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Absorbance (AU)")
ax.set_title("UV-Vis Spectrum")
ax.grid(True, alpha=0.3)

# Mark peaks
peaks_idx = [np.argmax(spectrum[50:100]) + 50, np.argmax(spectrum[120:180]) + 120]
for idx in peaks_idx:
    ax.annotate(f"{wavelength[idx]:.0f} nm",
                xy=(wavelength[idx], spectrum[idx]),
                xytext=(wavelength[idx] + 20, spectrum[idx] + 0.05),
                arrowprops=dict(arrowstyle="->", color="gray"),
                fontsize=9)

plt.tight_layout()
save_fig("spectrum_example")


print(f"\nDone! Generated 3 figures in {OUTPUT_DIR}/")
