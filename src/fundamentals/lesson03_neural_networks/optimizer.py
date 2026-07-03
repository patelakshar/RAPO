import torch
import torch.nn as nn
import torch.optim as optim

model = nn.Linear(1, 1)

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

x = torch.tensor([[1.0]])
y = torch.tensor([[2.0]])

prediction = model(x)
loss = criterion(prediction, y)

print("Initial Prediction:")
print(prediction)

print("\nInitial Loss:")
print(loss)

optimizer.zero_grad()
loss.backward()
optimizer.step()

new_prediction = model(x)
new_loss = criterion(new_prediction, y)

print("\nNew Prediction:")
print(new_prediction)

print("\nNew Loss:")
print(new_loss)
