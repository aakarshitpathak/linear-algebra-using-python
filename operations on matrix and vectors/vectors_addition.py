# The function add() of the NumPy library, is used to add vectors. 
# Vector addition is illustrated below: 

# importing required libraries (numpy as np)
import numpy as np
#Create 2 vectors
vector_1 = np.array([[2, -1, 1]]) 
vector_2 = np.array([[1, 2, -1]]) 
   
print ("1st  Vector :  ", vector_1)  
print ("2nd  Vector :  ", vector_2)  
# Addition of the vectors using the function np.add()
out = np.add(vector_1, vector_2)  
print ("Added Vector : ", out)
