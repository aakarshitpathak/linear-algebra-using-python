'''A triangular matrix can be either a lower triangular 
or an upper triangular matrix.

A lower triangular matrix is a square matrix in which all 
the elements above the main diagonal are zero.

An upper triangular matrix is a square matrix in which all 
the elements below the main diagonal are zero.'''

# importing required libraries (numpy as np)
import numpy as np
#Creating a lower triangular matrix
lower_triangular_matrix_1 = np.tril([[1,2,3],
                               [4,5,6],
                               [7,8,9]])
print("Lower triangular matrix\n",lower_triangular_matrix_1)

#Creating a Upper triangular matrix
upper_triangular_matrix_1 = np.triu([[1,2,3],
                               [4,5,6],
                               [7,8,9]])
print("Upper triangular matrix\n",upper_triangular_matrix_1)
