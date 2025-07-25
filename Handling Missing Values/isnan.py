# np.isnan(array_name)

import numpy as np
arr = np.array([1,2,np.nan,4,np.nan])
# We can not compare those nan-values we replace those values
print(np.isnan(arr))
