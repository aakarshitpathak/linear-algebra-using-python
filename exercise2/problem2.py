# Rank of A

import numpy as np
A = np.array([[3,-1,2],
                  [1,2,3],
                  [4,1,1]])
print("Rank of matrix A is : ", np.linalg.matrix_rank(A))