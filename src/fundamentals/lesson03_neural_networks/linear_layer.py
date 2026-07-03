import torch
import torch.nn as nn

# One neuron:
# Input Features = 3
# Output Features = 1

layer = nn.Linear(
    in_features=3,
    out_features=1
)

# Example input (1 sample with 3 features)
x = torch.tensor([[1.0, 2.0, 3.0]])

print("Input:")
print(x)

print("\nWeights:")
print(layer.weight)

print("\nBias:")
print(layer.bias)

output = layer(x)

print("\nOutput:")
print(output)
