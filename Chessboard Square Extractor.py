import numpy as np

# Create the chessboard
chessboard = np.zeros((8, 8), dtype=int)
chessboard[1::2, 0::2] = 1
chessboard[0::2, 1::2] = 1

# Take row number(0-7) as input
a = int(input())

# Take column number(0-7) as input
b = int(input())


# Extract the 3x3 subgrid
row_start = max(0, a - 1)
row_end = min(8, a + 2)
col_start = max(0, b - 1)
col_end = min(8 , b + 2)
subgrid = chessboard[row_start:row_end, col_start:col_end]


# Print the result
print(subgrid)
