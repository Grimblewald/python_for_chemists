#!/usr/bin/env python3
"""
Generate figures for Chapter 10 (Matplotlib)
Run this script to create all PDF figures for the book.
"""

import matplotlib.pyplot as plt
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Output directory
OUTPUT_DIR = "chap10"

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


# ============================================================================
# Figure 1: Basic sine wave
# ============================================================================
print("Generating figures...")

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure()
plt.plot(x, y)
save_fig("basic_sine")


# ============================================================================
# Figure 2: Sine with labels and title
# ============================================================================
plt.figure()
plt.plot(x, y)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Sine Wave")
save_fig("sine_labeled")


# ============================================================================
# Figure 3: Multiple lines (sin and cos)
# ============================================================================
plt.figure()
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
save_fig("sin_cos")


# ============================================================================
# Figure 4: Kinetics data (lab example)
# ============================================================================
time = np.array([0, 10, 20, 30, 40, 50, 60])
concentration = np.array([1.0, 0.82, 0.67, 0.55, 0.45, 0.37, 0.30])

plt.figure()
plt.plot(time, concentration, "ko-", label="Experimental")

# Add fitted curve
k = 0.02
t_fit = np.linspace(0, 60, 100)
c_fit = 1.0 * np.exp(-k * t_fit)
plt.plot(t_fit, c_fit, "r-", label=f"Fit: k = {k} s$^{{-1}}$")

plt.xlabel("Time (s)")
plt.ylabel("Concentration (M)")
plt.legend()
save_fig("kinetics")


# ============================================================================
# Figure 5: Basic scatter plot
# ============================================================================
x_scatter = np.random.rand(50)
y_scatter = 2 * x_scatter + 0.5 + np.random.randn(50) * 0.2

plt.figure()
plt.scatter(x_scatter, y_scatter)
plt.xlabel("Independent Variable")
plt.ylabel("Dependent Variable")
save_fig("scatter_basic")


# ============================================================================
# Figure 6: Scatter colored by value
# ============================================================================
z = x_scatter + y_scatter

plt.figure()
plt.scatter(x_scatter, y_scatter, c=z, cmap="viridis")
plt.colorbar(label="z value")
plt.xlabel("Independent Variable")
plt.ylabel("Dependent Variable")
save_fig("scatter_colorby")


# ============================================================================
# Figure 7: Basic bar chart
# ============================================================================
categories = ["A", "B", "C", "D"]
values = [23, 45, 56, 78]

plt.figure()
plt.bar(categories, values)
plt.xlabel("Category")
plt.ylabel("Value")
save_fig("bar_basic")


# ============================================================================
# Figure 8: Grouped bar chart
# ============================================================================
x_bar = np.arange(4)
width = 0.35
treatment = [23, 45, 56, 78]
control = [20, 38, 49, 65]

plt.figure()
plt.bar(x_bar - width/2, treatment, width, label="Treatment")
plt.bar(x_bar + width/2, control, width, label="Control")
plt.xticks(x_bar, ["A", "B", "C", "D"])
plt.xlabel("Category")
plt.ylabel("Value")
plt.legend()
save_fig("bar_grouped")


# ============================================================================
# Figure 9: Bar chart with error bars
# ============================================================================
means = [23, 45, 56, 78]
stds = [2, 4, 3, 5]

plt.figure()
plt.bar(categories, means, yerr=stds, capsize=5)
plt.xlabel("Category")
plt.ylabel("Value")
save_fig("bar_errorbars")


# ============================================================================
# Figure 10: Basic histogram
# ============================================================================
data_hist = np.random.randn(1000)

plt.figure()
plt.hist(data_hist, bins=30)
plt.xlabel("Value")
plt.ylabel("Frequency")
save_fig("histogram_basic")


# ============================================================================
# Figure 11: Customized histogram
# ============================================================================
plt.figure()
plt.hist(data_hist, bins=30, density=True, alpha=0.7,
         color="steelblue", edgecolor="black")
