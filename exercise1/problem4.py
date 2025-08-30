# Check whether matrix C is a diagonal matrix

import numpy as np
C = np.array([[2,0,0],
              [0,5,0],
              [0,0,9]])

is_diagonal = np.array_equal(C, np.diag(np.diag(C)))
print("Is diagonal:", is_diagonal)