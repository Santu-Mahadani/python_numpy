# Split the Array -
import numpy as np
my_arr=np.array([10,20,30,40,50,60])
split_arr=np.split(my_arr,3)
print("Splitted Array :\n",split_arr)
'''
Splitted Array :
 [array([10, 20]), array([30, 40]), array([50, 60])]
'''
# 1 array from the splitted array -
print("Array from Splitted Array :\n",np.array(split_arr))
'''
Array from Splitted Array :
 [[10 20]
 [30 40]
 [50 60]]
'''