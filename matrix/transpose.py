''' NumPy library has a function transpose() which is used to 
obtain the transpose of a given matrix '''

# importing required libraries (numpy as np)
import numpy as np
# Creating a 3x2 Matrix "A"
A = np.array([[2,-2],[3,1],[1,4]])
print("Matrix A:\n",A)
# Finding transpose of a matrix using the function transpose()
print("Matrix A Transpose: \n",np.transpose(A))
