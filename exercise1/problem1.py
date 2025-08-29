# Create a square matrix A of order 3. Solve the following:

# Convert A to an upper triangular matrix B

import numpy as np

A=np.array([[2,3,4],
            [4,5,6],
            [7,8,9]])

# converting A to upper triangular matrix
upper= np.triu(A)
print("Upper Triangular Matrix\n", upper)