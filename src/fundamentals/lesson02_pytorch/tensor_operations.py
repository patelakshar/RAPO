import torch

a = torch.tensor([
    [1, 2],
    [3, 4]
])

b = torch.tensor([
    [5, 6],
    [7, 8]
])

print("Tensor A:")
print(a)

print("\nTensor B:")
print(b)

print("\nAddition:")
print(a + b)

print("\nSubtraction:")
print(a - b)

print("\nElement-wise Multiplication:")
print(a * b)

print("\nMatrix Multiplication:")
print(a @ b)
