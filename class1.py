import numpy as np

list1 = [1,2,3,4,5]
#print(list1)
#print(list1[0])

list2 = ["John Elder", 41, list1, True]
#print(list2)

# Numpy - Nu meric Python
# ndarray = n-dimensional array

np1 = np.array([0,1,2,3,4,5,6,7,8,9])
np1 = np.array([0,1,2,3,4,5,6,7,8,9],np.int32)
print(np1)
print(np1.shape) 
print(np1.dtype) 
# Array Shape: (10,) — It's a one-dimensional array with 10 elements.
# np.shape gives dimensions of array and np.size gives size of array and np.itemsize gives size of items/elements in array
# array.size and np.size(array) are same
# arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
# arr.shape  # Output: (2, 3)
# arr.size  # Output: 6 (NOT 2) - it multiplies the dimensions in shape
# len(arr)  # Output: 2 - returns the size of the first dimension/axis of the array (the number of rows in a 2D array).

# Range - last is excluded
np2 = np.arange(10)
print(np2)

# Step
np3 = np.arange(0,10, 2)
print(np3)

# Zeros - default is float
# np4_int = np.zeros(10, dtype=int)  # Array of integers
np4 = np.zeros(10)
print(np4)
# np4 = np.zeros((10)) - same output but functioning check kar lena
# np4 = np.zeros((10,)) - is more explicit and consistent with multi-dimensional arrays.


# Multidimensional zeros
np5 = np.zeros((2,10))
print(np5)

# Full
np6 = np.full((10), 6)
print(np6)

# Multidimensional Full
np7 = np.full((2,10), 6)
print(np7)

# Convert Python lists to np
my_list = [1,2,3,4,5]
np8 = np.array(my_list)
print(np8)

print(np8[0])

np.array({34,23,23})
# array will only be 34,23 - A set in Python removes duplicates, so when passing a set to np.array(), any repeated elements are eliminated.

arr = np.empty((2, 3))
# If you want a 1D array, for example, pass an integer. For 2D, pass a tuple of two integers (rows, columns).
# np.empty() will contain whatever values were already present in that memory location, so the contents are essentially random or "uninitialized."

# np.empty_like is a function in NumPy that creates a new array with the same shape and data type as an existing array, but with uninitialized (random or "garbage") values.
b = np.empty_like(a)
