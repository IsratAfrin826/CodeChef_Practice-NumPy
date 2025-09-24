import numpy as np

# Get user input
input_string = input()
numbers = [int(x) for x in input_string.split()]

# Create a NumPy array
arr = np.array(numbers)

# Create a boolean mask for non-negative numbers
mask = arr >= 0

# Apply the mask to get only non-negative numbers
result = arr[mask]

# print the non-negative numbers
print( result)