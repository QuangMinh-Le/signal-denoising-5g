import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

def generate_signal(fs=1000, freq=50, duration=1, noise_std=0.3):
    """Generate a noisy sine wave signal."""
    t = np.linspace(0, duration, fs)
    clean_signal = np.sin(2 * np.pi * freq * t)  # Sine wave
    noise = np.random.normal(0, noise_std, clean_signal.shape)
    noisy_signal = clean_signal + noise
    return t, clean_signal, noisy_signal

if __name__ == "__main__":
    t, clean_signal, noisy_signal = generate_signal()
    plt.figure(figsize=(10, 4))
    plt.plot(t, noisy_signal, label="Noisy Signal")
    plt.plot(t, clean_signal, label="Clean Signal", linestyle='dashed')
    plt.legend()
    plt.show()
