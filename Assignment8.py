import numpy as np

'''
1) Create a numpy array with random values
(4 x 2) empty and a full numpy array
(3 x 5) array filled with all zeros
(4 x 3 x 2) array filled with all ones
'''

# NumPy Array with random values
arr_rand = np.random.rand(4,2)
print("NumPy array with random values: \n", arr_rand, '\n')

# (4 x 2) empty NumPy array
arr_empty = np.empty((4,2))
print("Empty array(uninitialized values): \n", arr_empty, '\n')

# (4 x 2) full numpy array
arr_full = np.full((4,2), 'star')
print("Full array filled with 'star' string: \n", arr_full, '\n')
# repr(arr_full) — Shows Quotes for Strings
''' Output with repr(arr_full)
    array([['star', 'star'],
       ['star', 'star'],
       ['star', 'star'],
       ['star', 'star']], dtype='<U4') 
'''

# (3 x 5) array filled with all zeros
arr_zeros = np.zeros((3,5))
print("Array filled with all zeros: \n", arr_zeros, '\n')
print(arr_zeros.shape)

# (4 x 3 x 2) array filled with all ones
arr_ones = np.ones((4,3,2))
print("Array filled with all ones: \n", arr_ones, '\n')
print(arr_ones.shape)


# 2) Write a NumPy program to create a 3x3 2D matrix with values ranging from 2 to 10(inclusive)
arr_2D = np.arange(2,11).reshape(3,3)
print("3 x 3 2D array with values ranging from 2 to 10: \n", arr_2D, '\n')
# reshape() is a method used to change the shape of an existing NumPy array without changing its data.

# 3) Write a NumPy program to create a null vector of size 10 and update the 6th value to 11
null_vector = np.zeros(10)
print("Array filled with all nulls: \n", null_vector, '\n')
null_vector[5] = 11
print("Array after updating the 6th value to 11: \n", null_vector, '\n')

# 4) Write a NumPy program to reverse the array
# Reversal of 2D array
arr_2d = np.arange(2,10).reshape(2,4)
print("Original 2D Array: \n", arr_2d, '\n')
print("Reverse 2D Array: \n", arr_2d[::-1, ::-1], '\n')
# Reverse rows only (flip vertically)
rows_reversed = arr_2d[::-1, :]
print("Rows reversed:\n", rows_reversed)
# Reverse columns only (flip horizontally)
cols_reversed = arr_2d[:, ::-1]
print("Columns reversed:\n", cols_reversed)

#np.flip() is another way to reverse arrays
#print(np.flip(arr_2d, axis=0))  # flip rows
#print(np.flip(arr_2d, axis=1))  # flip columns

# Reversal of 1D array
arr_1d = np.arange(1,10)
print("Original 1D Array: \n", arr_1d, '\n')
print("Reverse 1D Array: \n", arr_1d[::-1], '\n')

# 5) Write a NumPy program to convert an array to a floating type
arr = np.arange(1,10).astype(np.int32)
print("Original Array: \n", arr, '\n')
print("Original dtype: \n", arr.dtype, '\n')
arr = arr.astype(np.float32)        # Converts into a 32-bit float
print("Converted Array to float: \n", arr, '\n')
print("Converted Array's dtype: \n", arr.dtype, '\n')