import numpy as np

arr = np.array([33,23,66,182,90])

print(f"Access Specific element using indexing in an array: {arr[-1]}")
print(f"Extract a portion of the array using slicing: {arr[-1: -4: -1]}")

two_d_array = np.array([[1,2,3,4],[5,6,7,8]])
print(f"\nTwo dimensional array: {two_d_array}")
print("\nAccess specific rows and columns.")
print(f"Access 2nd element in 3rd row: {two_d_array[1,1]} ")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(f"Original Array: {arr}")
print(f"Dimension of an original array: {arr.ndim}")
print(f"Reshaped Array: {newarr}")
print(f"Dimension of an reshaped array: {newarr.ndim}")