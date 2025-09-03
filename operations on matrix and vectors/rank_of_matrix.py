# Importing required libraries (numpy as np)
import numpy as np
# Creating Matrices
A = np.array([[1,1.0],[3,3]])
print('The matrix A is:\n', A)
B = np.eye(4) 

''' eye()method is used to create identity matrix
with the number in it like here it is 4 so 4x4 identity matrix
will be formed '''

print('The matrix B is:\n', B)
# Finding the rank of matrix a using np.linalg.matrix_rank() function
print(" Rank of A is:",np.linalg.matrix_rank(A))
# Finding the rank of matrix b using np.linalg.matrix_rank() function
print(" Rank of B is:",np.linalg.matrix_rank(B))
