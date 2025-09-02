# importing required libraries (numpy as np)
import numpy as np
#Defining a matrix 'A' and scalar 's'
A = np.array([[1,2,1],
                     [-1,1,0],
                     [2,-1,1]])
print("Matrix:\n",A)
s = 2.5
print("Scalar :",s)
#Multiplication of Matrix by a Scalar
matrix_mul =  s * A
print("Multiplication of Matrix by a Scalar:\n",matrix_mul)
