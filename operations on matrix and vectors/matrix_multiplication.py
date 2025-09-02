# importing required libraries (numpy as np)
import numpy as np
# Creating Matrices
A = np.array([[1, 4, 7], 
            [2, 5, 8], 
            [3, 6, 9]])
B = np.array([[4, 2, 3],
            [2, 0, 7],
            [1, 3, 0]])
print("A :\n", A)
print("B :\n", B)
# Multiplying A and B
result=np.matmul(A,B)
print("Matrix Multiplication: A.B :\n",result)
