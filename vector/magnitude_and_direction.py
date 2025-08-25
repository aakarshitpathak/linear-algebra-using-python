'''Magnitude is the distance between the origin and 
the point representing the vector.'''

'''The direction is the path of displacement from the origin 
to the point which represents the vector.'''

'''The norm() function in NumPy helps in finding the magnitude of a vector.'''

# importing required libraries (numpy as np)
import numpy as np
#Create a vector
vector=np.array([3,3])
#Magnitude of vector can be found using function np.linalg.norm() function
print("\nMagnitude of the vector = ",np.linalg.norm(vector))
