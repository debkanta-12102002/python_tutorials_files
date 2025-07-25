"""
For 1D and 2D array both it can apply
np.add(array1,array2)
array1+array2
"""

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sum_array = a + b
#sum_array = np.add(a, b)
print(sum_array)


a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

sum_array = a + b
# or: sum_array = np.add(a, b)

print(sum_array)