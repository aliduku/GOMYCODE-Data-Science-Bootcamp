import numpy as np

# Empty arrays
array_1D = np.empty(10)
print(array_1D)
array_2D = np.empty((2,4))
print(array_2D)

# Zero arrays
array_1D = np.zeros(10)
print(array_1D)
array_2D = np.zeros((2,4))
print(array_2D)

# One arrays
array_1D = np.ones(10)
print(array_1D)
array_2D = np.ones((2,4))
print(array_2D)

# Two arrays
array_1D = np.full(10, fill_value = 2)
print(array_1D)
array_2D = np.full((2,4), fill_value = 2)
print(array_2D)