# Convert B to an lower triangular matrix C

import numpy as np

B=np.array([[2,3,4],
            [0,5,6],
            [0,0,9]])

# converting A to lower triangular matrix
lower = np.tril(B)
print("Lower Triangular Matrix\n",lower)