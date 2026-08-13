import numpy as np

arr = np.array(range(1,50,5))
print("Array: ",arr)

print("Mathematical functions on an array are: ")
print("Addition of 1.5: ", arr+1.5)
print("Subtraction of 2: ", arr-2)
print("Multiplication of 3: ", arr*3)
print("Floor Divition of 3: ", arr//3)

print("Statistical Functions on an array are: ")
# Mean
print(f"Mean of an array: {arr.mean()}")
# Median
print(f"Median of an array: {np.median(arr)}")
# Minimum
print(f"Minimum of an array: {arr.min()}")
# Maximum
print(f"Maximum of an array: {arr.max()}")
# Standard Deviation
print(f"Mean of an array: {arr.std()}")
# Sum
print(f"Mean of an array: {arr.sum()}")
