# Incompatable shapes

import numpy as np 
arr1 = np.array([[1,2,3],[4,5,6]]) # 2D array (2,3)
arr2 = np.array([10,20]) #1D array

new_arr = arr1.reshape(3,2) # 1st change 2D -> 1D then -> 2D 3 columns for match shape
result = new_arr + arr2
print(result)