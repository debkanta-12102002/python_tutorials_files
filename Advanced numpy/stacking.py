"""
It is use when two data sets needs to meerge 1D or 2D 
vartically
horizontally

np.vstack()->coloumn wise
np.hstack()->row wise
"""

import numpy as np
arr1=[1,2,3]
arr2=[4,5,6]

print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))