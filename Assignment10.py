import numpy as np

# 1)Replace nan with 0 and interchange 3 rows and 3 columns of 2D array [[6,-8,73,-110],[np.nan,-8,0,94]]
arr_2d = np.array([
    [6,-8,73,-110]
    ,[np.nan,-8,0,94]
])
print("Original Array: \n",arr_2d,'\n')
# After replacing nan with 0
res = np.nan_to_num(arr_2d, copy=True,nan=0.0)
print("After replacing nan values: \n",res,'\n')
# Since shape of matrix is (2,4) so 3 rows and 3 columns can not get interchanged

# New 2d array with 4x4 matrix
arr_2d = np.array([
    [1,    2,  np.nan, 4],
    [5,    np.nan, 7,  8],
    [9,   10, 11, 12],
    [13, 14, 15, 16]
])
print("Original Array:\n", arr_2d, "\n")
arr_no_nan = np.nan_to_num(arr_2d, copy=True, nan=0.0)
print("After replacing NaN with 0:\n", arr_no_nan, "\n")
result = arr_no_nan.copy()
# Get the 3x3 submatrix
sub = result[:3, :3]
# Transpose the 3x3 part and replace it in the result
result[:3, :3] = sub.T
print("After swapping (transposing) top-left 3x3 block:\n", result)

# 2) Move axes of 3D array to new positions
arr_3d = np.arange(24).reshape(2, 3, 4)
print("Original Array Shape:", arr_3d.shape)
print("Original Array:\n", arr_3d,'\n')
# Moving axes by np.moveaxis() method
moved = np.moveaxis(arr_3d, source=0, destination=2)
print("After np.moveaxis(arr_3d, 0, 2): Shape =", moved.shape)      # axis 0 and 2 are moved
print("Array after np.moveaxis(): \n",moved,'\n')
# Moving axes by np.transpose()
transposed = np.transpose(arr_3d, (2, 0, 1))
print("After arr_3d.transpose(2, 0, 1): Shape =", transposed.shape)     # axis 0->2, 1->0, 2->1
print("After after np.transpose(): \n",transposed,'\n')

# 3)Replace nan values with average of columns
arr_2d = np.array([
    [1,    2,  np.nan, 4],
    [5,    np.nan, 7,  8],
    [9,   10, 11, 12],
    [13, 14, 15, 16]
])
print("Original Array:\n", arr_2d, "\n")
col_mean = np.nanmean(arr_2d, axis=0)
print("Mean of columns: ", col_mean)
indices = np.where(np.isnan(arr_2d))        #Finds indices of NaN values in the array.
print("Nan positions: ",indices)
arr_2d[indices] = np.take(col_mean, indices[1])     #Selects values from an array based on index positions.
print("Array after replacing Nan with col_mean:\n", arr_2d, '\n')
# indices[0] = row indices of NaNs → [0, 1]
# indices[1] = column indices of NaNs → [2, 1]

# 4) Replace negative value with zero in numpy array using replace
arr_2d = np.array([
    [6,-8,73,-110]
    ,[-9,-8,5,94]
])
print("Original Array:\n", arr_2d, '\n')
# replace method is not a np method , it is present in pandas, and it is valid for specific values(if the value is known)
arr_2d[arr_2d < 0] = 0
print("After replacing negative values with 0: \n", arr_2d, '\n')

# 5) Find average of numpy arrays
arr1 = np.array([3,4])
arr2 = np.array([1,0])
avg = (arr1 + arr2) / 2
print(f"Average of {arr1} and {arr2}: {avg}\n")

# 6) Calculate average mean, median and mode values of two numpy 2d arrays

arr1 = np.array([
    [1, 2, 3],
    [4, 2, 6]
])

arr2 = np.array([
    [7, 3, 9],
    [10, 11, 3]
])
combined = np.concatenate((arr1, arr2), axis=0)
flattened = combined.flatten()
mean_val = np.mean(flattened)
median_val = np.median(flattened)
unique, counts = np.unique(flattened, return_counts=True)
max_count_index = np.argmax(counts)
mode_val = unique[max_count_index]
print("Combined Array:\n", combined, '\n')
print("Flattened Array:", flattened, '\n')
print(f"Mean: {mean_val:.2f}")
print("Median:", median_val)
print("Mode:", mode_val)

# 7) Solve the following equation using linalg() and inverse() method
'''
x - 2y + 3z = 9
-x + 3y - z = -6
2x - 5y + 5z = 17
'''
A = np.array([
    [1,-2,3],
    [-1,3,-1],
    [2,-5,5]
])
B = np.array([9, -6, 17])
X = np.linalg.solve(A, B)
print("\nSolution x-2y+3z=9, -x+3y-z=-6, 2x-5y+5z=17 using np.linalg.solve():")
print("x =", X[0])
print("y =", X[1])
print("z =", X[2])

A_inv = np.linalg.inv(A)
X = np.dot(A_inv, B)
print("\nSolution x-2y+3z=9, -x+3y-z=-6, 2x-5y+5z=17 using matrix inverse:")
print("x =", X[0])
print("y =", X[1])
print("z =", X[2])

# 8) Plot graph to compare your at least 2 semester result
import matplotlib.pyplot as plt
Semester = ['Semester 1', 'Semester 2', 'Semester 3']
SGPA = [9.22, 9.85, 9.51]
plt.figure(figsize=(10, 5))
plt.bar(Semester, SGPA, color=['skyblue', 'orange', 'lightgreen'], width=0.4)
plt.title('SGPA Comparison (Sem 1 to Sem 3)', fontsize=20)
plt.xlabel('Semester', fontsize=15)
plt.ylabel('SGPA', fontsize=15)
plt.ylim(0, 12)  # SGPA scale is out of 10
plt.grid(linestyle='--', alpha=0.7, color='grey')
for i in range(len(SGPA)):
    plt.text(i, SGPA[i] + 0.1, f"{SGPA[i]:.2f}", ha='center', fontsize=14)

plt.show()