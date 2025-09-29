import numpy as np


def create_3d_ones(depth, rows, columns):
    return np.ones((depth, rows, columns), dtype=int)


# Take depth, rows, and columns as input
d, r, c = map(int, input().split())

# Test the function
result = create_3d_ones(d, r, c)

print(result)
