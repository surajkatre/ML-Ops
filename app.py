import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
Fs = 500  # Sampling frequency (samples per second)
T = 1 / Fs  # Sampling interval (time between samples)
L = 1000  # Length of the signal (number of samples)
t = np.arange(0, L) * T  # Time vector

# Generate a signal composed of two sinusoids
f1 = 50  # Frequency of the first sine wave (50 Hz)
f2 = 120  # Frequency of the second sine wave (120 Hz)

# Create the signal: a sum of two sine waves with noise
signal = 0.7 * np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
noise = 0.5 * np.random.randn(L)
signal_noisy = signal + noise

# Plot the time-domain signal
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal_noisy)
plt.title('Time Domain Signal with Noise')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Compute the FFT
signal_fft = np.fft.fft(signal_noisy)
signal_fft = signal_fft[:L // 2]  # Keep only positive frequencies

# Frequency axis
frequencies = np.fft.fftfreq(L, T)[:L // 2]

# Compute magnitude of FFT
magnitude = np.abs(signal_fft) / L

# Plot the frequency domain signal (FFT)
plt.subplot(2, 1, 2)
plt.plot(frequencies, magnitude)
plt.title('Frequency Domain (FFT)')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.grid(True)
plt.tight_layout()

plt.show()
