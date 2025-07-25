"""
# this convert multi dimention array to 1D array
.ravel() -> views original array change
.flatten() -> original array not effected
"""

import numpy as np
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())