"""
Simple NumPy Learning Example
Author: Learning Demo

This script demonstrates:
1. Creating NumPy arrays
2. Basic arithmetic operations
3. Statistical calculations
4. Reshaping arrays
"""

import numpy as np   # Import NumPy library

# ==============================
# 1. Creating NumPy arrays
# ==============================

# Create an array from a Python list
data = np.array([10, 20, 30, 40, 50])
print("Original array:", data)


# ==============================
# 2. Arithmetic operations
# ==============================

# Add 5 to each element
add_result = data + 5
print("After adding 5:", add_result)

# Multiply each element by 2
multiply_result = data * 2
print("After multiplying by 2:", multiply_result)


# ==============================
# 3. Basic statistics
# ==============================

print("Mean:", np.mean(data))     # Average value
print("Max:", np.max(data))      # Largest value
print("Min:", np.min(data))      # Smallest value
print("Sum:", np.sum(data))      # Total sum


# ==============================
# 4. Reshaping arrays
# ==============================

# Change 1D array into 2 rows, 5 columns example
matrix = np.arange(10).reshape(2, 5)
print("Reshaped matrix:\n", matrix)