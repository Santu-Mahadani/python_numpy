# Stacking and Splitting -
import numpy as np
a=np.array([[10,20,30,40],[50,60,70,80]])
b=np.array([[100,200,300,400],[500,600,700,80]])
print("1st Array -\n",a)
print("2nd Array -\n",b)
# Horizontal Stacking - Side by side join
h_stacked=np.hstack((a,b))
print("Horizontally Stacked :\n",h_stacked)
'''
Horizontally Stacked :
 [[ 10  20  30  40 100 200 300 400]
 [ 50  60  70  80 500 600 700  80]]
'''

# Vertical Stacking - Top to bottom Join
v_stacked=np.vstack((a,b))
print("Vertically Stacked :\n",v_stacked)
'''
Vertically Stacked :
 [[ 10  20  30  40]
 [ 50  60  70  80]
 [100 200 300 400]
 [500 600 700  80]]
'''