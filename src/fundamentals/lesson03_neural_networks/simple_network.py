import torch
import torch.nn as nn

class SimpleNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.layer1 = nn.Linear(2, 4)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(4, 1)

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        return x


model = SimpleNetwork()

sample = torch.tensor([[5.0, 10.0]])

prediction = model(sample)

print("Network:")
print(model)

print("\nInput:")
print(sample)

print("\nPrediction:")
print(prediction)
