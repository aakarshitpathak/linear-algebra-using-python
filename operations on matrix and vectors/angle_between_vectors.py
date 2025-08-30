#import the library numpy
import numpy as np
# Function to find angle between two vectors
def angle_between(vector_1, vector_2):
    dot_pr = vector_1.dot(vector_2)
    norms = np.linalg.norm(vector_1) * np.linalg.norm(vector_2)
 
    return np.rad2deg(np.arccos(dot_pr / norms))
# Create two vectors
vector_1 = np.array([3,-1,2])
vector_2 = np.array([2,4,-1]) 
print("v1 = ",vector_1,"\nv2 = ", vector_2)
#Find the angle between them by using the function angle_between()
print("Angle Between the vectors v1 and v2 in 'degree' is :",angle_between(vector_1, vector_2))
