import numpy as np

# numbers = np.array(range(11,110,10))
numbers = np.array((10,20,67,22,34,21,45,66,786, 1))
print(numbers)

print("Array shape:   ",numbers.shape)
print("Array size:    ", len(numbers))
print("Type of Array: ",type(numbers))


one_dim_arr = np.array([10, 20, 30, 40, 50])
two_dim_arr = np.array([[1,2,3,4,5], [22,33,44,55,89]])

print(f"## {one_dim_arr.ndim} dimensional array ##")
print(one_dim_arr)

print(f"## {two_dim_arr.ndim} dimensional array ##")
print(two_dim_arr)