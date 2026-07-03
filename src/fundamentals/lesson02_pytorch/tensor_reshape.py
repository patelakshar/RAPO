import torch

tensor = torch.arange(1, 13)

print("Original:")
print(tensor)
print("Shape:", tensor.shape)

matrix = tensor.reshape(3, 4)

print("\nReshaped (3x4):")
print(matrix)
print("Shape:", matrix.shape)

flattened = matrix.flatten()

print("\nFlattened:")
print(flattened)
print("Shape:", flattened.shape)

transposed = matrix.T

print("\nTransposed:")
print(transposed)
print("Shape:", transposed.shape)

unsqueezed = tensor.unsqueeze(0)

print("\nUnsqueezed:")
print(unsqueezed)
print("Shape:", unsqueezed.shape)

squeezed = unsqueezed.squeeze()

print("\nSqueezed:")
print(squeezed)
print("Shape:", squeezed.shape)
