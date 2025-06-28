import numpy as np

# 1)Combine a 1D and 2D numpy array
arr_1d = np.arange(4)
arr_2d = np.arange(10,22).reshape(3,4)
print("1D Array: ",arr_1d)
print("2D Array: ",arr_2d)
res = np.concatenate((arr_1d.reshape(1,4), arr_2d), axis=0)
print("Combined 1D and 2D Array: \n",res)

# 2)Flatten a 2d NumPy array to 1d array
arr_2d = np.array([[10,20,30], [40,50,60], [70,80,90]])
print("2D Array: \n",arr_2d)
arr_1d = arr_2d.reshape(-1)
print("Flattening of 2D array to 1D array using .reshape(-1): ",arr_1d)
arr_1d = arr_2d.flatten()
print("Flattening of 1D array to 2D array using .flatten(): ",arr_1d)
arr_1d = arr_2d.ravel()
print("Flattening of 2D array to 1D array using .ravel(): ",arr_1d)

# 3)Reverse a numpy array
arr_1d = np.arange(10)
print("Original 1D Array: ",arr_1d)
print("1D Array after reversal: ", np.flip(arr_1d))

arr_2d = np.array([[1,2], [3,4], [5,6], [7,8]])
print("Original 2D Array: \n",arr_2d)
print("2D Array after reversal: \n", np.flip(arr_2d))
print("Row wise reversal of 2D array: \n", np.flip(arr_2d, axis=0))
print("Column wise reversal of 2D array: \n",np.flip(arr_2d, axis=1))

# 4) Practice operations like
arr_2d = np.array([[10,33,11],[44,23,10],[90,34,23],[80,45,28]])    #Common array for all the options of this question
print("Original 2D Array: \n",arr_2d)
# i)Get the maximum value from array
print("Maximum value in array: ", np.max(arr_2d))

# ii)Get the minimum value from array
print("Minimum value in array: ", np.min(arr_2d))

# iii)Find the number of rows and columns of the given array
rows, cols = arr_2d.shape
print("Rows:", rows, "\tColumns:", cols)

# iv)Select the elements from a given array(each element and specific element)

# Access each element using nested loops
print("\nEach element using nested loops:")
for row in arr_2d:
    for element in row:
        print(element, end=' ')
print()

# Access each element using np.nditer()
print("\nEach element using np.nditer():")
for x in np.nditer(arr_2d):
    print(x, end=' ')
print()

# Access a specific element (e.g., row 3, col 2)
print("\nElement at (2, 1):", arr_2d[2, 1])  # Output: 34

# Entire row (3rd row)
print("\nThird row:", arr_2d[2])

# Entire column (second column)
print("\nSecond column:", arr_2d[:, 1])

# Slice subarray (rows 1-2, columns 0-1)
print("\nSliced subarray (arr_2d[1:3, 0:2]):\n", arr_2d[1:3, 0:2])

# Boolean masking: elements greater than 30
print("\nElements greater than 30:", arr_2d[arr_2d > 30])

# Unique values in the array
print("\nUnique elements in the array:", np.unique(arr_2d))

# v) Find the sum of values in a 2D array using for loop
print("Array is: \n", arr_2d)
sum=0
for row in arr_2d:
    for element in row:
        sum += element
print("\nSum of all elements in the array:", sum)

# vi)Addition, Subtraction, Multiplication and Division of NumPy Arrays
arr1 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
arr2 = np.array([[7,8,9],
                 [10,11,12],
                 [13,14,15]])

print("Array1: \n", arr1, '\n')
print("Array2: \n", arr2, '\n')

print("Addition of arr1 and arr2: \n", arr1 + arr2)
print("Subtraction of arr1 and arr2: \n", arr1 - arr2)
print("Multiplication of arr1 and arr2: \n", arr1 * arr2)
print("Division of arr1 and arr2: \n", arr1 / arr2)
print("Floor division of arr1 and arr2: \n", arr1 // arr2)
print("Modulus of arr1 and arr2: \n", arr1 % arr2)