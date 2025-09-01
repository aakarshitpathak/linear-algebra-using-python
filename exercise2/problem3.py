# Inverse of A 

import numpy as np
A = np.array([[3,-1,2],
              [1,2,3],
              [4,1,1]])

print("Matrix A: ", A)
print("Inverse of matrix A: ", np.linalg.inv(A))