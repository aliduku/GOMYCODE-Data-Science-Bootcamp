import numpy as np
array_1D = np.array([10,11,12,13, 14])
array_2D = np.array([[20,30,40,50,60], [43,54,65,76,87], [11,22,33,44,55]])
array_3D = np.array([[[1,2,3,4,5], [11,21,31,41,51]], [[11,12,13,14,15], [51,52,53,54,5]]])

# Display the first element (not necessarily individual element) for each of the 3 arrays we defined above
print(array_1D[0])
print(array_2D[0])
print(array_3D[0])

# Call the first individual element of the each of the 3 arrays
print(array_1D[0])
print(array_2D[0, 0])
print(array_3D[0, 0, 0])

# Uses negative indices to display the last element of each array
print(array_1D[-1])
print(array_2D[-1])
print(array_3D[-1])