import torch

# Input (1 sample, 3 features)
x = torch.tensor([[1.0, 2.0, 3.0]])

# Weight matrix (3 inputs -> 2 outputs)
weights = torch.tensor([
    [0.5, -0.2],
    [0.3,  0.8],
    [0.7,  0.1]
])

# Bias (1 value for each output neuron)
bias = torch.tensor([0.1, -0.1])

# Forward Pass
output = torch.matmul(x, weights) + bias

print("Input:")
print(x)

print("\nWeights:")
print(weights)

print("\nBias:")
print(bias)

print("\nOutput:")
print(output)
