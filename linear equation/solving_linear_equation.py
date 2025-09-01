# import the library numpy 
import numpy as np
#Define the coefficient matrix
matrix_1 = np.array([[1, 3, -1],
              [2, 5, 4],
              [2, 3, -1]])
# Define the vector
matrix_2 = np.array([4,19,7])
# Find the solution for the system of equations using the solve() method
x= np.linalg.solve(matrix_1, matrix_2)
print("The value of x1 is: ",x[0])
print("The value of x2 is: ",x[1])
print("The value of x3 is: ",x[2])
