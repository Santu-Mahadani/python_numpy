# Numpy - Numerical Python
import numpy as np
my_array=np.array([10,20,30,40],int)
print(my_array) # [10 20 30 40]
print(type(my_array)) # <class 'numpy.ndarray'>
print(my_array.ndim) # 1
print(my_array.dtype) # int64
print(my_array.shape) # (4,)
arr_2d=np.array([[10,20,30],[40,50,60]])
print(arr_2d)
'''
[[10 20 30]
 [40 50 60]]
'''
print(arr_2d.ndim) # 2
print(arr_2d.shape) # (2,3)