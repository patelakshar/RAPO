import torch

x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(3.0, requires_grad=True)

z = x * y + y

print("x:", x)
print("y:", y)
print("z:", z)

z.backward()

print("\nGradient of x:")
print(x.grad)

print("\nGradient of y:")
print(y.grad)
