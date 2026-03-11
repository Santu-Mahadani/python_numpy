# Depth Stacking -
import numpy as np
a=np.array([[1,2,3],
           [4,5,6]])
b=np.array([[10,20,30],
           [40,50,60]])
print(a)
print(b)

# d stack-
d_stack=np.dstack((a,b))
print("Depth Stack:\n",d_stack) # End result is a 3D Array where pages are connected in depth wise
'''
Depth Stack:
 [[[ 1 10]
  [ 2 20]
  [ 3 30]]

 [[ 4 40]
  [ 5 50]
  [ 6 60]]]
'''