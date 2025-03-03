import torch
import torch.optim as optim
import torch.nn as nn
from model import DenoisingCNN
from dataset import generate_signal
import numpy as np

# Load dataset
t, clean_signal, noisy_signal = generate_signal()

# Convert to tensors
noisy_tensor = torch.tensor(noisy_signal, dtype=torch.float32).view(1, 1, -1)
clean_tensor = torch.tensor(clean_signal, dtype=torch.float32).view(1, 1, -1)

# Initialize model
model = DenoisingCNN()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
epochs = 100
for epoch in range(epochs):
    optimizer.zero_grad()
    output = model(noisy_tensor)
    loss = criterion(output, clean_tensor)
    loss.backward()
    optimizer.step()
    
    if epoch % 10 == 0:
        print(f"Epoch {epoch}/{epochs}, Loss: {loss.item()}")

# Save model
torch.save(model.state_dict(), "denoising_model.pth")
print("Model saved successfully.")
