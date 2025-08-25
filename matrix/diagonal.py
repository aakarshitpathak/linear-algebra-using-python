# importing required libraries (numpy as np)
import numpy as np
# Creating a diagonal matrix with diagonal elements as (1,3,2)
diagonal_matrix = np.diag((1,3,2))
print(diagonal_matrix)
# Creating a diagonal matrix with a range of values
matrix_range= np.diag(np.arange(1,6,2))
print(matrix_range)
