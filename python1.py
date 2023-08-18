import numpy as np

arr2 = np.array(([[1, 2, 3], [4, 5, 6]]))
print(arr2)

print("sum of axis",arr2.sum(axis=1))
print("sum of array",arr2.sum())

print("avg of array",np.average(arr2))

print("min of array",arr2.min())
print("max of array",arr2.max())

print("min axis of array",arr2.min(axis=1))
print("max axis of array",arr2.max(axis=1))

print("sum",arr2.cumsum())
print("\ntransprote\n",arr2.T)


import numpy as np

arr = np.array([1, 12, 3, 4, 5])
print(arr)
arr1 = np.array([23, 4, 9, 10, 6])
print(arr1)
print("\nadd 2 array\n",arr+arr1)
print("\nsum 2 array\n",arr-arr1)
print("\nmulti 2 array\n",arr*arr1)
print("\ndivi 2 array\n",arr/arr1)
print("\nmod 2 array\n",arr%arr1)
