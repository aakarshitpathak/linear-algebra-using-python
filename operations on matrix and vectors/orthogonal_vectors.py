'''If the inner product of two non-zero vectors v1 and v2 
is zero'''

# importing required libraries (numpy as np)
import numpy as np
#Creating vectors
Vector_1 = np.array([[3],[-1],[2]])
Vector_2 = np.array([[2],[4],[-1]])
print("Vector 1\n",Vector_1)
print("Vector 2\n",Vector_2)
#Finding the transpose of Vector_1 
trans = np.transpose(Vector_1)
#Finding the dot product 
result = np.dot(trans,Vector_2)
print("Dot Product\n",result)
