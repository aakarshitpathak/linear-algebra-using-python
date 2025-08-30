import numpy as np

C = np.array([[2,0,0],
              [0,5,0],
              [0,0,9]])
print("C:\n ",C)

# Finding transpose of matrix
tra = np.transpose(C)
print("Tranpose of matrix C:\n",tra)
#Checking if all the elements in the matrix com is true
com =(C == tra) 
eql= com.all()
print(eql)