plt.xlabel("Value")
plt.ylabel("Probability Density")
save_fig("histogram_custom")


# ============================================================================
# Figure 12: 2x2 Subplots
# ============================================================================
x_sub = np.linspace(0, 10, 100)

fig, axes = plt.subplots(2, 2, figsize=(8, 6))

axes[0, 0].plot(x_sub, np.sin(x_sub))
axes[0, 0].set_title("Sine")

axes[0, 1].plot(x_sub, np.cos(x_sub))
axes[0, 1].set_title("Cosine")

axes[1, 0].plot(x_sub, np.exp(-x_sub/3))
axes[1, 0].set_title("Exponential Decay")

axes[1, 1].plot(x_sub, x_sub**2 / 10)
axes[1, 1].set_title("Quadratic")

plt.tight_layout()
save_fig("subplots_2x2")


# ============================================================================
# Figure 13: Contour plot
# ============================================================================
x_cont = np.linspace(-3, 3, 100)
y_cont = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x_cont, y_cont)
Z = np.sin(X) * np.cos(Y)

plt.figure()
plt.contour(X, Y, Z, levels=10)
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Contour Plot")
save_fig("contour")


# ============================================================================
# Figure 14: Filled contour plot
# ============================================================================
plt.figure()
plt.contourf(X, Y, Z, levels=20, cmap="RdBu_r")
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Filled Contour Plot")
save_fig("contourf")


# ============================================================================
# Figure 15: Heatmap
# ============================================================================
data_heat = np.random.rand(10, 10)

plt.figure()
plt.imshow(data_heat, cmap="viridis", aspect="auto")
plt.colorbar(label="Value")
plt.xlabel("Column")
plt.ylabel("Row")
save_fig("heatmap")


# ============================================================================
# Figure 16: Box plot
# ============================================================================
data_box = [np.random.randn(100) + i for i in range(4)]

plt.figure()
plt.boxplot(data_box, labels=["A", "B", "C", "D"])
plt.ylabel("Value")
save_fig("boxplot")


# ============================================================================
# Figure 17: Complete spectroscopy example
# ============================================================================
wavelengths = np.linspace(400, 700, 150)
spectrum1 = np.exp(-((wavelengths - 500)**2) / 1000) * 0.8
spectrum2 = np.exp(-((wavelengths - 550)**2) / 800) * 0.6
spectrum3 = np.exp(-((wavelengths - 480)**2) / 1200) * 0.9

fig, axes = plt.subplots(2, 1, figsize=(7, 5), sharex=True)

# Top panel: raw spectra
ax1 = axes[0]
ax1.plot(wavelengths, spectrum1, label="Sample A")
ax1.plot(wavelengths, spectrum2, label="Sample B")
ax1.plot(wavelengths, spectrum3, label="Sample C")
ax1.set_ylabel("Absorbance (AU)")
ax1.legend(loc="upper right")
ax1.set_title("UV-Vis Spectra Comparison")

# Bottom panel: difference spectrum
ax2 = axes[1]
difference = spectrum1 - spectrum2
ax2.plot(wavelengths, difference, "k-")
ax2.axhline(y=0, color="gray", linestyle="--", alpha=0.5)
ax2.set_ylabel("Difference (A - B)")
ax2.set_xlabel("Wavelength (nm)")

# Add peak annotation
peak_idx = np.argmax(spectrum1)
ax1.annotate(f"Peak: {wavelengths[peak_idx]:.0f} nm",
             xy=(wavelengths[peak_idx], spectrum1[peak_idx]),
             xytext=(wavelengths[peak_idx] + 50, spectrum1[peak_idx] + 0.05),
             arrowprops=dict(arrowstyle="->", color="gray"))

plt.tight_layout()
save_fig("spectra_complete")


print(f"\nDone! Generated 17 figures in {OUTPUT_DIR}/")
