import torch
import torch.nn as nn

# ==========================================
# 1. CREATING DATA (TENSORS)
# ==========================================
# Tensors are the core data structure in PyTorch. 
# Think of them as Python lists or NumPy arrays that can run on a GPU.

# Input data (e.g., hours studied)
x = torch.tensor([[1.0], [2.0], [3.0]])

# Target data (e.g., test scores)
y = torch.tensor([[2.0], [4.0], [6.0]])


# ==========================================
# 2. DEFINING THE MODEL
# ==========================================
# All PyTorch models inherit from nn.Module
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        # A simple linear layer that applies a linear transformation: y = Wx + b
        # 1 input feature, 1 output feature
        self.linear = nn.Linear(1, 1) 

    def forward(self, x):
        # This defines how the data flows through the model
        return self.linear(x)


# ==========================================
# 3. RUNNING THE MODEL
# ==========================================
# Initialize the model
model = SimpleModel()

# Pass the input data through the model to get a prediction
# Note: Because the model hasn't been trained yet, the output will be random!
prediction = model(x)

print("--- Original Input ---")
print(x)

print("\n--- Model Prediction (Untrained) ---")
print(prediction)