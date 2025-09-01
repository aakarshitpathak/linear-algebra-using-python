# Symmetric Matrix:

'''A square matrix A of dimension (n, n) is symmetric, 
if A = AT i.e.  the matrix A is the same as its transpose.'''

# importing required libraries (numpy as np)
import numpy as np
#Creating matrix A
A = np.array([[2,3,1],
            [3,4,-1],
            [1,-1,1]])
print("A:\n" , A)
# Finding the Transpose of the matrix
transposed_matrix = A.transpose()
print("Transpose of A:\n" , transposed_matrix)
'''Comparing each element of both matrices 
(returns a matrix of boolean compared values) 
and saving it in a variable comparison'''
comparison = (A == transposed_matrix)
#Checking if all the elements in the matrix comparision is true
equal_arrays = comparison.all()
print(equal_arrays)
