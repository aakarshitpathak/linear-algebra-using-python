'''The inner product is a way to multiply two vectors and 
the result of this multiplication is a scalar.'''

# importing required libraries (numpy as np)
import numpy as np
#Creating the vectors
vector_1 = np.array([1,2,3]) 
vector_2 = np.array([1,0,3]) 
print("Vector 1:\n",vector_1)
print("Vector 2:\n",vector_2)
# Finding inner product of vector of same dimensions using inner() function of the NumPy library.
inner_product_1 = np.inner(vector_1,vector_2)
print("Inner Product of Vector 1, Vector 2:\n",inner_product_1)
