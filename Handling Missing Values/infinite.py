# np.isinf(array_name) -> handle infinite values. that check any value is infinite or not if present then return bool value

import numpy as np
arr = np.array([1, 2, np.nan, 4, -np.nan])
print(np.isinf(arr))
print(np.nan_to_num(arr, posinf=100, neginf=-100))

arr1 = np.array([1,2,3,4,5])
print(arr1.sum())