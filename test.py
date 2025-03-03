import torch
import matplotlib.pyplot as plt
from model import DenoisingCNN
from dataset import generate_signal

# Load model
model = DenoisingCNN()
model.load_state_dict(torch.load("denoising_model.pth"))
model.eval()

# Generate new noisy signal
t, clean_signal, noisy_signal = generate_signal()

# Convert to tensor
noisy_tensor = torch.tensor(noisy_signal, dtype=torch.float32).view(1, 1, -1)

# Denoise the signal
with torch.no_grad():
    denoised_signal = model(noisy_tensor).numpy().flatten()

# Plot results
plt.figure(figsize=(10, 4))
plt.plot(t, noisy_signal, label="Noisy Signal", alpha=0.6)
plt.plot(t, denoised_signal, label="Denoised Signal", linewidth=2)
plt.plot(t, clean_signal, label="Clean Signal", linestyle='dashed')
plt.legend()
plt.show()
