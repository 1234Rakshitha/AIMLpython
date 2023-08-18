import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
#creating 2D array
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

#Reshaping 1D to 2D
import numpy as np
arr = np.array([[1, 2,10],[19,3,12]])
newarr = arr.reshape(3,2)
print(newarr)
print("no of dimensions:",arr.ndim)
print("array is of type:",arr.dtype)
print("size os array",arr.size)

import numpy as np
arr=np.array([[1,2,3],[4,5,6]],dtype='float')
print("\narry created using passed list:\n",arr)

arr2=np.array((4,6,7))
print("\n narry created using passed tuple",arr2)

arr3=np.zeros(4,6)
print(arr3)

arr=np.full((2,5),dtype='float')
print("\narry created using passed list:\n",arr)


