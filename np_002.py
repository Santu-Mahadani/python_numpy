# Numpy Basic Operations  -
import numpy as np
simple_array=np.array([[10,20,30],[40,50,60]])
print("Simple Array -> \n",simple_array)
print("Shape :",simple_array.shape) # Shape : (2, 3)
print("Size:",simple_array.size) # Size: 6 [Total number of elements]
print("Data Type:",simple_array.dtype) # Data Type: int64
print("Dimensions:",simple_array.ndim) # Dimensions: 2

# Indexing and Slicing -
# 1D Array -
arr_1d=np.array([10,20,30,40,50],int)
print("1D Array -> \n",arr_1d)
print(arr_1d[2]) # 30 (* Access the third element [index 2])
print(arr_1d[1:4]) # [20 30 40] (* Slice from index 1 to 3)
# 2D Array -
arr_2d=np.array([[10,20,30,12],[40,50,60,15],[100,200,300,205]])
print(arr_2d)
print("Array Indexing :",arr_2d[1,2]) # Array Indexing : 60 [* Access element at row 1,column 2]
print("Array Slicing :\n",arr_2d[0:2,1:3]) # Row Slicer, Column Slicer
'''
Array Slicing :
 [[20 30]
 [50 60]]
'''
# 3D Array -
arr_3d=np.array([[[1,2,3,4],[6,7,8,9]],[[10,11,12,13],[14,15,16,17]]])
print(arr_3d)
print("Shape :",arr_3d.shape) # Shape : (2, 2, 4) [* Page = 2, Row = 2, Column = 2]
print("3D Array Slicing -",arr_3d[1,1,2]) # 3D Array Slicing - 16 [Page,Row,Column]