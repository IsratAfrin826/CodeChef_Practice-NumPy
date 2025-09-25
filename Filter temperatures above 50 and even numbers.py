import numpy as np

# Get temperature data from user input
temperatures = input().split()
temperatures = [int(score) for score in temperatures]
temp_array = np.array(temperatures)

filtered_temps = temp_array[(temp_array > 50) & (temp_array % 2 == 0)]

print(filtered_temps)
