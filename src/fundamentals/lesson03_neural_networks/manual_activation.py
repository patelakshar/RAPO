import torch

# Input values
x = torch.tensor([
    -3.0,
    -1.0,
     0.0,
     2.0,
     5.0
])

print("Input:")
print(x)

# Manual ReLU
relu = torch.maximum(x, torch.tensor(0.0))

print("\nManual ReLU:")
print(relu)

# PyTorch ReLU
torch_relu = torch.relu(x)

print("\nPyTorch ReLU:")
print(torch_relu)

print("\nMatch:")
print(torch.equal(relu, torch_relu))

