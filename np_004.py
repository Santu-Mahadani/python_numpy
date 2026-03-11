# Reshape,Flatten,Ravel -
import numpy as np
my_arr=np.arange(12)
print(my_arr) # [ 0  1  2  3  4  5  6  7  8  9 10 11]
reshape=my_arr.reshape(3,4)
print("Reshaped (3 X4 ) :\n",reshape)
'''
Reshaped (3 X4 ) :
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
# flatten() - Returns a copy of the array as 1D
flat=reshape.flatten()
print("Flattened Array :",flat) # Flattened Array : [ 0  1  2  3  4  5  6  7  8  9 10 11]

# ravel() - Returns a flattened view (if possible) of the array
ravel_arr=reshape.ravel()
print("Ravel Array :",ravel_arr) # Ravel Array : [ 0  1  2  3  4  5  6  7  8  9 10 11]

# Modify ravel array -
ravel_arr[0]=100
print("Modified Ravel Array :",ravel_arr) # Ravel Array : [ 0  1  2  3  4  5  6  7  8  9 10 11]
print("Original Array :\n",reshape)
'''
Original Array :
 [[100   1   2   3]
 [  4   5   6   7]
 [  8   9  10  11]] 
'''
# Modify flat array -
flat[1]=200
print("Modified Flat Array :",flat) # Modified Flat Array : [  0 200   2   3   4   5   6   7   8   9  10  11]
print("Original Array :\n",reshape)
'''
Original Array :
 [[100   1   2   3]
 [  4   5   6   7]
 [  8   9  10  11]]
'''
'''
Key Takeaways :
# flatten() creates a copy - original array is not affected by changes in the flattened array.
# ravel() creates a view (if possible) - modifying ravel array affects the original array.
'''