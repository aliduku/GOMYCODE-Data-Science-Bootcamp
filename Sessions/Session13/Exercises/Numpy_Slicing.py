import numpy as np
array_1D = np.array([10,11,12,13, 14])
array_2D = np.array([[20,30,40,50,60], [43,54,65,76,87], [11,22,33,44,55]])
array_3D = np.array([[[1,2,3,4,5], [11,21,31,41,51]], [[11,12,13,14,15], [51,52,53,54,5]]])

# Slice the first column of the 2-D array
print(array_2D[:,0])

# Slice the last two columns of the 2-nd row of the 2-D array
print(array_2D[1,-2:])

# Slice the 2-nd row of the 2-D array excluding the last two columns
print(array_2D[1,:-2])