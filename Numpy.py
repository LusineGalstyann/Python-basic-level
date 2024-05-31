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