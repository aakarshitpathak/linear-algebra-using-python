# importing required libraries (numpy as np)
import numpy as np
# Creation of 2 matrices
matrix_1 = np.array([[10,20,30],
                     [-30,-40,-50]]) 
matrix_2 = np.array([[100,-200,300],
                     [30,50,70]]) 
   
print ("1st  Matrix : \n", matrix_1)  
print ("2nd  Matrix : \n", matrix_2)  
# Addition of the matrices using np.add() function
out = np.add(matrix_1, matrix_2)  
print ("Added Matrix : \n", out)
