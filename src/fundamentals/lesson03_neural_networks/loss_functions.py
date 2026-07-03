import torch
import torch.nn as nn

predictions = torch.tensor([
    3.0,
    -0.5,
    2.0,
    7.0
])

targets = torch.tensor([
    3.0,
    -0.5,
    2.0,
    7.0
])

mse = nn.MSELoss()

loss = mse(predictions, targets)

print("Predictions:")
print(predictions)

print("\nTargets:")
print(targets)

print("\nMean Squared Error:")
print(loss)
