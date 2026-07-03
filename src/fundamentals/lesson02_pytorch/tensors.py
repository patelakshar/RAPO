import torch

tensor = torch.tensor([
    [1, 2, 3],
    [4, 5, 6]
])

print(tensor)
print(tensor.dtype)
print(tensor.shape)
print(tensor.ndim)
print(tensor[0][1].item())
