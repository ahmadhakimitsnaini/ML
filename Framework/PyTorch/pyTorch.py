import torch
import torch.nn as nn

x = torch.tensor([[1.0], [2.0], [3.0]])


y = torch.tensor([[2.0], [4.0], [6.0]])


class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(1, 1) 

    def forward(self, x):
        return self.linear(x)



model = SimpleModel()


prediction = model(x)

print("--- Original Input ---")
print(x)

print("\n--- Model Prediction (Untrained) ---")
print(prediction)