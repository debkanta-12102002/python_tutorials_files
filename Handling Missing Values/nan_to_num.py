# np.nan_to_num(array_name, value) -> this replace value default value is 0

import numpy as np
arr = np.array([1,2,np.nan,4,np.nan])
print(np.nan_to_num(arr,nan=100))