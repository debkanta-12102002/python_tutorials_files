"""
np.insert(array,index,value,  asix)
asix -> none means 1D arrray
asix -> set 0 means row wise adda 
        & set 1 means coloumn wise data entry

"""

import numpy as np
arr = np.array([10,20,30,40,])
add_arr = np.insert(arr,4,50)
print(add_arr)



import numpy as np
arr_2d=np.array([[1,2,3],
                 [4,5,6]
                 ])
new_arr = np.insert(arr_2d, 1, [10,20,30], axis=0)
print(new_arr)