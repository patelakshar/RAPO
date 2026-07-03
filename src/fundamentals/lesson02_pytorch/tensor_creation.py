import torch

print("Zeros:")
print(torch.zeros((2, 3)))

print("\nOnes:")
print(torch.ones((2, 3)))

print("\nRandom (0 to 1):")
print(torch.rand((2, 3)))

print("\nRandom Normal Distribution:")
print(torch.randn((2, 3)))

print("\nRange:")
print(torch.arange(0, 10))

print("\nLinear Space:")
print(torch.linspace(0, 1, 5))
