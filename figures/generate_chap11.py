#!/usr/bin/env python3
"""
Generate figures for Chapter 11 (SciPy)
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from scipy.optimize import curve_fit
from scipy.fft import fft, fftfreq

# Set random seed for reproducibility
np.random.seed(42)

# Output directory
OUTPUT_DIR = "chap11"

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


print("Generating Chapter 11 figures...")

# ============================================================================
# Figure 1: Exponential decay curve fit
# ============================================================================
def exponential_decay(t, A, k):
    return A * np.exp(-k * t)

t_data = np.array([0, 10, 20, 30, 40, 50])
c_data = np.array([1.0, 0.82, 0.67, 0.55, 0.45, 0.37])

popt, pcov = curve_fit(exponential_decay, t_data, c_data)
A_fit, k_fit = popt

t_smooth = np.linspace(0, 50, 100)
c_fit = exponential_decay(t_smooth, *popt)

plt.figure()
plt.plot(t_data, c_data, "ko", markersize=8, label="Data")
plt.plot(t_smooth, c_fit, "r-", label=f"Fit: k = {k_fit:.4f}")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend()
plt.title("Exponential Decay Fit")
save_fig("curve_fit_decay")


# ============================================================================
# Figure 2: Gaussian peak fit
# ============================================================================
def gaussian(x, amplitude, center, width, baseline):
    return amplitude * np.exp(-(x - center)**2 / (2 * width**2)) + baseline

wavelengths = np.linspace(400, 600, 100)
true_peak = gaussian(wavelengths, 0.8, 500, 20, 0.1)
noise = np.random.randn(100) * 0.02
spectrum = true_peak + noise

p0 = [0.7, 495, 25, 0.1]
popt, pcov = curve_fit(gaussian, wavelengths, spectrum, p0=p0)

plt.figure()
plt.plot(wavelengths, spectrum, "b-", alpha=0.7, label="Data")
plt.plot(wavelengths, gaussian(wavelengths, *popt), "r-", linewidth=2,
         label=f"Fit: center = {popt[1]:.1f} nm")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Absorbance")
plt.legend()
plt.title("Gaussian Peak Fit")
save_fig("curve_fit_gaussian")


# ============================================================================
# Figure 3: Simple ODE - exponential decay
# ============================================================================
def decay(y, t, k):
    return -k * y

k = 0.1
y0 = 1.0
t = np.linspace(0, 50, 100)

solution = odeint(decay, y0, t, args=(k,))

plt.figure()
plt.plot(t, solution, "b-", linewidth=2)
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.title("First-Order Decay (ODE Solution)")
save_fig("ode_decay")


# ============================================================================
# Figure 4: Coupled ODEs - A -> B -> C reaction
# ============================================================================
def reaction_system(y, t, k1, k2):
    A, B, C = y
    dAdt = -k1 * A
    dBdt = k1 * A - k2 * B
    dCdt = k2 * B
    return [dAdt, dBdt, dCdt]

k1, k2 = 0.1, 0.05
y0 = [1.0, 0.0, 0.0]
t = np.linspace(0, 100, 200)

solution = odeint(reaction_system, y0, t, args=(k1, k2))
A, B, C = solution.T

plt.figure()
plt.plot(t, A, "b-", label="A", linewidth=2)
plt.plot(t, B, "g-", label="B", linewidth=2)
plt.plot(t, C, "r-", label="C", linewidth=2)
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend()
plt.title("Consecutive Reactions: A → B → C")
save_fig("ode_reaction")


# ============================================================================
# Figure 5: Interpolation comparison
# ============================================================================
from scipy.interpolate import interp1d

x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([0, 0.8, 0.9, 0.1, -0.8, -1.0])

f_linear = interp1d(x_data, y_data, kind="linear")
f_cubic = interp1d(x_data, y_data, kind="cubic")

x_new = np.linspace(0, 5, 50)

plt.figure()
plt.plot(x_data, y_data, "ko", markersize=10, label="Data points")
plt.plot(x_new, f_linear(x_new), "b--", label="Linear", linewidth=2)
plt.plot(x_new, f_cubic(x_new), "r-", label="Cubic", linewidth=2)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Interpolation Methods")
save_fig("interpolation")


# ============================================================================
# Figure 6: FFT / Power spectrum
# ============================================================================
dt = 0.01
t = np.arange(0, 1, dt)
signal = np.sin(2*np.pi*5*t) + 0.5*np.sin(2*np.pi*10*t)

spectrum = fft(signal)
freqs = fftfreq(len(t), dt)

plt.figure()
plt.plot(freqs[:len(freqs)//2], np.abs(spectrum[:len(spectrum)//2]), "b-", linewidth=2)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("Power Spectrum (5 Hz + 10 Hz signal)")
plt.xlim(0, 20)
save_fig("fft_spectrum")


# ============================================================================
# Figure 7: Signal smoothing
# ============================================================================
from scipy.signal import savgol_filter
from scipy.ndimage import gaussian_filter1d

x = np.linspace(0, 10, 100)
y_clean = np.sin(x)
y_noisy = y_clean + np.random.randn(100) * 0.2

y_savgol = savgol_filter(y_noisy, window_length=11, polyorder=3)
y_gauss = gaussian_filter1d(y_noisy, sigma=2)

plt.figure(figsize=(6, 4))
plt.plot(x, y_noisy, "gray", alpha=0.5, label="Noisy data")
plt.plot(x, y_savgol, "b-", linewidth=2, label="Savitzky-Golay")
plt.plot(x, y_gauss, "r--", linewidth=2, label="Gaussian")
plt.plot(x, y_clean, "k:", linewidth=1, label="True signal")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Signal Smoothing")
save_fig("signal_smoothing")


print(f"\nDone! Generated 7 figures in {OUTPUT_DIR}/")
