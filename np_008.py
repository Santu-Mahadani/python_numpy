# Search,Sort and filter of numpy
import numpy as np
new_arr=np.array([10,20,30,40,50,60])
# Search for elements equal to  30
indices=np.where(new_arr==30)
print("Index of 30:",indices) # Index of 30: (array([2]),)
# Search for elements greater than 30
greater_30=np.where(new_arr>30)
print("Indices where arr>30 :",greater_30) # Indices where arr>30 : (array([3, 4, 5]),)

# Sorting -
my_arr=np.array([5,6,10,20,8,12])
print("Array:",my_arr) # Array: [ 5  6 10 20  8 12]
# Sort the array in ascending order
sorted_arr=np.sort(my_arr)
print("Sorted Array:",sorted_arr) # Sorted Array: [ 5  6  8 10 12 20]
# Sort the array in descending order
sort_desc=np.sort(my_arr)[::-1]
print("Sorted Array(Descending):",sort_desc) # Sorted Array(Descending): [20 12 10  8  6  5]

# Filter in numpy
my_arr=np.array([5,10,15,20,25,30])
# Filter elements which are greater than 15
new_arr=my_arr[my_arr>15]
print("Filtered elements:",new_arr) # Filtered elements: [20 25 30]
# Filter Even numbers from the array
even_arr=my_arr[my_arr%2==0]
print("Even elements:",even_arr) # Even elements: [10 20 30]