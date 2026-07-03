import torch
import torch.nn as nn

relu = nn.ReLU()
sigmoid = nn.Sigmoid()
tanh = nn.Tanh()

x = torch.tensor([-2.0, -1.0, 0.0, 1.0, 2.0])

print("Input:")
print(x)

print("\nReLU:")
print(relu(x))

print("\nSigmoid:")
print(sigmoid(x))

print("\nTanh:")
print(tanh(x))
