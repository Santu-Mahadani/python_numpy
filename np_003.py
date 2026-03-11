# Boolean Indexing -
import numpy as np
arr_bool=np.array([5,10,15,20,25])
print("Original Array :",arr_bool) # Original Array : [ 5 10 15 20 25]
bool_result=arr_bool>15
print("Result Array :",bool_result) # Result Array : [False False False  True  True]
print("Filtered Elements :",arr_bool[bool_result]) # Filtered Elements : [20 25]
print("Even numbers:",arr_bool[arr_bool%2==0]) # Even numbers: [10 20]