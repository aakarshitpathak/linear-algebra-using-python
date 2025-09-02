''' Matrix Inversion
Consider the matrices A and B of dimension (n, n). 
Let In be the identity matrix of order n.

If A * B = B * A = In, then B is called the inverse of A 
and is denoted as A-1.

AA-1 = A-1 A = In '''

# Importing required libraries (numpy as np)
import numpy as np
# Creating Matrix A
A = np.array([[1, 2],
                   [4, 5]])
print("Matrix A:\n", A)
# Finding the inverse matrix using np.linalg.inv() function
Ainv = np.linalg.inv(A)
print('The inverse of A is:\n', Ainv)
print("Multiplication of A and Ainv is:\n", np.matmul(A, Ainv))
