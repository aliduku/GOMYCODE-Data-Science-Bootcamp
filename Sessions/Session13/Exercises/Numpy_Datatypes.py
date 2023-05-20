import numpy as np
array_1D = np.array([10,11,12,13, 14])
array_2D = np.array([[20,30,40,50,60], [43,54,65,76,87], [11,22,33,44,55]])
array_3D = np.array([[[1,2,3,4,5], [11,21,31,41,51]], [[11,12,13,14,15], [51,52,53,54,5]]])

array_1D = np.array(array_1D, dtype = np.str_)
print(array_1D)

array_2D = np.array(array_2D, dtype = np.complex64)
print(array_2D)

array_3D = np.array(array_3D, dtype = np.float64)
print(array_3D)