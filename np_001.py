# Numpy - Numerical Python

import numpy as np

# 1D Array -
my_array=np.array([20,30,40,50],int)
print(my_array) # [20 30 40 50]
print(type(my_array)) # <class 'numpy.ndarray'>

# 2D Array -
arr_2d=np.array([[10,20,30],
                 [40,50,60],
                 [70,80,90]])
print(arr_2d)
print(arr_2d.ndim) # 2
print(arr_2d.shape) # (3, 3) * 3 rows, 3 columns

# Zeros Array -
zeros_array=np.zeros((2,3),int)
print(zeros_array)
print("Dimension :-",zeros_array.ndim) # Dimension :- 2

# 3D Array -
arr_3d=np.array([[[10,20,30],[40,50,60]],[[70,80,90],[100,200,300]]])
print(arr_3d)
print(arr_3d.ndim) # 3
print(arr_3d.shape) # (2, 2, 3) * 2 pages, 2 rows, 3 columns

# Range Array -
range_array=np.arange(0,10,2) # Start=0, Stop=10, Step=2
print(range_array) # [0 2 4 6 8]

# Linear Space - Array with evenly spaced values.
linspace_array=np.linspace(0,1,5)
print(linspace_array) # [0.   0.25 0.5  0.75 1.  ]

# Random -
# Random values from uniform distribution (0,1) -
rand_uniform=np.random.rand(2,3) # 2 means 2 rows and 3 means 3 columns
print(rand_uniform)
'''
[[0.09243137 0.98426889 0.21882525]
 [0.84903559 0.52335171 0.99999513]]
'''
# This directly gives random values between 10 and 15 in a (2,3) array -
rand_uniform = np.random.uniform(10,15,(2,3))
print(rand_uniform)
'''
[[10.34633812 14.88814287 13.16898269]
 [14.27534655 10.90327409 14.61136575]]
'''