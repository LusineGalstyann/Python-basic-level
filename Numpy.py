import numpy as np

print(np.__version__)

arr=np.array([1,2,3,4])
arr1=np.array((5,6))
print(arr,type(arr),arr1, type(arr1))

#0-D arrays Scalars  just value
arr=np.array(42)
#1-D  which elemets are 0D arreys
arr=np.array([1,2,3,4])
#2D arrey which elemets are 1D arreys
arr= np.array([[1,2,3],[4,5,6]])
#3D
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])


# ndim attribute show  dimensions count (0,1,2...) ndmin: give
arr = np.array([1, 2, 3, 4], ndmin=5)
arr=np.array([1, 2, 3, 4])

#dtypes
arr = np.array([1, 2, 3, 4])
arr1=arr.astype('f')
print(arr1)
arr[0]=0
print(arr1)


#join

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=0)

print(arr)
#split
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)


arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)

#searching
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)


arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)
#sorting
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

#filners
arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = []

for element in arr:
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)