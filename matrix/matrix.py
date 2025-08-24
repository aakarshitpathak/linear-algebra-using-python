# A matrix is defined as a rectangular array of numbers
''' The number of rows (m) and columns (n) is defined as the
dimension or order of the matrix and is represented as 
(m, n) '''

''' A matrix is called a square matrix if the number of
rows(m) is equal to the number of columns(n).'''

# importing required libraries (numpy as np)
import numpy as np
# Creating matrices of various dimension using np.array() function
matrix_2x2 = np.array([[1, 2], 
                       [3, 4]])
matrix_3x3 = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [8, 9, 10]])
print("2x2 Matrix\n",matrix_2x2,"\nshape of matrix -> ",matrix_2x2.shape)
print("\n3x3 Matrix\n",matrix_3x3,"\nshape of matrix -> ",matrix_3x3.shape)
