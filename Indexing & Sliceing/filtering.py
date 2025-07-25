# "boolean masking" or filtering data with condition
# faster then loops 
import numpy as np

arr = np.array([10,20,30,40])
print(arr[arr>25]) # return those values are >25
