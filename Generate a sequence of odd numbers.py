import numpy as np

start = int(input())
end = int(input())

# Create a NumPy array of odd numbers from start to end
odd_numbers = np.arange(start + (start % 2 == 0), end + 1, 2)

# Print array of odd numbers
print(odd_numbers)
