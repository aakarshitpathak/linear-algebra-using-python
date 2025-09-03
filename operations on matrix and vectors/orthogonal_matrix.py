''' Orthogonal Matrix
Consider matrix A of dimension (n, n) where, A is called 
an Orthogonal matrix if,

A.AT=AT.A=In

where, In is the Identity matrix.

For an orthogonal matrix A,

A^(-1)=A^(T) '''

# Importing required libraries (numpy as np)
import numpy as np
# Creating Matrix
A = np.array([[1.0,0.0],
                [0.0,1.0]])
print("A:\n", A)
#Checking for A.AT=AT.A
comparison_1 = np.dot(A.transpose(),A) == np.dot(A,A.transpose())
print(comparison_1)
#Checking for A.AT=Identity Matrix
comparison_2 =  np.dot(A.transpose(),A)== np.eye(2)
print(comparison_2)
# Comparing both the comparison done earlier
comparison_3 = comparison_1 == comparison_2
#Checking if all elements of matrix comparision are true.
equal_arrays = comparison_3.all()
print("A it an orthogonal matrix: ",equal_arrays)
