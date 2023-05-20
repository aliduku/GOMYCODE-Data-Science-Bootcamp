import numpy as np
array_1D = np.array([10,11,12,13, 14])
array_2D = np.array([[20,30,40,50,60], [43,54,65,76,87], [11,22,33,44,55]])
array_3D = np.array([[[1,2,3,4,5], [11,21,31,41,51]], [[11,12,13,14,15], [51,52,53,54,5]]])

# Add 2 to every element of the 3 arrays without overwriting their values.
print(array_1D)
print(array_1D + 2)

print(array_2D)
print(array_2D + 2)

print(array_3D)
print(array_3D + 2)

# Multiply the values of each array by 100 without overwriting their values.
print(array_1D)
print(array_1D * 100)

print(array_2D)
print(array_2D * 100)

print(array_3D)
print(array_3D * 100)